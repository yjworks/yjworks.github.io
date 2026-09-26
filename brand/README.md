# DigitalBrain 브랜드 키트

허브(dibrain.dev), 블로그, 도구, 딴짓, 키즈랩, AI 샷이 같이 쓰는 모양·색·아이콘의 원본.
다른 저장소의 로고·아이콘·색을 바꿀 때는 **여기를 먼저 고치고** 복사한다.

## 파일

| 파일 | 내용 |
|---|---|
| `src/dibrain.svg` | 브랜드 마크. 파랑 둥근 사각형 + 흰 "네모와 반원" D |
| `src/dibrain-mono.svg` | 한 색 마크(Safari 고정 탭, 도장, 흑백 인쇄) |
| `src/<앱>.svg`, `src/<앱>-maskable.svg` | 앱 아이콘. maskable 은 모서리 없이 꽉 채운 판(안드로이드·iOS 홈 화면용) |
| `src/dibrain-wordmark.svg` | 글자 로고 "DigitalBrain"(Pretendard ExtraBold 윤곽선) |
| `src/dibrain-lockup.svg`, `src/dibrain-lockup-dark.svg` | 마크 + 글자 가로 조합(밝은 바탕 / 어두운 바탕) |
| `src/og-default.svg` | 링크 공유 미리보기 1200×630(마크 + 글자 + 한 줄 소개) |
| `wordmark.py` | 위 세 가지를 Pretendard 윤곽선으로 다시 만든다(`pip install fonttools brotli`) |
| `tokens.css` | 공통 색·글꼴·모서리·상단 바. 각 저장소에 그대로 복사 |
| `build.cjs` | 위 SVG 에서 PNG(16~512)·favicon.ico·maskable·apple-touch-icon 생성 → `dist/` |

```
NODE_PATH=<playwright 가 있는 node_modules> node brand/build.cjs
```

## 브랜드 마크

- 왼쪽 네모 = 디지털, 오른쪽 반원 = 두뇌. 둘이 모여 D.
- 반원은 네모보다 위아래로 0.8 씩 크다(둥근 모양이 같은 높이로 보이게 하는 시각 보정). 지우지 않는다.
- 최소 크기 16px. 주변 여백은 네모 폭(96 기준 22)의 절반 이상.
- 색은 `#2F6FED` 바탕 + 흰 마크, 또는 한 색(검정/흰색)만. 그라데이션·그림자·기울이기·다른 색 금지.
- 마크 경로(96×96 기준):

```html
<svg viewBox="0 0 96 96" aria-hidden="true"><rect width="96" height="96" rx="22" fill="#2f6fed"/><path fill="#fff" d="M25.5 24H40.5a3.5 3.5 0 0 1 3.5 3.5V68.5a3.5 3.5 0 0 1-3.5 3.5H25.5a3.5 3.5 0 0 1-3.5-3.5V27.5a3.5 3.5 0 0 1 3.5-3.5Z M49 23.2a24.8 24.8 0 0 1 0 49.6Z"/></svg>
```

## 앱 아이콘

모서리 22/96 둥근 사각형, 앱 강조색 바탕, 가운데 그림 하나. 캐릭터·사진·글자 로고 넣지 않음.

| 앱 | 바탕 | 그림 | 강조색(밝은 화면 / 어두운 화면) |
|---|---|---|---|
| 허브·도구·블로그 | `#2F6FED` | 브랜드 마크 | `#2F6FED` / `#7AA2FF` |
| 키즈랩 | `#F5B400` | 검정 별 | `#F5B400`(위 글자는 검정) |
| 딴짓 | `#E8590C` | 주사위 | 버튼 `#C2410C` / `#FF8A4C` |
| AI 샷 | `#6D4AE6` | 뷰파인더 + 셔터 | `#6D4AE6` / `#9D86FF` |
| clip-box | `#0F766E` | 필름 + 재생 | `#0F766E` / `#2DD4BF` |
| snap-box | `#BE185D` | 사진 틀 + 모자이크 | `#BE185D` / `#F472B6` |

글자가 올라가는 버튼 색은 글자와 대비 4.5:1 이상으로 골랐다(`--db-accent-bg` / `--db-on-accent`).

## 공통 상단 바

높이 52. 왼쪽 브랜드 마크(22px, 누르면 https://dibrain.dev/ ) + 앱 이름, 오른쪽 앱 버튼(누르는 곳 44px 이상).
**키즈랩은 예외**: 아이가 광고·도구가 있는 첫 화면으로 나가지 않게, 첫 화면 링크는 보호자 메뉴 안에만 둔다.

## 글꼴

Pretendard 하나(SIL Open Font License 1.1, 상업용 사용 가능). 오프라인 앱은 글꼴 파일을 저장소 안에 두고, 온라인 페이지는 jsDelivr 를 쓴다.

## 이름

- 이름은 **DigitalBrain** (한글 표기 디지털브레인). 글자 로고는 글꼴 없이도 같게 보이도록 윤곽선으로 저장했다.
- 상표: 2026-09-26 KIPRIS 국내 검색에서 "디지털브레인" 상표 등록은 없었다(같은 이름 회사의 다른 상표 1건, 36류, 소멸).
  영문 "DIGITAL BRAIN" 검색과 출원은 아직 하지 않았다. 출원한다면 글자만보다 마크 + 글자 조합이 식별력 면에서 유리하다.

## 도구와 앱의 기준

- **도구**: 한 페이지에서 다 해결되는 기능. `yjworks/tools` 저장소에 폴더 하나로 넣는다(`docs/TOOL-SPEC.md`).
  자주 쓰는 도구는 `"pwa": true` 로 설치만 가능하게 한다. 도구는 첫 화면의 도구 목록에 나온다.
- **앱**: AI 샷 정도 이상으로 화면·기능이 여럿 얽힌 것. 저장소를 따로 만든다. 첫 화면의 '앱' 칸에 나온다.

## 앱 추가

1. `yjworks/<앱>` 저장소를 만든다. 주소는 `dibrain.dev/<앱>/` 가 된다(저장소 이름 = 경로).
2. 이 키트를 적용한다: `tokens.css` 복사, 공통 상단 바, `src/<앱>.svg` 아이콘(`build.cjs` 에 이름 추가 후 PNG 생성).
   manifest `id` 는 `"/<앱>/"` 처럼 절대 경로로(다른 앱과 겹치지 않게).
3. 이 저장소 `.github/workflows/hugo.yml` 에 앱을 더한다: 최신 커밋 찾기(`sources`), 받아오기(`fetch`),
   빌드가 있으면 빌드, `site/<앱>/` 로 복사. 그러면 30분 점검 때 함께 배포된다.
4. `hub/index.html` 의 앱 칸에 카드를 넣고 `scripts/build_hub.py` 의 `FIXED_APPS` 와 스크립트의 `FIXED_APPS` 숫자를 올린다.
