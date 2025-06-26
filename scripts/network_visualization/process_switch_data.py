import pandas as pd
import sys
import os

def process_switch_data(input_csv_path, output_dir):
    """
    Processes a CSV file with FortiSwitch port data, filters it,
    and saves the result as a structured Excel file with one table per switch.

    Args:
        input_csv_path (str): The path to the input CSV file.
        output_dir (str): The directory where the output Excel file will be saved.
    """
    try:
        df = pd.read_csv(input_csv_path)
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_csv_path}")
        return

    # Columns to keep for the final report
    columns_to_keep = [
        'Switch Name',
        'Port',
        'Native VLAN',
        'Negotiated Speed',
        'Bytes (Sent/Received)',
        'Packets (Sent/Received)',
        'Description'
    ]
    
    # Filter to only select columns that actually exist in the CSV
    existing_columns_to_keep = [col for col in columns_to_keep if col in df.columns]
    
    df_filtered = df[existing_columns_to_keep]

    # Get unique switch names
    switch_names = df_filtered['Switch Name'].unique()

    # Filter to only include distribution and core switches
    switch_names = [name for name in switch_names if 'dist' in name.lower() or 'core' in name.lower()]

    # Separate 'lcore' switches and sort them
    lcore_switches = sorted([name for name in switch_names if 'core' in name.lower()])
    
    # Get the rest of the switches and sort them alphabetically
    other_switches = sorted([name for name in switch_names if 'core' not in name.lower()])

    # Combine the lists with lcore switches first
    sorted_switch_names = lcore_switches + other_switches
    
    # Create the output filename
    original_filename = os.path.basename(input_csv_path)
    base_name_no_ext = os.path.splitext(original_filename)[0]
    # Create subfolder inside outputs named after raw file base
    output_subdir = os.path.join(output_dir, base_name_no_ext)
    if not os.path.exists(output_subdir):
        os.makedirs(output_subdir)

    # remove original extension and add .xlsx
    output_filename = f"processed_{base_name_no_ext}.xlsx"
    output_filepath = os.path.join(output_subdir, output_filename)

    with pd.ExcelWriter(output_filepath, engine='xlsxwriter') as writer:
        current_row = 0
        for switch_name in sorted_switch_names:
            # Write the switch name as a title for the table
            title_df = pd.DataFrame([switch_name])
            title_df.to_excel(writer, sheet_name='Switches', startrow=current_row, index=False, header=False)
            current_row += 2 # Add a little space after title

            # Get the data for the current switch
            switch_df = df_filtered[df_filtered['Switch Name'] == switch_name].copy()
            
            # We don't need the 'Switch Name' column inside the table itself
            switch_df.drop(columns=['Switch Name'], inplace=True)

            # Write the sub-table to Excel
            switch_df.to_excel(writer, sheet_name='Switches', startrow=current_row, index=False)
            
            # Update the current row for the next table
            current_row += len(switch_df) + 3 # Add 3 rows of space before the next table

    print(f"Successfully processed data and saved Excel report to {output_filepath}")

    # After writing Excel, also build visualization CSVs
    # Collect node and link information for visualization
    def normalize_switch_name(raw_name: str) -> str:
        """Return canonical switch identifier without serial number / trailing underscores."""
        if not isinstance(raw_name, str):
            return raw_name
        base = raw_name.split(' - ')[0].strip()
        return base.rstrip('_')

    def get_switch_type(raw_name: str) -> str:
        upper = raw_name.upper()
        if 'CORE' in upper or 'FIB' in upper:
            return 'core'
        if 'DIST' in upper:
            return 'dist'
        return 'other'

    import re
    def get_location_from_name(switch_name: str) -> str:
        """Return building letter grouping or Data Center"""
        if not isinstance(switch_name, str):
            return 'Unknown'
        upp = switch_name.upper()
        if 'CORE' in upp or 'FIB' in upp or upp.startswith('DC'):
            return 'Data Center'
        m = re.match(r'^([A-Z])', switch_name)
        if m:
            return f"Building {m.group(1)}"
        return 'Unknown'

    def parse_speed_gbps(speed_str: str) -> int:
        """Return connection speed in Gbps as integer (e.g., 10, 1)."""
        if not isinstance(speed_str, str):
            return 0
        low = speed_str.lower()
        if 'gbps' in low:
            try:
                num = float(low.split('gbps')[0].strip())
                return int(num)
            except ValueError:
                return 0
        if 'mbps' in low:
            try:
                num = float(low.split('mbps')[0].strip())
                # Convert Mbps to Gbps rounding if matches 1000
                return int(num / 1000)
            except ValueError:
                return 0
        return 0

    # Build nodes and links sets
    node_info = {}
    links = []

    for _, row in df.iterrows():
        raw_source = row['Switch Name']
        src_norm = normalize_switch_name(raw_source)
        # Register source node
        if src_norm not in node_info:
            node_info[src_norm] = {
                'id': src_norm,
                'label': src_norm,
                'type': get_switch_type(raw_source),
                'location': get_location_from_name(src_norm)
            }

        # Determine target switch from Native VLAN if present
        native_vlan = row.get('Native VLAN', '')
        target_norm = None
        if isinstance(native_vlan, str) and native_vlan.strip():
            m = re.match(r'^([^(]+)', native_vlan.strip())
            if m:
                raw_target = m.group(1).strip()
                target_norm = normalize_switch_name(raw_target)
                if target_norm not in node_info:
                    node_info[target_norm] = {
                        'id': target_norm,
                        'label': target_norm,
                        'type': get_switch_type(raw_target),
                        'location': get_location_from_name(target_norm)
                    }

        # If valid connection, store link
        if target_norm and src_norm != target_norm:
            speed_gbps = parse_speed_gbps(row.get('Negotiated Speed', ''))
            medium = 'Fiber' if speed_gbps >= 10 else 'Copper'
            links.append({
                'source': src_norm,
                'target': target_norm,
                'port': row.get('Port', 'N/A'),
                'speed_Gbps': speed_gbps,
                'medium': medium
            })

    # Convert to DataFrame and write CSVs
    nodes_df = pd.DataFrame(node_info.values())
    links_df = pd.DataFrame(links)

    vis_nodes_filename = f"nodes_for_vis_{base_name_no_ext}.csv"
    vis_links_filename = f"links_for_vis_{base_name_no_ext}.csv"

    nodes_df.to_csv(os.path.join(output_subdir, vis_nodes_filename), index=False)
    links_df.to_csv(os.path.join(output_subdir, vis_links_filename), index=False)

    print(f"✅ Visualization helper CSVs saved in {output_subdir}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python process_switch_data.py <path_to_input_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_directory = 'outputs'
    
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    process_switch_data(input_file, output_directory) 