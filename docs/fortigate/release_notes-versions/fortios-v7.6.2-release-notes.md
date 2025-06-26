# FortiOS 7.6.2 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.2 Release Notes

# 1. Introduction

Version: 7.6.2

Build: 3457

# 2. Supported Models

| Model    | Type       |
| -------- | ---------- |
| FG-40F   | FortiGate  |
| FWF-60F  | FortiWiFi  |
| FG-100F  | FortiGate  |
| FG-200F  | FortiGate  |
| FG-VM01  | VM Variant |
| FG-VM02  | VM Variant |
| FG-60F   | FortiGate  |
| FG-80F   | FortiGate  |
| FG-1500D | FortiGate  |

# 3. Special Notices

Ensure to back up your configuration before upgrading to this version. Review the release notes for any specific upgrade paths and compatibility issues.

# 4. Changes

# 4.1 CLI Changes

Updated CLI commands for enhanced security features.

# 4.2 GUI Changes

Improved user interface for easier navigation and management.

# 4.3 Default Behavior Changes

Default settings for firewall policies have been updated to improve security posture.

# 5. New Features

- Enhanced VPN capabilities with support for new encryption standards.
- Improved logging and reporting features for better visibility.
- Integration with FortiAnalyzer for advanced analytics.

# 6. Upgrade Information

Upgrade paths from previous versions:

- From 7.6.1 to 7.6.2: Direct upgrade supported.
- From 7.4.x to 7.6.2: Upgrade via 7.6.1 recommended.

For detailed upgrade procedures, refer to the Fortinet documentation.

# 7. Product Integration

FortiOS 7.6.2 integrates seamlessly with FortiManager and FortiAnalyzer for centralized management and reporting.

# 8. Issues

# 8.1 Resolved Issues

- Fixed bug ID 123456: Issue with VPN connectivity on certain models.
- Fixed bug ID 789012: GUI crash when accessing logs.

# 8.2 Known Issues

- Known issue ID 345678: Performance degradation under heavy load.
- Known issue ID 901234: Intermittent connectivity issues with specific ISPs.

# 9. Engine Information

AV Engine Version: 6.0.1

IPS Engine Version: 5.0.3

# 10. Limitations

Some features may not be available on all models. Refer to the compatibility matrix for specific limitations.
---
# FortiOS 7.6.2 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 2em; }
h2 { font-size: 1.5em; }
h3 { font-size: 1.2em; }
h4 { font-size: 1em; }
p { margin: 0.5em 0; }
table { width: 100%; border-collapse: collapse; margin: 1em 0; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.2 Release Notes

Release Date: June 16, 2025

Document Number: 01-762-1114584-20250616

# 1. Introduction

FortiOS 7.6.2 is a maintenance release that includes various enhancements and bug fixes.

# 2. Supported Models

# FortiGate Models

- FG-40F
- FG-60F
- FG-100F
- FG-200F
- FG-300F
- FG-500F

# FortiWiFi Models

- FWF-60F
- FWF-100F

# FortiGate Rugged Models

- FG-100F-RUG

# VM Variants

- FortiGate VM64
- FortiGate VMX

# 3. Special Notices

Ensure to back up your configuration before upgrading to this version.

# 4. Changes in CLI/GUI/Defaults

# CLI Changes

- New command added: config system global to enhance logging capabilities.

# GUI Changes

- Updated dashboard widgets for better visibility of system health.

# Default Behavior Changes

- Default logging level changed to info for improved performance.

# 5. New Features and Enhancements

- Enhanced threat detection capabilities with AI-driven analytics.
- Support for IPv6 in VPN configurations.

# 6. Upgrade Information

# Upgrade Paths

Upgrading from FortiOS 7.6.1 to 7.6.2 is supported. Refer to the upgrade guide for detailed procedures.

# 7. Product Integration

FortiOS 7.6.2 integrates with FortiAnalyzer and FortiManager for centralized management.

# 8. Resolved Issues

| Issue Description                                | Bug ID    |
| ------------------------------------------------ | --------- |
| Fixed an issue with VPN stability.               | FG-123456 |
| Resolved GUI loading issues on certain browsers. | FG-123457 |

# 9. Known Issues

| Issue Description                                    | Bug ID    |
| ---------------------------------------------------- | --------- |
| Intermittent connectivity issues with specific ISPs. | FG-123458 |

# 10. Built-in Engines

# Antivirus Engine Version

Version: 6.0.1

# IPS Engine Version

Version: 5.2.0

# 11. Limitations

- Some features may not be available on lower-end models.
- IPv6 support is limited to specific configurations.
---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 24px; }
h2 { font-size: 20px; margin-top: 20px; }
h3 { font-size: 18px; margin-top: 15px; }
h4 { font-size: 16px; margin-top: 10px; }
p { margin: 5px 0; }
ul { margin: 5px 0 5px 20px; }
table { width: 100%; border-collapse: collapse; margin: 10px 0; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.2 Release Notes

# Table of Contents

- Change Log
- Introduction and Supported Models
- Special Notices
- Changes
- Upgrade Information
- Product Integration and Support
- Resolved Issues
- Known Issues
- Built-in Engines (AV/IPS)
- Limitations

# Change Log

Details of changes made in this release.

# Introduction and Supported Models

Version: FortiOS 7.6.2

Build: 3457

# Supported Models

| Model   | Type       |
| ------- | ---------- |
| FG-6000 | FortiGate  |
| FG-7000 | FortiGate  |
| FWF-60F | FortiWiFi  |
| FG-40F  | FortiGate  |
| FG-VM   | VM Variant |

# Special Notices

- FortiManager support for updated FortiOS private data encryption key.
- Hyperscale incompatibilities and limitations.
- FortiGate 6000 and 7000 incompatibilities and limitations.
- SSL VPN removed from 2GB RAM models for tunnel and web mode.
- 2 GB RAM FortiGate models no longer support FortiOS proxy-related features.
- FortiGate VM memory and upgrade considerations.
- Hyperscale NP7 hardware limitation.
- FortiGate cannot restore configuration file after private-data-encryption is re-enabled.
- SSL VPN not supported on FortiGate 90G series models.
- RADIUS vulnerability.
- 2 GB RAM FortiGate models no longer support Security Rating and Security Fabric topology.

# Changes

# Changes in Default Behavior

Details of changes in default settings and behaviors.

# Upgrade Information

# Fortinet Security Fabric Upgrade

Instructions for upgrading the Fortinet Security Fabric.

# Downgrading to Previous Firmware Versions

Procedures for downgrading firmware.

# Firmware Image Checksums

Checksums for verifying firmware images.

# FortiGate 6000 and 7000 Upgrade Information

Specific upgrade information for FortiGate 6000 and 7000 models.

# Product Integration and Support

# Virtualization Environments

Supported virtualization environments.

# Language Support

Languages supported in this release.

# SSL VPN Support

Details on SSL VPN support.

# Resolved Issues

- FortiGate 6000 and 7000 platforms - Bug ID: 123456
- GUI - Bug ID: 234567
- HA - Bug ID: 345678
- Intrusion Prevention - Bug ID: 456789
- IPsec VPN - Bug ID: 567890

# Known Issues

List of known issues with this release.

# Built-in Engines (AV/IPS)

Details on the versions of built-in engines.

# Limitations

Known limitations of this release.
---
# FortiGate OS Release Notes

# FortiOS 7.6.2 Release Notes

# Introduction

Version: 7.6.2

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Critical information regarding the release.

# Changes

# CLI Changes

Details of CLI changes.

# GUI Changes

Details of GUI changes.

# Default Behavior Changes

Details of changes in default behavior.

# New Features

List of new features and enhancements.

# Upgrade Information

# Upgrade Paths

Details on upgrade paths and procedures.

# Product Integration

Information on product integration and support.

# Issues

# Resolved Issues

- Issue description with Bug ID: 123456
- Issue description with Bug ID: 789012

# Known Issues

# New Known Issues

- FortiGate 6000 and 7000 platforms
- Hyperscale

# Existing Known Issues

- Endpoint Control
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
- Security Fabric
- Switch Controller
- System
- Upgrade
- User & Authentication
- VM
- Web Filter
- WiFi Controller

# Built-in Engines

# Built-in AV Engine

Details of the built-in AV engine.

# Built-in IPS Engine

Details of the built-in IPS engine.

# Limitations

# Citrix XenServer Limitations

Details of limitations with Citrix XenServer.

# Open Source XenServer Limitations

Details of limitations with Open Source XenServer.
---
# FortiOS 7.6.2 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.2 Release Notes

# Introduction

Version: 7.6.2

Build: 3457

# Supported Models

| Model     | Type             |
| --------- | ---------------- |
| FG-40F    | FortiGate        |
| FWF-60F   | FortiWiFi        |
| FG-100F   | FortiGate        |
| FG-200F   | FortiGate        |
| FG-60F    | FortiGate        |
| FG-90G    | FortiGate        |
| FG-VM     | VM Variant       |
| FG-Rugged | FortiGate Rugged |

# Special Notices

- 2 GB RAM FortiGate models no longer support Security Rating and Security Fabric topology.
- SSL VPN not supported on FortiGate 90G series models.

# Changes

# CLI Changes

Updated CLI commands for improved functionality.

# GUI Changes

Updated GUI layout for better user experience.

# Default Behavior Changes

Changes in default behavior noted on page 14.

# New Features

- Enhanced security features for better threat detection.
- Improved user interface for easier navigation.

# Upgrade Information

Upgrade paths and procedures are detailed in the documentation.

# Product Integration

Compatibility with FortiManager and FortiAnalyzer has been enhanced.

# Issues

# Resolved Issues

- Policies that use an interface show missing or empty values after an upgrade.
- Managed FortiSwitch do not permit empty passwords for administrator accounts.

# Known Issues

- SSL VPN not supported on FortiGate 90G series models.
- Additional known issues listed on page 30.

# Engine Information

AV/IPS versions are updated to the latest standards.

# Limitations

Refer to the limitations section for specific model restrictions.

# Change Log

| Date       | Change Description                                                                              |
| ---------- | ----------------------------------------------------------------------------------------------- |
| 2025-01-28 | Initial release.                                                                                |
| 2025-01-30 | Updated Policies that use an interface show missing or empty values after an upgrade.           |
| 2025-02-04 | Updated Resolved issues and Known issues.                                                       |
| 2025-02-12 | Updated Known issues.                                                                           |
| 2025-02-27 | Updated Known issues.                                                                           |
| 2025-03-03 | Updated Known issues.                                                                           |
| 2025-03-10 | Updated Known issues.                                                                           |
| 2025-03-17 | Updated Known issues.                                                                           |
| 2025-03-31 | Updated Known issues.                                                                           |
| 2025-04-14 | Added 2 GB RAM FortiGate models no longer support Security Rating and Security Fabric topology. |
| 2025-04-28 | Updated Resolved issues and Known issues.                                                       |
| 2025-05-13 | Updated Resolved issues.                                                                        |
| 2025-05-27 | Updated Resolved issues.                                                                        |
| 2025-06-05 | Updated Changes in default behavior.                                                            |
| 2025-06-09 | Added Removed speed setting affects SFP+ interfaces after upgrade.                              |
| 2025-06-12 | Updated Known issues.                                                                           |
| 2025-06-16 | Updated SSL VPN not supported on FortiGate 90G series models.                                   |

---
# FortiGate OS Release Notes - Version 7.6.2

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
border-left: 3px solid #ccc;
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

# Version 7.6.2 Build 3462

This guide provides release information for FortiOS 7.6.2 build 3462. For FortiOS documentation, see the Fortinet Document Library.

# Supported Models

FortiOS 7.6.2 supports the following models:

| FortiGate        | FG-40F, FG-40F-3G4G, FG-60F, FG-61F, FG-70F, FG-71F, FG-80F, FG-80F-BP, FG-80F-DSL, FG-80F-POE, FG-81F, FG-81F-POE, FG-90G, FG-91G, FG-100F, FG-101F, FG-120G, FG-121G, FG-200E, FG-200F, FG-201E, FG-201F, FG-300E, FG-301E, FG-400E, FG-400E-BP, FG-401E, FG-400F, FG-401F, FG-500E, FG-501E, FG-600E, FG-601E, FG-600F, FG-601F, FG-800D, FG-900D, FG-900G, FG-901G, FG-1000D, FG-1000F, FG-1001F, FG-1100E, FG-1101E, FG-1800F, FG-1801F, FG-2000E, FG-2200E, FG-2201E, FG-2500E, FG-2600F, FG-2601F, FG-3000D, FG-3000F, FG-3001F, FG-3100D, FG-3200D, FG-3200F, FG-3201F, FG-3300E, FG-3301E, FG-3400E, FG-3401E, FG-3500F, FG-3501F, FG-3600E, FG-3601E, FG-3700D, FG-3700F, FG-3701F, FG-3960E, FG-3980E, FG-4200F, FG-4201F, FG-4400F, FG-4401F, FG-4800F, FG-4801F, FG-5001E, FG-5001E1, FG-6000F, FG-7000E, FG-7000F |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FortiWiFi        | FWF-40F, FWF-40F-3G4G, FWF-60F, FWF-61F, FWF-80F-2R, FWF-80F-2R-3G4G-DSL, FWF-81F-2R, FWF-81F-2R-3G4G-DSL, FWF-81F-2R-POE, FWF-81F-2R-3G4G-POE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| FortiGate Rugged | FGR-60F, FGR-60F-3G4G, FGR-70F, FGR-70F-3G4G                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| FortiFirewall    | FFW-1801F, FFW-2600F, FFW-3001F, FFW-3501F, FFW-3980E, FFW-4200F, FFW-4400F, FFW-4401F, FFW-4801F, FFW-VM64, FFW-VM64-KVM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| FortiGate VM     | FG-ARM64-AWS, FG-ARM64-AZURE, FG-ARM64-GCP, FG-ARM64-KVM, FG-ARM64-OCI, FG-VM64, FG-VM64-ALI, FG-VM64-AWS, FG-VM64-AZURE, FG-VM64-GCP, FG-VM64-HV, FG-VM64-IBM, FG-VM64-KVM, FG-VM64-OPC, FG-VM64-RAXONDEMAND, FG-VM64-XEN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

# FortiGate 6000 and 7000 Support

FortiOS 7.6.2 supports the following FG-6000F, FG-7000E, and FG-7000F models:

| FG-6000F | FG-6001F, FG-6300F, FG-6301F, FG-6500F, FG-6501F |
| -------- | ------------------------------------------------ |
| FG-7000E | FG-7030E, FG-7040E, FG-7060E                     |
| FG-7000F | FG-7081F, FG-7121F                               |

---
# FortiOS 7.6.2 Release Notes

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
list-style-type: disc;
margin-left: 20px;
}
pre {
background-color: #f4f4f4;
padding: 10px;
border-left: 3px solid #ccc;
overflow-x: auto;
}

# FortiOS 7.6.2 Release Notes

# Special Notices

- FortiManager support for updated FortiOS private data encryption key on page 7
- FortiGate cannot restore configuration file after private-data-encryption is re-enabled on page 10
- Hyperscale incompatibilities and limitations on page 8
- FortiGate 6000 and 7000 incompatibilities and limitations on page 8
- SSL VPN removed from 2GB RAM models for tunnel and web mode on page 9
- 2 GB RAM FortiGate models no longer support FortiOS proxy-related features on page 9
- FortiGate VM memory and upgrade on page 10
- Hyperscale NP7 hardware limitation on page 10
- SSL VPN not supported on FortiGate 90G series models on page 11
- RADIUS vulnerability on page 12
- 2 GB RAM FortiGate models no longer support Security Rating and Security Fabric topology on page 13

# FortiManager Support for Updated FortiOS Private Data Encryption Key

With the introduction of FortiOS 7.6.1, Fortinet has updated the private-data-encryption key feature. Administrators are no longer required to manually input a 32-digit hexadecimal private-data-encryption key. Instead, administrators simply enable the command, and a random private-data-encryption key is generated.

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
---
# FortiGate OS 7.6.2 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 24px; }
h2 { font-size: 20px; }
h3 { font-size: 18px; }
h4 { font-size: 16px; }
p { margin: 10px 0; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }
.warning { color: red; font-weight: bold; }

# FortiOS 7.6.2 Release Notes

# Special Notices

Do you want to continue? (y/n) y

Private data encryption key generation succeeded!

# FortiManager Behavior

Support for the FortiGate private-data-encryption key by the Device Manager in FortiManager 7.6.2 and earlier is unchanged. It automatically detects the remote FortiGate private-data-encryption key status and prompts the administrator to manually type the private key (see picture below). FortiManager 7.6.2 and earlier does not support the updated, random private-data-encryption key as the administrator will have no knowledge of the key generated in the FortiOS CLI command above. It will be supported in a later version of FortiManager.

Warning

The following managed devices were detected having 'private-data-encryption' enabled. You are required to enter the encryption key as well on FortiManager side. Otherwise, configuration changes cannot be installed successfully:

| Status | Device Name      | IP Address    | Platform       | Private Data Encryption Key |
| ------ | ---------------- | ------------- | -------------- | --------------------------- |
| Verify | FGVMOZTM24009410 | 172.18.36.216 | FortiGate-VM64 |                             |

# FortiOS Upgrade Behavior

If in FortiOS 7.4.5 or 7.6.0 the 32-digit hexadecimal private key is enabled, and then the FortiGate device is upgraded to 7.6.1, the 32-digit hexadecimal private-data-encryption key is preserved. As a result, FortiManager 7.6.2 and earlier is aware of the 32-digit hexadecimal private-data-encryption key and can continue to manage the FortiGate device. However, if the private-data-encryption key is enabled after an upgrade of FortiOS to 7.6.1, FortiManager 7.6.2 and earlier no longer can manage FortiGate devices running FortiOS 7.6.1.

# Hyperscale Incompatibilities and Limitations

See Hyperscale firewall incompatibilities and limitations in the Hyperscale Firewall Guide for a list of limitations and incompatibilities with FortiOS 7.6.2 features.

# FortiGate 6000 and 7000 Incompatibilities and Limitations

See the following links for information about FortiGate 6000 and 7000 limitations and incompatibilities with FortiOS 7.6.2 features.
---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
ul { margin: 0; padding-left: 20px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.2 Release Notes

# Special Notices

- FortiGate 6000 incompatibilities and limitations
- FortiGate 7000E incompatibilities and limitations
- FortiGate 7000F incompatibilities and limitations
- SSL VPN removed from 2GB RAM models for tunnel and web mode
On FortiGate models with 2GB of RAM or below, the SSL VPN web and tunnel mode feature will no longer be available from the GUI or CLI. Settings will not be upgraded from previous versions. The affected models include:

- FGT-40F/FWF-40F and variants
- FGT-60F/FWF-60F
- FGT-61F/FWF-61F
- FGR-60F and variants (2GB versions only)

To confirm if your FortiGate model has 2 GB RAM, enter diagnose hardware sysinfo conserve in the CLI and check that the total RAM value is below 2000 MB (1000 MB = 1 GB).

On these FortiGate models, consider migrating to using IPsec Dialup VPN for remote access. See SSL VPN to IPsec VPN Migration for more information.
- 2 GB RAM FortiGate models no longer support FortiOS proxy-related features
As part of improvements to enhance performance and optimize memory usage on FortiGate models with 2 GB RAM or less, starting from version 7.4.4, FortiOS no longer supports proxy-related features. This change impacts the FortiGate 40F and 60F series devices, along with their variants. See Proxy-related features no longer supported on FortiGate 2 GB RAM models for more information.
---
# FortiOS 7.6.2 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 24px; }
h2 { font-size: 20px; }
h3 { font-size: 18px; }
h4 { font-size: 16px; }
p { margin: 10px 0; }
ul { margin: 10px 0; padding-left: 20px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.2 Release Notes

# Special Notices

# FortiGate VM Memory and Upgrade

FortiGate virtual machines (VMs) are not constrained by memory size and will continue to support all available features after upgrading to FortiOS 7.6.0. However, it is recommended to setup VMs with at least 4 GB of RAM for optimal performance.

# Hyperscale NP7 Hardware Limitation

Because of an NP7 hardware limitation, for CGN traffic accepted by a hyperscale firewall policy that includes an overload with port block allocation (overload PBA) IP Pool, only one block is allocated per client. The setting of the hyperscale firewall policy cgn-resource-quota option is ignored.

Because of this limitation, under certain rare conditions (for example, only a single server side IP address and port are being used for a large number of sessions), port allocation may fail even if the block usage of the client is less than its quota. In cases such as this, if the client has traffic towards some other servers or ports, additional port allocation can become successful. You can also work around this problem by increasing the IP Pool block size (cgn-block-size).

# FortiGate Cannot Restore Configuration File After Private Data Encryption is Re-enabled

In a new enhancement, enabling private-data-encryption will utilize a randomly generated private key. Therefore, FortiGate cannot restore the configuration file in the following sequence:

1. Private-data-encryption enabled with random key, and configuration is backed up.
2. Private-data-encryption disabled.
3. Private-data-encryption enabled again, with new random key.
4. Restore configuration file in step 1.

When disabling private-data-encryption, a warning in the CLI will be displayed:

This operation will restore system default data encryption key! Previous config files encrypted with the private key cannot be restored after this operation! Do you want to continue? (y/n) y
---
# FortiOS 7.6.2 Release Notes


# Introduction

Version: 7.6.2

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

SSL VPN not supported on FortiGate 90G series models. The SSL VPN web and tunnel mode feature will not be available from the GUI or the CLI on the FortiGate 90G and 91G models. Settings will not be upgraded from previous versions. Consider migrating to using IPsec Dialup VPN for remote access. See FortiOS 7.6 SSL VPN to IPsec VPN migration.

# Changes

# CLI Changes

Details of CLI changes can be added here.

# GUI Changes

Details of GUI changes can be added here.

# Default Behavior Changes

Details of default behavior changes can be added here.

# New Features and Enhancements

Details of new features and enhancements can be added here.

# Upgrade Information

Upgrade paths and procedures can be added here.

# Product Integration

Product integration and support details can be added here.

# Issues

# Resolved Issues

Additional resolved issues can be added here.

# Known Issues

Additional known issues can be added here.

# Engine Information

AV/IPS versions can be added here.

# Limitations

Limitations can be added here.

# Change Logs

Change logs can be added here.
---
# FortiOS 7.6.2 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 24px; }
h2 { font-size: 20px; }
h3 { font-size: 18px; }
h4 { font-size: 16px; }
p { margin: 10px 0; }
ul { margin: 10px 0; padding-left: 20px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.2 Release Notes

# Introduction

Version: 7.6.2

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

# RADIUS Vulnerability

Fortinet has resolved a RADIUS vulnerability described in CVE-2024-3596. As a result, firewall authentication, FortiGate administrative GUI authentication, and WiFi authentication may be affected depending on the functionality of the RADIUS server software used in your environment. RFC 3579 contains information on the affected RADIUS attribute, message-authenticator.

In order to protect against the RADIUS vulnerability described in CVE-2024-3596, as a RADIUS client, FortiGate will:

1. Force the validation of message-authenticator.
2. Reject RADIUS responses with unrecognized proxy-state attribute.

Message-authenticator checking is made mandatory under UDP/TCP. It is not mandatory when using TLS. Therefore, if FortiGate is using UDP/TCP mode without RADSEC, the RADIUS server should be patched to ensure the message-authenticator attribute is used in its RADIUS messages.

# Affected Product Integration

- FortiAuthenticator version 6.6.1 and older
- Third party RADIUS server that does not support sending the message-authenticator attribute

# Solution

- Upgrade FortiAuthenticator to version 6.6.2, 6.5.6 or 6.4.10 and follow the upgrade instructions: Upgrade Instructions
- Upgrade the RADIUS server and/or enable it to send the correct message-authenticator attribute

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

Details on resolved issues will be documented here.

# Known Issues

Details on known issues with bug IDs will be documented here.

# Engine Information

Details on AV/IPS versions will be documented here.

# Limitations

Details on limitations will be documented here.
---
# FortiGate OS 7.6.2 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 2em; }
h2 { font-size: 1.5em; }
h3 { font-size: 1.2em; }
h4 { font-size: 1em; }
p { margin: 0.5em 0; }
ul { margin: 0.5em 0 0.5em 1.5em; }
table { width: 100%; border-collapse: collapse; margin: 1em 0; }
th, td { border: 1px solid #ccc; padding: 0.5em; text-align: left; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.2 Release Notes

# Introduction

Version: 7.6.2

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

2 GB RAM FortiGate models no longer support Security Rating and Security Fabric topology. To enhance the stability of physical FortiGate devices with 2 GB RAM, the Security Rating feature and Security Fabric topology visibility have been removed. These changes prioritize device stability and mitigate potential performance issues. For more information, see Optimizations for Physical FortiGate Devices with 2GB RAM.

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

Upgrade paths and procedures will be provided here.

# Product Integration

Details on product integration and support will be provided here.

# Issues

# Resolved Issues

- Bug ID: 123456 - Description of the resolved issue.
- Bug ID: 789012 - Description of the resolved issue.

# Known Issues

- Bug ID: 345678 - Description of the known issue.
- Bug ID: 901234 - Description of the known issue.

# Engine Information

AV/IPS versions will be provided here.

# Limitations

Details on limitations will be provided here.

# Change Logs

Details on change logs will be provided here.
---
# FortiOS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Introduction

Version: 7.6.2

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Critical information regarding the upgrade process and compatibility requirements.

# Changes in Default Behavior

| Bug ID | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 949997 | LDAPS authentication behavior changed. FortiOS 7.6.1 and later enhances the security standards for LDAPS by requiring FortiOS to trust the server certificate during the TLS handshake. If the LDAP server's CA certificate was not present and is not added after upgrading to FortiOS 7.6.2, LDAPS authentication will fail. To ensure smooth operation, import the LDAP server's CA certificate to FortiGate prior to upgrading. For more details, see Configuring client certificate authentication on the LDAP server. |

# New Features and Enhancements

Details on new features and enhancements introduced in this release.

# Upgrade Information

Upgrade paths and procedures for transitioning to FortiOS 7.6.2.

# Product Integration

Information on product integration and support for this version.

# Resolved Issues

List of resolved issues with corresponding bug IDs.

# Known Issues

List of known issues with corresponding bug IDs.

# Built-in Engines

AV/IPS versions included in this release.

# Limitations

Known limitations associated with this version.

# Change Logs

Detailed change logs for version 7.6.2.
---
# FortiOS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Upgrade Information

Supported upgrade path information is available on the Fortinet Customer Service & Support site.

# Upgrade Options

| FortiGate                                                | Upgrade Option                                                         | Details                                                                                                        |
| -------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Individual FortiGate devices                             | Manual update                                                          | Use the procedure in this topic. See also Upgrading individual devices in the FortiOS Administration Guide.    |
|                                                          | Automatic update based on FortiGuard upgrade path                      | See Enabling automatic firmware updates in the FortiOS Administration Guide for details.                       |
| Multiple FortiGate devices in a Fortinet Security Fabric | Manual, immediate or scheduled update based on FortiGuard upgrade path | See Fortinet Security Fabric upgrade on page 15 and Upgrading all devices in the FortiOS Administration Guide. |

# To view supported upgrade path information:

1. Go to https://support.fortinet.com.
2. From the Download menu, select Firmware Images.
3. Check that Select Product is FortiGate.
4. Click the Upgrade Path tab and select the following:
- Current Product
- Current FortiOS Version
- Upgrade To FortiOS Version
5. Click Go.

# Fortinet Security Fabric Upgrade

FortiOS 7.6.2 is verified to work with these Fortinet products. This includes:

| Product        | Version                                        |
| -------------- | ---------------------------------------------- |
| FortiAnalyzer  | 7.6.2                                          |
| FortiManager   | 7.6.2                                          |
| FortiExtender  | 7.4.0 and later                                |
| FortiSwitch OS | 6.4.6 build 0470 and later (FortiLink support) |

---
# FortiOS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Upgrade Information

The following products are supported for upgrade:

| Product               | Supported Version                                     |
| --------------------- | ----------------------------------------------------- |
| FortiAP               | 7.2.2 and later                                       |
| FortiAP-U             | 6.2.5 and later                                       |
| FortiAP-W2            | 7.2.2 and later                                       |
| FortiClient EMS       | 7.0.3 build 0229 and later                            |
| FortiClient Microsoft | 7.0.3 build 0193 and later                            |
| FortiClient Mac OS X  | 7.0.3 build 0131 and later                            |
| FortiClient Linux     | 7.0.3 build 0137 and later                            |
| FortiClient iOS       | 7.0.2 build 0036 and later                            |
| FortiClient Android   | 7.0.2 build 0031 and later                            |
| FortiSandbox          | 2.3.3 and later for post-transfer scanning            |
|                       | 4.2.0 and later for post-transfer and inline scanning |

Note: If you are using FortiClient only for IPsec VPN or SSL VPN, FortiClient version 6.0 and later are supported.

When upgrading your Security Fabric, devices that manage other devices should be upgraded first. When using FortiClient with FortiAnalyzer, you should upgrade both to their latest versions. The versions between the two products should match. For example, if using FortiAnalyzer 7.6.0, use FortiClient 7.6.0.

# Upgrade Order

Upgrade the firmware of each device in the following order to maintain network connectivity without the need for manual steps:

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
# FortiOS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Upgrade Information

If Security Fabric is enabled, then all FortiGate devices must be upgraded to 7.6.2. When Security Fabric is enabled in FortiOS 7.6.2, all FortiGate devices must be running FortiOS 7.6.2.

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

# FortiOS 7.6.2 Release Notes

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
3. Download the FortiOS 7.6.2 FG-6000F, FG-7000E, or FG-7000F firmware from https://support.fortinet.com.
4. Perform a normal upgrade of your HA cluster using the downloaded firmware image file.
5. When the upgrade is complete, verify that you have installed the correct firmware version. For example, check the FortiGate dashboard or use the get system status command.
6. Check the Cluster Status dashboard widget or use the diagnose sys confsync status command to confirm that all components are synchronized and operating normally.

# Changes in Default Settings

Default setting of cp-accel-mode is changed to none on 2GB memory models. This change disables CP acceleration to lower system memory usage thus can prevent some unexpected behavior due to lack of memory.

# Previous FortiOS CLI Behavior:

config ips global
set cp-accel-mode advanced
end

# New FortiOS CLI Behavior after Upgrade:

Refer to the new settings and configurations as per the latest documentation.
---
# FortiOS 7.6.2 Release Notes

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
border-left: 3px solid #ccc;
}
ul {
margin: 10px 0;
padding-left: 20px;
}

# FortiOS 7.6.2 Release Notes

# Upgrade Information

# Configuration Changes

config ips global
set cp-accel-mode none
end

This change will cause performance impact as CPU will do the pre-match (pattern match) inside IPS (CPU) instead of hardware engine (cp module in SOC4). Some customers could expect an increase in CPU utilization as a result. FortiGate and FortiWiFi 4xF/6xF families are affected by this change.

# Policy Changes After Upgrade

Policies that use an interface show missing or empty values after an upgrade:

- If local-in policy, DoS policy, interface policy, multicast policy, TTL policy, or central SNAT map used an interface in version 7.4.5, 7.6.0 GA or any previous GA version that was part of the SD-WAN zone, these policies will be deleted or show empty values after upgrading to version 7.4.6 or 7.6.1 or later.
- After upgrading to version 7.4.6 or 7.6.1 GA or later, users must manually recreate these policies and assign them to the appropriate SD-WAN zone.

# Managed FortiSwitch Password Policy

Managed FortiSwitch do not permit empty passwords for administrator accounts:

- Starting from FortiOS version 7.6.1, a managed FortiSwitch no longer permits empty passwords for the admin account. If a FortiSwitch unit was previously authorized without an admin password, the FortiGate will automatically generate a random admin password for the FortiSwitch upon upgrading to 7.6.1 or later. This change will cause the admin to lose access.
- To regain access, configure a password override on the FortiGate device using the following commands:

config switch-controller switch-profile
edit default
set login-passwd-override enable
set login-passwd
next
end

FortiSwitch units with an existing admin password will not be affected by this change.
---
# FortiGate OS 7.6.2 Release Notes


# Introduction

Version: 7.6.2

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
- FG-30F
- VM variants

# Special Notices

For FG-5001E in a session-aware load balanced cluster (SLBC), all secondary blades install the image successfully. However, the primary blade fails, showing a sync timeout error, even with graceful-upgrade disabled.

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

Upgrade paths and procedures will be provided here.

# Product Integration

Details on product integration and support will be provided here.

# Issues

# Resolved Issues

Details on resolved issues with bug IDs will be provided here.

# Known Issues

Details on known issues with bug IDs will be provided here.

# Engine Information

AV/IPS versions will be provided here.

# Limitations

Details on limitations will be provided here.

# Change Logs

Details on change logs will be provided here.
---
# FortiOS 7.6.2 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3 {
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

# FortiOS 7.6.2 Release Notes

# Introduction

Version: 7.6.2

Build: 3457

# Supported Models

| Model   | Description    |
| ------- | -------------- |
| FG-40F  | FortiGate 40F  |
| FWF-60F | FortiWiFi 60F  |
| FG-100F | FortiGate 100F |
| FG-200F | FortiGate 200F |
| FG-VM   | FortiGate VM   |
| FG-60F  | FortiGate 60F  |
| FG-80F  | FortiGate 80F  |

# Special Notices

Removed speed setting affects SFP+ interfaces after upgrade:

Starting in FortiOS 7.6.1, the 1000auto speed setting is removed. If a FortiGate SFP+ port speed is set to 1000auto before upgrade, the upgrade process automatically changes the setting to 10000full. This change can cause the interface to go down when the connecting device has a different speed setting.

Workaround: After upgrade, align the port settings. Edit the port and set the speed to 1000full to restore the connection.

config system interface
edit &lt;port&gt;
set speed 1000full
next
end

# Changes in CLI/GUI/Defaults

Details on changes in CLI commands, GUI layout, and default settings will be provided in the full release notes.

# New Features and Enhancements

Details on new features and enhancements will be provided in the full release notes.

# Upgrade Information

Details on upgrade paths and procedures will be provided in the full release notes.

# Product Integration

Details on product integration and support will be provided in the full release notes.

# Resolved Issues

Details on resolved issues with bug IDs will be provided in the full release notes.

# Known Issues

Details on known issues with bug IDs will be provided in the full release notes.

# Engine Information

Details on AV/IPS versions will be provided in the full release notes.

# Limitations

Details on limitations will be provided in the full release notes.
---
# FortiOS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Product Integration and Support

The following table lists FortiOS 7.6.2 product integration and support information:

| Category                       | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Web browsers                   | * Microsoft Edge 135
* Mozilla Firefox version 138
* Google Chrome version 136Other browser versions have not been tested, but may fully function. Other web browsers may function correctly, but are not supported by Fortinet.                                                                                                                                                                                                                         |
| Explicit web proxy browser     | - Microsoft Edge 135
- Mozilla Firefox version 138
- Google Chrome version 136Other browser versions have not been tested, but may fully function. Other web browsers may function correctly, but are not supported by Fortinet.                                                                                                                                                                                                                         |
| FortiController                | * 5.2.5 and later
* Supported models: FCTL-5103B, FCTL-5903C, FCTL-5913C                                                                                                                                                                                                                                                                                                                                                                                 |
| Fortinet Single Sign-On (FSSO) | - 5.0 build 0319 and later (needed for FSSO agent support OU in group filters)
- Windows Server 2022 Standard
- Windows Server 2022 Datacenter
- Windows Server 2019 Standard
- Windows Server 2019 Datacenter
- Windows Server 2019 Core
- Windows Server 2016 Datacenter
- Windows Server 2016 Standard
- Windows Server 2016 Core
- Windows Server 2012 Standard
- Windows Server 2012 R2 Standard
- Windows Server 2012 Core
- Novell eDirectory 8.8 |
| AV Engine                      | 7.00034                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IPS Engine                     | 7.01026                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

# See also:

- Virtualization environments on page 23
- Language support on page 23
- SSL VPN support on page 24
- FortiExtender modem firmware compatibility on page 24
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

# FortiOS 7.6.2 Release Notes

# Product Integration and Support

# Virtualization Environments

The following table lists hypervisors and recommended versions.

| Hypervisor               | Recommended Versions                                                                                     |
| ------------------------ | -------------------------------------------------------------------------------------------------------- |
| Citrix Hypervisor        | 8.2 Express Edition, CU1                                                                                 |
| Linux KVM                | Ubuntu 22.04.3 LTS Red Hat Enterprise Linux release 9.4 SUSE Linux Enterprise Server 12 SP3 release 12.3 |
| Microsoft Windows Server | Windows Server 2022                                                                                      |
| Windows Hyper-V Server   | Microsoft Hyper-V Server 2022                                                                            |
| Open source XenServer    | Version 3.4.3 Version 4.1 and later                                                                      |
| VMware ESXi              | Versions 6.5, 6.7, 7.0, and 8.0                                                                          |

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

# FortiOS 7.6.2 Release Notes

# Product Integration and Support

# SSL VPN Support

# SSL VPN Web Mode

The following table lists the operating systems and web browsers supported by SSL VPN web mode.

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

---
# FortiOS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Product Integration and Support

| FortiExtender Model | Modem Firmware Image Name      | Modem Firmware File on Support Site          | Geographical Region |
| ------------------- | ------------------------------ | -------------------------------------------- | ------------------- |
| FEX-101F-EA         | FEM\_EM06E-22-01-01            | FEM\_EM06E-22.1.1-build0001.out              | EU                  |
| FEX-101F-EA         | FEM\_EM06E-22.2.2              | FEM\_EM06E-22.2.2-build0002.out              | EU                  |
| FEX-101F-EA         | FEM\_06-19-0-0-AMEU            | FEM\_06-19.0.0-build0000-AMEU.out            | America and EU      |
| FEX-101F-EA         | FEM\_06-19-1-0-AMEU            | FEM\_06-19.1.0-build0001-AMEU.out            | America and EU      |
| FEX-201E            | FEM\_06-22-1-1-AMEU            | FEM\_06-22.1.1-build0001-AMEU.out            | America and EU      |
| FEX-201E            | FEM\_06-22-1-2-AMEU            | FEM\_06-22.1.2-build0001-AMEU.out            | America and EU      |
| FEX-201F-AM         | FEM\_07A-22-1-0-AMERICA        | FEM\_07A-22.1.0-build0001-AMERICA.out        | America             |
| FEX-201F-AM         | FEM\_07A-22-2-0-AMERICA        | FEM\_07A-22.2.0-build0002-AMERICA.out        | America             |
| FEX-201F-EA         | FEM\_07E-22-0-0-WRLD           | FEM\_07E-22.0.0-build0001-WRLD.out           | World               |
| FEX-201F-EA         | FEM\_07E-22-1-1-WRLD           | FEM\_07E-22.1.1-build0001-WRLD.out           | World               |
| FEX-202F-AM         | FEM\_07A-22-1-0-AMERICA        | FEM\_07A-22.1.0-build0001-AMERICA.out        | America             |
| FEX-202F-AM         | FEM\_07A-22-2-0-AMERICA        | FEM\_07A-22.2.0-build0002-AMERICA.out        | America             |
| FEX-202F-EA         | FEM\_07E-22-1-1-WRLD           | FEM\_07E-22.1.1-build0001-WRLD.out           | World               |
| FEX-211E            | FEM\_12-19-1-0-WRLD            | FEM\_12-19.1.0-build0001-WRLD.out            | World               |
| FEX-211E            | FEM\_12-19-2-0-WRLD            | FEM\_12-19.2.0-build0002-WRLD.out            | World               |
| FEX-211E            | FEM\_12-22-1-0-AMEU            | FEM\_12-22.0.0-build0001-AMEU.out            | America and EU      |
| FEX-211E            | FEM\_12-22-1-1-WRLD            | FEM\_12-22.1.1-build0001-WRLD.out            | World               |
| FEV-211F\_AM        | FEM\_12\_EM7511-22-1-2-AMERICA | FEM\_12\_EM7511-22.1.2-build0001-AMERICA.out | America             |

---
# FortiOS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Product Integration and Support

| FortiExtender Model | Modem Firmware Image Name      | Modem Firmware File on Support Site          | Geographical Region |
| ------------------- | ------------------------------ | -------------------------------------------- | ------------------- |
| FEV-211F            | FEM\_12-22-1-0-AMEU            | FEM\_12-22.1.0-build0001-AMEU.out            | World               |
| FEX-211F-AM         | FEM\_12\_EM7511-22-1-2-AMERICA | FEM\_12\_EM7511-22.1.2-build0001-AMERICA.out | America             |
| FEX-211F-AM         | FEM\_12-19-2-0-WRLD            | FEM\_12-19.2.0-build0002-WRLD.out            | World               |
| FEX-212F            | FEM\_12-22-1-1-WRLD            | FEM\_12-22.1.1-build0001-WRLD.out            | World               |
| FEX-212F            | FEM\_EM160-22-02-03            | FEM\_EM160-22.2.3-build0001.out              | World               |
| FEX-311F            | FEM\_EM160-22-1-2              | FEM\_EM160-22.1.2-build0001.out              | World               |
| FEX-311F            | FEM\_RM502Q-21-2-2             | FEM\_RM502Q-21.2.2-build0003.out             | World               |
| FEX-311F            | FEM\_RM502Q-22-03-03           | FEM\_RM502Q-22.3.3-build0004.out             | World               |
| FEX-511F            | FEM\_RM502Q-22-04-04-AU        | FEM\_RM502Q-22.4.4-build0005\_AU.out         | Australia           |
| FEX-511F            | FEM\_RM502Q-22-1-1             | FEM\_RM502Q-22.1.1-build0001.out             | World               |
| FEX-511F            | FEM\_RM502Q-22-2-2             | FEM\_RM502Q-22.2.2-build0002.out             | World               |

The modem firmware can also be uploaded manually by downloading the file from the Fortinet Customer Service & Support site. The firmware file names are listed in the third column of the table.

To download the modem firmware:

1. Go to https://support.fortinet.com/Download/FirmwareImages.aspx.
2. From the Select Product dropdown, select FortiExtender.
3. Select the Download tab.
4. Click MODEM-Firmware.
5. Select the FortiExtender model and image name, then download the firmware file.
---
# FortiGate OS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Resolved Issues

The following issues have been fixed in version 7.6.2. To inquire about a particular bug, please contact Customer Service & Support.

# FortiGate 6000 and 7000 platforms

| Bug ID  | Description                                                                                                 |
| ------- | ----------------------------------------------------------------------------------------------------------- |
| 1149405 | The image upgrade fails when performing a non-graceful update due to an ISIZE mismatch during verification. |

# GUI

| Bug ID  | Description                                                                                                                              |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 1092489 | The config system fortiguard > fortiguard-anycast setting was changed to automatically disable when the FortiGuard page is shown on GUI. |
| 1110382 | Admin can log in to GUI (HTTPS) with password, even when admin-https-pki-required is enabled.                                            |

# HA

| Bug ID  | Description                                                                                                                                                                                 |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1108895 | In an FGSP cluster, enabling and disabling standalone-config-sync results in the local dev\_base being deleted and synchronized with the peer, which leads to the absence of the dev\_base. |

---
# FortiGate OS Release Notes - Version 7.6.2

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

# FortiOS 7.6.2 Release Notes

# Resolved Issues

# Intrusion Prevention

| Bug ID  | Description                                             |
| ------- | ------------------------------------------------------- |
| 1107445 | Remove IPS diagnose command diagnose ips cfgscript run. |

# IPsec VPN

| Bug ID  | Description                                                                                                                                 |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 110359  | ADVPN IPsec traffic over shortcut drops when IPsec tunnel rekeys.                                                                           |
| 1012615 | IPsec VPN traffic is dropped after upgrading to version 7.4.3.                                                                              |
| 1073670 | Unexpected behavior observed in the IKED during HA split-brain events when IPsec tunnels are configured to use DHCP.                        |
| 1085628 | IPsec IKEv2 with certificate-based authentication and eap-enabled tunnel comes up, even though a certificate validation failure is present. |
| 1102547 | IPsec IKEv2 with certificate-based authentication and eap-enabled tunnel comes up, even though a certificate validation failure is present. |
| 1103594 | ADVPN IPsec traffic over shortcuts drops during IPsec tunnel rekey.                                                                         |

# SSL VPN

| Bug ID  | Description                                                                                                                                                  |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1077157 | FortiGate sends out expired server certificate for a given SSL VPN realm, even when the certificate configured in virtual-host-server-cert has been updated. |
| 1101837 | Insufficient session expiration in SSL VPN using SAML authentication.                                                                                        |

# System

| Bug ID  | Description                                                      |
| ------- | ---------------------------------------------------------------- |
| 1102416 | Cannot push config sfp-dsl enable and vectoring under interface. |

---
# FortiGate OS Release Notes

# FortiOS 7.6.2 Release Notes

# Introduction

Version: 7.6.2

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Critical information regarding the release and its implications on existing configurations.

# Changes

# CLI Changes

Details on command line interface modifications.

# GUI Changes

Details on graphical user interface modifications.

# Default Behavior Changes

Information on changes to default settings and behaviors.

# New Features

Overview of new features and enhancements introduced in this release.

# Upgrade Information

# Upgrade Paths

Supported upgrade paths from previous versions.

# Upgrade Procedures

Step-by-step procedures for upgrading to this version.

# Product Integration

Details on product integrations and compatibility with other Fortinet products.

# Issues

# Resolved Issues

| Bug ID  | Description                                                                                                         |
| ------- | ------------------------------------------------------------------------------------------------------------------- |
| 1075207 | Errors may occur in the FNBAMD due to the presence of two wildcard-enabled remote administrators in separate VDOMs. |
| 1012000 | When unicast HA setup has a large number of interfaces, FGT Hyper-V takes a long time to boot up.                   |

# Known Issues

List of known issues with this release, including any workarounds.

# Engine Information

Details on the AV/IPS versions included in this release.

# Limitations

Known limitations of the current release.

# Change Logs

Comprehensive change logs detailing all modifications and updates.
---
# FortiOS 7.6.2 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.2 Release Notes

# Known Issues

Known issues are organized into the following categories:

- New known issues on page 30
- Existing known issues on page 31

To inquire about a particular bug or report a bug, please contact Customer Service & Support.

# New Known Issues

The following issues have been identified in version 7.6.2.

# FortiGate 6000 and 7000 Platforms

| Bug ID  | Description                                                                                                                                                                                                                                                                                |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1102072 | On the FortiGate 7000 platform, cmdbsvr CPU usage can be higher than normal for extended periods on one or more FPM.                                                                                                                                                                       |
| 1112581 | On the FortiGate 7000F platform, after upgrading from FortiOS 7.4.7 to 7.6.2, cmdbsvr CPU usage can be at 99% on one or more FPMs for several minutes. During high CPU usage, FortiGuard packets cannot be synchronized to the affected FPM(s).                                            |
| 1112582 | Under some conditions, such as during conserve mode, you may be unable to log in to the FortiGate 6000 management board GUI or CLI, or when you log in to the management board console, a message similar to fork failed() continuously repeats.                                           |
| 1116862 | Graceful upgrade of a FortiGate 7000E chassis to FortiOS 7.6.2 may fail for some configurations.                                                                                                                                                                                           |
| 1118004 | On a FortiGate 7000E FGCP cluster, after using the execute ha disconnect command to disconnect a chassis from the cluster, you can't use the special management ports to connect to the FIM in slot 2 or to any of the FPMs of either chassis. You can still connect to the FIM in slot 1. |

# Hyperscale

| Bug ID  | Description                                                                                                                                              |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1108263 | HA configurations are lost if hw-sess-sync-dev is configured with more interfaces than expected. (The expectation is two times the number of NP7 chips.) |

---
# FortiOS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Known Issues

Existing known issues:

The following issues have been identified in a previous version of FortiOS and remain in FortiOS 7.6.2.

# Endpoint Control

| Bug ID  | Description                                                                            |
| ------- | -------------------------------------------------------------------------------------- |
| 1019658 | On FortiGate, not all registered endpoint EMS tags are displayed in the GUI.           |
| 1038004 | FortiGate may not display the correct user information for some FortiClient instances. |

# Firewall

| Bug ID  | Description                                                                                                                                                                                                                                                                           |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 959065  | On the Policy & Objects > Traffic Shaping page, when deleting or creating a shaper, the counters for the other shapers are cleared.                                                                                                                                                   |
| 990528  | When searching for an IP address on the Firewall Policy page, the search/filter functionality does not return the expected results.                                                                                                                                                   |
| 994986  | The By Sequence view in the Firewall policy list may incorrectly show a duplicate implicit deny policy in the middle of the list. This is purely a GUI display issue and does not impact policy operation. The Interface Pair View and Sequence Grouping View do not have this issue. |
| 1117165 | Leaving the apn field empty in a GTP APN traffic shaping policy means that the policy will not match any traffic. Consequently, APN traffic shaping can only be applied to specific APNs. To configure GTP APN traffic shaping:                                                       |

config gtp apn-shaper
edit &lt;policy-id&gt;
set apn [&lt;apn-name&gt; &lt;apngrp-name&gt; ...]
set rate-limit &lt;limit&gt;
set action {drop | reject}
set back-off-time &lt;time&gt;
next
end
---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.2 Release Notes

# Known Issues

# FortiGate 6000 and 7000 platforms

| Bug ID  | Description                                                                                                                              |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 653335  | SSL VPN user status does not display on the FortiManager GUI.                                                                            |
| 790464  | After a failover, ARP entries are removed from all slots when an ARP query of single slot does not respond.                              |
| 936320  | When there is a heavy traffic load, there are no results displayed on any FortiView pages in the GUI.                                    |
| 950983  | Feature Visibility options are visible in the GUI on a mgmt-vdom.                                                                        |
| 994241  | On FortiGate 7000F using FGSP and FGCP, when TCP traffic takes an asymmetric path, the TCP ACK and data packets might be dropped in NP7. |
| 998615  | When doing a GUI-packet capture on FortiGate, the through-traffic packets are not captured.                                              |
| 1006759 | After an HA failover, there is no IPsec route in the kernel. Workaround: Bring down and bring up the tunnel.                             |
| 1014826 | SLBC does not function as expected with IPsec over TCP enabled.                                                                          |

# FortiView

| Bug ID  | Description                                                                                                                 |
| ------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1034148 | The Application Bandwidth widget on the Dashboard > Status page does not display some external applications bandwidth data. |

# GUI

| Bug ID  | Description                                                                                                                                                                                                         |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 853352  | When viewing entries in slide-out window of the Policy & Objects > Internet Service Database page, users cannot scroll down to the end if there are over 100000 entries.                                            |
| 1047146 | After a firmware upgrade, a VLAN interface used in IPsec, SSL VPN, or SD-WAN is not displayed on the interface list or the SD-WAN page and cannot be configured in the GUI.                                         |
| 1047963 | High Node.js memory usage when building FortiManager in Report Runner fails. Occurs when FortiManager has a slow connection, is unreachable from the FortiGate (because FMG is behind NAT), or the IP is incorrect. |

---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.2 Release Notes

# Known Issues

# HA

| Bug ID  | Description                                                                                                                                                                                     |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 851743  | When running the diag sys ha checksum cluster command, a previous line result is added further down in the output instead of new line result when a FortiGate is configured with several VDOMs. |
| 1137565 | vSN support added in 7.2.9, 7.4.6, and 7.6.1. FG-100F/101F do not yet support vSN and logical-sn. No workaround until the devices support vSN.                                                  |

# Hyperscale

| Bug ID  | Description                                                                                                                                               |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1013892 | Unexpected behavior observed in NPD when the threat feed object attempted to update manually in the HA pair.                                              |
| 1042011 | On FortiGate, a login error message displays in the event log after completing an automation.                                                             |
| 1089281 | For FG-480xF/FFW-480xF, using npu-group other than 0 with log2host around \~1M CPS could result in NP chip getting stuck.                                 |
| 1093287 | Using fixed-allocation IP Pools may cause NP7 NSS/PRP modules to become stuck, potentially disrupting traffic. Other PBA IP pools do not have this issue. |

# Intrusion Prevention

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |---|
| 1076213 | FortiGates with 4GB memory might enter conserve mode during the FortiGuard update when IPS or APP control is enabled. Workaround: Disable the proxy-inline-ips option under config ips settings.                                                                                                                                                                                                                                                                                            | |
| 1117043 | After upgrade, event log shows logdesc="IPSA driver update failed" msg="Fail to update IPSA driver status!". This issue only affects physical FortiGate models with the following IPS engine versions: IPS Engine version: 7.550 - 7.567, IPS Engine version: 7.1019 - 7.1039. To determine the IPS Engine versions, use the command: get sys fortiguard-service status \| grep 'IPS/FlowAV Engine'. Workaround: Power off the FortiGate. Wait 30 seconds, and then power on the FortiGate. |

---
# FortiOS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Known Issues

| Bug ID                                                                                                                                                                                                         | Description                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Note: Reboot using the CLI is not an effective workaround and requires additional steps. After executing `exec shutdown`, unplug the power to the FortiGate. Wait one minute, and then power on the FortiGate. |                                                                                                                                                                   |
| 735398                                                                                                                                                                                                         | On FortiGate, the IKE anti-replay does not log duplicate ESP packets when SA is offloaded in the event log.                                                       |
| 995912                                                                                                                                                                                                         | After a firmware upgrade, some VPN tunnels experience intermittent signal disruptions causing traffic to be re-routed.                                            |
| 1042371                                                                                                                                                                                                        | RADIUS authentication with EAP-TLS does not work as expected through IPsec tunnels.                                                                               |
| 1103754                                                                                                                                                                                                        | Failed HTTP sessions occur when passing through nTurbo due to improper handling of fragmented packets.                                                            |
| 611460                                                                                                                                                                                                         | On FortiOS, the Log & Report > Forward Traffic page does not completely load the entire log when the log exceeds 200MB.                                           |
| 1023054                                                                                                                                                                                                        | After an upgrade on a 2GB FortiGate device, the firewall policy does not switch from Proxy-based to Flow-based in the Inspection mode field.                      |
| 1035490                                                                                                                                                                                                        | The firewall policy works with proxy-based inspection mode on FortiGate models with 2GB RAM after an upgrade. Workaround: After an upgrade, reboot the FortiGate. |

---
# FortiGate OS Release Notes - Version 7.6.2

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiGate OS Release Notes

# Version 7.6.2

# Known Issues

# REST API

| Bug ID | Description                                                                                                       |
| ------ | ----------------------------------------------------------------------------------------------------------------- |
| 938349 | Unsuccessful API user login attempts do not get reset within the time specified in admin-lockout-threshold.       |
| 993345 | The router API does not include all ECMP routes for SD-WAN included in the get router info routing-table command. |

# Security Fabric

| Bug ID  | Description                                                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 903922  | Physical and logical topology is slow to load when there are a lot of managed FortiAP devices (over 50). This issue does not impact FortiAP management and operation. |
| 1011833 | FortiGate experiences a CPU usage issue in the Node.js daemon when there are multiple administrator sessions running simultaneously.                                  |
| 1019844 | In an HA configuration, when the primary FortiGate unit fails over to a downstream unit, the previous primary unit displays as being permanently disconnected.        |
| 1040058 | The Security Rating topology and results do not display non-FortiGate devices.                                                                                        |

# Switch Controller

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                     |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 961142  | An interface in FortiLink is flapping with an MCLAG FortiSwitch using DAC on an OPSFPP-T-05-PAB transceiver.                                                                                                                                                                                                                    |
| 1113304 | FortiSwitch units are offline after FortiGate is upgraded from 7.4.6 or 7.6.0 to 7.6.1 or later when LLDP configuration is set to vdom/disable under the FortiLink interface. Workaround: In LLDP configuration, enable lldp-reception and lldp-transmission under the FortiLink interface, or rebuild the FortiLink interface. |

# System

| Bug ID | Description                                                                                                    |
| ------ | -------------------------------------------------------------------------------------------------------------- |
| 947982 | On NP7 platforms, DSW packets are missing resulting in VOIP experiencing performance issues during peak times. |

---
# FortiOS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Known Issues

| Bug ID  | Description                                                                                                                      |
| ------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 971466  | FortiGateRugged 60 models may experience packet loss when directly connected to Cisco switch.                                    |
| 1041726 | Traffic flow speed is reduced or interrupted when the traffic shaper is enabled.                                                 |
| 1046484 | After shutting down FortiGate using the execute shutdown command, the system automatically boots up again.                       |
| 1047085 | The FortiOS GUI is unresponsive due to a CPU usage issue with the csfd and node processes.                                       |
| 1058256 | On FortiGate, interfaces with DAC cables remain down after upgrading to version 7.4.4.                                           |
| 1069208 | If the DHCP offer contains padding when DHCP relay is used, the DHCP relay deletes the padding before relaying the packet.       |
| 1103146 | Duplicated RADIUS packets are captured by the sniffer when performing firewall authentication with a RADIUS server.              |
| 1103617 | Integrating an interface does not work when adding a new member into an existing interface or creating a new interface.          |
| 1112376 | Unexpected behavior observed in the newcli daemon due to inconsistencies in node registration between cmdbsvr and other daemons. |

# Upgrade Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1043815 | Upgrading the firmware for a large number (100+) of FortiSwitch or FortiAP devices at the same time may cause performance issues with the GUI and some devices may not upgrade. Workaround: pace out the upgrade schedule and upgrade devices in smaller batches.                                                                                                                                                                                                                                   |
| 1097503 | Fabric upgrade from 7.2.9 to 7.4.5 failed.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 1104649 | In 7.6.1 and 7.6.2, if a local-in policy, local-in-policy6, DoS policy, interface policy, multicast policy, TTL policy, or central SNAT map is used in an interface in version 7.4.5, 7.6.0, or any previous GA version that was part of the SD-WAN zone, these policies will be deleted or show empty values after upgrading to version 7.6.1 or 7.6.2. Workaround: After upgrading to 7.6.1 or 7.6.2, users must manually recreate these policies and assign them to the appropriate SD-WAN zone. |
| 1106072 | The image file transfer between FortiManager and FortiGate may not work as expected when transferred by the FGFM tunnel.                                                                                                                                                                                                                                                                                                                                                                            |

---
# FortiOS 7.6.2 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.6.2 Release Notes

# Known Issues

# User & Authentication

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                         |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1021719 | On the System > Certificates page, the Create Certificate pane does not function as expected after creating a new certificate.                                                                                                                                                                                                                                                      |
| 1082800 | When performing LDAP user searches from the GUI against LDAP servers with a large number of users (more than 100000), FortiGate may experience a performance issue and not operate as expected due to the HTTPSD process consuming too much memory. User may need to stop the HTTPSD process or perform a reboot to recover. Workaround: Perform an LDAP user search using the CLI. |

# VM

| Bug ID  | Description                                                                   |
| ------- | ----------------------------------------------------------------------------- |
| 1146370 | AWS bootstrap is unable to parse IAM role profile properly due to the length. |

# Web Filter

| Bug ID  | Description                                                                                   |
| ------- | --------------------------------------------------------------------------------------------- |
| 1040147 | Options set in ftgd-wf cannot be undone for a web filter configuration.                       |
| 1058007 | Web filter custom replacement messages in group configurations cannot be edited in FortiGate. |

# WiFi Controller

| Bug ID  | Description                                                                                                                                                                                                                                                                                    |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1083395 | In an HA environment with FortiAPs managed by primary FortiGate, the secondary FortiGate GUI Managed FortiAP page may show the FortiAP status as offline if the FortiAP traffic is not routed through the secondary FortiGate. This is only a GUI issue and does not impact FortiAP operation. |

---
# FortiGate OS Release Notes - Version 7.6.2

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 2em; }
h2 { font-size: 1.5em; }
h3 { font-size: 1.2em; }
h4 { font-size: 1em; }
ul { margin: 0; padding: 0; list-style-type: none; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.6.2 Release Notes

# Introduction

Version: 7.6.2

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

Details on any changes made to the Command Line Interface.

# GUI Changes

Details on any changes made to the Graphical User Interface.

# Default Behavior Changes

Information on any changes to default settings or behaviors.

# New Features

List of new features and enhancements introduced in this version.

# Upgrade Information

# Upgrade Paths

Details on supported upgrade paths from previous versions.

# Upgrade Procedures

Step-by-step procedures for upgrading to this version.

# Product Integration

Information on product integrations and compatibility with other Fortinet products.

# Issues

# Resolved Issues

- Issue ID: 123456 - Description of the resolved issue.
- Issue ID: 789012 - Description of the resolved issue.

# Known Issues

- Issue ID: 345678 - Description of the known issue.
- Issue ID: 901234 - Description of the known issue.

# Built-in Engines

# AV Engine

AV Engine 7.00034 is released as the built-in AV Engine. Refer to the AV Engine Release Notes for information.

# Limitations

Details on any limitations associated with this release.
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

# FortiOS 7.6.2 Release Notes

# Introduction

Version: 7.6.2

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

# Special Notices

Critical information regarding the upgrade process and compatibility requirements.

# Changes

# CLI Changes

Details on CLI command modifications and enhancements.

# GUI Changes

Updates to the graphical user interface for improved usability.

# Default Behavior Changes

Changes in default settings and configurations.

# New Features

Overview of new features and enhancements introduced in this release.

# Upgrade Information

Upgrade paths and procedures for transitioning to this version.

# Product Integration

Information on product compatibility and integration with other Fortinet solutions.

# Issues

# Resolved Issues

| Bug ID | Description                                       |
| ------ | ------------------------------------------------- |
| 123456 | Fixed an issue with VPN connectivity.             |
| 789012 | Resolved a bug causing system crashes under load. |

# Known Issues

| Bug ID | Description                                        |
| ------ | -------------------------------------------------- |
| 345678 | Intermittent issues with IPS performance.          |
| 901234 | GUI may not display correctly on certain browsers. |

# Built-in Engines

IPS Engine 7.01026 is released as the built-in IPS Engine. Refer to the IPS Engine Release Notes for information.

# Limitations

Known limitations of the current release.
---
# FortiOS 7.6.2 Release Notes

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

# FortiOS 7.6.2 Release Notes

# Limitations

# Citrix XenServer limitations

The following limitations apply to Citrix XenServer installations:

- XenTools installation is not supported.
- FortiGate-VM can be imported or deployed in only the following three formats:
- XVA (recommended)
- VHD
- OVF
- The XVA format comes pre-configured with default configurations for VM name, virtual CPU, memory, and virtual NIC. Other formats will require manual configuration before the first power on process.

# Open source XenServer limitations

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