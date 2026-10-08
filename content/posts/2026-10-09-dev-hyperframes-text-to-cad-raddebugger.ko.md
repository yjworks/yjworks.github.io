---
title: "에이전트가 영상과 CAD를 뽑고, 디버거는 아직 알파"
seoTitle: "HyperFrames·text-to-cad·RAD Debugger 사용법 | GitHub 트렌딩"
date: 2026-10-09T03:12:38+09:00
slug: "dev-hyperframes-text-to-cad-raddebugger"
summary: "이번 주 GitHub 주간 트렌딩에서 HTML로 영상을 렌더링하는 HyperFrames, 에이전트에게 3D CAD 모델링을 맡기는 text-to-cad, 에픽게임즈의 그래픽 디버거 RAD Debugger를 골라 라이선스와 설치 방법, 현재 한계를 정리했습니다."
tags: ["GitHub"]
categories: ["Dev Picks"]
cover:
  image: "/images/posts/dev-hyperframes-text-to-cad-raddebugger.ko.png"
  alt: "커버 카드: HyperFrames 스타 5만 9천 개, text-to-cad 스타 1만 8천 개, RAD Debugger 스타 8천 개, RAD Debugger 지원 범위 Windows x64"
  relative: false
draft: true
---

AI 에이전트에게 코드만 짜게 하던 시기가 지나고, 영상과 3D 모델 같은 결과물까지 맡기는 저장소가 GitHub 주간 트렌딩에 올라왔습니다. 같은 목록에는 에이전트와 전혀 상관없는 네이티브 디버거도 있어서, 방향이 다른 세 개를 골랐습니다. 스타 수와 주간 증가분은 2026년 10월 9일 [GitHub 주간 트렌딩](https://github.com/trending?since=weekly) 화면 기준입니다.

| 저장소 | 총 스타 | 이번 주 증가 | 라이선스 |
|---|---|---|---|
| heygen-com/hyperframes | 59,060 | 3,908 | Apache 2.0 |
| earthtojake/text-to-cad | 18,430 | 1,800 | MIT |
| EpicGames/raddebugger | 8,053 | 257 | MIT |

출처: [GitHub Trending (weekly)](https://github.com/trending?since=weekly), [hyperframes](https://github.com/heygen-com/hyperframes), [text-to-cad](https://github.com/earthtojake/text-to-cad), [raddebugger](https://github.com/EpicGames/raddebugger)

> **아직 확인하지 못한 것:** 세 저장소 모두 GitHub Releases 항목이 비어 있어 최신 릴리스 번호와 날짜를 확인하지 못했습니다.

## HyperFrames: HTML을 써서 MP4로 굽습니다

[HyperFrames](https://github.com/heygen-com/hyperframes)는 README 설명으로 "HTML, CSS, 미디어, 탐색 가능한 애니메이션을 결정론적인 MP4 영상으로" 만드는 오픈소스 프레임워크입니다. CLI로 직접 쓸 수도 있고, AI 코딩 에이전트에 스킬로 붙이거나 렌더링 코어로 쓸 수도 있다고 합니다. 요구 사항은 Node.js 22 이상과 FFmpeg입니다.

```bash
npx hyperframes init my-video
cd my-video
npx hyperframes preview      # 브라우저에서 실시간 미리보기
npx hyperframes render       # MP4로 렌더링
```

Claude Code 플러그인으로 쓰려면 README는 아래 두 줄을 안내합니다.

```bash
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```

영상을 "타임라인 편집"이 아니라 "웹 페이지 작성"으로 바꿔 놓았다는 점이 요점입니다. 에이전트가 이미 잘 쓰는 HTML과 CSS로 장면을 만들고, 같은 입력에서 같은 영상이 나오도록(결정론적) 렌더링하는 구조입니다. 렌더링 속도나 해상도 한계는 확인한 자료가 없어 적지 않습니다.

추천 대상: 제품 소개나 데이터 리포트 영상을 반복 생성해야 하고, 편집 툴 대신 코드로 관리하고 싶은 팀.

## text-to-cad: 에이전트가 STEP·STL 파일을 만듭니다

[text-to-cad](https://github.com/earthtojake/text-to-cad)는 MIT 라이선스 플러그인입니다. README는 에이전트가 "STEP, GLB, STL, 3MF 파일로 3D 모델을 생성하는 로컬 워크플로"를 쓰게 해 주고, 제조 적합성 검사(DFM)와 공학 도면 생성, 제작 서비스 연결까지 다룬다고 설명합니다. Python 3.11 이상과 Node.js 20 이상 배지가 붙어 있습니다.

설치는 쓰는 에이전트마다 다릅니다. Claude Code 기준은 다음과 같습니다.

```bash
claude plugin marketplace add earthtojake/text-to-cad#latest
claude plugin install text-to-cad@earthtojake
```

그 밖에 Codex, Cursor, Gemini용 명령과, 스킬만 쓰는 `npx skills add earthtojake/text-to-cad#latest` 가 README에 있습니다.

**쓰기 전에 알아 둘 조건이 있습니다.** README는 CAD 실행에 `uv`가 필요하고, 처음 시작할 때 CAD 런타임을 내려받으려면 네트워크가 있어야 한다고 적었습니다. Windows 11에서는 스마트 앱 컨트롤을 꺼야 하며, 아니면 WSL에서 CAD 스킬을 돌려야 `OCP`가 불러와집니다. 원격 측정은 기본으로 켜져 있고 `uvx cadgen telemetry off`로 끌 수 있습니다.

임베디드·하드웨어 쪽에서는 케이스나 브래킷 같은 부품의 초안을 STL로 뽑아 3D 프린터로 보내는 용도가 가장 가깝습니다. 생성된 모델의 정밀도나 공차는 확인한 자료가 없어 판단하지 않습니다.

추천 대상: 3D 프린팅용 부품을 자주 설계하고, 파라미터 수정을 코드처럼 반복하고 싶은 개발자.

## RAD Debugger: 지금은 Windows x64 로컬 디버깅만 됩니다

[RAD Debugger](https://github.com/EpicGames/raddebugger)는 에픽게임즈 조직 저장소이고 MIT 라이선스입니다. README는 이것을 "네이티브, 사용자 모드, 다중 프로세스 그래픽 디버거"라고 소개합니다. 같은 저장소에 디버그 정보 형식인 RDI와, 아주 큰 실행 파일의 빠른 링킹을 목표로 하는 RAD Linker도 들어 있습니다.

에이전트와는 무관한 저장소가 한 주에 257개 스타를 더한 것은 눈에 띄지만, **README가 스스로 알파라고 밝히고 있습니다.** 현재는 PDB를 쓰는 로컬 Windows x64 디버깅만 지원하고, 리눅스 네이티브 디버깅과 DWARF 지원은 계획 단계입니다. 리눅스 x64는 빌드 대상이지만 디버깅 대상은 아직 아닙니다.

빌드 명령은 README에 아래처럼 나옵니다. 성공하면 `build` 폴더에 `raddbg.exe`(Windows) 또는 `raddbg`(리눅스) 바이너리가 생깁니다.

```bash
# Windows x64
build release

# Linux x64
./build.sh release
```

추천 대상: Windows에서 MSVC 계열 C/C++ 프로그램을 디버깅하며 대체 도구를 찾는 개발자. 리눅스나 임베디드 타깃 디버깅이 목적이라면 아직 쓸 단계가 아닙니다.

## 같은 트렌딩, 쓸 수 있는 시점은 다릅니다

HyperFrames와 text-to-cad는 명령 몇 줄로 오늘 시험해 볼 수 있지만 둘 다 에이전트 환경이 갖춰져 있어야 합니다. RAD Debugger는 설치가 간단해도 지원 범위가 Windows x64로 좁습니다. 스타 수가 많은 순서가 아니라, 내 작업 환경이 각 저장소의 전제 조건과 맞는지를 먼저 보는 편이 안전합니다.
