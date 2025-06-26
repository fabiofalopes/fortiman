#!/usr/bin/env python3
"""
FortiSwitch Log Analyzer
Analyzes FortiSwitch controller logs to identify patterns and create visualizations
"""

import re
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import seaborn as sns
from collections import defaultdict, Counter
import argparse
import sys

class FortiSwitchLogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.events = []
        self.parsed_data = None
        
    def parse_log_line(self, line):
        """Parse a single log line and extract structured data"""
        # Regex pattern to match FortiSwitch log format
        pattern = r'date=(\S+)\s+time=(\S+).*?logid="(\S+)".*?subtype="(\S+)".*?level="(\S+)".*?logdesc="([^"]*)".*?sn="([^"]*)"(?:.*?switchphysicalport="([^"]*)")?(?:.*?action="([^"]*)")?(?:.*?status="([^"]*)")?(?:.*?eventtype="([^"]*)")?(?:.*?msg="([^"]*)")?'
        
        match = re.search(pattern, line)
        if match:
            date_str, time_str, logid, subtype, level, logdesc, serial_number, port, action, status, eventtype, message = match.groups()
            
            # Combine date and time
            datetime_str = f"{date_str} {time_str}"
            try:
                timestamp = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                return None
                
            return {
                'timestamp': timestamp,
                'logid': logid,
                'subtype': subtype,
                'level': level,
                'description': logdesc,
                'serial_number': serial_number,
                'port': port,
                'action': action,
                'status': status,
                'eventtype': eventtype,
                'message': message,
                'raw_line': line.strip()
            }
        return None
    
    def parse_log_file(self):
        """Parse the entire log file"""
        print(f"Parsing log file: {self.log_file}")
        
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            with open(self.log_file, 'r', encoding='latin-1') as f:
                lines = f.readlines()
        
        for line_num, line in enumerate(lines, 1):
            parsed = self.parse_log_line(line)
            if parsed:
                self.events.append(parsed)
            elif line.strip():  # Only report non-empty lines that failed to parse
                print(f"Warning: Could not parse line {line_num}: {line.strip()[:100]}...")
        
        if self.events:
            self.parsed_data = pd.DataFrame(self.events)
            self.parsed_data = self.parsed_data.sort_values('timestamp')
            print(f"Successfully parsed {len(self.events)} events")
        else:
            print("No events could be parsed from the log file")
            sys.exit(1)
    
    def analyze_port_activity(self):
        """Analyze port up/down activity"""
        port_events = self.parsed_data[self.parsed_data['port'].notna()]
        
        # Count events per port
        port_counts = port_events['port'].value_counts()
        
        # Count up/down events
        port_status_events = port_events[port_events['action'].isin(['port-up', 'port-down'])]
        port_status_counts = port_status_events.groupby(['port', 'action']).size().unstack(fill_value=0)
        
        return port_counts, port_status_counts
    
    def analyze_spanning_tree_events(self):
        """Analyze spanning tree state changes"""
        stp_events = self.parsed_data[self.parsed_data['description'] == 'FortiSwitch spanning Tree']
        
        if stp_events.empty:
            return None, None
        
        # State changes
        state_changes = stp_events[stp_events['eventtype'] == 'state migration']
        state_summary = state_changes.groupby(['port', 'message']).size().reset_index(name='count')
        
        # Role changes
        role_changes = stp_events[stp_events['eventtype'] == 'role migration']
        role_summary = role_changes.groupby(['port', 'message']).size().reset_index(name='count')
        
        return state_summary, role_summary
    
    def identify_unstable_ports(self, threshold=10):
        """Identify ports with excessive activity"""
        port_counts, _ = self.analyze_port_activity()
        unstable_ports = port_counts[port_counts > threshold]
        return unstable_ports
    
    def create_timeline_visualization(self):
        """Create timeline visualization of events"""
        fig, axes = plt.subplots(3, 1, figsize=(15, 12))
        
        # Port activity timeline
        port_events = self.parsed_data[self.parsed_data['action'].isin(['port-up', 'port-down'])]
        if not port_events.empty:
            for port in port_events['port'].unique()[:10]:  # Limit to top 10 for readability
                port_data = port_events[port_events['port'] == port]
                up_events = port_data[port_data['action'] == 'port-up']
                down_events = port_data[port_data['action'] == 'port-down']
                
                axes[0].scatter(up_events['timestamp'], [port] * len(up_events), 
                              c='green', marker='^', s=50, alpha=0.7, label='Port Up' if port == port_events['port'].iloc[0] else "")
                axes[0].scatter(down_events['timestamp'], [port] * len(down_events), 
                              c='red', marker='v', s=50, alpha=0.7, label='Port Down' if port == port_events['port'].iloc[0] else "")
        
        axes[0].set_title('Port Up/Down Events Timeline')
        axes[0].set_ylabel('Port')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Event level distribution over time
        event_levels = self.parsed_data.groupby([self.parsed_data['timestamp'].dt.floor('H'), 'level']).size().unstack(fill_value=0)
        if not event_levels.empty:
            event_levels.plot(kind='bar', stacked=True, ax=axes[1])
            axes[1].set_title('Event Levels Over Time (Hourly)')
            axes[1].set_ylabel('Event Count')
            axes[1].tick_params(axis='x', rotation=45)
        
        # STP events timeline
        stp_events = self.parsed_data[self.parsed_data['description'] == 'FortiSwitch spanning Tree']
        if not stp_events.empty:
            stp_hourly = stp_events.groupby(stp_events['timestamp'].dt.floor('H')).size()
            stp_hourly.plot(kind='line', ax=axes[2], marker='o')
            axes[2].set_title('Spanning Tree Events Over Time')
            axes[2].set_ylabel('STP Events per Hour')
            axes[2].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('fortiswitch_timeline.png', dpi=300, bbox_inches='tight')
        print("Timeline visualization saved as 'fortiswitch_timeline.png'")
        return fig
    
    def create_port_analysis_charts(self):
        """Create port analysis charts"""
        port_counts, port_status_counts = self.analyze_port_activity()
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Top ports by activity
        top_ports = port_counts.head(15)
        top_ports.plot(kind='bar', ax=axes[0,0])
        axes[0,0].set_title('Top 15 Ports by Event Count')
        axes[0,0].set_ylabel('Event Count')
        axes[0,0].tick_params(axis='x', rotation=45)
        
        # Port up/down comparison
        if not port_status_counts.empty:
            port_status_counts.head(10).plot(kind='bar', ax=axes[0,1])
            axes[0,1].set_title('Port Up/Down Events (Top 10 Ports)')
            axes[0,1].set_ylabel('Event Count')
            axes[0,1].legend(['Port Down', 'Port Up'])
            axes[0,1].tick_params(axis='x', rotation=45)
        
        # Event type distribution
        event_types = self.parsed_data['action'].value_counts().head(10)
        event_types.plot(kind='pie', ax=axes[1,0], autopct='%1.1f%%')
        axes[1,0].set_title('Event Type Distribution')
        
        # Log level distribution
        log_levels = self.parsed_data['level'].value_counts()
        log_levels.plot(kind='pie', ax=axes[1,1], autopct='%1.1f%%')
        axes[1,1].set_title('Log Level Distribution')
        
        plt.tight_layout()
        plt.savefig('fortiswitch_port_analysis.png', dpi=300, bbox_inches='tight')
        print("Port analysis charts saved as 'fortiswitch_port_analysis.png'")
        return fig
    
    def generate_summary_report(self):
        """Generate a text summary report"""
        report = []
        report.append("="*60)
        report.append("FORTISWITCH LOG ANALYSIS SUMMARY")
        report.append("="*60)
        
        # Basic statistics
        report.append(f"\nBasic Statistics:")
        report.append(f"- Total events: {len(self.parsed_data)}")
        report.append(f"- Time range: {self.parsed_data['timestamp'].min()} to {self.parsed_data['timestamp'].max()}")
        report.append(f"- Duration: {self.parsed_data['timestamp'].max() - self.parsed_data['timestamp'].min()}")
        
        # Event levels
        level_counts = self.parsed_data['level'].value_counts()
        report.append(f"\nEvent Levels:")
        for level, count in level_counts.items():
            report.append(f"- {level}: {count}")
        
        # Port activity
        port_counts, port_status_counts = self.analyze_port_activity()
        unstable_ports = self.identify_unstable_ports()
        
        report.append(f"\nPort Activity:")
        report.append(f"- Unique ports with events: {len(port_counts)}")
        report.append(f"- Ports with >10 events (potentially unstable): {len(unstable_ports)}")
        
        if len(unstable_ports) > 0:
            report.append(f"\nMost Active Ports:")
            for port, count in unstable_ports.head(10).items():
                report.append(f"- {port}: {count} events")
        
        # STP analysis
        state_summary, role_summary = self.analyze_spanning_tree_events()
        if state_summary is not None:
            report.append(f"\nSpanning Tree Activity:")
            report.append(f"- Total STP state changes: {len(state_summary)}")
            report.append(f"- Total STP role changes: {len(role_summary)}")
        
        # Common messages
        common_messages = self.parsed_data['message'].value_counts().head(5)
        report.append(f"\nMost Common Messages:")
        for msg, count in common_messages.items():
            if msg:
                report.append(f"- {msg[:60]}{'...' if len(msg) > 60 else ''}: {count}")
        
        # Recommendations
        report.append(f"\nRecommendations:")
        if len(unstable_ports) > 0:
            report.append("- CRITICAL: Multiple ports showing high activity - possible network instability")
            report.append("- Check physical connections for ports with high down/up cycles")
            report.append("- Review spanning tree configuration for optimal network topology")
        
        if 'warning' in level_counts or 'alert' in level_counts:
            report.append("- WARNING: Alert/warning events detected - immediate attention required")
        
        report.append("- Monitor memory usage - log indicates memory event log filling up")
        report.append("- Consider adjusting STP timers if topology changes are frequent")
        
        report_text = "\n".join(report)
        
        # Save to file
        with open('fortiswitch_analysis_report.txt', 'w') as f:
            f.write(report_text)
        
        print(report_text)
        print(f"\nDetailed report saved as 'fortiswitch_analysis_report.txt'")
        
        return report_text

def main():
    parser = argparse.ArgumentParser(description='Analyze FortiSwitch controller logs')
    parser.add_argument('logfile', help='Path to the FortiSwitch log file')
    parser.add_argument('--no-plots', action='store_true', help='Skip generating plots')
    
    args = parser.parse_args()
    
    # Initialize analyzer
    analyzer = FortiSwitchLogAnalyzer(args.logfile)
    
    # Parse the log file
    analyzer.parse_log_file()
    
    # Generate summary report
    analyzer.generate_summary_report()
    
    # Create visualizations unless disabled
    if not args.no_plots:
        try:
            analyzer.create_timeline_visualization()
            analyzer.create_port_analysis_charts()
            plt.show()
        except Exception as e:
            print(f"Error creating plots: {e}")
            print("You may need to install matplotlib and seaborn: pip install matplotlib seaborn")

if __name__ == "__main__":
    main() 