---
title: "로봇·엣지 AI 보드, 무엇을 고를까"
seoTitle: "엣지 AI·로봇 보드 비교 2026: Jetson Orin Nano 2·아두이노 우노Q·벤투노Q·피코 2·VIEWE ESP32-S31"
date: 2026-09-25T09:39:05+09:00
lastmod: 2026-11-27T03:06:24+09:00
slug: "edge-ai-boards-update"
updateOf: "edge-ai-boards"
summary: "Jetson Orin Nano 2와 Orin Nano Super, 아두이노 우노Q·벤투노Q, 유즈키네코, 라즈베리파이 피코 2, VIEWE ESP32-S31 터치 보드를 연산 칩·메모리·전력·가격 기준으로 한 표에 모았습니다. 새 보드가 나오면 갱신합니다."
tags: ["SBC", "Robot"]
hubTags: ["SBC", "Robot"]
cover:
  image: "/images/posts/guide-edge-ai-boards-update.ko.png"
  alt: "비교 가이드 카드: 보드 7종, 가격 5달러부터 299달러, 최대 78 TOPS, Orin Nano 2 출하 2027년 상반기"
  relative: false
---
로봇이나 비전 장비에 올릴 보드를 고를 때 스펙표 한 장으로는 답이 안 나옵니다. 연산 성능보다 전원 예산과 메모리 한계가 먼저 발목을 잡는 경우가 많기 때문입니다. 이 페이지는 DigitalBrain에서 다룬 보드를 한 표에 모으고, 새 보드가 나오면 표와 판단 기준을 갱신합니다. 수치는 모두 각 심층 글의 출처에서 확인된 것이고, 확인되지 않은 칸은 "확인 필요"로 둡니다.

## 한눈에 비교

| 보드 | 연산 칩 | 메모리 | 전력(공식) | 가격 | 상태 |
|---|---|---|---|---|---|
| NVIDIA Jetson Orin Nano 2 | 8코어 Arm Cortex-A78, Ampere GPU(CUDA 1,536), 78 TOPS | 8GB LPDDR5X, 120GB/s | 15~40W | 확인 필요(미발표) | 2027년 상반기 출하 예정 |
| NVIDIA Jetson Orin Nano Super 개발자 키트 | 6코어 Arm Cortex-A78AE, Ampere GPU(CUDA 1,024), 67 TOPS | 8GB LPDDR5, 102GB/s | 7~25W | 249달러 | 판매 중 |
| 아두이노 벤투노Q | Qualcomm Dragonwing IQ8 + STM32H5 | 16GB LPDDR5 / 64GB eMMC | 확인 필요 | 299달러(사전 주문 도입가) | 사전 주문 |
| 아두이노 우노Q | Qualcomm QRB2210(쿼드코어 Cortex-A53) + STM32U585 | 2GB/16GB 또는 4GB/32GB | 확인 필요 | 59달러(2GB) / 79달러(4GB) | 판매 중 |
| 유즈키네코 | Allwinner F101S3(XuanTie C907 RISC-V 1코어, 1.008GHz) | PSRAM 16MiB | 확인 필요 | 미정 | 판매 전 |
| VIEWE ESP32-S31 4.3인치 터치 보드 | ESP32-S31(듀얼코어 RISC-V, 320MHz), Wi-Fi 6·블루투스 5.4·802.15.4 | SRAM 512KB, PSRAM 16MB, 플래시 16MB | USB 5V 또는 DC 7~24V 입력, 5V 기준 보통 320mA(백라이트 최대 500mA). 칩 소비전력은 확인 필요 | 38.99달러 | 판매 중 |
| 라즈베리파이 피코 2 | RP2350(Cortex-M33·Hazard3 RISC-V 각 2코어, 150MHz) | SRAM 520KiB | 확인 필요 | 5달러 | 판매 중 |

출처: [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-jetson-orin-nano-2-robotics-computer-to-redefine-entry-level-edge-ai), [SparkFun(Orin Nano Super 개발자 키트)](https://www.sparkfun.com/nvidia-jetson-orin-nano-developer-kit.html), [CNX Software(벤투노Q)](https://www.cnx-software.com/2026/08/25/299-arduino-ventuno-q-sbc-combines-qualcomm-dragonwing-iq8-soc-and-stm32h5-mcu/), [Arduino 블로그(우노Q 가격 조정)](https://blog.arduino.cc/2026/06/26/a-heads-up-on-the-arduino-uno-q-board-pricing-straight-from-marcello-majonchi/), [CNX Software(유즈키네코)](https://www.cnx-software.com/2026/09/08/yuzukineko-a-linux-capable-allwinner-f101-64-bit-risc-v-sbc-with-raspberry-pi-pico-form-factor/), [Raspberry Pi(피코 2)](https://www.raspberrypi.com/news/raspberry-pi-pico-2-our-new-5-microcontroller-board-on-sale-now/), [VIEWE 제품 보드 GitHub](https://github.com/VIEWESMART/PLCM-UES31S043H800V480C-U), [CNX Software(VIEWE ESP32-S31 보드)](https://www.cnx-software.com/2026/10/14/viewe-4-3-inch-esp32-s31-display-development-board/), [VIEWE 제품 페이지](https://viewedisplay.com/product/4-3-inch-800x480-esp32-s31-wifi6-touch-smart-hmi-uart-display/)

위의 네 보드는 리눅스가 도는 컴퓨터이고, VIEWE 보드와 피코 2는 마이크로컨트롤러 계열입니다. 유즈키네코는 피코와 같은 크기에 리눅스를 올린 중간 지점입니다. 같은 표에 두었지만 같은 일을 하는 보드는 아닙니다.

## 무엇을 하려는지부터 정합니다

- **모터·센서를 실시간으로 제어하고 가장 싸게 끝내고 싶다** → 라즈베리파이 피코 2. 5달러에 상시 구매할 수 있고, 베어메탈·MicroPython·CircuitPython으로 바로 시작합니다.
- **터치 화면과 Wi-Fi 6가 필요한 장비 패널(HMI)을 한 보드로** → VIEWE ESP32-S31 4.3인치 보드. 38.99달러에 24V 장비 전원에서 바로 구동하고 RS485·CAN이 기판에 올라와 있습니다. 다만 예제가 ESP-IDF master와 `--preview` 플래그를 요구하는 단계라 양산 설계는 안정 릴리스 지원 뒤가 안전합니다.
- **피코 크기에 리눅스와 디스플레이 출력이 필요하다** → 유즈키네코. 다만 아직 판매 전이고 가격도 미정이라, 지금 설계에 넣을 보드는 아닙니다.
- **카메라·디스플레이를 붙인 교육용·취미용 비전 프로젝트** → 아두이노 우노Q 4GB에 [우노 미디어 캐리어](/2026/09/23/embedded-arduino-uno-media-carrier/)(19.25달러). 카메라 두 대와 비전 모델을 같이 돌릴 계획이면 2GB보다 4GB가 안전합니다.
- **무거운 온디바이스 AI와 실시간 MCU를 한 보드에** → 아두이노 벤투노Q. 우노Q와 캐리어 호환은 같으므로, 카메라를 붙이는 것만이 목적이라면 240달러를 더 낼 이유는 약합니다.
- **CUDA 기반 비전·로봇 스택을 지금 당장** → Jetson Orin Nano Super. Orin Nano 2는 2027년 상반기 출하라 지금 살 수 있는 선택지가 아닙니다.

## 보드를 로봇에 올리기 전에 확인할 것

**전원 예산.** Jetson Orin Nano 2의 최대 모드는 40W로, 현행 Orin Nano Super의 25W보다 15W 높습니다. 기존 25W 기준으로 설계한 전원 레일과 방열을 그대로 쓰면 최대 성능 모드를 쓸 수 없습니다. 나머지 보드는 공식 소비전력 수치를 이 페이지 기준으로 확인하지 못했습니다. 배터리로 구동한다면 제조사 데이터시트에서 직접 확인해야 합니다.

**메모리 한계.** Jetson은 신형과 현행 모두 8GB입니다. 신형의 향상은 대역폭(102→120GB/s)과 CUDA 코어 수에서 오고, 올릴 수 있는 모델 크기는 늘지 않습니다.

**커넥터와 케이블.** 우노 미디어 캐리어처럼 MIPI 리본 케이블을 쓰는 구성은 진동이 있는 이동체에서 케이블 고정과 스트레인 릴리프를 따로 설계해야 합니다.

## 심층 글

- [ESP32-S31 첫 보드, 5V만 보면 안 되고 7~24V도 들어옵니다](/2026/11/06/embedded-viewe-esp32-s31-display/) — VIEWE 4.3인치 보드, 전원·RS485·CAN
- [Jetson Orin Nano 2, 두 배는 두 배가 아니다](/2026/09/02/embedded-jetson-orin-nano-2/) — 신형과 Orin Nano Super 스펙 비교, 전력 하한과 메모리
- [카메라엔 우노Q, 벤투노Q는 과하다](/2026/09/23/embedded-arduino-uno-media-carrier/) — 우노 미디어 캐리어와 두 보드
- [유즈키네코, 피코 크기에 리눅스 두뇌](/2026/09/09/embedded-yuzukineko-risc-v-pico/) — RISC-V 리눅스 보드와 피코 2 비교

## 업데이트 기록

- 2026-11-27: VIEWE ESP32-S31 4.3인치 터치 보드 추가(보드 7종). 장비 패널용 선택지와 전원 항목 반영.
- 2026-09-25: 첫 작성. 보드 6종.
