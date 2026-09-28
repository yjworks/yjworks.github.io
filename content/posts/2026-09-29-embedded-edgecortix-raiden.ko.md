---
title: "라이덴, 젯슨 토르 1.6배인데 전력은 안 나왔다"
seoTitle: "EdgeCortix RAIDEN vs Jetson AGX Thor 성능 비교: FP4 PFLOPS·메모리"
date: 2026-09-29T03:15:13+09:00
slug: "embedded-edgecortix-raiden"
summary: "EdgeCortix가 로봇·물리 AI용 칩렛 플랫폼 라이덴(RAIDEN)을 공개했습니다. FP4 연산 성능과 메모리 대역폭을 엔비디아 젯슨 AGX 토르와 비교하고, 아직 나오지 않은 전력 수치를 짚었습니다."
tags: ["AI Device", "Robot", "Global"]
categories: ["Deep Dive"]
cover:
  image: "/images/posts/embedded-edgecortix-raiden.ko.png"
  alt: "커버 카드: 라이덴 X4 구성 FP4 3.36 페타플롭스, 메모리 256GB, 대역폭 548GB/s, 젯슨 토르 대비 1.6배"
  relative: false
draft: false
---

로봇에 얹을 AI 칩을 고를 때 가장 먼저 봐야 할 숫자는 페타플롭스가 아니라 와트입니다. 연산 성능이 아무리 높아도 로봇 팔이나 이동형 플랫폼에 들어갈 전력 예산을 넘으면 그 칩은 후보에서 빠지기 때문입니다. 그런데 이번에 공개된 칩은 성능 숫자만 크게 내놓고 이 부분을 비워뒀습니다.

일본 AI 반도체 스타트업 EdgeCortix가 9월 24일(현지 시간) 가나가와에서 물리 AI(Physical AI) 전용 칩렛 플랫폼 '라이덴(RAIDEN)'을 발표했습니다. 데이터센터가 아니라 로봇·자율주행·산업 장비처럼 전력과 공간이 제한된 곳에 들어가는 것을 목표로 만든 제품입니다.

## X4 구성이면 젯슨 AGX 토르의 1.6배입니다

라이덴은 다이(die) 하나짜리 X1부터 두 개를 묶은 X2, 네 개를 묶은 최상위 X4까지 같은 DNA-X 가속기 아키텍처를 모듈처럼 늘려 쓰는 구조입니다. 세 구성 모두 EdgeCortix의 MERA 소프트웨어 스택을 공유합니다.

| 구성 | 최대 FP4 연산 | 메모리 | 메모리 대역폭 | 다이 간 대역폭 |
|---|---|---|---|---|
| 라이덴 X4 (최상위) | 3.36 PFLOPS (3,360 TFLOPS) | 최대 256GB | 548GB/s | 최대 1.54TB/s |
| 젯슨 AGX 토르 | 2,070 TFLOPS (2.07 PFLOPS) | 128GB LPDDR5X | 약 273GB/s | 해당 없음(단일 다이) |

출처: [EdgeCortix RAIDEN 발표 자료(HPCwire)](https://www.hpcwire.com/off-the-wire/edgecortix-unveils-raiden-a-scalable-energy-efficient-ai-chiplet-platform-for-physical-ai/), [EdgeCortix RAIDEN 발표(Embedded.com)](https://www.embedded.com/edgecortix-launches-scalable-raiden-ai-chiplet-platform), [Jetson AGX Thor 스펙(Waveshare)](https://www.waveshare.com/jetson-agx-thor-developer-kit.htm)

![라이덴 X4와 젯슨 AGX 토르를 FP4 연산·메모리·대역폭으로 비교한 막대 그래프](/images/posts/embedded-edgecortix-raiden.ko-compare.png "표를 막대로 그린 것입니다. 라이덴 X4가 세 항목 모두에서 앞섭니다.")

X1과 X2의 개별 수치는 이번 발표 자료에 나오지 않았고, X4만 구체적인 숫자가 공개됐습니다. 이 최상위 구성 기준으로 FP4 연산 성능은 젯슨 AGX 토르 대비 약 1.6배, 메모리는 두 배, 메모리 대역폭은 약 2배입니다. 칩 4개를 다이 간 1.54TB/s로 묶는 구조라 단일 다이인 젯슨 토르와는 애초에 설계 방향이 다릅니다.

## 정작 전력 수치는 나오지 않았습니다

발표 자료는 라이덴의 전력에 대해 "구성 가능한 전력 설정(configurable power settings)"이라고만 밝혔습니다. X1·X2·X4 각 구성이 몇 와트에서 도는지, 최상위 X4가 몇 와트까지 올라가는지는 이번 자료에 없습니다.

비교 대상인 젯슨 AGX 토르는 40~130W 범위에서 동작하고, 개발자 키트 기준으로는 75~120W 구간에서 설정해 쓰는 제품으로 알려져 있습니다. 로봇에 실제로 올릴 때는 이 범위 안에서 방열판 크기와 배터리 용량이 정해지는데, 라이덴은 이 기준점이 아직 없어 젯슨과 나란히 놓고 전력 대비 성능을 계산할 수 없습니다.

> **아직 공개되지 않은 것:** 각 구성(X1/X2/X4)의 소비전력, 공정 노드, 가격, 실제 실리콘 공급(샘플링·양산) 시점. 공식 자료가 나오면 이 글을 고칩니다.

## 로봇 개발자가 지금 살 수 있는 칩은 아닙니다

젯슨 AGX 토르는 개발자 키트 형태로 소매 채널에서 바로 구매할 수 있는 제품입니다. 반면 라이덴은 EdgeCortix가 로봇·장비 제조사에 공급하는 칩렛 플랫폼으로, 발표 시점에는 개인이나 소규모 팀이 보드에 얹어 바로 쓸 수 있는 형태로 나온 게 아닙니다. 성능·메모리 숫자만 보고 "젯슨보다 좋은 대안"으로 받아들이기엔 아직 이릅니다.

다이를 여러 개 묶는 칩렛 구조 자체는 대형 로봇·산업 장비처럼 전력 여유가 있는 곳에서 먼저 채택될 가능성이 큽니다. 배터리로 움직이는 소형 로봇이나 개인 프로젝트에는 전력 수치가 나오기 전까지는 여전히 젯슨 계열이 현실적인 선택지입니다.

## 지금은 숫자보다 공급 시점을 봐야 합니다

라이덴은 성능·메모리 지표만 놓고 보면 물리 AI용 칩 중 눈에 띄는 스펙을 내놓은 게 맞습니다. 하지만 로봇에 실제로 들어가려면 전력, 공정, 공급 시점, 그리고 개발자가 손에 넣을 수 있는 보드 형태까지 나와야 판단할 수 있습니다. 이 정보가 나오기 전까지는 발표 수치만으로 젯슨 AGX 토르의 대안이라고 단정하기 어렵습니다.
