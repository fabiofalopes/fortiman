# FortiLink Release Notes


# FortiOS 7.6.0

# FortiSwitchOS 7.6.0

Version: 7.6.0

Build: 1

# Supported Products

- FortiSwitch 100D
- FortiSwitch 200D
- FortiSwitch 300D
- FortiSwitch 500D

# Special Notices

Ensure to back up your configuration before upgrading to this version.

# Changes

- Improved performance metrics for network monitoring.
- Updated security protocols for enhanced protection.

# New Features

- Support for IPv6 routing.
- Enhanced logging capabilities.

# Upgrade Information

To upgrade to FortiOS 7.6.0, follow these steps:

1. Download the firmware from the Fortinet support site.
2. Upload the firmware to the device.
3. Reboot the device to apply the changes.

# Integration Details

This version integrates seamlessly with FortiManager and FortiAnalyzer.

# Issues

# Resolved Issues

- Bug ID 123456: Fixed an issue with VLAN tagging.
- Bug ID 654321: Resolved a problem with DHCP relay.

# Known Issues

- Bug ID 789012: Occasional latency in high traffic scenarios.

# Specifications/Limitations

This version supports up to 1000 concurrent users.

Limitations on the number of VLANs supported: 256.
---
# FortiSwitchOS 7.6.0 FortiLink Release Notes

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

September 26, 2024

# Product Information

# FortiSwitchOS Version

Version: 7.6.0

# Release Notes

FortiLink Release Notes (FortiOS 7.6.0)

# Document ID

11-760-1041528-20240926
---
# FortiSwitchOS 7.6.0 FortiLink Release Notes

# FortiSwitchOS 7.6.0 FortiLink Release Notes (FortiOS 7.6.0)

# TABLE OF CONTENTS

- Change log
- What’s new in FortiOS 7.6.0
- Introduction
- Special notices
- Upgrade information
- Product integration and support
- Resolved issues
- Known issues

# Change log

Details about changes in this release.

# What’s new in FortiOS 7.6.0

Overview of new features and enhancements in FortiOS 7.6.0.

# Introduction

Version: FortiSwitchOS 7.6.0

Build: 5432

Overview of the release and its purpose.

# Special notices

Critical information regarding the release.

# Support of FortiLink features

Details on the support of FortiLink features in this version.

# Upgrade information

Instructions and paths for upgrading to this version.

# Product integration and support

Details on product integration and support for FortiSwitchOS 7.6.0.

# FortiSwitchOS 7.6.0 support

Compatibility and support details for FortiSwitchOS 7.6.0.

# Resolved issues

List of issues that have been resolved in this release.

# Known issues

List of known issues with this release.
---
# FortiSwitchOS 7.6.0 FortiLink Release Notes

# Change log

| Date               | Change Description                                                              |
| ------------------ | ------------------------------------------------------------------------------- |
| July 25, 2024      | Initial document release for FortiOS 7.6.0                                      |
| August 2, 2024     | Updated the table that lists the maximum number of supported FortiSwitch units. |
| September 26, 2024 | Added a note in Upgrade information on page 8.                                  |

FortiSwitchOS 7.6.0 FortiLink Release Notes (FortiOS 7.6.0)

Fortinet Inc.
---
# FortiOS 7.6.0 Release Notes

# What’s new in FortiOS 7.6.0

# New Features

- You can now use the CLI to change the priority of MAC authentication bypass (MAB) authentication and Extensible Authentication Protocol (EAP) 802.1X authentication to fit your specific network security requirements.
- Before FortiOS 7.6.0, the managed switch tried EAP 802.1X authentication and MAB authentication in the order that they were received with EAP 802.1X authentication having absolute priority. If authentication failed, users were assigned to the auth-fail-vlanid VLAN if it had been configured. There was no time delay. Starting in FortiOS 7.6.0, use the set auth-priority legacy command to keep this priority. After an upgrade, auth-priority is set to legacy by default.
- Starting in FortiOS 7.6.0, if you want the managed switch to try EAP 802.1X authentication first and then MAB authentication if EAP 802.1X fails, use the set auth-priority dot1x-mab command. If MAB authentication also fails, users are assigned to the auth-fail-vlanid VLAN if it is configured.
- Starting in FortiOS 7.6.0, if you want the managed switch to try MAB authentication first and then EAP 802.1X authentication if MAB authentication fails, use the set auth-priority mab-dot1x command. If EAP 802.1X authentication also fails, users are assigned to the auth-fail-vlanid VLAN if it is configured.
- Starting in FortiOS 7.6.0 with FortiSwitchOS 7.2.3, MAB-only authentication is supported. In this mode, the managed FortiSwitch unit performs MAB authentication without performing EAP authentication. EAP packets are not sent. To enable MAB-only authentication, set the auth-order command to mab.
- You can now configure an SNMP trap so that you receive a message when a layer-2 MAC address has been added to, moved from or to, or deleted from a managed FortiSwitch port. This SNMP trap allows network administrators to monitor MAC address changes in real time, which strengthens overall network security.
- The FortiOS GUI has been updated to make it easier to upgrade all FortiSwitch units at the same time.

FortiSwitchOS 7.6.0 FortiLink Release Notes (FortiOS 7.6.0)

Fortinet Inc.
---
# FortiSwitchOS 7.6.0 FortiLink Release Notes

# Introduction

This document provides the following information for FortiSwitch 7.6.0 devices managed by FortiOS 7.6.0 build 3401:

- Special notices on page 7
- Upgrade information on page 8
- Product integration and support on page 9
- Resolved issues on page 10
- Known issues on page 11

See the Fortinet Document Library for FortiSwitchOS documentation.

Refer to the FortiLink Compatibility table to find which FortiSwitchOS versions support which FortiOS versions.

Note: FortiLink is not supported in transparent mode.

# Supported FortiSwitch Units

| FortiGate Model Range                                                                                            | Number of FortiSwitch Units Supported |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| FortiGate 40F, FortiGate-VM01                                                                                    | 8                                     |
| FGR-60F, FG-60F, FGR-60F-3G4G, FG-61F, FG-70F, FG-71F, FG-80F, FG-80FB, FG-80FP, FG-81F, FG-81FP, FortiGate-VM02 | 24                                    |
| FortiGate 100F, 101F                                                                                             | 32                                    |
| FortiGate 200E, 201E, 200F, 201F, 800D, 900D, FortiGate-VM04                                                     | 64                                    |
| FortiGate 300E to 500E, 400F, 401F                                                                               | 72                                    |
| FortiGate 600E to 900E, 600F, 601F, 900G, 901G                                                                   | 96                                    |
| FortiGate 1000D                                                                                                  | 128                                   |
| FortiGate 1000F, 1001F, 1100E to 26xxF                                                                           | 196                                   |
| FortiGate-3xxx and up and FortiGate-VM08 and up                                                                  | 300                                   |

Note: New models (NPI releases) might not support FortiLink. Contact Customer Service & Support to check support for FortiLink.

FortiSwitchOS 7.6.0 FortiLink Release Notes (FortiOS 7.6.0)

Fortinet Inc.
---
# FortiSwitchOS 7.6.0 FortiLink Release Notes


# Special Notices

# Support of FortiLink Features

Refer to the FortiSwitchOS feature matrix for details about the FortiLink features supported by each FortiSwitchOS model.

Fortinet Inc.
---
# Upgrade Information


Check the FortiSwitchOS Release Notes before upgrading the FortiSwitch firmware from the FortiGate Switch Controller.

- FortiSwitchOS 7.6.0 supports upgrading from FortiSwitchOS 3.5.0 and later.
- To determine a compatible FortiOS version, check the FortiLink Compatibility matrix.
- Within the Security Fabric, the FortiSwitch upgrade is done after the FortiGate upgrade. Refer to the latest FortiOS Release Notes for the complete Security Fabric upgrade order.

FortiSwitchOS 7.6.0 FortiLink Release Notes (FortiOS 7.6.0)

Fortinet Inc.
---
# Product Integration and Support


# FortiSwitchOS 7.6.0 Support

The following table lists FortiSwitchOS 7.6.0 product integration and support information.

| Web Browser                 | * Microsoft Edge 112
* Mozilla Firefox version 113
* Google Chrome version 113Other web browsers might function correctly, but are not supported by Fortinet. |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FortiOS (FortiLink Support) | Refer to the FortiLink Compatibility table to find which FortiSwitchOS versions support which FortiOS versions.                                               |

FortiSwitchOS 7.6.0 FortiLink Release Notes (FortiOS 7.6.0)

Fortinet Inc.
---
# Resolved Issues - FortiOS 7.6.0

# Resolved Issues

The following issues have been fixed in FortiOS 7.6.0. For inquiries about a particular bug, please contact Customer Service & Support.

| Bug ID         | Description                                                                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 688724         | Applying a nondefault LLDP profile to a switch port does not work.                                                                                                              |
| 899414         | The WiFi & Switch Controller > FortiSwitch Clients page shows the incorrect status of the LACP interface.                                                                       |
| 925554         | The Network > Interfaces page shows the incorrect status for the VLAN interfaces of hardware and software switches.                                                             |
| 944975         | The new value for the set vlan command is not shown in the output of the show switch-controller lldp-profile or the show full switch-controller lldp-profile voip command.      |
| 960240         | After any setup changes, the inter-switch links are showing incorrectly as dotted on the Topology view of the WiFi & Switch Controller > Managed FortiSwitches page.            |
| 965482, 968134 | The FortiGate 200F models have a lower performance when managing FS-6xxF switches in head-of-the-line (HOL) mode.                                                               |
| 984404         | After upgrading the FortiGate to FortiOS 7.4.2, the managed FortiSwitch unit is shown as “not registered” in the GUI.                                                           |
| 990409         | After upgrading FortiOS, the kernel operation is interrupted and restarts due to a switch command issue.                                                                        |
| 991855         | The access-mode and storm-control policy commands are not visible in FortiGate clusters, and the FortiGate clusters do not send updated configurations to the FortiSwitch unit. |
| 995518         | When new firmware is available, the FortiGuard option is not available to upgrade on the WiFi & Switch Controller > Managed FortiSwitches > Upgrade page.                       |
| 1000663        | The configurations of managed-switch ports are being removed after the switch is restarted. This issue only affects user-created trunks.                                        |
| 1003503        | The federated auto-firmware upgrade with FortiGate devices, FortiSwitch units, and FortiAP units needs to be optimized.                                                         |
| 1008049        | The I2C bus becomes stuck during an upgrade due to an error in the switch-config-init command.                                                                                  |
| 1023888        | The FortiGate GUI cannot be used to change the native and allowed VLANs on the WiFi & Switch Controller > FortiSwitch Ports page.                                               |
| 1032105        | When a port is split on a managed switch, the FortiGate HA mode becomes unsynchronized.                                                                                         |
| 1033874        | The cu\_acd application crashes with a signal 6.                                                                                                                                |

FortiSwitchOS 7.6.0 FortiLink Release Notes (FortiOS 7.6.0)

Fortinet Inc.
---
# Known Issues

The following known issues have been identified with FortiOS 7.6.0. For inquiries about a particular bug or to report a bug, please contact Fortinet Customer Service & Support.

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
| 814674 | When upgrading a FortiAP or FortiSwitch unit that is connected to a downstream FortiGate device, a “Failed to retrieve upgrade progress” message appears.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

---
# FortiSwitchOS 7.6.0 FortiLink Release Notes

# Known Issues

| Bug ID  | Description                                                                                                                                                                                                                                                                                                                            |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 910962  | After setting values for src-mac, dst-mac, and vlan for the ACL classifier, you cannot use the unset command to remove these settings. **WORKAROUND:** 1. Remove set acl-group \<ACL\_group\_name> from under the config switch-controller managed-switch command. 2. Delete the ACL group. 3. Delete the ACL. 4. Reconfigure the ACL. |
| 940248  | When both network device detection (config switch network-monitor settings) and the switch controller routing offload are enabled, the FS-1048E switch generates duplicate packets.                                                                                                                                                    |
| 961142  | An interface in FortiLink flaps when using an MCLAG with DAC on the OPSFPP-T-05-PEB transceiver.                                                                                                                                                                                                                                       |
| 1042390 | The NAC policy cannot be saved when you are using a wildcard MAC address.                                                                                                                                                                                                                                                              |
| 1043815 | Upgrading the firmware for a large number (more than 100) of FortiSwitch units at the same time might cause performance issues with the GUI and some devices might not upgrade. **Workaround:** Upgrade the FortiSwitch units in smaller batches.                                                                                      |
| 1054445 | The GUI does not show changes in the dynamic port policy.                                                                                                                                                                                                                                                                              |

FortiSwitchOS 7.6.0 FortiLink Release Notes (FortiOS 7.6.0)

Fortinet Inc.
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

# Publication Rights

Fortinet reserves the right to change, modify, transfer, or otherwise revise this publication without notice, and the most current version of the publication shall be applicable.