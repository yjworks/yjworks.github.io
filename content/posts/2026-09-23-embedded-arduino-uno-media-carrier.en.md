---
title: "For a Camera Add-On, Skip the $299 VENTUNO Q"
date: 2026-09-23T03:12:53+09:00
slug: "embedded-arduino-uno-media-carrier"
summary: "Arduino's new $19.25 UNO Media Carrier bolts a camera, display, and audio onto both the UNO Q and the pricier VENTUNO Q. Since the same accessory fits either board, we looked at whether a vision project actually needs the expensive one."
tags: ["SBC", "Global"]
categories: ["Deep Dive"]
cover:
  image: "/images/posts/embedded-arduino-uno-media-carrier.en.png"
  alt: "Cover card: UNO Media Carrier $19.25, operating range -10 to 60C, 2 MIPI-CSI camera inputs, announced Sept 9"
  relative: false
draft: false
---

Arduino announced the UNO Media Carrier on September 9, an add-on board that snaps onto the dual-brain UNO Q and its higher-end sibling, the VENTUNO Q, to add two camera inputs, a display connector, and audio I/O in one shot. At $19.25 (€19.89 VAT included), it costs far less than the UNO Q itself. The most practical detail in this launch isn't the connectors — it's that the exact same carrier fits both boards, from the $39 entry-level UNO Q up to the $299 VENTUNO Q.

Both host boards were already on the market before this launch. What's new is that Arduino is now shipping an official, documented way to wire a camera and display to either one, rather than leaving builders to source their own MIPI adapters and breakout cables.

## UNO Media Carrier

| Spec | Value |
|---|---|
| Price | $19.25 / €19.89 (VAT incl.) |
| Dimensions | 68.58 × 53.34mm |
| Camera input | Dual MIPI-CSI (two cameras at once) |
| Display | One 22-pin MIPI-DSI connector, supports 5", 8", 10.1" Waveshare touch panels |
| Audio | Three 3.5mm jacks |
| Operating temperature | -10°C to 60°C |
| Power | Drawn from the host board's JMEDIA/JMISC connectors (exact voltage/current TBC) |
| Compatible boards | UNO Q, VENTUNO Q |

It's a pass-through accessory with no power input of its own, so buying one means first picking a host: the UNO Q ($39 for 2GB, $59 for a 4GB variant shipping later this year, prices vary by region) or the VENTUNO Q ($299).

## Same Carrier, Two Very Different Hosts

| Spec | UNO Q | VENTUNO Q |
|---|---|---|
| SoC | Qualcomm QRB2210 (quad-core Cortex-A53, up to 2GHz) | Qualcomm Dragonwing IQ8 |
| Real-time MCU | STM32U585 | STM32H5 |
| RAM/storage | 2GB/16GB or 4GB/32GB | TBC |
| Price | $39 (2GB) / $59 (4GB, shipping later this year) | $299 |
| OS | Debian Linux runs on the Qualcomm side | TBC |
| Media Carrier support | Yes | Yes |

The VENTUNO Q's exact memory configuration and benchmarks weren't disclosed in the sources checked for this piece — that's TBC. What is clear is a $260 price gap between the two boards that use the identical camera/display expansion path.

## What This Means at the Embedded Level

**Power**: The carrier has no separate power input; it pulls current from the host's JMEDIA/JMISC pins. How much of the UNO Q's power budget two live cameras plus a display consume isn't published anywhere we found — worth checking the datasheet directly before putting this on a battery-powered robot.

**Memory**: The base UNO Q ships with 2GB of RAM. Running two MIPI-CSI camera streams simultaneously, let alone adding a vision model on top, could get tight on 2GB — the 4GB variant is the safer pick for camera-heavy builds.

**Thermal**: The board's rated -10°C to 60°C range is a component spec, not a measurement of what happens with two cameras and a display running inside a sealed robot chassis. No real-world thermal data has been published for that scenario.

**Connectors**: MIPI ribbon cables are short and not very tolerant of flexing. Anything mounted on a moving arm or mobile robot will need its own cable strain relief and routing — this carrier doesn't solve that on its own.

## Who Should Buy Which

For hobbyist or educational vision projects, a $39 UNO Q plus a $19.25 carrier covers a camera-and-display setup without spending more. The VENTUNO Q's Dragonwing IQ8 is aimed at heavier on-device AI workloads, so paying $260 more just to plug in a camera doesn't make much sense on its own. If the plan involves real-time video inference or fusing multiple sensor streams, that's where the VENTUNO Q's extra headroom starts to matter.

## Availability

No regional retail or local pricing beyond Arduino's own international store was found for this launch. For now, that means shipping costs and import handling from Arduino's store are part of the real price for buyers outside the US and EU.

## Why This Matters Beyond Arduino

The pattern here — a cheap, official accessory that unlocks camera and display I/O across an entire board lineup rather than just one SKU — is worth watching regardless of what you think of Arduino specifically. It lowers the cost of the first step in any vision or HMI project built on these boards, and it means a maker doesn't have to commit to the priciest SKU in a lineup just to get camera support. Whether Arduino keeps extending that same carrier to future boards, or whether this becomes a one-off for the UNO Q family, isn't something the current announcement answers.

## Verdict

The UNO Media Carrier isn't a technical breakthrough so much as a cheap, well-executed way to expose standard MIPI interfaces. But the fact that the same $19.25 board plugs into both a $39 and a $299 host is the useful takeaway: starting a camera project doesn't require buying the flagship. The numbers that actually matter for putting this into real hardware — power draw and thermal behavior under load — still need to come from a closer read of Arduino's datasheets.
