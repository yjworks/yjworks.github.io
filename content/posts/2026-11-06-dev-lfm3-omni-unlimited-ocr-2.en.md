---
title: "LFM3-Omni-2B Is the One You Can Put on a Device Today"
seoTitle: "LFM3-Omni-2B and Unlimited-OCR-2: On-Device Omni Model and Long-Document OCR | Hugging Face Trending"
date: 2026-11-06T06:29:17+09:00
slug: "dev-lfm3-omni-unlimited-ocr-2"
summary: "From this week's Hugging Face trending list: Liquid AI's LFM3-Omni-2B, a 2.2B model that listens, sees and speaks, and Baidu's Unlimited-OCR-2, a 3.34B OCR model that parses hundreds of pages in one pass. Licenses, benchmarks, run commands and whether they fit on edge hardware."
tags: ["Hugging Face"]
categories: ["Dev Picks"]
cover:
  image: "/images/posts/dev-lfm3-omni-unlimited-ocr-2.en.png"
  alt: "Cover card: LFM3-Omni-2B has 2.2B parameters and a 1.1GB Q4_K_M GGUF; Unlimited-OCR-2 has 3.34B parameters and is 7.0x faster per decoding step at hundred-page scale"
  relative: false
draft: true
---

If a device runs separate models for speech recognition, image understanding, chat and text-to-speech, can one model replace all four? This week's Hugging Face trending list has a 2B-class model built around that question, alongside a 3B-class OCR model that goes the other way: it wants a server GPU so it can read a few hundred pages in a single request.

On the [Hugging Face trending page](https://huggingface.co/models?sort=trending) on the morning of November 6, 2026 (KST), Unlimited-OCR-2 sat at #23 and LFM3-Omni-2B at #29. Sizes, licenses and commands below come from each model card.

## LFM3-Omni-2B: one 2.2B model that listens, sees and talks back

- Model card: [LiquidAI/LFM3-Omni-2B](https://huggingface.co/LiquidAI/LFM3-Omni-2B)
- GGUF: [LiquidAI/LFM3-Omni-2B-GGUF](https://huggingface.co/LiquidAI/LFM3-Omni-2B-GGUF)
- Made by Liquid AI, license: LFM Open License v1.0
- Size: 2.17B, 32K-token context
- Released October 27 with the six-model LFM3 family ([MarkTechPost](https://www.marktechpost.com/2026/10/27/liquid-ai-lfm3-open-weight-2b-multimodal-models/))

It takes text, images, video (with or without its soundtrack) and 16 kHz audio, and answers in text, 24 kHz speech, or both interleaved. The model card pitches it as a single replacement for a separate ASR model, vision-language model, LLM and TTS model. Korean is on both the text and speech language lists.

Selected numbers from the model card (all measured by Liquid AI):

| Metric | LFM3-Omni-2B | Qwen2.5-Omni 3B | Qwen2.5-Omni 7B |
|---|---|---|---|
| Total parameters | 2.2B | 6B | 10.7B |
| Daily-Omni (video + audio) | 70.09 | 58.81 | 61.32 |
| English ASR WER (lower is better) | 6.36 | 6.30 | — |
| Multilingual ASR WER/CER (9 languages incl. Korean, lower is better) | 6.72 | 7.41 | — |

Sources: [LiquidAI/LFM3-Omni-2B model card](https://huggingface.co/LiquidAI/LFM3-Omni-2B)

> **Not yet disclosed:** per-language ASR error rates, and measured speed on a Raspberry Pi 5 or Jetson. We'll update this post when they are.

This is not Apache-2.0. Under the LFM Open License v1.0, commercial use is only granted to organizations below $10 million in annual revenue ([LICENSE](https://huggingface.co/LiquidAI/LFM3-Omni-2B/raw/main/LICENSE), section 5). Hobby, research and small-company use is fine; anyone shipping it in a product should check that threshold first.

Run it with llama.cpp (commands from the GGUF repo card):

```bash
llama serve -hf LiquidAI/LFM3-Omni-2B-GGUF:Q4_K_M --reasoning off --temp 0 --port 8080

llama cli -hf LiquidAI/LFM3-Omni-2B-GGUF:Q4_K_M \
  --image photo.png -p "Describe this image." --temp 0

llama cli -hf LiquidAI/LFM3-Omni-2B-GGUF:Q4_K_M \
  --audio speech.wav -sys "Perform ASR in English." -p "<__media__>" --temp 0
```

Or with Transformers for speech recognition (model card example):

```bash
pip install "transformers>=5.20.2" torch torchvision torchcodec accelerate pillow librosa soundfile
```

```python
import torch
import soundfile as sf

from transformers import AutoModelForMultimodalLM, AutoProcessor

model_id = "LiquidAI/LFM3-Omni-2B"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if device == "cuda" else torch.float32

model = AutoModelForMultimodalLM.from_pretrained(
    model_id, dtype=dtype, device_map=device, trust_remote_code=True
).eval()
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
codec = processor.audio_tokenizer.to(device=device).eval()

conversation = [
    {"role": "system", "content": "Perform ASR in English."},
    {"role": "user", "content": [{"type": "audio", "audio": "audio.wav"}]},
]

inputs = processor.apply_chat_template(
    conversation,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(device)
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=1024, generation_mode="text")
text = processor.decode(
    outputs.sequences[0, inputs["input_ids"].shape[1]:outputs.sequence_lengths[0]],
    skip_special_tokens=True,
)
print(text)
```

## Unlimited-OCR-2: a 3.34B model that reads a whole document in one request

- Model card: [baidu/Unlimited-OCR-2](https://huggingface.co/baidu/Unlimited-OCR-2)
- Code: [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)
- Paper: [Unlimited OCR Works 2 (arXiv)](https://arxiv.org/abs/2610.39308)
- Made by Baidu, license: MIT
- Size: 3.34B (per the repo's safetensors metadata), about 6.7GB of BF16 weights
- Released October 27 (model card release notes)

Instead of OCR-ing page by page, it parses a multi-page document in one request so later pages can use earlier context. The usual problem is that attention cost grows with document length; Unlimited-OCR-2 caps the tokens each decoder step attends to with Sparse Reference Sliding Window Attention (SR-SWA). The paper abstract reports 7.0x and 5.6x per-step speedups over full attention and the earlier R-SWA at hundred-page scale, and state-of-the-art results on MPDocBench and Baidu's new hundred-page benchmark, MarathonDocBench. Those scores are the authors' own.

Run it with Transformers (model card example, tested on an NVIDIA A800-80GB):

```bash
pip install torch==2.13.0 torchvision pillow transformers==4.52.1 huggingface-hub==0.36.0 \
  tokenizers==0.21.4 addict==2.4.0 einops==0.8.2 easydict==1.13
```

```python
import torch
from transformers import AutoModel, AutoTokenizer

model_name = "baidu/Unlimited-OCR-2"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True, use_safetensors=True,
                                  torch_dtype=torch.bfloat16).eval().cuda()

# Single page
text = model.infer(tokenizer, image_file="your_doc/page_1.jpg",
                   output_path="output/single", save_results=True)

# Multiple pages in one request, in page order
pages = [f"your_doc/page_{i}.jpg" for i in range(1, 8)]
text, num_tokens = model.infer_multi(tokenizer, image_files=pages,
                                     output_path="output/multi", save_results=True)
```

The example calls `.cuda()`, so it expects an NVIDIA GPU as written. For batch work the model card recommends an SGLang server built from a custom wheel.

## Where each one actually fits

Liquid AI publishes its own GGUF for LFM3-Omni-2B: 1.1GB for the Q4_K_M model plus 0.29GB for the Q4_K_M vision/audio projector ([file list](https://huggingface.co/LiquidAI/LFM3-Omni-2B-GGUF)). That is small enough to try on a 4GB board, but nobody has published Raspberry Pi 5 or Jetson numbers yet, so real-time voice chat on that class of hardware is unconfirmed.

Unlimited-OCR-2's official path is a CUDA GPU with about 6.7GB of BF16 weights. Community GGUF, MLX and LiteRT conversions already exist, but whether SR-SWA and multi-page parsing survive those runtimes is unverified. For now it belongs on a server that turns long PDFs into Markdown.

If you build a robot or kiosk with a microphone and camera and want fewer models in the stack, LFM3-Omni-2B is the one to try first — after checking the revenue cap. If the job is turning hundreds of pages of reports or manuals into structured text, MIT-licensed Unlimited-OCR-2 on a GPU server is the starting point.
