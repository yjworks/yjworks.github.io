---
title: "Cloudflare's Skill Says: Unverified Isn't a Vulnerability"
date: 2026-09-24T03:13:22+09:00
slug: "dev-security-audit-skill-deepseek-harness"
summary: "This week's GitHub picks: DeepSeek Harness, a plugin-based agent runtime that crossed 200k stars two weeks after launch, and Cloudflare's security-audit-skill, which adds independent verification before an AI agent's finding counts as a real vulnerability."
tags: ["GitHub"]
categories: ["Dev Picks"]
draft: false
cover:
  image: "/images/posts/dev-security-audit-skill-deepseek-harness.en.png"
  alt: "Cover card: security-audit-skill at 20.8k stars, a 6-phase pipeline, DeepSeek Harness past 200k stars, latest release v0.1.7-rc.1"
  relative: false
---

This week's GitHub trending list is heavy on tooling built for AI coding agents — skills, harnesses, and middleware meant to make agents like Claude Code, Codex, or Cursor faster and more reliable. Two repos stood out for taking opposite approaches to that same problem. One makes an agent audit code but refuses to count a finding until it's independently verified by a second agent. The other tears the entire agent runtime apart into swappable plugins so developers can rebuild it however they want. Read together, they say something about where "agent tooling" is headed this year: less about the model itself, more about the scaffolding around it.

## Cloudflare security-audit-skill

[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) is MIT-licensed, Node.js-based, and sits at roughly 20.8k stars. It ships without GitHub Release tags — updates land straight on the main branch.

The skill turns a coding agent (Claude Code and similar) into a six-phase security auditor:

1. **Recon** — maps architecture, trust boundaries, and input surfaces
2. **Coverage-led hunting** — isolated agents attack the codebase from different angles (injection, access control, business logic, and more)
3. **Candidate validation** — a separate agent tries to disprove each finding
4. **Structured output** — produces a machine-readable findings JSON
5. **Independent record verification** — yet another agent re-checks the underlying evidence
6. **Target-neutral reporting** — the final report is built only from findings that survived verification

Install with one line:

```bash
npx skills add https://github.com/cloudflare/security-audit-skill \
  --skill security-audit --global
```

Once installed, it triggers automatically on prompts like "security audit this codebase" or "find security vulnerabilities in ./src". **The interesting part isn't step 6, it's steps 3 through 5.** A finding from the first pass doesn't make the report just because an agent flagged it — a different agent has to fail to disprove it, and the underlying evidence gets re-checked before it counts. That's a structural answer to the well-known problem of AI-generated security reports padded with false positives: instead of trusting one pass, the pipeline builds disbelief into the process by design, so a plausible-sounding but wrong finding has three separate chances to get thrown out before it ever reaches a human reviewer.

Best for: teams already using AI agents to write or review code who want an automated security pass inserted before merge.

## DeepSeek Harness

[deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) is an MIT-licensed, TypeScript agent runtime. Published on August 13, it passed 100k stars within 48 hours and has since climbed past 200k — one of the fastest-growing repos this year. The latest release is `v0.1.7-rc.1`; the exact release date is TBC (fetched metadata was inconsistent).

Its design principle is "Everything is a Plugin." Built on Cordis, every piece — model adapters, the tool registry, session logs, even the agent loop itself — is a replaceable plugin. In practice that means you're not locked into whatever model or tool set the maintainers shipped by default: swap the model adapter for a different provider, or drop in your own tool registry, without forking the core.

```bash
# quick start
npx @deepseek-ai/dsh web

# build from source
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```

Running it launches a local web UI at `http://127.0.0.1:3080`. Per the v0.1.7-rc.1 release notes, this build adds experimental Playwright-based browser automation and Computer Use support, plus plugin management through the web UI.

**The version string tells its own story: `-rc.1` means this isn't a 1.0 release yet.** Star count and maturity are two different things here.

Best for: developers who want to assemble their own agent runtime instead of relying on a closed product like Claude Code or Codex — better suited to studying the architecture and cherry-picking plugins than to dropping straight into production.

## Wrap-up

Both repos ride the same wave — tooling built for AI agents — but pull in opposite directions. security-audit-skill assumes an agent's own findings can't be trusted and adds verification layers; DeepSeek Harness assumes you want to rebuild the agent itself and hands you every piece as a plugin. The audit skill is ready to slot into an existing workflow today; the harness is still at rc, so start by reading the core loop before betting production on it. Pick based on what you're missing: an extra verification pass in front of code you already ship, or a runtime you can actually take apart.
