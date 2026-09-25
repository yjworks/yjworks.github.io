---
name: my-post
description: 운영자(yjworks)가 직접 해 본 것을 글로 올릴 때 쓴다. 사용자가 준 메모·측정값·사진을 사용자의 말투 그대로 정리해 categories Hands-on 글(ko, 원하면 en)로 만들고, 사용자가 확인한 뒤에만 main에 발행한다. 자동 발행(weekly-post)과 달리 사실을 조사해 채우지 않고, 사용자가 말하지 않은 경험·수치를 만들어 내지 않는다.
---

# my-post — 운영자가 직접 쓴 글

이 글은 사이트에서 **"yjworks 직접 작성"** 표시가 붙는다. 그 표시가 참이려면 내용이 전부 사용자에게서 나와야 한다.

## 절대 규칙

- **사용자가 말하지 않은 경험, 수치, 부품, 결과를 만들어 넣지 않는다.** 빈 곳이 있으면 채우지 말고 물어본다.
  예: "서보 몇 개를 동시에 돌렸나요?", "측정은 어떤 장비로 했나요?"
- 사용자의 표현을 최대한 살린다. 고치는 것은 맞춤법, 문장 순서, 중복 정도. 말투를 매끈한 기사체로 바꾸지 않는다.
  "~했는데 안 되더라고요" 같은 말은 그대로 둔다(존댓말은 유지).
- 전압·전류 정격, 핀맵, 타이밍 같은 하드웨어 사실을 **보태는** 경우에는 데이터시트 출처를 달고, 사용자에게 보태도 되는지 먼저 묻는다.
- 회사 프로젝트(Pibo, pibo-lab, 회사 내부 자료)는 쓰지 않는다. 사용자가 명시적으로 공개해도 된다고 한 것만 쓴다.
- **발행 전에 반드시 초안 전체를 보여주고 OK를 받는다.**

## 1. 받을 것

사용자에게서 받는다. 없는 것은 물어본다(한 번에 모아서).

1. 무엇을 하려고 했나
2. 무엇을 썼나 — 보드·부품·라이브러리 이름과 버전(영문 원문 그대로)
3. 해 보니 어땠나 — 측정값, 동작 여부, 스크린샷·사진
4. 막힌 것과 푼 방법
5. 다음에 다르게 할 것 / 추천하는 사람

## 2. 사진

사진 파일이 작업 폴더에 들어와 있으면(첨부가 파일로 들어왔거나 사용자가 저장소에 올린 경우) 처리한다.
파일이 없으면 사용자에게 GitHub 웹에서 `static/images/uploads/` 에 올려 달라고 안내한다.

**위치 정보(EXIF GPS)를 반드시 지운다.** 폰 사진에는 집·회사 좌표가 들어 있다.

```bash
python3 - <<'PY'
from PIL import Image, ImageOps
import sys, pathlib
src, dst = sys.argv[1], sys.argv[2]
im = ImageOps.exif_transpose(Image.open(src))      # 회전 반영
im.thumbnail((1600, 1600))                          # 긴 변 1600px
im.convert("RGB").save(dst, "JPEG", quality=85)     # EXIF 없이 새로 저장
print("saved", dst, im.size)
PY
```

- 저장 위치: `static/images/uploads/YYYY-MM-DD-<slug>-<n>.jpg`. 원본은 커밋하지 않는다.
- 저장 후 `python3 -c "from PIL import Image; print(Image.open('<dst>').getexif())"` 가 빈 값인지 확인한다.
- 사진에 사람 얼굴, 모니터 속 사내 화면, 회사 로고가 보이면 사용자에게 알리고 쓸지 묻는다.
- 첫 사진을 커버로 쓴다. 커버 카드(postimg.py)는 쓰지 않는다. 직접 찍은 사진이 이 글의 증거다.

## 3. 파일

```
content/posts/YYYY-MM-DD-handson-<slug>.ko.md
content/posts/YYYY-MM-DD-handson-<slug>.en.md   # 사용자가 원할 때만
```

- 날짜: `TZ=Asia/Seoul date +%FT%T+09:00` 출력 그대로.
- slug 는 `handson-` 로 시작한다. 자동 발행이 이 접두어를 보고 운영자 글로 인식한다.

```yaml
---
title: "<사용자와 정한 제목>"
seoTitle: "<검색어가 들어간 제목. 부품명·보드명 + 무엇을 했는지>"
date: <명령 출력>
slug: "handson-<slug>"
summary: "<무엇을 해 봤고 결과가 어땠는지 한두 문장>"
tags: ["SBC"]                     # data/topics.yaml 의 주제 태그 중 해당하는 것
categories: ["Hands-on"]
cover:
  image: "/images/uploads/YYYY-MM-DD-<slug>-1.jpg"
  alt: "<사진에 실제로 보이는 것>"
  relative: false
draft: false
---
```

본문은 1인칭("제가", "저는")으로. 순서는 1번의 다섯 가지를 따르되 소제목은 내용으로 쓴다.
코드가 있으면 사용자가 실제로 돌린 코드만 넣는다. 의사코드 금지.

영어판은 사용자의 글을 영어권 독자에 맞게 옮긴 것이다. 새 내용을 보태지 않는다.

## 4. 확인과 발행

1. 초안 전체를 사용자에게 보여 주고, 보탠 것이 있으면 무엇을 보탰는지 따로 적는다.
2. OK를 받으면:

```bash
git add content/posts/YYYY-MM-DD-handson-<slug>.*.md static/images/uploads/YYYY-MM-DD-<slug>-*.jpg
git -c user.name=yjworks -c user.email=leeyunjai1982@gmail.com commit -m "post (hands-on): <English title>"
git push origin main
```

3. GitHub Actions 배포 결과를 확인하고 URL(`https://dibrain.dev/YYYY/MM/DD/handson-<slug>/`)을 알려 준다.
