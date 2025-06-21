import pandas as pd
import graphviz
import sys
import os
import glob
from collections import defaultdict

# --- Enhanced Configuration for Better Layout ---

GRAPH_STYLE = {
    'graph_attr': {
        'layout': 'dot',
        'rankdir': 'TB',       # Top-to-Bottom for cleaner vertical hierarchy
        'splines': 'polyline', # Polyline for better edge label support
        'nodesep': '0.8',      # Optimal spacing between nodes
        'ranksep': '1.5',      # Good vertical spacing between layers
        'concentrate': 'false',
        'bgcolor': '#FAFAFA',  # Subtle background
        'fontname': 'Arial',
        'label': f'Campus Network Topology\\nGenerated on {pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")}',
        'fontsize': '20',
        'labelloc': 't',       # Label at top
        'dpi': '300',
        'size': '12,16',       # Portrait orientation for better vertical layout
        'ratio': 'auto',
        'overlap': 'false',
        'compound': 'true'
    },
    'node_attr': {
        'shape': 'box',
        'style': 'rounded,filled',
        'fontname': 'Arial-Bold',
        'fontsize': '11',
        'margin': '0.2,0.1',
        'penwidth': '2'
    },
    'edge_attr': {
        'fontname': 'Arial',
        'fontsize': '9',
        'arrowsize': '0.7',
        'penwidth': '1.5'
    }
}

# Enhanced color scheme
NODE_COLORS = {
    'core': {
        'fillcolor': '#E74C3C',  # Strong red for core
        'fontcolor': 'white'
    },
    'dist': {
        'fillcolor': '#3498DB',  # Blue for distribution
        'fontcolor': 'white'
    },
    'access': {
        'fillcolor': '#2ECC71',  # Green for access
        'fontcolor': 'white'
    },
    'default': {
        'fillcolor': '#95A5A6',  # Grey for others
        'fontcolor': 'white'
    }
}

# Enhanced edge styles based on speed and medium
def get_edge_style(speed_gbps, medium):
    """Return edge style based on speed and medium"""
    styles = {
        'color': '#34495E',  # Default dark grey
        'penwidth': '1',
        'style': 'solid'
    }
    
    # Color based on medium
    if medium == 'Fiber':
        styles['color'] = '#E67E22'  # Orange for fiber
    elif medium == 'Copper':
        styles['color'] = '#8E44AD'  # Purple for copper
    
    # Width based on speed
    if speed_gbps >= 100:
        styles['penwidth'] = '6'
    elif speed_gbps >= 40:
        styles['penwidth'] = '5'
    elif speed_gbps >= 10:
        styles['penwidth'] = '4'
    elif speed_gbps >= 1:
        styles['penwidth'] = '3'
    else:
        styles['penwidth'] = '2'
        styles['style'] = 'dashed'
    
    return styles


def load_nodes_csv(nodes_path: str) -> pd.DataFrame:
    """Load nodes_for_vis_*.csv produced by process_switch_data.py"""
    try:
        nodes_df = pd.read_csv(nodes_path)
        required_cols = {"id", "label", "type", "location"}
        if not required_cols.issubset(nodes_df.columns):
            print(f"Error: nodes CSV is missing required columns {required_cols}")
            return None
        return nodes_df
    except FileNotFoundError:
        print(f"Error: could not find nodes CSV at '{nodes_path}'")
        return None


def load_links_csv(links_path: str) -> pd.DataFrame:
    """Load links_for_vis_*.csv produced by process_switch_data.py"""
    try:
        links_df = pd.read_csv(links_path)
        required_cols = {"source", "target", "port", "speed_Gbps", "medium"}
        if not required_cols.issubset(links_df.columns):
            print(f"Error: links CSV is missing required columns {required_cols}")
            return None
        return links_df
    except FileNotFoundError:
        print(f"Error: could not find links CSV at '{links_path}'")
        return None


def create_enhanced_network_diagram(nodes_df: pd.DataFrame, links_df: pd.DataFrame, output_path: str):
    """Create an enhanced network topology diagram with improved layout and readability"""
    
    if nodes_df is None or links_df is None or nodes_df.empty:
        print("Cannot build diagram – missing or empty dataframes.")
        return

    # Filter to core and distribution switches only
    filtered_nodes = nodes_df[nodes_df['type'].isin(['core', 'dist'])].copy()
    node_ids = set(filtered_nodes['id'])
    filtered_links = links_df[
        (links_df['source'].isin(node_ids)) & 
        (links_df['target'].isin(node_ids))
    ].copy()
    
    print(f"Building enhanced diagram: {len(filtered_nodes)} nodes, {len(filtered_links)} links")

    if filtered_nodes.empty:
        print("No core or distribution switches found after filtering.")
        return

    # Create the main graph
    dot = graphviz.Digraph('EnhancedNetworkTopology', **GRAPH_STYLE)
    
    # Separate nodes by type for hierarchical layout
    core_nodes = filtered_nodes[filtered_nodes['type'] == 'core']
    dist_nodes = filtered_nodes[filtered_nodes['type'] == 'dist']
    
    # Create Data Center cluster for core switches
    if not core_nodes.empty:
        with dot.subgraph(name='cluster_core') as core_cluster:
            core_cluster.attr(
                label='Data Center - Core Layer',
                style='rounded,filled',
                fillcolor='#FADBD8',  # Light red background
                fontname='Arial-Bold',
                fontsize='14',
                penwidth='3',
                color='#E74C3C'
            )
            
            # Add core switches in same rank for horizontal layout
            with core_cluster.subgraph() as core_rank:
                core_rank.attr(rank='same')
                for _, node in core_nodes.iterrows():
                    # Simplify core node labels
                    simple_label = node['label'].replace('DC-L_CORE-', '').replace('_CORE', '')
                    core_rank.node(
                        node['id'],
                        label=f"{simple_label}\\n[CORE]",
                        **NODE_COLORS['core'],
                        width='2.0',
                        height='1.0'
                    )
    
    # Group distribution switches by building and organize in rows
    buildings = dist_nodes['location'].unique()
    buildings_sorted = sorted([b for b in buildings if b not in ['Data Center', 'Unknown']])
    
    # Organize buildings in rows for better layout
    BUILDINGS_PER_ROW = 3
    for row_idx in range(0, len(buildings_sorted), BUILDINGS_PER_ROW):
        row_buildings = buildings_sorted[row_idx:row_idx + BUILDINGS_PER_ROW]
        
        # Create a subgraph for this row to keep buildings aligned
        with dot.subgraph() as row_subgraph:
            row_subgraph.attr(rank='same')
            
            for building in row_buildings:
                building_nodes = dist_nodes[dist_nodes['location'] == building]
                if building_nodes.empty:
                    continue
                    
                cluster_name = f"cluster_{building.replace(' ', '_').replace('-', '_')}"
                
                with dot.subgraph(name=cluster_name) as building_cluster:
                    building_cluster.attr(
                        label=f'{building}',
                        style='rounded,filled',
                        fillcolor='#D6EAF8',  # Light blue background
                        fontname='Arial-Bold',
                        fontsize='12',
                        penwidth='2',
                        color='#3498DB'
                    )
                    
                    # Add distribution switches
                    for _, node in building_nodes.iterrows():
                        # Simplify node labels for better readability
                        simple_label = node['label'].replace('_SW-DIST', '').replace('_DIST', '')
                        building_cluster.node(
                            node['id'],
                            label=simple_label,
                            **NODE_COLORS['dist'],
                            width='1.6',
                            height='0.7'
                        )
    
    # Add edges with enhanced styling and information
    edge_info = defaultdict(list)  # Group multiple connections between same nodes
    
    for _, link in filtered_links.iterrows():
        source = link['source']
        target = link['target']
        port = link['port']
        speed = link['speed_Gbps'] if not pd.isna(link['speed_Gbps']) else 0
        medium = link['medium']
        
        # Create normalized edge key to handle bidirectional connections
        # Always put the lexicographically smaller node first
        edge_key = tuple(sorted([source, target]))
        edge_info[edge_key].append({
            'port': port,
            'speed': speed,
            'medium': medium,
            'source': source,
            'target': target
        })
    
    # Create edges with aggregated information (bidirectional consolidated)
    for edge_key, connections in edge_info.items():
        node1, node2 = edge_key
        if node1 not in node_ids or node2 not in node_ids:
            continue
            
        # Aggregate connection info
        total_speed = sum(conn['speed'] for conn in connections)
        max_speed = max(conn['speed'] for conn in connections)
        ports = [conn['port'] for conn in connections]
        mediums = list(set(conn['medium'] for conn in connections))
        
        # Create simplified edge label showing bidirectional info
        if len(connections) == 1:
            conn = connections[0]
            speed_str = f"{int(conn['speed'])}G" if conn['speed'] > 0 else "N/A"
            medium_str = "F" if conn['medium'] == 'Fiber' else "C"
            label = f"{speed_str}{medium_str}"
        elif len(connections) == 2:
            # Check if it's truly bidirectional (A->B and B->A)
            sources = [conn['source'] for conn in connections]
            targets = [conn['target'] for conn in connections]
            if set(sources) == set(targets) and len(set(sources)) == 2:
                # It's bidirectional, show as single connection
                speeds = [conn['speed'] for conn in connections]
                avg_speed = sum(speeds) / len(speeds)
                speed_str = f"{int(avg_speed)}G" if avg_speed > 0 else "N/A"
                primary_medium = mediums[0] if mediums else 'Copper'
                medium_str = "F" if primary_medium == 'Fiber' else "C"
                label = f"{speed_str}{medium_str}"
            else:
                # Multiple connections same direction
                speed_str = f"{int(total_speed)}G" if total_speed > 0 else "N/A"
                label = f"{len(connections)}x {speed_str}"
        else:
            speed_str = f"{int(total_speed)}G" if total_speed > 0 else "N/A"
            label = f"{len(connections)}x {speed_str}"
        
        # Get edge style
        primary_medium = mediums[0] if mediums else 'Copper'
        edge_style = get_edge_style(max_speed, primary_medium)
        
        # Add the edge as undirected (no arrowhead for bidirectional)
        dot.edge(
            node1,
            node2,
            label=label,
            **edge_style,
            fontsize='8',
            labeldistance='1.5',
            labelangle='0',
            dir='none'  # Remove arrowhead for undirected connection
        )
    
    # Add legend
    with dot.subgraph(name='cluster_legend') as legend:
        legend.attr(
            label='Legend',
            style='rounded,filled',
            fillcolor='#F8F9FA',
            fontname='Arial-Bold',
            fontsize='12',
            penwidth='2'
        )
        
        # Node type legend
        legend.node('leg_core', label='Core Switch', **NODE_COLORS['core'], width='1.5', height='0.5')
        legend.node('leg_dist', label='Distribution Switch', **NODE_COLORS['dist'], width='1.5', height='0.5')
        
        # Connection type legend
        legend.node('leg_fiber_start', shape='point', width='0.1')
        legend.node('leg_fiber_end', shape='point', width='0.1')
        legend.edge('leg_fiber_start', 'leg_fiber_end', 
                   label='Fiber (10G)', color='#E67E22', penwidth='4')
        
        legend.node('leg_copper_start', shape='point', width='0.1')
        legend.node('leg_copper_end', shape='point', width='0.1')
        legend.edge('leg_copper_start', 'leg_copper_end', 
                   label='Copper (1G)', color='#8E44AD', penwidth='3')
    
    # Render the diagram
    try:
        dot.render(output_path, format='png', view=False, cleanup=True)
        print(f"✅ Enhanced diagram saved to {output_path}.png")
        dot.render(output_path, format='svg', view=False, cleanup=True)
        print(f"✅ Enhanced diagram saved to {output_path}.svg")
        
        # Also save the dot source for debugging
        with open(f"{output_path}.dot", 'w') as f:
            f.write(dot.source)
        print(f"✅ Graphviz source saved to {output_path}.dot")
        
    except Exception as e:
        print(f"Error rendering enhanced graph: {e}")


def create_simplified_mermaid_diagram(nodes_df: pd.DataFrame, links_df: pd.DataFrame, output_path: str):
    """Create a simplified Mermaid diagram focusing on core network connections"""
    
    if nodes_df is None or links_df is None or nodes_df.empty:
        print("Cannot build Mermaid diagram – missing or empty dataframes.")
        return

    # Filter to core and distribution switches only
    filtered_nodes = nodes_df[nodes_df['type'].isin(['core', 'dist'])].copy()
    node_ids = set(filtered_nodes['id'])
    filtered_links = links_df[
        (links_df['source'].isin(node_ids)) & 
        (links_df['target'].isin(node_ids))
    ].copy()

    if filtered_nodes.empty:
        print("No core or distribution nodes found for Mermaid diagram.")
        return

    def sanitize_id(name):
        """Sanitize node IDs for Mermaid"""
        return (name.replace('-', '_')
                   .replace(' ', '_')
                   .replace('.', '_')
                   .replace('(', '_')
                   .replace(')', '_')
                   .replace('[', '_')
                   .replace(']', '_'))

    # Build Mermaid diagram
    mmd_lines = ["graph TD", ""]
    
    # Add core nodes
    core_nodes = filtered_nodes[filtered_nodes['type'] == 'core']
    if not core_nodes.empty:
        mmd_lines.append("  %% Core Layer")
        for _, node in core_nodes.iterrows():
            safe_id = sanitize_id(node['id'])
            mmd_lines.append(f"  {safe_id}[\"{node['label']}<br/>CORE\"]")
        mmd_lines.append("")
    
    # Add distribution nodes grouped by building
    dist_nodes = filtered_nodes[filtered_nodes['type'] == 'dist']
    buildings = sorted(dist_nodes['location'].unique())
    
    for building in buildings:
        if building in ['Data Center', 'Unknown']:
            continue
        mmd_lines.append(f"  %% {building}")
        building_nodes = dist_nodes[dist_nodes['location'] == building]
        for _, node in building_nodes.iterrows():
            safe_id = sanitize_id(node['id'])
            mmd_lines.append(f"  {safe_id}[\"{node['label']}<br/>DIST\"]")
        mmd_lines.append("")
    
    # Add connections
    mmd_lines.append("  %% Connections")
    for _, link in filtered_links.iterrows():
        source_id = sanitize_id(link['source'])
        target_id = sanitize_id(link['target'])
        speed = int(link['speed_Gbps']) if not pd.isna(link['speed_Gbps']) else 0
        medium = link['medium']
        
        label = f"{speed}G {medium}"
        mmd_lines.append(f"  {source_id} -->|{label}| {target_id}")
    
    # Add styling
    mmd_lines.extend([
        "",
        "  %% Styling",
        "  classDef coreStyle fill:#E74C3C,stroke:#C0392B,stroke-width:3px,color:#fff",
        "  classDef distStyle fill:#3498DB,stroke:#2980B9,stroke-width:2px,color:#fff"
    ])
    
    # Apply styles
    for _, node in core_nodes.iterrows():
        safe_id = sanitize_id(node['id'])
        mmd_lines.append(f"  class {safe_id} coreStyle")
    
    for _, node in dist_nodes.iterrows():
        safe_id = sanitize_id(node['id'])
        mmd_lines.append(f"  class {safe_id} distStyle")
    
    # Write Mermaid file
    mermaid_content = "\n".join(mmd_lines)
    output_filepath_mmd = f"{output_path}_enhanced.mmd"
    
    try:
        with open(output_filepath_mmd, 'w') as f:
            f.write(mermaid_content)
        print(f"✅ Enhanced Mermaid diagram saved to {output_filepath_mmd}")
    except Exception as e:
        print(f"Error writing enhanced Mermaid file: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python visualize_network_test.py <path_to_processed_data_folder>")
        sys.exit(1)

    input_dir = sys.argv[1]
    if not os.path.isdir(input_dir):
        print(f"Error: Provided path is not a directory: {input_dir}")
        sys.exit(1)

    # Find nodes and links files
    nodes_files = glob.glob(os.path.join(input_dir, 'nodes_for_vis_*.csv'))
    links_files = glob.glob(os.path.join(input_dir, 'links_for_vis_*.csv'))

    if not nodes_files or not links_files:
        print(f"Error: Could not find required CSV files in '{input_dir}'")
        sys.exit(1)

    nodes_csv_path = nodes_files[0]
    links_csv_path = links_files[0]
    
    # Create output path
    base_name = os.path.basename(input_dir)
    output_filepath = os.path.join(input_dir, f"network_topology_enhanced_{base_name}")

    print("Loading data...")
    nodes_df = load_nodes_csv(nodes_csv_path)
    links_df = load_links_csv(links_csv_path)
    
    if nodes_df is not None and links_df is not None:
        print("Creating enhanced network diagram...")
        create_enhanced_network_diagram(nodes_df, links_df, output_filepath)
        
        print("Creating enhanced Mermaid diagram...")
        create_simplified_mermaid_diagram(nodes_df, links_df, output_filepath)
        
        print("✅ Enhanced visualization complete!")
    else:
        print("❌ Failed to load data files") 