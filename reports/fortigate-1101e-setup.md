# FortiGate 1101E – Current Setup (FortiOS 7.4.5)

## 1. Device Overview
- **Model:** FortiGate 1101E
- **Form Factor:** Rack Mount, 2RU
- **Weight:** 25.4 lbs (11.55 kg)
- **Onboard Storage:** 2 × 480 GB SSD
- **Serial Number:** `<your-serial-number>`
- **Location:** `<your-location>`
- **Deployment Date:** `<deployment-date>`
- **Purpose/Role:** `<e.g., Perimeter Firewall, Core Security Gateway>`

## 2. Hardware & Licensing
- **CPU:** Dual custom Fortinet NP6 network processors, CP9 content processor
- **RAM:** (Not officially listed; typically 32GB+ for this class)
- **Hardware Accelerated Ports:**
  - 2 × 40 GE QSFP+ slots
  - 4 × 25 GE SFP28 slots
  - 4 × 10 GE SFP+ slots
  - 8 × GE SFP slots
  - 16 × GE RJ45 ports
  - 2 × GE RJ45 Management/HA ports
- **USB Ports:** 1 (client), 2 (server)
- **Console Port:** 1
- **Redundant Power Supplies:** Yes (hot swappable)
- **Certifications:** FCC, CE, RCM, VCCI, BSMI, UL/cUL, CB, USGv6/IPv6
- **Licensed Features:** `<e.g., UTM, IPS, Web Filtering, Application Control, etc.>`
- **Support Contract:** `<expiry date / type>`

## 3. Performance
- **IPS Throughput:** 12.5 Gbps
- **NGFW Throughput:** 9.8 Gbps
- **Threat Protection Throughput:** 7.1 Gbps
- **IPv4/IPv6 Firewall Throughput:** 80 Gbps
- **Concurrent Sessions:** 8 million
- **New Sessions/Second:** 500,000
- **IPsec VPN Throughput:** 48 Gbps
- **SSL-VPN Throughput:** 8.4 Gbps
- **Max SSL-VPN Users:** 10,000
- **Power Consumption (Avg/Max):** 222 W / 346 W
- **Operating Temp:** 0°C to 40°C
- **Humidity:** 10% to 90% non-condensing

## 4. Firmware & Updates
- **Current Firmware Version:** FortiOS v7.4.5
- **Last Firmware Update:** `<date>`
- **Planned Updates:** `<planned version or schedule>`

## 5. Network Interfaces & VLANs
| Interface | Role         | IP Address      | VLAN | Zone | Comments           |
|-----------|--------------|-----------------|------|------|--------------------|
| port1     | WAN          | `<ip>`          |      |      | `<ISP details>`    |
| port2     | LAN          | `<ip>`          |      |      | `<LAN segment>`    |
| ...       | ...          | ...             | ...  | ...  | ...                |

## 6. Routing & Static Routes
- **Default Gateway:** `<ip>`
- **Static Routes:**
  - `<destination>` via `<gateway>` on `<interface>`
- **Dynamic Routing Protocols:** `<OSPF/BGP/etc. if used>`

## 7. Security Policies
- **Total Policies:** `<number>`
- **Sample Policy Table:**
| ID | Source      | Destination | Service | Action | Comments         |
|----|-------------|-------------|---------|--------|------------------|
| 1  | LAN_SUBNET  | ANY         | ALL     | ACCEPT | Allow LAN to WAN |
| 2  | ANY         | DMZ         | HTTP    | DENY   | Block HTTP to DMZ|
| ...| ...         | ...         | ...     | ...    | ...              |

## 8. VPN Configuration
- **Site-to-Site VPNs:**
  - `<peer info, type, status>`
- **Remote Access VPNs:**
  - `<SSL/IPSec, user groups, portals>`

## 9. User & Authentication
- **Admin Users:** `<list or reference>`
- **User Groups:** `<list or reference>`
- **Authentication Methods:** `<local, LDAP, RADIUS, etc.>`

## 10. Logging & Monitoring
- **Syslog Servers:** `<ip/hostname>`
- **SNMP:** `<enabled/disabled, community>`
- **Alerting:** `<email, SMS, etc.>`
- **Log Retention Policy:** `<duration>`

## 11. Backup & Maintenance
- **Backup Schedule:** `<frequency, location>`
- **Last Backup:** `<date>`
- **Maintenance Tasks:** `<regular checks, updates, etc.>`

## 12. References
- [FortiGate 1100E Series Datasheet (PDF)](https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortigate-1100e-series.pdf)
- [FortiGate 1101E Fast Path Architecture](https://docs.fortinet.com/document/fortigate/7.0.7/hardware-acceleration/824164/fortigate-1100e-and-1101e-fast-path-architecture)
- [FortiOS 7.4.5 Administration Guide](docs/FortiOS-7.4.5-Administration_Guide.md)
- [FortiOS 7.4.5 CLI Reference](docs/FortiOS-7.4.5-CLI_Reference.md)
- [Release Notes](docs/release_notes-versions/fortios-v7.4.5-release-notes.md)

---

> **Note:** Replace all `<...>` placeholders with your actual device and configuration details. This file should be updated whenever there are significant changes to your FortiGate setup. 