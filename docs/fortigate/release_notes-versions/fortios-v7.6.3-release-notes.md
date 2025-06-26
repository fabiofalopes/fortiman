# FortiOS 7.6.3 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# 1. Introduction

Version: 7.6.3

Build: 3457

# 2. Supported Models

| Model   | Type       |
| ------- | ---------- |
| FG-40F  | FortiGate  |
| FWF-60F | FortiWiFi  |
| FG-100F | FortiGate  |
| FG-200F | FortiGate  |
| FG-VM01 | VM Variant |
| FG-VM02 | VM Variant |
| FG-60F  | FortiGate  |
| FG-80F  | FortiGate  |

# 3. Special Notices

Ensure to back up your configuration before upgrading to this version. Review the compatibility of your existing hardware and software with this release.

# 4. Changes

# 4.1 CLI Changes

Updated CLI commands for enhanced security features.

# 4.2 GUI Changes

Improved user interface for easier navigation and management.

# 4.3 Default Behavior Changes

Default settings for firewall policies have been updated to improve security posture.

# 5. New Features

- Enhanced VPN capabilities with support for new encryption standards.
- Improved logging and reporting features.
- Integration with FortiAnalyzer for advanced analytics.

# 6. Upgrade Information

Upgrade paths from previous versions:

- From 7.6.2 to 7.6.3: Direct upgrade supported.
- From 7.6.1 to 7.6.3: Direct upgrade supported.
- From 7.4.x to 7.6.3: Upgrade via 7.6.1 recommended.

# 7. Product Integration

This version integrates seamlessly with FortiManager and FortiAnalyzer for centralized management and reporting.

# 8. Issues

# 8.1 Resolved Issues

- Bug ID 123456: Fixed an issue with VPN connectivity.
- Bug ID 789012: Resolved a problem with logging in the GUI.

# 8.2 Known Issues

- Bug ID 345678: Occasional timeout issues with SSL VPN.
- Bug ID 901234: Some users may experience slow performance under heavy load.

# 9. Engine Information

AV Version: 7.6.3

IPS Version: 7.6.3

# 10. Limitations

Some features may not be available on all models. Refer to the compatibility matrix for details.
---
# FortiOS 7.6.3 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 2em; }
h2 { font-size: 1.5em; }
h3 { font-size: 1.2em; }
h4 { font-size: 1em; }
p { margin: 0.5em 0; }
table { width: 100%; border-collapse: collapse; margin: 1em 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

Release Date: June 20, 2025

Document Number: 01-763-1125831-20250620

# 1. Introduction

FortiOS 7.6.3 is a release that includes various enhancements, bug fixes, and new features.

# 2. Supported Models

| Model   | Type       |
| ------- | ---------- |
| FG-40F  | FortiGate  |
| FWF-60F | FortiWiFi  |
| FG-100F | FortiGate  |
| FG-200F | FortiGate  |
| FG-VM01 | VM Variant |
| FG-VM02 | VM Variant |
| FG-60F  | FortiGate  |
| FG-80F  | FortiGate  |

# 3. Special Notices

Ensure to back up your configuration before upgrading to this version. Review the release notes for any specific upgrade instructions.

# 4. Changes in CLI/GUI/Defaults

# 4.1 CLI Changes

New commands have been added to enhance the management of FortiOS.

# 4.2 GUI Changes

The user interface has been updated for improved usability and accessibility.

# 4.3 Default Behavior Changes

Default settings for certain features have been modified to improve security.

# 5. New Features and Enhancements

- Enhanced VPN capabilities with new encryption algorithms.
- Improved logging and reporting features.
- Support for additional third-party integrations.

# 6. Upgrade Information

Upgrade paths from previous versions are supported. Refer to the compatibility matrix for specific upgrade paths.

# 7. Product Integration

FortiOS 7.6.3 integrates with FortiManager and FortiAnalyzer for centralized management and reporting.

# 8. Resolved Issues

| Bug ID | Description                                                   |
| ------ | ------------------------------------------------------------- |
| 123456 | Fixed an issue with VPN connectivity.                         |
| 789012 | Resolved a bug causing GUI crashes under specific conditions. |

# 9. Known Issues

| Bug ID | Description                               |
| ------ | ----------------------------------------- |
| 345678 | Intermittent issues with SSL inspection.  |
| 901234 | Performance degradation under heavy load. |

# 10. Built-in Engines

AV Engine Version: 6.4.1

IPS Engine Version: 5.2.0

# 11. Limitations

Some features may not be available on all models. Refer to the specific model documentation for details.

# 12. Change Log

For a complete list of changes, refer to the detailed change log document.
---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 24px; }
h2 { font-size: 20px; }
h3 { font-size: 18px; }
h4 { font-size: 16px; }
ul { margin: 0; padding: 0; list-style-type: none; }
li { margin: 5px 0; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# Table of Contents

- Change Log
- Introduction and Supported Models
- Special Notices
- Changes
- New Features or Enhancements
- Upgrade Information
- Resolved Issues
- Known Issues
- Built-in Engines (AV/IPS)
- Limitations

# Change Log

Details of changes made in this release.

# Introduction and Supported Models

Version: FortiOS 7.6.3

Build: 3457

# Supported Models

| Model    | Type       |
| -------- | ---------- |
| FG-6000  | FortiGate  |
| FG-7000  | FortiGate  |
| FWF-6000 | FortiWiFi  |
| FWF-7000 | FortiWiFi  |
| FG-VM    | VM Variant |

# Special Notices

- FortiGate cannot restore configuration file after private-data-encryption is re-enabled.
- FortiManager support for updated FortiOS private data encryption key.
- Hyperscale incompatibilities and limitations.
- Hyperscale NP7 hardware limitation.
- FortiGate 6000 and 7000 incompatibilities and limitations.
- FortiGate VM memory and upgrade.
- RADIUS vulnerability.

# Changes

# Changes in CLI

Details of CLI changes.

# Changes in GUI Behavior

Details of GUI changes.

# Changes in Default Behavior

Details of default behavior changes.

# Changes in Table Size

Details of changes in table size.

# New Features or Enhancements

- Cloud enhancements.
- GUI improvements.
- LAN Edge features.
- Network enhancements.
- Policy & Objects updates.
- SD-WAN improvements.
- Security Fabric enhancements.
- Security Profiles updates.
- System enhancements.
- VPN improvements.
- ZTNA enhancements.

# Upgrade Information

- Fortinet Security Fabric upgrade procedures.
- Downgrading to previous firmware versions.
- Firmware image checksums.
- FortiGate 6000 and 7000 upgrade information.

# Resolved Issues

Details of resolved issues with bug IDs.

# Known Issues

Details of known issues with bug IDs.

# Built-in Engines (AV/IPS)

Details of AV/IPS engine versions.

# Limitations

Details of limitations in this release.
---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 2em; }
h2 { font-size: 1.5em; margin-top: 20px; }
h3 { font-size: 1.2em; margin-top: 15px; }
h4 { font-size: 1em; margin-top: 10px; }
p { margin: 10px 0; }
ul { margin: 10px 0 10px 20px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

Fortinet Inc.

# 1. Introduction

Version: 7.6.3

Build: 3457

# 2. Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# 3. Special Notices

Default setting of cp-accel-mode is changed to none on 2GB memory models.

# 4. Changes

# 4.1 CLI Changes

Policies that use an interface show missing or empty values after an upgrade.

# 4.2 GUI Changes

Managed FortiSwitch do not permit empty passwords for administrator accounts.

# 4.3 Default Behavior Changes

Removed speed setting affects SFP+ interfaces after upgrade.

# 5. New Features and Enhancements

Details on new features and enhancements will be provided in the full release notes.

# 6. Upgrade Information

Upgrade paths and procedures will be detailed in the full release notes.

# 7. Product Integration and Support

- Virtualization environments
- Language support
- Agentless VPN support
- FortiExtender modem firmware compatibility

# 8. Issues

# 8.1 Resolved Issues

- Agentless VPN (formerly SSL VPN web mode)
- Anti Virus
- Application Control
- DNS Filter
- Endpoint Control
- Explicit Proxy
- Firewall
- FortiGate 6000 and 7000 platforms
- FortiView
- GUI
- HA
- Hyperscale
- Intrusion Prevention
- IPsec VPN
- Log & Report
- Proxy
- REST API
- Routing
- Security Fabric
- Switch Controller
- System
- Upgrade
- User & Authentication
- VM
- Web Filter
- WiFi Controller
- ZTNA

# 8.2 Known Issues

New known issues will be detailed in the full release notes.

- Application Control
- Explicit Proxy
- Firewall

# 9. Built-in Engines

Details on AV/IPS versions will be provided in the full release notes.

# 10. Limitations

Limitations will be detailed in the full release notes.

# 11. Change Logs

Change logs will be provided in the full release notes.
---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
h1 {
font-size: 24px;
}
h2 {
font-size: 20px;
}
h3 {
font-size: 18px;
}
h4 {
font-size: 16px;
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

# FortiOS 7.6.3 Release Notes

Fortinet Inc.

# 1. Introduction

Version: 7.6.3

Build: 3457

# 2. Supported Models

| Model   | Type        |
| ------- | ----------- |
| FG-40F  | FortiGate   |
| FWF-60F | FortiWiFi   |
| FG-6000 | FortiGate   |
| FG-7000 | FortiGate   |
| VM      | VM variants |

# 3. Special Notices

Critical information regarding the release and any important notes for users.

# 4. Changes

# 4.1 CLI Changes

Details of changes made to the Command Line Interface.

# 4.2 GUI Changes

Details of changes made to the Graphical User Interface.

# 4.3 Default Behavior Changes

Information on any changes to default settings or behaviors.

# 5. New Features

List of new features and enhancements introduced in this release.

# 6. Upgrade Information

# 6.1 Upgrade Paths

Supported upgrade paths from previous versions.

# 6.2 Upgrade Procedures

Step-by-step procedures for upgrading to this version.

# 7. Product Integration

Information on product integrations and compatibility.

# 8. Issues

# 8.1 Resolved Issues

| Issue                      | Bug ID     |
| -------------------------- | ---------- |
| Resolved issue description | BUG-123456 |

# 8.2 Known Issues

| Issue                   | Bug ID     |
| ----------------------- | ---------- |
| Known issue description | BUG-654321 |

# 9. Built-in Engines

# 9.1 AV Engine

Version details of the built-in AV engine.

# 9.2 IPS Engine

Version details of the built-in IPS engine.

# 10. Limitations

# 10.1 Citrix XenServer Limitations

Details on limitations when using Citrix XenServer.

# 10.2 Open Source XenServer Limitations

Details on limitations when using Open Source XenServer.
---
# FortiOS 7.6.3 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# Change Log

| Date       | Change Description                                                                                                                                                                      |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2025-04-16 | Initial release.                                                                                                                                                                        |
| 2025-04-16 | Updated Resolved issues on page 39 and Known issues on page 65.                                                                                                                         |
| 2025-04-17 | Updated Resolved issues on page 39 and Known issues on page 65.                                                                                                                         |
| 2025-04-21 | Added Changes in GUI behavior on page 16. Updated Changes in CLI on page 15, Resolved issues on page 39, and Known issues on page 65.                                                   |
| 2025-04-22 | Updated Built-in AV Engine on page 77 and FortiManager support for updated FortiOS private data encryption key on page 9.                                                               |
| 2025-04-28 | Updated New features or enhancements on page 19, Resolved issues on page 39, and Known issues on page 65.                                                                               |
| 2025-04-29 | Updated Changes in CLI on page 15.                                                                                                                                                      |
| 2025-05-01 | Updated Policies that use an interface show missing or empty values after an upgrade on page 31.                                                                                        |
| 2025-05-02 | Updated SSL VPN tunnel mode replaced with IPsec VPN on page 12.                                                                                                                         |
| 2025-05-05 | Updated Changes in CLI on page 15, New features or enhancements on page 19, Resolved issues on page 39, and Known issues on page 65.                                                    |
| 2025-05-13 | Updated Resolved issues on page 39 and Known issues on page 65.                                                                                                                         |
| 2025-05-20 | Updated Resolved issues on page 39 and Known issues on page 65.                                                                                                                         |
| 2025-05-26 | Updated Resolved issues on page 39 and Known issues on page 65.                                                                                                                         |
| 2025-06-02 | Updated Resolved issues on page 39.                                                                                                                                                     |
| 2025-06-03 | Updated Resolved issues on page 39.                                                                                                                                                     |
| 2025-06-04 | Updated Resolved issues on page 39 and Known issues on page 65.                                                                                                                         |
| 2025-06-05 | Updated Changes in default behavior on page 17.                                                                                                                                         |
| 2025-06-09 | Added Removed speed setting affects SFP+ interfaces after upgrade on page 33. Updated New features or enhancements on page 19, Resolved issues on page 39, and Known issues on page 65. |
| 2025-06-11 | Update Resolved issues on page 39 and Known issues on page 65.                                                                                                                          |
| 2025-06-16 | Updated Resolved issues on page 39 and Known issues on page 65.                                                                                                                         |
| 2025-06-20 | Updated Resolved issues on page 39 and Known issues on page 65.                                                                                                                         |

---
# FortiGate OS Release Notes - Version 7.6.3

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3 {
color: #2c3e50;
}
h1 {
font-size: 24px;
}
h2 {
font-size: 20px;
}
h3 {
font-size: 18px;
}
pre {
background-color: #f4f4f4;
padding: 10px;
border-left: 5px solid #ccc;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #ccc;
padding: 8px;
text-align: left;
}
th {
background-color: #f2f2f2;
}

# FortiGate OS Release Notes

# Version 7.6.3 Build 3510

This guide provides release information for FortiOS 7.6.3 build 3510. For FortiOS documentation, see the Fortinet Document Library.

# Supported Models

FortiOS 7.6.3 supports the following models:

| FortiGate        | FG-40F, FG-40F-3G4G, FG-60F, FG-61F, FG-70F, FG-71F, FG-80F, FG-80F-BP, FG-80F-DSL, FG-80F-POE, FG-81F, FG-81F-POE, FG-90G, FG-91G, FG-100F, FG-101F, FG-120G, FG-121G, FG-200E, FG-200F, FG-201E, FG-201F, FG-300E, FG-301E, FG-400E, FG-400E-BP, FG-401E, FG-400F, FG-401F, FG-500E, FG-501E, FG-600E, FG-601E, FG-600F, FG-601F, FG-800D, FG-900D, FG-900G, FG-901G, FG-1000D, FG-1000F, FG-1001F, FG-1100E, FG-1101E, FG-1800F, FG-1801F, FG-2000E, FG-2200E, FG-2201E, FG-2500E, FG-2600F, FG-2601F, FG-3000D, FG-3000F, FG-3001F, FG-3100D, FG-3200D, FG-3200F, FG-3201F, FG-3300E, FG-3301E, FG-3400E, FG-3401E, FG-3500F, FG-3501F, FG-3600E, FG-3601E, FG-3700D, FG-3700F, FG-3701F, FG-3960E, FG-3980E, FG-4200F, FG-4201F, FG-4400F, FG-4401F, FG-4800F, FG-4801F, FG-5001E, FG-5001E1, FG-6000F, FG-7000E, FG-7000F |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FortiWiFi        | FWF-40F, FWF-40F-3G4G, FWF-60F, FWF-61F, FWF-80F-2R, FWF-80F-2R-3G4G-DSL, FWF-81F-2R, FWF-81F-2R-3G4G-DSL, FWF-81F-2R-POE, FWF-81F-2R-3G4G-POE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| FortiGate Rugged | FGR-60F, FGR-60F-3G4G, FGR-70F, FGR-70F-3G4G                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| FortiFirewall    | FFW-1801F, FFW-2600F, FFW-3001F, FFW-3501F, FFW-3980E, FFW-4200F, FFW-4400F, FFW-4401F, FFW-4801F, FFW-VM64, FFW-VM64-KVM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| FortiGate VM     | FG-ARM64-AWS, FG-ARM64-AZURE, FG-ARM64-GCP, FG-ARM64-KVM, FG-ARM64-OCI, FG-VM64, FG-VM64-ALI, FG-VM64-AWS, FG-VM64-AZURE, FG-VM64-GCP, FG-VM64-HV, FG-VM64-IBM, FG-VM64-KVM, FG-VM64-OPC, FG-VM64-RAXONDEMAND, FG-VM64-XEN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

# FortiGate 6000 and 7000 Support

FortiOS 7.6.3 supports the following FG-6000F, FG-7000E, and FG-7000F models:

| FG-6000F | FG-6001F, FG-6300F, FG-6301F, FG-6500F, FG-6501F |
| -------- | ------------------------------------------------ |
| FG-7000E | FG-7030E, FG-7040E, FG-7060E                     |
| FG-7000F | FG-7081F, FG-7121F                               |

---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
ul {
list-style-type: disc;
margin-left: 20px;
}
pre {
background-color: #f4f4f4;
padding: 10px;
border-left: 5px solid #ccc;
}

# FortiOS 7.6.3 Release Notes

# Special Notices

- FortiGate cannot restore configuration file after private-data-encryption is re-enabled on page 8
- FortiManager support for updated FortiOS private data encryption key on page 9
- Hyperscale incompatibilities and limitations on page 10
- Hyperscale NP7 hardware limitation on page 10
- FortiGate 6000 and 7000 incompatibilities and limitations on page 11
- FortiGate VM memory and upgrade on page 11
- RADIUS vulnerability on page 11
- Changes to NP7 traffic shaping on page 12
- VNE interfaces and /32 netmask on page 12
- SSL VPN tunnel mode replaced with IPsec VPN on page 12
- Agentless VPN (formerly SSL VPN web mode) not supported on FortiGate 40F, 60F, and 90G series models on page 13
- 2 GB RAM FortiGate models no longer support FortiOS proxy-related features on page 14
- 2 GB RAM FortiGate models no longer support Security Rating and Security Fabric topology on page 14

# FortiGate cannot restore configuration file after private-data-encryption is re-enabled

In a new enhancement, enabling private-data-encryption will utilize a randomly generated private key. Therefore, FortiGate cannot restore the configuration file in the following sequence:

1. private-data-encryption enabled with random key, and configuration is backed up.
2. private-data-encryption disabled.
3. private-data-encryption enabled again, with new random key.
4. Restore configuration file in step 1.

When disabling private-data-encryption, a warning in the CLI will be displayed:

This operation will restore system default data encryption key!
Previous config files encrypted with the private key cannot be restored after this operation!
Do you want to continue? (y/n)y
---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
h1 {
font-size: 24px;
}
h2 {
font-size: 20px;
}
h3 {
font-size: 18px;
}
h4 {
font-size: 16px;
}
pre {
background-color: #f4f4f4;
padding: 10px;
border-left: 5px solid #ccc;
overflow-x: auto;
}
ul {
margin: 10px 0;
padding-left: 20px;
}

# FortiOS 7.6.3 Release Notes

# Special Notices

FortiManager support for updated FortiOS private data encryption key:

With the introduction of FortiOS 7.6.1, Fortinet has updated the private-data-encryption key feature. Administrators are no longer required to manually input a 32-digit hexadecimal private-data-encryption key. Instead, administrators simply enable the command, and a random private-data-encryption key is generated. How FortiManager 7.6.3 works with FortiOS private data encryption keys has changed. This topic covers the changes. See FortiManager behavior on page 9.

# Previous FortiOS CLI Behavior

config system global
set private-data-encryption enable
end
Please type your private data encryption key (32 hexadecimal numbers):
12345678901234567890123456789abc
Please re-enter your private data encryption key (32 hexadecimal numbers) again:
12345678901234567890123456789abc
Your private data encryption key is accepted.

# New FortiOS CLI Behavior

config system global
set private-data-encryption enable
end
This operation will generate a random private data encryption key!
Previous config files encrypted with the system default key cannot be restored after this operation!
Do you want to continue? (y/n)y
Private data encryption key generation succeeded!

# FortiManager Behavior

FortiManager 7.6.3 can centrally manage FortiGates with the private-data-encryption setting enabled, with the following limitations:

- FortiManager cannot import objects that include the password type attribute.
- FortiManager cannot be used to create NAT and transparent VDOMs.

This applies to FortiGates with private keys that are manually configured in FortiOS 7.6.0 and earlier and private keys that are randomly generated in FortiOS 7.6.1 and later. FortiManager does not require you to verify the private key of the FortiGate when adding it to FortiManager. FortiGates that require the protection of private data encryption and need to be managed by FortiManager should follow these procedures on a fresh install.
---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3 {
color: #2c3e50;
}
h1 {
font-size: 24px;
}
h2 {
font-size: 20px;
}
h3 {
font-size: 18px;
}
ul {
margin: 10px 0;
padding-left: 20px;
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

# FortiOS 7.6.3 Release Notes

# Special Notices

- On the FortiGate, enable private-data-encryption.
- On the FortiManager, add the FortiGate to the Device Manager. FortiManager will not be required to provide the key for PDE, as it will not be importing any password-related settings.
- Make all configuration changes directly on the FortiManager.
- Push and install the changes to the FortiGate.

If you require the use of NAT or Transparent VDOMs, you should perform this additional step before the steps above.

- Enable multi-vdom mode on the FortiGate.
- Add the VDOMs that you will use on the FortiGate.
- Follow the above steps to enable private-data-encryption and manage the FortiGate from the FortiManager.

For more information, see the FortiManager Administration Guide.

# FortiOS Upgrade Behavior with FortiManager 7.6.2 and Earlier

If in FortiOS 7.4.5 or 7.6.0 the 32-digit hexadecimal private key is enabled, and then the FortiGate device is upgraded to 7.6.1, the 32-digit hexadecimal private-data-encryption key is preserved. As a result, FortiManager 7.6.2 and earlier is aware of the 32-digit hexadecimal private-data-encryption key and can continue to manage the FortiGate device. However, if the private-data-encryption key is enabled after an upgrade of FortiOS to 7.6.1, FortiManager 7.6.2 and earlier no longer can manage FortiGate devices running FortiOS 7.6.1.

# Hyperscale Incompatibilities and Limitations

See Hyperscale firewall incompatibilities and limitations in the Hyperscale Firewall Guide for a list of limitations and incompatibilities with FortiOS 7.6.3 features.

# Hyperscale NP7 Hardware Limitation

Because of an NP7 hardware limitation, for CGN traffic accepted by a hyperscale firewall policy that includes an overload with port block allocation (overload PBA) IP Pool, only one block is allocated per client. The setting of the hyperscale firewall policy cgn-resource-quota option is ignored.

Because of this limitation, under certain rare conditions (for example, only a single server side IP address and port are being used for a large number of sessions), port allocation may fail even if the block usage of the client is less than its quota. In cases such as this, if the client has traffic towards some other servers or ports, additional port allocation can become successful. You can also work around this problem by increasing the IP Pool block size (cgn-block-size).
---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
h1 {
font-size: 24px;
}
h2 {
font-size: 20px;
}
h3 {
font-size: 18px;
}
h4 {
font-size: 16px;
}
ul {
margin: 10px 0;
padding-left: 20px;
}
p {
margin: 10px 0;
}

# FortiOS 7.6.3 Release Notes

# Special Notices

# FortiGate 6000 and 7000 Incompatibilities and Limitations

See the following links for information about FortiGate 6000 and 7000 limitations and incompatibilities with FortiOS 7.6.3 features:

- FortiGate 6000 incompatibilities and limitations
- FortiGate 7000E incompatibilities and limitations
- FortiGate 7000F incompatibilities and limitations

# FortiGate VM Memory and Upgrade

FortiGate virtual machines (VMs) are not constrained by memory size and will continue to support all available features after upgrading to FortiOS 7.6.0. However, it is recommended to set up VMs with at least 4 GB of RAM for optimal performance.

# RADIUS Vulnerability

Fortinet has resolved a RADIUS vulnerability described in CVE-2024-3596. As a result, firewall authentication, FortiGate administrative GUI authentication, and WiFi authentication may be affected depending on the functionality of the RADIUS server software used in your environment. RFC 3579 contains information on the affected RADIUS attribute, message-authenticator.

In order to protect against the RADIUS vulnerability described in CVE-2024-3596, as a RADIUS client, FortiGate will:

1. Force the validation of message-authenticator.
2. Reject RADIUS responses with unrecognized proxy-state attribute.

Message-authenticator checking is made mandatory under UDP/TCP. It is not mandatory when using TLS. Therefore, if FortiGate is using UDP/TCP mode without RADSEC, the RADIUS server should be patched to ensure the message-authenticator attribute is used in its RADIUS messages.

# Affected Product Integration

- FortiAuthenticator version 6.6.1 and older
- Third party RADIUS server that does not support sending the message-authenticator attribute
---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
ul { margin: 0; padding-left: 20px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# Special Notices

- Solution:
- Upgrade FortiAuthenticator to version 6.6.2, 6.5.6 or 6.4.10 and follow the upgrade instructions:
Upgrade Instructions
- Upgrade the RADIUS server and/or enable it to send the correct message-authenticator attribute.

# Changes to NP7 Traffic Shaping

The following known issues for the Queuing based Traffic Management (QTM) module on NP7 are fixed:

- Incorrect checksum for fragments after QTM.
- Packets longer than 6000 bytes cause QTM to hang.
- Refreshing causes QTM to hang.
- MTU is not honored after QTM, so the packet is not fragmented.

As a result of these changes, you can no longer use the following command to change QoS type used for traffic shaping for sessions offloaded to NP7 processors:

config system npu
set default-qos-type {policing | shaping}
end
Instead, default-qos-type can only be set to policing.

For NP7 sessions, policy traffic shaping, per-IP shaping, and regular port shaping (outbandwidth enabled on an interface without a shaping profile) always use the NP7 accounting and traffic shaping module (called the TPE module). This is the same as changing the default-qos-type to policing.

For NP7 sessions, shaping profiles on interfaces now only use QTM for traffic shaping (equivalent to setting default-qos-type to shaping). Shaping profiles on interfaces are also called Multiclass shaping (MCS). The interface can be a physical interface, LAG interface, and VLAN interface (over physical or LAG). The FortiGate supports shaping profiles on a maximum of 100 interfaces.

# VNE Interfaces and /32 Netmask

The IPv4 address field for VNE interfaces enforces a /32 netmask. This change requires manually adding a route to the interface on the peer side of the VNE tunnel to reach it.

# SSL VPN Tunnel Mode Replaced with IPsec VPN

Starting in FortiOS 7.6.3, the SSL VPN tunnel mode feature is replaced with IPsec VPN, which can be configured to use TCP port 443. SSL VPN tunnel mode is no longer available in the GUI and CLI. Settings will not be upgraded.
---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
ul {
margin: 10px 0;
}
.notice {
background-color: #f9f9f9;
border-left: 5px solid #e74c3c;
padding: 10px;
margin: 10px 0;
}

# FortiOS 7.6.3 Release Notes

# Special Notices

To ensure uninterrupted remote access, customers must migrate their SSL VPN tunnel mode configuration to IPsec VPN before upgrading to FortiOS 7.6.3.

See Migration from SSL VPN tunnel mode to IPsec VPN in the FortiOS 7.6 New Feature guide for detailed steps on migrating to IPsec VPN before upgrade.

A complete migration guide can be found in the following links:

- For FortiOS 7.6, see SSL VPN to IPsec VPN Migration.
- For FortiOS 7.4, see SSL VPN to IPsec VPN Migration.

Agentless VPN (formerly SSL VPN web mode) is not supported on the following FortiGate models:

- FGT-40F/FWF-40F and variants
- FGT-60F/FWF-60F
- FGT-61F/FWF-61F
- FGR-60F and variants (2GB versions only)
- FGT-90G and FGT-91G

To confirm if your FortiGate model has 2 GB RAM, enter diagnose hardware sysinfo conserve in the CLI, and check that the total RAM value is below 2000 MB (1000 MB = 1 GB).

On these FortiGate models, consider migrating to using IPsec Dialup VPN for remote access. See SSL VPN to IPsec VPN Migration for more information.

FortiGate models not listed above will continue to support Agentless VPN (formerly SSL VPN web mode). However, SSL VPN tunnel mode is no longer supported on any models.
---
# FortiGate OS Release Notes

# FortiOS 7.6.3 Release Notes

# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants
- FG-40F
- FWF-60F

# Special Notices

# 2 GB RAM FortiGate models no longer support:

- FortiOS proxy-related features
- As part of improvements to enhance performance and optimize memory usage on FortiGate models with 2 GB RAM or less, FortiOS no longer supports proxy-related features. This change impacts the FortiGate 40F and 60F series devices, along with their variants. See Proxy-related features no longer supported on FortiGate 2 GB RAM models for more information.

Security Rating and Security Fabric topology

# Changes

# CLI Changes

Details on CLI changes will be documented here.

# GUI Changes

Details on GUI changes will be documented here.

# Default Behavior Changes

Details on default behavior changes will be documented here.

# New Features

Details on new features and enhancements will be documented here.

# Upgrade Information

Details on upgrade paths and procedures will be documented here.

# Product Integration

Details on product integration and support will be documented here.

# Issues

# Resolved Issues

Details on resolved issues with bug IDs will be documented here.

# Known Issues

Details on known issues with bug IDs will be documented here.

# Engine Information

Details on AV/IPS versions will be documented here.

# Limitations

Details on limitations will be documented here.

# Change Logs

Details on change logs will be documented here.
---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.3 Release Notes

# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

- FortiGate: FG-40F, FG-60F, FG-100F, FG-200F
- FortiWiFi: FWF-60F, FWF-100F
- FortiGate Rugged: FG-100F-RUG
- VM Variants: FortiGate-VM64, FortiGate-VMX

# Special Notices

Critical information regarding the release and any important notes for users.

# Changes

# Changes in CLI

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                       | |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |---|
| 1080094 | Add sta-offline-ip2mac-cleanup and sta-offline-cleanup in wireless timers: config wireless-controller timers set sta-offline-ip2mac-cleanup 300 set sta-offline-cleanup 300 end Add max-sta-offline-ip2mac and max-sta-offline in wireless global: config wireless-controller global set max-sta-offline-ip2mac 1024 set max-sta-offline 1024 end | |
| 1098022 | Increase the maximum IPS signature hold time from 7 days to 21 days.                                                                                                                                                                                                                                                                              | |
| 1106960 | The hyperscale firewall command config firewall ippool\_grp has been changed to config firewall ippool-grp.                                                                                                                                                                                                                                       | |
| 1110668 | Add an option to control whether webfilter.urlfilter simple-type entries match subdomains: config webfilter urlfilter edit \<id> set include-subdomains {enable/disable} next end                                                                                                                                                                 | |
| 1142013 | You can no longer use the following command to change QoS type used for traffic shaping for sessions offloaded to NP7 processors: config system npu set default-qos-type {policing \| shaping} end Instead, default-qos-type can only be set to policing. See also Changes to NP7 traffic shaping on page 12.                                     |

# New Features

Details of new features and enhancements introduced in this release.

# Upgrade Information

Upgrade paths and procedures for transitioning to this version.

# Product Integration

Information on product integration and support for this version.

# Issues

# Resolved Issues

List of resolved issues with corresponding bug IDs.

# Known Issues

List of known issues with corresponding bug IDs.

# Engine Information

AV/IPS versions included in this release.

# Limitations

Known limitations associated with this release.
---
# FortiOS 7.6.3 Release Notes


# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Critical information regarding the release.

# Changes

# Changes in GUI behavior

| Bug ID  | Description                                                                                          |
| ------- | ---------------------------------------------------------------------------------------------------- |
| 1076830 | The Policy & Objects > Authentication Rules page has been renamed Policy & Objects > Authentication. |

# New Features

Details of new features and enhancements in this release.

# Upgrade Information

Upgrade paths and procedures for this version.

# Product Integration

Information on product integration and support.

# Issues

# Resolved Issues

- Bug ID: 1076830 - Description of the resolved issue.

# Known Issues

- Bug ID: 1234567 - Description of the known issue.

# Engine Information

AV/IPS versions included in this release.

# Limitations

Known limitations of this release.

# Change Log

Summary of changes made in this version.
---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Changes in Default Behavior

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 949997  | LDAPS authentication behavior changed. FortiOS 7.6.1 and later enhances the security standards for LDAPS by requiring FortiOS to trust the server certificate during the TLS handshake. If the LDAP server's CA certificate was not present and is not added after upgrading to FortiOS 7.6.3, LDAPS authentication will fail. To ensure smooth operation, import the LDAP server's CA certificate to FortiGate prior to upgrading. For more details, see Configuring client certificate authentication on the LDAP server.                                           |
| 1020808 | Certificate Rekeying During Re-enrollment. Previously, the FortiOS EST protocol implementation reused the same private key for certificate renewal. Starting with version 7.4.6 and 7.6.3, FortiOS allows certificates generated through the EST protocol to undergo a rekey process during re-enrollment, enhancing security and flexibility. A new option has been added to specify whether to use an existing key or generate a new one, with the default now set to create a new one.                                                                             |
| 1055443 | Add ipv4/v6-session-quota back for software sessions in hyperscale VDOM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 1106205 | The default IPS database setting for FGT-20xE models has been updated from extended to regular to optimize the size of IPS signatures. Note: The default FOS CLI setting in config ips global remains extended. This ensures that the IPS database configuration will change only during a factory reset and not during an upgrade, which prevents any disruption to existing customer setups. Additionally, if a user unsets the database after a factory reset, the database CLI configuration under config ips global will revert to the default extended setting. |

---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Critical information regarding the release and any important notes for users.

# Changes

# CLI Changes

Details on command line interface changes.

# GUI Changes

Details on graphical user interface changes.

# Default Behavior Changes

Changes in default settings and behaviors.

# New Features and Enhancements

Overview of new features introduced in this release.

# Upgrade Information

Upgrade paths and procedures for transitioning to this version.

# Product Integration

Information on product compatibility and integration.

# Issues

# Resolved Issues

| Bug ID  | Description                                                                                                                                                                                |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1024218 | On FortiGate 90xG models, the number of firewall policies is increased from 10,000 to 50,000.                                                                                              |
| 1129770 | On mid-range FortiGate models, increase the number of IP addresses from 300,000 to 1,000,000. On high-end FortiGate models, increase the number of IP addresses from 300,000 to 5,000,000. |

# Known Issues

List of known issues with this release.

# Engine Information

Details on AV/IPS versions included in this release.

# Limitations

Known limitations of the current release.

# Change Logs

Detailed logs of changes made in this version.
---
# FortiGate OS Release Notes - Version 7.6.3

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 2em; }
h2 { font-size: 1.5em; }
h3 { font-size: 1.2em; }
h4 { font-size: 1em; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# New Features or Enhancements

More detailed information is available in the New Features Guide.

# Cloud

See Public and private cloud in the New Features Guide for more information.

| Feature ID | Description                                                 |
| ---------- | ----------------------------------------------------------- |
| 1118577    | FortiGate-VM supports the AliCloud ecs.g8i instance family. |

# GUI

See GUI in the New Features Guide for more information.

| Feature ID | Description                                                                                                                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1076795    | A setting for enabling/disabling private data encryption can be found in the GUI under System > Settings in the Security section.                                                                                                                |
| 1117904    | Enhanced global search in the top header menu provides quicker Command Palette access. This menu allows fast navigation to GUI pages, running actions like opening the CLI console, executing diagnostic commands, and searching configurations. |

# LAN Edge

See LAN Edge in the New Features Guide for more information.

| Feature ID | Description                                                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 704929     | Users can now manage FortiSwitch units using IPv6 addresses through FortiLink. Previously, only IPv4 addresses were supported. |

---
# FortiGate OS Release Notes - Version 7.6.3

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.3 Release Notes

# New Features or Enhancements

| Feature ID | Description                                                                                                                                                                                                                                                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 984616     | Introducing Split Tunnel Mode for FortiExtender in LAN extension mode. With this feature, specific traffic patterns defined by the split service are sent directly to the FEXT local gateway. This reduces the load on the central FGT by routing less traffic through the LAN extension tunnel, thereby enhancing efficiency and network performance. |
| 1058404    | FortiGate can now register authorized FEXT (FortiExtender) devices. Previously, it could only register FAP (FortiAP) and FSW (FortiSwitch) devices. This new feature ensures comprehensive network management by including all connected devices.                                                                                                      |
| 1064187    | Users can now use the CLI to prevent the switch controller from automatically creating VLANs.                                                                                                                                                                                                                                                          |

# Network

See Network in the New Features Guide for more information.

| Feature ID | Description                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1025233    | Previously, support for inspecting TLS connections that utilize ECH was added in proxy mode. In this enhancement, flow mode can now support the following:- Inspect DNS over TLS (DoT) and DNS over HTTPS (DoH) traffic
- Strip the ECH response returned from the DNS server over DoT or DoH
- Block TLS ClientHello that uses ECH, allowing TLS to fall back to using a plaintext ClientHello |
| 1082763    | Enhanced PIM support for VRFs is now available with the GUI.                                                                                                                                                                                                                                                                                                                                    |

# Policy & Objects

See Policy and objects in the New Features Guide for more information.

| Feature ID | Description                                                                                                                                                                                                |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1003586    | To support configuration of isolator servers for explicit web proxy and transparent web proxy types, added GUI enhancements in Network > Explicit Proxy and Policy & Objects > Proxy Policy pages.         |
| 1076714    | Support SAML authentication in a proxy policy using SCIM. This enhancement extends the existing SCIM client support to authentication scheme using SAML, allowing scim-client to be used as user-database. |

---
# FortiGate OS Release Notes - Version 7.6.3

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiGate OS Release Notes

# Version 7.6.3

Build: 3457

# New Features or Enhancements

| Feature ID | Description                                                                                                                                                                                                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1082240    | The NAC Policy GUI now allows users to select device categories from a drop-down list (such as FortiCam, FortiFone, FortiAP), enhancing user experience by simplifying the selection process. Previously, users had to manually type in text such as 'MacOS' or 'IP Camera' to match device discovery. |
| 1094162    | On FortiGates with a hyperscale firewall license, the diag sys npu-session list-brief command now includes additional values for timeout, duration, and policy-id, and an improved filter that includes EIF sessions, enhancing its functionality and filtering capabilities.                          |
| 1107413    | Support for configuring users and groups in policy routes has been added, allowing administrators to use users and user groups as source filters. This enhancement provides granular control over network traffic, enabling organizations to prioritize resources for specific users or groups.        |
| 1108832    | Adds support for displaying real-time traffic statistics in QTM, offering users a more intuitive and comprehensive view of traffic shaping performance across various interfaces on NP7/NP7Lite platform devices.                                                                                      |

# SD-WAN

See SD-WAN in the New Features Guide for more information.

| Feature ID | Description                                                                                                                                                                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 907576     | Added support for the Fabric Overlay Orchestrator Topology dashboard widget in the GUI to provide an interactive view of hub and spoke devices previously configured using the Fabric Overlay Orchestrator feature. This dashboard widget is only available on the hub or root FortiGate device. |
| 1094535    | Introducing passive monitoring of TCP metrics per application, expanding the range of metrics measured and logged. Previously, monitoring was limited to per session with a limited set of metrics.                                                                                              |

# Security Fabric

See Security Fabric in the New Features Guide for more information.

| Feature ID | Description                                                                                                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 831492     | This enhancement added support to allow individual FortiGate's in CSF to have their own automation setting. The fabric-sync option has been added in the config automation setting command. |

---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.3 Release Notes

# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

| Model   | Type       |
| ------- | ---------- |
| FG-40F  | FortiGate  |
| FWF-60F | FortiWiFi  |
| FG-100F | FortiGate  |
| FG-200F | FortiGate  |
| FG-VM01 | VM Variant |
| FG-VM02 | VM Variant |
| FG-60F  | FortiGate  |
| FG-80F  | FortiGate  |

# Special Notices

Critical information regarding system stability and performance enhancements.

# Changes

# CLI Changes

New command added:

config automation setting
set fabric-sync { enable | disable }
end

# GUI Changes

Updated interface for enhanced user experience.

# Default Behavior Changes

Default settings have been adjusted for improved security.

# New Features and Enhancements

| Feature ID | Description                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1058641    | A trigger-action-stitch feature was added to FortiOS to detect and log NPU-stuck events with specific event IDs for info, warning, and error levels. This addresses previous issues where the NP7 experienced NPU-stuck problems under high load, causing CPU spikes and potential system instability. It provides real-time monitoring and logging of NPU health, helping to maintain system stability by allowing timely awareness. |
| 1055921    | The inline CASB security profile has been enhanced to support control factors, such as tenant information in JSON data exchanged between a web browser and a custom SaaS application.                                                                                                                                                                                                                                                 |
| 1074271    | Enhanced the IPS engine to detect industrial Ethernet protocols, such as LLDP, GOOSE, EtherCAT, and PROFINET RT.                                                                                                                                                                                                                                                                                                                      |
| 1078890    | Fortinet now leverages AMQP (Advanced Message Queuing Protocol) to deliver real-time update notifications to FortiGate devices.                                                                                                                                                                                                                                                                                                       |
| 1091818    | AI/ML-based models trained on features extracted during protocol decoding are now used to improve detection capabilities.                                                                                                                                                                                                                                                                                                             |

# Upgrade Information

Upgrade paths and procedures are outlined in the documentation.

# Product Integration

Details on product integration and support are available in the technical specifications.

# Issues

# Resolved Issues

List of resolved issues with bug IDs.

# Known Issues

List of known issues with bug IDs.

# Engine Information

AV/IPS versions and details on built-in engines.

# Limitations

Known limitations of the current release.
---
# FortiGate OS Release Notes - Version 7.6.3

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
pre { background-color: #f4f4f4; padding: 10px; border-left: 3px solid #ccc; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiGate OS Release Notes

# Version 7.6.3

Build Number: 3457

# Supported Models

- FortiGate: FG-40F, FG-60F, FG-100F, FG-200F
- FortiWiFi: FWF-60F, FWF-100F
- FortiGate Rugged: FG-30F-R, FG-60F-R
- VM Variants: FortiGate-VM04, FortiGate-VM08

# Special Notices

Critical information regarding the release and its implications on existing configurations.

# Changes

# CLI Changes

config ips global
set machine-learning-detection {enable | disable}
end

# GUI Changes

Refer to the GUI documentation for detailed changes.

# Default Behavior Changes

Default settings may have changed; review the configuration guide for specifics.

# New Features and Enhancements

| Feature ID | Description                                                                                                                                                                                                                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1102608    | Zero-day malware stream scanning feature enables real-time delivery of malware IOCs to FortiGate devices using fortimq daemon, eliminating the need for frequent cloud polling and reducing server load. This approach ensures that new threats are blocked within seconds, improving detection speed and response time. |
| 1104259    | FortiOS Carrier includes a new GTP profile option to control whether the FortiGate will block GTP Echo Requests if there is no active tunnel over the associated GTP path.                                                                                                                                               |

# Upgrade Information

Review the upgrade paths and procedures to ensure compatibility with existing configurations.

# Product Integration

Details on integration with other Fortinet products and services.

# Issues

# Resolved Issues

List of resolved issues with corresponding bug IDs.

# Known Issues

List of known issues with corresponding bug IDs.

# Engine Information

AV/IPS versions and other engine-related information.

# Limitations

Known limitations of the current release.
---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# New Features or Enhancements

| Feature ID | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 947069     | Introducing a new desktop application developed for Windows and macOS called Fortinet Support Tool. This application is an evolution of the Fortinet Support Tool Chrome extension, formerly the FortiGate Support Tool. While the extension remains available, this new software expands its capabilities, empowering administrators to capture real-time debugging information through a REST API key generated directly on the FortiGate device.                                           |
| 1077192    | Add FortiOS support for ACME External Account Binding (EAB) as defined in RFC 8555 section 7.3.4. EAB is a way to associate an ACME account with an existing non-ACME account, such as a CA customer database, by adding additional information in newAccount requests. This additional information is used by the CA operating the ACME server to verify domain ownership by the requester without the need for human users to follow interactive natural-language instructions from the CA. |
| 1077562    | Add statistics for traffic shaping using QTM, and add egress-shaping-profile offload for SoC5.                                                                                                                                                                                                                                                                                                                                                                                                |
| 1106111    | FortiTelemetry provides information about the user experience based on application and network performance, which is collected by FortiTelemetry agents that send raw metrics to FortiTelemetry Cloud for analysis. FortiTelemetry Cloud then returns "application experience score" and "application failure rate" metrics to the FortiGate acting as a FortiTelemetry Controller, and these metrics are displayed on FortiTelemetry monitor pages.                                          |
| 1115892    | Connectivity Fault Management (CFM) has been extended to the following models: FG80F-POE and FG20xF. This enhancement allows administrators to diagnose and resolve issues in Ethernet networks efficiently.                                                                                                                                                                                                                                                                                  |

# VPN Enhancements

See IPsec and SSL VPN or Agentless VPN in the New Features Guide for more information.

| Feature ID | Description                                                                                                                                                                 |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 976976     | In IPsec dial-up VPN config using IKEv2, users can now configure Remote Gateway Match and Security posture tags within the VPN tunnel configuration in the GUI.             |
| 1051144    | Display GUI warnings for IKE-TCP port conflicts. FortiOS version 7.6.1 and later by default uses TCP port 443 for encapsulating IKE and ESP traffic using TCP as transport. |

---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 2em; }
h2 { font-size: 1.5em; margin-top: 20px; }
h3 { font-size: 1.2em; margin-top: 15px; }
h4 { font-size: 1em; margin-top: 10px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Critical information regarding configuration and compatibility.

# Changes

# CLI Changes

Details on CLI command modifications.

# GUI Changes

Details on GUI interface updates.

# Default Behavior Changes

Changes in default settings and behaviors.

# New Features and Enhancements

# Feature ID: 1058426

Added a new FortiClient Secure Internet Access (SIA) template for VPN Wizard, enabling the configuration of a Remote access IPsec VPN to ensure all FortiClient traffic is routed through FortiGate IPsec VPN tunnel for security inspection. The template allows administrators to select the desired security profile, including certificate or deep inspection, and configure policies to block access to botnet and C&C servers. Additionally, it provides an option to allow remote VPN users access to specified local subnets and local interfaces.

# Feature ID: 1069114

Introducing a set of debugging tools for IPSec on NP6 and NP7 platforms, this feature helps determine whether issues originate from the NP driver or the kernel module/IKE daemon, thereby enhancing troubleshooting capabilities.

# Feature ID: 1070448

Add support for configuring Quantum Key Distribution (QKD) and Digital Signature Algorithm/Post-Quantum Cryptography (PQC). This feature allows you to mix keys from QKD, PQC, and traditional Diffie-Hellman (DH) key exchange, ensuring robust security. By combining different types of keys, users can achieve maximum resilience against potential threats.

# Zero Trust Network Access (ZTNA)

See Zero Trust Network Access in the New Features Guide for more information.

# Feature ID: 1049209

In this enhancement, Windows users signed in to their workstations using Microsoft Entra ID domain are automatically allowed access to ZTNA-protected TCP resources by using the same IdP login information. FortiGate queries Entra ID using the client’s login token to look up and validate the user. This allows single sign-on (SSO) and eliminates the extra step for each user to authenticate when they access a TCP application.

# Feature ID: 1132509

Entry-level platforms with 2GB memory now support ZTNA tags in IP/MAC-based access control. Once registered with the EMS server, the platforms can synchronize posture tags and IP/MAC addresses for use in firewall policies.

# Upgrade Information

Details on upgrade paths and procedures.

# Product Integration

Compatibility and integration details with other products.

# Issues

# Resolved Issues

Details on resolved issues with bug IDs.

# Known Issues

Details on known issues with bug IDs.

# Engine Information

AV/IPS versions and details.

# Limitations

Known limitations of the current release.
---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
pre { background-color: #f4f4f4; padding: 10px; border-left: 3px solid #ccc; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Critical information regarding the release and any important notes for users.

# Changes

# CLI Changes

config firewall policy
edit <id>
set ztna-status {enable | disable}
set ztna-ems-tag <tag>
set ztna-ems-tag-secondary <tag>
set ztna-geo-tag <tag>
set ztna-ems-tag-negate {enable | disable}
next
end

# GUI Changes

Details on any changes made to the graphical user interface.

# Default Behavior Changes

Information on any changes to default settings or behaviors.

# New Features and Enhancements

Details on new features introduced in this release.

# Upgrade Information

Upgrade paths and procedures for transitioning to this version.

# Product Integration

Information on product compatibility and integration with other Fortinet products.

# Issues

# Resolved Issues

- Bug ID: 123456 - Description of the resolved issue.
- Bug ID: 789012 - Description of another resolved issue.

# Known Issues

- Bug ID: 345678 - Description of the known issue.
- Bug ID: 901234 - Description of another known issue.

# Engine Information

Details on the AV/IPS versions included in this release.

# Limitations

Any limitations or restrictions associated with this release.

# Change Logs

Summary of changes made in this version compared to previous versions.
---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Upgrade Information

Supported upgrade path information is available on the Fortinet Customer Service & Support site.

# Upgrade Options

| FortiGate                                                | Upgrade Option                                                         | Details                                                                                                        |
| -------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Individual FortiGate devices                             | Manual update                                                          | Use the procedure in this topic. See also Upgrading individual devices in the FortiOS Administration Guide.    |
|                                                          | Automatic update based on FortiGuard upgrade path                      | See Enabling automatic firmware updates in the FortiOS Administration Guide for details.                       |
| Multiple FortiGate devices in a Fortinet Security Fabric | Manual, immediate or scheduled update based on FortiGuard upgrade path | See Fortinet Security Fabric upgrade on page 27 and Upgrading all devices in the FortiOS Administration Guide. |

# To View Supported Upgrade Path Information:

1. Go to https://support.fortinet.com.
2. From the Download menu, select Firmware Images.
3. Check that Select Product is FortiGate.
4. Click the Upgrade Path tab and select the following:
- Current Product
- Current FortiOS Version
- Upgrade To FortiOS Version
5. Click Go.

# Fortinet Security Fabric Upgrade

FortiOS 7.6.3 is verified to work with these Fortinet products. This includes:

| Product        | Version                                        |
| -------------- | ---------------------------------------------- |
| FortiAnalyzer  | 7.6.3                                          |
| FortiManager   | 7.6.3                                          |
| FortiExtender  | 7.4.0 and later                                |
| FortiSwitch OS | 6.4.6 build 0470 and later (FortiLink support) |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3 {
color: #2c3e50;
}
h1 {
font-size: 24px;
}
h2 {
font-size: 20px;
}
h3 {
font-size: 18px;
}
ul {
margin: 10px 0;
padding-left: 20px;
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

# FortiOS 7.6.3 Release Notes

# Upgrade Information

The following products are supported for upgrade:

| Product                       | Supported Version                                                                                |
| ----------------------------- | ------------------------------------------------------------------------------------------------ |
| FortiAP                       | 7.2.2 and later                                                                                  |
| FortiAP-U                     | 6.2.5 and later                                                                                  |
| FortiAP-W2                    | 7.2.2 and later                                                                                  |
| FortiClient EMS               | 7.0.3 build 0229 and later                                                                       |
| FortiClient Microsoft Windows | 7.0.3 build 0193 and later                                                                       |
| FortiClient Mac OS X          | 7.0.3 build 0131 and later                                                                       |
| FortiClient Linux             | 7.0.3 build 0137 and later                                                                       |
| FortiClient iOS               | 7.0.2 build 0036 and later                                                                       |
| FortiClient Android           | 7.0.2 build 0031 and later                                                                       |
| FortiSandbox                  | 2.3.3 and later for post-transfer scanning 4.2.0 and later for post-transfer and inline scanning |

Note: If you are using FortiClient only for IPsec VPN, FortiClient version 6.0 and later are supported.

When upgrading your Security Fabric, devices that manage other devices should be upgraded first. When using FortiClient with FortiAnalyzer, you should upgrade both to their latest versions. The versions between the two products should match. For example, if using FortiAnalyzer 7.6.0, use FortiClient 7.6.0.

# Upgrade Order

Upgrade the firmware of each device in the following order to maintain network connectivity without the need to use manual steps:

1. FortiAnalyzer
2. FortiManager
3. FortiGate devices
4. Managed FortiExtender devices
5. Managed FortiSwitch devices
6. Managed FortiAP devices
7. FortiClient EMS
8. FortiClient
9. FortiSandbox
10. FortiMail
11. FortiWeb
12. FortiNAC
13. FortiVoice
14. FortiDeceptor
15. FortiNDR
16. FortiTester
17. FortiMonitor
---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
h1 {
font-size: 24px;
}
h2 {
font-size: 20px;
}
h3 {
font-size: 18px;
}
h4 {
font-size: 16px;
}
ul {
margin: 10px 0;
padding-left: 20px;
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

# FortiOS 7.6.3 Release Notes

# Upgrade Information

If Security Fabric is enabled, then all FortiGate devices must be upgraded to 7.6.3. When Security Fabric is enabled in FortiOS 7.6.3, all FortiGate devices must be running FortiOS 7.6.3.

# Downgrading to Previous Firmware Versions

Downgrading to previous firmware versions results in configuration loss on all models. Only the following settings are retained:

- Operation mode
- Interface IP/management IP
- Static route table
- DNS settings
- Admin user account
- Session helpers
- System access profiles

# Firmware Image Checksums

The MD5 checksums for all Fortinet software and firmware releases are available at the Customer Service & Support portal, https://support.fortinet.com. After logging in, go to Support > Firmware Image Checksums (in the Downloads section), enter the image file name including the extension, and click Get Checksum Code.

# FortiGate 6000 and 7000 Upgrade Information

Upgrade FortiGate 6000 firmware from the management board GUI or CLI. Upgrade FortiGate 7000 firmware from the primary FIM GUI or CLI. The FortiGate 6000 management board and FPCs or the FortiGate 7000 FIMs and FPMs all run the same firmware image. Upgrading the firmware copies the firmware image to all components, which then install the new firmware and restart. A FortiGate 6000 or 7000 firmware upgrade can take a few minutes, the amount of time depending on the hardware and software configuration and whether DP or NP7 processor software is also upgraded.

On a standalone FortiGate 6000 or 7000, or an HA cluster with uninterruptible-upgrade disabled, the firmware upgrade interrupts traffic because all components upgrade in one step. These firmware upgrades should be done during a quiet time because traffic can be interrupted for a few minutes during the upgrade process.

Fortinet recommends running a graceful firmware upgrade of a FortiGate 6000 or 7000 FGCP HA cluster by enabling uninterruptible-upgrade and session-pickup. A graceful firmware upgrade only causes minimal traffic interruption.
---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 24px; }
h2 { font-size: 20px; }
h3 { font-size: 18px; }
h4 { font-size: 16px; }
pre { background-color: #f4f4f4; padding: 10px; border-left: 3px solid #ccc; }
ul { margin: 0; padding-left: 20px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# Upgrade Information

Fortinet recommends that you review the services provided by your FortiGate 6000 or 7000 before a firmware upgrade and then again after the upgrade to make sure that these services continue to operate normally. For example, you might want to verify that you can successfully access an important server used by your organization before the upgrade and make sure that you can still reach the server after the upgrade and performance is comparable. You can also take a snapshot of key performance indicators (for example, number of sessions, CPU usage, and memory usage) before the upgrade and verify that you see comparable performance after the upgrade.

# Graceful Upgrade Procedure

1. Use the following command to set the upgrade-mode to uninterruptible to support HA graceful upgrade:
config system ha
set uninterruptible-upgrade enable
end
2. When upgrading from FortiOS 7.4.1 to a later version, use the following command to enable uninterruptible upgrade:
config system ha
set upgrade-mode uninterruptible
end
3. Download the FortiOS 7.6.3 FG-6000F, FG-7000E, or FG-7000F firmware from https://support.fortinet.com.
4. Perform a normal upgrade of your HA cluster using the downloaded firmware image file.
5. When the upgrade is complete, verify that you have installed the correct firmware version. For example, check the FortiGate dashboard or use the get system status command.
6. Check the Cluster Status dashboard widget or use the diagnose sys confsync status command to confirm that all components are synchronized and operating normally.

# Changes in CLI/GUI/Defaults

# Default Setting Change

The default setting of cp-accel-mode is changed to none on 2GB memory models. This change disables CP acceleration to lower system memory usage thus can prevent some unexpected behavior due to lack of memory.

# Previous FortiOS CLI Behavior:

config ips global
set cp-accel-mode advanced
end

# New FortiOS CLI Behavior After Upgrade:

Refer to the updated documentation for the new settings.
---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
pre {
background-color: #f4f4f4;
padding: 10px;
border-left: 3px solid #2c3e50;
overflow-x: auto;
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
background-color: #2c3e50;
color: white;
}

# FortiOS 7.6.3 Release Notes

# Upgrade Information

# Configuration Changes

config ips global
set cp-accel-mode none
end

This change will cause performance impact as CPU will do the pre-match (pattern match) inside IPS (CPU) instead of hardware engine (cp module in SOC4). Some customers could expect an increase in CPU utilization as a result. FortiGate and FortiWiFi 4xF/6xF families are affected by this change.

# Policy Changes After Upgrade

Policies that use an interface show missing or empty values after an upgrade. If local-in policy, DoS policy, interface policy, multicast policy, TTL policy, or central SNAT map used an interface in version 7.4.5, 7.6.0 GA or any previous GA version that was part of the SD-WAN zone, these policies will be deleted or show empty values after upgrading to version 7.4.6 or 7.6.1 or later. This issue is resolved in FortiOS 7.6.3 with mantis 1104649.

After following the upgrade path to FortiOS 7.6.3, you must manually recreate these policies and assign them to the appropriate SD-WAN zone. Although not recommended, you can skip the upgrade path and upgrade directly to FortiOS 7.6.3, and the policies remain untouched. Skipping upgrade steps might cause devices to miss other important FortiOS checks and changes and is not recommended.

# Managed FortiSwitch Password Policy

Starting from FortiOS version 7.6.1, a managed FortiSwitch no longer permits empty passwords for the admin account. If a FortiSwitch unit was previously authorized without an admin password, the FortiGate will automatically generate a random admin password for the FortiSwitch upon upgrading to 7.6.1 or later. This change will cause the admin to lose access.

To regain access, configure a password override on the FortiGate device using the following commands:

config switch-controller switch-profile
edit default
set login-passwd-override enable
set login-passwd
next
end
---
# FortiOS 7.6.3 Release Notes


# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

- FortiGate
- FG-40F
- FG-60F
- FG-100F
- FG-200F
- FG-5001E
- FortiWiFi
- FWF-60F
- FWF-100F
- FortiGate Rugged
- FG-100F-RUG
- VM variants
- FortiGate-VM04
- FortiGate-VM08

# Special Notices

FortiSwitch units with an existing admin password will not be affected by this change.

# Changes

# CLI Changes

Details on CLI changes will be provided here.

# GUI Changes

Details on GUI changes will be provided here.

# Default Behavior Changes

Details on default behavior changes will be provided here.

# New Features

Details on new features and enhancements will be provided here.

# Upgrade Information

For FG-5001E in a session-aware load balanced cluster (SLBC), all secondary blades install the image successfully. However, the primary blade fails, showing a sync timeout error, even with graceful-upgrade disabled.

# Product Integration

Details on product integration will be provided here.

# Issues

# Resolved Issues

Details on resolved issues will be provided here.

# Known Issues

Details on known issues will be provided here.

# Engine Information

Details on AV/IPS versions will be provided here.

# Limitations

Details on limitations will be provided here.

# Change Logs

Details on change logs will be provided here.
---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
pre {
background-color: #f4f4f4;
padding: 10px;
border-left: 5px solid #ccc;
overflow-x: auto;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #ccc;
padding: 8px;
text-align: left;
}
th {
background-color: #f2f2f2;
}

# FortiOS 7.6.3 Release Notes

# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Removed speed setting affects SFP+ interfaces after upgrade:

Starting in FortiOS 7.6.1, the 1000auto speed setting is removed. If a FortiGate SFP+ port speed is set to 1000auto before upgrade, the upgrade process automatically changes the setting to 10000full. This change can cause the interface to go down when the connecting device has a different speed setting.

Workaround: After upgrade, align the port settings. Edit the port and set the speed to 1000full to restore the connection.

config system interface
edit &lt;port&gt;
set speed 1000full
next
end

# Changes

# CLI Changes

Details on CLI changes will be documented here.

# GUI Changes

Details on GUI changes will be documented here.

# Default Behavior Changes

Details on default behavior changes will be documented here.

# New Features

Details on new features and enhancements will be documented here.

# Upgrade Information

Upgrade paths and procedures will be documented here.

# Product Integration

Details on product integration and support will be documented here.

# Issues

# Resolved Issues

- Bug ID: 123456 - Description of resolved issue.
- Bug ID: 789012 - Description of resolved issue.

# Known Issues

- Bug ID: 345678 - Description of known issue.
- Bug ID: 901234 - Description of known issue.

# Engine Information

AV/IPS versions will be documented here.

# Limitations

Details on limitations will be documented here.
---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Product Integration and Support

The following table lists FortiOS 7.6.3 product integration and support information:

| Category                       | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Web Browsers                   | * Microsoft Edge 135
* Mozilla Firefox version 138
* Google Chrome version 136Other browser versions have not been tested, but may fully function. Other web browsers may function correctly, but are not supported by Fortinet.                                                                                                                                                                                                                                                                                                |
| Explicit Web Proxy Browser     | - Microsoft Edge 135
- Mozilla Firefox version 138
- Google Chrome version 136Other browser versions have not been tested, but may fully function. Other web browsers may function correctly, but are not supported by Fortinet.                                                                                                                                                                                                                                                                                                |
| FortiController                | * Version: 5.2.5 and later
* Supported models: FCTL-5103B, FCTL-5903C, FCTL-5913C                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Fortinet Single Sign-On (FSSO) | - Version: 5.0 build 0319 and later (needed for FSSO agent support OU in group filters)

- Supported Windows Server Versions:

* Windows Server 2022 Standard
* Windows Server 2022 Datacenter
* Windows Server 2019 Standard
* Windows Server 2019 Datacenter
* Windows Server 2019 Core
* Windows Server 2016 Datacenter
* Windows Server 2016 Standard
* Windows Server 2016 Core
* Windows Server 2012 Standard
* Windows Server 2012 R2 Standard
* Windows Server 2012 Core

- Novell eDirectory 8.8 |
| AV Engine                      | 7.00040                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| IPS Engine                     | 7.01040                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

See also:

- Virtualization environments
- Language support
- Agentless VPN support
- FortiExtender modem firmware compatibility
---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Product Integration and Support

# Virtualization Environments

The following table lists hypervisors and recommended versions.

| Hypervisor               | Recommended Versions                                                                                           |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| Citrix Hypervisor        | 8.2 Express Edition, CU1                                                                                       |
| Linux KVM                | * Ubuntu 22.04.3 LTS
* Red Hat Enterprise Linux release 9.4
* SUSE Linux Enterprise Server 12 SP3 release 12.3 |
| Microsoft Windows Server | Windows Server 2022                                                                                            |
| Windows Hyper-V Server   | Microsoft Hyper-V Server 2022                                                                                  |
| Open source XenServer    | - Version 3.4.3
- Version 4.1 and later                                                                        |
| VMware ESXi              | Versions 6.5, 6.7, 7.0, and 8.0                                                                                |

# Language Support

The following table lists language support information.

| Language              | GUI |
| --------------------- | --- |
| English               | ✔   |
| Chinese (Simplified)  | ✔   |
| Chinese (Traditional) | ✔   |
| French                | ✔   |
| Japanese              | ✔   |
| Korean                | ✔   |
| Portuguese (Brazil)   | ✔   |
| Spanish               | ✔   |

---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Product Integration and Support

# Agentless VPN Support

The following table lists the operating systems and web browsers supported by Agentless VPN (formerly SSL VPN web mode). See also SSL VPN tunnel mode replaced with IPsec VPN on page 12.

| Operating System                          | Web Browser                                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------- |
| Microsoft Windows 7 SP1 (32-bit & 64-bit) | Mozilla Firefox version 138 Google Chrome version 136                         |
| Microsoft Windows 10 (64-bit)             | Microsoft Edge 135 Mozilla Firefox version 138 Google Chrome version 136      |
| Ubuntu 20.04 (64-bit)                     | Mozilla Firefox version 138 Google Chrome version 136                         |
| macOS Ventura 13.1                        | Apple Safari version 18 Mozilla Firefox version 137 Google Chrome version 136 |
| iOS                                       | Apple Safari Mozilla Firefox Google Chrome                                    |
| Android                                   | Mozilla Firefox Google Chrome                                                 |

Other operating systems and web browsers may function correctly, but are not supported by Fortinet.

# FortiExtender Modem Firmware Compatibility

The following table lists the modem firmware file name and version for each FortiExtender model and its compatible geographical region.

| FortiExtender Model | Modem Firmware Image Name | Modem Firmware File on Support Site | Geographical Region |
| ------------------- | ------------------------- | ----------------------------------- | ------------------- |
| FEX-101F-AM         | FEM\_EM06A-22-1-1         | FEM\_EM06A-22.1.1-build0001.out     | America             |
|                     | FEM\_EM06E-22-01-01       | FEM\_EM06E-22.1.1-build0001.out     | EU                  |
| FEX-101F-EA         | FEM\_EM06E-22.2.2         | FEM\_EM06E-22.2.2-build0002.out     | EU                  |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Product Integration and Support

FortiExtender Model

|                                |                                              |                     |   |
| ------------------------------ | -------------------------------------------- | ------------------- | - |
| Modem Firmware Image Name      | Modem Firmware File on Support Site          | Geographical Region |   |
| FEM\_06-19-0-0-AMEU            | FEM\_06-19.0.0-build0000-AMEU.out            | America and EU      |   |
| FEM\_06-19-1-0-AMEU            | FEM\_06-19.1.0-build0001-AMEU.out            | America and EU      |   |
| FEM\_06-22-1-1-AMEU            | FEM\_06-22.1.1-build0001-AMEU.out            | America and EU      |   |
| FEM\_06-22-1-2-AMEU            | FEM\_06-22.1.2-build0001-AMEU.out            | America and EU      |   |
| FEM\_07A-22-1-0-AMERICA        | FEM\_07A-22.1.0-build0001-AMERICA.out        | America             |   |
| FEM\_07A-22-2-0-AMERICA        | FEM\_07A-22.2.0-build0002-AMERICA.out        | America             |   |
| FEM\_07E-22-0-0-WRLD           | FEM\_07E-22.0.0-build0001-WRLD.out           | World               |   |
| FEM\_07E-22-1-1-WRLD           | FEM\_07E-22.1.1-build0001-WRLD.out           | World               |   |
| FEM\_12-19-1-0-WRLD            | FEM\_12-19.1.0-build0001-WRLD.out            | World               |   |
| FEM\_12-19-2-0-WRLD            | FEM\_12-19.2.0-build0002-WRLD.out            | World               |   |
| FEM\_12-22-1-0-AMEU            | FEM\_12-22.0.0-build0001-AMEU.out            | America and EU      |   |
| FEM\_12-22-1-1-WRLD            | FEM\_12-22.1.1-build0001-WRLD.out            | World               |   |
| FEM\_12\_EM7511-22-1-2-AMERICA | FEM\_12\_EM7511-22.1.2-build0001-AMERICA.out | America             |   |
| FEM\_12-22-1-0-AMEU            | FEM\_12-22.1.0-build0001-AMEU.out            | World               |   |
| FEM\_12\_EM7511-22-1-2-AMERICA | FEM\_12\_EM7511-22.1.2-build0001-AMERICA.out | America             |   |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Product Integration and Support

| FortiExtender Model | Modem Firmware Image Name | Modem Firmware File on Support Site  | Geographical Region |
| ------------------- | ------------------------- | ------------------------------------ | ------------------- |
| FEX-212F            | FEM\_12-19-2-0-WRLD       | FEM\_12-19.2.0-build0002-WRLD.out    | World               |
| FEX-311F            | FEM\_12-22-1-1-WRLD       | FEM\_12-22.1.1-build0001-WRLD.out    | World               |
| FEX-311F            | FEM\_EM160-22-02-03       | FEM\_EM160-22.2.3-build0001.out      | World               |
| FEX-311F            | FEM\_EM160-22-1-2         | FEM\_EM160-22.1.2-build0001.out      | World               |
| FEX-511F            | FEM\_RM502Q-21-2-2        | FEM\_RM502Q-21.2.2-build0003.out     | World               |
| FEX-511F            | FEM\_RM502Q-22-03-03      | FEM\_RM502Q-22.3.3-build0004.out     | World               |
| FEX-511F            | FEM\_RM502Q-22-04-04-AU   | FEM\_RM502Q-22.4.4-build0005\_AU.out | Australia           |
| FEX-511F            | FEM\_RM502Q-22-1-1        | FEM\_RM502Q-22.1.1-build0001.out     | World               |
| FEX-511F            | FEM\_RM502Q-22-2-2        | FEM\_RM502Q-22.2.2-build0002.out     | World               |

# Modem Firmware Upload Instructions

The modem firmware can also be uploaded manually by downloading the file from the Fortinet Customer Service & Support site. The firmware file names are listed in the third column of the table.

1. Go to https://support.fortinet.com/Download/FirmwareImages.aspx.
2. From the Select Product dropdown, select FortiExtender.
3. Select the Download tab.
4. Click MODEM-Firmware.
5. Select the FortiExtender model and image name, then download the firmware file.
---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

The following issues have been fixed in version 7.6.3. To inquire about a particular bug, please contact Customer Service & Support.

# Agentless VPN (formerly SSL VPN web mode)

See also SSL VPN tunnel mode replaced with IPsec VPN on page 12.

| Bug ID           | Description                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 947536           | SSLVPN crashes on corporate FortiGate due to watchdog timeout when a single connection enters an infinite loop of read iterations and the worker process becomes unresponsive to new connections. |
| 1017304          | SSL VPN web mode missing several security headers in the HTTP response.                                                                                                                           |
| 1036557, 1091173 | Performance degradation occurs in SSL-VPN due to connection/session timeout management issues.                                                                                                    |
| 1058211          | Traffic could not go through SSL VPN tunnel when DTLS is enabled with a loopback interface as source address.                                                                                     |
| 1077157          | FortiGate sends out expired server certificate for a given SSL VPN realm, even when the certificate configured in virtual-host-server-cert has been updated.                                      |
| 1083262          | FNBAMD session hangs after a massive authorization request.                                                                                                                                       |
| 1093580          | SSL VPN authentication is triggered even with EMS SN check enabled.                                                                                                                               |
| 1101837          | Insufficient session expiration in SSL VPN using SAML authentication.                                                                                                                             |
| 1102362          | SSL VPN web mode missing HTTP response headers.                                                                                                                                                   |
| 1107663          | FortiClient 7.2.6 GA Azure auto login cannot connect after upgrade.                                                                                                                               |
| 1111135          | Log additional debug information to aid troubleshooting.                                                                                                                                          |
| 1115510          | SAML metadata fails to generate when haproxy binds to the reserved SSL VPN source port 8900, preventing SAML authentication.                                                                      |
| 1126825          | SSL VPN stops functioning when ssl.root interface is added to a zone used by at least one policy.                                                                                                 |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

# Anti Virus

| Bug ID  | Description                                                                                                                                                                 |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1054835 | Large file downloads take longer than expected due to a WAD process issue.                                                                                                  |
| 1100819 | SMB traffic fails when the file server uses AES-256-GCM/CCM encryption with FortiOS.                                                                                        |
| 1104189 | In TP VDOM, the WAD creates the expectation session for FTP data connection if the firewall is in the proxy mode. This session does not have the outdev info.               |
| 1111973 | Security Profiles > Antivirus: Creating a new antivirus profile on 2G models displays error notification Cannot read properties of undefined (reading 'entries') and fails. |

# Application Control

| Bug ID  | Description                                                                                                                                                            |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1064413 | Traffic fails to follow SD-WAN rules when SNAT is enabled and "snat-route-change" is activated due to session drops caused by SNAT check failures after route changes. |
| 1102636 | After the first DB update, only signatures in the built-in DB are loaded, preventing new categories and updated signatures from appearing correctly.                   |

# DNS Filter

| Bug ID  | Description                                                                                                                      |
| ------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 1025233 | Support Encrypted Client Hello (ECH) in flow mode.                                                                               |
| 1096380 | FortiGate in proxy mode sends the cached DNS response when it receives a DNS registration request.                               |
| 1100282 | When using FortiGate DNS servers, some clients cannot handle large UDP DNS responses exceeding 512B received from the FortiGate. |

---
# FortiGate OS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

# Endpoint Control

| Bug ID  | Description                                                                                                                                                                  |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1066250 | Verification of EMS and upgrade of FGT with verified EMS should promote CA to fabric-ca.                                                                                     |
| 1090981 | EMS is unable to properly synchronize the FortiGate configuration for non-web ZTNA applications when FortiGate has multiple EMS units.                                       |
| 1093786 | Expired 'FCEM' contracts are loaded in FGVM when multiple account-level licenses exist under the same tag due to selection based on entry order rather than expiration date. |
| 1098350 | Sometimes the GUI > Asset FortiClient cannot display ems-tag for VPN user which makes "Matched Endpoints" page miss those users.                                             |

# Explicit Proxy

| Bug ID  | Description                                                                                                                            |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 1103272 | Wrong SSL certificate for block page replacement messages returns.                                                                     |
| 1107762 | Overflow occurs in WAD daemon when oversize-limit exceeds 4096 MiB during byte conversion.                                             |
| 1114438 | Policy Test feature fails to function correctly when testing HTTP(S) server configurations due to missing source port initialization.  |
| 1115137 | Expand the proxy-auth-timeout maximum value.                                                                                           |
| 1116555 | Deep scanning occurs when accessing subcategories of websites with category-based proxy policies despite disabling subcategory checks. |
| 1134310 | SSL exemption not working on proxy policy when partial match occurs.                                                                   |

# Firewall

| Bug ID | Description                                                                                                                                                           |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 723186 | Policy & Objects > Multicast Policy: Mac type addresses are not listed in the Src/dst omniselect on the GUI.                                                          |
| 946762 | Policy & Objects > Firewall Policy: The column filter for Secondary security posture Tag does not filter matching results when multiple tags are present on a policy. |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID           | Description                                                                                                                                                                                                                                                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 993138           | Misleading logs with subtype="ztna" appear when only virtual-server in a firewall policy.                                                                                                                                                                                                                                           |
| 994986           | The By Sequence view in the Firewall policy list may incorrectly show a duplicate implicit deny policy in the middle of the list. This is purely a GUI display issue and does not impact policy operation. The Interface Pair View and Sequence Grouping View do not have this issue.                                               |
| 1025078, 1086315 | When using a virtual server, some customers observed issues of memory usage increases and client sessions not disconnecting.                                                                                                                                                                                                        |
| 1025969          | Policy enforcement fails for wildcard FQDN hosts as destination targets because the address records are not added to the wildcard entry when processing a server response for an FQDN's domain name.                                                                                                                                |
| 1038650          | Policy list refreshes entirely when right-clicking on hitcount or bytes columns to update statistics or clear counters.                                                                                                                                                                                                             |
| 1050906          | Under heavy network traffic, the Netflow session cache for sampled traffic quickly reaches the hardcoded RAM limit, causing the sFlow daemon to shut down.                                                                                                                                                                          |
| 1055898          | HTTP/2 post without content-length is not supported in half-ssl virtual server.                                                                                                                                                                                                                                                     |
| 1066136          | Denied sessions were bidirectional and caused all traffic to be blocked.                                                                                                                                                                                                                                                            |
| 1078662          | If an interface on an NP7 platform has the set inbandwidth XXX, set outbandwidth XXX, and set egress-shaping-profile XX settings, the following issues may occur:- Fragment packet checksum is incorrect.
- MTU is not honored when sending packets out.
- QTM hangs and blocks traffic when packet size is larger than 6000 bytes. |
| 1081542          | Packet drops occur when high traffic causes nTurbo buffers to be reused without proper initialization under CPU-intensive conditions with ASIC offloading enabled.                                                                                                                                                                  |
| 1088507          | ICMP Echo replies sent through local-in-policy with virtual-patch enabled are routed through incorrect interfaces during traffic handling.                                                                                                                                                                                          |
| 1097628          | Firewall policy filter does not work well on source and destination columns for "all" and "ems" addresses.                                                                                                                                                                                                                          |
| 1098208          | After FortiGate exits conserve mode, some policies failed to install into the kernel at the same time.                                                                                                                                                                                                                              |
| 1101865          | Trailing stray characters appear in Netflow App Info reports, causing warnings in analysis programs.                                                                                                                                                                                                                                |
| 1102471          | Unexpected traffic hit policy in forward traffic log.                                                                                                                                                                                                                                                                               |
| 1103748, 111268  | Threat feeds used as source or destination addresses in security policies may not match correctly.                                                                                                                                                                                                                                  |
| 1104208          | NAT is incorrectly applied to traffic when a single SYN packet is sent to a VIP without an acknowledgment or reset.                                                                                                                                                                                                                 |

---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                                                       | |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |---|
| 1106112 | Shared memory files on entry-level platforms can't be removed upon restart due to being stored in a persistent directory instead of a temporary one.                                                                                                                                                              | |
| 1107003 | Policy & Objects: local-in policy, central-snat map, DoS Policy, and multicast policy have SD-WAN member in omniselect list of interface, and choosing the member interface results in an error. Central-snat map, DoS Policy, and multicast policy do not list the SD-WAN zone in omniselect list of interfaces. | |
| 1108540 | Search in the Address group dialog box using a partial word match takes more than a minute.                                                                                                                                                                                                                       | |
| 1110135 | Policy & Objects > Firewall Policy: Policy lookup for UDP protocol with FQDN does not work. Workaround: Use the command line for policy lookup.                                                                                                                                                                   | |
| 1111263 | tcpsock command missing PID/process name for sessions in established state.                                                                                                                                                                                                                                       | |
| 1117165 | Leaving the apn field empty in a GTP APN traffic shaping policy means that the policy will not match any traffic. Consequently, APN traffic shaping can only be applied to specific APNs. To configure GTP APN traffic shaping:                                                                                   | |
|         | config gtp apn-shaper edit \<policy-id> set apn \[\<apn-name> \<apngrp-name> ...] set rate-limit \<limit> set action {drop \| reject} set back-off-time \ next end                                                                                                                                          |
| 1120749 | If session is in SYN\_SENT or SYN\_RECV state, and FortiGate receives a second SYN with different ISN, it will drop the second SYN.                                                                                                                                                                               | |
| 1121944 | A firewall policy allows traffic from client to server, but no policy exists for server to client. When traffic is not matched from server to client, a block session forms that blocks traffic in both directions.                                                                                               | |
| 1127977 | Traffic fails to pass FortiGate when firewall policies are applied in TP VDOM due to flag checks treating packets as local instead of forwarding them.                                                                                                                                                            | |
| 1136058 | Policies are deleted and replaced with "implicit" when exporting CSV from the Interface Pair View in Firewall Policy GUI.                                                                                                                                                                                         | |
| 1136163 | The local-in-policy session TTL does not follow the service session-ttl.                                                                                                                                                                                                                                          | |
| 1139282 | VIP with set ldb-method http-host sends incorrect FQDN in ClientHello to second realserver when using HTTP2.                                                                                                                                                                                                      | |
| 1139282 | Incorrect SNI is sent during HTTP2/HTTP3 requests using "http-host" load balancing because WAD uses the proxy's SNI instead of the request's hostname.                                                                                                                                                            | |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

# FortiGate 6000 and 7000 platforms

| Bug ID  | Description                                                                                                                                                                                                                                                                                |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 790464  | After a failover, ARP entries are removed from all slots when an ARP query of single slot does not respond.                                                                                                                                                                                |
| 976521  | High CPU usage by the node process occurs when loading 7000 policies due to fetching all statistics in one request.                                                                                                                                                                        |
| 998615  | When doing a GUI-packet capture on FortiGate, the through-traffic packets are not captured.                                                                                                                                                                                                |
| 1062080 | SNMP query returns an error when there is a large number of BGP routes.                                                                                                                                                                                                                    |
| 1078334 | High cmdbsvr CPU usage and FTP hang issues occur during scheduled automation backup executions due to automated backups appending device serial numbers to file names.                                                                                                                     |
| 1095936 | Fewer sensor entries appear when executing 'chassis-sensor list' after system bootup due to delayed sensor initialization on SMM.                                                                                                                                                          |
| 1096156 | GUI unreachable due to certificates and private keys mismatches in a HA setup.                                                                                                                                                                                                             |
| 1097428 | The Security Profile menu does not appear in the GUI for Global VDOM on FortiGate 6K/7K devices despite being accessible through CLI.                                                                                                                                                      |
| 1102413 | Session count for VDOMs incorrect in FortiGate 6K/7K devices.                                                                                                                                                                                                                              |
| 1102481 | Local-in remote access issues due to incorrect destination address.                                                                                                                                                                                                                        |
| 1105009 | The command execute load-balance slot manage X fails on FortiGate 6K/7K devices when admin-telnet is disabled and then re-enabled.                                                                                                                                                         |
| 1108181 | Unexpected behavior observed in the confsyncd daemon due to an erroneous memory allocation.                                                                                                                                                                                                |
| 1109415 | New SNMP MIB table for chassis sensor.                                                                                                                                                                                                                                                     |
| 1109601 | Graceful upgrades fail when hatalk daemon restarts, disrupting slbha state synchronization during FortiOS version transitions.                                                                                                                                                             |
| 1109963 | SFF-8472 diagnostic support was not recognized on SFP transceivers in FG-7941F systems.                                                                                                                                                                                                    |
| 1112581 | On the FortiGate 7000F platform, after upgrading from FortiOS 7.4.7 to 7.6.2, cmdbsvr CPU usage can be at 99% on one or more FPMs for several minutes. During high CPU usage, FortiGuard packets cannot be synchronized to the affected FPM(s).                                            |
| 1115656 | FG-6K session filter by source interface doesn't set correct interface index.                                                                                                                                                                                                              |
| 1116862 | Graceful upgrade of a FortiGate 7000E chassis to FortiOS 7.6.2 may fail for some configurations.                                                                                                                                                                                           |
| 1118004 | On a FortiGate 7000E FGCP cluster, after using the execute ha disconnect command to disconnect a chassis from the cluster, you can't use the special management ports to connect to the FIM in slot 2 or to any of the FPMs of either chassis. You can still connect to the FIM in slot 1. |

---
# FortiGate OS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                        |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1121918 | Confsyncd crashes occur when syncing ha-mgmt-intf to a newly joined HA slave due to invalid pointer attributes.                                    |
| 1124603 | Traffic drop occurs on 7KF-FGT devices when traffic shaping is enabled during or after migration, causing intermittent internet connectivity loss. |
| 1130218 | Policies fail when Security Posture Tags are configured on SLBC platforms due to dynamic address sync issues outside HA mode.                      |
| 1139867 | In a 7121F chassis HA system with 7000F image, the secondary chassis GTP-C tunnels were not synced with the primary chassis GTP-C tunnels.         |
| 1149405 | The image upgrade fails when performing a non-graceful update due to an ISIZE mismatch during verification.                                        |

# FortiView

| Bug ID  | Description                                                                                                                                                                               |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1125124 | When running more than 1 million concurrent HTTP sessions across the firewall, and trying to access session list on FortiView in the GUI, packet loss and loss of a session are observed. |

# GUI

| Bug ID  | Description                                                                                                                                                                                                         |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 919473  | Network > Interfaces: When an IPsec tunnel is bound to an interface, the "Interface Integrate" option for the interface fails.                                                                                      |
| 1047963 | High Node.js memory usage when building FortiManager in Report Runner fails. Occurs when FortiManager has a slow connection, is unreachable from the FortiGate (because FMG is behind NAT), or the IP is incorrect. |
| 1054026 | Offline license file cannot be uploaded to FGT by GUI.                                                                                                                                                              |
| 1055197 | On FortiGate G series with dual WAN links, Interface bandwidth widget may show incorrect incoming and outgoing bandwidth count, where the actual traffic does not match the display numbers.                        |
| 1055865 | NodeJS errors when event log socket is closed.                                                                                                                                                                      |
| 1092489 | The config system fortiguard > fortiguard-anycast setting was changed to automatically disable when the FortiGuard page is shown on GUI.                                                                            |

---
# FortiOS 7.6.3 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }
.bug-id { width: 15%; }
.description { width: 85%; }

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                                                                        |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1097405 | Patch schedule minutes are ignored when set through the GUI for automatic upgrades.                                                                                                                |
| 1099309 | The FortiOS GUI fails to load topology-related pages when temporary files generated during Security Rating operations are mistakenly read by the REST API.                                         |
| 1101932 | IPsec monitor widget: IPsec phase2 tunnel details are not displayed in the tooltip when hovering over the phase2 selector.                                                                         |
| 1102404 | VDOM search function does not work properly if VDOM has uppercase letters.                                                                                                                         |
| 1110382 | Admin can log in to GUI (HTTPS) with password, even when admin-https-pki-required is enabled.                                                                                                      |
| 1110827 | GUI shows LAN interfaces that have an IP address in the network ranges 172.31.0.0/16 or 192.168.0.0/16 to be managed by IPAM, even though the feature is globally disabled.                        |
| 1111113 | When launching the GUI console using Jet Stream theme, the character spacing appears wider than usual.                                                                                             |
| 1112716 | No log output when running debug flow on GUI.                                                                                                                                                      |
| 1114658 | Duplicated logs occur during Node.js health-check operations when internal communication between daemons is exposed through HTTP requests, as the traffic is captured in logs and packet captures. |
| 1115684 | System > FortiGuard: FortiCare elite contract is not displayed accurately under Licensing information.                                                                                             |
| 1118810 | Asset Identity Center: Tooltip on IoT/OT Vulnerabilities says OT license is inactive even with full license.                                                                                       |

# HA

| Bug ID  | Description                                                                                                                                                                 |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 982081  | After changing the status to down on the ha1 and ha2 ports, setting the status back to up does not bring up the ports.                                                      |
| 1068674 | PBA logs missing during HA failover.                                                                                                                                        |
| 1073514 | In HA cluster, when a FortiToken is aggregated or revoked from a local.user, cluster is out of SYNC.                                                                        |
| 1085314 | Firewall policy page takes a long time to load on the HA Primary unit due to a loop condition between BGP and NSM when other protocols' same route is redistributed to BGP. |
| 1095879 | HA secondary unit experiences high CPU usage when frequent changes are made to CMDB on the HA primary unit.                                                                 |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                                                                        |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1088956 | Duplicated logs occur in FAZ during sniffer mode operation in HA active-passive setups because both active and passive FortiGates forward L2 packets to the IPS engine, causing duplicate entries. |
| 1091189 | Switches observe MAC address flapping in HA A-A setups when both FortiGates use identical virtual MACs on their primary VLANs.                                                                     |
| 1091657 | SDN connector limits the API traffic flow through root VDOM or HA management VDOM.                                                                                                                 |
| 1095786 | Traffic interruption occurs when performing a manual HA failback after an initial failover in VWP setups.                                                                                          |
| 1098192 | Joining a FortiGate with RAID enabled in an existing cluster causes the primary to shut down due to differing RAID statuses.                                                                       |
| 1100177 | In an FGSP setup, on asymmetric TCP flow during SYN/ACK packet on the other member, the TCP MSS value is not adjusted according to the firewall policy.                                            |
| 1101456 | In a HA setup, the aggregate interface status remains up after configuring 'status down' in FortiOS due to a race condition.                                                                       |
| 1101879 | Multiple SCTP expectation sessions are created during resynchronization due to a flag allowing duplication.                                                                                        |
| 1104892 | Duplicate IP detected messages are seen from the Secondary Fortigate in a cluster.                                                                                                                 |
| 1105422 | "Detected Tx Unit Hang" error occurs on the HA secondary, causing it to become out-of-sync.                                                                                                        |
| 1107137 | The secondary FortiGate with an HA Reserved Management Interface cannot be accessed using HTTPS after upgrading from version 7.4.3.                                                                |
| 1108895 | In an FGSP cluster, enabling and disabling standalone-config-sync results in the local dev\_base being deleted and synchronized with the peer, which leads to the absence of the dev\_base.        |
| 1109919 | Cluster experiences split-brain when EMAC interfaces are disabled within a zone.                                                                                                                   |
| 1110498 | Add IPv6 destination support under HA management interface configuration.                                                                                                                          |
| 1113842 | New LACP interface is not shown under diagnose sys ha standalone-peers on both FGSP members.                                                                                                       |
| 1115190 | The SNMP value of fgVWLHealthCheckLinkState on the secondary unit should always be set to dead(1).                                                                                                 |
| 1117725 | HA synchronization fails due to checksum mismatches on CA certificates across all VDOMs when adding or modifying certificates sourced from a bundle.                                               |
| 1121117 | When two HA clusters are on the same subnet, the L2 session-sync packets could be received by each other, even if they are from two different HA clusters.                                         |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                                             |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1129088 | The sessionsync daemon experiences high CPU usage when syncing expectation sessions under heavy SCTP traffic and FGSP enablement due to inefficiencies in the dump API. |
| 1135866 | HA second unit cannot sync firewall ZTNA dynamic address with HA primary unit after primary disables EMS server.                                                        |
| 1137565 | vSN support added in 7.2.9, 7.4.6, and 7.6.1. FG-100F/101F do not yet support vSN and logical-sn.                                                                       |
| 1138763 | IKE hasync loop and high memory consumption when peer address/port changes.                                                                                             |

# Hyperscale

| Bug ID  | Description                                                                                                                                                                                                                |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1013892 | Unexpected behavior observed in NPD when the threat feed object attempted to update manually in the HA pair.                                                                                                               |
| 1055443 | Add ipv4/v6-session-quota back for software sessions in hyperscale VDOM.                                                                                                                                                   |
| 1074547 | SNAT session drops occur when kernel sessions become dirty in hyperscale VDOM environments due to inconsistent NAT resource allocation between software and hardware sessions.                                             |
| 1093287 | Using fixed-allocation IP Pools may cause NP7 NSS/PRP modules to become stuck, potentially disrupting traffic. Other PBA IP pools do not have this issue.                                                                  |
| 1094162 | The diag sys npu-session list-brief command now includes additional values for timeout, duration, and policy-id and an improved filter that includes EIF sessions to enhance its functionality and filtering capabilities. |
| 1108263 | HA configurations are lost if hw-sess-sync-dev is configured with more interfaces than expected. (The expectation is two times the number of NP7 chips.)                                                                   |
| 1114113 | The get sys ha status command does not offer detailed interface statistics for hardware session sync devices.                                                                                                              |
| 1115761 | When handling very high traffic loads (150M 250M concurrent sessions), the system sometimes fails to free up memory, even after all sessions have been cleared and traffic has stopped.                                    |
| 1121524 | Client could not get DHCP IP address with policy-offload-level set to full-offload.                                                                                                                                        |

---
# FortiGate OS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

# Intrusion Prevention

| Bug ID  | Description                                                                                           |
| ------- | ----------------------------------------------------------------------------------------------------- |
| 1040783 | FortiGate encounters CPU usage issue due to IPSEngine utilization when using an app-ctrl utm profile. |
| 1090616 | IPS does not pass channel ID/category ID from the first video in a YouTube playlist to WAD.           |
| 1101633 | Child process that loads IPS database does not have CMDB permission to write to IPS table.            |
| 1107445 | Remove IPS diagnose command diagnose ips cfgscript run.                                               |
| 1113473 | When IPS generates traffic log for tunnel traffic, traffic log should include outer packet details.   |
| 1121953 | IPSengine processes consume memory and can lead to the conserve mode.                                 |

# IPsec VPN

| Bug ID  | Description                                                                                                                                                                                                                                        |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1002325 | When spoke re-authauthorization is enabled, shortcut tunnel rekey fails and goes down when SA expires. Shortcut tunnel flaps while it re-establishes again.                                                                                        |
| 1042465 | Packet drops occur when FortiOS CPUs are overwhelmed by high traffic bursts while IPsec acceleration is enabled, leading to CP queue overflows despite prior optimizations.                                                                        |
| 1049015 | IPsec performance issue on Intel-based platforms occurs due to FortiOS not enabling all available IPsec drivers.                                                                                                                                   |
| 1054440 | Incrementing TX and RX errors on VPN interface occur when NPU offload is disabled, busy CPU cores, or high burst traffic cause packet drops due to full queues on SoC3/Soc4 platforms.                                                             |
| 1057558 | Dialup and loopback-asymroute disable with multiple paths for IKE/IPsec traffic are configured. When the incoming ESP traffic changes path because of a routing change, reply traffic still egresses on the old interface, and traffic is dropped. |
| 1059778 | IPsec does not work as expected when the traffic path is from spoke dial-up to hub1, and then from hub1 to another site through a site-to-site tunnel.                                                                                             |
| 1060048 | Throughput is limited in Site to Site VPN connections between the FW1kF and the FWVM Google Cloud platform.                                                                                                                                        |
| 1064078 | Egress shaper fails to enforce bandwidth limits on VPN ID with IPIP encapsulation IPsec interfaces due to incorrect handling of traffic forwarding across multiple network processing units.                                                       |
| 1071769 | L2TP/IPsec connections fail due to interface changes from break-before-make rekeys and Windows rejecting selectors during FGT-initiated QM rekeys.                                                                                                 |

---
# FortiGate OS Release Notes - Version 7.6.3

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiGate OS Release Notes

# Version 7.6.3

# Resolved Issues

| Bug ID  | Description                                                                                                                                                                           |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1073670 | Unexpected behavior observed in the IKED during HA split-brain events when IPsec tunnels are configured to use DHCP.                                                                  |
| 1087651 | Authentication fails when using FortiClient with IPsec IKEv2 after waiting more than 60 seconds to enter the 2FA token, caused by a fixed 60-second RADIUS timeout.                   |
| 1094028 | Unexpected behavior observed in the IKED after configuration changes when the phase1 monitor feature is used.                                                                         |
| 1102528 | NP7 tunnel offloading failure recovery issue may cause use-after-free memory corruption when there are many concurrent IPSec tunnels, which leads to high CPU usage and kernel panic. |
| 1102584 | Kernel crash caused by memory corruption due to a use-after-free issue, resulting in a system hang. This issue occurs with a large number of IPsec tunnels.                           |
| 1103594 | ADVPN IPsec traffic over shortcuts drops during IPsec tunnel rekey.                                                                                                                   |
| 1103754 | Failed HTTP sessions occur when passing through nTurbo due to improper handling of fragmented packets.                                                                                |
| 1107198 | Transparent mode, policy-based IPsec VPN, local-out traffic automatically enters VPN.                                                                                                 |
| 1109028 | With set peertype one, the FortiGate will not accept ID\_IPV4\_Address as peer ID for dynamic IPsec IKEv2.                                                                            |
| 1109627 | IPsec VPN match-security-posture-tag feature won't work when FortiClient is behind NAT.                                                                                               |
| 1112665 | Static routes are marked inactive when an old IPSec tunnel is deleted during an INITIAL-CONTACT message in IKEv1, mistakenly deactivating the new tunnel's status in the kernel.      |
| 1113354 | Group list is truncated because of fixed-size buffers.                                                                                                                                |
| 1116825 | Juniper device unable to establish IKEv1 tunnel with FGT.                                                                                                                             |
| 1117758 | FGT fails to negotiate encryption algorithm CHACHA20\_POLY1305 against third-party client.                                                                                            |
| 1117910 | iked spikes to 99.9% if client sends FIN after ike tcp session is established.                                                                                                        |
| 1120003 | FortiGate presents certificate information when accessed using IPsec VPN listening interface.                                                                                         |
| 1125487 | Autoconnect to IPsec VPN using Entra ID logon fails when there are multiple IPsec tunnels.                                                                                            |
| 1127444 | For ADVPN 2.0 shortcut negotiation, UDP hole punching for spoke behind NAT uses source port 500 instead of 4500.                                                                      |
| 1136536 | SIA IPsec VPN authentication fails on FortiSASE when number of groups is greater than 150 user groups.                                                                                |

---
# FortiOS 7.6.3 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.3 Release Notes

# Resolved Issues

# Log & Report

| Bug ID  | Description                                                                                                                                                 |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 864002  | Unauthenticated User mismatch with User in logs.                                                                                                            |
| 1004103 | Log & Report > Reports: When reports are renamed, the scheduled reports page does not load and the unable to fetch reports error notification is displayed. |
| 1009584 | FGT-VM64 has no crash log record and event logs for license status change from Valid to Warning.                                                            |
| 1074460 | Erroneous memory allocation results in intermittent HTTPSD disruption caused by a corrupted traffic log file.                                               |
| 1084934 | Firewall logs show Object Object in GUI and dstintf="unknown-0" in raw logs.                                                                                |
| 1091064 | Missing poluuid and policyname fields occur in Forward Traffic logs when HA failover happens in FGCP clusters.                                              |
| 1100883 | Forward Traffic log fetched from FortiGate Cloud takes a long time to load on GUI.                                                                          |
| 1107571 | Some WiFi Log descriptions are inaccurate.                                                                                                                  |
| 1116428 | Observed Device vulnerability lookup on FortiGuard in high frequency under the system event log.                                                            |
| 1118089 | Temporary log files persist in /var/log after successful FTP uploads, leading to increased disk usage.                                                      |
| 1119147 | Secondary device fails to generate reports at the set time.                                                                                                 |
| 1121505 | Log & report > Forward Traffic: The Security tab for security event logs does not load.                                                                     |
| 1122938 | Syslog traffic uses the correct exit interface after a change in source interface but fails to update the source IP.                                        |
| 1129448 | The body is partially missing from emails sent by alert mail.                                                                                               |
| 1130821 | IPS sensor log-attack-context output is both truncated and monitored with payload loss.                                                                     |

# Proxy

| Bug ID  | Description                                                                                                                  |
| ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 958200  | Packets captured by IPS indicates HTTP/1.1 in case of HTTP/2 request.                                                        |
| 988473  | On FortiGate 61E and 81E models, a daemon WAD issue causes high memory usage.                                                |
| 1014014 | Proxyd always selects the first certificate in the list when multiple server certificates are configured, regardless of SNI. |

---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                  |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 1023054 | After an upgrade on a 2GB FortiGate device, the firewall policy does not switch from Proxy-based to Flow-based in the Inspection mode field. |
| 1051875 | Strict SNI certificate checks skip IP destination validation under strict mode.                                                              |
| 1054835 | HTTP/2 large file transfers are slow when IPS, APP, or SSL inspect-all is enabled due to excessive buffering during traffic forwarding.      |
| 1066113 | Accessing certain websites through HTTPS fails when using inspect-all deep-inspection in proxy mode firewall policy.                         |
| 1096728 | An error case observed in the WAD, affecting some VIP traffic, caused by erroneous memory allocation.                                        |
| 1107205 | FortiGate encounters a WAD memory usage issue when using a secure explicit web proxy with WAD user authentication to visit some websites.    |
| 1116771 | Add a limit on the memory used by user-device-store as a percentage of the total system memory.                                              |
| 1121171 | Large file downloads through proxy HTTP2 are slow when IPS/APP/SSL inspect-all enabled.                                                      |
| 1126253 | When VDOM configuration file is restored, it changes the no-inspection profile under ssl-ssh-profile to deep-inspection.                     |
| 1126385 | WAD fails to handle deep-inspection traffic under FIPS mode.                                                                                 |

# REST API

| Bug ID  | Description                                                                                                                                                   |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 943756  | When creating a VPN remote certificate with the API, the "remote" key fails to be set, resulting in incomplete configuration.                                 |
| 1019750 | The available interfaces list is slow in configurations with many IPsec tunnel connections.                                                                   |
| 1026547 | Sensor information through REST API on a FG-81F returns 404 error.                                                                                            |
| 1071799 | Failed to rename switch-controller managed-switch entries through the CMDB REST API.                                                                          |
| 1107698 | Adding ipv6-trusthost under api-user will override ipv4-trusthost setting and allow all IPv4 source IP addresses.                                             |
| 1110811 | HTTPSD crash due to a memory leak in the libjson-c library when the monitor/virtual-wan/health-check API returns an error and response is not free correctly. |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

# Routing

| Bug ID  | Description                                                                                                                                                                                   |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 897308  | The system fib version does not match VDOM fib version in 1801F when queried due to a misalignment in how genid is reported by the Linux kernel to user space.                                |
| 1008434 | The speed-test result files are not deleted after test runs. The new test ID may collide with a previous result. In this case, the GUI may read a previously failed result and report errors. |
| 1058283 | Routing monitor: The Routing widget becomes unresponsive when using route lookup on a configuration that has a large number of routes.                                                        |
| 1058700 | The load-balance mode in SD-WAN rules only considers up to 8 paths as active when more than 8 are configured.                                                                                 |
| 1072311 | BGP flaps occur when high L2P TPE drops are detected under heavy IPsec traffic conditions.                                                                                                    |
| 1080449 | IPv6 prefix delegation does not add IPv6 route automatically.                                                                                                                                 |
| 1082842 | The loopback interface does not appear as an outgoing option for BGP peer connections when configuring through the GUI.                                                                       |
| 1084851 | When adding new static route and prefix-list using CLI, 0.0.0.0/0 takes effect, in spite of invalid format of dst and prefix.                                                                 |
| 1084907 | Inactive IPv6 routes occur when dual stack BFD is configured without assigning the correct interface for IPv6, causing it to default to an IPv4 interface instead.                            |
| 1086944 | The BGP router-id fails to reset after editing the neighbor group settings because the dialog doesn't properly handle the reset functionality.                                                |
| 1093215 | Users can create a BGP neighbor without configuring remote-as using CLI, and after completing BGP neighbor configuration, neighbor will remain in admin down state.                           |
| 1095307 | Network > SD-WAN > SD-WAN Rules: Filtering on members with alias names does not display matching results.                                                                                     |
| 1099554 | FortiGate uses link-local IPv6 address as nexthop in VLAN network, instead of global address.                                                                                                 |
| 1100529 | BGP Stale route not working as expected.                                                                                                                                                      |
| 1103034 | Application "cmdbsvr" crashes when processing a configuration from OaaS controller. This issue occurs when adding another ISP to the test spokes and applying the change.                     |
| 1103212 | Network > Routing Objects: BGP AS number with asdot/asdot+ format will drop the trailing 0s on "set set-aspath" router-map config.                                                            |
| 1105064 | IPv6 traffic can't match the correct firewall policy in certain SD-WAN cases.                                                                                                                 |
| 1108192 | Restore image from FTP server failed using SD-WAN.                                                                                                                                            |
| 1108874 | SD-WAN Default\_DNS performance SLA shows all participants of Default\_DNS are down.                                                                                                          |
| 1109286 | Incorrect priorities are applied during remote health-checks when iked restarts because lnkmtd retains stale tunnel cache entries.                                                            |

---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                                                             |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1111233 | auto-asic-offload disabled under vne-interface after upgrading from 7.4.6 to 7.6.1.                                                                                                     |
| 1113929 | Incorrect SDWAN rule is matched. fib-best-match is configured under zone.                                                                                                               |
| 1114687 | The snmpd cache update takes longer when querying SD-WAN health-check data due to delays in retrieving bandwidth statistics.                                                            |
| 1116924 | In SD-WAN, when detect mode Prefer Passive is used, routing table is not updated in time.                                                                                               |
| 1118891 | ADVPN shortcut is established between different transport-groups.                                                                                                                       |
| 1119119 | Inadvertent behavior observed in BGPD due to erroneous memory freeing when applying route-maps.                                                                                         |
| 1122021 | FortiGate disregards SD-WAN members for path selection even when they are in SLA.                                                                                                       |
| 1128032 | Traffic fails with Fabric Overlay Orchestrator using automatic policy creation with system zones.                                                                                       |
| 1129698 | When FortiAnalyzer setting interface-select-method is sdwan, FortiAnalyzer connection is closed and restarted, even though SD-WAN interface doesn't change.                             |
| 1133796 | IPv6 routes are stuck on kernel routing table.                                                                                                                                          |
| 1138483 | The link-monitor daemon truncates hostnames exceeding 63 characters when used in SDWAN health-check configurations, causing DNS resolution failures and impacting service availability. |

# Security Fabric

| Bug ID  | Description                                                                                                                                                                               |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 903922  | Physical and logical topology is slow to load when there are a lot of managed FortiAP devices (over 50). This issue does not impact FortiAP management and operation.                     |
| 1006397 | Granular failure details for each device in a federated upgrade are now reported, allowing users to identify individual devices with specific failure reasons during the upgrade process. |
| 1011833 | FortiGate experiences a CPU usage issue in the Node.js daemon when there are multiple administrator sessions running simultaneously.                                                      |
| 1021684 | In some cases, the Security Fabric topology cannot load properly and displays a Failed to load Topology Results error.                                                                    |
| 1090401 | Error messages from netxd API calls are not displayed when running as a daemon because they are printed to stderr instead of the CLI.                                                     |
| 1099235 | Scheduled triggers do not include eventtime in log entries, causing automation scripts using %%log.eventtime%% to fail and generate filenames with missing or incorrect timestamps.       |
| 1101806 | Failed to trigger Security Rating Summary event automation stitch due to issue with log field ID.                                                                                         |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                                                                           |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1019844 | In an HA configuration, when the primary FortiGate unit fails over to a downstream unit, the previous primary unit displays as being permanently disconnected.                                        |
| 1111619 | The replacemsg-group in automation-action gets unset when system reboots.                                                                                                                             |
| 1113463 | FortiGate Azure connector fails to retrieve AKS information on AKS 1.29.5.                                                                                                                            |
| 1119616 | Externally maintained threat feed contains both resource FQDNs and IP address ranges/subnets. Entry such as \<addr>/0x1 then matches half of all possible IPv4 address and causes network disruption. |
| 1120652 | Fabric topology with two devices on different VDOMs but behind the same router shows wrong VDOM data on tooltip.                                                                                      |
| 1134970 | Inconsistent DNS TTL behavior in Kubernetes API through SDN-Connector.                                                                                                                                |

# Switch Controller

| Bug ID  | Description                                                                                                                                                                 |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1015992 | WiFi & Switch Controller > FortiLink Interface: When a FortiLink interface is down and the Lockdown ISL toggle is set to 'disable' on the GUI, the setting is not retained. |
| 1016034 | In an HA environment with FortiSwitches connected, the lockdown ISL setting on FortiLink gets enabled during HA failover.                                                   |
| 1108965 | Sync errors occur when incomplete transaction flags related to dhcp-snooping-static-client replay past configuration changes during sync attempts.                          |
| 1113465 | VLAN configurations intermittently fail to assign on FSW ports when devices matching DPP policy come online, which is caused by a race condition during FSW initialization. |
| 1130242 | Only the last SNMP community configuration is pushed from FGT to FSW during bulk processing.                                                                                |
| 1138333 | Increase efficiency of FortiLink configuration daemon memory usage.                                                                                                         |

# System

| Bug ID | Description                                                                                                                                                                    | |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |---|
| 814119 | drop-overlapped-fragment {enable \| disable} does not work on NP7 platforms.                                                                                                   |
| 932077 | Connection issue between SOC4 platform and third-party switches, for example Hirschmann GRS 105 or Cisco switch, since SOC4 doesn't support certain carrier extension signals. | |

---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID                                     | Description                                                                                                                                                                                                       |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 976722                                     | Invalid YAML files are generated when exporting configurations containing multi-value attributes or long strings with newline characters.                                                                         |
| 992323, 1056133, 1075607, 1082413, 1084898 | Traffic interrupted when traffic shaping is enabled on 9xG and 12xG.                                                                                                                                              |
| 1017941                                    | GUI interface bandwidth shows Tetrabyte spike for Gigabyte interface. Affected platforms: FGT-220xE and FGT-330xE                                                                                                 |
| 1040137                                    | NPD skips config parsing when policy-offload-level set to disable.                                                                                                                                                |
| 1040489                                    | Traffic using VXLAN VTEP with a loopback over an IPsec VPN is dropped when VXLAN and IPsec are configured in different VDOMs due to incorrect tunnel creation success indicators.                                 |
| 1046484                                    | After shutting down FortiGate using the "execute shutdown" command, the system automatically boots up again.                                                                                                      |
| 1067448                                    | VLAN switch is not working on 120G/121G.                                                                                                                                                                          |
| 1069208                                    | If the DHCP offer contains padding when DHCP relay is used, the DHCP relay deletes the padding before relaying the packet.                                                                                        |
| 1075279                                    | Member interfaces of VWP appear in packet capture creation dialog despite being ineligible.                                                                                                                       |
| 1076883                                    | When the top application bandwidth feature is disabled, the GUI process still performs the initial check for application bandwidth, which may cause FortiCron to experience high CPU usage.                       |
| 1077562                                    | Hardware egress shaping doesn't work on SOC5 when NPU offload is enabled.                                                                                                                                         |
| 1078119                                    | Traffic is intermittently interrupted on virtual-vlan-switch on Soc5 based platforms when a multicast or broadcast packet is received.                                                                            |
| 1078568                                    | When FortiManager adds FortiGate via serial number and is behind NAT, FortiGate cannot initiate requests to FortiManager, causing the GUI to fail in retrieving the certificate CN/SAN and resulting in an error. |
| 1079850                                    | HA1/HA2 ports remain down after setting status to up. Rebooting fixes the issue.                                                                                                                                  |
| 1085407                                    | FortiGate unresponsive when default-qos-type is set to shaping.                                                                                                                                                   |
| 1086268                                    | VXLAN interface cannot be created if its underlying interface is DHCP.                                                                                                                                            |
| 1087160                                    | NP drops traffic when VXLAN is a member of software switch in implicit mode.                                                                                                                                      |
| 1087270                                    | Unexpected traffic increase over the FortiGate 6000 base backplane.                                                                                                                                               |
| 1089143                                    | The time change in FOS is restored after reboot. The RTC node is not created correctly so the time change can't be kept in RTC.                                                                                   |
| 1089272                                    | The inability to view or click the "+" sign occurs when a user is assigned an admin profile with only read access, restricting actions that require write privileges.                                             |

---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                               |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1090372 | Access profile entries exceed global limit when built-in profiles consume table size slots.                                                                                                                                                                                                                                               |
| 1091175 | VLAN statistics on LAGs are not displayed correctly when asic-offload is enabled due to incorrect OID usage.                                                                                                                                                                                                                              |
| 1091551 | Hardware limitation on the NP7 platform causes the following QTM related issues:- Incorrect checksum for fragments after QTM.
- Packets longer than 6000 bytes cause QTM unresponsiveness.
- Refresh issue causes QTM unresponsiveness.
- MTU is not honored after QTM, so packets are not fragmented.                                    |
| 1094404 | State of peer ports of FGT ports(negotiated speed, 1G) is down after upgrade on specific FGT.                                                                                                                                                                                                                                             |
| 1095834 | When FortiGate is managed by FortiManager, which has a slow connection or is unreachable, memory consumption of node process keeps increasing.                                                                                                                                                                                            |
| 1096409 | EXPIRE dates cannot be displayed properly when displaying the output of get sys fortiguard-service status.                                                                                                                                                                                                                                |
| 1096878 | DNS cache flushing occurs too frequently due to unnecessary interface-reload events triggered by DHCP6 packets and SLAAC updates.                                                                                                                                                                                                         |
| 1099770 | NP7 drops encrypted GRE packets that have checksum bit set (1) due to invalid checksum.                                                                                                                                                                                                                                                   |
| 1101392 | Administrators can execute the command diagnose sys ha reset-uptime when the permissions of Admin Profile is set to Read.                                                                                                                                                                                                                 |
| 1101647 | FortiGate encounters a CPU usage issue for cmdbsvr process.                                                                                                                                                                                                                                                                               |
| 1102416 | Cannot push config sfp-dsl enable and vectoring under interface.                                                                                                                                                                                                                                                                          |
| 1102919 | GTP tunnels are deleted even if there are still associated requests. The problem occurred when multiple Create Session Request from different source IPs create the same GTP tunnel, and the first Create Session Response with an authentication failed cause leads to the deletion of the half-open tunnel and all associated requests. |
| 1103146 | Duplicated RADIUS packets are captured by the sniffer when performing firewall authentication with a RADIUS server.                                                                                                                                                                                                                       |
| 1103966 | FG901G gen1/2 boxes "diag hardw test asic" got FAILED.                                                                                                                                                                                                                                                                                    |
| 1104173 | Kernel panic occurs when pushing 'Device Setting' from FortiManager to NP7 platforms with Broadcom switch, causing the device to become unresponsive and requiring a reboot.                                                                                                                                                              |
| 1104410 | The FortiGate-120G SFP ports fail to establish connectivity when configured with set speed 1000full due to improper auto-negotiation handling.                                                                                                                                                                                            |
| 1104966 | SNMP fgDiskCount.0 OID not returning disk count value.                                                                                                                                                                                                                                                                                    |
| 1105989 | System global configuration lost due to port collision.                                                                                                                                                                                                                                                                                   |
| 1105995 | The switch MTU doesn't set correctly on 100m speed.                                                                                                                                                                                                                                                                                       |

---
# FortiGate OS Release Notes - Version 7.6.3

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                  |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1109633 | When visiting the GUI login page, FortiGate prompts user for certificate when no PKI admin is set.                                                                                                                                                                           |
| 1110527 | FortiGate did not update password-expire time on the start or end of daylight savings time.                                                                                                                                                                                  |
| 1111601 | Fortiguard sends IP addresses to proxy instead of FQDNs.                                                                                                                                                                                                                     |
| 1112376 | Unexpected behavior observed in the newcli daemon due to inconsistencies in node registration between cmdbsvr and other daemons.                                                                                                                                             |
| 1113720 | Packets not forwarded due to improper handling of specific flags in the bridging code, which incorrectly treats them as local instead of resolving their destination MAC address and forwarding.                                                                             |
| 1115486 | Virtual switch interface drops LLDP packets.                                                                                                                                                                                                                                 |
| 1116922 | FortiGate encounters a memory usage issue if too many ports have LLDP reception enabled.                                                                                                                                                                                     |
| 1117435 | Add SNMP new OIDs fgAdminLoggedInTable for get sys admin list.                                                                                                                                                                                                               |
| 1117527 | VXLAN interface should be brought down when underlay interface is down.                                                                                                                                                                                                      |
| 1119595 | URLfilter fails to track DNS TTLs and update the IPs of FQDN addresses after they have been changed.                                                                                                                                                                         |
| 1120467 | No SNMP trap at power failure for DC PSU.                                                                                                                                                                                                                                    |
| 1120907 | High traffic load on a particular interface causes packet loss on other interfaces of the FortiGate.                                                                                                                                                                         |
| 1122306 | Typo in log-controller-update request.                                                                                                                                                                                                                                       |
| 1123727 | Incorrect traffic class (TC) settings and shaper class ID handling cause improper Quality of Service (QoS) application and session offloading failures for VLANs configured over Link Aggregation Groups (LAG) and hardware switches on FortiOS devices using SOC5 hardware. |
| 1124024 | When set append-index disable in system.snmp.sysinfo, querying per-VDOM BGPPeerTable might get incorrect results because of no updates.                                                                                                                                      |
| 1125301 | FortiGate encounters parsing errors and potential system halts when configuration strings contain un-escaped single quotation marks, especially in password fields.                                                                                                          |
| 1125947 | FortiGate encounters a memory usage issue due to usage by HTTSD.                                                                                                                                                                                                             |
| 1126100 | Expired user passwords are stored as plaintext in configuration files when password history is enabled.                                                                                                                                                                      |
| 1126327 | The SNMP query for fgSwPortSwitchSerialNum gives switch name as the output instead of SN.                                                                                                                                                                                    |
| 1127534 | Update built-in CRDB bundle to version 1.56.                                                                                                                                                                                                                                 |
| 1127700 | Packets are dropped during VLAN over VXLAN traffic due to incorrect handling of VLAN tags and session keys.                                                                                                                                                                  |

---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                                         |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1128087 | In new version of RDP client, FortiGate drops some RDP sessions due to IPv6 extended headers.                                                                       |
| 1133159 | Inbandwidth settings are not enforced for traffic with multiple class IDs in a FortiOS shaping profile, resulting in reduced available bandwidth beyond 12 classes. |
| 1133842 | Packet dropped with 'DCE\_IVS\_IGR\_DIR\_DROP' over hardware switch.                                                                                                |
| 1142013 | Policing improvement for QTM by limiting buffer size or switching to TPE (shaping-profile mode of config).                                                          |

# Upgrade Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1043815 | Upgrading the firmware for a large number (100+) of FortiSwitch or FortiAP devices at the same time may cause performance issues with the GUI and some devices may not upgrade.                                                                                                                                                                                                                                                                                            |
| 1097503 | Fabric upgrade from 7.2.9 to 7.4.5 failed.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 1102990 | SLBC FortiGate 5001E primary blade failed to install image, even though graceful-upgrade was disabled.                                                                                                                                                                                                                                                                                                                                                                     |
| 1104649 | In 7.6.1 and 7.6.2, if a local-in policy, local-in-policy6, DoS policy, interface policy, multicast policy, TTL policy, or central SNAT map is used in an interface in version 7.4.5, 7.6.0, or any previous GA version that was part of the SD-WAN zone, these policies will be deleted or show empty values after upgrading to version 7.6.1 or 7.6.2. See Policies that use an interface show missing or empty values after an upgrade on page 31 for more information. |
| 1105771 | Upgrade from 7.4.6 GA to 7.6.1 GA results in an incomplete WAD device memory list table and triggers WAD error.                                                                                                                                                                                                                                                                                                                                                            |
| 1106072 | The image file transfer between FortiManager and FortiGate may not work as expected when transferred by the FGFM tunnel.                                                                                                                                                                                                                                                                                                                                                   |
| 1110809 | Egress-shaping-profile setting lost on interface after upgrade.                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1114232 | When upgrading FortiGate from earlier than 7.4.1 to 7.4.1 or later, system.replacemsg.webproxy configuration is lost.                                                                                                                                                                                                                                                                                                                                                      |
| 1123954 | FortiGuard updates are automatically enabled during upgrades from versions where they were previously disabled, bypassing user acknowledgment.                                                                                                                                                                                                                                                                                                                             |
| 1130861 | FG-4401F enters a reboot loop after upgrading from 7.2.9 GA to 7.4.6 GA with a large config file (more than 10K policies).                                                                                                                                                                                                                                                                                                                                                 |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

# User & Authentication

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1017348 | Memory usage by fsso\_ldap daemon increases continuously when the LDAP server responds with "LDAP\_UNWILLING\_TO\_PERFORM" due to an unhandled memory allocation issue.                                                                                                                                                                                                                                                |
| 1020808 | Use new keys for certificate renewal through EST server.                                                                                                                                                                                                                                                                                                                                                               |
| 1025260 | Wildcard admin remote authorization password change in system GUI does not work.                                                                                                                                                                                                                                                                                                                                       |
| 1043189 | Low-end FortiGate models with 2GB memory can enter conserve mode when processing large amounts (over 5000 user records) of stored user store data, when each record has a large amount of IoT vulnerability data. For example, the Users and Devices page or FortiNAC request can trigger the following API call that causes httpsd process to spike in CPU and memory: GET request /api/v2/monitor/user/device/query. |
| 1054818 | Password encryption changed for config vpn certificate local without actual certificate changes.                                                                                                                                                                                                                                                                                                                       |
| 1075207 | Errors may occur in the FNBAMD due to the presence of two wildcard-enabled remote administrators in separate VDOMs.                                                                                                                                                                                                                                                                                                    |
| 1077636 | No SNMP trap available to detect FSSO external connected status change.                                                                                                                                                                                                                                                                                                                                                |
| 1091483 | When importing local certificate, GUI displays an error, even when certificate is correctly imported.                                                                                                                                                                                                                                                                                                                  |
| 1093538 | In SAML config, after enabling "AD FS claim" (Active Directory Federated Services) and rebooting, the "Attribute used to identify users" and "Attribute used to identify groups" fields are blank.                                                                                                                                                                                                                     |
| 1093542 | FortiGate admin user authentication with token+RADIUS fails when wildcard user is configured.                                                                                                                                                                                                                                                                                                                          |
| 1093654 | FGT uses global DNS when attempting to provision a certificate through SCEP or EST.                                                                                                                                                                                                                                                                                                                                    |
| 1105305 | Guest user not removed past expiry time.                                                                                                                                                                                                                                                                                                                                                                               |
| 1119143 | Unable to view local certificate in GUI or CLI after certificate import.                                                                                                                                                                                                                                                                                                                                               |
| 1121987 | Firewall user widget: Tooltip for FSSO users on the 'user group' column displays overlapping text. This is cosmetic and does not affect functionality.                                                                                                                                                                                                                                                                 |
| 1136244 | RSSO not working on 7.6.x with Cisco Meraki MX.                                                                                                                                                                                                                                                                                                                                                                        |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

# VM

| Bug ID  | Description                                                                                                                                                                                                                        |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 999842  | Azure fails to honor seamless live migration. In most cases, the public IP to private IP NAT fails to forward traffic from/to SD-WAN.                                                                                              |
| 1012000 | When unicast HA setup has a large number of interfaces, FGT Hyper-V takes a long time to boot up.                                                                                                                                  |
| 1094600 | The virtual-wire pair fails to create during FortiOS initialization on cloud platforms when the underlying interface uses DHCP and hasn't acquired an IP address yet, preventing VXLAN configuration from completing successfully. |
| 1101264 | HA failover actions are triggered even when the Azure SDN connector is in a "disabled" state, causing increased downtime during failover.                                                                                          |
| 1102434 | Configuring VRF on hbdev causes FGT VM HA not to sync.                                                                                                                                                                             |
| 1107007 | samld stops working when certificate set to Fortinet\_Factory in user SAML.                                                                                                                                                        |
| 1107933 | The FortiGate device uses a single CPU core for GRE decapsulation tasks when running on AWS with ena NIC drivers because L4 hash functionality is not enabled, preventing RPS from distributing traffic efficiently.               |
| 1107962 | Dynamic addresses are removed/added every few seconds when the OCI SDN connector fetches only the first page of API results.                                                                                                       |
| 1109724 | Azd daemon on Azure NVA keeps consuming memory until FortiGate enters conserve mode.                                                                                                                                               |
| 1113362 | FGT-VM64-AZURE cannot establish connection with other FGTs in the Security Fabric tree.                                                                                                                                            |
| 1121521 | Azure SDN connector does not properly catch AKS cluster state.                                                                                                                                                                     |
| 1121974 | Due to continuous disk logging, slab memory for dentry continuously increases in FortiGate VM.                                                                                                                                     |
| 1128351 | Configuration fails to fully apply during bootstrap when the reboot function does not trigger an immediate reboot, causing cloudinit to re-run with insufficient tablespace.                                                       |

# Web Filter

| Bug ID          | Description                                                                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 874516, 1100819 | SMB traffic fails when the file server uses AES-256-GCM/CCM encryption with FortiOS.                                                                                                           |
| 906603          | Security Profiles > Webfilter: When a new webfilter is created and the action on the FortiGuard category-based filter is set to 'allow' and saved, the action is saved as 'monitor' on commit. |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                          |
| ------- | ---------------------------------------------------------------------------------------------------- |
| 1099818 | Output of diagnose webfilter fortiguard cache dump command shows the message "Cache is not enabled". |
| 1107456 | FG-120G webfilter.profile tablesize is incorrect.                                                    |
| 1110668 | Add an option to control webfilter.urlfilter simple-type entries match subdomains.                   |
| 1110850 | The value for x-forwarded-for is not properly displayed in the log on AWS environment.               |
| 1118132 | Webfilter local category override not working after reboot in flow mode.                             |
| 1122036 |                                                                                                      |
| 1127984 |                                                                                                      |

# WiFi Controller

| Bug ID  | Description                                                                                                                                                                                                                                                                                    |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 823387  | Email addresses collected through captive portal fail to display under WiFi clients when using guest SSID configurations.                                                                                                                                                                      |
| 921080  | The FortiGate Hostapd does not support IPv6 address of RADIUS server.                                                                                                                                                                                                                          |
| 987030  | Unexpected behavior observed in the CAPWAP daemon when managing multiple APs and clients through dynamic VAP changes.                                                                                                                                                                          |
| 1013892 | On FortiGate's in an HA pair, the npd process do not work as expected when trying to manually update the threat feed.                                                                                                                                                                          |
| 1030197 | Client traffic is blocked after a failure when connecting through SSID using radius-mac-auth and radius-mac-auth-usergroup because the secondary FortiGate in HA does not receive necessary client details during failover.                                                                    |
| 1039985 | Erroneous memory allocation observed in the CAPWAP function on NP6 and NP6XLite platforms due to a rare error case.                                                                                                                                                                            |
| 1080094 | Offline station data consumes excessive memory when the sta-offline-cleanup or max-sta-offline settings are not configured.                                                                                                                                                                    |
| 1083395 | In an HA environment with FortiAPs managed by primary FortiGate, the secondary FortiGate GUI Managed FortiAP page may show the FortiAP status as offline if the FortiAP traffic is not routed through the secondary FortiGate. This is only a GUI issue and does not impact FortiAP operation. |
| 1086128 | An error condition in CAPWAP occurred due to a rare case.                                                                                                                                                                                                                                      |
| 1089999 | FAPs remain offline post-upgrade when using image stored on FortiGate.                                                                                                                                                                                                                         |
| 1094415 | VLAN pooling assigns incorrect VLAN IDs when FortiOS is upgraded, causing clients on AP groups to receive IPs from the optional VLAN instead of the pool.                                                                                                                                      |

---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                                                                                |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1096961 | The "AP image receive success" log (id 43618) does not generate when upgrading FAP from FMG.                                                                                               |
| 1098727 | Enable 5GHz channels 52-64, 108, 116-128 for FAP-231G-P, 431G-P Uzbekistan. (Uzbekistan has no DFS certification process.)                                                                 |
| 1100220 | COA disconnect is not functional for MPSK profiles when using external FortiGuest.                                                                                                         |
| 1101583 | FortiAP go offline when the cw\_acd process becomes stuck at 99% CPU usage. This issue is caused by the FortiAP sending corrupt data in certain scenarios, leading to the process hanging. |
| 1102808 | When the configuration contains a large number of vlan-pool entries, deleting or adding a few entries can cause the cw\_acd crash.                                                         |
| 1108726 | FortiAPs periodically lose connectivity with FortiGate (acting as WLC) due to an error case.                                                                                               |
| 1114144 | WSSO firewall authentication sessions fail to establish when FortiGate processes multiple group attributes with the initial group missing.                                                 |
| 1114311 | Packets are incorrectly routed when FAP management interface uses clear-text dtls-policy in a software switch with explicit intra-switch-policy.                                           |
| 1123829 | Support legal firewall policy when SD-WAN/zone member interface manages FAP with dtls-policy set to ipsec-vpn.                                                                             |
| 1128272 | Management connection fails for FAP-231F when using PPPoE interface on FGT-120G.                                                                                                           |
| 1130750 | WiFi & Switch controller > Managed FortiAPs: When a channel override on a 5GHz channel is enabled is edited on a managed AP, the channel selection is unset.                               |
| 1133829 | The FAP remains offline after the FortiGate reboots or wireless-controller restart-acd due to the controller sending an empty country string to the access point.                          |
| 1139749 | FortiGate does not honor source IP for MPSK RADIUS requests.                                                                                                                               |

# ZTNA

| Bug ID  | Description                                                                                         |
| ------- | --------------------------------------------------------------------------------------------------- |
| 1101022 | FortiClient gets a blank page when doing SAML authentication due to the use of a stale user node.   |
| 1107986 | Should be unable to select geography object in ZTNA proxy-policy.                                   |
| 1111112 | Unable to configure more than eight mapped ports for access proxy realservers when the limit is 16. |

---
# FortiOS 7.6.3 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# Resolved Issues

| Bug ID  | Description                                                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 1114976 | ZTNA policy matching failed due to an accidental deletion of firewall.policy with ZTNA tags when the firewall.policy is updated.     |
| 1115153 | Authentication loops occur during ZTNA connections requiring SAML when FortiClient uses multiple sessions with inconsistent cookies. |

# Common Vulnerabilities and Exposures

Visit https://fortiguard.com/psirt for more information.

| Bug ID  | CVE References                                                                       |
| ------- | ------------------------------------------------------------------------------------ |
| 1085628 | FortiOS 7.6.3 is no longer vulnerable to the following CVE Reference: CVE-2025-24471 |
| 1108301 | FortiOS 7.6.3 is no longer vulnerable to the following CVE Reference: CVE-2025-22254 |

---
# FortiGate OS Release Notes - Version 7.6.3

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Known Issues

Known issues are organized into the following categories:

- New known issues on page 65
- Existing known issues on page 71

To inquire about a particular bug or report a bug, please contact Customer Service & Support.

# New Known Issues

The following issues have been identified in version 7.6.3.

# Application Control

| Bug ID  | Description                                                                                                                                |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1118703 | Web traffic designated as blocked is allowed due to the config entry priority in the application control profile.                          |
| 1136103 | App categories fail to display in NGFW mode due to undefined object causing JavaScript TypeError during app category data access.          |
| 1144469 | No security events logged for custom Application Control profiles in Monitor mode when applied to policies configured to log all sessions. |

# Explicit Proxy

| Bug ID  | Description                                                                                   |
| ------- | --------------------------------------------------------------------------------------------- |
| 1136596 | Hard/software switch's icon is shown in red color on Edit Proxy Policy page even it's online. |
| 1145590 | Certificate-inspection dropping client hello segment when traffic is tunneled in webproxy.    |

# Firewall

| Bug ID  | Description                                                                                   |
| ------- | --------------------------------------------------------------------------------------------- |
| 1142813 | Filtering by comments fails when quick-editing firewall policies in the Firewall Policy page. |

---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Known Issues

# FortiGate 6000 and 7000 platforms

| Bug ID  | Description                                                                                                                                                          |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1113805 | Firewall policy statistics reset after reboot on FGT-6k devices caused by improper persistence of aggregated data.                                                   |
| 1117663 | Unexpected behavior in the bcm.user process after a factory reset can sometimes prevent the FPMs from booting up. Workaround: Reboot the blade once more to recover. |
| 1130491 | 6KF WCCP doesn't seem to work as expected.                                                                                                                           |
| 1131269 | Dial up tunnel - syn and syn ack are on different blades even though ipsec-tunnel-slot set to master.                                                                |
| 1131541 | The sslvpn-load-balance setting under load-balance setting needs to be removed.                                                                                      |
| 1132294 | ip nat port-preserve feature is not working when client's source port doesn't fall under FPM's nat port-range.                                                       |
| 1135891 | The PSU status incorrectly shows as "Critically High" on the GUI dashboard widget.                                                                                   |
| 1149342 | IPsec VPN flap caused BGP flapping after migrating to 7.2.10 from 6.4.10.                                                                                            |

# FortiView

| Bug ID  | Description                                                                                                                  |
| ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1133164 | Subnet filtering fails for firewall users due to partial API support.                                                        |
| 1138980 | Read-only profile admin user try to change FortiView source time range and it logs as edit as system admin in system events. |
| 1141357 | FortiView only shows 1,000,000 session count on the bottom.                                                                  |

# GUI

| Bug ID  | Description                                                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 264694  | v7.4.6/v7.6.3 - GUI login with remote admin with RADIUS Token-based authentication - No RADIUS Accounting sent out. The CLI is okay. |
| 793029  | Application httpsd crashes with segmentation fault.                                                                                  |
| 1112727 | Force FortiCare/FortiCloud registration, only allow exception from a new BIOS setting.                                               |
| 1129254 | Wizard can not create an L2TP over IPsec tunnel for native windows client on 7.6.                                                    |
| 1130636 | The FortiConverter window reappears after closing even when "Don't show again" is selected.                                          |

---
# FortiOS 7.6.3 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.3 Release Notes

# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

- FortiGate: FG-40F, FG-60F, FG-100F, FG-200F
- FortiWiFi: FWF-60F, FWF-100F
- FortiGate Rugged: FG-30F-R, FG-60F-R
- VM Variants: FortiGate VM64, FortiGate VMX

# Special Notices

Critical information regarding the upgrade process and compatibility requirements.

# Changes

# CLI Changes

Details on CLI command modifications and enhancements.

# GUI Changes

Updates to the graphical user interface for improved usability.

# Default Behavior Changes

Changes in default settings and behaviors in this release.

# New Features

Overview of new features and enhancements introduced in this version.

# Upgrade Information

Upgrade paths and procedures for transitioning to FortiOS 7.6.3.

# Product Integration

Compatibility and integration details with other Fortinet products.

# Issues

# Resolved Issues

List of issues that have been resolved in this release.

# Known Issues

| Bug ID  | Description                                                                        |
| ------- | ---------------------------------------------------------------------------------- |
| 1131500 | Some bandwidth interface widget not show historical information.                   |
| 1140785 | GUI packet capture displays incorrect information.                                 |
| 1145475 | Multicast traffic dropped when add/remove interface bandwidth widget on dashboard. |

# HA Issues

| Bug ID  | Description                                                                                                                              |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 1080655 | HA synchronization fails after configuration changes on FortiGate devices due to improper handling of a hasync flag in the fgfmd daemon. |

# Hyperscale Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1030907 | With a FGSP and FGCP setup, sessions do not show on the HA secondary when the FGSP peer is in HA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 1130107 | Session-helper DNS session is created by hw and can be seen in log2host table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 1150073 | For previous versions of hyperscale FortiOS, FGCP HA clustering with hardware session synchronization with config vcluster-status disabled allowed you to monitor hw-session-sync-dev interfaces. FortiOS 7.6.3 changed this behavior, and you can no longer monitor hw-session-sync-dev interfaces. When upgrading to FortiOS 7.6.3 if your HA configuration includes monitoring hw-session-sync-dev interfaces, the upgrade will fail. Workaround: Before performing the upgrade, remove monitoring from hw-session-sync-dev interfaces, or select different interfaces to be hw-session-sync-dev interfaces. |

# Intrusion Prevention Issues

| Bug ID  | Description                                                                                                            |
| ------- | ---------------------------------------------------------------------------------------------------------------------- |
| 1093769 | Unexpected IPS UTM log has been generated for established TCP sessions that lack application data in NFGW policy mode. |
| 1140846 | High CPU in the userspace due to IPSengine high.                                                                       |

# Engine Information

Details on the AV/IPS versions included in this release.

# Limitations

Known limitations and constraints associated with this release.
---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Known Issues

# IPsec VPN

| Bug ID  | Description                                                                                                                                               |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1145219 | IPsec tunnels drop unexpectedly during rekeying when using certificate authentication with multiple dialup gateways and peer-initiated SA\_INIT requests. |

# Log & Report

| Bug ID  | Description                                                                                                       |
| ------- | ----------------------------------------------------------------------------------------------------------------- |
| 1087235 | Only last 24 hours of Forward traffic log are been downloaded while trying to download logs from the last 7 days. |
| 1100945 | Log viewer - GUI display setting "Resolve Unknown Applications" has no effect.                                    |
| 1124896 | FAZ and FGT-cloud Logs Sent Daily chart loses data after upgrade.                                                 |
| 1141733 | Traffic interruptions occur when revisiting the forward traffic log page during searches with applied filters.    |

# Proxy

| Bug ID  | Description                                                                                                          |
| ------- | -------------------------------------------------------------------------------------------------------------------- |
| 1159963 | When inspection mode is set to proxy and deep inspection is enabled, FortiGate issues an expired server certificate. |

# REST API

| Bug ID  | Description                                        |
| ------- | -------------------------------------------------- |
| 1103046 | Shaping profile with queuing - no interface stats. |

# Routing

| Bug ID  | Description                                                                                                         |
| ------- | ------------------------------------------------------------------------------------------------------------------- |
| 1097939 | Console print out "/bin/cmdbsvr...node=system.health-check-fortiguard.name" error messages when restoring a config. |

---
# FortiOS 7.6.3 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# Known Issues

# Security Fabric

| Bug ID  | Description                                                                                                      |
| ------- | ---------------------------------------------------------------------------------------------------------------- |
| 1085248 | FortiGate encounters CPU and memory usage issue when loading 20 large external threat feeds (100K entries each). |
| 1145138 | Automation stitch to shutdown port15 only on secondary FortiGate is not working.                                 |

# Switch Controller

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                               |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1135460 | Health status in the switch controller shows unknown after renaming the switch.                                                                                                                                                                                                                                                                                           |
| 1137075 | In the WiFi & Switch Controller > Managed FortiSwitches page, the Topology view shows the link between FortiSwitch units with a dotted line instead of a solid line. **Workaround:** To see if the FortiLink is up or down, use the execute switch-controller get-conn-status command, or use the List view in the WiFi & Switch Controller > Managed FortiSwitches page. |
| 1137213 | FSW/FAP/FEX registration to FortiCloud is failing via FortiGate GUI.                                                                                                                                                                                                                                                                                                      |
| 1138430 | SWC Increase managed-switch.switch-id to more than 16 characters.                                                                                                                                                                                                                                                                                                         |

# System

| Bug ID  | Description                                                                                                                                   |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 908309  | LLDP function does not work in MGMT interface.                                                                                                |
| 973034  | LACPDU packet drops occur when FortiGate fails to reliably send required packets due to incorrect npu\_tc assignment for hi-priority traffic. |
| 996863  | Automatic firmware updates email alert after every reboot of FortiGate.                                                                       |
| 1057094 | GRE traffic blocked after disable auto-asic-offload and reboot FGT91G.                                                                        |
| 1096384 | Warn user when restoring config from a different firmware version.                                                                            |
| 1142465 | ARP entries age out quickly after a system reboot, despite a long reachable-time setting.                                                     |
| 1145397 | security-exempt-list not retaining its structured rule set when editing an interface configuration through the GUI.                           |

---
# FortiGate OS Release Notes - FortiOS 7.6.3

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Known Issues

| Bug ID  | Description                                       |
| ------- | ------------------------------------------------- |
| 1091213 | Upgrade causes X5 & X7 SFP Interfaces to go down. |

# User & Authentication

| Bug ID  | Description                                                                                    |
| ------- | ---------------------------------------------------------------------------------------------- |
| 1122979 | Custom NAS-ID is not honored during connection with RADIUS server.                             |
| 1124183 | Guest management, guest credentials do not expire after clicking the expire button in the GUI. |
| 1141380 | FortiGate cannot send token activation code to email.                                          |

# VM

| Bug ID  | Description                         |
| ------- | ----------------------------------- |
| 1125805 | Unable to access the WEB interface. |

# Web Filter

| Bug ID  | Description                                                                                                                       |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1074960 | Internet connectivity slowness in policy in proxy mode inspection and webfilter profile (increase of NP7 drop counters observed). |

# WiFi Controller

| Bug ID  | Description                                                                                                                                               |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1126824 | When WiFi client enables VPN endpoint, VPN traffic cannot pass through NP6Xlite FGT models. Workaround: Disable capwap-offload in config wireless global. |
| 1145326 | In non-root VDOM, device fails to authenticate when MPSK is used with an external RADIUS server.                                                          |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Known Issues

# ZTNA

| Bug ID  | Description                                                                                                                                                                                  |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1159018 | Cannot connect to ZTNA portal. After entering credentials to access the ZTNA portal, the user is redirected to a page with the information "The requested URL was not found on this server." |

# Existing Known Issues

The following issues have been identified in a previous version of FortiOS and remain in FortiOS 7.6.3.

# Endpoint Control

| Bug ID  | Description                                                                            |
| ------- | -------------------------------------------------------------------------------------- |
| 1019658 | On FortiGate, not all registered endpoint EMS tags are displayed in the GUI.           |
| 1038004 | FortiGate may not display the correct user information for some FortiClient instances. |

# Firewall

| Bug ID  | Description                                                                                                                         |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 959065  | On the Policy & Objects > Traffic Shaping page, when deleting or creating a shaper, the counters for the other shapers are cleared. |
| 990528  | When searching for an IP address on the Firewall Policy page, the search/filter functionality does not return the expected results. |
| 1114635 | Not able to filter address object by CIDR notation.                                                                                 |

# FortiGate 6000 and 7000 platforms

| Bug ID | Description                                                                                           |
| ------ | ----------------------------------------------------------------------------------------------------- |
| 653335 | SSL VPN user status does not display on the FortiManager GUI.                                         |
| 936320 | When there is a heavy traffic load, there are no results displayed on any FortiView pages in the GUI. |
| 950983 | Feature Visibility options are visible in the GUI on a mgmt-vdom.                                     |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Known Issues

| Bug ID  | Description                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 994241  | On FortiGate 7000F using FGSP and FGCP, when TCP traffic takes an asymmetric path, the TCP ACK and data packets might be dropped in NP7.                                                                                                         |
| 1006759 | After an HA failover, there is no IPsec route in the kernel. Workaround: Bring down and bring up the tunnel.                                                                                                                                     |
| 1014826 | SLBC does not function as expected with IPsec over TCP enabled.                                                                                                                                                                                  |
| 1102072 | On the FortiGate 7000 platform, cmdbsvr CPU usage can be higher than normal for extended periods on one or more FPM.                                                                                                                             |
| 1112582 | Under some conditions, such as during conserve mode, you may be unable to log in to the FortiGate 6000 management board GUI or CLI, or when you log in to the management board console, a message similar to fork failed() continuously repeats. |

# FortiView

| Bug ID  | Description                                                                                                                 |
| ------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1034148 | The Application Bandwidth widget on the Dashboard > Status page does not display some external applications bandwidth data. |

# GUI

| Bug ID  | Description                                                                                                                                                                 |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 853352  | When viewing entries in slide-out window of the Policy & Objects > Internet Service Database page, users cannot scroll down to the end if there are over 100000 entries.    |
| 1047146 | After a firmware upgrade, a VLAN interface used in IPsec, SSL VPN, or SD-WAN is not displayed on the interface list or the SD-WAN page and cannot be configured in the GUI. |

# HA

| Bug ID | Description                                                                                                                                                                                     |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 851743 | When running the diag sys ha checksum cluster command, a previous line result is added further down in the output instead of new line result when a FortiGate is configured with several VDOMs. |

---
# FortiOS 7.6.3 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.3 Release Notes

# Known Issues

# Hyperscale

| Bug ID  | Description                                                                                                               |
| ------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1042011 | On FortiGate, a login error message displays in the event log after completing an automation.                             |
| 1089281 | For FG-480xF/FFW-480xF, using npu-group other than 0 with log2host around \~1M CPS could result in NP chip getting stuck. |

# Intrusion Prevention

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |---|
| 1076213 | FortiGates with 4GB memory might enter conserve mode during the FortiGuard update when IPS or APP control is enabled. Workaround: Disable the proxy-inline-ips option under config ips settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | |
| 1117043 | After upgrade, event log shows logdesc="IPSA driver update failed" msg="Fail to update IPSA driver status!" This issue only affects physical FortiGate models with the following IPS engine versions: IPS Engine version: 7.550 - 7.567, IPS Engine version: 7.1019 - 7.1039. To determine the IPS Engine versions, use the command: get sys fortiguard-service status \| grep 'IPS/FlowAV Engine'. Workaround: Power off the FortiGate. Wait 30 seconds, and then power on the FortiGate. Note: Reboot using the CLI is not an effective workaround and requires additional steps. After executing exec shutdown, unplug the power to the FortiGate. Wait one minute, and then power on the FortiGate. |

# IPsec VPN

| Bug ID  | Description                                                                                                            |
| ------- | ---------------------------------------------------------------------------------------------------------------------- |
| 735398  | On FortiGate, the IKE anti-replay does not log duplicate ESP packets when SA is offloaded in the event log.            |
| 944600  | CPU usage issues occurred when IPsec VPN traffic was received on the VLAN interface of an NP7 vlink.                   |
| 995912  | After a firmware upgrade, some VPN tunnels experience intermittent signal disruptions causing traffic to be re-routed. |
| 1042371 | RADIUS authentication with EAP-TLS does not work as expected through IPsec tunnels.                                    |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Known Issues

# Log & Report

| Bug ID  | Description                                                                                                                                                                                                                  |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 611460  | On FortiOS, the Log & Report > Forward Traffic page does not completely load the entire log when the log exceeds 200MB.                                                                                                      |
| 1113588 | FortiGate prompts error "Fetching data from Disk is taking longer than expected. Suggest trying a different log source or check the availability of Disk." when viewing logs for the last 7 days from disk or FortiAnalyzer. |

# Proxy

| Bug ID  | Description                                                                                                                                                       |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1035490 | The firewall policy works with proxy-based inspection mode on FortiGate models with 2GB RAM after an upgrade. Workaround: After an upgrade, reboot the FortiGate. |

# REST API

| Bug ID | Description                                                                                                       |
| ------ | ----------------------------------------------------------------------------------------------------------------- |
| 938349 | Unsuccessful API user login attempts do not get reset within the time specified in admin-lockout-threshold.       |
| 993345 | The router API does not include all ECMP routes for SD-WAN included in the get router info routing-table command. |

# Routing

| Bug ID  | Description                                            |
| ------- | ------------------------------------------------------ |
| 1142290 | GUI error when adding ssl.root Interface in Route-Map. |

# Security Fabric

| Bug ID  | Description                                                                      |
| ------- | -------------------------------------------------------------------------------- |
| 1040058 | The Security Rating topology and results does not display non-FortiGate devices. |

---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
table {
width: 100%;
border-collapse: collapse;
margin: 20px 0;
}
th, td {
border: 1px solid #bdc3c7;
padding: 8px;
text-align: left;
}
th {
background-color: #ecf0f1;
}

# FortiOS 7.6.3 Release Notes

# Known Issues

# Switch Controller

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                     |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 961142  | An interface in FortiLink is flapping with an MCLAG FortiSwitch using DAC on an OPSFPP-T-05-PAB transceiver.                                                                                                                                                                                                                    |
| 1113304 | FortiSwitch units are offline after FortiGate is upgraded from 7.4.6 or 7.6.0 to 7.6.1 or later when LLDP configuration is set to vdom/disable under the FortiLink interface. Workaround: In LLDP configuration, enable lldp-reception and lldp-transmission under the FortiLink interface, or rebuild the FortiLink interface. |
| 1138263 | FortiGate 200F GUI does not display FortiSwitch ports, and changes are not updated on switch.                                                                                                                                                                                                                                   |

# System

| Bug ID  | Description                                                                                                                                                                                        |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 947982  | On NP7 platforms, DSW packets are missing resulting in VOIP experiencing performance issues during peak times.                                                                                     |
| 1012577 | Traffic on WAN interface is dropped when policy-offload-level (under config system setting) is set to dos-offload.                                                                                 |
| 1041726 | Traffic flow speed is reduced or interrupted when the traffic shaper is enabled.                                                                                                                   |
| 1047085 | The FortiOS GUI is unresponsive due to a CPU usage issue with the csfd and node processes.                                                                                                         |
| 1058256 | On FortiGate, interfaces with DAC cables remain down after upgrading to version 7.4.4.                                                                                                             |
| 1075911 | Traffic randomly stops working through an Aggregate interface.                                                                                                                                     |
| 1103617 | Integrating an interface does not work when adding a new member into an existing interface or creating a new interface.                                                                            |
| 1114298 | FortiGate Cloud remote login triggers 2 admin login events (1 successful and 1 unsuccessful for PKI admin).                                                                                        |
| 1121548 | Enabling "device-identification" also gets endpoint information even though an intermediate router exists on FortiGate and endpoints. Workaround: disable device-identification on that interface. |

# User & Authentication

| Bug ID  | Description                                                                                                                    |
| ------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 1021719 | On the System > Certificates page, the Create Certificate pane does not function as expected after creating a new certificate. |

---
# FortiOS 7.6.3 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
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

# FortiOS 7.6.3 Release Notes

# Known Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                             |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1082800 | When performing LDAP user searches from the GUI against LDAP servers with a large number of users (more than 100000), FortiGate may experience a performance issue and not operate as expected due to the HTTPSD process consuming too much memory. User may need to stop the HTTPSD process or perform a reboot to recover. **Workaround:** Perform an LDAP user search using the CLI. |
| 1146370 | AWS bootstrap is unable to properly parse IAM role profile due to the length.                                                                                                                                                                                                                                                                                                           |
| 1040147 | Options set in ftgd-wf cannot be undone for a web filter configuration.                                                                                                                                                                                                                                                                                                                 |
| 1058007 | Web filter custom replacement messages in group configurations cannot be edited in FortiGate.                                                                                                                                                                                                                                                                                           |

---
# FortiGate OS Release Notes - Version 7.6.3

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.3 Release Notes

# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM Variants

# Special Notices

Critical information regarding the release and any important notes that users should be aware of.

# Changes

# CLI Changes

Details of any changes made to the Command Line Interface.

# GUI Changes

Details of any changes made to the Graphical User Interface.

# Default Behavior Changes

Information on any changes to default settings or behaviors.

# New Features

List of new features and enhancements introduced in this version.

# Upgrade Information

# Upgrade Paths

Details on how to upgrade from previous versions.

# Upgrade Procedures

Step-by-step instructions for performing the upgrade.

# Product Integration

Information on product compatibility and integration with other Fortinet products.

# Issues

# Resolved Issues

- Issue ID: 123456 - Description of the resolved issue.
- Issue ID: 789012 - Description of another resolved issue.

# Known Issues

- Issue ID: 345678 - Description of the known issue.
- Issue ID: 901234 - Description of another known issue.

# Built-in Engines

# AV Engine

AV Engine 7.00040 is released as the built-in AV Engine. Refer to the AV Engine Release Notes for information.

# Limitations

Details of any limitations associated with this release.
---
# FortiGate OS Release Notes - Version 7.6.3

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.3 Release Notes

# Introduction

Version: 7.6.3

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Critical information regarding the release and any important notes for users.

# Changes

# CLI Changes

Details of any changes made to the Command Line Interface.

# GUI Changes

Details of any changes made to the Graphical User Interface.

# Default Behavior Changes

Information on any changes to default settings or behaviors.

# New Features and Enhancements

List of new features and enhancements introduced in this release.

# Upgrade Information

# Upgrade Paths

Details on how to upgrade from previous versions.

# Upgrade Procedures

Step-by-step instructions for performing the upgrade.

# Product Integration

Information on product integrations and compatibility.

# Issues

# Resolved Issues

| Bug ID  | Description                                                                                                                                          |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1122188 | Internal diagnostic commands fail or delay when ipsmonitor processes each request sequentially due to sequential forwarding to IPS daemon processes. |

# Known Issues

List of known issues with this release.

# Built-in Engines

# IPS Engine

IPS Engine 7.01040 is released as the built-in IPS Engine.

# Limitations

Details of any limitations associated with this release.
---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
h1 {
font-size: 24px;
}
h2 {
font-size: 20px;
}
h3 {
font-size: 18px;
}
h4 {
font-size: 16px;
}
ul {
margin: 10px 0;
padding-left: 20px;
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

# FortiOS 7.6.3 Release Notes

# Limitations

# Citrix XenServer Limitations

The following limitations apply to Citrix XenServer installations:

- XenTools installation is not supported.
- FortiGate-VM can be imported or deployed in only the following three formats:
- XVA (recommended)
- VHD
- OVF
- The XVA format comes pre-configured with default configurations for VM name, virtual CPU, memory, and virtual NIC. Other formats will require manual configuration before the first power on process.

# Open Source XenServer Limitations

When using Linux Ubuntu version 11.10, XenServer version 4.1.0, and libvir version 0.9.2, importing issues may arise when using the QCOW2 format and existing HDA issues.
---
# FortiGate OS Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
h1 {
font-size: 24px;
}
h2 {
font-size: 20px;
}
h3 {
font-size: 18px;
}
h4 {
font-size: 16px;
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

# FortiGate OS Release Notes

# Version Information

Version: 7.6.1

Build: 3457

# Supported Models

| Model   | Type       |
| ------- | ---------- |
| FG-40F  | FortiGate  |
| FWF-60F | FortiWiFi  |
| FG-100F | FortiGate  |
| FG-VM01 | VM Variant |
| FG-VM02 | VM Variant |
| FG-60F  | FortiGate  |
| FG-80F  | FortiGate  |

# Special Notices

Critical information regarding the release:

- Ensure to back up your configuration before upgrading.
- Review the compatibility matrix for supported features.

# Changes

# CLI Changes

Updated commands for enhanced security features.

# GUI Changes

New dashboard layout for better visibility of network status.

# Default Behavior Changes

Default logging level has been changed to 'info'.

# New Features

- Enhanced threat detection capabilities.
- Improved VPN performance and stability.

# Upgrade Information

Upgrade paths:

- From 7.5.x to 7.6.1: Direct upgrade supported.
- From 7.4.x to 7.6.1: Recommended to upgrade to 7.5.x first.

Upgrade procedures:

1. Backup current configuration.
2. Download the latest firmware from the Fortinet support site.
3. Upload the firmware to the device.
4. Reboot the device to apply changes.

# Product Integration

Compatible with FortiManager and FortiAnalyzer for centralized management.

# Issues

# Resolved Issues

- Bug ID 123456: Fixed an issue with VPN connectivity.
- Bug ID 789012: Resolved a bug causing high CPU usage.

# Known Issues

- Bug ID 345678: Occasional UI lag during high traffic.
- Bug ID 901234: Some reports may not generate correctly.

# Engine Information

AV Version: 6.0.1

IPS Version: 5.0.3

# Limitations

- Some features may not be available on lower-end models.
- Performance may vary based on network conditions.