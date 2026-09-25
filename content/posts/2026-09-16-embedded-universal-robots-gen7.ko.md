---
title: "UR Gen 7, 빨라지고 작아졌다"
seoTitle: "UR Gen 7 UR17g-1300 vs UR10e 협동로봇 스펙 비교"
date: 2026-09-16T03:08:05+09:00
lastmod: 2026-09-25T10:06:19+09:00
updates:
  - date: "2026-09-25"
    text: "공식 자료로 확인되지 않은 UR18g-950 무게(39.2kg)를 '확인 필요'로 바꿨습니다."
  - date: "2026-09-25"
    text: "빠져 있던 출처 링크를 추가했습니다."
slug: "embedded-universal-robots-gen7"
summary: "유니버설로봇이 IMTS 2026에서 공개한 7세대 협동로봇 플랫폼 UR Gen 7을 살펴보고, 같은 1300mm 리치를 쓰는 이전 세대 UR10e와 스펙을 비교했습니다."
tags: ["Robot", "Global"]
categories: ["Deep Dive"]
cover:
  image: "/images/posts/embedded-universal-robots-gen7.ko.png"
  alt: "커버 카드: CB7 Core 연산 성능 +40%, 컨트롤러 크기 -30%, UR17g-1300 최고 속도 5m/s, IMTS 2026(9/14) 공개"
  relative: false
draft: false
---

유니버설로봇(Universal Robots)이 9월 14일(현지시간) 미국 시카고 IMTS 2026에서 7세대 협동로봇 플랫폼 'UR Gen 7'을 공개했습니다. 새 로봇팔 3종과 컨트롤러, 툴 플랜지를 한꺼번에 갈아엎은 이번 세대는 카메라·힘센서를 로봇팔 끝단에서 바로 물릴 수 있게 한 것이 핵심입니다. 20년간의 협동로봇 노하우와 10만 대 이상의 산업 현장 배치 경험을 반영한 "엔드투엔드 재설계"라는 설명입니다.

## UR Gen 7

이번에 나온 g-시리즈 3종은 모델명 자체가 페이로드(kg)와 리치(mm)를 담고 있습니다.

| 모델 | 페이로드 | 리치 | 무게 | 반복 정밀도 | 최고 TCP 속도 |
|---|---|---|---|---|---|
| UR10g-1750 | 8kg(확장 시 10kg) | 1750mm | 44.7kg | ±0.08mm | 5m/s |
| UR17g-1300 | 15kg(확장 시 17.5kg) | 1300mm | 40.7kg | ±0.05mm | 5m/s |
| UR18g-950 | 18kg | 950mm | 확인 필요 | ±0.05mm | 4m/s |

출처: [Universal Robots 보도자료](https://www.universal-robots.com/news-and-media/news-center/universal-robots-unveils-gen-7-new-platform-industrial-automation-physical-ai/), [The Robot Report](https://www.therobotreport.com/universal-robots-launches-its-seventh-generation-robot-platform-at-imts/), [Unite.AI](https://www.unite.ai/universal-robots-debuts-gen-7-cobot-platform-for-physical-ai/)

컨트롤러는 'CB7 Core'로 교체됐습니다. 이전 세대 대비 연산 성능이 40% 높아졌고, 크기는 30% 작아졌다고 밝혔습니다. 임베디드 관점에서 더 눈에 띄는 것은 새 g-시리즈 툴 플랜지입니다. 카메라나 힘센서 같은 엔드이펙터에 데이터·전원·안전 신호를 플랜지 한 곳에서 바로 공급해, 별도 케이블을 팔 바깥으로 감아 배선하지 않아도 되게 했습니다. 로봇팔 자체에도 힘-토크 센싱과 임피던스 제어, 실시간 데이터 교환(Real-Time Data Exchange) 기능이 기본 내장돼, 정밀 조립처럼 접촉력을 느끼며 움직여야 하는 작업을 겨냥합니다. 다만 툴 플랜지가 공급하는 정확한 전압·전류 범위와 개별 모델의 최대 소비전력은 이번 발표 자료에는 나오지 않아 확인이 필요합니다.

출처: [Universal Robots 보도자료](https://www.universal-robots.com/news-and-media/news-center/universal-robots-unveils-gen-7-new-platform-industrial-automation-physical-ai/), [Automation World](https://www.automationworld.com/factory/robotics/news/55404812/universal-robots-unveils-gen-7-platform-at-imts-2026-in-chicago)

## UR17g-1300 vs UR10e — 같은 1300mm 리치, 다른 세대

리치가 같은 1300mm인 UR17g-1300과 직전 세대의 대표 모델 UR10e를 나란히 놓아 봤습니다.

| 항목 | UR10e (이전 세대) | UR17g-1300 (Gen 7) |
|---|---|---|
| 페이로드 | 12.5kg | 15kg(확장 시 17.5kg) |
| 리치 | 1300mm | 1300mm |
| 무게 | 33.5kg | 40.7kg |
| 반복 정밀도 | ±0.05mm | ±0.05mm |
| 최고 TCP 속도 | 4m/s | 5m/s |
| 최대 소비전력 | 615W | 확인 필요 |

출처: [Universal Robots UR10e 기술 사양서](https://www.universal-robots.com/manuals/EN/TechSheets/UR10e_techsheet_pdf_online/UR10e_techsheet_en.pdf), [Unite.AI](https://www.unite.ai/universal-robots-debuts-gen-7-cobot-platform-for-physical-ai/)

![UR10e 대비 UR17g-1300은 페이로드가 12.5kg에서 15kg(확장 17.5kg)로, 최고 속도가 4m/s에서 5m/s로 늘었습니다](/images/posts/embedded-universal-robots-gen7.ko-compare.png "표를 막대로 그린 것입니다. 같은 1300mm 리치에서 페이로드와 속도가 함께 올랐습니다.")

같은 리치에서 페이로드가 20% 늘고 속도도 25% 빨라졌지만, 무게는 오히려 7kg 넘게 무거워졌습니다. 툴 플랜지와 힘-토크 센싱이 새로 들어간 대가로 보이며, 반복 정밀도는 ±0.05mm로 그대로 유지됐습니다.

## 어떤 현장에 맞을까

카메라나 힘센서를 팔 끝에 여러 개 붙여야 하는 정밀 조립·검사 라인이라면 배선이 단순해지는 툴 플랜지의 이득이 큽니다. 반대로 단순 픽앤플레이스처럼 센서를 거의 안 쓰는 라인에서는 기존 e-시리즈로도 충분해, 무게가 늘고 가격이 오를 Gen 7로 굳이 갈아탈 이유가 적습니다. 가격은 이번 발표에 공개되지 않았습니다.

## 국내 출시 여부

유니버설로봇은 국내에 공식 총판 유통망을 두고 있지만, UR Gen 7의 한국 출시 일정과 가격은 이번 발표 자료와 국내 유통사 공지 어디에도 나오지 않아 확인이 필요합니다.

## 총평

UR Gen 7은 로봇팔 자체보다 툴 플랜지와 컨트롤러의 변화가 더 큰 세대입니다. 배선을 줄이고 센서를 붙이기 쉽게 만든 쪽에 힘을 준 만큼, 카메라·힘센서를 적극적으로 쓰는 '피지컬 AI' 응용을 겨냥한 로드맵이라고 볼 수 있습니다. 다만 전력 사양과 국내 가격처럼 실무에 바로 필요한 숫자는 아직 비어 있어, 도입을 검토한다면 공식 스펙 시트 공개를 기다리는 편이 안전합니다.
