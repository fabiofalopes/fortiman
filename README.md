# FortiMan: FortiSwitch Port Analysis Tool

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 2. Setup Credentials
Create a `.env` file in the project root:
```dotenv
FORTIGATE_URL="https://192.168.1.99"
USERNAME="your_username"
PASSWORD="your_password"
```

### 3. Run the Pipeline
```bash
# Step 1: Extract data from FortiGate
python fortiswitch_ports_scraper.py

# Step 2: Process the CSV file (replace with your actual filename)
python process_switch_data.py outputs/fortiswitch_ports_2025-01-20_15-30-45.csv

# Step 3: Generate network topology visualization (optional)
python visualize_network.py outputs/fortiswitch_ports_2025-01-20_15-30-45
```

### 4. Output Files Generated

After running the complete pipeline, you'll get a structured output directory:

```
outputs/fortiswitch_ports_YYYY-MM-DD_HH-MM-SS/
├── processed_fortiswitch_ports_YYYY-MM-DD_HH-MM-SS.xlsx    # Excel report
├── links_for_vis_fortiswitch_ports_YYYY-MM-DD_HH-MM-SS.csv # Network links data
├── nodes_for_vis_fortiswitch_ports_YYYY-MM-DD_HH-MM-SS.csv # Network nodes data
├── network_topology_fortiswitch_ports_YYYY-MM-DD_HH-MM-SS.png # Network diagram (PNG)
├── network_topology_fortiswitch_ports_YYYY-MM-DD_HH-MM-SS.svg # Network diagram (SVG)
└── network_topology_fortiswitch_ports_YYYY-MM-DD_HH-MM-SS.mmd # Mermaid diagram source
```

**File Descriptions:**
- **Excel Report**: Organized port data grouped by switch with core switches prioritized
- **CSV Files**: Helper files for network visualization (nodes and links)
- **PNG/SVG Diagrams**: Visual network topology showing switch connections
- **Mermaid File**: Source code for the network diagram (can be edited/customized)

---

## What This Tool Does

This project provides a complete pipeline to extract, process, and analyze FortiSwitch Ports data from a FortiGate web interface.

### Phase 1: Data Extraction (`fortiswitch_ports_scraper.py`)
- Automated login to FortiGate
- Navigates to FortiSwitch Ports page
- Automatically enables all table columns
- Handles virtual scrolling to extract all data
- Saves data to timestamped CSV file

### Phase 2: Data Processing (`process_switch_data.py`)
- Reads CSV and creates Excel report
- Groups ports by switch
- Prioritizes core switches at the top
- Creates organized mini-tables for each switch
- Generates helper CSV files for network visualization

### Phase 3: Network Visualization (`visualize_network.py`)
- Creates visual network topology diagrams
- Filters to show core and distribution switches only
- Generates multiple output formats (PNG, SVG, Mermaid)
- Provides interactive network diagram source code

## Requirements

- Python 3.8+
- FortiGate access with permissions to view FortiSwitch Ports
- User credentials with appropriate access level

## Project Structure

```
fortiman/
├── fortiswitch_ports_scraper.py  # Data extraction script
├── process_switch_data.py        # Data processing script
├── visualize_network.py          # Network visualization script
├── requirements.txt              # Python dependencies
├── outputs/                      # Generated files and reports
└── .env                         # Credentials (create this)
```

## Security Note

The `.env` file contains sensitive credentials and should never be shared or committed to version control. It's already included in `.gitignore`. 