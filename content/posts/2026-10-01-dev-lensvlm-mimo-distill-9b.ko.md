---
title: "9B 두 개, 하나는 압축해 읽고 하나는 증류해 배운다"
seoTitle: "Apple LensVLM-9B·MiMo-V2.6-Distill-Qwen-9B 9B 모델 | Hugging Face 트렌딩"
date: 2026-10-01T03:12:05+09:00
slug: "dev-lensvlm-mimo-distill-9b"
summary: "이번 주 Hugging Face 트렌딩에서 긴 문서를 압축 이미지로 읽는 애플의 LensVLM-9B와, 코딩·에이전트 데이터로 Qwen3.5-9B를 미세조정한 샤오미 MiMo-V2.6-Distill-Qwen-9B를 골랐습니다. 라이선스와 벤치마크, 실행 방법을 정리했습니다."
tags: ["Hugging Face"]
categories: ["Dev Picks"]
draft: false
cover:
  image: "/images/posts/dev-lensvlm-mimo-distill-9b.ko.png"
  alt: "커버 카드: LensVLM-9B는 4.3배 압축에서 정확도 유지, MiMo-V2.6-Distill-Qwen-9B는 SWE-bench Verified 61.1"
  relative: false
---

이번 주 Hugging Face 트렌딩에는 같은 9B 크기, 같은 Qwen3.5-9B 기반이면서 목적이 전혀 다른 두 모델이 올라왔습니다. 하나는 긴 글을 이미지로 압축해 훑고 필요한 쪽만 펼쳐 읽는 모델이고, 다른 하나는 코딩·에이전트 작업 데이터로 다시 학습한 모델입니다. 트렌딩 순위는 집계 사이트([agents-radar 9월 28일 주간 집계](https://github.com/kakapez/agents-radar/issues/1614))에서 확인했고, 세부 사항은 각 모델 소개 자료를 따로 찾아 교차 확인했습니다.

## LensVLM-9B

- 모델 카드: [apple/LensVLM-9B](https://huggingface.co/apple/LensVLM-9B)
- 코드: [apple-aiml-research/ml-lensvlm](https://github.com/apple-aiml-research/ml-lensvlm)
- 논문 요약: [Apple Machine Learning Research](https://machinelearning.apple.com/research/lensvlm-context-expansion)
- 제작: Apple, 라이선스: Apple Machine Learning Research Model License(apple-amlr) — Apache-2.0이 아닙니다
- 크기: 9B, 기반 모델 Qwen3.5-9B, 태스크: 비전-언어(긴 문서 QA)
- 공개: 9월 21일 Apple의 Hugging Face 계정에 올라왔고 코드는 22일 GitHub에 공개됨

긴 텍스트를 이미지로 압축해서 읽고, 답에 필요한 페이지만 학습된 도구로 원래 해상도로 펼치는 방식입니다. 논문 요약에 따르면 7개 텍스트 QA 벤치마크에서 4.3배 유효 압축까지는 전체 텍스트를 그대로 읽은 상한선과 비슷한 정확도를 유지했고, 10.1배 압축까지 검색 기반·텍스트 압축·시각 압축 기준선을 앞섰습니다. 데모 스크립트는 5배·10배·15배 압축 옵션을 받습니다.

실행: 정확한 설치·실행 명령은 저장소 README를 따라야 하며, 이 글에서는 원문을 직접 열어 확인하지 못해 명령을 싣지 않습니다. 커뮤니티 GGUF·MLX 변환본([bartowski/LensVLM-9B-GGUF](https://huggingface.co/bartowski/LensVLM-9B-GGUF), [mlx-community/LensVLM-9B-OptiQ-4bit](https://huggingface.co/mlx-community/LensVLM-9B-OptiQ-4bit))이 이미 올라와 있어 노트북에서 돌려 볼 길은 열려 있습니다. 다만 압축·확장 도구 호출이 포함된 추론 흐름이 일반 채팅 런타임에서 그대로 동작하는지는 확인 필요입니다.

## MiMo-V2.6-Distill-Qwen-9B

- 모델 카드: [XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B)
- 제작: 샤오미 MiMo, 라이선스: MIT
- 크기: 9B, 기반 모델 Qwen3.5-9B를 MiMo가 생성한 데이터로 지도 미세조정(SFT)
- 공개: 9월 하순(MiMo V2.6이 Flash-RL·Pro-RL·Distill-Qwen-9B 세 가지로 나왔다는 [9월 22일자 해설](https://kenashe.ai/blog/2026-09-22-xiaomis-mimo-v2-6-ships-in-three-flavors-and-the-split-matters)로 확인)

코딩, 범용 에이전트, 비주얼 코딩, 사이버보안 작업 데이터를 섞어 학습했고, 에이전트 강화학습 연구의 출발점으로 쓰라고 내놓은 SFT 체크포인트입니다. 검색 결과로 확인된 수치는 SWE-bench Verified 61.1, SWE-bench Pro 44.6(둘 다 avg@3)입니다([출처 요약](https://vast.ai/model/mimo-v26-distill-qwen-9b)). 모델 카드의 전체 표는 직접 열어 보지 못했습니다.

실행(검색 결과로 확인된 명령):

```bash
vllm serve "XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B"
```

OpenAI 호환 API 서버가 뜹니다. 로컬용으로는 [bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF](https://huggingface.co/bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF) 같은 GGUF 변환본이 있습니다.

## 같은 9B, 다른 쓸모

LensVLM은 "긴 문서를 싸게 읽는" 문제를, MiMo 증류 모델은 "작은 모델로 코드 에이전트를 돌리는" 문제를 겨냥합니다. 노트북 GPU나 Jetson급 장비에서 9B를 양자화해 올릴 수 있다는 점은 같지만, 두 모델의 메모리 요구량과 Raspberry Pi 5 구동 가능성은 출처에서 확인하지 못했습니다(확인 필요). 문서 검색·요약 파이프라인이라면 LensVLM, 로컬 코딩 에이전트 실험이라면 MiMo 쪽이 출발점입니다. LensVLM은 애플 전용 라이선스라 상업 이용 조건을 먼저 읽어야 하고, MiMo는 MIT라 제약이 적습니다.
