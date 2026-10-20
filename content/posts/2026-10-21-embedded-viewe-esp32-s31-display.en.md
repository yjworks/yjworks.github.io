---
title: "The First ESP32-S31 Board Takes 5V — and Also 7–24V"
seoTitle: "VIEWE ESP32-S31 4.3-inch Board vs ESP32-S3: Wi-Fi 6, RS485, CAN, 7–24V Power"
date: 2026-10-21T03:08:00+09:00
slug: "embedded-viewe-esp32-s31-display"
summary: "Display maker VIEWE is selling a 4.3-inch touch dev board built on Espressif's new ESP32-S31 for $38.99. We look at what changed from the ESP32-S3 and what matters when you wire it into equipment: power input, RS485 and CAN."
tags: ["SBC", "Global"]
categories: ["Deep Dive"]
cover:
  image: "/images/posts/embedded-viewe-esp32-s31-display.en.png"
  alt: "Cover card: VIEWE ESP32-S31 4.3-inch board $38.99, 320 MHz dual-core RISC-V, 16 MB PSRAM, 7–24V DC input"
  relative: false
draft: true
---

If you have been building touchscreen products on the ESP32-S3, the obvious question about a new board is how much faster the chip is. On this one the more useful detail is that 5V from USB is not the only way to power it.

VIEWE began selling the 4.3-inch 800×480 touch board (PLCM-UES31S043H800V480C-U) around October 14 for $38.99. It is reported as the first third-party board built on the ESP32-S31 module.

## What changed in the chip: mostly radios

| Item | ESP32-S31 (VIEWE board) | ESP32-S3 |
|---|---|---|
| CPU | Dual-core RISC-V, up to 320 MHz | Dual-core Xtensa LX7, up to 240 MHz |
| Internal SRAM | 512 KB | 512 KB |
| External memory on this board | 16 MB PSRAM, 16 MB flash | — |
| Wi-Fi | 2.4 GHz Wi-Fi 6 | 2.4 GHz Wi-Fi 4 |
| Bluetooth | 5.4 LE + Classic | 5 LE |
| 802.15.4 (Thread, Zigbee) | Yes | No |
| Price | $38.99 | — |

Sources: [VIEWE board GitHub](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U), [CNX Software on the VIEWE board](https://www.cnx-software.com/2026/10/14/viewe-4-3-inch-esp32-s31-display-development-board/), [VIEWE product page](https://viewedisplay.com/product/4-3-inch-800x480-esp32-s31-wifi6-touch-smart-hmi-uart-display/), [S3 comparison (Hubtronics)](https://hubtronics.in/learn/esp32-s3-s31-comparison-guide)

> **Not yet disclosed:** Korean retailers and pricing, and datasheet-level power draw. Much of the chip comparison comes from secondary sources and should be checked against the datasheet.

## Power: USB 5V or 7–24V DC, chosen by a jumper

The GitHub page says power comes from USB-C 5V or a DCIN input of 7–24V, selected with a jumper cap. At 5V it draws 320 mA typical and 500 mA at full backlight, and 100 mA with the backlight off. That lets the panel sit next to 24V equipment without an extra regulator. The USB-A host port supplies only about 500 mA at 5V.

## RS485 and CAN are on the board

RS485 uses a SIT3088E and CAN uses a SIT1050T, both with 120 Ω termination. Defaults are 115200 8N1 for RS485 and classic CAN at 500 kbit/s. One catch: header pins GPIO35/36 and GPIO53/54 are wired in parallel with those transceivers, so do not drive the terminal and the header at once.

## Software is still thin

The 18 ESP-IDF examples are Apache-2.0, but they need ESP-IDF master with the `--preview` flag, and there are no Arduino or PlatformIO examples yet. For a shipping product, wait for stable release support. For trying Wi-Fi 6 and Thread on one chip, $38.99 is a small bet.
