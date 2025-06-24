# FortiSwitch Log Analysis Tools

## 🔍 What's happening in your log?

Your FortiSwitch log shows **significant network instability** with multiple concerning patterns:

### 🚨 Critical Issues Identified

1. **Port Flapping**: Multiple ports (especially port24, port36, port29) are rapidly going up and down
2. **High STP Activity**: 455 spanning tree events indicating topology instability
3. **Memory Issues**: Switch memory event log is 95% full
4. **Network Instability**: 26 ports showing excessive activity over 18 hours

### 📊 Key Statistics

- **686 total events** in 18 hours (very high for a stable network)
- **26 ports** with potentially unstable behavior
- **455 spanning tree events** (sign of topology issues)
- **95 port down events** vs **102 port up events** (concerning churn)

### 🔍 Pattern Analysis

- **Peak activity**: 547 events in just one hour at 18:00
- **Most affected ports**: port24 (CRITICAL), port36, port29
- **STP instability**: Excessive role and state changes
- **Memory crisis**: 95% memory usage approaching critical threshold

## 🛠️ Enhanced Analysis Tools

### 1. **Enhanced Quick Analysis** (`quick_log_analysis.py`)
**NEW:** Now includes FortiOS 7.4.5 documentation-based analysis!

```bash
# Quick enhanced analysis (no dependencies required)
python quick_log_analysis.py memory-event-switch-controller-2025_06_06.log

# With verbose diagnostic output
python quick_log_analysis.py memory-event-switch-controller-2025_06_06.log --verbose
```

**Enhanced Features:**
- 📚 **FortiOS Documentation Integration**: Based on FortiOS 7.4.5 Administration Guide
- 🔍 **FortiSwitch Log ID Knowledge**: Recognizes specific event types
- 🌳 **Advanced STP Analysis**: Detailed spanning tree convergence analysis
- 💾 **Memory Health Assessment**: FortiSwitch-specific memory thresholds
- ⚡ **Intelligent Port Flapping Detection**: Sophisticated stability analysis
- 🔗 **Correlation Analysis**: Identifies ports with multiple issues
- 📊 **Expert Recommendations**: Prioritized action items based on severity

### 2. **Full Analysis with Visualizations** (`fortiswitch_log_analyzer.py`)

```bash
# Full analysis with charts
python fortiswitch_log_analyzer.py memory-event-switch-controller-2025_06_06.log

# Analysis without generating plots (faster)
python fortiswitch_log_analyzer.py memory-event-switch-controller-2025_06_06.log --no-plots
```

## 📊 Enhanced Analysis Output

The enhanced quick analysis now provides:

### 📋 FortiSwitch Event Types
- **Log ID Recognition**: Identifies FortiSwitch-specific event types
- **Event Distribution**: Shows which types of events are most common
- **Severity Analysis**: Breaks down events by priority level

### 🔌 Enhanced Port Stability Analysis
- **Critical Ports**: Immediate attention required (>20 state changes)
- **Unstable Ports**: Showing flapping or rapid state changes
- **Port Health Status**: Categorized as stable, unstable, flapping, or critical

### 🌳 Spanning Tree Protocol Analysis
- **STP Health Status**: Overall topology stability assessment
- **State Transitions**: Detailed analysis of STP state changes
- **Convergence Issues**: Identifies excessive activity patterns
- **Role Changes**: Tracks STP role instabilities

### 💾 Memory Health Analysis
- **Memory Status**: Based on FortiSwitch-specific thresholds
- **Peak Usage Tracking**: Identifies maximum memory consumption
- **Immediate Actions**: Specific recommendations for memory issues

### 🔍 Advanced Pattern Detection
- **Time-based Analysis**: Peak activity hours identification
- **Correlation Analysis**: Ports with multiple types of issues
- **Network Topology Stability**: Overall network health assessment

### 💡 Expert Recommendations
- **Priority-based Actions**: Critical, high, and medium priority tasks
- **FortiSwitch Best Practices**: Based on official documentation
- **Specific Technical Actions**: Detailed implementation guidance

## 📈 Sample Enhanced Output

```
🚨 CRITICAL PORTS (Immediate Attention Required):
   • port24: 21 state changes
     └─ 🚨 CRITICAL FLAPPING: 21 state changes

🌳 SPANNING TREE PROTOCOL ANALYSIS
   Total STP Events: 455
   🔄 STP State Transitions:
      • disabled→designated: 136 times
      • discarding→forwarding: 114 times
   📊 STP Health Status: CRITICAL

💾 MEMORY HEALTH ANALYSIS
   Memory Status: WARNING
   Peak Usage: 95%
   💾 CRITICAL - Memory usage at dangerous levels (95%)

💡 FORTISWITCH EXPERT RECOMMENDATIONS
   🚨 CRITICAL PRIORITY
   • Immediate physical inspection of critical ports
   • Configure external syslog immediately
   ⚠️  HIGH PRIORITY
   • Review spanning tree configuration
   • Consider implementing RSTP or MSTP
```

## 🎯 What This Analysis Tells You

### 🚨 **IMMEDIATE ACTION REQUIRED**

1. **Port24 is CRITICAL** - 21 state changes indicating severe instability
2. **Memory at 95%** - **IMMEDIATE ACTION REQUIRED**
3. **STP topology is unstable** - 455 events indicate serious network issues

### 📋 **Priority Actions**

1. **Immediate**: Physical inspection of port24, enable external syslog
2. **Short-term**: Review STP configuration, implement memory management
3. **Medium-term**: Review and optimize spanning tree configuration

## 📁 Generated Files

Both tools generate detailed reports:
- `fortiswitch_analysis_report.txt` - Detailed text report
- `fortiswitch_timeline.png` - Event timeline visualization
- `fortiswitch_port_analysis.png` - Port activity charts
- `fortiswitch_stp_analysis.png` - STP state transitions

## 🚀 Quick Start

```bash
# Install dependencies (only needed for full analysis with charts)
pip install pandas matplotlib seaborn

# Run enhanced quick analysis (recommended first step)
python quick_log_analysis.py your-log-file.log

# Run full analysis with visualizations
python fortiswitch_log_analyzer.py your-log-file.log

# For systems without display (servers)
python fortiswitch_log_analyzer.py your-log-file.log --no-plots
```

## 🆘 When to Seek Help

Contact your network administrator or FortiSwitch support if:
- Memory usage stays above 90% after implementing recommendations
- Critical port flapping continues after physical inspection
- STP events exceed 100 per hour consistently
- More than 5 ports show critical flapping simultaneously
- Memory issues persist after log management

## 📚 Documentation Reference

This analysis is based on:
- **FortiOS 7.4.5 Administration Guide**
- **FortiOS 7.4.5 CLI Reference**
- **FortiSwitch Best Practices**

The enhanced analysis incorporates official Fortinet documentation to provide expert-level insights and recommendations specific to FortiSwitch operations. 