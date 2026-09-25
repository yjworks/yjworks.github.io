---
title: "카메라엔 우노Q, 벤투노Q는 과하다"
seoTitle: "아두이노 우노 미디어 캐리어: 우노Q vs 벤투노Q 카메라 프로젝트 비교"
date: 2026-09-23T03:12:53+09:00
lastmod: 2026-09-25T10:06:19+09:00
updates:
  - date: "2026-09-25"
    text: "우노Q 가격을 $39(2GB)·$59(4GB)에서 7월 6일 인상 후 가격 $59·$79로 고쳤습니다. 4GB 모델은 이미 판매 중입니다."
  - date: "2026-09-25"
    text: "벤투노Q 메모리(16GB/64GB)와 OS를 채우고, 두 보드 가격 차이를 $240으로 고쳤습니다."
  - date: "2026-09-25"
    text: "빠져 있던 출처 링크를 추가했습니다."
slug: "embedded-arduino-uno-media-carrier"
summary: "아두이노가 우노Q와 벤투노Q에 카메라·디스플레이·오디오를 붙여주는 19.25달러짜리 확장보드 '우노 미디어 캐리어'를 내놨습니다. 두 보드에 똑같이 꽂히는 만큼, 카메라 프로젝트에 굳이 비싼 쪽을 살 필요가 있는지 따져봤습니다."
tags: ["SBC", "Global"]
categories: ["Deep Dive"]
cover:
  image: "/images/posts/embedded-arduino-uno-media-carrier.ko.png"
  alt: "커버 카드: 우노 미디어 캐리어 19.25달러, 동작온도 -10~60℃, MIPI-CSI 카메라 입력 2개, 9월 9일 발표"
  relative: false
draft: false
---

아두이노(Arduino)가 9월 9일 '우노 미디어 캐리어(UNO Media Carrier)'를 공개했습니다. 듀얼 브레인 보드 우노Q(UNO Q)와 상위 모델 벤투노Q(VENTUNO Q) 위에 그대로 얹으면 카메라 2개, 디스플레이, 오디오 입출력을 한 번에 붙일 수 있는 확장보드입니다. 가격은 19.25달러(부가세 포함 유럽가 19.89유로)로, 우노Q 본체보다 훨씬 저렴합니다. 두 보드 모두에 같은 캐리어가 꽂힌다는 점이 이번 발표에서 가장 실용적인 대목입니다.

## 우노 미디어 캐리어

| 항목 | 사양 |
|---|---|
| 가격 | $19.25 / €19.89(VAT 포함) |
| 크기 | 68.58 × 53.34mm |
| 카메라 입력 | MIPI-CSI 2개(듀얼 카메라 동시 연결) |
| 디스플레이 | 22핀 MIPI-DSI 1개, Waveshare 5·8·10.1인치 터치 디스플레이 지원 |
| 오디오 | 3.5mm 잭 3개 |
| 동작 온도 | -10°C ~ 60°C |
| 전원 공급 | 호스트 보드의 JMEDIA·JMISC 커넥터를 통해 공급(전압·전류 수치는 확인 필요) |
| 호환 보드 | 우노Q, 벤투노Q |

출처: [Arduino 공식 스토어](https://store-usa.arduino.cc/products/uno-media-carrier), [Arduino 문서](https://docs.arduino.cc/hardware/uno-media-carrier/), [CNX Software](https://www.cnx-software.com/2026/09/10/arduino-uno-media-carrier-adds-mipi-csi-dsi-and-audio-connectors-to-uno-q-and-ventuno-q-boards/), [Electronics For You](https://www.electronicsforu.com/news/uno-media-carrier-adds-camera-display-audio-i-o)

호스트 보드 없이는 동작하지 않는 순수 확장보드라서, 실제 구매는 우노Q(2GB $59 / 4GB $79, 국가별로 약간 다름)나 벤투노Q($299) 중 하나를 먼저 골라야 합니다.

## 우노Q와 벤투노Q, 캐리어는 같다

| 항목 | 우노Q | 벤투노Q |
|---|---|---|
| SoC | Qualcomm QRB2210(쿼드코어 Cortex-A53, 최대 2GHz) | Qualcomm Dragonwing IQ8 |
| 실시간 MCU | STM32U585 | STM32H5 |
| RAM/스토리지 | 2GB/16GB 또는 4GB/32GB | 16GB LPDDR5 / 64GB eMMC |
| 가격 | $59(2GB) / $79(4GB), 7월 6일 인상 기준 | $299(사전 주문 도입가) |
| 운영체제 | Qualcomm 측이 데비안 리눅스 구동 | Qualcomm 측 우분투·데비안 |
| 미디어 캐리어 호환 | O | O |

출처: [Arduino 블로그(UNO Q 가격 조정)](https://blog.arduino.cc/2026/06/26/a-heads-up-on-the-arduino-uno-q-board-pricing-straight-from-marcello-majonchi/), [Arduino 블로그(UNO Q 4GB 출시)](https://blog.arduino.cc/2026/01/20/arduino-uno-q-is-now-available-with-4gb-ram-and-32gb-storage/), [CNX Software(UNO Q 4GB)](https://www.cnx-software.com/2026/01/21/arduino-uno-q-4gb-board-with-4gb-ram-32gb-storage-available-59/), [CNX Software(벤투노Q)](https://www.cnx-software.com/2026/08/25/299-arduino-ventuno-q-sbc-combines-qualcomm-dragonwing-iq8-soc-and-stm32h5-mcu/), [Notebookcheck(벤투노Q)](https://www.notebookcheck.net/Qualcomm-unveils-Arduino-Ventuno-Q-single-board-computer-for-physical-AI-projects-with-Dragonwing-IQ8-SoC-16-GB-LPDDR5-RAM-and-64-GB-eMMC.1243587.0.html), [Circuit Digest(벤투노Q)](https://circuitdigest.com/news/arduino-ventuno-q-opens-pre-orders-at-299-with-dual-brain-architecture-and-40-tops-ai)

벤투노Q의 벤치마크는 이번 조사에서 원문에 나오지 않아 확인이 필요합니다. 다만 가격 차이가 240달러에 달하는데도 카메라·디스플레이 확장 방식은 동일하다는 점은 분명합니다.

## 임베디드 관점에서 본 것

**전원**: 캐리어는 자체 전원 커넥터 없이 호스트의 JMEDIA·JMISC 핀에서 전력을 끌어옵니다. 카메라 2개와 디스플레이를 동시에 물리면 우노Q 본체의 전원 예산을 얼마나 잡아먹는지, 정확한 전압·전류 수치는 공개 자료에 없어 확인이 필요합니다. 배터리로 로봇에 올릴 계획이라면 이 부분을 데이터시트로 직접 확인해야 합니다.

**메모리**: 우노Q의 기본 구성은 2GB RAM입니다. MIPI-CSI 카메라 2개를 동시에 띄우고 여기에 비전 모델까지 얹으려면 2GB로는 빠듬할 수 있어, 카메라 중심 프로젝트라면 4GB 모델을 고르는 편이 안전합니다.

**발열**: 동작 온도 범위는 -10~60°C로 명시돼 있지만, 이는 보드 자체 스펙이고 카메라·디스플레이를 동시에 구동하며 밀폐된 로봇 섀시 안에 넣었을 때의 실측 발열 데이터는 공개되지 않았습니다.

**커넥터**: MIPI 리본 케이블은 길이가 짧고 구부림에 약한 편이라, 로봇 팔이나 이동체처럼 진동이 있는 장비에 올릴 때는 케이블 고정과 커넥터 스트레스 릴리프를 별도로 설계해야 합니다.

## 어떤 프로젝트에 맞을까

카메라·디스플레이가 필요한 취미·교육용 비전 프로젝트라면 59달러짜리 우노Q에 19.25달러 캐리어만 더해도 충분합니다. 벤투노Q의 Dragonwing IQ8은 더 무거운 온디바이스 AI 연산을 노리는 제품이라, 단순히 카메라를 붙이고 싶은 목적이라면 240달러를 더 낼 이유가 약합니다. 반대로 실시간 영상 추론이나 다중 센서 융합처럼 연산량이 큰 작업을 계획 중이라면 벤투노Q 쪽이 맞습니다.

## 국내 출시 여부

아두이노 공식 스토어를 통한 해외 직배송 외에 국내 정식 유통이나 국내 가격 공지는 확인되지 않았습니다.

## 총평

우노 미디어 캐리어 자체는 특별한 기술이라기보다 검증된 MIPI 인터페이스를 저렴하게 노출한 확장보드에 가깝습니다. 다만 같은 캐리어가 59달러 보드와 299달러 보드에 동일하게 꽂힌다는 사실은, 카메라 프로젝트를 시작할 때 무조건 상위 모델부터 살 필요가 없다는 걸 보여줍니다. 전원 예산과 발열처럼 실제 장비에 올릴 때 필요한 숫자는 아직 공개 데이터시트를 더 파봐야 나올 것으로 보입니다.
