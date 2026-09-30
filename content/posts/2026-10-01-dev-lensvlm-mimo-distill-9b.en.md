---
title: "Two 9B Models: One Reads Compressed, One Learns Distilled"
seoTitle: "Apple LensVLM-9B vs MiMo-V2.6-Distill-Qwen-9B | Hugging Face Trending"
date: 2026-10-01T03:12:05+09:00
slug: "dev-lensvlm-mimo-distill-9b"
summary: "Two 9B models from this week's Hugging Face trending list, both built on Qwen3.5-9B: Apple's LensVLM-9B, which reads long documents as compressed images, and Xiaomi's MiMo-V2.6-Distill-Qwen-9B, tuned for coding and agents. Licenses, numbers and how to run them."
tags: ["Hugging Face"]
categories: ["Dev Picks"]
draft: false
cover:
  image: "/images/posts/dev-lensvlm-mimo-distill-9b.en.png"
  alt: "Cover card: LensVLM-9B holds accuracy at 4.3x compression, MiMo-V2.6-Distill-Qwen-9B scores 61.1 on SWE-bench Verified"
  relative: false
---

Two models on this week's Hugging Face trending list share a size (9B) and a base (Qwen3.5-9B) but
have nothing else in common. One scans long text as compressed images and expands only what it needs.
The other is a supervised fine-tune on coding and agent data. Trending ranks come from an aggregator
([agents-radar, Sept 28 digest](https://github.com/kakapez/agents-radar/issues/1614)); details were
cross-checked against separate write-ups of each model.

## LensVLM-9B

- Model card: [apple/LensVLM-9B](https://huggingface.co/apple/LensVLM-9B)
- Code: [apple-aiml-research/ml-lensvlm](https://github.com/apple-aiml-research/ml-lensvlm)
- Paper summary: [Apple Machine Learning Research](https://machinelearning.apple.com/research/lensvlm-context-expansion)
- Publisher: Apple. License: Apple Machine Learning Research Model License (apple-amlr), not Apache-2.0
- Size: 9B, based on Qwen3.5-9B; task: vision-language, long-document QA
- Released: appeared on Apple's Hugging Face profile Sept 21; code on GitHub Sept 22

The model reads long text as compressed images and uses learned tools to expand only the pages a
question needs. Per Apple's summary, across seven text QA benchmarks it keeps accuracy comparable to
the full-text upper bound at 4.3x effective compression and beats retrieval, text-compression and
visual-compression baselines up to 10.1x. The demo script takes 5x, 10x or 15x compression options.

Running it: follow the repository README; the card could not be opened directly here, so no command is
printed here. Community GGUF and MLX conversions already exist
([bartowski/LensVLM-9B-GGUF](https://huggingface.co/bartowski/LensVLM-9B-GGUF),
[mlx-community/LensVLM-9B-OptiQ-4bit](https://huggingface.co/mlx-community/LensVLM-9B-OptiQ-4bit)),
but whether the compress-and-expand tool loop works in a stock chat runtime is TBC.

## MiMo-V2.6-Distill-Qwen-9B

- Model card: [XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B)
- Publisher: Xiaomi MiMo. License: MIT
- Size: 9B; Qwen3.5-9B fine-tuned (SFT) on MiMo-generated data
- Released: late September (MiMo V2.6 shipped as Flash-RL, Pro-RL and Distill-Qwen-9B, per a [Sept 22 write-up](https://kenashe.ai/blog/2026-09-22-xiaomis-mimo-v2-6-ships-in-three-flavors-and-the-split-matters))

Training data spans coding, general agent tasks, visual coding and cybersecurity, and the checkpoint
is offered as a starting point for open agentic-RL research. The figures found: SWE-bench Verified 61.1
and SWE-bench Pro 44.6, both avg@3 ([summary](https://vast.ai/model/mimo-v26-distill-qwen-9b)). The full card table was not checked.

Run it (command confirmed in search results):

```bash
vllm serve "XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B"
```

That starts an OpenAI-compatible server. For local use there are GGUF builds such as
[bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF](https://huggingface.co/bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF).

## Same size, different job

LensVLM targets cheap reading of long documents; the MiMo distill targets running a coding agent on a
small model. Both fit the quantized-9B-on-a-laptop-GPU class, but memory needs and Raspberry Pi 5
feasibility were not confirmed from sources (TBC). Start with LensVLM for document search and
summarization pipelines, MiMo for local coding-agent experiments. LensVLM's Apple-specific license
needs reading before commercial use; MIT leaves MiMo nearly unrestricted.
