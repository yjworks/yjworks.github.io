---
title: "ESP32-S31 첫 보드, 5V만 보면 안 되고 7~24V도 들어옵니다"
seoTitle: "VIEWE ESP32-S31 4.3인치 보드 스펙 비교: ESP32-S3 대비 Wi-Fi 6·RS485·CAN"
date: 2026-10-21T03:08:00+09:00
slug: "embedded-viewe-esp32-s31-display"
summary: "디스플레이 업체 VIEWE가 에스프레소프의 새 칩 ESP32-S31을 올린 4.3인치 터치 개발 보드를 38.99달러에 내놨습니다. ESP32-S3와 무엇이 달라졌는지, 전원과 RS485·CAN 같은 장비 연결 관점에서 무엇을 확인해야 하는지 정리했습니다."
tags: ["SBC", "Global"]
categories: ["Deep Dive"]
cover:
  image: "/images/posts/embedded-viewe-esp32-s31-display.ko.png"
  alt: "커버 카드: VIEWE ESP32-S31 4.3인치 보드 38.99달러, 320MHz 듀얼코어 RISC-V, 16MB PSRAM, 7~24V DC 입력"
  relative: false
draft: true
---

ESP32-S3로 터치 패널 제품을 만들던 사람이 새 보드를 고를 때 먼저 묻는 것은 "칩이 얼마나 빨라졌나"일 겁니다. 이 보드에서는 그보다 "5V 하나로 끝나지 않는다"는 점이 눈에 띕니다.

VIEWE가 10월 14일 전후로 ESP32-S31 모듈을 올린 4.3인치 800×480 터치 개발 보드(PLCM-UES31S043H800V480C-U)를 38.99달러에 팔기 시작했습니다. 공개된 자료로는 이 칩을 쓴 첫 서드파티 보드로 보도됐습니다.

## 칩이 바뀐 부분: 무선이 가장 크게 늘었습니다

| 항목 | VIEWE 보드의 ESP32-S31 | ESP32-S3 |
|---|---|---|
| CPU | 듀얼코어 RISC-V, 최대 320MHz | 듀얼코어 Xtensa LX7, 최대 240MHz |
| 내장 SRAM | 512KB | 512KB |
| 이 보드의 외장 메모리 | PSRAM 16MB, 플래시 16MB | — |
| Wi-Fi | 2.4GHz Wi-Fi 6 | 2.4GHz Wi-Fi 4 |
| 블루투스 | 5.4 LE + Classic | 5 LE |
| 802.15.4(Thread·Zigbee) | 지원 | 미지원 |
| 가격 | $38.99 | — |

출처: [VIEWE 제품 보드 GitHub](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U), [VIEWE 4.3인치 ESP32-S31 보드 기사(CNX Software)](https://www.cnx-software.com/2026/10/14/viewe-4-3-inch-esp32-s31-display-development-board/), [VIEWE 제품 페이지](https://viewedisplay.com/product/4-3-inch-800x480-esp32-s31-wifi6-touch-smart-hmi-uart-display/), [ESP32-S3 대비 비교(Hubtronics)](https://hubtronics.in/learn/esp32-s3-s31-comparison-guide)

> **아직 공개되지 않은 것:** 국내 판매처와 국내 가격, 공식 데이터시트 기준 소비전력. 이 글의 칩 비교는 2차 자료가 많아 데이터시트로 다시 확인해야 합니다.

## 전원은 USB 5V와 DC 7~24V 중 점퍼로 고릅니다

GitHub 문서에 따르면 USB-C 5V 또는 DCIN 7~24V를 점퍼 캡으로 선택합니다. 5V 기준 전류는 보통 320mA, 백라이트 최대에서 500mA이고 백라이트를 끄면 100mA입니다. 24V 장비 패널 옆에 바로 달 수 있다는 뜻이라, 레귤레이터 하나를 덜 붙여도 됩니다. 다만 USB-A 호스트 포트는 5V 약 500mA까지만 내줍니다.

## RS485와 CAN이 기판에 올라와 있습니다

RS485는 SIT3088E, CAN은 SIT1050T 트랜시버를 쓰고 둘 다 120Ω 종단이 있습니다. CAN은 클래식 500kbit/s, RS485는 115200 8N1이 기본입니다. 주의할 점은 20핀 헤더의 GPIO35/36, GPIO53/54가 이 트랜시버와 병렬이라는 것입니다. 터미널과 헤더를 동시에 구동하면 안 됩니다.

## 지금 쓰기에는 소프트웨어가 아직 얇습니다

ESP-IDF 예제 18개가 Apache-2.0으로 공개돼 있지만, 예제는 ESP-IDF master와 `--preview` 플래그가 필요하고 Arduino·PlatformIO 예제는 아직 없습니다. 양산 제품이라면 안정 릴리스 지원이 붙을 때까지 기다리는 쪽이 안전합니다. 반대로 Wi-Fi 6와 Thread를 한 칩에서 시험해 보려는 개발용이라면 38.99달러는 부담이 작습니다.
