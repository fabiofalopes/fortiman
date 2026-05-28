# FortiGate VDOM Troubleshooting Guide

## Understanding VDOM Implementation

### What VDOMs Are
Virtual Domains (VDOMs) allow a single FortiGate to operate as multiple virtual firewalls, each with:
- Independent security policies
- Separate routing tables
- Isolated administrative domains
- Dedicated interface assignments

### VDOM Impact on FortiLink Management

#### Normal FortiLink Operation
- FortiGate manages FortiSwitches through FortiLink protocol
- Switch ports appear in FortiGate interface as managed ports
- Centralized policy and VLAN management
- Unified visibility across switching infrastructure

#### VDOM Complications
- Switch ports can be assigned to specific VDOMs
- Administrative access may be VDOM-restricted
- Policy inheritance from VDOM configuration
- Potential isolation between VDOM environments

## Troubleshooting VDOM-Related Issues

### Symptoms of VDOM Problems
- Configuration changes not taking effect
- Devices not appearing in network discovery
- Inconsistent behavior across switch locations
- MAC address visibility issues

### Diagnostic Questions
1. **VDOM Assignment**: Which VDOM are the problematic switches assigned to?
2. **User Context**: What VDOM context is your user account operating in?
3. **Policy Inheritance**: Are there VDOM-level policies overriding switch configurations?
4. **Interface Mapping**: How are physical interfaces mapped to VDOMs?

### Investigation Steps

#### 1. Identify Current VDOM Context
- Check if GUI shows VDOM selector
- Note which VDOM is currently active
- Verify if user has multi-VDOM access

#### 2. Map Switch-to-VDOM Assignments
- Document which switches work vs. don't work
- Identify patterns in switch locations
- Check if problematic switches share VDOM assignment

#### 3. Compare Working vs. Non-Working Configurations
- Export configurations from working switches
- Compare VLAN assignments and policies
- Look for VDOM-specific restrictions

#### 4. Check Policy Inheritance
- Verify if VDOM policies override switch settings
- Look for conflicting security policies
- Check if VLAN ranges are restricted per VDOM

## Common VDOM-Related Problems

### Access Control Issues
- User restricted to specific VDOM
- Switch assigned to different VDOM than user access
- Insufficient permissions within VDOM context

### Configuration Conflicts
- VDOM policies overriding switch configurations
- VLAN restrictions at VDOM level
- Security policies blocking traffic

### Visibility Problems
- MAC learning disabled in VDOM
- Monitoring restricted to specific VDOM
- Cross-VDOM communication blocked

## Recommended Solutions

### For Network Administrators
1. **Document VDOM Architecture**: Create clear mapping of VDOMs to infrastructure
2. **User Role Management**: Ensure operational staff have appropriate VDOM access
3. **Policy Documentation**: Document how VDOM policies affect switch behavior
4. **Troubleshooting Access**: Provide diagnostic tools within VDOM constraints

### For Network Technicians
1. **VDOM Awareness**: Understand which VDOM context you're working in
2. **Pattern Recognition**: Document which switches/locations have issues
3. **Escalation Information**: Provide VDOM context when escalating issues
4. **Workaround Documentation**: Record successful configuration patterns

## Questions to Ask When Escalating

1. "Which VDOM are the problematic switches assigned to?"
2. "Does my user account have access to the correct VDOM?"
3. "Are there VDOM-level policies affecting switch port configuration?"
4. "Can you verify the VLAN assignments are not restricted in this VDOM?"
5. "Is there a way to check if MAC learning is enabled for this VDOM?"

## Long-term Recommendations

### Architecture Review
- Evaluate if VDOM complexity is justified
- Consider simplifying VDOM structure if possible
- Document business requirements for VDOM separation

### Access Management
- Implement role-based access that spans necessary VDOMs
- Provide troubleshooting tools within security constraints
- Create operational procedures for VDOM environments

### Training and Documentation
- Train staff on VDOM concepts and implications
- Document VDOM-to-infrastructure mappings
- Create troubleshooting guides specific to VDOM environment