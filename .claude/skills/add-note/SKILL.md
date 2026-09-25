---
name: add-note
description: 운영자(yjworks)가 이미 발행된 글에 "yjworks 한마디"를 달 때 쓴다. 사용자가 말한 문장을 그 글의 front matter note 에 넣고 발행한다. 문장을 새로 지어내지 않는다.
---

# add-note — yjworks 한마디

글 본문 위에 서명이 붙은 박스로 나간다. **사용자가 한 말만 넣는다.**

1. 어느 글인지 찾는다. 사용자가 제목 일부, 제품명, 날짜 중 하나만 말해도 된다.
   ```bash
   grep -l -i '<키워드>' content/posts/*.ko.md content/guides/*.ko.md
   ```
   여러 개면 후보를 보여 주고 고르게 한다.
2. 사용자의 문장을 거의 그대로 쓴다. 맞춤법과 띄어쓰기만 고친다. 한두 문장, 길어도 세 문장.
   내용을 보태거나 매끈하게 다듬지 않는다. 고친 것이 있으면 무엇을 고쳤는지 말한다.
3. front matter 의 `slug:` 줄 위에 넣는다. 따옴표 안에 `"` 가 있으면 `\"` 로 바꾼다.
   ```yaml
   note: "Orin Nano 2의 40W는 로봇 전원부 기준으로 보면 레일을 새로 설계해야 하는 수준입니다."
   ```
   - 영어판(.en.md)에는 사용자가 원할 때만, 사용자 문장을 옮겨서 넣는다.
   - 이미 `note` 가 있으면 바꿀지, 뒤에 이어 붙일지 묻는다.
4. 발행한다.
   ```bash
   git add <파일>
   git -c user.name=yjworks -c user.email=leeyunjai1982@gmail.com commit -m "note: <slug>"
   git push origin main
   ```
