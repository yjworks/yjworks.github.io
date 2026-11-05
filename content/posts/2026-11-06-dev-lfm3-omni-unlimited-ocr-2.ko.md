---
title: "기기에 바로 올릴 쪽은 LFM3-Omni-2B입니다"
seoTitle: "LFM3-Omni-2B·Unlimited-OCR-2 온디바이스 음성·긴 문서 OCR 모델 | Hugging Face 트렌딩"
date: 2026-11-06T07:09:08+09:00
slug: "dev-lfm3-omni-unlimited-ocr-2"
summary: "Hugging Face 트렌딩에서 듣고 보고 말하는 2.2B 옴니 모델 Liquid AI LFM3-Omni-2B와, 수백 쪽 문서를 한 번에 읽는 3.34B OCR 모델 Baidu Unlimited-OCR-2를 골랐습니다. 라이선스, 벤치마크, 실행 명령, 기기에 올릴 수 있는지를 정리했습니다."
tags: ["Hugging Face"]
categories: ["Dev Picks"]
cover:
  image: "/images/posts/dev-lfm3-omni-unlimited-ocr-2.ko.png"
  alt: "커버 카드: LFM3-Omni-2B는 2.2B 파라미터에 Q4_K_M GGUF 1.1GB, Unlimited-OCR-2는 3.34B 파라미터에 100쪽 규모에서 단계당 7.0배 빠름"
  relative: false
draft: false
reviewed: "2026-11-06"
---

음성 인식, 이미지 이해, 답변 생성, 음성 합성을 모델 네 개로 나눠 돌리는 기기라면 하나로 줄일 수 있을까요? 이번 주 Hugging Face 트렌딩에는 그 질문에 답하려는 2B급 모델과, 반대로 서버 GPU에서 수백 쪽 문서를 한 번에 읽으려는 3B급 OCR 모델이 함께 올라왔습니다.

순위는 2026년 11월 6일 오전 [Hugging Face 트렌딩](https://huggingface.co/models?sort=trending) 기준으로 Unlimited-OCR-2가 23위, LFM3-Omni-2B가 29위였습니다. 크기·라이선스·실행 명령은 각 모델 카드 원문에서 확인했습니다.

## LFM3-Omni-2B: 듣고 보고 말하는 2.2B 모델

- 모델 카드: [LiquidAI/LFM3-Omni-2B](https://huggingface.co/LiquidAI/LFM3-Omni-2B)
- GGUF: [LiquidAI/LFM3-Omni-2B-GGUF](https://huggingface.co/LiquidAI/LFM3-Omni-2B-GGUF)
- 제작: Liquid AI, 라이선스: LFM Open License v1.0
- 크기: 2.17B, 컨텍스트 32K 토큰
- 공개: 10월 27일 LFM3 제품군 6종과 함께 공개([MarkTechPost](https://www.marktechpost.com/2026/10/27/liquid-ai-lfm3-open-weight-2b-multimodal-models/))

텍스트, 이미지, 동영상(소리 포함), 16kHz 오디오를 입력으로 받고, 텍스트와 24kHz 음성으로 답합니다. 모델 카드는 음성 인식(ASR), 비전-언어 모델, LLM, 음성 합성(TTS)을 모델 하나로 대신하도록 만들었다고 설명합니다. 텍스트 언어와 음성 언어 목록 모두에 한국어가 들어 있습니다.

모델 카드의 표(모두 Liquid AI가 측정)에서 눈에 띄는 값은 다음과 같습니다.

| 항목 | LFM3-Omni-2B | Qwen2.5-Omni 3B | Qwen2.5-Omni 7B |
|---|---|---|---|
| 전체 파라미터 | 2.2B | 6B | 10.7B |
| Daily-Omni(영상+소리) | 70.09 | 58.81 | 61.32 |
| 영어 ASR WER(낮을수록 좋음) | 6.36 | 6.30 | — |
| 다국어 ASR WER/CER(한국어 포함 9개 언어, 낮을수록 좋음) | 6.72 | 7.41 | — |

출처: [LiquidAI/LFM3-Omni-2B 모델 카드](https://huggingface.co/LiquidAI/LFM3-Omni-2B)

> **아직 공개되지 않은 것:** 한국어 단독 ASR 오류율, Raspberry Pi 5·Jetson에서 잰 속도. 공식 자료가 나오면 이 글을 고칩니다.

라이선스는 Apache-2.0이 아닙니다. LFM Open License v1.0은 연 매출 1,000만 달러 이상인 법인의 상업적 이용을 허용하지 않습니다([LICENSE](https://huggingface.co/LiquidAI/LFM3-Omni-2B/raw/main/LICENSE) 5조). 개인·연구용이나 작은 회사는 쓸 수 있지만, 제품에 넣기 전에 회사 규모부터 확인해야 합니다.

실행 1 — llama.cpp(모델 카드의 GGUF 저장소 명령 그대로):

```bash
llama serve -hf LiquidAI/LFM3-Omni-2B-GGUF:Q4_K_M --reasoning off --temp 0 --port 8080

llama cli -hf LiquidAI/LFM3-Omni-2B-GGUF:Q4_K_M \
  --image photo.png -p "Describe this image." --temp 0

llama cli -hf LiquidAI/LFM3-Omni-2B-GGUF:Q4_K_M \
  --audio speech.wav -sys "Perform ASR in English." -p "<__media__>" --temp 0
```

실행 2 — Transformers로 음성 인식(모델 카드 예제):

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

모델 카드 예제의 시스템 프롬프트는 영어 ASR입니다. 한국어 음성에 같은 방식으로 언어만 바꿔 쓸 수 있는지는 확인 필요입니다.

## Unlimited-OCR-2: 수백 쪽 문서를 한 번에 읽는 3.34B 모델

- 모델 카드: [baidu/Unlimited-OCR-2](https://huggingface.co/baidu/Unlimited-OCR-2)
- 코드: [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)
- 논문: [Unlimited OCR Works 2 (arXiv)](https://arxiv.org/abs/2610.39308)
- 제작: Baidu, 라이선스: MIT
- 크기: 3.34B(모델 저장소의 safetensors 기준), 가중치 파일 합계 약 6.7GB(BF16)
- 공개: 10월 27일(모델 카드 Release 항목)

여러 쪽짜리 문서를 쪽마다 따로 읽지 않고 한 요청으로 읽어, 앞쪽 내용을 이어 받아 정리하는 OCR 모델입니다. 문서가 길어지면 어텐션 계산이 커지는 문제를, 디코더가 참조하는 토큰을 고정 개수로 묶는 SR-SWA(Sparse Reference Sliding Window Attention)로 풀었습니다. 논문 초록에 따르면 100쪽 규모에서 디코딩 단계당 속도가 전체 어텐션 대비 7.0배, 이전 방식(R-SWA) 대비 5.6배 빠르고, MPDocBench와 직접 만든 100쪽 단위 벤치마크 MarathonDocBench에서 최고 성능을 냈다고 합니다. 점수는 제작사 측정입니다.

실행 — Transformers(모델 카드 예제, NVIDIA A800-80GB에서 시험됨):

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

# 한 쪽
text = model.infer(tokenizer, image_file="your_doc/page_1.jpg",
                   output_path="output/single", save_results=True)

# 여러 쪽을 한 요청으로(쪽 순서대로)
pages = [f"your_doc/page_{i}.jpg" for i in range(1, 8)]
text, num_tokens = model.infer_multi(tokenizer, image_files=pages,
                                     output_path="output/multi", save_results=True)
```

예제는 `.cuda()` 를 부르므로 NVIDIA GPU가 있어야 그대로 돕니다. 대량 처리용으로는 모델 카드가 SGLang 서버(전용 휠 필요)를 권합니다.

## 기기에 올릴 수 있는지가 둘을 가릅니다

LFM3-Omni-2B는 제작사가 직접 GGUF를 올렸고, Q4_K_M 본체 1.1GB에 비전·오디오 프로젝터(mmproj) Q4_K_M 0.29GB입니다([파일 목록](https://huggingface.co/LiquidAI/LFM3-Omni-2B-GGUF)). 파일 크기로 보면 RAM 4GB급 보드에도 올려 볼 만하지만, Raspberry Pi 5나 Jetson에서 실시간 음성 대화가 되는 속도인지는 측정 자료가 없어 확인 필요입니다.

Unlimited-OCR-2는 공식 예제가 CUDA GPU 기준이고 BF16 가중치만 약 6.7GB입니다. 커뮤니티 GGUF·MLX·LiteRT 변환본이 이미 여럿 올라와 있지만, 이 모델의 핵심인 SR-SWA와 여러 쪽 한 번에 읽기가 그 런타임에서도 그대로 동작하는지는 확인 필요입니다. 지금은 사내 서버에서 긴 PDF를 마크다운으로 바꾸는 파이프라인 쪽이 맞는 자리입니다.

정리하면, 음성·카메라가 달린 로봇이나 키오스크에서 모델 개수를 줄이고 싶다면 LFM3-Omni-2B가 바로 시험해 볼 대상입니다(상업 이용 매출 기준은 먼저 확인). 수백 쪽 보고서·매뉴얼을 구조를 살려 텍스트로 옮기는 작업이라면 MIT 라이선스의 Unlimited-OCR-2를 GPU 서버에 올리는 쪽이 출발점입니다.
