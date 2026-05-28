# QuickStart Guide - FortiSwitch 448E Series

# QuickStart Guide

# FortiSwitch 448E Series

- FS-448E
- FS-448E-PoE
- FS-448E FPoE
---
# Fortinet FortiSwitch Product Registration

# Product Registration

Thank you for purchasing a Fortinet FortiSwitch. To access:

- Cloud Management
- FortiGuard Updates
- Firmware Upgrades
- Technical Support
- Warranty Coverage

Please register your Fortinet FortiSwitch:

Vous devez enregistrer le produir:

Debe registrar el producto:

登録のお願い:

请马上注册:

http://support.fortinet.com

Date: March 13, 2025

This guide covers: FS-448E, FS-448E-POE, FS-448E-FPOE

Copyright © 2025 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., in the U.S. and other jurisdictions, and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or company names may be trademarks of their respective owners.

Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other conditions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s Legal and above, with a purchaser that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. In no event does Fortinet make any commitment related to future deliverables, features or development, and circumstances may change such that any forward-looking statements herein are not accurate. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise revise this publication without notice, and the most current version of the publication shall be applicable.

For Product License Agreement / EULA and Warranty Terms, visit https://www.fortinet.com/content/dam/fortinet/assets/legal/EULA.pdf
---
# FortiSwitch 448E QuickStart Guide

# Contents - FS 448E

# Front Panel - FS 448E

- #RTINET POWER
- MGMT ALARM
- PSU
- USB

FortiSwitch 448E

- FZRTINET POWER
- MGMT ALARM
- PSU

# Ports Overview

Ports 1 to 48 (RJ45) GE network connections

| Speed                                  | LED                         | Act/Link                      |
| -------------------------------------- | --------------------------- | ----------------------------- |
| Green: Connected at 1000Mbps           | Amber: Connected at 100Mbps | Green: Connected              |
| Off: Connected at 10Mbps or not in use | Off: No link established    | Flashing Green: Data activity |

# Ports 49 to 52 (SFP+) 10Gbps SFP connections

|   |   | Speed | LED                        | Act/Link                  |                               |
| - | - | ----- | -------------------------- | ------------------------- | ----------------------------- |
|   |   |       | Green: Connected at 10Gbps | Amber: Connected at 1Gbps | Green: Connected              |
|   |   |       |                            | Off: No link established  | Flashing Green: Data activity |

# QuickStart Guide

# FortiSwitch 448E Series

- Models: FS-448E, FS-448E-PoE, FS-448E FPoE

# Included Items

- 2x Rack-Mount Brackets
- 2x Power Cables
- 8x Bracket Screws
- Console Cable (USB to RJ45)
- 4x Rubber Feet

# LED Indicators

- Power:
- Green: Power is on
- Amber: Power supply operating normally
- Off: Power is off
- ALARM:
- Amber: Fault detected
- Off: No fault detected
- MGMT:
- Green: Link connected
- Flashing Green: Management data activity
- Off: No link established
---
# Rear Panel - FS 448E

body {
font-family: Arial, sans-serif;
line-height: 1.6;
}
h1, h2, h3 {
color: #333;
}
.caution {
color: red;
font-weight: bold;
}
.table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
.table, .th, .td {
border: 1px solid #ddd;
}
.th, .td {
padding: 8px;
text-align: left;
}
.th {
background-color: #f2f2f2;
}

# Rear Panel - FS 448E

# CONSOLE

CAUTION/ATTENTION

SHOCK HAZARD. DISCONNECT ALL POWER SOURCES.

RISQUE D’ÉLECTROCUTION. DÉBRANCHEZ TOUTES SOURCES D’ALIMENTATION.

| AC INPUT          | AC INPUT          |
| ----------------- | ----------------- |
| 100-240Vac        | 100-240Vac        |
| 1.5A Max, 50-60Hz | 1.5A Max, 50-60Hz |

# Ports

1. CONSOLE (RJ45) CLI management port
2. Redundant Power Supplies 100-240V AC, 1.5A Max, 50/60Hz
---
# FS 448E-PoE Documentation

# Contents - FS 448E-PoE

- Front Panel - FS 448E-PoE
- RTINET POWER
- MGMT ALARM
- PoE MAX
- USB

# Front Panel - FS 448E-PoE

|   |                                              |           | 1 | MGMT (RJ45) client management port, default IP 192.168.1.99                        |                           |                            |                              |                               |                          |                               |                          |
| - | -------------------------------------------- | --------- | - | ---------------------------------------------------------------------------------- | ------------------------- | -------------------------- | ---------------------------- | ----------------------------- | ------------------------ | ----------------------------- | ------------------------ |
|   |                                              |           | 2 | POWER                                                                              | ALARM                     | Green: Power is on         | Amber: Fault detected        | Off: Power is off             | Off: No fault detected   |                               |                          |
|   |                                              |           | 3 | PoE Ports 1 to 48 (RJ45) GE network connections providing up to 421W for all ports | PoE LED                   | Amber: Providing PoE power | Off: Not providing PoE power | Link/Act                      | Green: Connected         | Flashing Green: Data activity | Off: No link established |
| 4 | Ports 49 to 52 (SFP+) 10Gbps SFP connections | Speed LED |   | Green: Connected at 10Gbps                                                         | Amber: Connected at 1Gbps | Link/Act                   | Green: Connected             | Flashing Green: Data activity | Off: No link established |                               |                          |

# Included Items

- QuickStart Guide
- 2x Rack-Mount Brackets
- 2x Power Cables
- 8x Bracket Screws
- Console Cable (USB to RJ45)
- 4x Rubber Feet
---
# Rear Panel - FS 448E-PoE

body {
font-family: Arial, sans-serif;
line-height: 1.6;
}
h1, h2, h3 {
color: #333;
}
.caution {
color: red;
font-weight: bold;
}
.specs {
margin: 20px 0;
}
.table {
width: 100%;
border-collapse: collapse;
}
.table, .table th, .table td {
border: 1px solid black;
}
.table th, .table td {
padding: 8px;
text-align: left;
}

# Rear Panel - FS 448E-PoE

CAUTION/ATTENTION
SHOCK HAZARD. DISCONNECT ALL POWER SOURCES.

RISQUE D’ÉLECTROCUTION. DÉBRANCHEZ TOUTES SOURCES D’ALIMENTATION.

# AC INPUT

100-240Vac

7.0A Max, 50-60Hz

# Ports

| Port Number | Description                                             |
| ----------- | ------------------------------------------------------- |
| 1           | CONSOLE (RJ45) CLI management port                      |
| 2           | Redundant Power Supplies 100-240V AC, 7.0A Max, 50/60Hz |

---
# FS 448E-FPoE Documentation

# Contents - FS 448E-FPoE

# Front Panel - FS 448E-FPoE

| RTINETS POWER | MGMT | ALARM | PoE MAX |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |       |       |
| ------------- | ---- | ----- | ------- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | ----- | ----- |
| USB           | 10   | 12    | 16      | 18 | 20 | 22 | 24 | 26 | 28 | 30 | 32 | 34 | 36 | 38 | 40 | 42 | 44 | 46 | 48 | 49/50 | 51/52 |

# FortiSwitch 448E-FPoE

1. MGMT (RJ45) client management port, default IP 192.168.1.99

USB (2.0) for future use
2. POWER
- Green: Power is on
- Amber: Fault detected
- Off: Power is off

ALARM
- Off: No fault detected

PoE MAX
- Amber: Max PoE output reached
- Off: PoE power available

MGMT
- Green: Link connected
- Flashing Green: Management data activity
- Off: No link established
3. PoE Ports 1 to 48 (RJ45) GE network connections providing up to 800W for all ports
- Amber: Providing PoE power
- Off: Not providing PoE power

LED
- Green: Connected
- Flashing Green: Data activity
- Off: No link established
4. Ports 49 to 52 (SFP+) 10Gbps SFP connections
- Green: Connected at 10Gbps
- Amber: Connected at 1Gbps
- Flashing Green: Data activity
- Off: No link established

# Top port LEDs

Link/Act

# Bottom port LEDs

Link/Act

# Included Accessories

- 2x Rack-Mount Brackets
- 2x Power Cables
- 8x Bracket Screws
- Console Cable (USB to RJ45)
- 4x Rubber Feet
---
# Rear Panel - FS 448E-FPoE

body {
font-family: Arial, sans-serif;
line-height: 1.6;
}
h1, h2, h3 {
color: #333;
}
.caution {
color: red;
font-weight: bold;
}
.table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
.table th, .table td {
border: 1px solid #ddd;
padding: 8px;
}
.table th {
background-color: #f2f2f2;
}

# Rear Panel - FS 448E-FPoE

# CONSOLE

CAUTION/ATTENTION

SHOCK HAZARD. DISCONNECT ALL POWER SOURCES.

RISQUE D’ÉLECTROCUTION. DÉBRANCHEZ TOUTES SOURCES D’ALIMENTATION.

# AC INPUT

| Specification | Details    |
| ------------- | ---------- |
| Voltage       | 100-240Vac |
| Current       | 12.0A Max  |
| Frequency     | 50-60Hz    |

# Ports

| Port Number | Description                                              |
| ----------- | -------------------------------------------------------- |
| 1           | CONSOLE (RJ45) CLI management port                       |
| 2           | Redundant Power Supplies 100-240V AC, 12.0A Max, 50/60Hz |

---
# Installation Options


# Rack Installation

Your device includes a rackmount kit. You can also install your device as Desktop. Custom Rack/Rail kits are also available.

This device mounts in a standard 19 inch rack.

1. Attach the provided rack-mount brackets and screws
2. Position the device and slide into the rack
3. Fasten rack screws to secure the device

# Basic Connections

# Power Connection

Plug in your device to a power outlet using the provided power cables.

Note: We recommend connecting your FortiSwitch to an uninterruptible power supply (UPS) in case of a power outage.

Warning: For safety, it is recommended that two people install the device.
---
# Technical Documentation

body {
font-family: Arial, sans-serif;
line-height: 1.6;
}
h1, h2, h3 {
color: #333;
}
.section {
margin-bottom: 20px;
}
.subsection {
margin-left: 20px;
}
.list {
list-style-type: decimal;
margin-left: 20px;
}

# Desktop Option

Place the unit on a flat, clean and stable surface
Ensure there is at least 1.5in of clearance for adequate airflow

1.5in

1.5in

# SPF Transceivers

# Installation

Slide the SFP into the cage socket until it clicks into place
Lift the latch to lock the SFP

Cage Socket

1

ERTINET

1.5in

1.5in

SFP

2 Tx

3. Plug the provided power cables into the rear of the unit and then into a grounded electrical outlet or separate power source

# To remove the SFP transceivers:

Lower the latch to unlock the SFP
Carefully pull the SFP out of the cage socket

Cage Socket

1

SFP

2

Latch
---
# Setup Options

body {
font-family: Arial, sans-serif;
line-height: 1.6;
}
h1, h2, h3 {
color: #333;
}
.section {
margin-bottom: 20px;
}
.note {
background-color: #f9f9f9;
border-left: 4px solid #007BFF;
padding: 10px;
margin: 10px 0;
}

# Setup Options

# GUI

Set up your device locally using the GUI or CLI. Choose an option to complete your setup, then configure your device.

Browse to 192.168.1.99

# A GUI

An easy-to-use GUI, compatible with most web browsers.

To minimize scrolling, the screen resolution should be at least 1280 x 1024 pixels.

# B Command Line Interface (CLI)

An alternate configuration tool from the web-based manager that uses a terminal emulation application to type commands or upload batches of commands from a text file or configuration script.

1. Connect port 1 to the Management Computer using the supplied Ethernet cable
2. Enable DHCP or set the Management Computer’s IP and subnet to:
3. - Static IP Address: 192.168.1.1
- Subnet Mask: 255.255.255.0

Visit 192.168.1.99 in a web browser
4. Log in with the username admin and no password
5. You can now configure your FortiSwitch

# C FortiLink Management

FortiGate units can remotely manage FortiSwitch units, known as using a FortiSwitch in FortiLink mode. See the FortiOS Admin guide on docs.fortinet.com for detailed information.

# D FortiCloud Management

FortiSwitch Cloud manages FortiSwitch devices in standalone mode. It allows you to provision, monitor, troubleshoot, and optimize your standalone FortiSwitch deployment through an easy to understand user interface.

Note: After you log in for the first time, you will be prompted to set a new password.
---
# FortiSwitch Configuration Guide


# Console Port Configuration

1. Connect the Console Port with a Console Cable to the Serial Port on the Management Computer
2. Start a terminal program on the Management Computer and select an available COM Port using the following default settings:
- Baud rate: 115200
- Data bits: 8
- Parity: None
- Stop bits: 1
- Flow control: None
3. Log in using username admin and no password
4. You can now configure your FortiSwitch

Note: After you log in for the first time, you will be prompted to set a new password.

# FortiLink Configuration

1. Connect a FortiSwitch FortiLink Port directly using an Ethernet Cable to a FortiGate FortiLink Port or any FortiGate Port that is not an HA port.
2. Login to the FortiGate and go to the WiFi & Switch Controller --> FortiLink Interface.
3. Add a FortiGate Port in the FortiLink interface and choose Automatically authorize devices.
4. When the FortiSwitch is online in the WiFi & Switch Controller --> Managed FortiSwitch section, you can now manage your FortiSwitch.

# Cloud Management

1. Visit support.fortinet.com to register your device and cloud management license.
2. Sign in at https://fortiedge.forticloud.com to manage your Inventory List.
---
# FortiSwitch Setup Resources

# Resources

# Cautions and Warnings

# Regulatory Notices

Refer to the following resources to continue your FortiSwitch setup.

# Environmental specifications

- Ambient operating temperature: 0°C to 45°C
- Rack Mount Instructions - The following or similar rack-mount instructions are included with the installation instructions:
- Instructions de montage en rack - Les instructions de montage en rack suivantes ou similaires sont incluses avec les instructions d’installation:

# Federal Communication Commission (FCC) – USA

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions:

1. this device may not cause harmful interference, and
2. this device must accept any interference received; including interference that may cause undesired operation.

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference when the equipment is operated in a commercial environment. This equipment generates, uses, and can radiate radio frequency energy, and if it is not installed and used in accordance with the instruction manual, it may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference, in which case the user will be required to correct the interference at his own expense.

WARNING: Any changes or modifications to this product not expressly approved by the party responsible for compliance could void the user’s authority to operate the equipment.

# Industry Canada Equipment Standard for Digital Equipment (ICES) – Canada

CAN ICES-003 (A) / NMB-003 (A)

This digital apparatus does not exceed the Class A limits for radio noise emissions from digital apparatus set out in the Radio Interference Regulations of the Canadian Department of Communications.

# European Conformity (CE) - EU

This is a Class A product. In a domestic environment, this product may cause radio interference, in which case the user may be required to take adequate measures.

# Voluntary Control Council for Interference (VCCI) – Japan

この装置は、クラスＡ機器です。この装置を住宅環境で使用すると電波妨害を引き起こすことがあります。この場合には使用者が適切な対策を講ずるよう要求されることがあります。

# Product Safety Electrical Appliance & Material (PSE) – Japan

日本では電気用品安全法(PSE)の規定により、同梱している電源コードは本製品の専用電源コードとして利用し、他の製品に使用しないでください。

# Bureau of Standards Metrology and Inspection (BSMI) – Taiwan

The presence conditions of the restricted substance (BSMI RoHS table) are available at the link below:

限用物質含有情況表 (RoHS Table)

For Class A – intended for industrial use such as data centers etc.

# Korea Certification (KC) – Korea

A급 기기 (업무용 방송통신기자재) 이 기기는 업무용(A급) 전자파적합기기로서 판매자 또는 사용자는 이 점을 주의하시기를 바라며, 가정외의 지역에서 사용하는 것을 목적으로 합니다.

# Agência Nacional de Telecomunicações (ANATEL) – Brazil

Este produto não é apropriado para uso em ambientes domésticos, pois poderá causar interferências eletromagnéticas que obrigam o usuário a tomar medidas necessárias para minimizar estas interferências. Para maiores informações, consulte o site da ANATEL http://www.anatel.gov.br

# Fortinet Customer Service & Support

Create a support account, register and manage your products, download updates, firmware images and release notes, and create technical support tickets.

https://support.fortinet.com

# Fortinet Document Library

Up-to-date versions of Fortinet publications for the entire family of Fortinet products.

http://docs.fortinet.com

# Training Services

Course descriptions, availability, schedules, and location of training programs in your area.

http://www.fortinet.com/support/training.html

# Technical Discussion Forums

Communicate with other customers and Fortinet partners about Fortinet products, services, and configuration issues.

https://support.fortinet.com/forum

# FortiGuard Threat Research and Response

Up-to-date information on vulnerabilities and threats, includes a virus scanner, IP signature look-up, and web filtering tools.

http://www.fortiguard.com

# CAUTION: Shock Hazard

Disconnect all power sources.

ATTENTION: Risque d’électrocution. Débranchez toutes les sources d’alimentation.
---
# Technical Documentation

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #333;
}
h1 {
font-size: 2em;
}
h2 {
font-size: 1.5em;
}
h3 {
font-size: 1.2em;
}
h4 {
font-size: 1em;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #ddd;
padding: 8px;
text-align: left;
}
th {
background-color: #f2f2f2;
}

# Technical Documentation

# 1. Introduction

Version: v2.1.3

Build: 5432

# 2. Supported Products

- Model-X
- Product-Y
- Device-Z

# 3. Special Notices

Critical information regarding security vulnerabilities and system requirements.

# 4. Changes

- Updated compatibility for Model-X.
- Improved performance for Product-Y.

# 5. New Features

- Feature A: Description of Feature A.
- Feature B: Description of Feature B.

# 6. Upgrade Information

# 6.1 Upgrade Paths

Upgrade from v2.0.0 to v2.1.3 is recommended.

# 6.2 Upgrade Procedures

Follow the standard upgrade procedure outlined in the manual.

# 7. Integration Details

Integration with third-party applications is supported.

# 8. Issues

# 8.1 Resolved Issues

- Issue ID 101: Fixed bug related to Model-X.
- Issue ID 102: Resolved performance issue in Product-Y.

# 8.2 Known Issues

- Issue ID 201: Known issue with Device-Z.

# 9. Specifications/Limitations

Specifications for Model-X and Product-Y are as follows:

| Model     | Specification                        |
| --------- | ------------------------------------ |
| Model-X   | Specification details for Model-X.   |
| Product-Y | Specification details for Product-Y. |

---
# Technical Documentation


# Introduction

Version: v2.1.3

Build: 5432

# Supported Products

- Model-X
- Product-Y
- Device-Z

# Special Notices

Critical information regarding security vulnerabilities and updates.

# Changes

- Updated user interface for better accessibility.
- Improved performance metrics tracking.

# New Features

- Feature A: Description of Feature A.
- Feature B: Description of Feature B.

# Upgrade Information

# Upgrade Paths

Upgrade from v2.0.0 to v2.1.3 is recommended.

# Upgrade Procedures

Follow the standard upgrade procedure outlined in the user manual.

# Integration Details

Integration with third-party applications is supported.

# Issues

# Resolved Issues

- Issue ID 12345: Fixed login timeout issue.
- Issue ID 67890: Resolved data synchronization error.

# Known Issues

- Issue ID 54321: Occasional UI lag on older devices.
- Issue ID 09876: Compatibility issues with certain browsers.

# Specifications/Limitations

System requirements: Minimum 4GB RAM, 2GHz processor.

Limitations: Not compatible with legacy systems.