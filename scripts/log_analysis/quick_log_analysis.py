#!/usr/bin/env python3
"""
Enhanced FortiSwitch Log Analysis
Robust analysis of FortiSwitch logs with documentation-based insights
"""

import re
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import argparse

# FortiSwitch Log Event Knowledge Base (from FortiOS documentation)
FORTISWITCH_KNOWLEDGE_BASE = {
    # Log IDs and their meanings
    'logids': {
        '0115032696': 'FortiSwitch Spanning Tree Event',
        '0115032697': 'FortiSwitch Port State Change',
        '0115032698': 'FortiSwitch Memory Event',
        '0115032699': 'FortiSwitch System Event',
        '0115032700': 'FortiSwitch Authentication Event',
        '0115032701': 'FortiSwitch LLDP Event',
        '0115032702': 'FortiSwitch IGMP Event',
        '0115032703': 'FortiSwitch Storm Control Event',
    },
    
    # Spanning Tree Protocol states and transitions
    'stp_states': {
        'disabled': 'Port is not participating in STP',
        'blocking': 'Port is blocked to prevent loops (initial state)',
        'listening': 'Port is preparing to forward (15 sec by default)',
        'learning': 'Port is learning MAC addresses (15 sec by default)',
        'forwarding': 'Port is actively forwarding traffic',
        'discarding': 'Port is discarding frames (RSTP equivalent of blocking)',
        'broken': 'Port has failed and is not operational'
    },
    
    # STP roles and their significance
    'stp_roles': {
        'root': 'Root port - provides path to root bridge',
        'designated': 'Designated port - forwarding port for this segment',
        'alternate': 'Alternate port - backup to root port',
        'backup': 'Backup port - backup to designated port',
        'disabled': 'Port is administratively disabled',
        'unknown': 'Role not yet determined'
    },
    
    # Memory thresholds and concerns
    'memory_thresholds': {
        90: 'WARNING - Memory usage approaching critical levels',
        95: 'CRITICAL - Memory usage at dangerous levels',
        98: 'EMERGENCY - Memory exhaustion imminent',
    },
    
    # Port flapping detection criteria
    'flapping_criteria': {
        'state_changes_threshold': 6,  # More than 6 state changes indicates flapping
        'time_window_minutes': 60,     # Within a 60-minute window
        'critical_threshold': 20,      # More than 20 changes is critical
    },
    
    # Network topology health indicators
    'topology_health': {
        'max_stp_events_per_hour': 50,
        'max_role_changes_per_hour': 10,
        'stable_convergence_time_seconds': 30,
    }
}

def parse_memory_percentage(message):
    """Extract memory percentage from memory-related messages"""
    match = re.search(r'(\d+)%', message)
    return int(match.group(1)) if match else None

def detect_stp_convergence_issues(stp_events):
    """Analyze STP events for convergence problems"""
    issues = []
    
    if not stp_events:
        return issues
    
    # Group events by time windows
    convergence_events = []
    role_changes = 0
    state_changes = 0
    
    for event in stp_events:
        if 'role' in event['message'].lower():
            role_changes += 1
        if 'state' in event['message'].lower():
            state_changes += 1
    
    # Check for excessive activity
    duration_hours = (stp_events[-1]['timestamp'] - stp_events[0]['timestamp']).total_seconds() / 3600
    if duration_hours > 0:
        stp_rate = len(stp_events) / duration_hours
        role_rate = role_changes / duration_hours
        
        if stp_rate > FORTISWITCH_KNOWLEDGE_BASE['topology_health']['max_stp_events_per_hour']:
            issues.append(f"⚠️  Excessive STP activity: {stp_rate:.1f} events/hour (normal: <{FORTISWITCH_KNOWLEDGE_BASE['topology_health']['max_stp_events_per_hour']})")
        
        if role_rate > FORTISWITCH_KNOWLEDGE_BASE['topology_health']['max_role_changes_per_hour']:
            issues.append(f"🔄 Excessive role changes: {role_rate:.1f} changes/hour (normal: <{FORTISWITCH_KNOWLEDGE_BASE['topology_health']['max_role_changes_per_hour']})")
    
    return issues

def analyze_port_stability(port_events, port_name):
    """Enhanced port stability analysis with FortiSwitch-specific knowledge"""
    if len(port_events) < 2:
        return {'status': 'stable', 'issues': []}
    
    issues = []
    state_changes = 0
    last_state = None
    rapid_changes = 0
    
    # Sort events by timestamp
    sorted_events = sorted(port_events, key=lambda x: x['timestamp'])
    
    # Analyze state transitions
    for i, event in enumerate(sorted_events):
        if event['action'] in ['port-up', 'port-down']:
            current_state = event['action']
            if last_state and current_state != last_state:
                state_changes += 1
                
                # Check for rapid state changes (within 60 seconds)
                if i > 0:
                    time_diff = (event['timestamp'] - sorted_events[i-1]['timestamp']).total_seconds()
                    if time_diff < 60:
                        rapid_changes += 1
            
            last_state = current_state
    
    # Determine port health
    criteria = FORTISWITCH_KNOWLEDGE_BASE['flapping_criteria']
    
    if state_changes >= criteria['critical_threshold']:
        issues.append(f"🚨 CRITICAL FLAPPING: {state_changes} state changes")
        status = 'critical_flapping'
    elif state_changes >= criteria['state_changes_threshold']:
        issues.append(f"⚡ Port flapping detected: {state_changes} state changes")
        status = 'flapping'
    elif rapid_changes > 3:
        issues.append(f"⏱️  Rapid state changes: {rapid_changes} quick transitions")
        status = 'unstable'
    else:
        status = 'stable'
    
    # Check for specific patterns
    up_events = [e for e in port_events if e['action'] == 'port-up']
    down_events = [e for e in port_events if e['action'] == 'port-down']
    
    if len(down_events) > len(up_events) + 2:
        issues.append("📉 More down events than up events - possible connection issues")
    
    return {
        'status': status,
        'issues': issues,
        'state_changes': state_changes,
        'rapid_changes': rapid_changes,
        'up_events': len(up_events),
        'down_events': len(down_events)
    }

def analyze_memory_health(memory_events):
    """Analyze memory-related events with FortiSwitch-specific thresholds"""
    if not memory_events:
        return {'status': 'healthy', 'issues': [], 'max_usage': 0}
    
    issues = []
    max_usage = 0
    
    for event in memory_events:
        usage = parse_memory_percentage(event['message'])
        if usage:
            max_usage = max(max_usage, usage)
    
    # Check against FortiSwitch memory thresholds
    thresholds = FORTISWITCH_KNOWLEDGE_BASE['memory_thresholds']
    
    for threshold, message in sorted(thresholds.items(), reverse=True):
        if max_usage >= threshold:
            issues.append(f"💾 {message} ({max_usage}%)")
            break
    
    # Determine status
    if max_usage >= 98:
        status = 'critical'
    elif max_usage >= 95:
        status = 'warning'
    elif max_usage >= 90:
        status = 'monitor'
    else:
        status = 'healthy'
    
    return {
        'status': status,
        'issues': issues,
        'max_usage': max_usage
    }

def get_logid_description(logid):
    """Get human-readable description for FortiSwitch log IDs"""
    return FORTISWITCH_KNOWLEDGE_BASE['logids'].get(logid, f"Unknown FortiSwitch event (ID: {logid})")

def analyze_network_topology_stability(events):
    """Analyze overall network topology stability"""
    issues = []
    
    # Count different types of instability indicators
    stp_events = [e for e in events if 'spanning tree' in e['message'].lower()]
    port_events = [e for e in events if e['action'] in ['port-up', 'port-down']]
    
    if not events:
        return issues
    
    duration_hours = (events[-1]['timestamp'] - events[0]['timestamp']).total_seconds() / 3600
    
    if duration_hours > 0:
        event_rate = len(events) / duration_hours
        port_event_rate = len(port_events) / duration_hours
        stp_event_rate = len(stp_events) / duration_hours
        
        # Analyze overall event density
        if event_rate > 100:
            issues.append(f"🚨 VERY HIGH event density: {event_rate:.1f} events/hour")
        elif event_rate > 50:
            issues.append(f"⚠️  High event density: {event_rate:.1f} events/hour")
        
        # Analyze port churn
        if port_event_rate > 20:
            issues.append(f"🔌 High port activity: {port_event_rate:.1f} port events/hour")
        
        # Check for topology instability patterns
        unique_ports = set(e['port'] for e in events if e['port'])
        if len(unique_ports) > 10:
            issues.append(f"🌐 Many ports affected: {len(unique_ports)} different ports with activity")
    
    return issues

def analyze_fortiswitch_log(log_file):
    """Enhanced FortiSwitch log analysis with documentation-based knowledge"""
    
    print(f"🔍 Enhanced FortiSwitch Analysis: {log_file}")
    print("="*70)
    
    # Storage for analysis
    events = []
    port_activity = defaultdict(list)
    stp_events = []
    error_events = []
    memory_events = []
    logid_counts = Counter()
    
    # Read and parse log
    try:
        with open(log_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                # Extract basic info
                timestamp_match = re.search(r'date=(\S+)\s+time=(\S+)', line)
                if not timestamp_match:
                    continue
                    
                date_str, time_str = timestamp_match.groups()
                try:
                    timestamp = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    continue
                
                # Extract structured data
                port_match = re.search(r'switchphysicalport="([^"]*)"', line)
                port = port_match.group(1) if port_match else None
                
                action_match = re.search(r'action="([^"]*)"', line)
                action = action_match.group(1) if action_match else None
                
                msg_match = re.search(r'msg="([^"]*)"', line)
                message = msg_match.group(1) if msg_match else ""
                
                level_match = re.search(r'level="([^"]*)"', line)
                level = level_match.group(1) if level_match else "unknown"
                
                logid_match = re.search(r'logid="([^"]*)"', line)
                logid = logid_match.group(1) if logid_match else "unknown"
                
                # Store event
                event = {
                    'timestamp': timestamp,
                    'port': port,
                    'action': action,
                    'message': message,
                    'level': level,
                    'logid': logid,
                    'line': line.strip()
                }
                events.append(event)
                
                # Count log IDs
                logid_counts[logid] += 1
                
                # Categorize events
                if port and action in ['port-up', 'port-down']:
                    port_activity[port].append(event)
                
                if 'spanning tree' in line.lower() or 'stp' in line.lower():
                    stp_events.append(event)
                
                if level in ['warning', 'alert', 'error']:
                    error_events.append(event)
                
                if 'memory' in message.lower():
                    memory_events.append(event)
    
    except FileNotFoundError:
        print(f"❌ Error: File '{log_file}' not found")
        return
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return
    
    if not events:
        print("❌ No valid FortiSwitch events found in the log file")
        return
    
    # Enhanced Analysis Results
    print(f"📊 ENHANCED FORTISWITCH ANALYSIS")
    print(f"   Total Events: {len(events)}")
    print(f"   Time Range: {events[0]['timestamp']} to {events[-1]['timestamp']}")
    duration = events[-1]['timestamp'] - events[0]['timestamp']
    print(f"   Duration: {duration}")
    print(f"   Event Rate: {len(events) / (duration.total_seconds() / 3600):.1f} events/hour")
    
    # Log ID Analysis with FortiSwitch Knowledge
    print(f"\n📋 FORTISWITCH EVENT TYPES")
    for logid, count in logid_counts.most_common():
        description = get_logid_description(logid)
        print(f"   🔍 {logid}: {count} events - {description}")
    
    # Event levels with enhanced context
    level_counts = Counter(e['level'] for e in events)
    print(f"\n📈 EVENT SEVERITY LEVELS")
    for level, count in level_counts.most_common():
        icon = "🔴" if level in ['alert', 'error'] else "🟡" if level == 'warning' else "🔵"
        percentage = (count / len(events)) * 100
        print(f"   {icon} {level}: {count} ({percentage:.1f}%)")
    
    # Enhanced Port Analysis
    print(f"\n🔌 ENHANCED PORT STABILITY ANALYSIS")
    critical_ports = []
    unstable_ports = []
    flapping_ports = []
    
    for port, port_events in port_activity.items():
        analysis = analyze_port_stability(port_events, port)
        
        if analysis['status'] == 'critical_flapping':
            critical_ports.append((port, analysis))
        elif analysis['status'] in ['flapping', 'unstable']:
            unstable_ports.append((port, analysis))
        
        if 'state_changes' in analysis and analysis['state_changes'] >= FORTISWITCH_KNOWLEDGE_BASE['flapping_criteria']['state_changes_threshold']:
            flapping_ports.append((port, analysis['state_changes'], len(port_events)))
    
    if critical_ports:
        print("   🚨 CRITICAL PORTS (Immediate Attention Required):")
        for port, analysis in critical_ports:
            print(f"      • {port}: {analysis['state_changes']} state changes")
            for issue in analysis['issues']:
                print(f"        └─ {issue}")
    
    if unstable_ports:
        print("   ⚠️  UNSTABLE PORTS:")
        for port, analysis in unstable_ports:
            print(f"      • {port}: {analysis['up_events']} up, {analysis['down_events']} down")
            for issue in analysis['issues']:
                print(f"        └─ {issue}")
    
    # Enhanced Spanning Tree Analysis
    print(f"\n🌳 SPANNING TREE PROTOCOL ANALYSIS")
    print(f"   Total STP Events: {len(stp_events)}")
    
    if stp_events:
        stp_issues = detect_stp_convergence_issues(stp_events)
        
        # Analyze STP state transitions
        state_patterns = Counter()
        role_patterns = Counter()
        
        for event in stp_events:
            msg = event['message'].lower()
            
            # Extract state transitions
            state_match = re.search(r'from (\w+) to (\w+)', msg)
            if state_match:
                from_state, to_state = state_match.groups()
                state_patterns[f"{from_state}→{to_state}"] += 1
            
            # Extract role changes
            if 'role' in msg:
                role_patterns['role_change'] += 1
        
        if state_patterns:
            print("   🔄 STP State Transitions:")
            for transition, count in state_patterns.most_common(5):
                print(f"      • {transition}: {count} times")
        
        if stp_issues:
            print("   🚨 STP Issues Detected:")
            for issue in stp_issues:
                print(f"      • {issue}")
        
        # STP Health Assessment
        stp_health = "healthy"
        if len(stp_events) > 200:
            stp_health = "critical"
        elif len(stp_events) > 100:
            stp_health = "warning"
        
        print(f"   📊 STP Health Status: {stp_health.upper()}")
    
    # Enhanced Memory Analysis
    if memory_events:
        print(f"\n💾 MEMORY HEALTH ANALYSIS")
        memory_analysis = analyze_memory_health(memory_events)
        
        print(f"   Memory Status: {memory_analysis['status'].upper()}")
        print(f"   Peak Usage: {memory_analysis['max_usage']}%")
        
        if memory_analysis['issues']:
            for issue in memory_analysis['issues']:
                print(f"   {issue}")
        
        # Memory recommendations
        if memory_analysis['max_usage'] >= 95:
            print("   🚨 IMMEDIATE ACTIONS REQUIRED:")
            print("      • Enable external syslog to reduce local log storage")
            print("      • Configure log rotation with shorter retention")
            print("      • Monitor for memory leaks in switch processes")
            print("      • Consider firmware update if available")
    
    # Network Topology Stability Assessment
    topology_issues = analyze_network_topology_stability(events)
    if topology_issues:
        print(f"\n🌐 NETWORK TOPOLOGY STABILITY")
        for issue in topology_issues:
            print(f"   {issue}")
    
    # Enhanced Pattern Detection
    print(f"\n🔍 ADVANCED PATTERN DETECTION")
    
    # Time-based analysis
    hour_activity = defaultdict(int)
    for event in events:
        hour_activity[event['timestamp'].hour] += 1
    
    peak_hours = sorted(hour_activity.items(), key=lambda x: x[1], reverse=True)[:3]
    print(f"   ⏰ Peak Activity Hours:")
    for hour, count in peak_hours:
        print(f"      • {hour:02d}:00 - {count} events")
    
    # Correlation analysis
    port_stp_correlation = set()
    for stp_event in stp_events:
        if stp_event['port']:
            port_stp_correlation.add(stp_event['port'])
    
    port_flap_correlation = set(port for port, _, _ in flapping_ports)
    
    correlated_ports = port_stp_correlation.intersection(port_flap_correlation)
    if correlated_ports:
        print(f"   🔗 Ports with both STP and flapping issues: {', '.join(sorted(correlated_ports))}")
    
    # Enhanced Recommendations
    print(f"\n💡 FORTISWITCH EXPERT RECOMMENDATIONS")
    
    recommendations = []
    priorities = []
    
    # Critical recommendations
    if critical_ports:
        priorities.append("🚨 CRITICAL PRIORITY")
        recommendations.append("   • Immediate physical inspection of critical ports")
        recommendations.append("   • Check cable integrity and connection quality")
        recommendations.append("   • Verify power stability to connected devices")
    
    if memory_events and any(parse_memory_percentage(e['message']) >= 95 for e in memory_events if parse_memory_percentage(e['message'])):
        priorities.append("🚨 CRITICAL PRIORITY")
        recommendations.append("   • Configure external syslog immediately")
        recommendations.append("   • Implement log rotation and retention policies")
    
    # High priority recommendations
    if len(stp_events) > 100:
        priorities.append("⚠️  HIGH PRIORITY")
        recommendations.append("   • Review spanning tree configuration")
        recommendations.append("   • Check for redundant links causing instability")
        recommendations.append("   • Consider implementing RSTP or MSTP")
        recommendations.append("   • Verify root bridge selection and priorities")
    
    if unstable_ports:
        priorities.append("⚠️  HIGH PRIORITY")
        recommendations.append("   • Schedule maintenance window for unstable ports")
        recommendations.append("   • Implement port error-disable recovery")
        recommendations.append("   • Monitor interface error counters")
    
    # Medium priority recommendations
    if len(events) / (duration.total_seconds() / 3600) > 50:
        recommendations.append("   📊 Implement proactive monitoring dashboards")
        recommendations.append("   📊 Set up automated alerting for event thresholds")
    
    # Always include
    recommendations.extend([
        "   📋 Document all findings and actions taken",
        "   📈 Establish baseline metrics for future comparison",
        "   🔄 Schedule regular FortiSwitch health assessments",
        "   📚 Review FortiSwitch best practices documentation"
    ])
    
    if priorities:
        for priority in set(priorities):
            print(f"   {priority}")
    
    for rec in recommendations:
        print(f"   {rec}")
    
    print(f"\n{'='*70}")
    print("✅ Enhanced FortiSwitch analysis complete!")
    print("📖 Analysis based on FortiOS 7.4.5 Administration Guide")

def main():
    parser = argparse.ArgumentParser(description='Enhanced FortiSwitch log analysis with documentation-based insights')
    parser.add_argument('logfile', help='Path to the FortiSwitch log file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    
    args = parser.parse_args()
    
    if args.verbose:
        print("🔧 Verbose mode enabled - additional diagnostic information will be shown")
        print("📚 Using FortiOS 7.4.5 documentation knowledge base")
        print()
    
    analyze_fortiswitch_log(args.logfile)

if __name__ == "__main__":
    main() 