---
title: "MiniCPM5 Wins Big, Flash-Next Spends Small"
seoTitle: "MiniCPM5-2B and Qwen3.8-Flash-Next | Hugging Face Trending"
date: 2026-09-17T10:10:00+09:00
slug: "dev-minicpm5-qwen-flash-next"
summary: "This week's Hugging Face trending picks: MiniCPM5-2B, a 2.52B on-device model that beats a 4B rival, and Qwen3.8-Flash-Next, a 125B MoE that only wakes up 6B parameters per token."
tags: ["Hugging Face"]
categories: ["Dev Picks"]
draft: false
cover:
  image: "/images/posts/dev-minicpm5-qwen-flash-next.en.png"
  alt: "Cover card: MiniCPM5-2B at 2.52B parameters, Qwen3.8-Flash-Next at 6B active per token, both with GGUF on-device builds"
  relative: false
---

Two picks from this week's Hugging Face trending list take opposite routes to the same goal.
One shrinks the whole model to win. The other keeps the total size but only wakes up a fraction
of it per token. Both target the same practical problem — running a capable model without
sending every request to someone else's cloud — but they solve it at completely different
scales. If you want something to run on your own hardware, both are worth a look.

## MiniCPM5-2B

- Model card: [openbmb/MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B)
- Source: [GitHub - OpenBMB/MiniCPM](https://github.com/openbmb/minicpm)
- Publisher: OpenBMB
- License: Apache-2.0
- Parameters: 2.52B dense, 42 layers, GQA (16 query heads / 2 KV heads)
- Context: 131,072 tokens
- Released: 2026-09-07

The second checkpoint in the MiniCPM5 line, built for local and on-device use rather than
cloud serving. Its grouped-query attention setup — 16 query heads sharing just 2 key/value
heads — is one of the reasons it stays light enough for phone-class memory budgets while
still handling a 131K-token context. OpenBMB's own numbers put its average across 34
benchmarks at 53.9, ahead of the larger Qwen3.5-4B at 51.1, despite having roughly half the
parameters. Standouts include MATH-500 at 94.6, AIME 2026 at 86.5, LiveCodeBench v6 at 69.1,
SWE-bench Verified at 46.4, τ²-Bench Telecom at 97.1, and GAIA Text-103 at 88.7 (all OpenBMB's
own figures). It shipped same-day in GGUF, MLX, GPTQ, and mobile-oriented LiteRT builds, so
it's ready to try on a laptop or a phone-class device right away, without waiting on a
community quantization pass.

Run example (transformers):

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "openbmb/MiniCPM5-2B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype="auto", device_map="auto"
)
messages = [{"role": "user", "content": "Who are you?"}]
inputs = tokenizer.apply_chat_template(
    messages, tokenize=True, add_generation_prompt=True,
    enable_thinking=True, return_dict=True, return_tensors="pt"
).to(model.device)
outputs = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:]))
```

It also runs out of the box on Ollama, llama.cpp, LM Studio, and vLLM. **Good for**: developers
who want to run coding, math, or agentic workloads locally without server costs, or teams
building an on-device chatbot.

## Qwen3.8-Flash-Next

- Model card: [Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- GGUF: [unsloth/Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)
- Publisher: Qwen Team, Alibaba Group
- License: Qwen Community License 1.0 (services over 100M monthly active users or $20M
  monthly revenue, and Model-as-a-Service or AI work-assistant businesses, need a separate
  license — not Apache-2.0)
- Parameters: sources disagree here — Qwen's own material describes 125B total with 6B
  active per token (512 experts, 10 routed + 1 shared), plus a separate 51B n-gram embedding
  and a 4B MTP layer; some third-party write-ups add these up to a 177B total. TBC.
- Context: 262,144 tokens
- Task: multimodal (text + vision) MoE
- Released: 2026-08-26

Released as the first open-weight preview of the architecture behind Qwen4. The hybrid design
repeats three Gated DeltaNet layers plus one Qwen Sparse Attention (QSA) block across the
network; QSA operates at the micro-block level rather than per token, which is what lets the
262K-token context stay usable for agentic workloads instead of falling off a latency cliff.
The sparse MoE routing — 512 experts with 10 routed plus 1 shared expert active at a time —
is the whole point: only 6B of the total footprint actually does compute for any given token,
even though the full checkpoint has to sit in memory. Community GGUF quantizations run in
roughly 82GB at 4-bit (58GB for the main model plus 24GB for the n-gram component), so 75GB
or more of unified memory is enough with no discrete GPU required. One community report has
an 85GB quant running on an M5 Max Mac with 64GB of memory at 36 tokens/sec with vision input
(third-party benchmark, not an official figure). Treat this as workstation-class on-device,
not phone-class — it needs serious unified memory or a multi-GPU box, just not a datacenter.

Run example (vLLM):

```bash
vllm serve Qwen/Qwen3.8-Flash-Next --port 8000 --tensor-parallel-size 4
```

GGUF builds load directly in llama.cpp. **Good for**: developers with a high-memory unified
Mac or a multi-GPU box who want an early look at the Qwen4-generation architecture.

## Wrap-up

Both models chase "on-device" from opposite directions. MiniCPM5-2B shrinks the parameter
count itself down to 2.52B, low enough to reach phones. Qwen3.8-Flash-Next keeps a 125B total
but caps active parameters per token at 6B, aiming at high-memory Macs and workstations
instead. Need something light to run locally today? Go with MiniCPM5-2B. Want a preview of
where the next architecture generation is headed? Qwen3.8-Flash-Next is the one to try.
