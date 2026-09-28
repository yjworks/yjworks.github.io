---
title: "RAIDEN beats Jetson Thor by 1.6x, minus the watts"
seoTitle: "EdgeCortix RAIDEN vs NVIDIA Jetson AGX Thor: FP4 PFLOPS, Memory Compared"
date: 2026-09-29T03:15:13+09:00
slug: "embedded-edgecortix-raiden"
summary: "EdgeCortix unveiled RAIDEN, a chiplet platform for robotics and physical AI. We compare its FP4 compute and memory bandwidth against NVIDIA's Jetson AGX Thor, and flag the power figure that's still missing."
tags: ["AI Device", "Robot", "Global"]
categories: ["Deep Dive"]
cover:
  image: "/images/posts/embedded-edgecortix-raiden.en.png"
  alt: "Cover card: RAIDEN X4 delivers 3.36 PFLOPS FP4, 256GB memory, 548GB/s bandwidth, 1.6x Jetson Thor"
  relative: false
draft: false
---

Before you look at PFLOPS, look at watts. A robot arm or a mobile platform has a fixed power budget, and a chip that blows past it is disqualified no matter how fast its benchmark numbers are. This week's announcement leads with the big performance number and leaves that budget blank.

Japanese AI chip startup EdgeCortix unveiled RAIDEN on September 24 in Kanagawa, a chiplet platform built specifically for physical AI — robots, autonomous vehicles, and industrial equipment operating outside the data center, where power and space are both tight.

## The X4 config claims 1.6x Jetson AGX Thor

RAIDEN scales through a modular chiplet design: a single-die X1, a two-die X2, and a four-die flagship X4, all sharing the same DNA-X accelerator architecture and EdgeCortix's MERA software stack.

| Configuration | Peak FP4 compute | Memory | Memory bandwidth | Die-to-die bandwidth |
|---|---|---|---|---|
| RAIDEN X4 (flagship) | 3.36 PFLOPS (3,360 TFLOPS) | up to 256GB | 548GB/s | up to 1.54TB/s |
| Jetson AGX Thor | 2,070 TFLOPS (2.07 PFLOPS) | 128GB LPDDR5X | ~273GB/s | n/a (single die) |

Sources: [EdgeCortix RAIDEN announcement (HPCwire)](https://www.hpcwire.com/off-the-wire/edgecortix-unveils-raiden-a-scalable-energy-efficient-ai-chiplet-platform-for-physical-ai/), [EdgeCortix RAIDEN launch (Embedded.com)](https://www.embedded.com/edgecortix-launches-scalable-raiden-ai-chiplet-platform), [Jetson AGX Thor specs (Waveshare)](https://www.waveshare.com/jetson-agx-thor-developer-kit.htm)

![Bar chart comparing RAIDEN X4 and Jetson AGX Thor on FP4 compute, memory, and bandwidth](/images/posts/embedded-edgecortix-raiden.en-compare.png "The table drawn as bars. RAIDEN X4 leads on all three.")

EdgeCortix didn't publish individual specs for the X1 or X2 tiers — only the X4 flagship got hard numbers. At that top configuration, FP4 compute comes in at roughly 1.6x Jetson AGX Thor, memory capacity is double, and memory bandwidth is about 2x. The four-die design, linked at 1.54TB/s die-to-die, is also a fundamentally different architecture from Thor's single monolithic die.

## The power number is the part that's missing

The announcement describes RAIDEN's power draw only as "configurable power settings." There's no wattage figure for any of the three tiers — not for X1, X2, or the X4 flagship.

Jetson AGX Thor, by contrast, is documented to run in a 40–130W range, with developer kits typically configured between 75W and 120W. That range is what determines heatsink size and battery capacity when you're actually mounting the chip on a robot. Without a comparable number for RAIDEN, you can't yet compute performance-per-watt against Thor — the metric that usually matters more than raw throughput once a chip leaves the data center.

> **Not yet disclosed:** power draw for each configuration (X1/X2/X4), process node, pricing, and the sampling or mass-production timeline. We'll update this post when official figures land.

## Not something a robot builder can buy today

Jetson AGX Thor ships as a developer kit you can order through retail channels. RAIDEN, at announcement, is a chiplet platform EdgeCortix supplies to robot and equipment manufacturers — not a board an individual or small team can drop into a project right now. The performance and memory numbers are real, but treating RAIDEN as a ready alternative to Jetson would be premature.

Multi-die chiplet designs like this tend to land first in larger robots and industrial equipment where power headroom isn't the constraint it is on battery-powered platforms. Until a wattage figure ships, Jetson-class boards remain the practical choice for smaller, battery-run robots and hobbyist projects.

## What to watch next is supply, not the spec sheet

On paper, RAIDEN posts numbers that stand out among physical-AI chips. But whether it actually belongs in a robot depends on power draw, process node, supply timeline, and whether a buyable board ever appears — none of which are public yet. Until then, the announced figures alone aren't enough to call it a Jetson AGX Thor alternative.
