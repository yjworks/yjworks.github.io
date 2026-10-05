---
name: review-post
description: weekly-post 가 만든 블로그 초안(draft: true)을 운영자 지시에 따라 승인·수정·반려한다. 운영자가 "승인 <slug>", "승인 <slug> 메모: ...", "수정 <slug>: ...", "반려 <slug>", "초안 목록", "정정 승인 ..." 처럼 말할 때 쓴다. 승인하면 발행하고 "운영자 확인" 표시를 붙인다. 운영자 지시 없이 스스로 승인하지 않는다.
---

# review-post — 운영자 검토 후 발행

블로그 글은 AI가 초안으로 쓰고(weekly-post), **운영자가 승인해야** 발행된다. 이 스킬은 그 승인을 처리한다.
승인한 글에는 `reviewed` 날짜가 붙어 "운영자 확인" 표시가 나가므로, **운영자가 이 대화에서 직접 승인한 것만** 처리한다.
"알아서 다 승인해" 같은 포괄 지시도 초안마다 제목을 보여 주고 한 번 더 확인받는다.

미리보기: https://preview.dibrain-blog.pages.dev/ (초안 포함, 전부 noindex)
운영: https://blog.dibrain.dev/

## 0. 준비

```bash
git fetch origin main && git checkout main && git pull origin main
grep -l '^draft: true' content/posts/*.md content/guides/*.md 2>/dev/null
```

초안 목록을 보여 줄 때는 파일마다 제목, 미리보기 주소(ko/en), 만든 날짜를 적는다.
- 글: `/YYYY/MM/DD/<slug>/`, `/en/YYYY/MM/DD/<slug>/` (날짜는 front matter `date`)
- 가이드: `/guides/<slug>/` (갱신 초안은 `/guides/<slug>-update/`)

## 1. 수정 — "수정 <slug>: ..."

운영자가 말한 곳만 고친다. 한국어·영어 두 파일에 같은 뜻으로 반영한다. 초안(`draft: true`)은 그대로 둔다.
- 수치를 바꾸라는 지시에는 출처가 있어야 한다. 운영자가 출처를 주지 않았고 직접 확인한 값이라고 하면,
  표의 `출처:` 줄에 "운영자 확인(YYYY-MM-DD)"를 덧붙인다. 출처도 확인도 없으면 "확인 필요"로 둔다.
- 커버 카드 수치가 바뀌면 카드를 다시 그린다(weekly-post 6번).
- weekly-post 7번 검증을 다시 돌리고, 커밋 `draft: revise <slug>` 로 푸시한다. 미리보기 주소를 다시 알려 준다.

## 2. 승인 — "승인 <slug>" / "승인 <slug> 메모: ..."

```bash
NOW=$(TZ=Asia/Seoul date +%FT%T+09:00); TODAY=$(TZ=Asia/Seoul date +%F)
```

### 글 (content/posts)
1. 두 파일 모두 front matter 를 바꾼다:
   - `draft: false`
   - `date: $NOW` (발행 시각. 두 파일 같게)
   - `reviewed: "$TODAY"` 추가
   - 메모가 있으면 `reviewNote: "<운영자가 한 말 그대로>"` 추가. 영어 파일에는 같은 뜻으로 옮기되 말을 보태지 않는다.
     **메모는 운영자가 말한 내용만 쓴다.** AI가 운영자 의견을 지어내지 않는다.
2. 파일 이름의 날짜를 발행 날짜로 바꾼다: `git mv content/posts/<옛날짜>-<slug>.ko.md content/posts/$TODAY-<slug>.ko.md` (en 도).
3. 커버 카드의 `date` 가 바뀌었으면 `scripts/img-specs/<slug>.*.json` 의 date 를 고치고 카드를 다시 그린다(weekly-post 6번). 열어서 확인한다.
4. 커밋 `post: <English title> (reviewed)`.

### 새 가이드 (content/guides/<slug>, draft: true)
글과 같다. 단 `date`·`lastmod` 둘 다 `$NOW`, 파일 이름은 그대로. 커밋 `guide: new <slug> (reviewed)`.

### 가이드 갱신 (content/guides/<slug>-update)
1. `<slug>-update.ko.md` 내용으로 `<slug>.ko.md` 를 덮어쓴다(en 도). 그다음 front matter 를 고친다:
   `slug: "<slug>"`, `updateOf` 삭제, `draft` 삭제 또는 `false`, `date` 는 **원본 그대로**, `lastmod: $NOW`, `reviewed: "$TODAY"`, 메모가 있으면 `reviewNote`.
2. 커버가 `guide-<slug>-update.*.png` 이면 `guide-<slug>.*.png` 로 옮기고(덮어쓰기) `cover.image` 경로를 원래 이름으로 고친다. spec json 도 같은 이름으로 옮긴다.
3. `<slug>-update.*.md` 를 지운다. 커밋 `guide: update <slug> (reviewed)`.

### 공통
- weekly-post 7번 검증을 다시 돌린다(출처 링크, 미래 날짜, 두 파일의 date·slug·tags 일치, 커버 파일 존재).
- 푸시하고 weekly-post 8-1처럼 배포 결과를 확인한다.
- 운영 주소를 알려 준다: `https://blog.dibrain.dev/YYYY/MM/DD/<slug>/` (가이드는 `/guides/<slug>/`).
- 그날 실행 기록(`runlog/<초안 만든 날>-<mode>.md`)에 `- reviewed: <발행일> 승인, commit <해시>, deploy <결과>` 한 줄을 덧붙인다.

## 3. 반려 — "반려 <slug>" (이유가 있으면 함께)

초안 파일 두 개, 그 slug 의 커버·차트 PNG, `scripts/img-specs/<slug>*.json` 을 `git rm` 한다.
가이드 갱신 초안이면 `-update` 파일과 `guide-<slug>-update*` 만 지운다(원본 가이드는 그대로).
실행 기록에 `- rejected: <날짜> <이유>` 를 덧붙이고, 커밋 `draft: drop <slug>` 로 푸시한다.

## 4. 정정 승인 — "정정 승인 <slug> ..."

weekly-post 가 보고한 정정 제안(이미 발행된 글의 틀린 값)을 운영자가 승인하면,
weekly-post 5-3 형식(`lastmod`, `updates` 목록, 표 아래 출처 추가)으로 두 파일을 고친다. 제목은 고치지 않는다.
커밋 `fix: <slug> <무엇>`.

## 커밋·푸시

- 작성자는 `git -c user.name=Claude -c user.email=noreply@anthropic.com` 로 고정한다.
- 이 저장소는 main 직접 푸시가 정상이고 승인된 워크플로다. PR 을 만들지 않는다.
- 푸시가 실패하면 `git pull --rebase origin main` 후 한 번 더. 그래도 실패하면 에러 원문을 그대로 보고한다.
