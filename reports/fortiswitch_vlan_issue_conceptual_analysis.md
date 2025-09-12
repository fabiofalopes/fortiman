# FortiSwitch VLAN Configuration Issue - Conceptual Analysis

**Context:** Limited user access, GUI-only interaction, multiple switches affected  
**Goal:** Understand what's happening conceptually without administrative access  

## What You're Actually Experiencing

Based on your description and the documented bugs, here's what's conceptually happening in your environment:

### The GUI Deception
- You click and configure VLAN settings in the FortiGate web interface
- The interface accepts your changes and appears to save them
- **Behind the scenes**: Due to Bug #1023888, these changes never actually get written to the switch configuration
- The FortiGate's database might even show the "new" configuration, but it's not pushed to the physical switches
- This creates a disconnect between what you see in the GUI and what's actually configured on the hardware

### Why Devices Stay on Old Networks
When you change a port's native VLAN from VLAN 10 to VLAN 20:
1. **What should happen**: The switch port gets reconfigured, device gets new DHCP lease on VLAN 20
2. **What actually happens**: The switch port stays on VLAN 10 because the configuration never changed
3. **Result**: Device keeps its old IP and network access as if nothing happened

### The Visibility Problem
The lack of device information (MAC addresses, device details) suggests:
- **Device detection services are impaired**: High CPU/memory usage from FortiLink bugs affects monitoring
- **Network monitoring is degraded**: The same performance issues impact the systems that track connected devices
- **Database synchronization issues**: Information about connected devices isn't being properly collected or displayed

## What's Likely Configured Differently Now

Something changed in your environment recently that's causing this behavior. Possible scenarios:

### Scenario 1: Firmware-Related Change
- Someone updated FortiOS to a version with these bugs
- A firmware update introduced the GUI VLAN configuration bug
- Performance degradation from new firmware is affecting device detection

### Scenario 2: Permission/Access Control Changes
- Your user account permissions were modified
- A policy change restricted GUI configuration capabilities
- Administrative access was centralized, leaving you with read-only-like access

### Scenario 3: System Performance Degradation
- High CPU/memory usage on FortiGate is preventing proper configuration processing
- FortiLink communication between FortiGate and switches is impaired
- Database corruption or synchronization issues between GUI and actual configuration

### Scenario 4: Network Architecture Changes
- New VLANs or network policies were implemented that conflict with your changes
- Centralized configuration management was implemented that overrides local changes
- Network segmentation policies are preventing your configurations from taking effect

## Why This Affects Multiple Switches

The fact that this happens across several switches in different locations strongly suggests:

### Centralized Issue
- **FortiGate-level problem**: Since all switches are managed by the same FortiGate, a bug or configuration issue there affects everything
- **Not a hardware problem**: Multiple switches having the same issue simultaneously points to software/configuration
- **Systematic change**: Something was changed at the management level that affects all managed switches

### Consistent Bug Behavior
- Bug #1023888 affects all FortiSwitch port configurations via GUI
- The bug is consistent - it doesn't work on any switch, not just specific ones
- This explains why you see the same behavior everywhere

## The Administrative Lock-Out Pattern

Your description of having "barely minimum" access suggests:

### Intentional Restriction
- Someone implemented stricter access controls
- Your role was changed to a more limited permission set
- New security policies restrict configuration capabilities

### System Protection Mode
- The FortiGate might be in a degraded state where it's protecting itself by limiting changes
- High resource usage could trigger protective measures that limit user operations
- Database inconsistencies might cause the system to restrict configuration changes

## What's Actually Happening When You "Configure"

When you make changes in the GUI:

1. **GUI Level**: Interface accepts and displays your changes
2. **Application Level**: FortiOS processes the change request
3. **Bug Intervention**: Bug #1023888 prevents the change from being written to the configuration database
4. **Switch Level**: No configuration update is sent to the physical switch
5. **Result**: Switch continues operating with old configuration

This creates the illusion that you're configuring things when you're actually just interacting with a broken interface layer.

## Why Traditional Troubleshooting Won't Work

The standard approach would be:
- Check logs → You can't access logs
- Verify configuration → You can't run CLI commands  
- Test connectivity → You have limited network access
- Check system status → You can't run diagnostic commands

This leaves you in a "black box" situation where you can observe symptoms but can't investigate causes.

## The Real Problem (Conceptually)

You're dealing with a **software bug masquerading as a configuration issue**. The problem isn't that you don't know how to configure VLANs - the problem is that the configuration system is fundamentally broken due to known bugs, and you don't have the access level needed to work around those bugs.

## What This Means for Your Work

### Short-term Reality
- VLAN configuration via GUI will continue to fail
- Device visibility will remain impaired
- Network changes will require alternative approaches or escalation

### The Access Problem
- Your current access level is insufficient to work around the bugs
- The people with proper access aren't available
- You're stuck in a situation where you can see the problem but can't fix it

### Business Impact
- Network configuration requests will continue to fail
- Troubleshooting capabilities are severely limited
- Work backlog will continue to grow until someone with proper access addresses the underlying bugs

## Conceptual Solutions (If You Had Access)

The fix would involve:
1. **Using CLI instead of GUI** for VLAN configuration (requires admin access)
2. **Upgrading firmware** to versions that fix the CPU/memory issues (requires admin access)
3. **Implementing workarounds** for the persistent GUI bugs (requires admin access)

Since you don't have this access, the issue will persist until someone with appropriate permissions addresses it at the system level.

## Documentation Value

This analysis serves as:
- **Evidence** of a systematic issue affecting multiple switches
- **Technical context** for when you need to escalate to administrators
- **Conceptual understanding** of why traditional configuration approaches aren't working
- **Business justification** for why network configuration tasks are currently impossible

The core issue isn't your configuration skills or network knowledge - it's a combination of software bugs and access restrictions that create an impossible working situation.