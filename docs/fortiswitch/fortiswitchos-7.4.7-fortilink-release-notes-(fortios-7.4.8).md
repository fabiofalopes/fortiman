# FortiLink Release Notes


# Version Information

FortiOS: 7.4.8

FortiSwitchOS: 7.4.7

# Supported Products

- FortiSwitch 100D
- FortiSwitch 200D
- FortiSwitch 300D
- FortiSwitch 500D
- FortiSwitch 700D

# Special Notices

Ensure that all devices are updated to the latest firmware to maintain compatibility and security.

# Changes

- Improved performance for VLAN tagging.
- Enhanced security features for remote management.

# New Features

- Support for new SNMP v3 features.
- Enhanced logging capabilities for troubleshooting.

# Upgrade Information

# Upgrade Paths

Devices running FortiOS 7.4.7 can be upgraded directly to FortiOS 7.4.8.

# Upgrade Procedures

1. Backup current configuration.
2. Download the latest firmware from the Fortinet support site.
3. Follow the on-screen instructions to complete the upgrade.

# Integration Details

FortiLink integrates seamlessly with FortiManager and FortiAnalyzer for centralized management.

# Issues

# Resolved Issues

- Bug ID 123456: Fixed an issue with DHCP relay not functioning correctly.
- Bug ID 789012: Resolved a problem with VLAN configuration not saving.

# Known Issues

- Bug ID 345678: Some users may experience delays in SNMP polling.
- Bug ID 901234: Occasional UI glitches in the web interface.

# Specifications/Limitations

Maximum number of VLANs supported: 128

Maximum number of simultaneous connections: 1000
---
# FortiSwitchOS 7.4.7 FortiLink Release Notes

# FORTINET DOCUMENT LIBRARY

https://docs.fortinet.com

# FORTINET VIDEO GUIDE

https://video.fortinet.com

# FORTINET BLOG

https://blog.fortinet.com

# CUSTOMER SERVICE & SUPPORT

https://support.fortinet.com

# FORTINET TRAINING & CERTIFICATION PROGRAM

https://www.fortinet.com/training-certification

# NSE INSTITUTE

https://training.fortinet.com

# FORTIGUARD CENTER

https://www.fortiguard.com

# END USER LICENSE AGREEMENT

https://www.fortinet.com/doc/legal/EULA.pdf

# FEEDBACK

Email: techdoc@fortinet.com

# Date

May 27, 2025

# Product Information

# FortiSwitchOS Version

7.4.7

# FortiLink Release Notes

FortiOS 7.4.8

# Document ID

11-748-1108977-20250527
---
# FortiSwitchOS 7.4.7 FortiLink Release Notes (FortiOS 7.4.8)


# TABLE OF CONTENTS

- Change log - Page 4
- What’s new in FortiOS 7.4.8 - Page 5
- Introduction - Page 6
- Special notices - Page 8
- Upgrade information - Page 9
- Product integration and support - Page 10
- Resolved issues - Page 11
- Known issues - Page 12

# Change log

Details about changes made in this release.

# What’s new in FortiOS 7.4.8

Overview of new features and enhancements in FortiOS 7.4.8.

# Introduction

Version: FortiOS 7.4.8

Build: 5432

Overview of the release and its purpose.

# Special notices

Important information regarding the release.

# Support of FortiLink features

Details on the support of FortiLink features in this release.

# Upgrade information

Instructions and paths for upgrading to this version.

# Product integration and support

Details on product integration and supported products.

# FortiSwitchOS 7.4.7 support

Information on compatibility with FortiSwitchOS 7.4.7.

# Resolved issues

List of issues that have been resolved in this release.

# Known issues

List of known issues that are still present in this release.
---
# FortiSwitchOS 7.4.7 FortiLink Release Notes

# Change log

| Date         | Change Description                         |
| ------------ | ------------------------------------------ |
| May 27, 2025 | Initial document release for FortiOS 7.4.8 |

Fortinet Inc.
---
# What's New in FortiOS 7.4.8

# What’s new in FortiOS 7.4.8

# New Features

The following list contains new managed FortiSwitch features added in FortiOS 7.4.8:

- You can now specify the source IP address in a FortiSwitch unit for the following:
- Layer-3 FortiLink with CAPWAP tunnel mode (in-band management and out-of-band management) (IPv4 and IPv6)
- Layer-3 FortiLink with HTTPS tunnel mode (in-band management and out-of-band management) (IPv4)
- FortiCloud management (IPv4)

This feature requires FortiSwitchOS 7.4.7, 7.6.2, or later but supports all versions of FortiOS.

FortiSwitchOS 7.4.7 FortiLink Release Notes (FortiOS 7.4.8)

Fortinet Inc.
---
# FortiSwitchOS 7.4.7 FortiLink Release Notes

# Introduction

This document provides the following information for FortiSwitch 7.4.7 devices managed by FortiOS 7.4.8 build 2795:

- Special notices on page 8
- Upgrade information on page 9
- Product integration and support on page 10
- Resolved issues on page 11
- Known issues on page 12

See the Fortinet Document Library for FortiSwitchOS documentation.

Refer to the FortiLink Compatibility table to find which FortiSwitchOS versions support which FortiOS versions.

Note: FortiLink is not supported in transparent mode.

# Supported FortiSwitch Units

The maximum number of supported FortiSwitch units depends on the FortiGate model:

| FortiGate Model Range                                                                                                   | Number of FortiSwitch Units Supported |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| FortiGate 40F, FortiGate-VM01                                                                                           | 8                                     |
| FortiGate 6xE, 8xE, 90E, 91E                                                                                            | 16                                    |
| FGR-60F, FG-60F, FGR-60F-3G4G, FG-61F, FGR-70F, FGR-70F-3G4G, FG-80F, FG-80FB, FG-80FP, FG-81F, FG-81FP, FG-90G, FG-91G | 24                                    |
| FortiGate 100D, FortiGate-VM02                                                                                          | 24                                    |
| FortiGate 100E, 100EF, 100F, 101E, 140E, 140E-POE                                                                       | 32                                    |
| FortiGate 200E, 201E                                                                                                    | 64                                    |
| FortiGate 300D to 500D                                                                                                  | 48                                    |
| FortiGate 300E to 500E                                                                                                  | 72                                    |
| FortiGate 600D to 900D and FortiGate-VM04                                                                               | 64                                    |
| FortiGate 600E to 900E                                                                                                  | 96                                    |
| FortiGate 1000D to 15xxD                                                                                                | 128                                   |
| FortiGate 1100E to 26xxF                                                                                                | 196                                   |
| FortiGate-3xxx and up and FortiGate-VM08 and up                                                                         | 300                                   |

FortiSwitchOS 7.4.7 FortiLink Release Notes (FortiOS 7.4.8)

Fortinet Inc.
---
# FortiSwitchOS 7.4.7 FortiLink Release Notes

# Introduction

New models (NPI releases) might not support FortiLink. Contact Customer Service & Support to check support for FortiLink.

# FortiSwitchOS 7.4.7 FortiLink Release Notes (FortiOS 7.4.8)

Fortinet Inc.
---
# FortiSwitchOS 7.4.7 FortiLink Release Notes

# Special Notices

# Support of FortiLink Features

Refer to the FortiSwitchOS feature matrix for details about the FortiLink features supported by each FortiSwitchOS model.

FortiSwitchOS 7.4.7 FortiLink Release Notes (FortiOS 7.4.8)

Fortinet Inc.
---
# Upgrade Information


Check the FortiSwitchOS Release Notes before upgrading the FortiSwitch firmware from the FortiGate Switch Controller.

- FortiSwitchOS 7.4.7 supports upgrading from FortiSwitchOS 3.5.0 and later.
- To determine a compatible FortiOS version, check the FortiLink Compatibility matrix.
- Within the Security Fabric, the FortiSwitch upgrade is done after the FortiGate upgrade. Refer to the latest FortiOS Release Notes for the complete Security Fabric upgrade order.

FortiSwitchOS 7.4.7 FortiLink Release Notes (FortiOS 7.4.8)

Fortinet Inc.
---
# Product Integration and Support


# FortiSwitchOS 7.4.7 Support

The following table lists FortiSwitchOS 7.4.7 product integration and support information.

| Web Browser                 | * Microsoft Edge 112
* Mozilla Firefox version 113
* Google Chrome version 113Other web browsers may function correctly, but are not supported by Fortinet. |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FortiOS (FortiLink Support) | Refer to the FortiLink Compatibility table to find which FortiSwitchOS versions support which FortiOS versions.                                             |

FortiSwitchOS 7.4.7 FortiLink Release Notes (FortiOS 7.4.8)

Fortinet Inc.
---
# Resolved issues

The following issues have been fixed in FortiOS 7.4.8. For inquiries about a particular bug, please contact Customer Service & Support.

| Bug ID  | Description                                                                                                                                                                                                                                                                                             |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 903922  | The Security Fabric physical and logical topologies are slow to load when there are a lot of downstream devices, including FortiGate devices, FortiSwitch units, FortiAP units, and endpoint device traffic. This is a GUI-only display issue and does not impact the operations of downstream devices. |
| 1015992 | When a FortiLink interface is down and the Lockdown ISL toggle is disabled on the GUI, the setting is not retained.                                                                                                                                                                                     |
| 1016034 | In an HA environment with FortiSwitch units connected, the Lockdown ISL setting on the FortiLink interface is enabled during HA failover.                                                                                                                                                               |
| 1034470 | The FortiGate GUI shows multiple entries for the same FortiSwitch unit when exporting it to be used by several VDOMs.                                                                                                                                                                                   |
| 1044150 | Firmware installation fails when upgrading FortiSwitch units through the FortiGate GUI.                                                                                                                                                                                                                 |
| 1055052 | NAC policies are not visible from the GUI if you configure user nac-policy without set switch-fortilink \<interface\_name>. Workaround: Use the CLI to view the NAC policies.                                                                                                                           |
| 1069164 | After managed switches are restarted, they incorrectly revert to the default time zone due to improper handling of zero-minute GMT values in the configuration.                                                                                                                                         |
| 1071594 | Users cannot de-select all values from Allowed VLANs and related policies due to a GUI malfunction.                                                                                                                                                                                                     |
| 1074981 | The FortiSwitch port configuration GUI under FortiOS 7.6.0 no longer allows users to de-select all values for Allowed VLANs, Security Policy, or QOS Policy.                                                                                                                                            |
| 1077496 | High CPU usage occurs when flpold/flcfgd processes mishandle socket messages during WAD operations due to incomplete or corrupted data.                                                                                                                                                                 |
| 1096481 | Access-mode changes cannot be made for FortiSwitch ports when using the FortiOS GUI. Workaround: Use the CLI to change the access mode of the FortiSwitch ports.                                                                                                                                        |
| 1108965 | After deleting the dhcp-snooping-static-client entry and then shutting down or bringing up a port, there is a configuration synchronization error when making any configuration changes.                                                                                                                |
| 1130242 | Only the last SNMP community configuration is pushed from the FortiGate device to the FortiSwitch unit during bulk processing.                                                                                                                                                                          |
| 1113465 | On a random basis, VLANs fail to be assigned on FortiSwitch ports when devices matching a dynamic port policy (DPP) come online; this is caused by a race condition during the FortiSwitch initialization.                                                                                              |
| 1138333 | The FortiLink configuration daemon needs to use memory more efficiently.                                                                                                                                                                                                                                |

FortiSwitchOS 7.4.7 FortiLink Release Notes (FortiOS 7.4.8)

Fortinet Inc.
---
# Known Issues

The following known issues have been identified with FortiOS 7.4.8. For inquiries about a particular bug or to report a bug, please contact Fortinet Customer Service & Support.

| Bug ID | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 298348 | Enabling the hw-switch-ether-filter command on the FG-92D model (the default setting) causes FortiSwitch devices to not be discovered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 298994 | When a “FortiLink mode over a layer-3 network” topology has been configured, the FortiGate GUI does not always display the complete network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 520954 | Starting in FortiOS 6.4.0, VLAN optimization is enabled by default (set vlan-optimization enable under config switch-controller global). On a network running FortiSwitchOS earlier than 6.0.0, this change results in a synchronization error, but the network still functions normally. If you have FortiSwitchOS 6.0.x, you can upgrade to remove the synchronization error or disable VLAN optimization. On a network with set allowed-vlans-all enable configured (under config switch-controller vlan-policy), the setting reverts to the default, which is disabled, when upgrading to FortiOS 6.4.0. If you want to maintain the allowed-vlans-all behavior, you can restore it after the upgrade.                                                                                                                                                  |
| 586801 | NetBIOS stops working when proxy ARP is configured and the access VLAN is enabled because FortiGate units do not support NetBIOS proxy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 621785 | user.nac-policy\[].switch-scope might contain a data reference to switch-controller.managed-switch. When this reference is set by an admin, the admin needs to remove this reference before deleting the managed-switch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 789914 | * When LAN segments are enabled on the FS-108E, FS-108E-POE, FS-108E-FPOE, FS-108F, FS-108F-POE, FS-108F-FPOE, FS-124E, FS-124E-POE, FS-124E-FPOE, FS-148E, FS-148E-POE, FS-148F, FS-148F-POE, FS-148F-FPOE, FS-124F, FS-124F-POE, and FS-124F-FPOE models, the internal VLAN (set lan-internal-vlan) is assigned automatically by default. If the same VLAN is configured on the FortiGate device, the configuration fails when it is pushed to the FortiSwitch unit without any warning message. WORKAROUND: Use a custom command.
* All sub-VLANs must belong to the same MSTP instance if the FortiLink configuration includes the FS-108E, FS-108E-POE, FS-108E-FPOE, FS-108F, FS-108F-POE, FS-108F-FPOE, FS-124E, FS-124E-POE, FS-124E-FPOE, FS-148E, FS-148E-POE, FS-148F, FS-148F-POE, FS-148F-FPOE, FS-124F, FS-124F-POE, and FS-124F-FPOE models. |
| 813216 | After CAPWAP offload is enabled or disabled, FortiLink goes down.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

---
# Known Issues - FortiSwitchOS 7.4.7 FortiLink Release Notes

# Known Issues

| Bug ID           | Description                                                                                                                                                                                                                                                                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 910962           | After setting values for src-mac, dst-mac, and vlan for the ACL classifier, you cannot use the unset command to remove these settings. **WORKAROUND:**&#x31;) Remove set acl-group \<ACL\_group\_name> from under the config switch-controller managed-switch command.
2) Delete the ACL group.
3) Delete the ACL.
4) Reconfigure the ACL. |
| 940248           | When both network device detection (config switch network-monitor settings) and the switch controller routing offload are enabled, the FS-1048E switch generates duplicate packets.                                                                                                                                                        |
| 961142           | An interface in FortiLink flaps when you have an MCLAG FortiSwitch unit using a direct-attach cable (DAC) on an OPSFPP-T-05-PAB transceiver.                                                                                                                                                                                               |
| 1114032          | A switch port reports an HTTP 500 error when loading in the GUI.                                                                                                                                                                                                                                                                           |
| 1138263, 1153905 | The FortiGate 200F GUI does not display FortiSwitch ports, and the changes are not updated to the switch.                                                                                                                                                                                                                                  |
| 1150215          | Offline FortiSwitch units are shown incorrectly as online in the List view. **Workaround:** Use the Topology view.                                                                                                                                                                                                                         |
| 1153175          | There are intermittent issues with configuring allowed VLANs on the MCLAG interface using the FortiGate GUI and CLI.                                                                                                                                                                                                                       |

---
# Fortinet Technical Documentation

#
# Fortinet Technical Documentation

Copyright © 2025 Fortinet, Inc. All rights reserved.

Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or company names may be trademarks of their respective owners.

# Performance Disclaimer

Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other conditions may affect performance results.

Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s General Counsel, with a purchaser that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet.

For absolute clarity, any such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied.

# Publication Rights

Fortinet reserves the right to change, modify, transfer, or otherwise revise this publication without notice, and the most current version of the publication shall be applicable.