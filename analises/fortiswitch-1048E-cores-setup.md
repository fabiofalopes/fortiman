# FortiSwitch 1048E Core Switches - Setup

This document outlines the setup and configuration for the two core FortiSwitch 1048E devices in the infrastructure.

## 1. Device Overview

Our core network infrastructure relies on two FortiSwitch 1048E switches managed in FortiLink mode by our FortiGate 1101E firewall.

### Core Switch 1
- **Name:** DC-L_CORE-FIB01
- **Model:** FortiSwitch 1048E
- **Serial Number:** `<S/N for DC-L_CORE-FIB01>` FS1E48T422002174
- **Role:** Core Network Switch

### Core Switch 2
- **Name:** DC-L_CORE-FIB02
- **Model:** FortiSwitch 1048E
- **Serial Number:** `<S/N for DC-L_CORE-FIB02>`
- **Role:** Core Network Switch (Redundant)

## 2. Hardware & Licensing (FortiSwitch 1048E)
- **Form Factor:** 1 RU Rack Mount
- **Ports:**
  - 48 × 10G/1G SFP+/SFP ports
  - 6 × 40G QSFP+ ports (can be used as 4 x 100G QSFP28)
- **Management Ports:** 1 x RJ-45 Serial Console, 1 x 10/100/1000 Service Port
- **Power Supplies:** Dual hot-swappable AC PSUs
- **Licensed Features:** Advanced features (such as BGP, VRF, PIM) require `FS-SW-LIC-1000`. Currently operating with standard feature set.

## 3. Performance (FortiSwitch 1048E)
- **Switching Capacity (Duplex):** 1.76 Tbps
- **Packets Per Second (Duplex):** 1,518 Mpps
- **MAC Address Storage:** 144,000
- **Network Latency:** < 800 ns
- **VLANs Supported:** 4,096
- **Packet Buffers:** 12 MB
- **Memory:** 8 GB DDR3
- **Storage:** 128 GB SSD

## 4. Firmware & Management
- **Management Mode:** FortiLink
- **Managed By:** FortiGate 1101E
- **FortiGate Firmware:** FortiOS v7.4.5

### Firmware Status: DC-L_CORE-FIB01
- **Current Firmware Version:** `FS1E48-v7.4.4-build0861`
- **Available Upgrade:** `FS1E48-v7.6.0-build1015` is available.
- **Last Firmware Update:** `<date>`

### Firmware Status: DC-L_CORE-FIB02
- **Current Firmware Version:** `<check device for version>`
- **Available Upgrade:** `<check device for version>`
- **Last Firmware Update:** `<date>`

## 5. Network Interfaces & Key Connections
The switches are configured with numerous connections to distribution layer switches across the campus. The following is a high-level summary of active links from the core switches.

- **DC-L_CORE-FIB01 Uplinks:** Connects to distribution switches in blocks A, B, C, D, E, F, G, I, L, M, N, P, Q, S, U, V.
- **DC-L_CORE-FIB02 Uplinks (Redundancy):** Provides redundant links to key distribution switches in blocks A, C, F, L, V.

A full link mapping can be found in the network visualization CSV files.

## 6. References
- [FortiSwitch Data Center Series Datasheet](./fortiswitch-docs/FortiSwitch_Data_Center_Series.md)
- [FortiSwitchOS 7.4.4 Release Notes (for FortiOS 7.4.4)](./fortiswitch-docs/FortiSwitchOS-7.4.3-FortiLink-Release-Notes-(FortiOS-7.4.4).md)
- [FortiGate 1101E Setup](./fortigate-1101E-setup.md)

---

> **Note:** This file should be updated whenever there are significant changes to the core switches' configuration or firmware. 