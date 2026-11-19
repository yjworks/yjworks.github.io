---
title: "내 앱에 넣을 SDK 둘, 에이전트에 넣을 지침 하나"
seoTitle: "Univer·Astryx·Modern Web Guidance 설치 방법 | GitHub 트렌딩"
date: 2026-11-20T03:06:42+09:00
slug: "dev-univer-astryx-modern-web-guidance"
summary: "이번 주 GitHub 주간 트렌딩에서 앱에 스프레드시트를 넣는 Univer, 에이전트용 디자인 시스템 Astryx, 코딩 에이전트의 낡은 웹 코드를 막아 주는 Chrome팀의 Modern Web Guidance를 골라 라이선스와 설치 명령, 현재 한계를 정리했습니다."
tags: ["GitHub"]
categories: ["Dev Picks"]
cover:
  image: "/images/posts/dev-univer-astryx-modern-web-guidance.ko.png"
  alt: "커버 카드: Univer 스타 3만 407개, Astryx 스타 3만 874개, Modern Web Guidance 스타 9,053개와 주간 증가 7,257개"
  relative: false
draft: true
---

코딩 에이전트에게 웹 화면을 맡기면, 결과물이 몇 해 전 방식으로 나오는 일이 흔합니다. 이번 주 GitHub 주간 트렌딩의 상위권에는 이 문제를 서로 다른 쪽에서 푸는 저장소가 올라와 있습니다. 하나는 앱 안에 오피스 편집기를 넣는 SDK, 하나는 에이전트가 쓰도록 만든 디자인 시스템, 하나는 에이전트에게 최신 웹 표준을 알려 주는 지침입니다.

아래 스타 수와 주간 증가분은 2026년 11월 20일에 본 [GitHub 주간 트렌딩 페이지](https://github.com/trending?since=weekly) 값입니다.

| 저장소 | 총 스타 | 이번 주 증가 | 라이선스 | 언어 |
|---|---|---|---|---|
| dream-num/univer | 30,407 | 6,840 | Apache-2.0 (오픈소스 패키지) | TypeScript |
| meta/astryx | 30,874 | 6,250 | MIT | TypeScript |
| GoogleChrome/modern-web-guidance-src | 9,053 | 7,257 | Apache-2.0 | TypeScript |

출처: [GitHub Trending (weekly)](https://github.com/trending?since=weekly), [univer](https://github.com/dream-num/univer), [astryx](https://github.com/meta/astryx), [modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)

> **아직 확인하지 못한 것:** 세 저장소 모두 조회한 페이지에 최신 릴리스 이름과 날짜가 나오지 않아 확인하지 못했습니다. 사용할 때는 각 저장소의 릴리스·태그를 직접 보고 버전을 고정해야 합니다.

## Univer: 앱 안에 스프레드시트를 넣는 SDK

[Univer](https://github.com/dream-num/univer)는 자기 제품 안에 시트·문서·슬라이드 같은 오피스 기능을 넣을 수 있게 하는 SDK입니다. 편집, 계산, 협업, 파일 처리를 다룹니다. README에 따르면 이 저장소의 오픈소스 패키지는 Apache-2.0이고, 상용 플러그인과 서버 SDK, AI SDK 확장은 별도 라이선스로 따로 제공됩니다. 오픈소스 범위와 유료 범위가 갈린다는 점은 도입 전에 확인해야 합니다.

README의 빠른 시작은 다음과 같습니다.

```bash
pnpm add @univerjs/presets @univerjs/preset-sheets-core
```

```javascript
import { UniverSheetsCorePreset } from '@univerjs/preset-sheets-core'
import UniverPresetSheetsCoreEnUS from '@univerjs/preset-sheets-core/locales/en-US'
import { createUniver, LocaleType, mergeLocales } from '@univerjs/presets'
import '@univerjs/preset-sheets-core/lib/index.css'

const { univerAPI } = createUniver({
  locale: LocaleType.EN_US,
  locales: {
    [LocaleType.EN_US]: mergeLocales(UniverPresetSheetsCoreEnUS),
  },
  presets: [
    UniverSheetsCorePreset({
      container: 'app',
    }),
  ],
})

univerAPI.createWorkbook({})
```

HTML에 `<div id="app" style="height: 100vh"></div>` 컨테이너를 두면 그 안에 시트가 뜹니다. 렌더링 성능이나 큰 파일 처리 한계는 확인한 자료가 없어 판단하지 않습니다.

추천 대상: 사내 도구나 SaaS에 엑셀 같은 편집 화면을 넣어야 하는 웹 개발자.

## Astryx: 에이전트를 염두에 둔 디자인 시스템

[Astryx](https://github.com/meta/astryx)는 메타 조직의 MIT 라이선스 디자인 시스템입니다. README는 접근성을 갖춘 컴포넌트 150개 이상, 브랜드 단위 테마, 다크 모드, 템플릿, CLI를 내세웁니다. React 19 이상과 StyleX 기반의 타입 있는 컴포넌트로 쓰고, 스타일은 `className`으로 Tailwind, CSS 모듈, 일반 CSS 어느 쪽으로든 덮어쓸 수 있다고 적었습니다. **현재 베타입니다.**

```bash
npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
npm install -D @astryxdesign/cli
npx @astryxdesign/cli init
```

컴포넌트 목록은 CLI로 볼 수 있습니다. README의 스크립트를 `package.json`에 넣으면 `npm run astryx -- component --list`로 실행합니다. "에이전트용"이라는 설명이 실제로 어떤 기능을 뜻하는지는 확인한 범위에서 구체적인 근거를 찾지 못했습니다.

추천 대상: React 19로 새 프로젝트를 시작하면서 베타 단계의 디자인 시스템을 감수할 수 있는 팀.

## Modern Web Guidance: 에이전트의 낡은 습관을 고치는 지침

이번 주 증가폭이 가장 큰 것은 [modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)입니다. 총 스타는 9,053개인데 한 주에 7,257개가 늘었습니다. Apache-2.0이고, README에 따르면 웹 플랫폼 모범 사례와 브라우저 호환성 데이터를 코딩 에이전트에 넣어 레거시 패턴 대신 최신 플랫폼 기능을 쓰게 하는 패키지의 소스 저장소입니다.

Chrome 문서는 에이전트가 학습 데이터에 쌓인 옛 코드를 따라간다고 설명하고, [현대화 워크플로 문서](https://developer.chrome.com/docs/modern-web-guidance/modernization-workflow)에서 `legacy-scan` 명령이 약 200개 가이드 중 오탐 없이 기계적으로 찾을 수 있는 20% 정도만 다룬다고 밝힙니다. 같은 문서 계열에서 초기 평가로 최신 모범 사례 준수율이 37%p 올랐다고 하지만, 평가 조건은 확인하지 못했고 Chrome팀 자체 수치입니다. README는 이 프로젝트를 프리뷰 릴리스로 표시합니다.

```bash
npx modern-web-guidance@latest install

# 설치 없이 쓰기
npx modern-web-guidance@latest search "animate a dialog modal backdrop"
npx modern-web-guidance@latest retrieve "animate-to-from-top-layer"
npx modern-web-guidance@latest legacy-scan .
```

`legacy-scan .`은 코드베이스에서 낡은 패턴을 찾아 줍니다. CI 연동은 아직 개발 중이라고 문서에 나와 있습니다.

추천 대상: 이미 코딩 에이전트로 프런트엔드를 짜고 있고, 결과물의 낡은 API 사용이 신경 쓰이는 팀.

## 앱에 넣는 것과 에이전트에 넣는 것은 부담이 다릅니다

Univer와 Astryx는 제품 코드에 들어가는 의존성이라 라이선스 범위(Univer의 상용 모듈)와 베타 상태(Astryx)를 먼저 따져야 합니다. Modern Web Guidance는 명령 한 줄로 시험하고 `legacy-scan`으로 영향 범위를 먼저 볼 수 있어 진입 부담이 가장 작습니다. 세 곳 모두 릴리스 버전을 확인하지 못했으니, 쓰기로 했다면 버전을 고정한 뒤 시작하는 편이 안전합니다.
