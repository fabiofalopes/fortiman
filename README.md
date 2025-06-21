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
```

### 4. Get Results
- Raw data: `outputs/fortiswitch_ports_YYYY-MM-DD_HH-MM-SS.csv`
- Processed report: `outputs/processed_fortiswitch_ports_YYYY-MM-DD_HH-MM-SS.xlsx`

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

## Requirements

- Python 3.8+
- FortiGate access with permissions to view FortiSwitch Ports
- User credentials with appropriate access level

## Project Structure

```
fortiman/
├── fortiswitch_ports_scraper.py  # Data extraction script
├── process_switch_data.py        # Data processing script
├── requirements.txt              # Python dependencies
├── outputs/                      # Generated files
└── .env                         # Credentials (create this)
```

## Security Note

The `.env` file contains sensitive credentials and should never be shared or committed to version control. It's already included in `.gitignore`. 