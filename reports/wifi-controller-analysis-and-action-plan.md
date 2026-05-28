# FortiGate WiFi Controller: Full Analysis & Action Plan

**Date:** 2025-06 (updated)
**Context:** FortiGate 1101E (FortiOS 7.4.5) | ~40 FortiAPs | 2x FortiSwitch 1048E Core | ~25 Distribution Switches | FortiAnalyzer
**Role Access:** Limited web UI (WiFi controller section only) — no CLI, no logging, no API tokens
**Sources:** Local docs (`FortiOS-7.4.5-CLI_Reference.md`, `FortiOS-7.4.5-Administration_Guide.md`, release notes), Fortinet official documentation, fortigate-api library

---

## Table of Contents

1. [The Problem Statement](#1-the-problem-statement)
2. [What We Have: Infrastructure Map](#2-what-we-have-infrastructure-map)
3. [What We CAN Do Right Now (Current Access)](#3-what-we-can-do-right-now)
4. [What We CANNOT Do (The Blockers)](#4-what-we-cannot-do)
5. [What to Request: Access Escalation Plan](#5-what-to-request-access-escalation-plan)
6. [Profile Architecture: How FortiGate WiFi Actually Works](#6-profile-architecture)
7. [Per-Zone WiFi Strategy (The Core Solution)](#7-per-zone-wifi-strategy)
8. [Intelligent Features We're Not Using](#8-intelligent-features-were-not-using)
9. [REST API: The Automation Potential](#9-rest-api-the-automation-potential)
10. [RADIUS: The Monitoring Goldmine](#10-radius-the-monitoring-goldmine)
11. [FortiAnalyzer: Stop Collecting, Start Analyzing](#11-fortianalyzer)
12. [Diagnostic Commands We Need CLI For](#12-diagnostic-commands)
13. [Prioritized Action Plan](#13-prioritized-action-plan)
14. [Quick Reference: CLI Commands for WiFi Management](#14-cli-quick-reference)

---

## 1. The Problem Statement

**Current situation:**
- Generic WiFi profiles applied uniformly to all ~40 APs
- No per-zone differentiation (lecture hall vs. office vs. outdoor treated identically)
- No access to CLI diagnostics → cannot see channel utilization, client RSSI, interference
- No access to logging → cannot correlate problems with events
- No API access → cannot automate monitoring or alerting
- FortiAnalyzer collecting logs but nobody analyzing them
- No DARRP, no band steering tuning, no airtime fairness, no DRMA configured
- WiFi performance "sucks" across multiple dimensions but we can't measure which ones
- Main administrator (super_admin) is disengaged / gatekeeping

**The core contradiction:** We have enterprise-grade infrastructure with ~40 APs managed by a FortiGate 1101E, plus FortiAnalyzer. The hardware is capable of intelligent, data-driven WiFi management. We're using approximately 5% of its capabilities because of access restrictions and the absence of differentiated profiles.

---

## 2. What We Have: Infrastructure Map

### Network Topology (from `outputs/connection_diagnostics.txt`)

```
FortiGate 1101E (FortiOS 7.4.5)
    ├── DC-L_CORE-FIB01 (FortiSwitch 1048E) — 17 distribution links (10 Gbps)
    │   ├── Building A switches (A-0-28, A-0-13, A-0-CC, A-2-9, A-0-1)
    │   ├── Building B (B-0-3)
    │   ├── Building C (C-0-6)
    │   ├── Building D (D-0-CTT, D-0-23, D-1-16)
    │   ├── Building E (E-1-6, E-2-3)
    │   ├── Building F (F-2-10, F-3-6, F-3-9)
    │   ├── Building G (G-2-6, G-2-1-1, G-0-2-1)
    │   ├── Building H (via P-1-1 → H-1-5)
    │   ├── Building I (I-0-1)
    │   ├── Building L (L--1-10)
    │   ├── Building M (M-0-1, M-0-3) → T-0-6, Y-1-3, Z-0-2
    │   ├── Building N (N-0-BOF)
    │   ├── Building P (P-1-1)
    │   ├── Building Q (Q-3-2)
    │   ├── Building S (S-0-10) ← X-0-2
    │   ├── Building U (U-0-18, U-3-8)
    │   ├── Building V (V-0-1)
    │   └── PVIAT_SW-DIST
    │
    └── DC-L_CORE-FIB02 (FortiSwitch 1048E) — 5 redundant links (10 Gbps)
        └── Redundant paths to A, C, F, L, V buildings
```

**Known stability issues** (from `reports/fortiswitch_analysis_report.txt`):
- 686 events in 18 hours
- 26 ports showing high instability
- port24 had 76 events (14 up/down cycles)
- 89 STP state changes, 78 STP role changes
- Bug 1081951 in FortiOS 7.4.5 causes continuous memory consumption
- Bug 940248 affects FortiSwitch 1048E with duplicate packets

### What's Documented Locally

| Resource | Location | Content |
|----------|----------|---------|
| FortiOS 7.4.5 CLI Reference | `docs/fortigate/FortiOS-7.4.5-CLI_Reference.md` | 120K+ lines, full wireless-controller CLI tree |
| FortiOS 7.4.5 Admin Guide | `docs/fortigate/FortiOS-7.4.5-Administration_Guide.md` | 191K+ lines, WiFi dashboard, monitoring sections |
| Release Notes (7.4.5 through 7.6.3) | `docs/fortigate/release_notes-versions/` | WiFi bug tracking, new features per version |
| FortiSwitch FortiLink Release Notes | `docs/fortiswitch/` | Compatibility, ISL stability |
| FortiGate 1101E Setup | `reports/fortigate-1101E-setup.md` | Hardware specs, 80 Gbps firewall throughput |
| Core Switch Upgrade Analysis | `reports/fortiswitch_core_upgrade_analysis.md` | Rec. upgrade to 7.4.7, avoid 7.6.x |
| Monitoring & Logging Analysis | `reports/fortiswitch_monitoring_and_logging_analysis.md` | CLI diagnostic commands, log forwarding setup |

**Key gap:** No dedicated WiFi controller / FortiAP configuration guide in local docs. The CLI reference contains all wireless-controller commands but not the strategic how-to. This document fills that gap.

---

## 3. What We CAN Do Right Now

### With current `wifi = read-write` web UI access:

| Action | Can We Do It? | Where in UI |
|--------|---------------|-------------|
| View WiFi Dashboard | ✅ Yes | Dashboard → WiFi |
| View FortiAP Status (online/offline) | ✅ Yes | WiFi & Switch Controller → Managed FortiAPs |
| View client counts per AP | ✅ Yes | Dashboard → WiFi → Clients by FortiAP widget |
| View channel utilization (basic) | ✅ Yes | Dashboard → WiFi → Channel Utilization widget |
| View current SSID configurations | ✅ Yes | WiFi & Switch Controller → SSIDs |
| View current WTP profiles | ✅ Yes | WiFi & Switch Controller → FortiAP Profiles |
| **Create/edit SSIDs (VAPs)** | ✅ Yes | WiFi & Switch Controller → SSIDs |
| **Create/edit WTP profiles** | ✅ Yes | WiFi & Switch Controller → FortiAP Profiles |
| **Change which profile an AP uses** | ✅ Yes | Managed FortiAPs → Edit AP → WTP Profile dropdown |
| **Adjust TX power per radio** | ✅ Yes | FortiAP Profile → Radio 1/2 → Transmit Power |
| **Enable/disable DARRP per radio** | ✅ Yes | FortiAP Profile → Radio 1/2 → DARRP checkbox |
| **Set channel width** | ✅ Yes | FortiAP Profile → Radio 1/2 → Channel Bandwidth |
| **Set max clients per radio** | ✅ Yes | FortiAP Profile → Radio 1/2 → Maximum Clients |
| **Create VAP groups** | ✅ Yes | WiFi & Switch Controller → SSID Groups |
| **Create ARRP profiles** | ✅ Yes | CLI Reference shows this — verify if UI exposes it |
| View login failures | ⚠️ Limited | Dashboard → WiFi widget, but no log drill-down |
| Run any CLI command | ❌ No | No CLI access |
| View logs | ❌ No | No `loggrp` permission |
| Run diagnostics | ❌ No | No `cli-diagnose` permission |
| Access REST API | ❌ No | No API token (requires super_admin to create) |
| Access FortiAnalyzer data | ❌ No | No FortiAnalyzer access |

### Critical realization:

**We CAN create differentiated WTP profiles and assign them per AP through the web UI.** This is the single most impactful action we can take right now without any access escalation. We don't need CLI to create zone-specific profiles — the WiFi & Switch Controller web UI exposes WTP profile creation and AP assignment.

---

## 4. What We CANNOT Do

### The blockers preventing data-driven WiFi management:

| Blocker | What It Prevents | Permission Needed |
|---------|------------------|-------------------|
| **No CLI access** | Cannot run `diagnose wireless-controller wlac -d sta online` to see real-time client details | `cli-diagnose` = enable |
| **No log viewing** | Cannot see WiFi association failures, roaming events, AP disconnects | `loggrp` = read |
| **No API token** | Cannot automate monitoring, pull client data programmatically, build dashboards | `super_admin` to create API user |
| **No CLI show/get** | Cannot export current configuration programmatically | `cli-show` / `cli-get` = enable |
| **No FortiAnalyzer access** | Cannot access historical WiFi analytics, traffic patterns, AP performance over time | Separate FortiAnalyzer account |
| **No SNMP** | Cannot monitor APs via SNMP monitoring tools (Zabbix, PRTG, etc.) | SNMP config (requires system access) |

### What we're flying blind on:

1. **Which APs are overloaded?** — We see client counts on the dashboard but not historical trends
2. **Which channels have interference?** — Dashboard shows basic utilization but we can't run spectrum analysis
3. **Why are clients disconnecting?** — No logs = no root cause analysis
4. **What's the RSSI distribution?** — We can't see signal quality of connected clients
5. **Is roaming working?** — No 802.11r/k/v event logs to verify roaming behavior
6. **What are the peak usage patterns?** — No FortiAnalyzer access for historical trends
7. **Are there rogue APs?** — WIDS requires configuration we can't verify without CLI

---

## 5. What to Request: Access Escalation Plan

### Tier 1: Minimum Viable (Request First)

**Profile name:** `wifi-operator`

```bash
config system accprofile
    edit "wifi-operator"
        set wifi read-write              # Already likely have this
        set loggrp read                  # ← NEW: View logs for troubleshooting
        set ftviewgrp read               # ← NEW: FortiView for WiFi analytics
        set sysgrp none
        set netgrp none
        set fwgrp none
        set vpngrp none
        set utmgrp none
        set secfabgrp none
        set authgrp none
        set wanoptgrp none
        set admintimeout-override enable
        set cli-get enable               # ← NEW: Run get commands
        set cli-show enable              # ← NEW: View configuration
        set cli-diagnose enable          # ← NEW: Run wireless diagnostics
        set cli-exec disable             # Block execute (prevents reboot, etc.)
        set cli-config disable           # Block CLI config changes (GUI only)
    next
end
```

**Justification for each request:**

| Permission | Why We Need It | Risk to Infrastructure |
|------------|----------------|----------------------|
| `loggrp = read` | See WiFi association failures, roaming events, AP disconnects. **READ ONLY** — cannot change log settings | None — read-only |
| `ftviewgrp = read` | FortiView dashboards for historical WiFi analytics | None — read-only |
| `cli-get` | Query current AP state, client lists, radio stats programmatically | None — read-only |
| `cli-show` | Export current configuration for documentation/backup | None — read-only |
| `cli-diagnose` | Run `diagnose wireless-controller` commands — the primary troubleshooting tool | Minimal — diagnostic output only |
| `cli-exec DISABLE` | Explicitly blocked — cannot run `execute` commands | N/A |
| `cli-config DISABLE` | Explicitly blocked — cannot change config via CLI | N/A |

### Tier 2: API Access (Request Second)

**Ask the super_admin to create an API user:**

```bash
config system api-user
    edit "wifi-api-monitor"
        set comments "WiFi monitoring API - read only"
        set accprofile "wifi-operator"     # Uses the profile above
        set vdom "root"
        config trusthost
            edit 1
                set ipv4-trusthost 10.0.0.0/8    # Restrict to internal network
            next
        end
    next
end

execute api-user generate-key wifi-api-monitor
```

**What this unlocks:**
- Automated client monitoring scripts
- Historical data collection (client counts, signal strength, channel utilization)
- Alerting when APs go offline or client counts spike
- Integration with Grafana/dashboards for WiFi visibility

### Tier 3: FortiAnalyzer Read Access (Request Third)

Request a FortiAnalyzer account with:
- Read access to WiFi reports and dashboards
- Ability to view historical WiFi analytics
- Access to FortiView data

### How to Frame the Request (adapted to the gatekeeper dynamic)

> "Can you help me set up a monitoring profile? I need to be able to check the WiFi logs and run some diagnostics from the CLI. I've prepared the exact configuration needed — it's read-only for everything except WiFi, and even CLI config changes are blocked. It would take 2 minutes to set up, and it means I can stop coming to you for basic WiFi troubleshooting."

**Key principles from the gatekeeper navigation strategy:**
1. Pre-digest the request — give the exact CLI commands
2. Frame it as reducing their burden, not increasing your power
3. One request at a time — start with the profile, then the API token
4. Validate their ego — "I know you're busy with X, so I figured this would save you time"

---

## 6. Profile Architecture: How FortiGate WiFi Actually Works

### The Layer Model

```
┌─────────────────────────────────────────────────┐
│  SSID (VAP) — "Campus-Student"                  │  What users see
│  config wireless-controller vap                  │  Security, VLAN, auth
│  ├── ssid, security, dynamic-vlan               │
│  ├── 802.11k, 802.11v, sticky-client settings   │
│  └── atf-weight, max-clients                     │
├─────────────────────────────────────────────────┤
│  VAP Group — "campus-all-ssids"                  │  Groups SSIDs for
│  config wireless-controller vap-group             │  assignment to radios
│  └── set vaps "student" "staff" "iot"            │
├─────────────────────────────────────────────────┤
│  WTP Profile — "FAP431F-high-density"           │  THE KEY LAYER
│  config wireless-controller wtp-profile          │  Radio settings per zone
│  ├── radio-1 (2.4 GHz): power, channel, DARRP   │
│  ├── radio-2 (5 GHz): power, channel, DARRP     │
│  ├── radio-3 (6 GHz): power, channel, DARRP     │
│  ├── band steering, airtime fairness, DRMA       │
│  └── SSID assignment (vap-all or specific)       │
├─────────────────────────────────────────────────┤
│  WTP (per-AP override) — "FP431FTF20012724"     │  Individual AP tweaks
│  config wireless-controller wtp                  │
│  └── radio-1 power-level override                │
└─────────────────────────────────────────────────┘
```

### Where to configure what:

| What you want to change | Where to configure it |
|-------------------------|----------------------|
| SSID name, password, security | **VAP** (`wireless-controller vap`) |
| Per-user VLAN assignment | **VAP** (`dynamic-vlan enable`) |
| 802.11k/v roaming protocols | **VAP** (`80211k`, `80211v`) |
| Sticky client thresholds | **VAP** (`sticky-client-remove`, thresholds) |
| Airtime fairness weight per SSID | **VAP** (`atf-weight`) |
| Transmission power | **WTP Profile → Radio** (`power-level`, `auto-power-level`) |
| Channel selection | **WTP Profile → Radio** (`channel`, `darrp`) |
| Channel width | **WTP Profile → Radio** (`channel-bonding`) |
| Band steering | **WTP Profile** (`handoff-rssi`, `handoff-sta-thresh`) |
| Airtime fairness (enable/disable) | **WTP Profile → Radio** (`airtime-fairness`) |
| DRMA (auto radio mode) | **WTP Profile → Radio** (`drma`, `drma-sensitivity`) |
| Max clients per radio | **WTP Profile → Radio** (`max-clients`) |
| DARRP optimization schedule | **ARRP Profile** (`wireless-controller arrp-profile`) |
| Assign profile to AP | **WTP** (per-AP) (`wtp-profile` field) |
| Per-AP power override | **WTP → Radio** (override profile setting) |

---

## 7. Per-Zone WiFi Strategy

### Current Problem

All ~40 APs are likely using 1–2 generic WTP profiles with default settings. This means:
- An AP in a lecture hall (100+ devices) has the same TX power and max-clients as an AP in a private office (5 devices)
- No DARRP → APs may be on overlapping channels
- No band steering → 2.4 GHz is saturated while 5 GHz is underutilized
- No airtime fairness → one slow client can degrade everyone's experience
- No DRMA → redundant radios in dense areas actively cause interference

### Recommended Zone Profiles

#### Zone A: High-Density (Lecture Halls, Auditoriums, Libraries)

**WTP Profile:** `WTP-HIGH-DENSITY`

```
config wireless-controller wtp-profile
    edit "WTP-HIGH-DENSITY"
        config radio-1                    # 2.4 GHz radio
            set mode ap
            set band 802.11ax-2G
            set channel-bonding 20MHz     # Narrow = less overlap in dense areas
            set darrp enable              # Auto channel selection
            set auto-power-level enable   # Auto TX power
            set auto-power-low 10         # Min 10 dBm
            set auto-power-high 17        # Max 17 dBm (reduced for density)
            set max-clients 50            # Hard cap per radio
            set airtime-fairness enable   # Prevent slow client domination
            set drma enable               # Auto-disable redundant radios
            set drma-sensitivity high     # Aggressive NCF threshold
            set vap-all enable
        end
        config radio-2                    # 5 GHz radio
            set mode ap
            set band 802.11ax-5G
            set channel-bonding 80MHz     # Wide channels for throughput
            set darrp enable
            set auto-power-level enable
            set auto-power-low 10
            set auto-power-high 17
            set max-clients 100
            set airtime-fairness enable
            set drma enable
            set drma-sensitivity high
            set vap-all enable
        end
        set handoff-rssi 25               # Band steering threshold
        set handoff-sta-thresh 10         # Load balancing kicks in at 10 clients
    next
end
```

**Per-SSID settings for high-density:**
```
config wireless-controller vap
    edit "campus-students"
        set ssid "Campus-Students"
        set 80211k enable                 # Neighbor list for smart roaming
        set 80211v enable                 # Active BSS transition
        set sticky-client-remove enable   # Kick sticky clients
        set sticky-client-threshold-5g "-65"  # RSSI threshold
        set atf-weight 20                 # Default airtime weight
    next
end
```

#### Zone B: Medium-Density (Corridors, Common Areas, Cafeterias)

**WTP Profile:** `WTP-MEDIUM-DENSITY`

```
config wireless-controller wtp-profile
    edit "WTP-MEDIUM-DENSITY"
        config radio-1
            set mode ap
            set band 802.11ax-2G
            set channel-bonding 40MHz
            set darrp enable
            set auto-power-level enable
            set auto-power-low 12
            set auto-power-high 17
            set max-clients 60
            set airtime-fairness enable
            set drma enable
            set drma-sensitivity medium
            set vap-all enable
        end
        config radio-2
            set mode ap
            set band 802.11ax-5G
            set channel-bonding 80MHz
            set darrp enable
            set auto-power-level enable
            set auto-power-low 12
            set auto-power-high 17
            set max-clients 80
            set airtime-fairness enable
            set drma enable
            set drma-sensitivity medium
            set vap-all enable
        end
        set handoff-rssi 25
        set handoff-sta-thresh 15
    next
end
```

#### Zone C: Low-Density (Offices, Meeting Rooms, Isolated Areas)

**WTP Profile:** `WTP-LOW-DENSITY`

```
config wireless-controller wtp-profile
    edit "WTP-LOW-DENSITY"
        config radio-1
            set mode ap
            set band 802.11ax-2G
            set channel-bonding 40MHz
            set darrp disable             # Static channels fine in low density
            set power-mode dBm
            set power-level 17            # Fixed power for max coverage
            set vap-all enable
        end
        config radio-2
            set mode ap
            set band 802.11ax-5G
            set channel-bonding 80MHz
            set darrp disable
            set power-mode dBm
            set power-level 17
            set vap-all enable
        end
    next
end
```

#### Zone D: Outdoor

**WTP Profile:** `WTP-OUTDOOR`

```
config wireless-controller wtp-profile
    edit "WTP-OUTDOOR"
        config radio-1
            set mode ap
            set band 802.11ax-2G
            set channel-bonding 20MHz     # Narrow for outdoor interference
            set darrp enable              # DFS-aware channel selection
            set power-mode dBm
            set power-level 20            # Higher power for outdoor
            set max-clients 50
            set vap-all enable
        end
        config radio-2
            set mode ap
            set band 802.11ax-5G
            set channel-bonding 80MHz
            set darrp enable
            set power-mode dBm
            set power-level 20
            set max-clients 50
            set vap-all enable
        end
    next
end
```

### How to Assign Profiles Per AP

**Via Web UI** (we can do this NOW):
1. Go to **WiFi & Switch Controller → Managed FortiAPs**
2. Click on an AP to edit it
3. Change the **WTP Profile** dropdown to the appropriate zone profile
4. Save — the AP will reboot and apply the new profile

**Via CLI** (when we get access):
```bash
config wireless-controller wtp
    edit "FP431FTF20012724"           # AP serial number
        set wtp-profile "WTP-HIGH-DENSITY"
    next
end
```

---

## 8. Intelligent Features We're Not Using

### 8.1 DARRP (Dynamic Automatic Radio Resource Provisioning)

**What it does:** Automatically selects optimal channels based on noise floor, channel load, managed AP count, and spectral RSSI. Runs on a schedule (default: daily).

**Why we need it:** Without DARRP, APs may sit on overlapping channels indefinitely. In a campus with 40 APs, manual channel planning is error-prone and doesn't adapt to changing conditions.

**Evidence** (FortiOS 7.4.5 CLI Reference, line 116313):
```
set darrp [enable|disable]
```

**ARRP Profile tuning:**
```bash
config wireless-controller arrp-profile
    edit "arrp-campus"
        set weight-channel-load 50       # Prioritize low-load channels
        set weight-noise-floor 40        # Avoid noisy channels
        set weight-managed-ap 30         # Spread across channels
        set include-dfs-channel enable   # Use DFS channels (52-144)
    next
end
```

**DARRP optimization schedule:**
```bash
config wireless-controller setting
    set darrp-optimize 86400             # Run every 24 hours
    set darrp-optimize-schedules "darrp-nightly"
end
```

### 8.2 Auto TX Power Control

**What it does:** Automatically adjusts transmission power within configured bounds based on environment.

**Why we need it:** APs blasting at full power in high-density areas causes co-channel interference. APs in offices at full power causes signal bleed into adjacent spaces.

**Evidence** (FortiOS 7.4.5 CLI Reference):
```
config radio-1
    set auto-power-level enable
    set auto-power-low 10               # Minimum dBm
    set auto-power-high 17              # Maximum dBm
end
```

### 8.3 DRMA (Dynamic Radio Mode Assignment)

**What it does:** Calculates Network Coverage Factor (NCF) for each radio. When redundant (coverage overlap), switches radios from AP mode to monitor mode.

**Why we need it:** In high-density areas where 3 APs cover the same space, the redundant 2.4 GHz radios actively cause interference. DRMA automatically silences them.

```bash
config radio-1
    set drma enable
    set drma-sensitivity high           # Aggressive — 90% NCF threshold
end
```

### 8.4 Band Steering (Frequency Handoff)

**What it does:** Withholds 2.4 GHz probe responses from dual-band clients that have strong 5 GHz signal, pushing them to 5 GHz.

**Why we need it:** 2.4 GHz has only 3 non-overlapping channels (1, 6, 11). With 40 APs, 2.4 GHz is guaranteed to be saturated. Band steering moves capable clients to the much wider 5 GHz spectrum.

**Configuration:** `handoff-rssi` (threshold for steering, default 25) and `handoff-sta-thresh` (client count trigger, default 10).

### 8.5 Airtime Fairness

**What it does:** Ensures each client gets a fair share of airtime, preventing distant/slow clients from monopolizing the radio.

**Why we need it:** One client at -85 dBm connecting at 1 Mbps can consume the same airtime as 20 clients at -50 dBm connecting at 300 Mbps. Airtime fairness prevents this.

```bash
config radio-2
    set airtime-fairness enable
end

# Per-SSID weight (VAP level)
config wireless-controller vap
    edit "campus-students"
        set atf-weight 20               # Default weight (1-100)
    next
end
```

### 8.6 802.11k/v Roaming

**What it does:**
- **802.11k** (RRM): AP provides neighbor list → client chooses best AP
- **802.11v** (BSTM): AP actively sends transition requests → pushes client to better AP
- **Sticky client removal**: Kicks clients that refuse to roam off overloaded APs

**Why we need it:** Without 802.11k/v, clients make dumb roaming decisions. They "stick" to the first AP they connected to even when a closer AP is available.

```bash
config wireless-controller vap
    edit "campus-students"
        set 80211k enable
        set 80211v enable
        set sticky-client-remove enable
        set sticky-client-threshold-5g "-65"
    next
end
```

### Summary: What We're Leaving on the Table

| Feature | Status | Impact If Enabled |
|---------|--------|-------------------|
| DARRP | ❌ Not configured | Channels are likely overlapping across 40 APs |
| Auto TX Power | ❌ Not configured | APs blasting full power = massive interference |
| DRMA | ❌ Not configured | Redundant 2.4 GHz radios causing co-channel interference |
| Band Steering | ❌ Not configured | 2.4 GHz overloaded, 5 GHz underutilized |
| Airtime Fairness | ❌ Not configured | Slow clients degrading everyone |
| 802.11k/v | ❌ Unknown | Clients making poor roaming decisions |
| Per-zone profiles | ❌ Single generic profile | All areas treated identically |
| RADIUS accounting | ❌ Not tapped | No user-session visibility |
| REST API monitoring | ❌ No access | No automated alerting or dashboards |
| FortiAnalyzer analysis | ❌ Not analyzed | Logs collected but never reviewed |

---

## 9. REST API: The Automation Potential

### If we get API access, here's what we can build:

### 9.1 Key WiFi Endpoints

| Endpoint | What It Returns |
|----------|----------------|
| `GET /api/v2/cmdb/wireless-controller/vap` | All SSID configurations |
| `GET /api/v2/cmdb/wireless-controller/wtp` | All AP configurations + profile assignments |
| `GET /api/v2/cmdb/wireless-controller/wtp_profile` | All WTP profiles (radio settings) |
| `GET /api/v2/cmdb/wireless-controller/arrp_profile` | DARRP profiles |
| `GET /api/v2/monitor/wifi/client` | **Real-time connected clients** (MAC, IP, RSSI, AP, channel, SNR) |
| `GET /api/v2/monitor/wifi/rogue_ap` | Detected rogue APs |

### 9.2 Monitoring Script Concept

```python
# Concept: WiFi monitoring dashboard data collector
# Requires: API token with wifi = read

import requests

FORTIGATE = "https://10.x.x.x"
TOKEN = "your-api-token"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# Get all connected clients
clients = requests.get(
    f"{FORTIGATE}/api/v2/monitor/wifi/client",
    headers=HEADERS, verify=False
).json()

# Analyze per-AP load
ap_load = {}
for client in clients.get("results", []):
    ap_name = client.get("wtp_name")
    rssi = client.get("rssi")
    ap_load.setdefault(ap_name, []).append({
        "mac": client["mac"],
        "rssi": rssi,
        "channel": client.get("channel"),
        "radio": client.get("radio_id")
    })

# Flag overloaded APs
for ap, clients_list in ap_load.items():
    if len(clients_list) > 50:
        print(f"⚠️  {ap}: {len(clients_list)} clients — OVERLOADED")
    weak_signal = [c for c in clients_list if c["rssi"] < -75]
    if weak_signal:
        print(f"📉 {ap}: {len(weak_signal)} clients with weak signal (<-75 dBm)")
```

### 9.3 What API Access Unlocks

| Automation | Description |
|------------|-------------|
| **Client monitoring** | Track client counts per AP, flag overloaded APs |
| **Signal quality tracking** | Monitor RSSI distribution, identify coverage gaps |
| **AP health monitoring** | Alert when APs go offline or show anomalies |
| **Configuration backup** | Export all WiFi configs programmatically |
| **Profile deployment** | Push updated WTP profiles to APs automatically |
| **Historical trending** | Build time-series data of client counts, signal quality |
| **Rogue AP detection** | Automated alerting when unauthorized APs appear |

---

## 10. RADIUS: The Monitoring Goldmine

### What RADIUS accounting data gives us:

If RADIUS accounting is enabled (and we can access the accounting logs), every WiFi session generates:

| RADIUS Attribute | WiFi Insight |
|-----------------|-------------|
| `User-Name` | Who is connecting |
| `Calling-Station-Id` (MAC) | Which device |
| `Called-Station-Id` (AP:SSID) | Which AP they connected to |
| `Acct-Session-Time` | How long they stayed |
| `Acct-Input-Octets` / `Acct-Output-Octets` | How much data transferred |
| `Acct-Terminate-Cause` | Why they disconnected |
| `NAS-IP-Address` | FortiGate IP |
| `Framed-IP-Address` | Client's assigned IP |

### What we can do with this data:

1. **Identify sticky clients** — Sessions lasting 4+ hours on the same AP
2. **Map user density per building** — Count unique MACs per Called-Station-Id
3. **Detect roaming failures** — Frequent short sessions with same user = poor roaming
4. **Bandwidth analysis** — Which APs/SSIDs consume the most data
5. **Disconnect pattern analysis** — Terminate-Cause reveals auth failures vs. timeouts vs. roaming

### FortiGate RADIUS called-station-id customization (FortiOS 7.6.1+):

```bash
# Customize what appears in RADIUS Access-Request packets
config wireless-controller vap
    edit "campus-students"
        set called-station-id-type {mac | ip | apname}
        # apname = AP name : SSID — most useful for analysis
    next
end
```

---

## 11. FortiAnalyzer: Stop Collecting, Start Analyzing

### Available WiFi reports in FortiAnalyzer:

| Report | What It Shows | Tuning Action |
|--------|---------------|---------------|
| Top APs by Bandwidth | Which APs carry the most load | Split load, adjust max-clients |
| Top SSIDs by Bandwidth | Which SSIDs are busiest | Adjust bandwidth limits |
| Top Rogue APs | Unauthorized APs detected | WIDS suppression |
| Authorized APs | AP inventory and status | Identify offline/problem APs |
| SSIDs Over Time | Historical traffic trends | Capacity planning |

### FortiGate WiFi Dashboard (available NOW via web UI):

| Widget | Location | What to Look For |
|--------|----------|-----------------|
| Clients by FortiAP | Dashboard → WiFi | APs with >50 clients = overloaded |
| Channel Utilization | Dashboard → WiFi | APs at >70% utilization = need DARRP |
| FortiAP Status | Dashboard → WiFi | Offline or degraded APs |
| Signal Strength | Dashboard → WiFi | % of clients below -75 dBm = coverage gaps |
| Login Failures | Dashboard → WiFi | Spikes = auth or interference issues |

### The 8-step tuning process using FortiAnalyzer data:

1. **Identify congested APs** → Top APs by Bandwidth → sort by sessions → flag >150 clients
2. **Detect sticky clients** → FortiView → WiFi Clients → sort by session duration → flag >4 hours
3. **Channel utilization heatmap** → Dashboard WiFi → identify >70% consistently
4. **Rogue AP analysis** → Top Rogue APs → determine co-channel vs. external threat
5. **SSID traffic patterns** → SSIDs Over Time → identify peak hours per SSID
6. **Login failure patterns** → Dashboard WiFi → correlate with specific APs/times
7. **RSSI distribution** → Signal Strength → flag high % below -75 dBm
8. **AI Insights** (if FortiAIOps available) → automated root cause analysis

---

## 12. Diagnostic Commands We Need CLI For

### The commands that would immediately help:

```bash
# 1. See all online clients with full details
diagnose wireless-controller wlac -d sta online

# 2. Filter clients by specific AP
diagnose wireless-controller wlac sta_filter <mac-address> 1

# 3. Check AP connection status
diagnose wireless-controller get-conn-status

# 4. View radio statistics per AP
diagnose wireless-controller wlac -d wtp

# 5. See DARRP optimization status
diagnose wireless-controller wlac darrp

# 6. View client association/reassociation events
diagnose wireless-controller wlac -d sta

# 7. Check radio resource information
diagnose wireless-controller wlac -d rrm

# 8. View FortiAP-to-controller connection details
diagnose wireless-controller wlac -d cdb [wtp-name]
```

**Source:** FortiOS 7.4.5 Administration Guide, lines 189439-189448:
```
FG600B3909600253   # diagnose  wireless-controller wlac -d sta
FG600B3909600253   # diagnose  wireless-controller wlac sta_filter 00:25:9c:e0:47:88     1
```

**All of these require `cli-diagnose = enable` in the admin profile.**

---

## 13. Prioritized Action Plan

### Phase 0: What We Can Do NOW (No access escalation needed)

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 1 | **Audit current WTP profiles** — count how many exist, what they configure | 15 min | Baseline understanding |
| 2 | **Map AP locations to zones** — create a spreadsheet: AP name → building → zone type | 1-2 hours | Foundation for profiling |
| 3 | **Create `WTP-HIGH-DENSITY` profile** — apply to lecture hall / auditorium APs | 30 min | Highest impact single change |
| 4 | **Create `WTP-MEDIUM-DENSITY` profile** — apply to corridor / common area APs | 30 min | Second highest impact |
| 5 | **Create `WTP-LOW-DENSITY` profile** — apply to office / isolated APs | 30 min | Completes zone coverage |
| 6 | **Enable DARRP on all profiles** — except low-density static channels | 10 min | Eliminates channel overlap |
| 7 | **Enable auto TX power on dense profiles** — set 10-17 dBm bounds | 10 min | Reduces interference |
| 8 | **Enable airtime fairness on dense profiles** | 5 min | Prevents slow client domination |
| 9 | **Set max-clients per radio** on dense profiles (50-100) | 5 min | Prevents AP saturation |
| 10 | **Monitor WiFi Dashboard daily** for a week — note problem areas | Ongoing | Data to justify access requests |

### Phase 1: Access Escalation (Request from admin)

| # | Action | Depends On |
|---|--------|-----------|
| 11 | Request `wifi-operator` admin profile with `loggrp=read`, `cli-diagnose=enable`, `cli-get=enable`, `cli-show=enable` | Admin cooperation |
| 12 | Start running diagnostic commands daily — build a baseline | #11 |
| 13 | Review FortiAnalyzer WiFi reports | #11 + FA access |
| 14 | Export current full config via CLI for documentation | #11 |

### Phase 2: API & Automation (Request API token)

| # | Action | Depends On |
|---|--------|-----------|
| 15 | Request API user creation with `wifi-operator` profile | #11 |
| 16 | Build WiFi monitoring script (client counts, RSSI, AP health) | #15 |
| 17 | Set up automated alerting (AP offline, client spikes, weak signal) | #16 |
| 18 | Build historical trending (Grafana/dashboard integration) | #16 |
| 19 | Create API-driven config deployment scripts | #16 |

### Phase 3: Advanced Features (With full visibility)

| # | Action | Depends On |
|---|--------|-----------|
| 20 | Tune ARRP profiles based on collected data | Phase 1 diagnostics |
| 21 | Enable DRMA on high-density profiles | Data confirming redundancy |
| 22 | Enable 802.11k/v on all SSIDs | Phase 1 baseline |
| 23 | Configure RADIUS accounting for session visibility | RADIUS server access |
| 24 | Implement RADIUS-based dynamic VLAN assignment | RADIUS + VLAN planning |
| 25 | Set up FortiAIOps integration (if licensed) | FortiCloud account |

---

## 14. Quick Reference: CLI Commands for WiFi Management

### Configuration Commands

```bash
# View all SSIDs
show wireless-controller vap

# View all WTP profiles
show wireless-controller wtp-profile

# View all APs and their profile assignments
show wireless-controller wtp

# View global WiFi settings
show wireless-controller setting
show wireless-controller global

# View DARRP schedules
show wireless-controller timers

# Create new WTP profile
config wireless-controller wtp-profile
    edit "WTP-HIGH-DENSITY"
        config radio-1
            set band 802.11ax-2G
            set darrp enable
            set auto-power-level enable
            set auto-power-low 10
            set auto-power-high 17
            set max-clients 50
            set airtime-fairness enable
            set drma enable
            set drma-sensitivity high
        end
        config radio-2
            set band 802.11ax-5G
            set channel-bonding 80MHz
            set darrp enable
            set auto-power-level enable
            set max-clients 100
            set airtime-fairness enable
        end
        set handoff-rssi 25
        set handoff-sta-thresh 10
    next
end

# Assign profile to AP
config wireless-controller wtp
    edit "AP-SERIAL-NUMBER"
        set wtp-profile "WTP-HIGH-DENSITY"
    next
end

# Enable 802.11k/v on SSID
config wireless-controller vap
    edit "campus-students"
        set 80211k enable
        set 80211v enable
        set sticky-client-remove enable
        set sticky-client-threshold-5g "-65"
    next
end

# Create ARRP profile
config wireless-controller arrp-profile
    edit "arrp-campus"
        set weight-channel-load 50
        set weight-noise-floor 40
        set include-dfs-channel enable
    next
end
```

### Diagnostic Commands (need cli-diagnose)

```bash
# All online clients
diagnose wireless-controller wlac -d sta online

# AP connection status
diagnose wireless-controller get-conn-status

# DARRP status
diagnose wireless-controller wlac darrp

# Radio resource info
diagnose wireless-controller wlac -d rrm

# WTP details
diagnose wireless-controller wlac -d wtp

# Filter specific client
diagnose wireless-controller wlac sta_filter <mac> 1
```

---

## Appendix A: Known Bugs Affecting Our Setup

| Bug ID | Version | Impact | Fixed In |
|--------|---------|--------|----------|
| 1081951 | 7.4.5 | Continuous memory consumption on FortiGate | 7.4.6+ |
| 940248 | All | Duplicate packets on FortiSwitch 1048E | Not fixed (workaround: disable network-monitor-mode) |
| 1062730 | 7.4.6-7.6.x | max-clients doesn't enforce properly | Not fixed as of 7.6.3 |
| 976646 | 7.4.3-7.4.4 | Captive portal separated from security modes | 7.4.4+ (config migration needed) |

**Source:** Local release notes in `docs/fortigate/release_notes-versions/`

## Appendix B: Recommended Firmware Path

- **FortiGate**: 7.4.5 → **7.4.7** (stable, mature, fixes memory bug)
- **FortiSwitch 1048E**: 7.4.4 → **7.4.7** (fixes CPU/memory bugs, avoid 7.6.x due to bug 940248)
- **FortiAP**: Check compatibility with FortiOS 7.4.7 before upgrade

**Source:** `reports/fortiswitch_core_upgrade_analysis.md`, `private/email_para_joao.md`

## Appendix C: REST API Endpoint Quick Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v2/cmdb/wireless-controller/vap` | List all SSIDs |
| GET | `/api/v2/cmdb/wireless-controller/wtp` | List all APs |
| GET | `/api/v2/cmdb/wireless-controller/wtp_profile` | List all WTP profiles |
| GET | `/api/v2/cmdb/wireless-controller/arrp_profile` | List ARRP profiles |
| GET | `/api/v2/cmdb/wireless-controller/global` | Global WiFi settings |
| GET | `/api/v2/cmdb/wireless-controller/setting` | WiFi controller settings |
| GET | `/api/v2/monitor/wifi/client` | Real-time client list |
| GET | `/api/v2/monitor/wifi/rogue_ap` | Rogue AP detection |
| GET | `/api/v2/monitor/wifi/spectrum` | Spectrum analysis |
| PUT | `/api/v2/cmdb/wireless-controller/wtp_profile/{name}` | Update WTP profile |
| PUT | `/api/v2/cmdb/wireless-controller/wtp/{serial}` | Update AP config |
| POST | `/api/v2/cmdb/wireless-controller/vap` | Create new SSID |

---

*Document generated from: FortiOS 7.4.5 CLI Reference, FortiOS 7.4.5 Administration Guide, Fortinet official documentation (docs.fortinet.com), fortigate-api library, FortiAP Configuration Guides 7.4/7.6, FortiAnalyzer Administration Guide 7.4, local project documentation.*
