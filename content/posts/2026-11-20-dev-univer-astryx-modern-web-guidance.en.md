---
title: "Two SDKs for your app, one rulebook for your agent"
seoTitle: "Univer, Astryx, Modern Web Guidance: GitHub Trending This Week"
date: 2026-11-20T10:30:15+09:00
slug: "dev-univer-astryx-modern-web-guidance"
summary: "Three repositories from this week's GitHub trending list: Univer embeds spreadsheets in your app, Astryx is a design system built with agents in mind, and Chrome's Modern Web Guidance steers coding agents away from outdated web code. Licenses, install commands and current limits."
tags: ["GitHub"]
categories: ["Dev Picks"]
cover:
  image: "/images/posts/dev-univer-astryx-modern-web-guidance.en.png"
  alt: "Cover card: Univer 30,407 stars, Astryx 30,874 stars, Modern Web Guidance 9,053 stars with 7,257 gained this week"
  relative: false
draft: false
reviewed: "2026-11-20"
---

Ask a coding agent for a web UI and the output often looks a few years old. Three entries near the top of this week's GitHub trending list come at that problem from different directions: an SDK that puts an office editor inside your app, a design system built for agents to use, and a rulebook that tells agents which web platform features are current.

Star counts and weekly gains below come from the [GitHub weekly trending page](https://github.com/trending?since=weekly) as of November 20, 2026.

| Repository | Total stars | Gained this week | License | Language |
|---|---|---|---|---|
| dream-num/univer | 30,407 | 6,840 | Apache-2.0 (open-source packages) | TypeScript |
| meta/astryx | 30,874 | 6,250 | MIT | TypeScript |
| GoogleChrome/modern-web-guidance-src | 9,053 | 7,257 | Apache-2.0 | TypeScript |

Sources: [GitHub Trending (weekly)](https://github.com/trending?since=weekly), [univer](https://github.com/dream-num/univer), [astryx](https://github.com/meta/astryx), [modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)

Latest tags (checked November 20, 2026): univer `v1.5.2` (November 16), astryx `v0.7.16` (November 13), modern-web-guidance-src `v1.0.1` (November 16). Pin a tag like these before building on them.

## Univer: spreadsheets inside your own app

[Univer](https://github.com/dream-num/univer) is an SDK for building office features, such as sheets, documents and slides, into your own product. It covers editing, calculation, collaboration and file processing. According to the README, the open-source packages in this repository are Apache-2.0, while commercial plugins, a Server SDK and AI SDK extensions are licensed separately. Check where the free and paid lines fall before you commit.

The README quick start:

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

Put a `<div id="app" style="height: 100vh"></div>` container in your HTML and the sheet renders inside it. We found no data on rendering speed or large-file limits, so we make no claims there.

Best for: web developers who need an Excel-style editing view inside an internal tool or SaaS product.

## Astryx: a design system with agents in mind

[Astryx](https://github.com/meta/astryx) is an MIT-licensed design system from Meta's organization. The README lists 150+ accessible components, brand-level theming, dark mode, templates and a CLI. It ships typed React components on React 19+ and StyleX, and styling can be overridden through `className` with Tailwind, CSS modules or plain CSS. **It is currently in beta.**

```bash
npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
npm install -D @astryxdesign/cli
npx @astryxdesign/cli init
```

The CLI can list components. Add the README's script to `package.json` and run `npm run astryx -- component --list`. The "built for agents" pitch has a concrete meaning in the README: running `init` once saves the Astryx guide to `AGENTS.md`/`CLAUDE.md`, so coding agents read the same reference instead of guessing.

Best for: teams starting a new React 19 project that can live with a beta design system.

## Modern Web Guidance: fixing an agent's old habits

The biggest weekly jump on the list is [modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src): 9,053 stars total, 7,257 of them gained this week. It is Apache-2.0, and the README describes it as the source for a package that feeds web platform best practices and browser compatibility data to coding agents so they pick current features over legacy patterns.

Chrome's docs say agents follow the old code in their training data. The [modernization workflow page](https://developer.chrome.com/docs/modern-web-guidance/modernization-workflow) says the `legacy-scan` command covers only the subset of roughly 200 guides, about 20%, where legacy code can be detected mechanically without false positives. The [get-started page](https://developer.chrome.com/docs/modern-web-guidance/get-started) says agents using it followed modern best practices 37 percentage points more often in early evals, with results varying by project, model and prompt; that is Chrome's own figure. Version 1.0 shipped with the `v1.0.0` tag on November 10 ([Chrome blog](https://developer.chrome.com/blog/modern-web-guidance-v1)).

```bash
npx modern-web-guidance@latest install

# without installing
npx modern-web-guidance@latest search "animate a dialog modal backdrop"
npx modern-web-guidance@latest retrieve "animate-to-from-top-layer"
npx modern-web-guidance@latest legacy-scan .
```

`legacy-scan .` looks for outdated patterns across a codebase. The docs say CI integration is still in development.

Best for: teams already building front ends with a coding agent who are bothered by outdated API usage in the output.

## Shipping in your app versus shipping to your agent

Univer and Astryx become dependencies in product code, so the license boundary (Univer's commercial modules) and the beta status (Astryx) come first. Modern Web Guidance is the cheapest to try: one command to start, and `legacy-scan` shows the affected area before you change anything. All three picked up new tags this week, so pin a version before you build on them.
