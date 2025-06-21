# Network Topology Visualization Specification

## 1. Overview & Goal

This document provides a strict specification for creating a network topology diagram. The primary goal is to produce a visualization that is clean, professional, hierarchical, symmetrical, and immediately understandable to both technical and non-technical audiences.

The current script-based iterative approach has proven inefficient, often resulting in unreadable, horizontally-sprawled diagrams with overlapping elements, poor resolution, and inconsistent layouts. This specification will serve as the definitive blueprint to solve these issues.

**The final output must be a high-resolution image that is aesthetically pleasing and functionally clear.** It must not look like a "mess."

## 2. Data Source

The visualization will be generated using two primary data files produced by the `process_switch_data.py` script:
- `nodes_for_vis_*.csv`: Contains information about each network device (ID, label, type, location).
- `links_for_vis_*.csv`: Contains information about each physical link (source, target, port, speed, medium).

Only nodes with `type` of `core` or `dist` (distribution) will be included in the diagram. All other node types must be filtered out to reduce clutter.

## 3. Core Layout Principles

The layout is the most critical aspect of the visualization and must adhere to the following principles without exception.

### 3.1. Strict Vertical Hierarchy

The diagram must follow a strict top-to-bottom (`TB`) hierarchical layout. The overall structure should resemble a pyramid or a tree, flowing from the central core down to the various buildings. **Horizontal sprawl is strictly prohibited.**

### 3.2. Apex: The Data Center

- The **Data Center** sits at the absolute top of the hierarchy.
- The Data Center itself is physically located in **Building L**. Therefore, the "Data Center" cluster must be visually nested *inside* the "Building L" cluster.
- The "Building L" cluster, containing the Data Center, will be the single element at the top rank of the diagram.

### 3.3. Building Placement & Connectivity Logic

This is the key to an organized layout and avoiding crossed lines.

1.  **Primary Tier (Direct Connections)**:
    - All buildings that have a **direct link** to a core switch in the Data Center will be placed in the primary tier directly below Building L.
    - These buildings should be arranged alphabetically in one or more horizontal rows.
    - The connections from the Data Center to these buildings must be drawn as clean, vertical lines.

2.  **Secondary Tiers (Indirect Connections)**:
    - Any building that **does not** connect directly to the Data Center, but instead connects to a distribution switch in another building (an "intermediate" building), belongs in a secondary tier.
    - These secondary buildings should be placed horizontally adjacent to the intermediate building they connect to.
    - For example, if Building X, Y, and Z connect to a switch in Building A (which connects to the DC), then X, Y, and Z should be arranged horizontally on the same rank as Building A, with clear lines drawn to Building A. This visually groups dependent buildings with their parent.

### 3.4. Symmetry and Spacing

- The layout must be as symmetrical as possible. Buildings in each tier should be evenly distributed.
- There must be generous spacing between all elements (nodes, clusters, labels) to ensure readability and prevent a cluttered appearance.

## 4. Visual Styling

### 4.1. No Overlapping Elements

**It is strictly forbidden for any element to overlap another.**
- Lines (edges) must **never** cross through node boxes (switches).
- Lines must **never** cross through cluster boxes (buildings).
- Lines should be routed cleanly around all objects. Use of orthogonal `ortho` line routing is preferred.

### 4.2. Building & Switch Representation

- **Buildings**: Each building must be rendered as a clearly delineated cluster (a container box with a light background color). The building name (e.g., "Building G") must be used as the label for the cluster.
- **Switches**: Each switch must be a node (a box) rendered *inside* its respective building cluster. The switch's label should be its hostname (e.g., `G-2-1_SW-DIST`).

### 4.3. Link (Edge) Representation

- **Individual Links**: Every single link between two switches must be drawn as a distinct, individual line. Aggregated, thick "summary" lines that obscure the underlying connections are prohibited.
- **Link Information Labels**: Every line representing a link must have a readable label placed alongside it. This label is critical and must contain:
    - **Source Port**: The port on the source switch (e.g., `DC-L_CORE-FIB01:port48`).
    - **Destination Port**: The port on the destination switch (e.g., `A-01-SW-DIST:port24`).
    - **Link Speed**: The negotiated speed of the link (e.g., `10 Gbps`).
- **Color/Style**: Line color and style can still be used to indicate medium (Fiber/Copper) and provide at-a-glance speed information, but this is secondary to the explicit labels.

## 5. Legend

A clear and concise legend must be present on the diagram, separate from the main topology. It should explain:
- Node colors (e.g., Red = Core Switch, Teal = Distribution Switch).
- Line colors/styles (e.g., Orange = Fiber, Blue = Copper).

## 6. Output Format

The final output must be a high-resolution PNG and SVG file. A high DPI (e.g., 300 or 600) is required to ensure that text remains crisp and readable when zooming in. 