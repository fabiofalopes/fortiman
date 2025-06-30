# FortiSwitch Monitoring and Logging Analysis

This document outlines the investigation into retrieving logs and hardware metrics from FortiSwitch devices, specifically the FS-648F model, managed by a FortiGate.

## Objective

To identify methods for extracting comprehensive logs and sensor data (e.g., temperature, fan speed) from a FortiSwitch in a structured format for analysis. This is prompted by a specific issue of a FortiSwitch FS-648F unit's fans running at high speed for unknown reasons.

## Environment

-   **FortiGate:** FortiOS 7.4.5
-   **FortiSwitch:** FS-648F running FortiSwitchOS 7.4.7

## Investigation Log

*This section will be updated as we discover more information.*

---

### Summary of Findings

This investigation has identified the key methods for retrieving hardware sensor data and system logs from a FortiSwitch managed by a FortiGate. The primary method for executing arbitrary diagnostic commands on one or all managed switches is via the FortiGate CLI.

### 1. Accessing Hardware Sensor Data (Temperature, Fans)

The most direct way to investigate the fan issue on the `FS-648F` is to query its hardware sensors directly. This can be done from the managing FortiGate without needing to log into the switch.

The recommended approach is to use the `custom-command` feature on the FortiGate. This allows you to define and run any native FortiSwitch diagnostic command across all connected switches.

**Steps to configure and run custom commands on the FortiGate:**

**Step 1: Define the Custom Commands**

You need to configure the specific FortiSwitch commands you want to run. For your case, the most relevant commands are `diagnose sys fan status` and `diagnose sys pcb temp`.

```bash
# Connect to the FortiGate CLI
config switch-controller custom-command
    edit "get-fan-status"
        set command "diagnose sys fan status"
    next
    edit "get-temp-status"
        set command "diagnose sys pcb temp"
    next
end
```

**Step 2: Execute the Custom Commands**

Once defined, you can execute these commands. The output will be displayed directly on the FortiGate console, showing results from each managed switch.

```bash
# Execute the command to see fan status from all switches
execute switch-controller custom-command get-fan-status

# Execute the command to see temperature from all switches
execute switch-controller custom-command get-temp-status
```

**Relevant FortiSwitch Commands for Hardware Diagnostics:**

*   `diagnose sys fan status`: Shows the status of the fans. This is the most direct command for the reported issue.
*   `diagnose sys pcb temp`: Shows the temperature of the main printed circuit board.
*   `diagnose sys soc temp`: Shows the "System on a Chip" temperature.
*   `diagnose sys psu status`: Shows the status of the power supply units.
*   `diagnose switch physical-ports port-stats`: Provides detailed statistics for ports, which could indicate excessive traffic causing high load and heat.

### 2. Retrieving and Structuring Logs

For ongoing analysis and to get a broader view of the switch's behavior, you should configure the switch to forward its logs to the FortiGate. From the FortiGate, these logs can then be sent to a syslog server or a FortiAnalyzer, which provides the structured format you need for ingestion and analysis.

**Step 1: Enable Log Forwarding on the Managed Switch**

From the FortiGate CLI, you can configure the logging behavior for each managed switch. You can enable `local-override` to create specific settings for the problematic switch.

```bash
# Connect to the FortiGate CLI
config switch-controller managed-switch
    # Replace SXXXXXXXXXXXXXXX with the serial number of your FS-648F
    edit <your-switch-serial-number>
        config switch-log
            # Enable override of global settings
            set local-override enable
            # Set the minimum severity of logs to forward.
            # 'information' or 'debug' will be most verbose.
            set severity information
        end
    next
end
```

**Step 2: Configure FortiGate to Forward Logs to a Syslog Server**

Once the FortiSwitch logs are being sent to the FortiGate's event log, you can configure the FortiGate to forward all its logs (including the switch logs) to an external syslog server.

This is done in the FortiGate UI under **Log & Report > Log Settings** or via the CLI:

```bash
config log syslogd setting
    set status enable
    set server "your.syslog.server.ip"
    set port 514
end
```

This setup provides a continuous, structured stream of log data that can be ingested into any log analysis platform.

### 3. Required Permissions

To perform all the actions described above, you will need:

*   **Administrator access (super_admin)** to the managing FortiGate unit. This is required to run `config` and `execute` commands.
*   Network access from the FortiGate to any external syslog server you wish to use.

This approach provides both immediate diagnostic capabilities for the fan issue and a robust, long-term solution for structured log collection and analysis.

### 4. Environmental Specifications and Sensor Behavior

Understanding the switch's intended operating environment is crucial for interpreting sensor data. The issue with the fans constantly running at high speed could be due to a high ambient temperature in the data closet.

**Optimal Environment:**

Based on the `FS-624F/648F-Series-QSG-llm.md` document, the official environmental specification for this switch series is:

*   **Ambient Operating Temperature:** 0°C to 45°C (32°F to 113°F)

You should ensure the environment where the switch is located is consistently within this range. The `diagnose sys pcb temp` command will provide the internal temperature reading, which should be compared against this specification.

**How the Hardware Sensors Work:**

The switch has dedicated hardware sensors that monitor its internal state. These sensors are tied to the physical LEDs on the front of the unit and the log messages you can collect.

*   **Temperature Sensors:** The switch contains multiple temperature sensors (e.g., on the main PCB and the SoC). If these sensors detect a temperature approaching the upper limit of the operating range, the system will automatically increase fan speed to try and cool the unit down. If the temperature exceeds the safe threshold, it will trigger an alarm state.
*   **Fan Sensors:** The fans themselves are monitored. A fan alarm can be triggered by two primary conditions:
    1.  A fan has mechanically failed or is not reporting its speed correctly.
    2.  The system has commanded the fans to run at maximum speed due to a high temperature reading, which is also considered an alarm-level event.
*   **ALARM and FAN LEDs:** The LEDs on the front of the switch provide a quick visual indicator of sensor status:
    *   **FAN LED:** An `Amber` light indicates a fan alarm, which correlates directly with the fan issue you are observing. `Green` means the fans are operating normally.
    *   **ALARM LED:** A general `Amber` light indicates that some alarm has been detected on the system, which could be related to temperature, fans, power, or another system fault.

By combining the CLI output from the `diagnose` commands with these official specifications, you can determine if the high fan speed is a legitimate response to a hot environment or a potential hardware fault with the switch itself. 