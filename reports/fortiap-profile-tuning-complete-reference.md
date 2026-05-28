# FortiAP Campus Deployment: The Complete Tuning & Survival Reference

**Context:** FortiGate 1101E (FortiOS 7.4.5) | ~40 FortiAPs | Campus spanning buildings A-V | 2 people with near-zero operational visibility | APs placed by gut feeling with no measurements | No CLI, no logs, no API
**Sources:** FortiOS 7.4.5 CLI Reference (local), FortiOS 7.4.5 Admin Guide (local), Fortinet official docs (docs.fortinet.com), Fortinet 4D-Demo GitHub, Fortinet Community, production deployment reports

---

## Table of Contents

1. [The Honest Assessment](#1-the-honest-assessment)
2. [Every Variable That Destroys WiFi Performance](#2-every-variable-that-destroys-wifi)
3. [Self-Inflicted Interference: The Campus Cancer](#3-self-inflicted-interference)
4. [Environmental Interference: What You Can't Control](#4-environmental-interference)
5. [Physical Placement: The Gut-Feeling Problem](#5-physical-placement)
6. [FortiAP Profile Parameter Reference: Complete](#6-parameter-reference)
7. [ARRP Profile: DARRP Deep Dive](#7-darrp-deep-dive)
8. [Band Steering & Load Balancing](#8-band-steering)
9. [DRMA: Dynamic Radio Mode Assignment](#9-drma)
10. [WiFi 6 (802.11ax) Considerations](#10-wifi-6)
11. [VAP/SSID Tuning Parameters](#11-vap-tuning)
12. [Dos and Don'ts: FortiAP Management from FortiGate](#12-dos-and-donts)
13. [Operating Blind: What to Do With No Access](#13-operating-blind)
14. [The Poor Man's Site Survey](#14-poor-mans-survey)
15. [Complete CLI Quick Reference](#15-cli-reference)

---

## 1. The Honest Assessment

Let's be direct about the situation:

**What happened:** ~40 APs were physically deployed across campus by gut feeling. No site survey was conducted. No RF measurements were taken before or after installation. APs were placed where it "seemed right" — near ceiling mounts, wherever Ethernet drops existed, wherever it was convenient.

**What's configured:** A single generic WTP profile (or maybe two) applied to all APs. Default settings everywhere. DARRP disabled. Auto-power disabled. Airtime fairness disabled. Band steering disabled. DRMA disabled. Max clients unlimited.

**What the team has access to:** A narrow web UI slice of the FortiGate WiFi controller. No CLI. No logs. No diagnostics. No API tokens. No FortiAnalyzer access. No SNMP. Essentially operating a 40-AP campus network blindfolded.

**Why this matters:** WiFi is the most sensitive layer of the network stack. It's affected by physics (walls, water, metal), by your own equipment (co-channel interference from your 40 APs blasting at full power), by client behavior (sticky clients, old drivers), by the environment (microwaves, Bluetooth, weather), and by configuration (channel width, power levels, roaming settings). Getting any one of these wrong degrades performance. Getting most of them wrong — which is the current state — guarantees terrible performance.

**The good news:** Even with limited access, the team CAN create differentiated WTP profiles and assign them per AP through the web UI. This single action — moving from one generic profile to zone-specific profiles — is the highest-impact change possible.

---

## 2. Every Variable That Destroys WiFi Performance

### 2.1 Co-Channel Interference (CCI)

**What it is:** Multiple APs on the same channel within hearing distance of each other. They must take turns transmitting — they share the same airtime.

**Campus impact:** With 40 APs and only 3 non-overlapping 2.4 GHz channels (1, 6, 11), you're GUARANTEED to have CCI. If DARRP is disabled and channels are auto-selected randomly, you likely have multiple APs in the same building on the same channel.

**Severity scale:**

| APs on Same Channel (within range) | Throughput Impact |
|------------------------------------|-------------------|
| 1 (no overlap) | 100% (baseline) |
| 2 | ~50% per AP |
| 3 | ~33% per AP |
| 4+ | <25% per AP, severe degradation |

**The math:** Two APs on channel 6 within hearing range = both get ~50% of the channel capacity. Add a third = each gets ~33%. This is NOT additive — it's time-division. They literally take turns.

**Fix:** Enable DARRP. Use 20 MHz channels (more channels available). Reduce TX power so APs can't "hear" each other as far.

### 2.2 Adjacent Channel Interference (ACI)

**What it is:** Overlapping channels interfering with each other. Primarily a 2.4 GHz problem.

**The 2.4 GHz channel overlap map:**
```
Ch 1:  ████──────────████████──────────
Ch 2:   ████──────────████████──────────
Ch 3:    ████──────────████████──────────
Ch 4:     ████──────────████████─────────
Ch 5:      ████──────────████████────────
Ch 6:       ████──────────████████───────
Ch 7:        ████──────────████████──────
Ch 8:         ████──────────████████─────
Ch 9:          ████──────────████████────
Ch 10:          ████──────────████████───
Ch 11:           ████──────────████████──
```

**Only channels 1, 6, and 11 don't overlap.** Using ANY other channel (2, 3, 4, 5, 7, 8, 9, 10) creates interference with TWO of your own APs instead of zero. This is the most common WiFi mistake.

**Fix:** Only use channels 1, 6, 11 on 2.4 GHz. Never use any other channel.

### 2.3 Hidden Node Problem

**What it is:** Two clients can hear the AP but can't hear each other. Both transmit simultaneously → collision → retransmission → wasted airtime.

**When it happens:** Large open areas where clients are far apart (auditoriums, libraries). The clients at opposite ends of a lecture hall can't hear each other, so they both transmit at the same time.

**Fix:** RTS/CTS handshake (`rts-threshold`). Setting a lower threshold forces clients to ask permission before transmitting, preventing collisions. But it adds overhead — only use when needed.

| RTS Threshold | Use Case |
|---------------|----------|
| 2347 (disabled) | Default. Fine for most deployments |
| 2346 | Barely enabled |
| 512-1024 | High-density areas with hidden node problems |
| 256 | Maximum protection, maximum overhead |

### 2.4 Signal-to-Noise Ratio (SNR)

**What it is:** The gap between the WiFi signal and background noise. Higher = better.

**Practical SNR guide:**

| SNR | WiFi Experience | Data Rate (approx) |
|-----|-----------------|-------------------|
| 40+ dB | Excellent, max speed | Full rated speed |
| 25-40 dB | Good | 50-80% of rated |
| 15-25 dB | Fair, some drops | 20-50% |
| 10-15 dB | Poor, frequent drops | 5-20% |
| <10 dB | Unusable | Near zero |

**What kills SNR:** Other APs (your own 40 APs), microwave ovens (2.4 GHz), Bluetooth devices, USB 3.0 devices (emit 2.4 GHz noise), neighboring networks, radar (DFS channels).

### 2.5 RSSI (Signal Strength) Practical Guide

| RSSI | User Experience | What Happens |
|------|----------------|--------------|
| -30 to -50 dBm | Excellent | Right next to AP. Max speed. |
| -50 to -60 dBm | Very Good | Same room. Full experience. |
| -60 to -67 dBm | Good | Reliable connection, good roaming threshold |
| -67 to -70 dBm | Adequate | Minimum for reliable streaming |
| -70 to -75 dBm | Marginal | Slow, may disconnect |
| -75 to -80 dBm | Poor | Frequent drops, crawling speed |
| -80 to -90 dBm | Very Poor | Barely connected, unusable |
| Below -90 dBm | Dead | No connection |

**Key thresholds:**
- **-67 dBm**: Minimum for good roaming handoff (design for this overlap between APs)
- **-70 dBm**: Minimum for reliable 802.11ac/ax connection
- **-75 dBm**: Below this, 802.11ax devices fall back to slower rates
- **-80 dBm**: Sticky client removal threshold (kick clients below this)

### 2.6 Channel Utilization

| Utilization | Status | User Impact |
|-------------|--------|-------------|
| 0-30% | Healthy | No noticeable impact |
| 30-50% | Moderate | Occasional slowdowns during peaks |
| 50-60% | Getting crowded | Noticeable latency and slowdowns |
| 60-70% | Problematic | Significant performance degradation |
| 70-80% | Severe | Users complaining, timeouts |
| >80% | Critical | Nearly unusable, massive retries |

**What drives utilization:** Client count, client activity (streaming vs browsing), interference, management frames (beacons, probes), control overhead.

### 2.7 TX Power and EIRP

**The critical principle:** "More power" is almost always WORSE in campus WiFi.

| Power Level | Coverage Radius (5 GHz indoor) | Use Case |
|-------------|-------------------------------|----------|
| 10 dBm | ~8-12 meters | High-density (auditoriums) |
| 13 dBm | ~12-18 meters | Medium density (classrooms) |
| 17 dBm | ~18-25 meters | Standard office |
| 20 dBm | ~25-35 meters | Low density / coverage focus |
| 23 dBm | ~35-50 meters | Outdoor / warehouse |

**Each 3 dB increase = roughly double the coverage area but also double the interference to neighbors.**

**The "match client power" rule:** Your AP can shout at 23 dBm, but the phone client transmits at ~15 dBm. The AP hears the phone poorly even though the phone hears the AP fine. This creates asymmetric connections where downlink works but uplink fails. **Set AP power to match client capabilities.**

### 2.8 Sticky Clients

**What it is:** Client devices that refuse to roam to a closer/better AP. They stay connected to the first AP they associated with, even when walking across campus.

**Why it happens:** Client-side roaming is entirely client-driven. The AP can't force a client to move (without 802.11v). Old or cheap WiFi drivers are terrible at roaming decisions.

**Impact:** Client at -82 dBm connected to AP in Building A while standing next to AP in Building F. This client consumes disproportionate airtime (many retransmissions at low data rate) and gets terrible throughput.

**Fix:** Enable 802.11v BSS Transition Management + sticky-client-remove on VAP.

---

## 3. Self-Inflicted Interference: The Campus Cancer

This is the most important section. With 40 APs and no RF planning, the biggest source of WiFi problems is YOUR OWN EQUIPMENT.

### 3.1 The Full-Power Problem

**Current state (likely):** All APs at default power (100% / ~20-23 dBm).

**What this means:** Each AP's signal bleeds through walls into adjacent rooms, corridors, floors, and buildings. APs in Building A can hear APs in Building C. All of them compete for the same 3 channels on 2.4 GHz.

**The result:** Every time ANY AP transmits, 5-10 other APs within range must wait their turn. Your "40 AP" network actually performs like a "5 AP" network because they're all fighting each other.

**Fix:** Reduce TX power. Enable auto-power-level. Set bounds to 10-17 dBm for dense areas.

### 3.2 The Wide-Channel Problem

**Current state (likely):** Default channel-bonding = 20MHz. (This is actually fine — it's the one default that's correct.)

**If someone "optimized" by setting 40 or 80 MHz on 5 GHz:** This REDUCES the number of available non-overlapping channels from 25 to 12 (40MHz) or 6 (80MHz). With 40 APs, you can't afford to waste channels.

### 3.3 The Single-Profile Problem

**Current state:** One generic profile applied to all APs.

**What this means:** The AP in a 200-seat auditorium has the same settings as the AP in a 4-person office. The AP next to a microwave has the same channel plan as the AP in a quiet library.

**Fix:** Create 3-4 zone-specific profiles. Assign per AP via the web UI.

### 3.4 The DARRP-Disabled Problem

**Current state:** DARRP = disabled (default).

**What this means:** APs are on whatever channel they landed on during initial setup. If 3 adjacent APs are all on channel 36 (5 GHz), they permanently share airtime and can't help it.

**Fix:** Enable DARRP on all profiles. Create a custom ARRP profile for campus.

---

## 4. Environmental Interference: What You Can't Control

### 4.1 Building Material Attenuation

| Material | 2.4 GHz Loss | 5 GHz Loss | Notes |
|----------|-------------|------------|-------|
| Drywall (12mm) | 3 dB | 5 dB | Minor |
| Wood door | 3 dB | 5 dB | Minor |
| Standard glass (8mm) | 3 dB | 6 dB | Minor |
| Brick wall (120mm) | 10 dB | 15 dB | Moderate |
| Concrete wall (150mm) | 15 dB | 20 dB | Heavy |
| Concrete wall (240mm) | 25 dB | 30 dB | Severe |
| Reinforced concrete | 25-30 dB | 35-40 dB | Near-total |
| Metal/steel | 35-45 dB | 40-50 dB | Total block |

**Rule:** Each 3 dB = 50% signal power lost. One concrete wall (25 dB at 5 GHz) reduces a -50 dBm signal to -75 dBm (marginal).

### 4.2 Low-E Glass: The Silent WiFi Killer

Modern energy-efficient windows have metallic coatings that act as Faraday cages:

| Glass Type | 2.4 GHz | 5 GHz |
|------------|---------|-------|
| Standard glass | 3-5 dB | 5-8 dB |
| Low-E single silver | 15-25 dB | 24-35 dB |
| Low-E double silver | 30-40 dB | 40-55 dB |

**A single pane of Low-E glass can block more WiFi than a concrete wall.** If campus buildings were renovated with modern windows, expect severe attenuation near exterior walls.

### 4.3 Non-WiFi Interference Sources

| Source | Band | Range of Impact | Pattern |
|--------|------|----------------|---------|
| Microwave ovens | 2.4 GHz | 5-10 meters | Intermittent (when running) |
| Bluetooth devices | 2.4 GHz | 3-5 meters | Hopping, constant |
| USB 3.0 devices/cables | 2.4 GHz | 1-3 meters | Broadband noise |
| Wireless cameras | 2.4 GHz | 10-30 meters | Constant |
| Radar (DFS channels) | 5 GHz | Variable | DFS triggers AP channel change |
| DECT phones | 1.9 GHz | Minimal | Usually not an issue |
| LED lighting (cheap drivers) | 2.4 GHz | 2-5 meters | Constant EMI |
| Aquariums / water features | 2.4 GHz | 3-5 meters | Absorption |
| Human bodies (crowds) | 2.4 GHz + 5 GHz | Per-person | 3-5 dB per person in path |

### 4.4 Floor-to-Floor Bleed

WiFi signals pass through ceilings/floors:

| Floor Type | 2.4 GHz Attenuation | 5 GHz Attenuation |
|-----------|---------------------|-------------------|
| Wood/linoleum | 5-8 dB | 8-12 dB |
| Concrete slab | 15-20 dB | 20-25 dB |
| Reinforced concrete | 20-25 dB | 25-30 dB |

**Implication:** APs on floor 1 can interfere with APs on floor 2. Stagger channels between floors (floor 1: ch 1, floor 2: ch 6, floor 3: ch 11 for 2.4 GHz).

---

## 5. Physical Placement: The Gut-Feeling Problem

### 5.1 Common Placement Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| AP in room corner | Uneven coverage, wasted signal into walls | Move to center of coverage area |
| AP against outer wall | Signal bleeds outside, reduced indoor coverage | Move inward 1-2 meters |
| AP near metal duct/HVAC | Signal reflection, dead zones | Move at least 1m away |
| AP above ceiling tiles (hidden) | Signal blocked by metal frame, insulation | Mount below ceiling or use specialized mount |
| AP mounted on wall (sideways) | Omnidirectional pattern shoots into adjacent rooms | Use ceiling mount, or aim correctly |
| AP too high (>5m) | Signal goes over clients' heads | Wall-mount at 3-4m or use directional antenna |
| AP too low (<2.5m) | Coverage too small, easily blocked by furniture | Raise to 2.8-4m ceiling height |
| APs directly above/below each other | Floor bleed creates co-channel interference | Offset APs between floors |
| AP near fluorescent lights | EMI in 2.4 GHz band | Move 1-2m away |
| AP in server/electric room | Metal racks block signal | Don't put APs in these rooms |

### 5.2 AP Spacing Guidelines

| Environment | 5 GHz Spacing | Coverage per AP |
|-------------|--------------|-----------------|
| High-density (auditorium) | 8-12 m | 1 AP per 20-30 seats |
| Standard classroom | 1 AP per room | 25-30 students |
| Open office | 12-18 m | 1,500-2,000 sq ft |
| Corridor | 15-25 m | Minimal users |
| Outdoor | 25-40 m | Weather-dependent |

**5 GHz practical indoor range: 6-8 meters for reliable coverage.** Not the 50+ meters marketing claims.

### 5.3 Antenna Radiation Pattern Reality

Omnidirectional AP antennas radiate in a donut shape:
- **Good coverage**: Horizontal plane (360° around AP)
- **Weak coverage**: Directly above and below AP

**Ceiling mount** = signal goes DOWN to users (optimal)
**Wall mount** = signal goes SIDEWAYS (suboptimal, creates dead zones above/below)

---

## 6. FortiAP Profile Parameter Reference: Complete

### 6.1 WTP Profile Radio Parameters (per radio-1/2/3/4)

Sourced directly from FortiOS 7.4.5 CLI Reference.

| Parameter | Type | Range | Default | Campus Optimal (Dense) | Campus Optimal (Standard) | Campus Optimal (Coverage) |
|-----------|------|-------|---------|----------------------|--------------------------|--------------------------|
| `band` | option | 802.11a/b/g/n/ac/ax/be (2G/5G/6G) | (AP-dependent) | 802.11ax-2G or 802.11ax-5G | Same | Same |
| `mode` | option | disabled, ap, monitor, sniffer, sam | ap | ap | ap | ap |
| `channel-bonding` | option | 20/40/80/160/240/320MHz | 20MHz | **20MHz** | 20-40MHz | 20MHz |
| `darrp` | option | enable, disable | **disable** | **enable** | **enable** | enable |
| `arrp-profile` | string | profile name | (none) | "campus-dense" | "campus-standard" | (default) |
| `auto-power-level` | option | enable, disable | **disable** | **enable** | **enable** | enable |
| `auto-power-low` | integer | 0-max | 10 | **10** dBm | 12 dBm | 15 dBm |
| `auto-power-high` | integer | 0-max | 17 | **17** dBm | 20 dBm | 23 dBm |
| `auto-power-target` | string | dBm | -70 | -70 | -70 | -65 |
| `power-mode` | option | dBm, percentage | percentage | dBm | dBm | dBm |
| `power-level` | integer | 0-100 (%) or 0-50 (dBm) | 100 | (use auto) | (use auto) | (use auto) |
| `max-clients` | integer | 0-4294967295 | 0 (unlimited) | **30** | **50** | 0 (unlimited) |
| `airtime-fairness` | option | enable, disable | **disable** | **enable** | **enable** | disable |
| `drma` | option | enable, disable | **disable** | **enable** | **enable** | disable |
| `drma-sensitivity` | option | low, medium, high | low | **high** | medium | N/A |
| `dtim` | integer | 1-255 | 1 | **3** | 2 | 1 |
| `frag-threshold` | integer | 800-2346 | 2346 | **2346** (disabled) | 2346 | 2346 |
| `rts-threshold` | integer | 256-2347 | 2346 | **2347** (disabled) | 2347 | 2347 |
| `beacon-interval` | integer | 0-65535 | 100 | 100 | 100 | 100 |
| `channel-utilization` | option | enable, disable | enable | **enable** | **enable** | **enable** |
| `coexistence` | option | enable, disable | enable | enable | enable | enable |
| `bss-color` | integer | 0-63 | 0 | auto (WiFi 6) | auto | auto |
| `bss-color-mode` | option | auto, static | auto | **auto** | auto | auto |
| `mimo-mode` | option | default/1x1/2x2/3x3/4x4/8x8 | default | default | default | default |
| `short-guard-interval` | option | enable, disable | disable | **enable** | **enable** | enable |
| `amsdu` | option | enable, disable | enable | enable | enable | enable |
| `wids-profile` | string | profile name | (none) | "campus-wids" | "campus-wids" | "campus-wids" |
| `vap-all` | option | tunnel, bridge, manual | (none) | tunnel/bridge | tunnel/bridge | tunnel/bridge |
| `zero-wait-dfs` | option | enable, disable | (AP-dependent) | **enable** | **enable** | **enable** |

### 6.2 WTP Profile Top-Level Parameters

| Parameter | Type | Range | Default | Campus Optimal |
|-----------|------|-------|---------|---------------|
| `frequency-handoff` | option | enable, disable | **disable** | **enable** |
| `ap-handoff` | option | enable, disable | **disable** | **enable** |
| `handoff-rssi` | integer | 20-30 | 25 | **25** |
| `handoff-sta-thresh` | integer | 5-60 | **0** (disabled!) | **30** |
| `handoff-roaming` | option | enable, disable | - | **enable** |
| `lldp` | option | enable, disable | - | **enable** |
| `energy-efficient-ethernet` | option | enable, disable | - | enable |

**CRITICAL FINDING:** `handoff-sta-thresh` defaults to **0** (disabled). This means AP load balancing is OFF by default. You MUST set this to 30+ for any meaningful load distribution between APs.

### 6.3 What Each Default Means in Practice

| Parameter | Default | What It Means for Your Campus |
|-----------|---------|-------------------------------|
| `darrp = disable` | Channels never optimized. APs sit on whatever channel they booted on. 10+ APs could be on the same channel. |
| `auto-power-level = disable` | All APs blast at 100% power. Every AP interferes with every other AP within range. |
| `airtime-fairness = disable` | One slow client at the edge of coverage can consume more airtime than 10 nearby clients. |
| `drma = disable` | Redundant 2.4 GHz radios in dense areas keep transmitting, causing interference for no benefit. |
| `max-clients = 0` | Unlimited clients per radio. An AP with 100 clients gives each client ~1% of available airtime. |
| `handoff-sta-thresh = 0` | No load balancing. Clients pile onto one AP while adjacent APs sit idle. |
| `frequency-handoff = disable` | No band steering. Dual-band clients camp on congested 2.4 GHz while 5 GHz sits empty. |
| `ap-handoff = disable` | No AP handoff. Clients stick to first AP forever. |

**Every single intelligent feature is OFF by default.** The default FortiGate WiFi configuration is designed to "work" in the simplest possible setup (1-2 APs). For 40 APs on a campus, defaults guarantee poor performance.

---

## 7. DARRP Deep Dive

### 7.1 How DARRP Scores Channels

DARRP runs in two phases:

**Phase 1 — Channel Exclusion:**
- AP scans all available channels
- Rejects channels exceeding ANY threshold:
  - `threshold-ap`: Too many neighboring APs (default 250)
  - `threshold-noise-floor`: Too noisy (default -85 dBm)
  - `threshold-channel-load`: Too utilized (default 60%)
  - `threshold-spectral-rssi`: Too much spectral energy (default -65 dBm)

**Phase 2 — Channel Scoring:**
- Remaining channels scored by weighted sum:
  - `weight-channel-load` × channel utilization
  - `weight-noise-floor` × noise measurement
  - `weight-spectral-rssi` × spectral interference
  - `weight-managed-ap` × nearby managed AP count
  - `weight-rogue-ap` × nearby rogue AP count
- Lowest score wins = cleanest channel

### 7.2 ARRP Profile Defaults vs Campus Optimal

**From FortiOS 7.4.5 CLI Reference (local):**

| Parameter | Default | Campus Dense | Campus Standard |
|-----------|---------|-------------|-----------------|
| `weight-channel-load` | 20 | **50** | 30 |
| `weight-managed-ap` | 50 | **50** | 50 |
| `weight-noise-floor` | 40 | **40** | 40 |
| `weight-rogue-ap` | 10 | **20** | 15 |
| `weight-spectral-rssi` | 40 | **40** | 40 |
| `weight-dfs-channel` | 0 | **10** | 5 |
| `weight-weather-channel` | 0 | **5** | 0 |
| `threshold-ap` | 250 | **200** | 250 |
| `threshold-channel-load` | 60% | **50%** | 60% |
| `threshold-noise-floor` | -85 | **-85** | -85 |
| `threshold-spectral-rssi` | -65 | **-70** | -65 |
| `include-dfs-channel` | enable | **enable** | **enable** |
| `selection-period` | 3600 | 3600 | 3600 |

### 7.3 DARRP Campus Configuration

```bash
# Create campus ARRP profile
config wireless-controller arrp-profile
    edit "campus-dense"
        set weight-channel-load 50
        set weight-managed-ap 50
        set weight-noise-floor 40
        set weight-rogue-ap 20
        set weight-spectral-rssi 40
        set threshold-channel-load 50
        set threshold-noise-floor "-85"
        set threshold-ap 200
        set include-dfs-channel enable
    next
end

# Set DARRP optimization schedule (run during off-hours)
config wireless-controller setting
    set darrp-optimize 86400        # Every 24 hours
end

# Assign ARRP profile to WTP profile radio
config wireless-controller wtp-profile
    edit "WTP-HIGH-DENSITY"
        config radio-2
            set darrp enable
            set arrp-profile "campus-dense"
        end
    next
end
```

### 7.4 DARRP Schedule Best Practice

- **Default: 86400 seconds (24 hours)** — run once daily
- **Schedule during off-hours** (2-4 AM) to minimize client disruption
- **DO NOT run more frequently than every 4 hours** — each channel change disconnects all clients briefly
- **DARRP takes 2-5 minutes** to complete across all APs

### 7.5 Verifying DARRP

```bash
# Check DARRP status per AP
diagnose wireless-controller wlac -c darrp

# Check on the AP itself
cw_diag -c darrp
```

### 7.6 Known DARRP Issues (from community)

1. **DARRP not working**: Requires BOTH `frequency-handoff enable` AND `ap-handoff enable` in the WTP profile
2. **All APs on same channel**: DARRP may have failed to run — check schedule and ARRP profile
3. **Channel flapping**: If DARRP runs too often, APs keep changing channels — reduce frequency
4. **For 12+ APs in one area**: Consider static channel assignment as backup when DARRP can't find clean channels

---

## 8. Band Steering & Load Balancing

### 8.1 Frequency Handoff (Band Steering)

**How it works:** AP suppresses probe responses on 2.4 GHz for dual-band clients with strong 5 GHz signal. Client eventually tries 5 GHz and connects there.

**Configuration:**
```bash
config wireless-controller wtp-profile
    edit "WTP-HIGH-DENSITY"
        set frequency-handoff enable    # Enable band steering
        set handoff-rssi 25             # 5 GHz signal threshold (20-30)
        set ap-handoff enable           # Enable AP load balancing
        set handoff-sta-thresh 30       # Client count trigger (5-60)
    next
end
```

**handoff-rssi values:**

| Value | Behavior | Use When |
|-------|----------|----------|
| 20 | Aggressive — steer at lower 5 GHz signal | Strong 5 GHz coverage everywhere |
| 25 | Balanced (default, recommended) | Standard deployment |
| 30 | Conservative — require very strong 5 GHz | Weak 5 GHz in some areas |

**handoff-sta-thresh values:**

| Value | Behavior |
|-------|----------|
| 0 | **DISABLED** (default — no load balancing!) |
| 20 | Trigger at 20 clients |
| 30 | Trigger at 30 clients (recommended for campus) |
| 55 | Trigger at 55 clients |
| 60 | Maximum, rarely triggers |

### 8.2 When Band Steering HURTS

**Disable frequency-handoff when:**
- Single AP deployment (no alternative AP to steer to)
- IoT devices that only support 2.4 GHz and get confused by probe suppression
- Areas with poor 5 GHz coverage (clients steered to dead zone)
- Guest networks where maximum range is preferred over speed

### 8.3 802.11v BSS Transition Management

More effective than frequency handoff alone. AP actively sends BSS Transition Management Request to clients, telling them to move.

```bash
# Enable on VAP (SSID level)
config wireless-controller vap
    edit "campus-students"
        set 80211v enable
        set sticky-client-remove enable
        set sticky-client-threshold-5g "-65"
    next
end
```

**Sticky client thresholds** (from FortiOS 7.4.5 CLI Ref):
- `sticky-client-threshold-2g`: default **-79 dBm**
- `sticky-client-threshold-5g`: default **-76 dBm**
- `sticky-client-threshold-6g`: default **-76 dBm**

**Recommended campus values:**
- 2G: **-75 dBm** (be more aggressive — kick weak 2G clients)
- 5G: **-70 dBm** (maintain good 5G connections)
- 6G: **-70 dBm** (same as 5G)

---

## 9. DRMA: Dynamic Radio Mode Assignment

### 9.1 How DRMA Works

DRMA calculates a **Network Coverage Factor (NCF)** for each radio:
- Analyzes top 4 neighboring FortiAPs with RSSI > -65 dBm
- If fewer than 4 neighbors detected → DRMA does NOT activate (not enough overlap)
- NCF = measure of how redundant this radio is given neighbor coverage

**NCF thresholds:**

| Sensitivity | NCF Threshold | Meaning |
|-------------|---------------|---------|
| low | 100% | Radio redundant only at 100% overlap coverage |
| medium | 95% | Radio redundant at 95% overlap |
| high | 90% | Radio redundant at 90% overlap |

### 9.2 When to Use DRMA

| Scenario | Enable? | Sensitivity |
|----------|---------|-------------|
| Auditorium (5+ APs overlapping) | Yes | high |
| Open-plan office (3-4 APs) | Yes | medium |
| Standard office (1-2 APs) | Maybe | low |
| Corridor / isolated AP | **No** | N/A |
| Outdoor | **No** | N/A |

### 9.3 DRMA Configuration

```bash
config wireless-controller wtp-profile
    edit "WTP-HIGH-DENSITY"
        config radio-1                # 2.4 GHz - most likely to be redundant
            set drma enable
            set drma-sensitivity high   # Aggressive: 90% NCF threshold
        end
        config radio-2                # 5 GHz - keep active
            set drma enable
            set drma-sensitivity medium # Less aggressive
        end
    next
end
```

### 9.4 Verifying DRMA

```bash
# Check which radios are in monitor mode
diagnose wireless-controller wlac -c wtp-drma-radio
```

### 9.5 DRMA Interval

```bash
config wireless-controller timers
    set drma-interval 60     # Minutes (1-1440), default 60
end
```

Default (60 minutes) is appropriate. Don't change unless you have a specific reason.

---

## 10. WiFi 6 (802.11ax) Considerations

### 10.1 BSS Coloring

WiFi 6 introduces BSS Coloring — each AP assigns a "color" (0-63) to its frames. Clients can differentiate frames from their own AP vs. neighboring APs, reducing co-channel interference impact.

**FortiOS 7.4.5 supports BSS Coloring:**
```bash
config wireless-controller wtp-profile
    edit "WTP-HIGH-DENSITY"
        config radio-2
            set bss-color-mode auto    # Auto-assign BSS color
        end
    next
end
```

**Default:** auto (FortiOS automatically assigns colors). **Keep it on auto.**

### 10.2 OFDMA (Orthogonal Frequency-Division Multiple Access)

WiFi 6's killer feature for high-density: splits a channel into sub-channels (RU - Resource Units), allowing simultaneous transmission to multiple clients.

**Impact:** Instead of serving clients one at a time, an AP can serve 4-8 clients simultaneously per transmission. This dramatically improves efficiency in dense deployments.

**FortiGate setting:** OFDMA is enabled automatically when `band` is set to 802.11ax. No separate configuration needed.

### 10.3 MU-MIMO (Multi-User MIMO)

WiFi 6 supports up to 8×8 MU-MIMO, allowing the AP to transmit to multiple clients simultaneously using different spatial streams.

**FortiGate setting:**
```bash
config wireless-controller vap
    edit "campus-students"
        set mu-mimo enable    # Default: enable
        set high-efficiency enable    # Default: enable
    next
end
```

### 10.4 Target Wake Time (TWT)

WiFi 6 feature that schedules when clients wake up to transmit. Reduces power consumption and airtime contention.

**Default:** enabled. Keep it enabled.

### 10.5 1024-QAM

Requires excellent SNR (>35 dB) to function. Only achievable when client is very close to AP (<5m). In campus deployments, most clients won't benefit.

**Don't design for 1024-QAM.** Design for robust 256-QAM coverage instead.

---

## 11. VAP/SSID Tuning Parameters

### 11.1 Critical VAP Parameters

**From FortiOS 7.4.5 CLI Reference:**

| Parameter | Default | Campus Optimal | Why |
|-----------|---------|---------------|-----|
| `80211k` | disable | **enable** | Neighbor list for smart roaming |
| `80211v` | enable | **enable** | BSS transition for load balancing |
| `sticky-client-remove` | disable | **enable** | Kick weak-signal clients |
| `sticky-client-threshold-2g` | -79 | **-75** | More aggressive on 2G |
| `sticky-client-threshold-5g` | -76 | **-70** | Maintain good 5G |
| `mu-mimo` | enable | **enable** | Multi-client simultaneous TX |
| `high-efficiency` | enable | **enable** | WiFi 6 features |
| `target-wake-time` | enable | **enable** | Power saving + airtime |
| `broadcast-ssid` | enable | **enable** | Visible SSID |
| `fast-roaming` | enable | **enable** | OKC (Opportunistic Key Caching) |
| `okc` | enable | **enable** | Fast reconnection |
| `dynamic-vlan` | disable | (if using RADIUS) | Per-user VLAN |
| `max-clients` | 0 | **0** (set per radio instead) | Unlimited at VAP level |
| `max-clients-ap` | 0 | **0** (set per radio instead) | Unlimited at AP level |
| `multicast-enhance` | disable | **enable** | Convert multicast to unicast |
| `probe-resp-suppression` | disable | **enable** (dense) | Reduce probe response overhead |
| `probe-resp-threshold` | -80 | **-70** | Only respond to nearby clients |
| `atf-weight` | (20) | **20** | Airtime weight (keep default) |

### 11.2 Broadcast Suppression

Reduces management frame overhead, freeing airtime for actual data:

```bash
config wireless-controller vap
    edit "campus-students"
        set broadcast-suppression dhcp-up dhcp-down arp-known arp-unknown ipv6
    next
end
```

This suppresses DHCP broadcasts, ARP floods, and IPv6 multicast — significant airtime savings in dense deployments.

### 11.3 Probe Response Suppression

In high-density areas, clients send many probe requests, creating significant overhead:

```bash
config wireless-controller vap
    edit "campus-students"
        set probe-resp-suppression enable
        set probe-resp-threshold "-70"    # Only respond to clients with signal > -70
    next
end
```

This means the AP only responds to probe requests from clients with signal stronger than -70 dBm. Distant clients (from other buildings) won't get responses, reducing airtime waste.

---

## 12. Dos and Don'ts: FortiAP Management from FortiGate

### 12.1 DO: Create Zone-Specific Profiles

**✅ Create at minimum 3 WTP profiles:**
1. `WTP-HIGH-DENSITY` — lecture halls, auditoriums, cafeterias
2. `WTP-STANDARD` — offices, classrooms, meeting rooms
3. `WTP-COVERAGE` — corridors, outdoor, isolated areas

**Why:** Different physical environments need different radio settings. One size fits nobody.

### 12.2 DO: Enable DARRP on All Radios

**✅ Enable DARRP on every 5 GHz radio.** Create a custom ARRP profile for campus. Let the system optimize channels automatically — manual channel planning for 40 APs across 20+ buildings is impractical without RF tools.

### 12.3 DO: Reduce TX Power

**✅ Enable auto-power-level.** Set 10-17 dBm for dense areas, 15-23 dBm for coverage areas. The default of 100% power is almost certainly causing co-channel interference across your entire campus.

### 12.4 DO: Enable Airtime Fairness

**✅ Enable on all radios in dense areas.** This single setting prevents one distant client from degrading everyone's experience.

### 12.5 DO: Set Max Clients Per Radio

**✅ Set max-clients to 30 for dense, 50 for standard.** An overloaded AP provides terrible service to everyone. It's better to deny new connections than to degrade existing ones.

### 12.6 DO: Use 20 MHz Channels on 5 GHz

**✅ Set channel-bonding to 20MHz for high-density areas.** This gives you 25+ non-overlapping channels (with DFS) instead of 6 with 80MHz. More channels = less CCI = better performance.

### 12.7 DO: Enable Band Steering + AP Handoff

**✅ Enable both frequency-handoff and ap-handoff.** Set handoff-sta-thresh to 30. This pushes clients to 5 GHz and balances them across APs.

### 12.8 DO: Enable 802.11k/v on All SSIDs

**✅ Both should be enabled.** 802.11k gives clients a neighbor list. 802.11v lets APs actively steer clients. Together they dramatically improve roaming.

### 12.9 DO: Document What You Change

**✅ Keep a spreadsheet: AP name → building → floor → room → WTP profile assigned.** Before-and-after notes on performance. This is the only way to learn what works in YOUR campus.

### 12.10 DO: Use the WiFi Dashboard

**✅ Check Dashboard → WiFi daily for a week after changes.** Note which APs have high client counts, which have high channel utilization. This data guides further tuning.

---

### 12.11 DON'T: Set All APs to Maximum Power

**❌ Never set all APs to 100% TX power.** This is the #1 cause of campus WiFi problems. More power = more interference = worse performance for everyone.

### 12.12 DON'T: Use Channels Other Than 1, 6, 11 on 2.4 GHz

**❌ Channels 2-5, 7-10 overlap with the big three.** Using them creates interference with TWO channels instead of zero. Only use 1, 6, 11.

### 12.13 DON'T: Use 40 MHz Channels on 2.4 GHz

**❌ FortiOS doesn't allow it by default for good reason.** 40 MHz on 2.4 GHz uses 2/3 of the entire band, guaranteeing interference with every other AP.

### 12.14 DON'T: Change Multiple Settings Simultaneously

**❌ Don't enable DARRP + DRMA + band steering + airtime fairness all on the same day.** If something goes wrong (and it will), you won't know which change caused it. Change ONE thing, observe for 24-48 hours, then change the next.

### 12.15 DON'T: Run DARRP During Peak Hours

**❌ DARRP causes brief client disconnections when changing channels.** Schedule during 2-4 AM. Running DARRP during class time will generate complaints.

### 12.16 DON'T: Enable DRMA on Isolated APs

**❌ DRMA requires 4+ neighboring APs with RSSI > -65 dBm to calculate NCF.** If an AP is isolated (corridor, outdoor), DRMA either won't activate or will make poor decisions.

### 12.17 DON'T: Blindly Trust DARRP

**❌ DARRP optimizes channels but can't fix physical placement problems.** If an AP is behind a metal duct, DARRP can't help. If two APs are 3 meters apart, DARRP can't fix the interference. Physical placement matters more than channel selection.

### 12.18 DON'T: Forget About 2.4 GHz

**❌ Don't disable 2.4 GHz entirely.** Many IoT devices, old laptops, and cheap phones only support 2.4 GHz. Instead: reduce 2.4 GHz power, enable band steering to push capable clients to 5 GHz, and accept that 2.4 GHz will always be congested.

### 12.19 DON'T: Make Changes Without Noting the Current State

**❌ Before changing ANY profile, screenshot or write down the current values.** If the change makes things worse, you need to revert to exactly what was there before.

### 12.20 DON'T: Assume More APs = Better WiFi

**❌ Adding APs to a badly tuned network makes things WORSE.** Each new AP adds interference. Only add APs after tuning power levels, enabling DARRP, and confirming actual coverage gaps.

---

## 13. Operating Blind: What to Do With No Access

### 13.1 What You CAN Do (Web UI Only)

| Action | How |
|--------|-----|
| View WiFi Dashboard | Dashboard → WiFi |
| See client counts per AP | Dashboard → WiFi → Clients by FortiAP |
| See channel utilization | Dashboard → WiFi → Channel Utilization |
| See AP online/offline | WiFi & Switch Controller → Managed FortiAPs |
| View current profiles | WiFi & Switch Controller → FortiAP Profiles |
| Create/edit WTP profiles | WiFi & Switch Controller → FortiAP Profiles → Create/Edit |
| Create/edit SSIDs | WiFi & Switch Controller → SSIDs |
| Assign profile to AP | Managed FortiAPs → Edit AP → WTP Profile dropdown |
| View AP serial numbers | Managed FortiAPs list |
| See which AP is in which building | AP names may indicate location (e.g., "A-0-13-AP1") |

### 13.2 What You CANNOT Do

| Action | Why | Permission Needed |
|--------|-----|-------------------|
| Run diagnostic commands | No CLI access | cli-diagnose = enable |
| View logs | No log access | loggrp = read |
| Export config programmatically | No CLI/API | cli-show = enable |
| Run spectrum analysis | No CLI | cli-diagnose = enable |
| See real-time client RSSI/SNR | No diagnostics | cli-diagnose = enable |
| Automate monitoring | No API token | super_admin creates API user |
| View historical data | No FortiAnalyzer access | FA account |

### 13.3 The Practical Workflow (With Current Access)

**Week 1: Baseline**
1. Screenshot the WiFi Dashboard — note AP names, client counts, channel utilization
2. Create a spreadsheet: AP name → building → floor → room → current profile
3. Walk campus with WiFi analyzer app on phone — note dead zones, weak areas
4. Identify the top 5 worst areas — these get profile changes first

**Week 2: First Profile Change**
1. Create `WTP-HIGH-DENSITY` profile with settings from Section 6
2. Assign to the 5-10 worst APs (auditoriums, lecture halls, crowded areas)
3. Monitor Dashboard for 48 hours — note client count and utilization changes

**Week 3: Expand**
1. Create `WTP-STANDARD` profile
2. Assign to remaining APs
3. Create ARRP profile "campus-dense"
4. Enable DARRP on all 5 GHz radios
5. Monitor for 48 hours

**Week 4: Refine**
1. Create `WTP-COVERAGE` for corridor/outdoor APs
2. Fine-tune max-clients and handoff thresholds based on Dashboard data
3. Document before/after for management

### 13.4 What to Request (Priority Order)

1. **`cli-diagnose = enable`** — Unlocks ALL wireless diagnostics
2. **`loggrp = read`** — Can see WiFi logs (auth failures, roaming events)
3. **API token** — Can automate monitoring and build dashboards
4. **FortiAnalyzer read access** — Historical analytics and trends

---

## 14. The Poor Man's Site Survey

### 14.1 Tools You Already Have

| Tool | What It Shows | Where to Get It |
|------|---------------|-----------------|
| **FortiGate WiFi Dashboard** | Client counts, channel util, AP status | Already have |
| **Phone WiFi analyzer** | RSSI, channel, SSID, security | Free app (WiFi Analyzer on Android, WiFiman on iOS) |
| **Laptop WiFi info** | Detailed connection stats | Built into OS |
| **Your feet** | Walking the campus is the best diagnostic | Already have |

### 14.2 The Walkthrough Process

**For each building/floor:**

1. **Stand directly under each AP** → check signal strength on phone
   - Expected: -30 to -45 dBm (very strong)
   - If weaker than -50 dBm → AP may have issues (bad placement, obstruction, failing radio)

2. **Walk to the midpoint between two APs** → check signal
   - Expected: -60 to -67 dBm (good overlap)
   - If weaker than -70 dBm → coverage gap between APs

3. **Walk to known problem areas** → check signal
   - Note exact RSSI, which AP you're connected to, which channel
   - Check if you're on 2.4 GHz or 5 GHz (band steering working?)

4. **Note dead zones** → mark on floor plan
   - Areas with no signal or signal below -80 dBm
   - These may need AP relocation or additional APs

### 14.3 Red Flags to Document

| What You See | What It Probably Means |
|-------------|----------------------|
| Strong signal but slow speed | Channel congestion — too many clients or interference |
| Weak signal everywhere | AP too far, obstructed, or too low power |
| Phone shows full bars but can't connect | Authentication issue or max-clients reached |
| Connection drops when walking | No roaming — sticky client, 802.11k/v not enabled |
| 2.4 GHz only in dense area | Band steering not working, or 5 GHz radio disabled |
| All APs on same channel | DARRP disabled or failed — enable it |
| Client count >50 on one AP | No max-clients set — add a hard cap |
| Channel utilization >70% | AP overloaded — reduce power, add APs, enable airtime fairness |

### 14.4 Building Material Quick Test

Walk toward an exterior wall with WiFi analyzer running:
- If signal drops rapidly near windows → likely Low-E glass (24-55 dB loss)
- If signal is fine until hitting a wall → standard attenuation (check material type)
- If signal is fine everywhere but speed is bad → congestion, not coverage

---

## 15. Complete CLI Quick Reference

### Profile Creation

```bash
# HIGH-DENSITY PROFILE (auditoriums, lecture halls)
config wireless-controller wtp-profile
    edit "WTP-HIGH-DENSITY"
        set frequency-handoff enable
        set ap-handoff enable
        set handoff-rssi 25
        set handoff-sta-thresh 30
        config radio-1
            set mode ap
            set band 802.11ax-2G
            set channel-bonding 20MHz
            set darrp enable
            set arrp-profile "campus-dense"
            set auto-power-level enable
            set auto-power-low 10
            set auto-power-high 17
            set max-clients 30
            set airtime-fairness enable
            set drma enable
            set drma-sensitivity high
            set dtim 3
            set bss-color-mode auto
            set channel-utilization enable
            set short-guard-interval enable
        end
        config radio-2
            set mode ap
            set band 802.11ax-5G
            set channel-bonding 20MHz
            set darrp enable
            set arrp-profile "campus-dense"
            set auto-power-level enable
            set auto-power-low 10
            set auto-power-high 17
            set max-clients 30
            set airtime-fairness enable
            set drma enable
            set drma-sensitivity medium
            set dtim 3
            set bss-color-mode auto
            set channel-utilization enable
            set short-guard-interval enable
        end
    next
end

# STANDARD PROFILE (offices, classrooms)
config wireless-controller wtp-profile
    edit "WTP-STANDARD"
        set frequency-handoff enable
        set ap-handoff enable
        set handoff-rssi 25
        set handoff-sta-thresh 40
        config radio-1
            set mode ap
            set band 802.11ax-2G
            set channel-bonding 20MHz
            set darrp enable
            set arrp-profile "campus-standard"
            set auto-power-level enable
            set auto-power-low 12
            set auto-power-high 20
            set max-clients 50
            set airtime-fairness enable
            set drma enable
            set drma-sensitivity medium
            set dtim 2
            set channel-utilization enable
        end
        config radio-2
            set mode ap
            set band 802.11ax-5G
            set channel-bonding 40MHz
            set darrp enable
            set arrp-profile "campus-standard"
            set auto-power-level enable
            set auto-power-low 12
            set auto-power-high 20
            set max-clients 50
            set airtime-fairness enable
            set channel-utilization enable
        end
    next
end

# COVERAGE PROFILE (corridors, outdoor, isolated)
config wireless-controller wtp-profile
    edit "WTP-COVERAGE"
        set frequency-handoff enable
        set ap-handoff enable
        set handoff-rssi 25
        set handoff-sta-thresh 50
        config radio-1
            set mode ap
            set band 802.11ax-2G
            set channel-bonding 20MHz
            set darrp enable
            set auto-power-level enable
            set auto-power-low 15
            set auto-power-high 23
            set channel-utilization enable
        end
        config radio-2
            set mode ap
            set band 802.11ax-5G
            set channel-bonding 80MHz
            set darrp enable
            set auto-power-level enable
            set auto-power-low 15
            set auto-power-high 23
            set channel-utilization enable
        end
    next
end
```

### ARRP Profile

```bash
config wireless-controller arrp-profile
    edit "campus-dense"
        set weight-channel-load 50
        set weight-managed-ap 50
        set weight-noise-floor 40
        set weight-rogue-ap 20
        set weight-spectral-rssi 40
        set threshold-channel-load 50
        set threshold-noise-floor "-85"
        set threshold-ap 200
        set include-dfs-channel enable
    next
    edit "campus-standard"
        set weight-channel-load 30
        set weight-managed-ap 50
        set weight-noise-floor 40
        set weight-rogue-ap 15
        set weight-spectral-rssi 40
        set threshold-channel-load 60
        set threshold-noise-floor "-85"
        set include-dfs-channel enable
    next
end
```

### SSID/VAP Configuration

```bash
config wireless-controller vap
    edit "campus-students"
        set ssid "Campus-Students"
        set security wpa2-only-personal
        set passphrase "REPLACE_ME"
        set broadcast-ssid enable
        set 80211k enable
        set 80211v enable
        set mu-mimo enable
        set high-efficiency enable
        set target-wake-time enable
        set sticky-client-remove enable
        set sticky-client-threshold-2g "-75"
        set sticky-client-threshold-5g "-70"
        set broadcast-suppression dhcp-up dhcp-down arp-known arp-unknown ipv6
        set fast-roaming enable
        set okc enable
        set multicast-enhance enable
    next
end
```

### DARRP Schedule

```bash
config wireless-controller setting
    set darrp-optimize 86400
end
```

### Diagnostic Commands (need cli-diagnose)

```bash
# All connected clients
diagnose wireless-controller wlac -d sta online

# Per-AP client details
diagnose wireless-controller wlac -d wtp <AP-SERIAL>

# DARRP status
diagnose wireless-controller wlac -c darrp

# DRMA status
diagnose wireless-controller wlac -c wtp-drma-radio

# Rogue AP scan
diagnose wireless-controller wlac -c ap-scan

# AP connection status
diagnose wireless-controller get-conn-status

# Radio resource info
diagnose wireless-controller wlac -d rrm

# Debug specific client
diagnose wireless-controller wlac sta_filter <MAC> 1

# Debug specific AP
diagnose wireless-controller wlac wtp_filter <SN> <IP>:5246 2
```

### Assign Profile to AP

```bash
config wireless-controller wtp
    edit "<AP-SERIAL-NUMBER>"
        set wtp-profile "WTP-HIGH-DENSITY"
    next
end
```

Or via Web UI: **WiFi & Switch Controller → Managed FortiAPs → Edit AP → WTP Profile dropdown**

---

## Appendix: Channel Planning Math for 40 APs

### 2.4 GHz Channel Plan

3 non-overlapping channels × 40 APs = average 13 APs per channel across campus.

With proper power reduction (10-17 dBm), each AP only "hears" APs within ~15-20 meters. In a multi-building campus, buildings provide natural isolation. The effective CCI is per-building.

**Per-building strategy:**
- Building with 3 APs: assign ch 1, 6, 11 (one each)
- Building with 6 APs: assign ch 1, 6, 11, 1, 6, 11 (alternate)
- Building with 2 APs: assign ch 1, 6 (or 1, 11)

### 5 GHz Channel Plan

With DFS enabled and 20 MHz channels: ~25 non-overlapping channels available.

40 APs ÷ 25 channels = ~1.6 APs per channel average. Much better than 2.4 GHz.

**This is why band steering to 5 GHz is critical.** 5 GHz has 8× more non-overlapping channels than 2.4 GHz.

### The Math Summary

| Band | Channels (20 MHz) | APs per Channel (40 APs) | Interference Level |
|------|-------------------|-------------------------|-------------------|
| 2.4 GHz | 3 | ~13 | Severe |
| 5 GHz (no DFS) | 8 | 5 | High |
| 5 GHz (with DFS) | 25 | 1.6 | Low |
| 6 GHz | 59 | 0.7 | None |

**Conclusion:** Enable DFS channels. Enable band steering. The vast majority of campus WiFi problems will improve when clients move from 3-channel 2.4 GHz to 25-channel 5 GHz.

---

*Document generated from: FortiOS 7.4.5 CLI Reference (120K+ lines), FortiOS 7.4.5 Administration Guide (191K+ lines), Fortinet FortiAP Configuration Guides 7.4/7.6, Fortinet Community forums, Fortinet 4D-Demo GitHub repository, RF engineering references, local project documentation.*
