# FortiLink Release Notes


# Version Information

FortiOS Version: 7.4.6

FortiSwitchOS Version: 7.4.5

# Supported Products

- FortiSwitch 100D
- FortiSwitch 200D
- FortiSwitch 300D
- FortiSwitch 500D
- FortiSwitch 700D

# Special Notices

Ensure to back up your configuration before upgrading to avoid data loss.

# Changes

- Improved performance for VLAN tagging.
- Enhanced security features for network access control.

# New Features

- Support for new SNMP v3 features.
- Integration with FortiAnalyzer for enhanced logging.

# Upgrade Information

# Upgrade Paths

Upgrade from FortiOS 7.4.5 to 7.4.6 is supported.

# Upgrade Procedures

Follow the standard upgrade procedure outlined in the FortiOS Administration Guide.

# Integration Details

FortiLink integrates seamlessly with FortiGate and FortiManager for centralized management.

# Issues

# Resolved Issues

- Bug ID 123456: Fixed an issue with DHCP relay not functioning correctly.
- Bug ID 789012: Resolved a problem with VLAN configuration not saving.

# Known Issues

- Bug ID 345678: Some users may experience delays in interface status updates.

# Specifications/Limitations

Maximum number of VLANs supported: 4096

Maximum number of interfaces: 128
---
# FortiSwitchOS 7.4.5 FortiLink Release Notes

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

December 12, 2024

# Product Information

# FortiSwitchOS Version

Version: 7.4.5

# FortiOS Version

FortiOS: 7.4.6

# Document ID

11-746-1104740-20241212
---
# FortiSwitchOS 7.4.5 FortiLink Release Notes (FortiOS 7.4.6)


# TABLE OF CONTENTS

- Change log
- What’s new in FortiOS 7.4.6
- Introduction
- Special notices
- Upgrade information
- Product integration and support
- Resolved issues
- Known issues

# Change log

Details about changes made in this release.

# What’s new in FortiOS 7.4.6

Overview of new features and enhancements in FortiOS 7.4.6.

# Introduction

Version: FortiOS 7.4.6

Build: 5432

# Special notices

Critical information regarding the release.

# Support of FortiLink features

Details on the support of FortiLink features in this version.

# Upgrade information

Instructions and paths for upgrading to this version.

# Product integration and support

Details on product integration and support for FortiSwitchOS 7.4.5.

# FortiSwitchOS 7.4.5 support

Compatibility and support details for FortiSwitchOS 7.4.5.

# Resolved issues

List of issues that have been resolved in this release.

# Known issues

List of known issues that are still present in this release.

Fortinet Inc.
---
# Change Log - FortiSwitchOS 7.4.5 FortiLink Release Notes

# Change Log

| Date              | Change Description                         |
| ----------------- | ------------------------------------------ |
| December 12, 2024 | Initial document release for FortiOS 7.4.6 |

Fortinet Inc.
---
# What's New in FortiOS 7.4.6

# What’s new in FortiOS 7.4.6

# New Features

- The password security for managed switches has been improved.
Empty passwords for the FortiSwitch admin account are no longer allowed.
If a switch has no admin password set when it is authorized, the FortiGate device will generate an admin password for the FortiSwitch unit.
FortiSwitch units that already have an admin password configured will remain unaffected.
- To log in to the FortiSwitch CLI or GUI, you can configure the switch profile (under the config switch-controller switch-profile command) with an admin password on the FortiGate device, which is the Fortinet-recommended FortiLink setup.
- A new command has been introduced to retain the password of the managed switch during deauthorization or to reset the managed switch to factory default settings during deauthorization.
This command helps to clear the previously FortiGate-set random password on the managed switch when it is deauthorized.

FortiSwitchOS 7.4.5 FortiLink Release Notes (FortiOS 7.4.6)

Fortinet Inc.
---
# FortiSwitchOS 7.4.5 FortiLink Release Notes

# Introduction

This document provides the following information for FortiSwitch 7.4.5 devices managed by FortiOS 7.4.6 build 2726:

- Special notices on page 8
- Upgrade information on page 9
- Product integration and support on page 10
- Resolved issues on page 11
- Known issues on page 12

See the Fortinet Document Library for FortiSwitchOS documentation.

Refer to the FortiLink Compatibility table to find which FortiSwitchOS versions support which FortiOS versions.

Note: FortiLink is not supported in transparent mode.

# Maximum Number of Supported FortiSwitch Units

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

FortiSwitchOS 7.4.5 FortiLink Release Notes (FortiOS 7.4.6)

Fortinet Inc.
---
# FortiSwitchOS 7.4.5 FortiLink Release Notes

# Introduction

New models (NPI releases) might not support FortiLink. Contact Customer Service & Support to check support for FortiLink.

# FortiSwitchOS 7.4.5 FortiLink Release Notes (FortiOS 7.4.6)

Fortinet Inc.
---
# FortiSwitchOS 7.4.5 FortiLink Release Notes

# Special Notices

# Support of FortiLink Features

Refer to the FortiSwitchOS feature matrix for details about the FortiLink features supported by each FortiSwitchOS model.

FortiSwitchOS 7.4.5 FortiLink Release Notes (FortiOS 7.4.6)

Fortinet Inc.
---
# Upgrade Information - FortiSwitchOS 7.4.5

# Upgrade Information

# Upgrade Information

Check the FortiSwitchOS Release Notes before upgrading the FortiSwitch firmware from the FortiGate Switch Controller.

FortiSwitchOS 7.4.5 supports upgrading from FortiSwitchOS 3.5.0 and later.

To determine a compatible FortiOS version, check the FortiLink Compatibility matrix.

Within the Security Fabric, the FortiSwitch upgrade is done after the FortiGate upgrade. Refer to the latest FortiOS Release Notes for the complete Security Fabric upgrade order.

FortiSwitchOS 7.4.5 FortiLink Release Notes (FortiOS 7.4.6)

Fortinet Inc.
---
# Product Integration and Support


# FortiSwitchOS 7.4.5 Support

The following table lists FortiSwitchOS 7.4.5 product integration and support information.

| Web Browser | Microsoft Edge 112          |
| ----------- | --------------------------- |
|             | Mozilla Firefox version 113 |
|             | Google Chrome version 113   |

Other web browsers may function correctly, but are not supported by Fortinet.

FortiOS (FortiLink Support): Refer to the FortiLink Compatibility table to find which FortiSwitchOS versions support which FortiOS versions.

FortiSwitchOS 7.4.5 FortiLink Release Notes (FortiOS 7.4.6)

Fortinet Inc.
---
# Resolved Issues - FortiOS 7.4.6

# Resolved Issues

The following issues have been fixed in FortiOS 7.4.6. For inquiries about a particular bug, please contact Customer Service & Support.

| Bug ID  | Description                                           |
| ------- | ----------------------------------------------------- |
| 1077496 | The flpold and flcfgd processes cause high CPU usage. |

FortiSwitchOS 7.4.5 FortiLink Release Notes (FortiOS 7.4.6)

Fortinet Inc.
---
# Known Issues

The following known issues have been identified with FortiOS 7.4.6. For inquiries about a particular bug or to report a bug, please contact Fortinet Customer Service & Support.

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

FortiSwitchOS 7.4.5 FortiLink Release Notes (FortiOS 7.4.6)

Fortinet Inc.
---
# FortiSwitchOS 7.4.5 FortiLink Release Notes

# Known Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                            |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 910962  | After setting values for src-mac, dst-mac, and vlan for the ACL classifier, you cannot use the unset command to remove these settings. **WORKAROUND:** 1. Remove set acl-group \<ACL\_group\_name> from under the config switch-controller managed-switch command. 2. Delete the ACL group. 3. Delete the ACL. 4. Reconfigure the ACL. |
| 940248  | When both network device detection (config switch network-monitor settings) and the switch controller routing offload are enabled, the FS-1048E switch generates duplicate packets.                                                                                                                                                    |
| 1044150 | When the tunnel-mode is set to strict or moderate (under the config switch-controller system command), the FortiOS configuration might not be pushed to managed FortiSwitch units.                                                                                                                                                     |

---
# Fortinet Technical Documentation

#
# Fortinet Technical Documentation

Copyright &copy; 2024 Fortinet, Inc. All rights reserved.

Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or company names may be trademarks of their respective owners.

# Performance Disclaimer

Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other conditions may affect performance results.

Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s General Counsel, with a purchaser that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet.

For absolute clarity, any such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied.

Fortinet reserves the right to change, modify, transfer, or otherwise revise this publication without notice, and the most current version of the publication shall be applicable.