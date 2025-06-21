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
        'rankdir': 'TB',
        'splines': 'ortho',
        'nodesep': '0.8',      # Reduced spacing
        'ranksep': '1.2',      # Reduced vertical spacing
        'concentrate': 'false',
        'bgcolor': '#FFFFFF',
        'fontname': 'Helvetica',
        'label': f'Campus Network Topology - Core & Distribution\\nGenerated on {pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")}',
        'fontsize': '16',      # Larger font for better readability
        'dpi': '600',          # Very high resolution for crisp text
        'size': '8.5,14',      # More portrait-oriented (narrower, taller)
        'ratio': 'compress',
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

    dot = graphviz.Digraph('NetworkTopology', **GRAPH_STYLE)

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
                    fill = NODE_COLORS.get('core')
                    dc_cluster.node(row['id'], label=row['label'], fillcolor=fill)

        # Add other 'Building L' switches to the 'Building L' cluster
        l_nodes = other_nodes[other_nodes['location'] == 'Building L']
        for _, row in l_nodes.iterrows():
            fill = NODE_COLORS.get(row['type'], NODE_COLORS['default'])
            l_cluster.node(row['id'], label=row['label'], fillcolor=fill)

    # --- Analyze connectivity to organize buildings intelligently ---
    other_locations = sorted([loc for loc in other_nodes['location'].unique() 
                             if loc not in ['Building L', 'Data Center', 'Unknown']])
    
    BUILDINGS_PER_ROW = 4  # More buildings per row can help with horizontal layout if needed
    for i in range(0, len(other_locations), BUILDINGS_PER_ROW):
        # Subgraph for the row to enforce rank=same
        with dot.subgraph() as row_sub:
            row_sub.attr(rank='same')
            chunk = other_locations[i:i+BUILDINGS_PER_ROW]
            for location in chunk:
                group = other_nodes[other_nodes['location'] == location]
                if group.empty:
                    continue
                cluster_name = f"cluster_{location.replace(' ', '_')}"
                # Add cluster to the main graph `dot`
                with dot.subgraph(name=cluster_name) as sub:
                    sub.attr(label=location, style='rounded', bgcolor='#F0F8FF', fontname='Helvetica-Bold')
                    for _, row in group.iterrows():
                        fill = NODE_COLORS.get(row['type'], NODE_COLORS['default'])
                        sub.node(row['id'], label=row['label'], fillcolor=fill)

    # --- Build EDGES as specified: ONE per LINK ---
    for _, link in filtered_links.iterrows():
        source_id = link['source']
        target_id = link['target']

        # Skip if for some reason a node doesn't exist in our filtered list
        if not (source_id in node_ids and target_id in node_ids):
            continue

        # Determine hierarchy for proper direction (Core -> Dist)
        source_node = filtered_nodes.loc[filtered_nodes['id'] == source_id].iloc[0]
        target_node = filtered_nodes.loc[filtered_nodes['id'] == target_id].iloc[0]

        # Always draw from higher-level to lower-level, or alphabetically
        if source_node['type'] == 'core' and target_node['type'] != 'core':
            source, target = source_id, target_id
        elif target_node['type'] == 'core' and source_node['type'] != 'core':
            source, target = target_id, source_id
            # The data source seems to have 'port' always on the non-core side.
            # Since we flipped, the labeled port is now on the target.
        else:
            # If same type (dist to dist), sort alphabetically
            source, target = sorted([source_id, target_id])

        # --- Get link style attributes ---
        speed_g = link['speed_Gbps'] if not pd.isna(link['speed_Gbps']) else 0
        medium = link['medium']
        penwidth = penwidth_from_speed(speed_g)
        style_attrs = EDGE_STYLES.get(medium, EDGE_STYLES['default']).copy() # Use copy to avoid modifying the original dict
        style_attrs['penwidth'] = penwidth # Override penwidth with dynamic value

        # --- Create the required detailed label ---
        # The spec requires source and dest port, but we only have one port from the source data.
        # We will label the port we have.
        port_label = link.get('port', 'N/A')
        speed_label = f"{int(speed_g)} Gbps" if speed_g > 0 else "N/A"
        
        # Determine which side the known port belongs to
        if source == source_id: # No flip
             edge_label = f"  {port_label} -> \n {speed_label}  "
        else: # Flipped
             edge_label = f"  -> {port_label}\n {speed_label}  "


        dot.edge(
            source,
            target,
            xlabel=edge_label,
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