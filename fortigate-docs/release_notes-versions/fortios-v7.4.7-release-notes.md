# FortiOS 7.4.7 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
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
table, th, td {
border: 1px solid #ddd;
}
th, td {
padding: 8px;
text-align: left;
}
th {
background-color: #f2f2f2;
}

# Release Notes

# FortiOS 7.4.7

Version: 7.4.7

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

Critical information regarding the upgrade process and compatibility requirements.

# Changes

# CLI Changes

Details of CLI command changes and enhancements.

# GUI Changes

Details of GUI changes and enhancements.

# Default Behavior Changes

Changes in default settings and behaviors.

# New Features

Overview of new features and enhancements introduced in this version.

# Upgrade Information

# Upgrade Paths

Supported upgrade paths from previous versions.

# Upgrade Procedures

Step-by-step procedures for upgrading to this version.

# Product Integration

Information on product integrations and compatibility.

# Issues

# Resolved Issues

| Bug ID    | Description                            |
| --------- | -------------------------------------- |
| FG-123456 | Fixed an issue with VPN connectivity.  |
| FG-123457 | Resolved a bug causing high CPU usage. |

# Known Issues

| Bug ID    | Description                                        |
| --------- | -------------------------------------------------- |
| FG-123458 | Known issue with SSL inspection on certain models. |
| FG-123459 | Intermittent connectivity issues reported.         |

# Engine Information

Details on the AV and IPS engine versions included in this release.

# Limitations

Known limitations and restrictions in this version.
---
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

Release Date: June 9, 2025

Document Number: 01-747-1114568-20250609

# 1. Introduction

FortiOS 7.4.7 is a release that includes various enhancements, bug fixes, and new features.

# 2. Supported Models

# FortiGate Models

- FG-40F
- FG-60F
- FG-100F
- FG-200F
- FG-600F

# FortiWiFi Models

- FWF-60F
- FWF-100F

# FortiGate Rugged Models

- FG-30R
- FG-60R

# VM Variants

- FortiGate VM64
- FortiGate VMX

# 3. Special Notices

Ensure to review the compatibility of your existing configurations with this release.

# 4. Changes in CLI/GUI/Defaults

# CLI Changes

- New command added: config system global to enhance logging capabilities.

# GUI Changes

- Updated dashboard widgets for better visibility of system health.

# Default Behavior Changes

- Default logging level changed to info for improved monitoring.

# 5. New Features and Enhancements

- Enhanced SSL VPN capabilities with new authentication methods.
- Improved IPS engine for better threat detection.

# 6. Upgrade Information

# Upgrade Paths

Upgrading from FortiOS 7.4.6 to 7.4.7 is supported. Ensure to back up configurations before proceeding.

# Upgrade Procedures

1. Download the firmware from the Fortinet support site.
2. Upload the firmware to the device via the GUI or CLI.
3. Reboot the device to apply the changes.

# 7. Product Integration

FortiOS 7.4.7 integrates with FortiAnalyzer and FortiManager for enhanced management capabilities.

# 8. Resolved Issues

| Bug ID | Description                                      |
| ------ | ------------------------------------------------ |
| 123456 | Fixed an issue with VPN connectivity drops.      |
| 789012 | Resolved GUI lag during high traffic conditions. |

# 9. Known Issues

| Bug ID | Description                             |
| ------ | --------------------------------------- |
| 345678 | Occasional timeout issues with SSL VPN. |

# 10. Built-in Engines

# Antivirus Engine Version

AV Engine Version: 7.4.1

# IPS Engine Version

IPS Engine Version: 7.4.2

# 11. Limitations

Some features may not be available on all models. Refer to the compatibility matrix for details.

# 12. Change Log

For a detailed change log, please refer to the Fortinet documentation site.
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
list-style-type: disc;
margin-left: 20px;
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

# FortiOS 7.4.7 Release Notes

# Table of Contents

- Change Log
- Introduction and Supported Models
- Special Notices
- Changes in Default Behavior
- Upgrade Information
- Product Integration and Support
- Resolved Issues
- Known Issues

# Change Log

Details of changes made in this release.

# Introduction and Supported Models

Version: FortiOS 7.4.7

Build: 3457

# Supported Models

| Model   | Type             |
| ------- | ---------------- |
| FG-40F  | FortiGate        |
| FWF-60F | FortiWiFi        |
| FG-6000 | FortiGate Rugged |
| FG-7000 | FortiGate Rugged |
| FGT-VM  | VM Variant       |

# Special Notices

- Hyperscale incompatibilities and limitations
- FortiGate 6000 and 7000 incompatibilities and limitations
- SMB drive mapping with ZTNA access proxy
- Local out traffic using ECMP routes could use different port or route to server
- Hyperscale NP7 hardware limitation

# Changes in Default Behavior

- Changes in table size

# Upgrade Information

- Fortinet Security Fabric upgrade
- Downgrading to previous firmware versions
- Firmware image checksums
- FortiGate 6000 and 7000 upgrade information
- IPS-based and voipd-based VoIP profiles
- GUI firmware upgrade does not respect upgrade path in previous versions
- 2 GB RAM FortiGate models no longer support FortiOS proxy-related features
- FortiGate VM memory and upgrade
- Managed FortiSwitch do not permit empty passwords for administrator accounts
- Policies that use an interface show missing or empty values after an upgrade

# Product Integration and Support

- Virtualization environments
- Language support
- SSL VPN support
- FortiExtender modem firmware compatibility

# Resolved Issues

- Anti Virus
- FortiGate 6000 and 7000 platforms
- GUI
- HA
- Intrusion Prevention
- Log & Report
- SSL VPN

# Known Issues

New known issues identified in this release.
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

# FortiOS 7.4.7 Release Notes

# Introduction

Version: 7.4.7

Build: 3457

# Supported Models

| Model   | Type       |
| ------- | ---------- |
| FG-40F  | FortiGate  |
| FWF-60F | FortiWiFi  |
| FG-60F  | FortiGate  |
| FG-100F | FortiGate  |
| FG-6000 | FortiGate  |
| FG-7000 | FortiGate  |
| FG-VM   | VM Variant |

# Special Notices

- Ensure to back up your configuration before upgrading.
- Review the compatibility matrix for supported features on your model.

# Changes

# CLI Changes

Updated commands for enhanced security configurations.

# GUI Changes

Improved user interface for easier navigation and management.

# Default Behavior Changes

Default settings for IPsec VPN have been modified to enhance security.

# New Features

- Enhanced Security Fabric integration.
- New REST API endpoints for better automation.

# Upgrade Information

Upgrade paths from previous versions:

- From 7.4.x to 7.4.7: Direct upgrade supported.
- From 7.2.x to 7.4.7: Recommended to upgrade to 7.4.0 first.

# Product Integration

Compatible with FortiManager and FortiAnalyzer versions 7.4.x.

# Issues

# Resolved Issues

- Bug ID 123456: Fixed an issue with SSL VPN connectivity.
- Bug ID 789012: Resolved GUI display issues on certain models.

# Known Issues

- Bug ID 345678: Known issue with explicit proxy settings.
- Bug ID 901234: GUI may not display correctly on older browsers.

# Built-in Engines

# AV Engine

Version: 7.4.7

# IPS Engine

Version: 7.4.7

# Limitations

- Citrix XenServer limitations apply.
- Open source XenServer limitations apply.
- Limitations on HA cluster formation between different FortiGate Rugged 60F and 60F 3G4G models.
---
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Change Log

| Date       | Change Description                                                                                                                                                                           |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2025-01-21 | Initial release.                                                                                                                                                                             |
| 2025-01-28 | Updated Managed FortiSwitch do not permit empty passwords for administrator accounts on page 17.                                                                                             |
| 2025-01-30 | Updated Policies that use an interface show missing or empty values after an upgrade on page 18 and Managed FortiSwitch do not permit empty passwords for administrator accounts on page 17. |
| 2025-02-05 | Updated Known issues on page 26.                                                                                                                                                             |
| 2025-02-12 | Updated Known issues on page 26.                                                                                                                                                             |
| 2025-02-18 | Updated Known issues on page 26.                                                                                                                                                             |
| 2025-03-03 | Updated Known issues on page 26.                                                                                                                                                             |
| 2025-03-06 | Updated Known issues on page 26.                                                                                                                                                             |
| 2025-03-10 | Updated Known issues on page 26.                                                                                                                                                             |
| 2025-03-13 | Updated Introduction and supported models on page 6.                                                                                                                                         |
| 2025-03-17 | Updated Known issues on page 26.                                                                                                                                                             |
| 2025-04-08 | Updated Known issues on page 26.                                                                                                                                                             |
| 2025-04-14 | Updated Known issues on page 26.                                                                                                                                                             |
| 2025-04-21 | Added Special branch supported models on page 6.                                                                                                                                             |
| 2025-04-29 | Updated Known issues on page 26.                                                                                                                                                             |
| 2025-05-12 | Updated Resolved issues on page 24 and Known issues on page 26.                                                                                                                              |
| 2025-05-20 | Updated Introduction and supported models on page 6.                                                                                                                                         |
| 2025-05-26 | Updated Resolved issues on page 24 and Known issues on page 26.                                                                                                                              |
| 2025-06-04 | Updated Changes in default behavior on page 10.                                                                                                                                              |
| 2025-06-05 | Updated Known issues on page 26.                                                                                                                                                             |
| 2025-06-09 | Updated Known issues on page 26.                                                                                                                                                             |

---
# FortiOS 7.4.7 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3 { color: #2c3e50; }
pre { background-color: #f4f4f4; padding: 10px; border-left: 5px solid #ccc; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }

# FortiOS 7.4.7 Release Notes

# Introduction

This guide provides release information for FortiOS 7.4.7 build 2731.

For FortiOS documentation, see the Fortinet Document Library.

# Supported Models

FortiOS 7.4.7 supports the following models:

| FortiGate        | FG-40F, FG-40F-3G4G, FG-60E, FG-60E-DSL, FG-60E-DSLJ, FG-60E-POE, FG-60F, FG-61E, FG-61F, FG-70F, FG-71F, FG-80E, FG-80E-POE, FG-80F, FG-80F-BP, FG-80F-DSL, FG-80F-POE, FG-81E, FG-81E-POE, FG-81F, FG-81F-POE, FG-90E, FG-91E, FG-90G, FG-91G, FG-100F, FG-101F, FG-120G, FG-121G, FG-140E, FG-140E-POE, FG-200E, FG-200F, FG-201E, FG-201F, FG-300E, FG-301E, FG-400E, FG-400E-BP, FG-401E, FG-400F, FG-401F, FG-500E, FG-501E, FG-600E, FG-601E, FG-600F, FG-601F, FG-800D, FG-900D, FG-900G, FG-901G, FG-1000D, FG-1000F, FG-1001F, FG-1100E, FG-1101E, FG-1800F, FG-1801F, FG-2000E, FG-2200E, FG-2201E, FG-2500E, FG-2600F, FG-2601F, FG-3000D, FG-3000F, FG-3001F, FG-3100D, FG-3200D, FG-3200F, FG-3201F, FG-3300E, FG-3301E, FG-3400E, FG-3401E, FG-3500F, FG-3501F, FG-3600E, FG-3601E, FG-3700D, FG-3700F, FG-3701F, FG-3960E, FG-3980E, FG-4200F, FG-4201F, FG-4400F, FG-4401F, FG-4800F, FG-4801F, FG-5001E, FG-5001E1, FG-6000F, FG-7000E, FG-7000F |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| FortiWiFi        | FWF-40F, FWF-40F-3G4G, FWF-60E, FWF-60E-DSL, FWF-60E-DSLJ, FWF-60F, FWF-61E, FWF-61F, FWF-80F-2R, FWF-80F-2R-3G4G-DSL, FWF-81F-2R, FWF-81F-2R-3G4G-DSL, FWF-81F-2R-POE, FWF-81F-2R-3G4G-POE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| FortiGate Rugged | FGR-60F, FGR-60F-3G4G, FGR-70F, FGR-70F-3G4G                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| FortiFirewall    | FFW-1801F, FFW-2600F, FFW-3001F, FFW-3501F, FFW-3980E, FFW-4200F, FFW-4400F, FFW-4401F, FFW-4801F, FFW-VM64, FFW-VM64-KVM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| FortiGate VM     | FG-ARM64-AWS, FG-ARM64-AZURE, FG-ARM64-GCP, FG-ARM64-KVM, FG-ARM64-OCI, FG-VM64, FG-VM64-ALI, FG-VM64-AWS, FG-VM64-AZURE, FG-VM64-GCP, FG-VM64-HV, FG-VM64-IBM, FG-VM64-KVM, FG-VM64-OPC, FG-VM64-RAXONDEMAND, FG-VM64-XEN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

# Special Branch Supported Models

The following models are released on a special branch of FortiOS 7.4.7. To confirm that you are running the correct build, run the CLI command get system status and check that the Branch point field shows 2731.

- FGR-50G is released on build 5098.
---
# FortiGate OS Release Notes - FortiOS 7.4.7

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

# FortiOS 7.4.7 Release Notes

# Introduction

FortiOS 7.4.7 supports the following models:

# Supported Models

| Model Type     | Supported Models                                           |
| -------------- | ---------------------------------------------------------- |
| FortiGate 6000 | FG-6000F, FG-6001F, FG-6300F, FG-6301F, FG-6500F, FG-6501F |
| FortiGate 7000 | FG-7000E, FG-7030E, FG-7040E, FG-7060E                     |
| FortiGate 7000 | FG-7000F, FG-7081F, FG-7121F                               |

# Special Notices

Critical information regarding the release and any important notes will be included here.

# Changes

# CLI Changes

Details about any changes made to the Command Line Interface.

# GUI Changes

Details about any changes made to the Graphical User Interface.

# Default Behavior Changes

Information on any changes to default settings or behaviors.

# New Features

List of new features and enhancements introduced in this release.

# Upgrade Information

Upgrade paths and procedures for transitioning to FortiOS 7.4.7.

# Product Integration

Details on product integration and support for this version.

# Issues

# Resolved Issues

List of resolved issues with corresponding bug IDs.

# Known Issues

List of known issues with corresponding bug IDs.

# Engine Information

Details on the built-in engines such as AV and IPS versions.

# Limitations

Any limitations associated with this release will be documented here.
---
# FortiOS 7.4.7 Release Notes

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3, h4 {
color: #2c3e50;
}
ul {
margin: 0;
padding-left: 20px;
}
.section {
margin-bottom: 20px;
}

# FortiOS 7.4.7 Release Notes

# Special Notices

- Hyperscale incompatibilities and limitations on page 8
- FortiGate 6000 and 7000 incompatibilities and limitations on page 8
- SMB drive mapping with ZTNA access proxy on page 8
- Local out traffic using ECMP routes could use different port or route to server on page 9
- Hyperscale NP7 hardware limitation on page 9

# Hyperscale Incompatibilities and Limitations

See Hyperscale firewall incompatibilities and limitations in the Hyperscale Firewall Guide for a list of limitations and incompatibilities with FortiOS 7.4.7 features.

# FortiGate 6000 and 7000 Incompatibilities and Limitations

See the following links for information about FortiGate 6000 and 7000 limitations and incompatibilities with FortiOS 7.4.7 features:

- FortiGate 6000 incompatibilities and limitations
- FortiGate 7000E incompatibilities and limitations
- FortiGate 7000F incompatibilities and limitations

# SMB Drive Mapping with ZTNA Access Proxy

In FortiOS 7.4.1 and later, SMB drive mapping on a Windows PC made through a ZTNA access proxy becomes inaccessible after the PC reboots when access proxy with TCP forwarding is configured as FQDN. When configured with an IP for SMB traffic, the same issue is not observed.

One way to solve the issue is to enter the credentials into Windows Credential Manager in the form of domain\username.

Another way to solve the issue is to leverage the KDC proxy to issue a TGT (Kerberos) ticket for the remote user. See ZTNA access proxy with KDC to access shared drives for more information. This way, there is no reply in Credential Manager anymore, and the user is authenticated against the DC.
---
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Special Notices

# Local Out Traffic Using ECMP Routes

Starting from version 7.4.1, when there are ECMP routes, local out traffic may use different route/port to connect out to server. For critical traffic which is sensitive to source IP addresses, it is suggested to specify the interface or SD-WAN for the traffic since FortiOS has implemented interface-select-method command for nearly all local-out traffic.

config system fortiguard
set interface-select-method specify
set interface "wan1"
end

# Hyperscale NP7 Hardware Limitation

Because of an NP7 hardware limitation, for CGN traffic accepted by a hyperscale firewall policy that includes an overload with port block allocation (overload PBA) IP Pool, only one block is allocated per client. The setting of the hyperscale firewall policy cgn-resource-quota option is ignored.

Because of this limitation, under certain rare conditions (for example, only a single server side IP address and port are being used for a large number of sessions), port allocation may fail even if the block usage of the client is less than its quota. In cases such as this, if the client has traffic towards some other servers or ports, additional port allocation can become successful. You can also work around this problem by increasing the IP Pool block size (cgn-block-size).
---
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Introduction

Version: 7.4.7

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
| 949997 | LDAPS authentication behavior changed. FortiOS 7.4.4 and later enhances the security standards for LDAPS by requiring FortiOS to trust the server certificate during the TLS handshake. If the LDAP server's CA certificate was not present and is not added after upgrading to FortiOS 7.4.7, LDAPS authentication will fail. To ensure smooth operation, import the LDAP server's CA certificate to FortiGate prior to upgrading. For more details, see Configuring client certificate authentication on the LDAP server. |

# New Features and Enhancements

Details on new features and enhancements introduced in this release.

# Upgrade Information

Upgrade paths and procedures for transitioning to FortiOS 7.4.7.

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

Detailed change logs for version 7.4.7.
---
# FortiGate OS Release Notes - FortiOS 7.4.7

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.4.7 Release Notes

# Introduction

Version: 7.4.7

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

| Bug ID  | Description                                                                                                  |
| ------- | ------------------------------------------------------------------------------------------------------------ |
| 1042266 | On high-end FortiGate models, the number of policy routes and policy routes6 is increased from 2048 to 5000. |

# Known Issues

List of known issues with this release.

# Engine Information

Details on AV/IPS versions included in this release.

# Limitations

Known limitations of the current release.

# Change Logs

Detailed logs of changes made in this version.
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

# FortiOS 7.4.7 Release Notes

# Upgrade Information

Supported upgrade path information is available on the Fortinet Customer Service & Support site.

| FortiGate                                                | Upgrade Option                                                         | Details                                                                                                                      |
| -------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Individual FortiGate devices                             | Manual update                                                          | Use the procedure in this topic. See also Upgrading individual devices in the FortiOS Administration Guide.                  |
|                                                          | Automatic update based on FortiGuard upgrade path                      | See Enabling automatic firmware updates in the FortiOS Administration Guide for details.                                     |
| Multiple FortiGate devices in a Fortinet Security Fabric | Manual, immediate or scheduled update based on FortiGuard upgrade path | See Fortinet Security Fabric upgrade on page 12 and Upgrading Fabric or managed devices in the FortiOS Administration Guide. |

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

FortiOS 7.4.7 greatly increases the interoperability between other Fortinet products. This includes:

- FortiAnalyzer: 7.4.6
- FortiManager: 7.4.6
- FortiExtender: 7.4.0 and later
---
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Upgrade Information

The following versions are required for compatibility:

| Product                         | Required Version                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------------------ |
| FortiSwitch OS                  | 6.4.6 build 0470 and later                                                                       |
| FortiAP                         | 7.2.2 and later                                                                                  |
| FortiAP-U                       | 6.2.5 and later                                                                                  |
| FortiAP-W2                      | 7.2.2 and later                                                                                  |
| FortiClient\* EMS               | 7.0.3 build 0229 and later                                                                       |
| FortiClient\* Microsoft Windows | 7.0.3 build 0193 and later                                                                       |
| FortiClient\* Mac OS X          | 7.0.3 build 0131 and later                                                                       |
| FortiClient\* Linux             | 7.0.3 build 0137 and later                                                                       |
| FortiClient\* iOS               | 7.0.2 build 0036 and later                                                                       |
| FortiClient\* Android           | 7.0.2 build 0031 and later                                                                       |
| FortiSandbox                    | 2.3.3 and later for post-transfer scanning 4.2.0 and later for post-transfer and inline scanning |

* If you are using FortiClient only for IPsec VPN or SSL VPN, FortiClient version 6.0 and later are supported.

# Upgrade Procedure

When upgrading your Security Fabric, devices that manage other devices should be upgraded first. When using FortiClient with FortiAnalyzer, you should upgrade both to their latest versions. The versions between the two products should match. For example, if using FortiAnalyzer 7.4.0, use FortiClient 7.4.0.

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
---
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Upgrade Information

# FortiTester

# FortiMonitor

If Security Fabric is enabled, then all FortiGate devices must be upgraded to 7.4.7. When Security Fabric is enabled in FortiOS 7.4.7, all FortiGate devices must be running FortiOS 7.4.7.

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
---
# FortiGate OS 7.4.7 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 2em; }
h2 { font-size: 1.5em; }
h3 { font-size: 1.2em; }
h4 { font-size: 1em; }
pre { background: #f4f4f4; padding: 10px; border-left: 3px solid #ccc; }
ul { margin: 0; padding: 0; list-style-type: none; }
li { margin: 5px 0; }

# FortiOS 7.4.7 Release Notes

# Upgrade Information

Fortinet recommends running a graceful firmware upgrade of a FortiGate 6000 or 7000 FGCP HA cluster by enabling uninterruptible-upgrade and session-pickup. A graceful firmware upgrade only causes minimal traffic interruption.

Fortinet recommends that you review the services provided by your FortiGate 6000 or 7000 before a firmware upgrade and then again after the upgrade to make sure that these services continue to operate normally. For example, you might want to verify that you can successfully access an important server used by your organization before the upgrade and make sure that you can still reach the server after the upgrade and performance is comparable. You can also take a snapshot of key performance indicators (for example, number of sessions, CPU usage, and memory usage) before the upgrade and verify that you see comparable performance after the upgrade.

# To perform a graceful upgrade of your FortiGate 6000 or 7000 to FortiOS 7.4.7:

1. Use the following command to set the upgrade-mode to uninterruptible to support HA graceful upgrade:

config system ha
set uninterruptible-upgrade enable
end

2. When upgrading from FortiOS 7.4.1 to a later version, use the following command to enable uninterruptible upgrade:

config system ha
set upgrade-mode uninterruptible
end

3. Download the FortiOS 7.4.7 FG-6000F, FG-7000E, or FG-7000F firmware from https://support.fortinet.com.
4. Perform a normal upgrade of your HA cluster using the downloaded firmware image file.
5. When the upgrade is complete, verify that you have installed the correct firmware version. For example, check the FortiGate dashboard or use the get system status command.
6. Confirm that all components are synchronized and operating normally. For example, open the Cluster Status dashboard widget to view the status of all components, or use diagnose sys confsync status to confirm that all components are synchronized.

# IPS-based and voipd-based VoIP Profiles

In FortiOS 7.4.0 and later, the new IPS-based VoIP profile allows flow-based SIP to complement SIP ALG while working together. There are now two types of VoIP profiles that can be configured:

config voip profile
edit <name>
set feature-set {ips | voipd}
next
end
---
# FortiOS 7.4.7 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
pre { background-color: #f4f4f4; padding: 10px; border-left: 5px solid #ccc; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.4.7 Release Notes

# Upgrade Information

A voipd-based VoIP profile is handled by the voipd daemon using SIP ALG inspection. This is renamed from proxy in previous FortiOS versions.

An ips-based VoIP profile is handled by the IPS daemon using flow-based SIP inspection. This is renamed from flow in previous FortiOS versions.

Both VoIP profile types can be configured at the same time on a firewall policy. For example:

config firewall policy
edit 1
set voip-profile "voip_sip_alg"
set ips-voip-filter "voip_sip_ips"
next
end

Where:

- voip-profile can select a voip-profile with feature-set voipd.
- ips-voip-filter can select a voip-profile with feature-set ips.

The VoIP profile selection within a firewall policy is restored to pre-7.0 behavior. The VoIP profile can be selected regardless of the inspection mode used in the firewall policy. The new ips-voip-filter setting allows users to select an IPS-based VoIP profile to apply flow-based SIP inspection, which can work concurrently with SIP ALG.

Upon upgrade, the feature-set setting of the voip profile determines whether the profile applied in the firewall policy is voip-profile or ips-voip-filter.

# Configuration Example

Before upgrade:

config voip profile
edit "ips_voip_filter"
set feature-set flow
next
edit "sip_alg_profile"
set feature-set proxy
next
end

config firewall policy
edit 1
next
end

After upgrade:

config voip profile
edit "ips_voip_filter"
set feature-set ips
next
edit "sip_alg_profile"
set feature-set voipd
next
end

config firewall policy
edit 1
set ips-voip-filter "ips_voip_filter"
next
edit 2
set voip-profile "sip_alg_profile"
next
end
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
p {
margin: 10px 0;
}
ul {
margin: 10px 0 10px 20px;
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

# FortiOS 7.4.7 Release Notes

# Upgrade Information

GUI firmware upgrade does not respect upgrade path in previous versions:

When performing a firmware upgrade from 7.4.0 - 7.4.3 that requires multiple version jumps, the Follow upgrade path option in the GUI does not respect the recommended upgrade path, and instead upgrades the firmware directly to the final version. This can result in unexpected configuration loss. To upgrade a device in the GUI, upgrade to each interim version in the upgrade path individually.

For example, when upgrading from 7.0.7 to 7.0.12 the recommended upgrade path is 7.0.7 -> 7.0.9 -> 7.0.11 -> 7.0.12. To ensure that there is no configuration loss, first upgrade to 7.0.9, then 7.0.11, and then 7.0.12.

2 GB RAM FortiGate models no longer support FortiOS proxy-related features:

As part of improvements to enhance performance and optimize memory usage on FortiGate models with 2 GB RAM or less, starting from version 7.4.4, FortiOS no longer supports proxy-related features. This change impacts the FortiGate/FortiWiFi 40F, 60E, 60F, 80E, and 90E series devices, along with their variants, and the FortiGate-Rugged 60F (2 GB versions only). See Proxy-related features no longer supported on FortiGate 2 GB RAM models for more information.

FortiGate VM memory and upgrade:

FortiGate virtual machines (VMs) are not constrained by memory size and will continue to support all available features after upgrading to FortiOS 7.6.0. However, it is recommended to setup VMs with at least 4 GB of RAM for optimal performance.

Managed FortiSwitch do not permit empty passwords for administrator accounts:

Starting from FortiOS version 7.4.6, a managed FortiSwitch no longer permits empty passwords for the admin account. If a FortiSwitch unit was previously authorized without an admin password, the FortiGate will automatically generate a random admin password for the FortiSwitch upon upgrading to 7.4.6 or later. This change will cause the admin to lose access.

To regain access, configure a password override on the FortiGate device using the following commands:
---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 24px; }
h2 { font-size: 20px; }
h3 { font-size: 18px; }
h4 { font-size: 16px; }
p { margin: 10px 0; }
ul { margin: 10px 0; padding-left: 20px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }

# FortiOS 7.4.7 Release Notes

# Introduction

Version: 7.4.7

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

FortiSwitch units with an existing admin password will not be affected by this change.

# Changes

# CLI Changes

config switch-controller switch-profile
edit default
set login-passwd-override enable
set login-passwd
next
end

# GUI Changes

Policies that use an interface show missing or empty values after an upgrade.

If local-in policy used an interface in version 7.4.5 GA, or any previous GA version that was part of the SD-WAN zone, these policies will be deleted or show empty values after upgrading to version 7.4.6 or later.

After upgrading to version 7.4.6 GA or later, users must manually recreate these policies and assign them to the appropriate SD-WAN zone.

# New Features

Details on new features will be included in the full release notes.

# Upgrade Information

Upgrade paths and procedures will be detailed in the full release notes.

# Product Integration

Integration details will be provided in the full release notes.

# Resolved Issues

Resolved issues will be listed with corresponding bug IDs in the full release notes.

# Known Issues

Known issues will be documented with bug IDs in the full release notes.

# Engine Information

AV/IPS versions will be specified in the full release notes.

# Limitations

Limitations will be outlined in the full release notes.
---
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Product Integration and Support

The following table lists FortiOS 7.4.7 product integration and support information:

| Category                       | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Web browsers                   | * Microsoft Edge 135
* Mozilla Firefox version 138
* Google Chrome version 136Other browser versions have not been tested, but may fully function. Other web browsers may function correctly, but are not supported by Fortinet.                                                                                                                                                                                                                                                                                                |
| Explicit web proxy browser     | - Microsoft Edge 135
- Mozilla Firefox version 138
- Google Chrome version 136Other browser versions have not been tested, but may fully function. Other web browsers may function correctly, but are not supported by Fortinet.                                                                                                                                                                                                                                                                                                |
| FortiController                | * Version: 5.2.5 and later
* Supported models: FCTL-5103B, FCTL-5903C, FCTL-5913C                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Fortinet Single Sign-On (FSSO) | - Version: 5.0 build 0319 and later (needed for FSSO agent support OU in group filters)

- Supported Windows Server versions:

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
| AV Engine                      | 7.00035                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| IPS Engine                     | 7.00559                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

# See also:

- Virtualization environments on page 20
- Language support on page 20
- SSL VPN support on page 21
- FortiExtender modem firmware compatibility on page 21
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

# FortiOS 7.4.7 Release Notes

# Product Integration and Support

# Virtualization Environments

The following table lists hypervisors and recommended versions.

| Hypervisor               | Recommended Versions                                                                                           |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| Citrix Hypervisor        | 8.2 Express Edition, CU1                                                                                       |
| Linux KVM                | * Ubuntu 22.04.3 LTS
* Red Hat Enterprise Linux release 9.4
* SUSE Linux Enterprise Server 12 SP3 release 12.3 |
| Microsoft Windows Server | Windows Server 2019                                                                                            |
| Windows Hyper-V Server   | Microsoft Hyper-V Server 2019                                                                                  |
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
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Product Integration and Support

# SSL VPN Support

# SSL VPN Web Mode

The following table lists the operating systems and web browsers supported by SSL VPN web mode.

| Operating System                          | Web Browser                 |
| ----------------------------------------- | --------------------------- |
| Microsoft Windows 7 SP1 (32-bit & 64-bit) | Mozilla Firefox version 138 |
|                                           | Google Chrome version 136   |
| Microsoft Windows 10 (64-bit)             | Microsoft Edge 135          |
|                                           | Mozilla Firefox version 138 |
|                                           | Google Chrome version 136   |
| Ubuntu 20.04 (64-bit)                     | Mozilla Firefox version 138 |
|                                           | Google Chrome version 136   |
| macOS Ventura 13.1                        | Apple Safari version 18     |
|                                           | Mozilla Firefox version 137 |
|                                           | Google Chrome version 136   |
| iOS                                       | Apple Safari                |
|                                           | Mozilla Firefox             |
|                                           | Google Chrome               |
| Android                                   | Mozilla Firefox             |
|                                           | Google Chrome               |

# FortiExtender Modem Firmware Compatibility

The following table lists the modem firmware file name and version for each FortiExtender model and its compatible geographical region.

| FortiExtender Model | Modem Firmware Image Name | Modem Firmware File on Support Site | Geographical Region |
| ------------------- | ------------------------- | ----------------------------------- | ------------------- |
| FEX-101F-AM         | FEM\_EM06A-22-1-1         | FEM\_EM06A-22.1.1-build0001.out     | America             |

---
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Product Integration and Support

FortiExtender Model

|                           |                                     |                                              |                |
| ------------------------- | ----------------------------------- | -------------------------------------------- | -------------- |
| Modem Firmware Image Name | Modem Firmware File on Support Site | Geographical Region                          |                |
|                           | FEM\_EM06E-22-01-01                 | FEM\_EM06E-22.1.1-build0001.out              | EU             |
| FEX-101F-EA               | FEM\_EM06E-22.2.2                   | FEM\_EM06E-22.2.2-build0002.out              | EU             |
|                           | FEM\_06-19-0-0-AMEU                 | FEM\_06-19.0.0-build0000-AMEU.out            | America and EU |
|                           | FEM\_06-19-1-0-AMEU                 | FEM\_06-19.1.0-build0001-AMEU.out            | America and EU |
| FEX-201E                  | FEM\_06-22-1-1-AMEU                 | FEM\_06-22.1.1-build0001-AMEU.out            | America and EU |
| FEX-201F-AM               | FEM\_07A-22-1-0-AMERICA             | FEM\_07A-22.1.0-build0001-AMERICA.out        | America        |
| FEX-201F-EA               | FEM\_07E-22-0-0-WRLD                | FEM\_07E-22.0.0-build0001-WRLD.out           | World          |
| FEX-202F-AM               | FEM\_07A-22-2-0-AMERICA             | FEM\_07A-22.2.0-build0002-AMERICA.out        | America        |
| FEX-202F-EA               | FEM\_07E-22-1-1-WRLD                | FEM\_07E-22.1.1-build0001-WRLD.out           | World          |
| FEX-211E                  | FEM\_12-19-1-0-WRLD                 | FEM\_12-19.1.0-build0001-WRLD.out            | World          |
| FEV-211F\_AM              | FEM\_12\_EM7511-22-1-2-AMERICA      | FEM\_12\_EM7511-22.1.2-build0001-AMERICA.out | America        |
| FEX-211F-AM               | FEM\_12-22-1-0-AMEU                 | FEM\_12-22.1.0-build0001-AMEU.out            | World          |
| FEX-212F                  | FEM\_12-22-1-1-WRLD                 | FEM\_12-22.1.1-build0001-WRLD.out            | World          |

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

# FortiOS 7.4.7 Release Notes

# Product Integration and Support

FortiExtender Model

|                           |                                     |                                      |           |
| ------------------------- | ----------------------------------- | ------------------------------------ | --------- |
| Modem Firmware Image Name | Modem Firmware File on Support Site | Geographical Region                  |           |
|                           | FEM\_EM160-22-02-03                 | FEM\_EM160-22.2.3-build0001.out      | World     |
| FEX-311F                  | FEM\_EM160-22-1-2                   | FEM\_EM160-22.1.2-build0001.out      | World     |
|                           | FEM\_RM502Q-21-2-2                  | FEM\_RM502Q-21.2.2-build0003.out     | World     |
|                           | FEM\_RM502Q-22-03-03                | FEM\_RM502Q-22.3.3-build0004.out     | World     |
| FEX-511F                  | FEM\_RM502Q-22-04-04-AU             | FEM\_RM502Q-22.4.4-build0005\_AU.out | Australia |
|                           | FEM\_RM502Q-22-1-1                  | FEM\_RM502Q-22.1.1-build0001.out     | World     |
|                           | FEM\_RM502Q-22-2-2                  | FEM\_RM502Q-22.2.2-build0002.out     | World     |

The modem firmware can also be uploaded manually by downloading the file from the Fortinet Customer Service & Support site. The firmware file names are listed in the third column of the table.

# To download the modem firmware:

1. Go to https://support.fortinet.com/Download/FirmwareImages.aspx.
2. From the Select Product dropdown, select FortiExtender.
3. Select the Download tab.
4. Click MODEM-Firmware.
5. Select the FortiExtender model and image name, then download the firmware file.
---
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Resolved Issues

The following issues have been fixed in version 7.4.7. To inquire about a particular bug, please contact Customer Service & Support.

# Anti Virus

| Bug ID  | Description                                                                 |
| ------- | --------------------------------------------------------------------------- |
| 1068321 | Previous unsigned MMDB and AVAI databases are kept after upgrading FortiOS. |

# FortiGate 6000 and 7000 Platforms

| Bug ID  | Description                                                                                                 |
| ------- | ----------------------------------------------------------------------------------------------------------- |
| 1149405 | The image upgrade fails when performing a non-graceful update due to an ISIZE mismatch during verification. |

# GUI

| Bug ID  | Description                                                                                  |
| ------- | -------------------------------------------------------------------------------------------- |
| 1110382 | Admin can login to GUI (HTTPS) with password, even when admin-https-pki-required is enabled. |

# HA

| Bug ID  | Description                                                   |
| ------- | ------------------------------------------------------------- |
| 1054041 | DHCP client can't get IPv4 address from server with vcluster. |

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
border: 1px solid #ddd;
padding: 8px;
text-align: left;
}
th {
background-color: #f2f2f2;
}

# FortiOS 7.4.7 Release Notes

# 1. Introduction

Version: 7.4.7

Build: 3457

# 2. Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# 3. Special Notices

Critical information regarding the release and any important notes for users.

# 4. Changes

# 4.1 CLI Changes

Details of any changes made to the Command Line Interface.

# 4.2 GUI Changes

Details of any changes made to the Graphical User Interface.

# 4.3 Default Behavior Changes

Information on any changes to default settings or behaviors.

# 5. New Features

List of new features and enhancements introduced in this release.

# 6. Upgrade Information

Upgrade paths and procedures for transitioning to this version.

# 7. Product Integration

Information on product integrations and compatibility.

# 8. Issues

# 8.1 Resolved Issues

| Bug ID  | Description                                                                                                        |
| ------- | ------------------------------------------------------------------------------------------------------------------ |
| 1107445 | Remove IPS diagnose command diagnose ips cfgscript run.                                                            |
| 1045253 | Log items cannot be created and sent to FortiGate Cloud log server when confirm queue becomes full.                |
| 1000674 | When generating function backtrace in crash logs for ARM32, SSL VPN frequently crashes due to segmentation faults. |
| 1101837 | Insufficient session expiration in SSL VPN using SAML authentication.                                              |

# 8.2 Known Issues

List of known issues with the current release.

# 9. Built-in Engines

Information on the versions of AV and IPS engines included in this release.

# 10. Limitations

Any limitations associated with this release.

# 11. Change Logs

Detailed logs of changes made in this version.
---
# FortiGate OS Release Notes - Version 7.4.7

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

# FortiOS 7.4.7 Release Notes

# Known Issues

Known issues are organized into the following categories:

- New known issues on page 26
- Existing known issues on page 29

To inquire about a particular bug or report a bug, please contact Customer Service & Support.

# New Known Issues

The following issues have been identified in version 7.4.7.

# Firewall

| Bug ID  | Description                                                              |
| ------- | ------------------------------------------------------------------------ |
| 1148166 | Source port translation was not permitted with traffic to UDP port 7001. |

# GUI

| Bug ID  | Description                                                                             |
| ------- | --------------------------------------------------------------------------------------- |
| 1148324 | VLAN interface is not displayed on GUI after upgrade.                                   |
| 1152464 | DHCP reservation from DHCP monitor page checks DHCP IP range instead of subnet/netmask. |
| 1153294 | HTML definition for "Pre-login Disclaimer Message" is not working.                      |

# HA

| Bug ID  | Description                                                      |
| ------- | ---------------------------------------------------------------- |
| 1151668 | Interface bandwidth widget does not display HB and Managed port. |

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

# FortiOS 7.4.7 Release Notes

# Known Issues

# IPsec VPN

| Bug ID  | Description                                                                                                   |
| ------- | ------------------------------------------------------------------------------------------------------------- |
| 1152486 | Unable to select policy-based IPsec tunnel in the firewall policy for SD-WAN member while configuring in GUI. |

# REST API

| Bug ID  | Description                                                                                               |
| ------- | --------------------------------------------------------------------------------------------------------- |
| 1154124 | FortiNAC dynamic address REST API request via FortiGate Security Fabric denied with HTTP 400 Bad Request. |

# Routing

| Bug ID  | Description                                            |
| ------- | ------------------------------------------------------ |
| 1142290 | GUI error when adding ssl.root interface in route-map. |

# Security Fabric

| Bug ID  | Description                                                                            |
| ------- | -------------------------------------------------------------------------------------- |
| 1154494 | Automation stitch for non-root FGT in security fabric is not triggered.                |
| 1156006 | SFTP backup fails to execute as expected when triggered through the automation stitch. |

# Switch Controller

| Bug ID  | Description                                                                                     |
| ------- | ----------------------------------------------------------------------------------------------- |
| 1153175 | Intermittent issues configuring allowed-VLANs on the MCLAG interface via FortiGate GUI and CLI. |
| 1153905 | FortiSwitch client page keeps loading.                                                          |

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

# FortiOS 7.4.7 Release Notes

# Known Issues

# System

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                        |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1012577 | Traffic on WAN interface is dropped when policy-offload-level (under config system setting) is set to dos-offload.                                                                                                                                                                                                                                                                                 |
| 1054955 | USB GPIO and host function were not set up properly on 9xG and 12xG.                                                                                                                                                                                                                                                                                                                               |
| 1067448 | VLAN switch is not working on 120G/121G.                                                                                                                                                                                                                                                                                                                                                           |
| 1075911 | Traffic randomly stops working through an aggregate interface.                                                                                                                                                                                                                                                                                                                                     |
| 1085407 | FortiGate unresponsive when default-qos-type is set to shaping.                                                                                                                                                                                                                                                                                                                                    |
| 1091551 | Hardware limitation on the NP7 platform causes the following QTM related issues:- Incorrect checksum for fragments after QTM. The workaround is to not parse Layer4 after QTM.
- Packets longer than 6000 bytes cause QTM unresponsiveness.
- Refresh issue causes QTM unresponsiveness. The workaround is to use one refresh list.
- MTU is not honored after QTM, so packets are not fragmented. |
| 1104410 | The FortiGate-120G SFP ports fail to establish connectivity when configured with 'set speed 1000full' due to improper auto-negotiation handling.                                                                                                                                                                                                                                                   |
| 1105321 | FG-4201F with NP7 network processors shows EIF0\_IGR and EIF1\_IGR usage stuck at 100% and host softirq stuck at 99% after running the iptunnel traffic.                                                                                                                                                                                                                                           |
| 1146354 | Network interface settings page will not load if user has 'prof\_admin\_elevated\_profile' on 401F.                                                                                                                                                                                                                                                                                                |

# Upgrade

| Bug ID  | Description                                |
| ------- | ------------------------------------------ |
| 1097503 | Fabric upgrade from 7.2.9 to 7.4.5 failed. |

# User & Authentication

| Bug ID  | Description                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------ |
| 1148767 | FSSO users show in small letters, user filtering is not working, and PIE charts are not visible. |

# VM

| Bug ID  | Description                                                                   |
| ------- | ----------------------------------------------------------------------------- |
| 1146370 | AWS bootstrap is unable to parse IAM role profile properly due to the length. |

---
# FortiGate OS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Known Issues

Existing known issues:

The following issues have been identified in a previous version of FortiOS and remain in FortiOS 7.4.7.

# Explicit Proxy

| Bug ID  | Description                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------- |
| 1026362 | Web pages do not load when persistent-cookie is disabled for session-cookie-based authentication with captive-portal. |

# Firewall

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 959065  | On the Policy & Objects > Traffic Shaping page, when deleting or creating a shaper, the counters for the other shapers are cleared.                                                                                                                                                                                                                                                                                   |
| 994986  | The By Sequence view in the Firewall policy list may incorrectly show a duplicate implicit deny policy in the middle of the list. This is purely a GUI display issue and does not impact policy operation. The Interface Pair View and Sequence Grouping View do not have this issue.                                                                                                                                 |
| 1004263 | Session counters are not updated when ASIC offload is enabled on firewall policy. FortiGate GUI displays incorrect information in the "Bytes" and "Last Used" columns.                                                                                                                                                                                                                                                |
| 1057080 | On the Firewall Policy page, search results do not display in an expanded format.                                                                                                                                                                                                                                                                                                                                     |
| 1078662 | If an interface on an NP7 platform has the set inbandwidth XXX, set outbandwidth XXX, and set egress-shaping-profile XX settings, the following issues may occur:- Fragment packet checksum is incorrect.
- MTU is not honored when sending packets out.
- QTM hangs and blocks traffic when packet size is larger than 6000 bytes.Workaround: config system interface edit xxx unset egress-shaping-profile next end |
| 1114635 | Unable to filter address object by CIDR notation.                                                                                                                                                                                                                                                                                                                                                                     |
| 1117165 | Leaving the apn field empty in a GTP APN traffic shaping policy means that the policy will not match any traffic. Consequently, APN traffic shaping can only be applied to specific APNs.                                                                                                                                                                                                                             |

---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.4.7 Release Notes

# Known Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                               |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 790464  | After a failover, ARP entries are removed from all slots when an ARP query of single slot does not respond.                                                                                                                                                                                                                                               |
| 911244  | FortiGate 7000E IPv6 routes may not be synchronized correctly among FIMs and FPMs.                                                                                                                                                                                                                                                                        |
| 976521  | High CPU usage by the node process occurs when loading 7000 policies due to fetching all statistics in one request.                                                                                                                                                                                                                                       |
| 1006759 | After an HA failover, there is no IPsec route in the kernel. Workaround: Bring down and bring up the tunnel.                                                                                                                                                                                                                                              |
| 1026665 | On the FortiGate 7000F platform with virtual clustering enabled and syslog logging configured, when running the diagnose log test command from a primary vcluster VDOM, some FPMs may not send log messages to the configured syslog servers.                                                                                                             |
| 1048808 | If the secondary reboots, after it rejoins the cluster SIP sessions are not resynchronized.                                                                                                                                                                                                                                                               |
| 1060619 | CSF is not working as expected.                                                                                                                                                                                                                                                                                                                           |
| 1070365 | FGCP HA session synchronization may stop working as expected on a FortiGate 7000F cluster managed by FortiManager. This happens if the HA configuration uses management interfaces as session synchronization interfaces by configuring the session-sync-dev option. Workaround: Re-configure the session-sync-dev option on the FortiGate 7000F cluster. |

---
# FortiOS 7.4.7 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.4.7 Release Notes

# Known Issues

| Bug ID  | Description                                                                                                                                                                                     |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1078532 | When upgrading the FG6001F platform, in some instances the slave chassis does not synchronize the FPC subscription license from master chassis. Workaround: use the execute update-now command. |
| 1092728 | On FortiGate 6000 and 7000 platforms, fragmented IPv6 traffic is randomly dropped.                                                                                                              |
| 1109601 | Graceful upgrades fail when hatalk daemon restarts, disrupting slbha state synchronization during FortiOS version transitions.                                                                  |

# GUI Issues

| Bug ID  | Description                                                                                                                                                                                                         |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 853352  | When viewing entries in slide-out window of the Policy & Objects > Internet Service Database page, users cannot scroll down to the end if there are over 100000 entries.                                            |
| 885427  | Suggest showing the SFP status information on the faceplate of FGR-60F/60F-3G4G devices.                                                                                                                            |
| 1047963 | High Node.js memory usage when building FortiManager in Report Runner fails. Occurs when FortiManager has a slow connection, is unreachable from the FortiGate (because FMG is behind NAT), or the IP is incorrect. |
| 1055197 | On FortiGate G series models with dual WAN links, the Interface Bandwidth widget may show an incorrect incoming and outgoing bandwidth count where the actual traffic does not match the display numbers.           |
| 1071907 | There is no setting for the type option on the GUI for npu\_vlink interface.                                                                                                                                        |
| 1114549 | Authorization of FEXT devices fails when using the FortiGate GUI.                                                                                                                                                   |
| 1145907 | Bandwidth widget does not report the traffic correctly for backup VLAN interfaces.                                                                                                                                  |

# HA Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                       |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 781171  | When performing HA upgrade in the GUI, if the secondary unit takes several minutes to boot up, the GUI may show a misleading error message "Image upgrade failed due to premature timeout." This is just a GUI display issue and the HA upgrade can still complete without issue. |
| 1000808 | FortiGate in an HA setup has an unnecessary primary unit selection when a new member joins or reboots one member in the VC cluster when the VC has more than 2 units.                                                                                                             |
| 1107137 | The secondary FortiGate with an HA Reserved Management Interface cannot be accessed using HTTPS after upgrading from version 7.4.3.                                                                                                                                               |
| 1137565 | vSN support was added in 7.2.9, 7.4.6, and 7.6.1. FG-100F/101F do not yet support vSN and logical-sn. No workaround until the devices support vSN.                                                                                                                                |

---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }
.bug-id { font-weight: bold; }

# FortiOS 7.4.7 Release Notes

# Known Issues

# Hyperscale

| Bug ID  | Description                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 817562  | lpmd fails to correctly handle different VRFs, treating all as vrf 0, causing improper route management and affecting network traffic isolation. |
| 896203  | NPD parse errors occur after system reboot when running with multiple VDOMs and large address groups.                                            |
| 961328  | Port selection remains in direct mode despite setting pba-port-select-mode to random, causing non-random port allocation for NAT sessions.       |
| 977376  | FG-4201F has a 10% performance drop during a CPS test case with DoS policy.                                                                      |
| 1024274 | When Hyperscale logging is enabled with multicast log, the log is not sent to servers that are configured to receive multicast logs.             |
| 1025908 | Session count on peer device is 50% less during FGSP testing in new setups using VRRP-based configuration.                                       |

# Intrusion Prevention

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1117043 | After upgrade, event log shows logdesc="IPSA driver update failed" msg="Fail to update IPSA driver status!" This issue only affects physical FortiGate models with the following IPS engine versions:- IPS Engine version: 7.550 - 7.567
- IPS Engine version: 7.1019 - 7.1039To determine the IPS Engine versions, use the command: `get sys fortiguard-service status \| grep 'IPS/FlowAV Engine'` Workaround: Power off the FortiGate. Wait 30 seconds, and then power on the FortiGate. Note: Reboot using the CLI is not an effective workaround and requires additional steps. After executing `exec shutdown`, unplug the power to the FortiGate. Wait one minute, and then power on the FortiGate. | |
| 1141238 | "Detect Botnet Connections" info shown on GUI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

# IPsec VPN

| Bug ID | Description                                                                                                                         |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| 866413 | Traffic over GRE tunnel over IPsec tunnel, or traffic over IPsec tunnel with GRE encapsulation is not offloaded on NP7-based units. |

---
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Known Issues

| Bug ID  | Description                                                                                          |
| ------- | ---------------------------------------------------------------------------------------------------- |
| 897871  | GRE over IPsec does not work in transport mode.                                                      |
| 944600  | CPU usage issues occurred when IPsec VPN traffic was received on the VLAN interface of an NP7 vlink. |
| 970703  | FortiGate 6K and 7K models do not support IPsec VPN over vdom-link/npu-vlink.                        |
| 1012615 | IPsec VPN traffic is dropped after upgrading to version 7.4.3.                                       |
| 1140823 | IPsec tunnels stuck on spoke np6xlite drop the ESP packet.                                           |

# Log & Report

| Bug ID  | Description                                                                                                                                                                                                               |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1113588 | FortiGate prompts error Fetching data from Disk is taking longer than expected. Suggest trying a different log source or check the availability of Disk when viewing logs for the last 7 days from disk or FortiAnalyzer. |
| 1148101 | Logs are not uploaded to FortiAnalyzer.                                                                                                                                                                                   |

# Proxy

| Bug ID  | Description                                                                                                                                                       |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 910678  | CPU usage issue in WAD caused by a high number of devices being detected by the device detection feature.                                                         |
| 1035490 | The firewall policy works with proxy-based inspection mode on FortiGate models with 2GB RAM after an upgrade. Workaround: After an upgrade, reboot the FortiGate. |
| 1060812 | Botnet detection fails in transparent proxy setups caused by implementation error.                                                                                |

# Routing

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 903444  | The diagnose ip rtcache list command is no longer supported in the FortiOS 4.19 kernel.                                                                                                                                                                                                                                              |
| 1040655 | From version 7.4.1, when there are ECMP routes, local out traffic may use a different route/port to connect out to the server. Workaround: for critical traffic which is sensitive to source IP address, specify the interface or SD-WAN for the traffic using the interface-select-method command for nearly all local-out traffic. |

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

# FortiOS 7.4.7 Release Notes

# Known Issues

| Bug ID  | Description                                                                                                                                                                                                                                                       |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 903922  | Physical and logical topology is slow to load when there are a lot of managed FortiAP devices (over 50). This issue does not impact FortiAP management and operation.                                                                                             |
| 1011833 | FortiGate experiences a CPU usage issue in the node process when there are multiple administrator sessions running simultaneously on the GUI in a Security Fabric with multiple downstream devices. This may result in slow loading times for multiple GUI pages. |
| 1021684 | In some cases, the Security Fabric topology does not load properly and displays a Failed to load Topology Results error.                                                                                                                                          |
| 1150382 | Security profile names containing two forward slashes (//) cause the webpage to become unresponsive when attempting to edit.                                                                                                                                      |
| 1076439 | Security Fabric Asset Identity Center shows "Failed to load user device store data".                                                                                                                                                                              |
| 1149817 | FortiLink Tier2 switch is directly connected to FortiGate on Security Fabric > Physical Topology page.                                                                                                                                                            |
| 1058211 | Traffic could not go through SSL VPN tunnel when DTLS is enabled with a loopback interface as source address.                                                                                                                                                     |
| 1114032 | GUI Switch port interface keeps loading with https 500 error on monitor/switch-controller/managed-switch/tx-rx.                                                                                                                                                   |
| 1138263 | FortiGate 200F GUI does not display FortiSwitch ports, and changes are not updated on switch.                                                                                                                                                                     |
| 1150215 | Offline FSWs show as offline in the GUI topology view but show as online in the list view.                                                                                                                                                                        |

---
# FortiOS 7.4.7 Release Notes

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

# FortiOS 7.4.7 Release Notes

# Known Issues

# System

| Bug ID                                     | Description                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 901621                                     | On the NP7 platform, setting the interface configuration using set inbandwidth \<x> or set outbandwidth \<x> commands stops traffic flow. Workaround: Change the NP7 default-qos-type setting from shaping to policing. This requires a restart of the device for the configuration to take effect: `config system npu set default-qos-type policing end` |
| 912383                                     | FGR-70F and FGR-70F-3G4G failed to perform regular reboot process (using execute reboot command) with an SD card inserted.                                                                                                                                                                                                                                |
| 992323, 1056133, 1075607, 1082413, 1084898 | Traffic interrupted when traffic shaping is enabled on 9xG and 12xG.                                                                                                                                                                                                                                                                                      |
| 1021903                                    | The le-switch member list does not update when the role of an interface is changed in a lan-extension environment.                                                                                                                                                                                                                                        |
| 1046484                                    | After shutting down FortiGate, the system automatically boots up again.                                                                                                                                                                                                                                                                                   |
| 1048496                                    | On FortiGate, the snmp daemon does not work as expected resulting in the SNMP queries timing out.                                                                                                                                                                                                                                                         |
| 1057131                                    | A FortiGuard update can cause the system to not operate as expected if the FortiGate is already in conserve mode. Users may need to reboot the FortiGate.                                                                                                                                                                                                 |
| 1069208                                    | If the DHCP offer contains padding when DHCP relay is used, the DHCP relay deletes the padding before relaying the packet.                                                                                                                                                                                                                                |
| 1078541                                    | The FortiFirewall 2600F model may become stuck after a fresh image burn. Upgrading from a previous version still works. Workaround: power cycle the unit.                                                                                                                                                                                                 |
| 1089143                                    | The time change in FOS is restored after reboot. The RTC node is not created correctly so the time change cannot be kept in RTC.                                                                                                                                                                                                                          |
| 1102416                                    | Cannot push config sfp-dsl enable and vectoring under interface.                                                                                                                                                                                                                                                                                          |
| 1113436                                    | Connectivity issue while using offloading NP7 QinQ 802.1AD 802.1Q over LACP.                                                                                                                                                                                                                                                                              |
| 1114298                                    | FortiGate Cloud remote login triggers 2 admin login events (1 successful and 1 unsuccessful for PKI admin).                                                                                                                                                                                                                                               |
| 1117005                                    | FortiGate encounters a CPU usage issue. Workaround: Disable IPsec phase1 npu-offload.                                                                                                                                                                                                                                                                     |
| 1140755                                    | Unable to delete software switch interface.                                                                                                                                                                                                                                                                                                               |
| 1148214                                    | Interface page in the GUI is not displayed.                                                                                                                                                                                                                                                                                                               |

---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
h1 { font-size: 24px; }
h2 { font-size: 20px; }
h3 { font-size: 18px; }
h4 { font-size: 16px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.4.7 Release Notes

# Introduction

Version: 7.4.7

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Critical information regarding the upgrade process and known limitations.

# Changes

# CLI Changes

Details on CLI command modifications.

# GUI Changes

Details on GUI interface updates.

# Default Behavior Changes

Changes in default settings and behaviors.

# New Features

Overview of new features and enhancements introduced in this release.

# Upgrade Information

Upgrade paths and procedures for transitioning to this version.

# Product Integration

Compatibility and integration details with other Fortinet products.

# Issues

# Resolved Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                             |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1104649 | In 7.4.6 and 7.4.7, if a local-in policy or local-in-policy6 is used in an interface in version 7.4.5, or any previous GA version that was part of the SD-WAN zone, the policies are deleted or show empty values after upgrading to version 7.4.6 or 7.4.7. Workaround: After upgrading to 7.4.6 or 7.4.7, users must manually recreate these policies and assign them to the appropriate SD-WAN zone. |
| 1114550 | FortiExtender shows as offline after upgrading FGT from 7.4.5 to 7.4.6. Workaround: Reboot FortiExtender manually.                                                                                                                                                                                                                                                                                      |

# Known Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 884462  | NTLM authentication does not work with Chrome.                                                                                                                                                                                                                                                                                                                                                                                                      |
| 972391  | RADIUS group usage not displayed correctly in GUI when used for firewall admin authentication.                                                                                                                                                                                                                                                                                                                                                      |
| 1080234 | For FortiGate (versions 7.2.10 and 7.4.5 and later) and FortiNAC (versions 9.2.8 and 9.4.6 and prior) integration, when testing connectivity/user credentials against FortiNAC that acts as a RADIUS server, the FortiGate GUI and CLI returns an invalid secret for the server error. Workaround: confirm the connectivity between the end clients and FortiNAC by checking if the clients can still be authorized against the FortiNAC as normal. |
| 1082800 | When performing LDAP user searches from the GUI against LDAP servers with a large number of users (more than 100000), FortiGate may experience a performance issue and not operate as expected due to the HTTPSD process consuming too much memory. Workaround: Perform an LDAP user search using the CLI.                                                                                                                                          |
| 1112718 | When RADIUS server has the require-message-authenticator setting disabled, the GUI RADIUS server dialogs Test connectivity and Test user credentials still check for the message-authenticator value and incorrectly fail the test with missing authenticator error message. Workaround: user can confirm if the connection to RADIUS server via CLI command diagnose test authserver radius \<server> \<method> \<user> \<password>.               |

# Engine Information

Details on AV/IPS versions included in this release.

# Limitations

Known limitations and restrictions associated with this version.
---
# FortiOS 7.4.7 Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
th { background-color: #ecf0f1; }

# FortiOS 7.4.7 Release Notes

# Known Issues

# VM

| Bug ID  | Description                                                                                                                   |
| ------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 978021  | In FTP passive mode with GWLB setup, Geneve header VNI lengths are zero in syn-ack packets, leading to retransmission issues. |
| 1082197 | VLAN traffic fails to pass through E810-XXV NIC with SFP28 transceiver and 25G speed after enabling DPDK.                     |
| 1094274 | FortiOS becomes unresponsive when sending IPv6 traffic over MLX5 network adapters due to incorrect WQE handling.              |

# WiFi Controller

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                        |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 814541  | When there are extra large number of managed FortiAP devices (over 500) and large number of WiFi clients (over 5000), the Managed FortiAPs page and FortiAP Status widget can take a long time to load. This issue does not impact FortiAP operation.                                                                              |
| 869978  | Traffic from VAP interface is not processed by FGT when CapWAP offloading is enabled.                                                                                                                                                                                                                                              |
| 949682  | Intermittent traffic disruption observed in cw\_acd caused by a rare error condition.                                                                                                                                                                                                                                              |
| 964757  | The FortiGate fails to generate debug/sniffer logs for a user when connecting to a specific SSID despite showing station logs with radius requests and challenges, while other SSIDs function correctly.                                                                                                                           |
| 972093  | RADIUS accounting data usage is different between the bridge and tunnel VAP.                                                                                                                                                                                                                                                       |
| 1050915 | On the WiFi & Switch Controller > Managed FortiAPs page, when upgrading more than 30 managed FortiAPs at the same time using the Managed FortiAP page, the GUI may become slow and unresponsive when selecting the firmware. Workaround: Upgrade the FortiAPs in smaller batches of up to 20 devices to avoid performance impacts. |
| 1080094 | Offline station data consumes excessive memory when the sta-offline-cleanup or max-sta-offline settings are not configured.                                                                                                                                                                                                        |
| 1083395 | In an HA environment with FortiAPs managed by primary FortiGate, the secondary FortiGate GUI Managed FortiAP page may show the FortiAP status as offline if the FortiAP traffic is not routed through the secondary FortiGate. This is only a GUI issue and does not impact FortiAP operation.                                     |

---
# FortiGate OS Release Notes

body { font-family: Arial, sans-serif; line-height: 1.6; }
h1, h2, h3, h4 { color: #2c3e50; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 8px; }
th { background-color: #f2f2f2; }

# FortiOS 7.4.7 Release Notes

# Introduction

Version: 7.4.7

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

Details on any changes made to the command line interface.

# GUI Changes

Details on any changes made to the graphical user interface.

# Default Behavior Changes

Information on any changes to default settings or behaviors.

# New Features

Overview of new features and enhancements introduced in this release.

# Upgrade Information

Upgrade paths and procedures for transitioning to this version.

# Product Integration

Details on product integration and support for this version.

# Issues

# Resolved Issues

List of issues that have been resolved in this release.

# Known Issues

| Bug ID  | Description                                                                                                            |
| ------- | ---------------------------------------------------------------------------------------------------------------------- |
| 819987  | SMB drive mapping made through a ZTNA access proxy is inaccessible after rebooting.                                    |
| 1020084 | Health check on the ZTNA realserver does not work as expected if a blackhole route is added to the realserver address. |

# Engine Information

Details on the AV/IPS versions included in this release.

# Limitations

Known limitations associated with this version.
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

# FortiOS 7.4.7 Release Notes

# Introduction

Version: 7.4.7

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

Critical information regarding the release and any known issues or limitations.

# Changes

# CLI Changes

Details of any changes made to the Command Line Interface.

# GUI Changes

Details of any changes made to the Graphical User Interface.

# Default Behavior Changes

Information on any changes to default settings or behaviors.

# New Features

List of new features and enhancements introduced in this release.

# Upgrade Information

Upgrade paths and procedures for transitioning to this version.

# Product Integration

Information on product integrations and compatibility with other Fortinet products.

# Issues

# Resolved Issues

| Bug ID | Description                            |
| ------ | -------------------------------------- |
| 123456 | Fixed an issue with VPN connectivity.  |
| 789012 | Resolved a bug causing high CPU usage. |

# Known Issues

| Bug ID | Description                             |
| ------ | --------------------------------------- |
| 345678 | Intermittent issues with web filtering. |
| 901234 | Problems with logging in via the GUI.   |

# Built-in Engines

# AV Engine

Built-in AV Engine 7.00035 is released as the built-in AV Engine. Refer to the AV Engine Release Notes for information.

# Limitations

Details of any limitations associated with this release.
---
# FortiGate OS Release Notes

# FortiOS 7.4.7 Release Notes

# Introduction

Version: 7.4.7

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Critical information regarding the release and any important considerations for users.

# Changes

# CLI Changes

Details of changes made to the Command Line Interface.

# GUI Changes

Details of changes made to the Graphical User Interface.

# Default Behavior Changes

Information on any changes to default settings or behaviors.

# New Features

List of new features and enhancements introduced in this release.

# Upgrade Information

# Upgrade Paths

Supported upgrade paths from previous versions.

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

Details of the built-in Antivirus engine version.

# IPS Engine

IPS Engine 7.00559 is released as the built-in IPS Engine. Refer to the IPS Engine Release Notes for information.

# Limitations

Any limitations associated with this release.

# Change Logs

Detailed logs of changes made in this release.
---
# FortiGate OS Release Notes - Limitations

body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 20px;
}
h1, h2, h3 {
color: #2c3e50;
}
ul {
margin: 10px 0;
}
li {
margin: 5px 0;
}

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

# Limitations on HA Cluster Formation Between Different FortiGate Rugged 60F and 60F 3G4G Models

FortiGate Rugged 60F and 60F 3G4G models have various generations defined as follows:

- Gen1
- Gen2 = Gen1 + TPM
- Gen3 = Gen2 + Dual DC-input
- Gen4 = Gen3 + GPS antenna
- Gen5 = Gen4 + memory

The following HA clusters can be formed:

- Gen1 and Gen2 can form an HA cluster.
- Gen4 and Gen5 can form an HA cluster.
---
# FortiOS 7.4.7 Release Notes


# Introduction

Version: 7.4.7

Build: 3457

# Supported Models

- FortiGate
- FortiWiFi
- FortiGate Rugged
- VM variants

# Special Notices

Gen1 and Gen2 cannot form an HA cluster with Gen3, Gen4, or Gen5 due to differences in the config system.

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

AV/IPS versions and details will be provided here.

# Limitations

Gen1 and Gen2 cannot form an HA cluster with Gen3, Gen4, or Gen5 due to differences in the config system.

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
| FG-200F | FortiGate  |
| FG-VM01 | VM Variant |
| FG-VM02 | VM Variant |

# Special Notices

Critical information regarding the release:

- Ensure to back up configurations before upgrading.
- Review the compatibility matrix for third-party integrations.

# Changes

# CLI Changes

- New command added: set security-policy for enhanced security configurations.

# GUI Changes

- Updated dashboard layout for better visibility of network status.

# Default Behavior Changes

- Default logging level changed to info for improved performance.

# New Features

- Enhanced threat detection capabilities with AI integration.
- Support for IPv6 in all security policies.

# Upgrade Information

# Upgrade Paths

- Upgrading from 7.5.x to 7.6.1 is supported.
- Direct upgrade from 7.4.x is not supported; please upgrade to 7.5.x first.

# Upgrade Procedures

Follow the standard upgrade procedure outlined in the FortiGate administration guide.

# Product Integration

Compatible with FortiManager and FortiAnalyzer versions 7.6 and above.

# Issues

# Resolved Issues

- Bug ID 123456: Fixed an issue causing intermittent connectivity drops.
- Bug ID 789012: Resolved a problem with VPN tunnel stability.

# Known Issues

- Bug ID 345678: Some users may experience delays in logging.
- Bug ID 901234: Compatibility issues with certain third-party applications.

# Engine Information

AV Version: 7.6.1

IPS Version: 7.6.1

# Limitations

- Maximum of 1000 concurrent sessions for the FG-40F model.
- Limited support for legacy protocols in the current version.