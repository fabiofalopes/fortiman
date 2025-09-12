# FortiSwitch VLAN Configuration Issue - Troubleshooting Guide

**Issue:** Unable to configure native VLANs on FortiSwitch ports via GUI, changes not persisting, lack of device visibility  
**Environment:** FortiGate 1101E (FortiOS 7.4.5) managing FortiSwitch 1048E devices  

## Problem Summary

You're experiencing multiple interconnected issues:

1. **VLAN Configuration Not Persisting**: Changes to native VLAN settings on switch ports appear to save but don't actually take effect
2. **Device Visibility Loss**: No MAC address information or device details visible on connected ports
3. **Network Connectivity Issues**: Devices remain on previous network segments despite VLAN changes
4. **Limited Administrative Access**: Restricted to FortiSwitch port management only

## Root Cause Analysis

Based on the FortiOS release notes and your environment, you're hitting **multiple known bugs**:

### Primary Issue: Bug #1023888
- **Description**: "Changes made to the Allowed VLANs and Native VLAN columns are not saved when edited on the GUI"
- **Affected Versions**: FortiOS 7.4.5 (your current version), 7.6.0
- **Status**: Known issue, still present in your firmware version
- **Impact**: GUI changes to VLAN configuration don't persist

### Secondary Issue: Bug #1096481  
- **Description**: "Access-mode changes cannot be made for FortiSwitch ports when using the FortiOS GUI"
- **Affected Versions**: FortiSwitchOS 7.4.7 and related FortiOS versions
- **Workaround**: Use CLI instead of GUI for access mode changes

### Contributing Factors
1. **High CPU/Memory Usage** (Bugs #1077496, #1138333): May cause configuration sync delays
2. **Device Detection Issues**: Network monitoring may be impacted by performance issues
3. **FortiLink Synchronization Problems**: Configuration changes may not propagate properly to switches

## Immediate Workarounds

### 1. Use CLI for VLAN Configuration (Primary Solution)

Since the GUI is broken for VLAN changes, you must use the CLI. Here's how:

```bash
# Connect to FortiGate CLI
# Navigate to switch controller configuration
config switch-controller managed-switch
    # Replace with your switch serial number
    edit "FS1E48T422002174"  # DC-L_CORE-FIB01 serial
        config ports
            # Replace with the specific port you want to configure
            edit "port24"  # Example port
                set vlan "your-target-vlan-name"
                set allowed-vlans "vlan1" "vlan2" "your-target-vlan-name"
                # For access mode (single VLAN)
                set access-mode enable
            next
        end
    next
end
```

### 2. Force Configuration Synchronization

After making CLI changes, force a configuration sync:

```bash
# Force FortiLink configuration push
execute switch-controller config-sync
```

### 3. Verify Configuration Applied

Check if the configuration actually took effect:

```bash
# Check switch port configuration
show switch-controller managed-switch FS1E48T422002174 ports port24

# Check if the switch received the configuration
execute switch-controller get-conn-status
```

## Device Visibility Issues

The lack of device information (MAC addresses, etc.) is likely related to:

### 1. Device Detection Disabled/Impaired
Check if device detection is enabled on the interfaces:

```bash
# Check device detection status
show system interface | grep -A 5 -B 5 "device-identification"

# Enable device detection if disabled (requires interface access)
config system interface
    edit "your-interface-name"
        set device-identification enable
    next
end
```

### 2. Network Monitor Issues
The network monitoring might be affected by the CPU/memory bugs. Check status:

```bash
# Check network monitor status
diagnose switch-controller dump network-monitor

# Check if switches are responding
execute switch-controller get-conn-status
```

## Systematic Troubleshooting Steps

### Step 1: Verify Current State
```bash
# Check FortiGate version
get system status

# Check managed switches status
show switch-controller managed-switch

# Check specific switch connectivity
execute switch-controller get-conn-status
```

### Step 2: Identify Problematic Ports
```bash
# List all managed switch ports and their current VLAN assignments
show switch-controller managed-switch FS1E48T422002174 ports

# Check for any error messages
diagnose debug application flcfgd -1
diagnose debug enable
# Make a configuration change and observe debug output
diagnose debug disable
```

### Step 3: Apply CLI Workaround
For each port that needs VLAN changes:

```bash
config switch-controller managed-switch
    edit "FS1E48T422002174"
        config ports
            edit "port[X]"
                # For access port (single VLAN)
                set vlan "target-vlan-name"
                set access-mode enable
                
                # For trunk port (multiple VLANs)
                set allowed-vlans "vlan1" "vlan2" "target-vlan"
                set untagged-vlans "native-vlan-name"
                set access-mode disable
            next
        end
    next
end
```

### Step 4: Force Synchronization and Verification
```bash
# Push configuration to switches
execute switch-controller config-sync

# Wait 30 seconds, then verify
show switch-controller managed-switch FS1E48T422002174 ports port[X]

# Check device connectivity
execute ping [device-ip-if-known]
```

## Long-term Solutions

### 1. Firmware Upgrade Path
Based on the upgrade analysis document, consider upgrading to **FortiSwitchOS 7.4.7**:
- Fixes CPU/memory issues (bugs #1077496, #1138333)
- More stable than 7.6.x versions
- Still requires CLI workaround for VLAN GUI issues

### 2. Configuration Management
- Document all VLAN changes in CLI format
- Create scripts for bulk port configuration
- Implement regular configuration backups

### 3. Monitoring Improvements
- Set up structured logging to external syslog server
- Monitor switch CPU/memory usage
- Implement automated configuration verification

## Emergency Procedures

If you need immediate network connectivity for critical devices:

### 1. Temporary Physical Workaround
- Move device to a port that's already on the correct VLAN
- Use a different switch if available

### 2. CLI Emergency Configuration
```bash
# Quick access mode configuration for immediate connectivity
config switch-controller managed-switch
    edit "FS1E48T422002174"
        config ports
            edit "port[X]"
                set vlan "emergency-vlan-name"
                set access-mode enable
            next
        end
    next
end
execute switch-controller config-sync
```

## Verification Commands

After implementing workarounds:

```bash
# Verify VLAN assignment
show switch-controller managed-switch FS1E48T422002174 ports port[X]

# Check device detection
diagnose switch-controller dump network-monitor

# Verify network connectivity
execute ping [target-device-ip]

# Check for any error logs
execute log filter category 3
execute log display
```

## Next Steps

1. **Immediate**: Use CLI workarounds for critical port configurations
2. **Short-term**: Plan firmware upgrade to 7.4.7 during maintenance window
3. **Long-term**: Implement proper configuration management and monitoring

This systematic approach should resolve your VLAN configuration issues and restore device visibility while working around the known FortiOS bugs.