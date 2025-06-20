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
    
    df_filtered = df[columns_to_keep]

    # Get unique switch names
    switch_names = df_filtered['Switch Name'].unique()

    # Separate 'lcore' switches and sort them
    lcore_switches = sorted([name for name in switch_names if 'core' in name.lower()])
    
    # Get the rest of the switches and sort them alphabetically
    other_switches = sorted([name for name in switch_names if 'core' not in name.lower()])

    # Combine the lists with lcore switches first
    sorted_switch_names = lcore_switches + other_switches
    
    # Create the output filename
    original_filename = os.path.basename(input_csv_path)
    # remove original extension and add .xlsx
    output_filename = f"processed_{os.path.splitext(original_filename)[0]}.xlsx"
    output_filepath = os.path.join(output_dir, output_filename)

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

    print(f"Successfully processed data and saved it to {output_filepath}")

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