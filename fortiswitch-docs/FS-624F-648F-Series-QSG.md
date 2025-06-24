# FortiSwitch 624F/648F Series QuickStart Guide

## Supported Models
- FS-624F
- FS-624F-FPOE
- FS-648F
- FS-648F-FPOE

## Overview
This guide provides a quick start for setting up and configuring the FortiSwitch 624F/648F series switches.
---
# Document Information

## Before You Begin

- **Registration**: Register your device to access FortiGuard updates, cloud management, firmware upgrades, technical support, and warranty coverage.
- **Registration Link**: https://support.fortinet.com

## Document Details

- **Date**: August 21, 2024
- **Models Covered**: 
  - FS-624F
  - FS-624F-FPOE
  - FS-648F
  - FS-648F-FPOE

## Copyright and Legal

- **Copyright**: © 2024 Fortinet, Inc. All rights reserved.
- **Trademarks**: Fortinet®, FortiGate®, FortiGuard®, FortiCare®, and FortiGuard® are registered trademarks of Fortinet, Inc.
- **Jurisdiction**: United States and other jurisdictions.
- **Disclaimer**: Information is provided "as is" without warranty of any kind. Performance and other metrics may vary based on conditions.
- **License Agreement**: For Product License Agreement / EULA and Warranty Terms, visit Fortinet EULA.
---
## The Essentials

### Default Logins
- **URL:** https://192.168.1.99
- **Username:** admin
- **Password:** leave blank

### Fortinet Documents Library
For a detailed Administration Guide, up-to-date Hardware documentation and Reference Manuals, visit Fortinet Documents Library.

### Customer Service
For contracts, licensing, product registration and account management, contact FortiCare Support at FortiCare Support Contact.

### Technical Support
To access our Resource Center, Professional Services and Technical Support Services, visit Fortinet Support.

Thank you for choosing Fortinet.

----

## Package Contents

### FortiSwitch 624F/648F Series
- **Models:** FS-624F, FS-624F-POE, FS-648F, FS-648F-POE

#### Included Items:
- FortiSwitch Device
- QuickStart Guide
- 1x Console Cable (RJ45 to USB)
- 2x Rack Mount Brackets and 2x Rail Stoppers
- 2x Rails w/screws (2x M4x5, 2x M4x8)
- 4x Rubber Feet
- 2x AC Power Cables
---
# Setup Options

Set up your Fortinet device locally or use cloud management mode.

## GUI

1. **Connect to MGMT Port:**
   - Use an Ethernet Cable to connect the MGMT port to a Management Computer.

2. **Access the Device:**
   - Open a web browser and go to `https://192.168.1.99`.
   - Use the credentials:
     - **Username:** admin
     - **Password:** [Your Password]

   **Note:** For static IP configuration, use `192.168.1.1` with subnet mask `255.255.255.0`.

## CLI

1. **Connect to Console Port:**
   - Use a Console Cable to connect the Console Port to a Management Computer.

2. **Configure Connection Settings:**
   - Speed (default): 115200
   - Data bits: 8
   - Stop bits: 1
   - Parity: None
   - Flow Control: None

   **Note:** For a detailed CLI guide, visit docs.fortinet.com.

## Cloud Management

(Connect a port to the Internet)

1. **Register Device:**
   - Visit support.fortinet.com to register your device and cloud management license.

2. **Manage Inventory:**
   - Sign in at https://fortilan.forticloud.com to manage your Inventory List.

## FortiLink

1. **Login to FortiGate:**
   - Go to **WiFi & Switch Controller -> FortiLink Interface**.

2. **Add a FortiGate Port:**
   - In the FortiLink interface, add a FortiGate Port.

3. **Authorize Device:**
   - When the device is discovered, select **Authorize**.

   **Optional:** To automatically authorize the device upon discovery, enable "Automatically authorize devices" in the FortiLink Interface settings.
---
```markdown
# SFP Modules

## Installation

1. Insert the SFP module into the cage socket.
2. Ensure the module is properly aligned with the Tx and Rx ports.

## Removal

1. Unlock the cage socket.
2. Carefully remove the SFP module.

# Rail Installation

1. Install rackmount brackets on the device.
2. Attach rails to the rackmount brackets.
3. Secure rail stoppers using rail stopper screws (2x M4x8 on each side).

### Screws Required

- **Rail Stopper Screws:** 2x M4x8 on each side
- **Rackmount Bracket Screws:** 28x M4x5 (14 on each side)

### Notes

- **Note:** The recommended clearance is 1.5 inches above and below the device.
- **Caution:** To avoid personal injury or damage to the device, it is recommended that two or more people mount the device on a rack.
```
---
## Front FS-624F /-FPOE

### Ports 1 to 24 (RJ45)
- **Green**: Link established at 5Gbps
- **Flashing Green**: 5Gbps data activity
- **Blue**: Link established at 2.5Gbps
- **Flashing Blue**: 2.5Gbps data activity
- **Amber**: Link established at 1000/100/10Mbps
- **Flashing Amber**: 1000/100/10Mbps data activity
- **Off**: No link established

### POE Ports 1 to 24 (RJ45) (FPOE models only)
- **Amber**: Powering a device
- **Off**: Not powering a device

### Ports 25 to 28 (SFP28)
- **Green**: Link established at 25Gbps
- **Flashing Green**: Data activity
- **Amber**: Link established at 10Gbps
- **Flashing Amber**: Data activity
- **Off**: No link established

**Note**: For FPOE models, the default port LED indicates port activity. Use the CLI to set `port-led-mode` to PoE to indicate the port PoE status.

### PWR1
- **Green**: Power is on
- **Amber**: PSU detected, but no AC power
- **Off**: PSU removed

### PWR2
- **Green**: Power is on
- **Amber**: PSU detected, but no AC power
- **Off**: PSU removed

### ALARM
- **Amber**: Alarm detected
- **Off**: No alarm detected

### FAN
- **Green**: Fan operating normally
- **Amber**: Fan alarm detected
- **Off**: Fan is off

### PoE Max (up to 1440W) (FPOE models only)
- **Amber**: Providing Max PoE power
- **Off**: PoE power available

### MGMT (RJ45)
- **Default IP**: 192.168.1.99
- **Green**: Link established
- **Flashing Green**: Data activity

### USB (USB A)
- **USB 2.0 server port**

### Console (RJ45)
- **CLI management port**
---
## Rear FS-624F /-FPOE

### Features

1. **1PPS IN/OUT (SMB)**
   - Pulse per second synchronization ports

2. **Redundant Power Supplies (System Rated per PSU)**
   - **FS-624F:** 100-240VAC, 3A Max, 50-60Hz
   - **FS-624F-FPOE:** 
     - 100-127VAC, 12A Max 
     - 200-240VAC, 6A Max, 50-60Hz
---
```markdown
# Front FS-648F /-FPOE

## Port Descriptions

### 1. Ports 1 to 32 (RJ45)
- **Green**: Link established at 2.5Gbps
- **Flashing Green**: 2.5Gbps data activity
- **Amber**: Link established at 1000/100/10Mbps
- **Flashing Amber**: 1000/100/10Mbps data activity
- **Off**: No link established

### 2. Ports 33 to 48 (RJ45)
- **Green**: Link established at 5Gbps
- **Flashing Green**: 5Gbps data activity
- **Blue**: Link established at 2.5Gbps
- **Flashing Blue**: 2.5Gbps data activity
- **Amber**: Link established at 1000/100/10Mbps
- **Flashing Amber**: 1000/100/10Mbps data activity
- **Off**: No link established

#### POE Ports 1 to 48 (RJ45) - FPOE models only
- **Amber**: Powering a device
- **Off**: Not powering a device

### 3. Ports 49 to 56 (SFP28)
- **Green**: Link established at 25Gbps
- **Flashing Green**: Data activity
- **Amber**: Link established at 10Gbps
- **Flashing Amber**: Data activity
- **Off**: No link established

### Note
For FPOE models, the default port LED indicates port activity. Use the CLI to set `port-led-mode` to PoE to indicate the port PoE status.

## Power and Status Indicators

### 4. Power Supply Units
- **PWR1 & PWR2**
  - **Green**: Power is on
  - **Amber**: PSU detected, but no AC power
  - **Off**: PSU removed

### Alarm
- **Amber**: Alarm detected
- **Off**: No alarm detected

### Fan
- **Green**: Fan operating normally
- **Amber**: Fan alarm detected
- **Off**: Fan is off

### PoE Max (up to 1800W) - FPOE models only
- **Amber**: Providing Max PoE power
- **Off**: PoE power available

## Management and Connectivity

### 5. MGMT (RJ45)
- **Default IP**: 192.168.1.99
- **Green**: Link established
- **Flashing Green**: Data activity
- **Off**: No link established

### USB and Console
- **USB (USB A)**: USB 2.0 server port
- **Console (RJ45)**: CLI management port
```
---
## Rear FS-648F /-FPOE

### Features

1. **1PPS IN/OUT (SMB)**
   - Pulse per second synchronization ports

2. **Redundant Power Supplies (System Rated per PSU)**
   - **FS-648F:** 100-240VAC, 3A Max, 50-60Hz
   - **FS-648F-FPOE:** 
     - 100-127VAC, 12A Max 
     - 200-240VAC, 6A Max, 50-60Hz
---
# Cautions and Warnings

## Environmental Specifications

- **Ambient Operating Temperature:** 0°C to 40°C

### Rack-Mount Instructions
- Follow the instructions included with the installation instructions.
- **Instructions de montage en rack:** Suivez les instructions de montage en rack fournies avec les instructions d'installation.

### Elevated Operating Ambient
- Installation should not exceed the manufacturer's maximum rated ambient temperature.
- **Température ambiante élevée:** L'installation ne doit pas dépasser la température ambiante maximale nominale du fabricant.

### Reduced Air Flow
- Installation should not compromise the equipment's safe operation.
- **Réduction du flux d'air:** L'installation ne doit pas compromettre le fonctionnement sûr de l'équipement.

### Mechanical Loading
- Ensure mechanical stability and avoid hazardous conditions.
- **Charge mécanique:** Assurez-vous de la stabilité mécanique pour éviter des conditions dangereuses.

### Circuit Overloading
- Consider equipment nameplate ratings to prevent overloading.
- **Surcharge de circuit:** Tenez compte des valeurs nominales de la plaque signalétique pour éviter la surcharge.

### Reliable Earthing
- Maintain reliable earthing of the equipment.
- **Mise à la terre fiable:** Assurez une mise à la terre fiable de l'équipement.

## Safety

### Battery
- Risk of explosion if the battery is replaced by an incorrect type.
- **Batterie:** Risque d'explosion si la batterie est remplacée par un type incorrect.

### Laser Safety
- **Laser Class 1:** Complies with IEC 60825-1.
- **Sécurité laser:** Classe 1 conforme à la norme IEC 60825-1.

### Electrical Safety
- Ensure proper grounding and avoid improper wiring.
- **Sécurité électrique:** Assurez une mise à la terre appropriée et évitez un câblage incorrect.

### Usage
- Do not connect directly to communication wiring or other wiring not part of a building's low-voltage power system.
- **Utilisation:** Ne connectez pas directement à un câblage de communication ou à d'autres câblages non partie d'un système de puissance basse tension d'un bâtiment.

### Additional Notes
- Follow all safety instructions and guidelines provided in the manual.
- **Remarques supplémentaires:** Suivez toutes les instructions de sécurité et les directives fournies dans le manuel.
---
```markdown
# Regulatory Notices

## Federal Communication Commission (FCC) – USA
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions:
1. This device may not cause harmful interference, and
2. This device must accept any interference received, including interference that may cause undesired operation.

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference when the equipment is operated in a commercial environment. This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

**WARNING:** Any changes or modifications to this product not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

## Industry Canada Equipment Standard for Digital Equipment (ICES) – Canada
CAN ICES-003 (A) / NMB-003 (A)

Cet appareil numérique de la classe A est conforme à la norme NMB-003 du Canada. Son fonctionnement est soumis aux deux conditions suivantes: (1) cet appareil ne doit pas causer d’interférences nuisibles, et (2) cet appareil doit accepter toute interférence reçue, y compris les interférences pouvant entraîner un fonctionnement indésirable.

## European Conformity (CE) – EU
This is a Class A product. In a domestic environment, this product may cause radio interference, in which case the user may be required to take adequate measures.

![CE Mark]

## Voluntary Control Council for Interference (VCCI) – Japan
この装置は、クラスA情報技術装置です。この装置を家庭環境で使用すると、電波妨害を引き起こすことがあります。この場合には使用者が適切な対策を講ずるよう要求されることがあります。

## Product Safety Electrical Appliance & Material (PSE) – Japan
この装置は電気用品安全法の基準に適合しています。詳細については、製品ラベルをご確認ください。

## Bureau of Standards Metrology and Inspection (BSMI) – Taiwan
The presence conditions of the restricted substance (BSMI RoHS table) are available at the link below:
BSMI RoHS Table

## China
本产品符合中国的相关法律法规要求。

## Agência Nacional de Telecomunicações (ANATEL) – Brazil
Este produto está homologado pela ANATEL, de acordo com os procedimentos regulamentares e atende aos requisitos técnicos aplicados.

----

For models: F5A-F5F-F5H-F5J-F5K
```
---
The image is a blank page with page numbers 22 and 23 at the bottom. There is no content to extract or analyze.
---
The image shows the Fortinet logo with the website URL "Fortinet.com" at the bottom. If you need information about Fortinet products or documentation, you can visit their official website.