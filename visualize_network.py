import pandas as pd
import graphviz
import sys
import os
import glob

# --- Configuration ---

# Style settings for the final diagram
GRAPH_STYLE = {
    'graph_attr': {
        'layout': 'dot',
        'rankdir': 'LR',       # Changed to Left-to-Right for horizontal layout
        'splines': 'polyline', # Use polyline for cleaner, more direct edges
        'nodesep': '1.0',      # Increased for more horizontal space between nodes
        'ranksep': '2.0',      # Increased for more vertical space between ranks
        'concentrate': 'false',
        'bgcolor': '#FFFFFF',
        'fontname': 'Helvetica',
        'label': f'Campus Network Topology - Core & Distribution\\nGenerated on {pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")}',
        'fontsize': '16',
        'dpi': '600',
        'size': '11.69,8.27', # A4 size in inches (landscape)
        'ratio': 'auto',       # Adjust ratio to fit page without distortion
        'overlap': 'false'     # Explicitly prevent node overlaps
    },
    'node_attr': {
        'shape': 'box',
        'style': 'rounded,filled', 
        'fontname': 'Helvetica-Bold', 
        'fontsize': '12',      # Larger font size
        'width': '1.2',        # Slightly smaller nodes
        'height': '0.6',
    },
    'edge_attr': {
        'fontname': 'Helvetica',
        'fontsize': '10',      # Larger edge font
        'arrowsize': '0.8',
    }
}

NODE_COLORS = {
    'core': '#FF6B6B',    # Bright Red for Core switches
    'dist': '#4ECDC4',    # Teal for Distribution switches  
    'default': '#FFE66D', # Yellow for others
}

CONNECTION_NODE_STYLE = {
    'shape': 'box',
    'style': 'filled',
    'fillcolor': '#F5F5F5', # Light grey for info box
    'fontname': 'Helvetica',
    'fontsize': '9',
    'width': '0.8',
    'height': '0.4'
}

EDGE_STYLES = {
    'Fiber': {'style': 'bold', 'color': '#FF6B35', 'penwidth': '2'},
    'Copper': {'style': 'solid', 'color': '#2E86AB', 'penwidth': '1.5'},
    'default': {'style': 'dashed', 'color': '#A8DADC', 'penwidth': '1'},
}

# ------------------------------------------------------------
# New helpers for nodes/links CSVs (Phase-2 refactor)
# ------------------------------------------------------------


def load_nodes_csv(nodes_path: str) -> pd.DataFrame:
    """Load nodes_for_vis_*.csv produced by process_switch_data.py"""
    try:
        nodes_df = pd.read_csv(nodes_path)
    except FileNotFoundError:
        print(f"Error: could not find nodes CSV at '{nodes_path}'")
        return None

    required_cols = {"id", "label", "type", "location"}
    if not required_cols.issubset(nodes_df.columns):
        print(f"Error: nodes CSV is missing required columns {required_cols}")
        return None
    return nodes_df


def load_links_csv(links_path: str) -> pd.DataFrame:
    """Load links_for_vis_*.csv produced by process_switch_data.py"""
    try:
        links_df = pd.read_csv(links_path)
    except FileNotFoundError:
        print(f"Error: could not find links CSV at '{links_path}'")
        return None

    required_cols = {"source", "target", "port", "speed_Gbps", "medium"}
    if not required_cols.issubset(links_df.columns):
        print(f"Error: links CSV is missing required columns {required_cols}")
        return None
    return links_df


def penwidth_from_speed(max_speed_g):
    """Return edge thickness based on Gbps integer."""
    if max_speed_g >= 100:
        return "5"
    if max_speed_g >= 40:
        return "4"
    if max_speed_g >= 10:
        return "3"
    if max_speed_g >= 1:
        return "2"
    return "1"


def create_mermaid_diagram(nodes_df: pd.DataFrame, links_df: pd.DataFrame, output_path: str):
    """Generates a Mermaid.js diagram definition from node and link data."""
    if nodes_df is None or links_df is None or nodes_df.empty:
        print("Cannot build Mermaid diagram – missing or empty dataframes.")
        return

    # --- Use the same filters as the main visualization ---
    filtered_nodes = nodes_df[nodes_df['type'].isin(['core', 'dist'])].copy()
    node_ids = set(filtered_nodes['id'])
    filtered_links = links_df[
        (links_df['source'].isin(node_ids)) & 
        (links_df['target'].isin(node_ids))
    ].copy()

    if filtered_nodes.empty:
        print("No core or distribution nodes found for Mermaid diagram.")
        return

    def sanitize_node_name(name):
        """Sanitize node names to avoid Mermaid parsing issues."""
        return (name
                .replace('--', '_')           # Replace double dashes
                .replace('-', '_')            # Replace single dashes  
                .replace(' ', '_')            # Replace spaces
                .replace('.', '_')            # Replace dots
                .replace('(', '_')            # Replace parentheses
                .replace(')', '_')
                .replace('[', '_')            # Replace brackets
                .replace(']', '_'))

    def sanitize_edge_label(label):
        """Sanitize edge labels to avoid parsing issues."""
        return label.replace('|', '-').replace('"', "'")

    # --- Build the Mermaid syntax string ---
    mmd_lines = ["graph LR", ""]
    style_lines = []  # Collect styles to add at the end

    # Group nodes by location to create the top-level subgraphs
    locations = sorted([loc for loc in filtered_nodes['location'].unique() if loc != 'Unknown'])

    for location in locations:
        safe_location = sanitize_node_name(location)
        mmd_lines.append(f'  subgraph {safe_location}["{location}"]')
        
        # Get all switches for the current location
        location_nodes = filtered_nodes[filtered_nodes['location'] == location]

        for _, switch_row in location_nodes.iterrows():
            switch_id = switch_row['id']
            switch_label = switch_row['label']
            safe_switch_id = sanitize_node_name(switch_id)
            
            # Define a subgraph for each switch
            mmd_lines.append(f'    subgraph {safe_switch_id}["{switch_label}"]')
            
            # Create an invisible anchor node for the switch itself to be a target
            anchor_id = f"{safe_switch_id}_anchor"
            mmd_lines.append(f'      {anchor_id}[" "]')
            
            # Collect style for this anchor (to be added at the end)
            style_lines.append(f'  style {anchor_id} fill:#fff,stroke:#fff,stroke-width:0')

            # Find all ports for this switch that are used in links
            ports = sorted(list(filtered_links[filtered_links['source'] == switch_id]['port'].unique()))
            for port in ports:
                # Define a node for each port
                safe_port = sanitize_node_name(port)
                port_node_id = f"{safe_switch_id}_{safe_port}"
                mmd_lines.append(f'      {port_node_id}["{port}"]')
            
            mmd_lines.append("    end") # End of switch subgraph
        mmd_lines.append("  end") # End of location subgraph
        mmd_lines.append("")

    # --- Add all the links between ports and switches ---
    mmd_lines.append("  %% --- Links ---")
    for _, link in filtered_links.iterrows():
        source_switch_id = link['source']
        target_switch_id = link['target']
        port_id = link['port']
        
        # Sanitized IDs
        safe_source_switch = sanitize_node_name(source_switch_id)
        safe_target_switch = sanitize_node_name(target_switch_id)
        safe_port = sanitize_node_name(port_id)
        
        source_port_node_id = f"{safe_source_switch}_{safe_port}"
        target_anchor_id = f"{safe_target_switch}_anchor"

        speed_g = link['speed_Gbps'] if not pd.isna(link['speed_Gbps']) else 0
        speed_label = f"{int(speed_g)}G" if speed_g > 0 else "N/A"
        medium = link['medium']

        # Sanitize the edge label
        edge_label = sanitize_edge_label(f"{speed_label} {medium}")
        
        # Mermaid link syntax: A -->|"text"| B
        mmd_lines.append(f"  {source_port_node_id} -->|{edge_label}| {target_anchor_id}")

    # --- Add all styles at the end (this is valid Mermaid syntax) ---
    if style_lines:
        mmd_lines.append("")
        mmd_lines.append("  %% --- Styles ---")
        mmd_lines.extend(style_lines)

    # --- Write the final string to a .mmd file ---
    mermaid_content = "\n".join(mmd_lines)
    output_filepath_mmd = f"{output_path}.mmd"
    try:
        with open(output_filepath_mmd, 'w') as f:
            f.write(mermaid_content)
        print(f"✅ Mermaid diagram definition saved to {output_filepath_mmd}")
    except Exception as e:
        print(f"Error writing Mermaid file: {e}")


def create_network_diagram_from_tables(nodes_df: pd.DataFrame, links_df: pd.DataFrame, output_path: str):
    """Render topology using explicit node/link tables with proper hierarchical building-based layout."""

    if nodes_df is None or links_df is None or nodes_df.empty:
        print("Cannot build diagram – missing or empty dataframes.")
        return

    # --- FILTER: Only keep core and distribution switches ---
    print(f"Original data: {len(nodes_df)} nodes and {len(links_df)} raw links")
    
    # Keep only core and distribution switches
    filtered_nodes = nodes_df[nodes_df['type'].isin(['core', 'dist'])].copy()
    
    # Filter links to only include connections between filtered nodes
    node_ids = set(filtered_nodes['id'])
    filtered_links = links_df[
        (links_df['source'].isin(node_ids)) & 
        (links_df['target'].isin(node_ids))
    ].copy()
    
    print(f"Filtered to: {len(filtered_nodes)} nodes and {len(filtered_links)} links (core + distribution only)")

    if filtered_nodes.empty:
        print("No core or distribution switches found after filtering.")
        return

    print(f"Building diagram from {len(filtered_nodes)} nodes and {len(filtered_links)} raw links …")

    # Pre-process links to find all unique ports for each switch
    ports_by_switch = {}
    for _, link in filtered_links.iterrows():
        # In our dataset, the 'port' is always on the 'source' of the link
        switch_id = link['source']
        port_id = link['port']
        if switch_id not in ports_by_switch:
            ports_by_switch[switch_id] = set()
        ports_by_switch[switch_id].add(port_id)

    dot = graphviz.Digraph('NetworkTopology', **GRAPH_STYLE)
    dot.attr('graph', compound='true')  # Needed for edges between clusters/nodes

    # --- Helper to create a cluster for a switch with its ports ---
    def create_switch_cluster(subgraph, switch_row):
        switch_id = switch_row['id']
        switch_label = switch_row['label']
        switch_type = switch_row['type']

        cluster_color = NODE_COLORS.get(switch_type, NODE_COLORS['default'])

        with subgraph.subgraph(name=f"cluster_{switch_id}") as c:
            c.attr(label=switch_label, style='rounded', bgcolor=cluster_color, fontname='Helvetica-Bold')
            # Add a central, invisible node to act as an anchor for targeting the switch
            c.node(switch_id, label="", shape='point', width='0.01', height='0.01')

            # Create nodes for each port inside the cluster
            if switch_id in ports_by_switch:
                # Use a ranked subgraph to lay out ports neatly
                with c.subgraph() as ports_sg:
                    ports_sg.attr(rank='same')
                    for port in sorted(list(ports_by_switch[switch_id])):
                        port_node_id = f"{switch_id}_{port.replace(' ', '_')}"
                        ports_sg.node(port_node_id, label=port, shape='box', style='filled', 
                                      fillcolor='white', height='0.3', width='0.6', fontsize='9')

    # --- Organize nodes by location and type ---
    cores = filtered_nodes[filtered_nodes['type'] == 'core']
    other_nodes = filtered_nodes[~filtered_nodes['type'].isin(['core'])]

    # --- Create Building L cluster first to contain the Data Center ---
    with dot.subgraph(name='cluster_Building_L') as l_cluster:
        l_cluster.attr(label='Building L', style='rounded', bgcolor='#F0F8FF', fontname='Helvetica-Bold')

        # --- Create Data Center cluster INSIDE Building L ---
        if not cores.empty:
            with l_cluster.subgraph(name='cluster_Data_Center') as dc_cluster:
                dc_cluster.attr(label='Data Center', style='rounded', bgcolor='#FFE0E0', fontname='Helvetica-Bold')
                for _, row in cores.iterrows():
                    create_switch_cluster(dc_cluster, row)

        # Add other 'Building L' switches to the 'Building L' cluster
        l_nodes = other_nodes[other_nodes['location'] == 'Building L']
        for _, row in l_nodes.iterrows():
            create_switch_cluster(l_cluster, row)

    # --- Analyze connectivity to organize buildings intelligently ---
    other_locations = sorted([loc for loc in other_nodes['location'].unique() 
                             if loc not in ['Building L', 'Data Center', 'Unknown']])
    
    BUILDINGS_PER_ROW = 4
    for i in range(0, len(other_locations), BUILDINGS_PER_ROW):
        with dot.subgraph() as row_sub:
            row_sub.attr(rank='same')
            chunk = other_locations[i:i+BUILDINGS_PER_ROW]
            for location in chunk:
                group = other_nodes[other_nodes['location'] == location]
                if group.empty:
                    continue
                cluster_name = f"cluster_{location.replace(' ', '_')}"
                with dot.subgraph(name=cluster_name) as sub:
                    sub.attr(label=location, style='rounded', bgcolor='#F0F8FF', fontname='Helvetica-Bold')
                    for _, row in group.iterrows():
                        create_switch_cluster(sub, row)

    # --- Build EDGES from port nodes to target switch clusters ---
    for _, link in filtered_links.iterrows():
        source_switch_id = link['source']
        target_switch_id = link['target']
        port_id = link['port']

        if not (source_switch_id in node_ids and target_switch_id in node_ids):
            continue

        source_port_node = f"{source_switch_id}_{port_id.replace(' ', '_')}"
        target_anchor_node = target_switch_id

        # --- Get link style attributes ---
        speed_g = link['speed_Gbps'] if not pd.isna(link['speed_Gbps']) else 0
        medium = link['medium']
        penwidth = penwidth_from_speed(speed_g)
        style_attrs = EDGE_STYLES.get(medium, EDGE_STYLES['default']).copy()
        style_attrs['penwidth'] = penwidth

        # --- Create the required detailed label ---
        speed_label = f"{int(speed_g)} Gbps" if speed_g > 0 else "N/A"
        edge_label = f" {speed_label} "
        
        # Draw edge from the specific port node to the anchor node of the target switch
        # Use lhead to make the arrow point to the cluster boundary
        dot.edge(
            source_port_node,
            target_anchor_node,
            xlabel=edge_label,
            lhead=f'cluster_{target_switch_id}',
            **style_attrs
        )

    # --- Simple legend ---
    with dot.subgraph(name='cluster_legend') as leg:
        leg.attr(label='Legend', style='rounded', fontsize='14', bgcolor='#F5F5F5')
        leg.node('legend_core', label='Core Switch', shape='box', style='filled', fillcolor=NODE_COLORS['core'], fontsize='12')
        leg.node('legend_dist', label='Distribution Switch', shape='box', style='filled', fillcolor=NODE_COLORS['dist'], fontsize='12')
        
        # Simple edge legend
        leg.node('lc1', shape='point', width='0.1', label='')
        leg.node('lc2', shape='point', width='0.1', label='')
        leg.edge('lc1', 'lc2', label='Fiber Link', color=EDGE_STYLES['Fiber']['color'], 
                penwidth='3', style=EDGE_STYLES['Fiber']['style'])

        leg.node('lc3', shape='point', width='0.1', label='')
        leg.node('lc4', shape='point', width='0.1', label='')
        leg.edge('lc3', 'lc4', label='Copper Link', color=EDGE_STYLES['Copper']['color'], 
                penwidth='1.5', style=EDGE_STYLES['Copper']['style'])

    # Render
    try:
        dot.render(output_path, format='png', view=False, cleanup=True)
        print(f"✅ Diagram saved to {output_path}.png")
        dot.render(output_path, format='svg', view=False, cleanup=True)
        print(f"✅ Diagram saved to {output_path}.svg")
    except Exception as e:
        print(f"Error rendering graph: {e}")

# ------------------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python visualize_network.py <path_to_processed_data_folder>")
        sys.exit(1)

    input_dir = sys.argv[1]
    if not os.path.isdir(input_dir):
        print(f"Error: Provided path is not a directory: {input_dir}")
        sys.exit(1)

    # Find nodes and links files in the directory
    nodes_files = glob.glob(os.path.join(input_dir, 'nodes_for_vis_*.csv'))
    links_files = glob.glob(os.path.join(input_dir, 'links_for_vis_*.csv'))

    if not nodes_files:
        print(f"Error: Could not find 'nodes_for_vis_*.csv' in '{input_dir}'")
        sys.exit(1)
    if not links_files:
        print(f"Error: Could not find 'links_for_vis_*.csv' in '{input_dir}'")
        sys.exit(1)

    nodes_csv_path = nodes_files[0]
    links_csv_path = links_files[0]
    
    # Create output path inside the same directory
    base_name = os.path.basename(input_dir)
    output_filepath = os.path.join(input_dir, f"network_topology_{base_name}")

    nodes_df = load_nodes_csv(nodes_csv_path)
    links_df = load_links_csv(links_csv_path)
    
    create_network_diagram_from_tables(nodes_df, links_df, output_filepath)
    create_mermaid_diagram(nodes_df, links_df, output_filepath) 