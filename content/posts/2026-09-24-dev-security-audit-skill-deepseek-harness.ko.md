---
title: "클라우드플레어 스킬, 검증 못하면 취약점도 아니다"
date: 2026-09-24T03:13:22+09:00
slug: "dev-security-audit-skill-deepseek-harness"
summary: "이번 주 GitHub 트렌딩에서 8월 공개 2주 만에 스타 20만 개를 넘긴 AI 에이전트 프레임워크 DeepSeek Harness와, 코드 에이전트에 독립 검증 단계까지 넣은 Cloudflare의 security-audit-skill을 골랐습니다."
tags: ["GitHub"]
categories: ["Dev Picks"]
draft: false
cover:
  image: "/images/posts/dev-security-audit-skill-deepseek-harness.ko.png"
  alt: "커버 카드: security-audit-skill 스타 2만 800개, 6단계 파이프라인, DeepSeek Harness 스타 20만 개 이상, 최신 릴리스 v0.1.7-rc.1"
  relative: false
---

이번 주 GitHub 트렌딩에는 AI 코딩 에이전트를 겨냥한 도구가 유독 많았습니다. 그중 방향이 뚜렷하게 다른 두 저장소를 골랐습니다. 하나는 에이전트에게 보안 감사를 시키되 "검증 안 된 결과는 취약점으로 세지 않는" 스킬이고, 다른 하나는 에이전트 러닝타임 자체를 통째로 플러그인으로 뜯어낸 프레임워크입니다.

## Cloudflare security-audit-skill

[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)은 MIT 라이선스, 약 2만 800개 스타를 받은 저장소입니다. Node.js 기반이며 별도 GitHub Releases 태그 없이 main 브랜치로 계속 배포됩니다.

이 스킬은 Claude Code 같은 코딩 에이전트를 여섯 단계 파이프라인으로 돌려 보안 감사를 수행합니다.

1. **정찰(Recon)** — 아키텍처, 트러스트 바운더리, 입력 경로를 매핑
2. **커버리지 기반 헌팅** — 인젝션, 접근 제어, 비즈니스 로직 등 서로 다른 관점의 독립 에이전트가 코드를 공격
3. **후보 검증** — 처음 찾은 에이전트와 다른 에이전트가 각 발견을 반증 시도
4. **구조화 출력** — 머신 리더블한 findings JSON 생성
5. **독립 레코드 검증** — 또 다른 에이전트가 근거 기록을 재확인
6. **타깃 중립 리포트** — 검증을 통과한 기록만으로 보고서 작성

설치는 아래처럼 한 줄입니다.

```bash
npx skills add https://github.com/cloudflare/security-audit-skill \
  --skill security-audit --global
```

설치 후에는 "security audit this codebase", "find security vulnerabilities in ./src" 같은 자연어 요청에 자동으로 반응합니다. **핵심은 6번이 아니라 3~5번입니다.** 한 에이전트가 찾았다고 바로 보고서에 올리지 않고, 별도 에이전트가 반증을 시도하고 근거를 다시 확인한 것만 최종 결과에 남깁니다. AI가 만든 보안 리포트에 실제로는 없는 취약점이 섞여 나오는 문제(허위 양성)를 구조로 줄이려는 설계입니다.

추천 대상: AI 에이전트로 코드를 짜거나 리뷰하는 팀 중, 머지 전에 자동 보안 감사를 한 단계 끼워 넣고 싶은 경우.

## DeepSeek Harness

[deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)는 MIT 라이선스, TypeScript로 작성된 오픈소스 에이전트 러닝타임입니다. 8월 13일 공개 이후 2주 만에 스타 10만 개를, 이번 주 기준 20만 개 이상을 넘기며 올해 가장 빠르게 성장한 저장소로 꼽힙니다. 최신 릴리스는 `v0.1.7-rc.1`이며, 정확한 배포 날짜는 확인 필요합니다.

설계 철학은 "Everything is a Plugin"입니다. Cordis 위에 모델 어댑터, 툴 레지스트리, 세션 로그, 에이전트 루프까지 전부 교체 가능한 플러그인으로 구성했습니다.

```bash
# 빠른 실행
npx @deepseek-ai/dsh web

# 소스에서 빌드
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```

실행하면 로컬에 `http://127.0.0.1:3080` 웹 UI가 뜹니다. v0.1.7-rc.1에는 Playwright 기반 브라우저 자동화·컴퓨터 유즈 실험 기능과 웹 UI를 통한 플러그인 관리가 새로 들어갔다고 릴리스 노트에 적혀 있습니다.

**버전 표기(`-rc.1`)가 그대로 알려주듯, 아직 정식 1.0 릴리스는 아닙니다.** 스타 수와 성숙도는 다른 지표라는 점을 감안해야 합니다.

추천 대상: Claude Code·Codex류 상용 에이전트 대신 직접 조립 가능한 에이전트 러닝타임이 필요한 개발자. 프로덕션에 바로 올리기보다는 구조를 뜯어보고 필요한 플러그인만 가져다 쓰는 용도로 먼저 검토하는 편이 안전합니다.

## 오늘의 정리

두 저장소 모두 "AI 에이전트를 위한 도구"라는 흐름 위에 있지만 방향은 정반대입니다. security-audit-skill은 에이전트의 결과를 못 믿을 수 있다는 전제에서 검증 단계를 늘렸고, DeepSeek Harness는 에이전트 자체를 마음대로 재구성할 수 있게 풀어놨습니다. 감사 스킬은 지금 바로 기존 워크플로에 끼워 넣을 수 있고, 하네스는 아직 rc 버전이니 핵심 로직만 먼저 들여다보는 쪽을 권합니다.
