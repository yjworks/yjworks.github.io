---
title: "Epson AX6: a 6 kg cobot that takes 48 V straight"
seoTitle: "Epson AX6 Cobot Specs vs UR5e: Payload, Reach, Weight, 48 V DC, Price"
date: 2026-09-30T04:24:22+09:00
slug: "embedded-epson-ax6"
summary: "Epson's first collaborative robot, the AX6, pairs a 6 kg payload and 900 mm reach with a 17 kg arm and 48 V DC input. We compare it with the UR5e and list what you still need to know before putting it on a battery-powered AMR."
tags: ["Robot", "Global"]
categories: ["Deep Dive"]
cover:
  image: "/images/posts/embedded-epson-ax6.en.png"
  alt: "Cover card: Epson AX6 with 6 kg payload, 900 mm reach, 17 kg arm weight and 48 V DC input"
  relative: false
draft: false
---

If you want to put a robot arm on a mobile robot, the first thing that bites is not payload but power. Most arms run from an AC-fed controller, so a battery-powered base needs an inverter in between just to feed the arm. Epson's new AX6 goes straight at that problem.

Epson Robots added the AX6, its first collaborative robot, to its six-axis line on September 22 (US). It is force- and power-limited, so with a proper risk assessment it can work next to people without safety fencing, and it accepts **48 V DC** as well as 100–240 V AC.

## At a glance: one size up from a UR5e, and 3 kg lighter

| | Epson AX6 | Universal Robots UR5e |
|---|---|---|
| Payload | 6 kg | 5 kg |
| Reach | 900 mm | 850 mm |
| Arm weight | 17 kg | 20.6 kg (incl. cable) |
| Repeatability | 0.03 mm | ±0.03 mm |
| Protection / cleanroom | IP54, ISO 14644-1 Class 5 | — |
| Power input | 100–240 V AC, 48 V DC | — |
| Max power draw | — | 570 W |
| Controller | RC-A1010 | — |
| Price | from €14,995 (Europe) | — |

Sources: [Epson US press release](https://news.epson.com/news/ax6-6-axis-collaborative-robot), [RoboticsTomorrow](https://www.roboticstomorrow.com/news/2026/09/22/epson-now-offers-complete-portfolio-of-robotic-safety-tools-with-introduction-of-first-collaborative-robot/27134/), [The Robot Report](https://www.therobotreport.com/epson-introduces-ax6-cobot-compact-design-no-code-programming/), [Epson Europe AX6 page](https://www.epson.eu/en_EU/robots/cobot-ax6), [AI Matters (Korean)](https://aimatters.co.kr/news-report/53196/), [UR5e datasheet](https://www.universal-robots.com/media/1807465/ur5e_e-series_datasheets_web.pdf)

> **Not yet disclosed:** the AX6's maximum power draw, the accepted voltage range and peak current on the 48 V input, the size and weight of the RC-A1010 controller, and Korean pricing and availability. We'll update this post when they are.

![The Epson AX6 carries 6 kg against the UR5e's 5 kg and reaches 900 mm against 850 mm](/images/posts/embedded-epson-ax6.en-compare.png "The table as bars. In the same class, the AX6 is slightly ahead on payload and reach.")

On the published numbers, the AX6 sits in the same class as the UR5e with 1 kg more payload and 50 mm more reach, while the arm is more than 3 kg lighter; Epson credits a carbon-fibre structure. Repeatability is 0.03 mm on both.

## Why 48 V DC matters on a mobile base

Many AMRs run on 48 V battery systems. An arm that takes 48 V DC directly lets you drop the inverter from the battery → inverter → controller chain, which removes a conversion loss, a box and a heat source. According to AI Matters, Epson also designed the AX6 with AMR mounting in mind.

Three numbers are still missing before anyone should finalise the wiring:

- **Accepted input range.** A 48 V lithium pack swings a long way between full and empty. How far the AX6 tolerates that swing is not published; if the window is narrow, you are back to adding a DC-DC stage.
- **Peak current.** Arms draw far more than their average during acceleration. If the drive motors and the arm accelerate at the same time on one pack, the bus can sag. You need the peak figure to size the battery's discharge rating and the fusing.
- **Grounding and e-stop.** Once base and arm share a supply, the emergency-stop chain and grounding have to be designed as one system. Cobot certification covers the arm alone; the combined AMR needs its own risk assessment.

## Budget the gripper out of the 6 kg

The 6 kg includes everything on the flange: gripper, camera, tool changer. Epson uses an ISO 50 flange so third-party grippers, suction cups and cameras bolt on directly. With 1.5–2 kg of electric gripper and camera, the usable part weight is closer to 4 kg. There is only one AX6 model for now, so heavier parts mean looking elsewhere.

## No-code setup, with a Python escape hatch

Setup runs in a web browser without code, and there is also a customisable Python environment for uploading your own libraries and modules, plus a 3D simulator. That suits labs and classrooms that want to wire in vision models from Python. Whether Epson ships an official ROS 2 driver is not stated in the launch material.

## Who should look at it first

The AX6 stands out less for its spec table than for the combination of 48 V DC input and a 17 kg arm. For a battery-powered base, it is the first arm worth shortlisting, because the inverter can go. Just don't lock the battery design until Epson publishes the input range and peak current.

For a fixed cell on the factory floor, the performance gap to established arms such as the UR5e is small on paper, so compare price, accessories and local support before switching.
