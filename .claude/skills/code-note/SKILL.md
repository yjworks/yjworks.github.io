---
name: code-note
description: 운영자가 직접 만든 코드를 받아 "코드 노트"(categories Code Notes) 글로 정리해 올릴 때 쓴다. 코드는 운영자의 것 그대로 두고, AI는 코드를 읽고 설명·실행 방법·주의점을 쓴다. 신원·회사 정보와 비밀값을 지우고, 운영자가 초안을 확인한 뒤에만 발행한다.
---

# code-note — 운영자 코드 + AI 설명

사이트에는 **"운영자 코드 · AI 정리"** 로 표시된다. 코드는 사람이, 글은 AI가 쓴 것이다.
이 구분이 참이려면 코드를 AI가 고쳐 쓰거나, 운영자가 하지 않은 시험을 한 것처럼 쓰면 안 된다.

## 0. 받기 전에 확인할 것 (한 번에 물어본다)

1. **개인 코드인가?** 회사(서큘러스, Pibo, pibo-lab) 코드이거나 회사 업무로 만든 것이면 올리지 않는다.
2. **공개 라이선스:** 따로 말이 없으면 MIT로 올려도 되는지 묻는다.
3. **어디까지 돌려 봤나:** 실제 보드에서 동작 확인, 컴파일만, 아직 안 돌려 봄 중 무엇인지. 사용 보드·부품·라이브러리 버전.
4. 글에서 꼭 짚었으면 하는 점이 있는지(선택).

## 1. 코드 정리 — 지울 것

코드 동작은 바꾸지 않는다. 아래만 지우거나 바꾸고, **무엇을 바꿨는지 목록으로 보여준다.**

- 사람 이름, 이메일, GitHub 계정명(`yjworks`, `leeyunjai` 등), 회사명, 사내 URL·IP·호스트명
- API 키, 토큰, 비밀번호, Wi-Fi SSID/비밀번호 → `"YOUR_API_KEY"` 같은 자리표시자
- 파일 경로의 사용자명(`/home/<이름>/`) → `~/`
- 저작권 줄의 실명 → `DigitalBrain`

```bash
grep -nEi 'yjworks|leeyunjai|circulus|pibo|@gmail|api[_-]?key|token|passw|ssid|/home/[a-z]' <코드 파일>
```

## 2. 글 쓰기

파일: `content/posts/YYYY-MM-DD-code-<slug>.ko.md` / `.en.md` (날짜는 `TZ=Asia/Seoul date +%FT%T+09:00` 그대로)

```yaml
---
title: "<무엇을 만드는 코드인지 한 줄>"
seoTitle: "<보드·라이브러리 이름 + 무엇을 하는지, 예: ESP32-S3 MicroPython 서보 16채널 제어 예제>"
date: <명령 출력>
slug: "code-<slug>"
summary: "<무엇을, 어떤 보드에서, 어디까지 확인했는지>"
tags: ["SBC"]                  # data/topics.yaml 주제 태그 중 해당하는 것
categories: ["Code Notes"]
cover:
  image: "/images/posts/code-<slug>.ko.png"
  alt: "커버 카드: <카드 수치를 문장으로>"
  relative: false
draft: false
---
```

본문에 들어갈 것(소제목은 내용으로 쓴다. "개요", "총평" 같은 틀 소제목 금지):

1. 이 코드가 하는 일과 쓸 만한 상황
2. **동작 확인 범위.** 운영자가 말한 그대로 쓴다. 예: "ESP32-S3 DevKitC-1에서 서보 4채널로 동작 확인. 16채널은 시험하지 않음."
   말하지 않은 시험은 절대 쓰지 않는다.
3. 준비물: 보드, 부품, 라이브러리와 버전(영문 원문 그대로)
4. 배선·핀: **코드에 있는 핀 번호만** 표로. 전압·전류 정격은 데이터시트 출처가 없으면 "확인 필요".
   3.3V/5V가 섞이는 지점, 서보 여러 개를 한 전원에 물릴 때의 전압 강하가 해당되면 먼저 짚는다.
5. **코드 전체.** 조각이 아니라 파일 전체를 싣는다. 파일이 여럿이면 파일마다 코드 블록.
6. 실행 방법: 실제 명령(업로드·설치·실행)
7. 코드를 읽고 보이는 주의점과 확장 방법. "코드를 보면 ~" 처럼 근거를 앞에 둔다.
8. 라이선스 한 줄

- 1인칭 경험("제가 해 보니")을 쓰지 않는다. 운영자의 확인 결과는 "운영자가 ~에서 확인했습니다"로 옮긴다.
- 영어판은 같은 내용을 영어권 독자에 맞게 쓴다. 코드는 같게 둔다(주석 번역은 하지 않는다).
- 커버 카드는 `scripts/postimg.py` 로 그린다. `accent` 는 `"code"`, kicker 는 `코드 노트 · <주제>` / `Code Notes · <topic>`.
  stats 는 코드에서 셀 수 있는 것(채널 수, 주기 ms, 줄 수, 대상 보드 등)만.

## 3. 확인과 발행

1. 초안 전체, 코드에서 바꾼 것 목록, 동작 확인 범위를 운영자에게 보여 주고 OK를 받는다.
2. 발행:

```bash
git add content/posts/YYYY-MM-DD-code-<slug>.*.md static/images/posts/code-<slug>*.png scripts/img-specs/code-<slug>*.json
git -c user.name=Claude -c user.email=noreply@anthropic.com commit -m "post (code note): <English title>"
git push origin main
```

3. 배포 결과를 확인하고 URL을 알려 준다.
