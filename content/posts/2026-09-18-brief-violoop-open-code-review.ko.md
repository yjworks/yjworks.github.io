---
title: "바이오루프, 얼리버드 지나면 300달러 오른다"
date: 2026-09-18T03:10:28+09:00
slug: "brief-violoop-open-code-review"
summary: "이번 주 국내 신제품 출시 소식은 확인되지 않았습니다. 해외에서는 화면을 보고 대신 조작하는 AI 하드웨어 '바이오루프'가 킥스타터에서 399달러로 시작했고, 소프트웨어에서는 알리바바의 오픈소스 코드 리뷰 도구가 일주일 새 스타 8,500개를 더했습니다."
tags: ["AI Device", "GitHub", "Global"]
categories: ["Weekly Brief"]
cover:
  image: "/images/posts/brief-violoop-open-code-review.ko.png"
  alt: "커버 카드: 바이오루프 얼리버드 399달러, 정가 699달러, 오픈코드리뷰 스타 34.4천 개, 일주일 증가분 8.5천 개"
  relative: false
draft: false
---

이번 주(9/11~9/18)는 국내보다 해외와 소프트웨어 쪽이 조용하지 않았습니다. 국내 출시 소식은 확인된 것이 없고, 대신 IFA 2026에서 공개됐던 화면 인식 AI 하드웨어가 킥스타터 캠페인을 열었고, 알리바바의 사내 코드 리뷰 도구가 오픈소스로 풀린 지 얼마 되지 않아 GitHub 트렌딩 상위에 올랐습니다.

## 국내

이번 주 국내 정식 출시 소식은 확인되지 않았습니다.

## 해외

**바이오루프(Violoop)** — BVIO 테크놀로지가 IFA 2026에서 처음 공개한 손바닥 크기 AI 하드웨어입니다. 이번 주(9월 15일) 킥스타터 캠페인을 열면서 본격적으로 시장에 등장했습니다.

- HDMI 입력과 USB-HID로 PC·맥에 연결해, 화면을 로컬에서 인식하고 키보드·마우스 명령을 되돌려 보내는 방식으로 작동합니다.
- 200개 앱, 1만 개 실제 화면으로 학습했다고 밝혔습니다.
- 얼리버드가는 **399달러**(홀드용 환불 가능 보증금 10달러), 캠페인이 끝나면 정가는 **699달러**로 오릅니다.
- 출고는 2026년 10월 목표.
- BVIO는 캠페인 전 2,000만 달러 규모 시드 투자를 유치했다고 밝혔습니다.
- 국내 정식 출시·가격은 확인 필요.
- 출처: [PC Guide](https://www.pcguide.com/pro/news-pro/violoop-unveiled-at-ifa-berlin-a-palm-sized-device-that-turns-any-computer-into-an-autonomous-ai-assistant/), [Tom's Guide](https://www.tomsguide.com/computing/laptops/violoop-hands-on-ifa-2026), [Violoop 공식](https://violoop.ai/)

## 소프트웨어

**alibaba/open-code-review** — 알리바바가 2년 넘게 사내에서 쓰던 AI 코드 리뷰 도구를 오픈소스로 공개한 것으로, 이번 주 GitHub 트렌딩에서 스타가 급증했습니다.

- 라이선스: Apache-2.0 / 주 언어: Go
- 스타 약 **34.4천 개**(조사 시점 기준, 최근 일주일 새 약 8,500개 증가)
- 최신 릴리스 **v1.12.5**(2026-09-17): 뷰어 UI 개선, 워크플로 PR 번호 선택 입력, Kimi Code 플러그인 추가, diff 처리·토큰 예산 관련 버그 수정
- 결정론적 파이프라인과 LLM 에이전트를 함께 써서 git diff를 줄 단위로 리뷰하고, NPE·스레드 세이프티·XSS·SQL 인젝션 등 다국어 룰셋을 내장했습니다.
- 설치 및 실행:
  ```bash
  npm install -g @alibaba-group/open-code-review
  ocr config provider
  ocr config model
  ```
  Git 2.41 이상이 필요합니다.
- 출처: [github.com/alibaba/open-code-review](https://github.com/alibaba/open-code-review)

## 이번 주 요약

| 구분 | 항목 | 핵심 수치 |
|---|---|---|
| 국내 | - | 확인된 출시 없음 |
| 해외 | 바이오루프 | 얼리버드 399달러 / 정가 699달러 |
| 소프트웨어 | alibaba/open-code-review | 스타 34.4천 개, 주간 +8.5천 |

## 이번 주 DigitalBrain

- [아이폰 듀오, 늦게 접고 비싸게 판다](/2026/09/14/phone-iphone-duo-galaxy-fold8/)
- [누로비의 자외선, 아쿠아20의 180도](/2026/09/15/appliance-dyson-nurovi-dreame-aqua20/)
- [UR Gen 7, 빨라지고 작아졌다](/2026/09/16/embedded-universal-robots-gen7/)
- [미니CPM5는 이기고, 플래시넥스트는 아낀다](/2026/09/17/dev-minicpm5-qwen-flash-next/)
