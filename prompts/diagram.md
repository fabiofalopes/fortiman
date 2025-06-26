### **Corrected Specification for Hierarchical Network Topology Diagram**

This document outlines the precise visual and structural requirements for generating the campus network topology diagram based on a strict, top-down, "ladder" hierarchy. The primary objective is to create an exceptionally clear, orderly, and vertically-oriented diagram.

#### **1. Core Principles: The Vertical Ladder**

*   **Canvas & Orientation:** The diagram must be rendered on a portrait-oriented canvas (taller than it is wide) to accommodate the vertical "ladder" structure.
*   **Hierarchy:** The layout is a strict top-to-bottom hierarchy. Elements are placed on discrete vertical "rungs" of the ladder.
*   **Primary Axis:** The primary organizing principle is vertical. Buildings with direct connections to the core infrastructure are stacked one below the other, each on its own rung.
*   **Secondary Axis:** The horizontal axis is used only to show direct dependencies. A building that connects to another building (instead of the core) will be placed horizontally next to its parent on the same ladder rung.

#### **2. Rung 1: Data Center (Core Layer)**

*   **Position:** At the absolute top of the ladder. The "Data Center - Core Layer" container is placed at the top-center of the canvas.
*   **Contents:**
    *   `FIB02 [CORE]` (Core 2) positioned on the left.
    *   `FIB01 [CORE]` (Core 1) positioned on the right.

#### **3. Rung 2: Building L**

*   **Position:** On the second rung of the ladder, placed directly below and horizontally centered with the Data Center. This building is treated as a special case and gets its own dedicated layer.

#### **4. Subsequent Rungs: The Main Building Stack**

This section defines the placement for all remaining buildings. The layout proceeds rung by rung, down the ladder.

*   **Ordering:** All buildings (except 'L') that connect **directly to the Core Layer** are identified and sorted alphabetically. This sorted list dictates the order of the rungs.
*   **Placement Logic:**
    1.  For each building in the sorted list (A, B, C, D, etc.), a new rung is created below the previous one.
    2.  The primary building for that rung (e.g., Building A) is placed on the left side of the rung.
    3.  **Dependency Check:** The system must then check if any other buildings use this primary building as their sole uplink.
    4.  **Horizontal Placement for Dependencies:**
        *   If a "child" building (e.g., Building T) connects to the primary "parent" building on this rung (e.g., Building M), the child is placed immediately to the right of the parent on the same rung.
        *   If a chain of dependencies exists (e.g., Building H connects to P, which connects to G), they are all laid out horizontally on the parent's rung: `[Building G] -- [Building P] -- [Building H]`.
        *   The connection between these horizontally-placed buildings should be a short, straight line.

*   **Resulting Ladder Structure:**
    *   **Rung for A:** `[Building A]`
    *   **Rung for B:** `[Building B]`
    *   **Rung for C:** `[Building C]`
    *   ...and so on alphabetically.
    *   **Rung for G:** `[Building G] --- [Building P] --- [Building H]`
    *   **Rung for M:** `[Building M] --- [Building T]`
    *   **Rung for S:** `[Building S] --- [Building X]`
    *   **Rung for Z:** `[Building Z] --- [Building Y]`

#### **5. Core Uplink Routing: The "Up and Over" Method**

The routing of connections from the ladder rungs to the Core Layer is critical to avoid clutter. This logic remains unchanged as it supports the vertical layout perfectly.

*   **Path Definition:** All uplink connections must be drawn with clean 90-degree angles (orthogonal routing).
*   **Routing Logic:**
    1.  **Egress:** Lines exit from the top of the primary building container on each rung and travel vertically upwards.
    2.  **Turnout:** After a short distance, lines turn 90 degrees to travel horizontally towards the edge of the canvas.
        *   Connections to `FIB02 [CORE]` (left) turn **left**.
        *   Connections to `FIB01 [CORE]` (right) turn **right**.
    3.  **Vertical Trunk:** Lines then turn 90 degrees upwards, running in parallel, dedicated lanes along the sides of the canvas until they are level with the Data Center.
    4.  **Ingress:** Lines make a final 90-degree turn inward to connect to the target core switch.

This ensures a clean "freeway" of uplink connections on either side of the central building ladder, with zero overlap.

#### **6. Intra-Building & Legend**

*   **Internal Layout:** Inside each building container, the switch providing the main uplink is at the top, with other switches stacked vertically below it.
*   **Legend:** A clear legend should be placed in the top-right corner.