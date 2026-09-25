---
title: "Robot and Edge AI Boards: Which One Fits"
seoTitle: "Edge AI and Robot Boards 2026: Jetson Orin Nano 2, Arduino UNO Q, VENTUNO Q, Pico 2"
date: 2026-09-25T09:39:05+09:00
lastmod: 2026-09-25T09:39:05+09:00
slug: "edge-ai-boards"
summary: "Jetson Orin Nano 2 and Orin Nano Super, Arduino UNO Q and VENTUNO Q, YuzukiNeko, and Raspberry Pi Pico 2 in one table: compute, memory, power, and price. Updated when a new board ships."
tags: ["SBC", "Robot"]
hubTags: ["SBC", "Robot"]
cover:
  image: "/images/posts/guide-edge-ai-boards.en.png"
  alt: "Guide card: six boards, priced from $5 to $299, up to 78 TOPS, Orin Nano 2 shipping first half of 2027"
  relative: false
---
A spec sheet rarely settles which board belongs in a robot or a vision rig. The power budget and the memory ceiling usually bite before raw compute does. This page collects every board DigitalBrain has covered into one table and gets updated when a new one ships. Every number comes from the sources in the linked deep dives; anything we couldn't confirm is marked TBC.

## At a glance

| Board | Compute | Memory | Power (official) | Price | Status |
|---|---|---|---|---|---|
| NVIDIA Jetson Orin Nano 2 | 8-core Arm Cortex-A78, Ampere GPU (1,536 CUDA cores), 78 TOPS | 8GB LPDDR5X, 120GB/s | 15–40W | TBC (not announced) | Ships first half of 2027 |
| NVIDIA Jetson Orin Nano Super Developer Kit | 6-core Arm Cortex-A78AE, Ampere GPU (1,024 CUDA cores), 67 TOPS | 8GB LPDDR5, 102GB/s | 7–25W | $249 | On sale |
| Arduino VENTUNO Q | Qualcomm Dragonwing IQ8 + STM32H5 | 16GB LPDDR5 / 64GB eMMC | TBC | $299 (introductory pre-order) | Pre-order |
| Arduino UNO Q | Qualcomm QRB2210 (quad-core Cortex-A53) + STM32U585 | 2GB/16GB or 4GB/32GB | TBC | $59 (2GB) / $79 (4GB) | On sale |
| YuzukiNeko | Allwinner F101S3 (one XuanTie C907 RISC-V core, 1.008GHz) | 16MiB PSRAM | TBC | TBC | Not yet on sale |
| Raspberry Pi Pico 2 | RP2350 (2× Cortex-M33 + 2× Hazard3 RISC-V, 150MHz) | 520KiB SRAM | TBC | $5 | On sale |

Sources: [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-jetson-orin-nano-2-robotics-computer-to-redefine-entry-level-edge-ai), [SparkFun (Orin Nano Super Developer Kit)](https://www.sparkfun.com/nvidia-jetson-orin-nano-developer-kit.html), [CNX Software (VENTUNO Q)](https://www.cnx-software.com/2026/08/25/299-arduino-ventuno-q-sbc-combines-qualcomm-dragonwing-iq8-soc-and-stm32h5-mcu/), [Arduino Blog (UNO Q pricing)](https://blog.arduino.cc/2026/06/26/a-heads-up-on-the-arduino-uno-q-board-pricing-straight-from-marcello-majonchi/), [CNX Software (YuzukiNeko)](https://www.cnx-software.com/2026/09/08/yuzukineko-a-linux-capable-allwinner-f101-64-bit-risc-v-sbc-with-raspberry-pi-pico-form-factor/), [Raspberry Pi (Pico 2)](https://www.raspberrypi.com/news/raspberry-pi-pico-2-our-new-5-microcontroller-board-on-sale-now/)

The first four are Linux computers; the Pico 2 is a microcontroller; YuzukiNeko sits in between, running Linux in a Pico-sized footprint. They share a table, not a job.

## Start from what you're building

- **Real-time motor and sensor control at the lowest cost**: Raspberry Pi Pico 2. $5, always in stock, and you can start in bare metal, MicroPython, or CircuitPython.
- **Linux and a display output in a Pico footprint**: YuzukiNeko, but it isn't on sale and has no price yet, so it's not something to design in today.
- **A hobby or classroom vision project with a camera and screen**: Arduino UNO Q 4GB plus the [UNO Media Carrier](/en/2026/09/23/embedded-arduino-uno-media-carrier/) ($19.25). If you plan to run two cameras and a vision model together, 4GB is the safer pick over 2GB.
- **Heavy on-device AI and a real-time MCU on one board**: Arduino VENTUNO Q. It takes the same carrier as the UNO Q, so if all you need is a camera, the extra $240 is hard to justify.
- **A CUDA-based vision or robotics stack right now**: Jetson Orin Nano Super. The Orin Nano 2 doesn't ship until the first half of 2027.

## Before a board goes into a robot

**Power budget.** The Jetson Orin Nano 2 tops out at 40W, 15W more than the Orin Nano Super's 25W. A power rail and heatsink sized for 25W won't let you use its top mode. For the other boards we haven't confirmed official power figures here; if you're running on batteries, pull the numbers from the manufacturer's datasheet.

**Memory ceiling.** Both Jetsons have 8GB. The newer one gains bandwidth (102 to 120GB/s) and CUDA cores, not room for bigger models.

**Connectors and cables.** Setups built on MIPI ribbon cables, like the UNO Media Carrier, need their own cable anchoring and strain relief on anything that moves or vibrates.

## Deep dives

- [Jetson Orin Nano 2: the 2x that isn't](/en/2026/09/02/embedded-jetson-orin-nano-2/): the new module against the Orin Nano Super, power floor and memory
- [For a Camera Add-On, Skip the $299 VENTUNO Q](/en/2026/09/23/embedded-arduino-uno-media-carrier/): the UNO Media Carrier and both boards
- [YuzukiNeko, Pico's Size With a Linux Brain](/en/2026/09/09/embedded-yuzukineko-risc-v-pico/): a RISC-V Linux board against the Pico 2

## Update log

- 2026-09-25: First version. Six boards.
