# FortiGate VLAN Configuration Issue - Forum Post Draft

**Environment:**
- FortiGate 1101E running FortiOS 7.4.5
- Multiple FortiSwitch 1048E devices in FortiLink mode
- Multi-location deployment

## Issue Description

We're experiencing consistent issues with VLAN configuration changes on FortiSwitch ports that don't seem to take effect, despite the GUI appearing to accept and save the changes. This is happening across multiple switches in different locations, all managed by the same FortiGate.

### Symptoms Observed:
1. **GUI Configuration Appears Successful**: When changing native VLAN assignments on switch ports via the FortiGate GUI (WiFi & Switch Controller > FortiSwitch Ports), the interface accepts the changes and shows them as saved.

2. **Changes Don't Take Effect**: Despite GUI confirmation, connected devices remain on their previous network segments. DHCP renewals, cable unplugging/reconnecting, and other standard troubleshooting steps don't resolve the connectivity.

3. **Device Visibility Issues**: We're also experiencing reduced visibility into connected devices - MAC address information and device details that were previously available are no longer showing up consistently.

4. **Consistent Across Multiple Switches**: This behavior is reproducible across several FortiSwitch 1048E units in different physical locations, suggesting a centralized rather than hardware-specific issue.

### Access Limitations:
Our current administrative access is limited to FortiSwitch port management through the GUI. We don't have CLI access to the FortiGate or switches, and have limited visibility into system logs or diagnostic information.

## Documentation Review Findings

While researching this issue, we found something potentially relevant in the FortiOS release notes:

**Bug ID 1023888** is described as: "On the WiFi & Switch Controller > FortiSwitch Ports page, changes made to the Allowed VLANs and Native VLAN columns are not saved when edited on the GUI."

This description matches our symptoms exactly. However, we noticed this bug appears in the release notes as follows:

- **FortiOS 7.4.5** (our current version): Listed under "Resolved Issues"
- **FortiOS 7.6.0**: Also listed under "Resolved Issues"

## Questions for the Community:

1. **Has anyone experienced similar VLAN configuration issues** with FortiOS 7.4.5 and FortiSwitch 1048E combinations?

2. **Is it normal for the same bug ID to appear as "resolved" in multiple versions?** We're trying to understand if this indicates the initial fix was incomplete.

3. **Are there any known workarounds** for VLAN configuration issues when GUI access is the only available option?

4. **What diagnostic information would be most helpful** for an administrator with full access to investigate this type of issue?

## Additional Context:

- The issue started recently (within the last few days)
- No known configuration changes were made to the FortiGate
- Physical connectivity and cable integrity have been verified
- Issue affects both new configuration attempts and modifications to existing port assignments

## What We're Looking For:

- Confirmation from others who may have experienced similar issues
- Understanding of whether this is a known limitation or bug
- Guidance on what information a network administrator would need to properly diagnose this issue
- Any workarounds that don't require CLI access

We're particularly interested in understanding whether this type of GUI/configuration synchronization issue is common with FortiLink deployments, and what steps typically resolve it.

Any insights or similar experiences would be greatly appreciated.

---

**Note**: We've anonymized specific network details and serial numbers for security purposes, but can provide additional technical details if needed for troubleshooting.