# 자동 작성 현재 상태: 초안만 만들고, 운영자 승인 후 발행

예약 실행 **하나**가 매일 새벽 03:00(KST)에 돌지만, 스킬은 **월·수·금에만** 초안을 만든다.
초안(`draft: true`)은 https://preview.dibrain-blog.pages.dev/ 에서만 보이고, 운영자가 `review-post` 로 승인해야 blog.dibrain.dev 에 나간다.

| 요일 | 모드 | 다루는 것 |
|---|---|---|
| 월 | `hw` | 노트북·스마트폰·가전·웨어러블 중 하나 |
| 수 | `embedded` | SBC·개발 보드·로봇·엣지 AI 기기 |
| 금 | `guide`(짝수 주) / `dev`(홀수 주) | 비교 가이드 / GitHub·Hugging Face 인기 항목 |
| 화·목·토·일 | — | 즉시 종료 |

- 검토를 기다리는 초안이 2편 이상이면 새 초안을 만들지 않는다.
- 2026-10-05 변경: AdSense 심사에서 "가치가 별로 없는 콘텐츠"로 거절된 뒤, 검토 없는 자동 발행을 멈추고 운영자 승인제로 바꿨다.
- 그 전(2026-09-25)에는 평일 매일 자동 발행이었다.

Routine 프롬프트에는 `hw1`이 적혀 있지만 **스킬이 그 인자를 무시하고 요일로 결정한다.**
요일별로 Routine을 5개 만들 필요가 없다.

## 왜 이렇게 됐나

Routine을 MCP 도구(`create_trigger`)로 만들면 커넥터가 붙지 않아 **예약 세션이 GitHub에 푸시하지 못한다.**
2026-09-02 밤에 만든 5개가 전부 그랬다. 진단 3회(지정 브랜치·새 브랜치·main) 모두 실패했고,
`connectors` 인자로 붙이는 것도 조직 정책으로 막혀 있다.

> create_trigger: the connectors parameter is not available for this organization.

**claude.ai Routines UI에서 만든 것만 작동한다.** 지금 살아 있는 Routine이 그것이다.
UI로 만든 Routine은 에이전트가 수정할 수 없어서(`update_trigger` 거부), cron을 매일로 두고
스킬 쪽에서 요일 분기를 하도록 맞췄다.

## 손댈 때 주의

- **Routine을 늘리지 말 것.** 하나로 5일을 담당한다.
- Routine 프롬프트의 `hw1`은 바꾸지 않아도 된다. 스킬이 무시한다.
- 카테고리나 요일 배치를 바꾸려면 `.claude/skills/weekly-post/SKILL.md` 의 0번 표만 고치면 된다.
- 새 Routine이 필요하면 **반드시 claude.ai Routines UI에서** 만들 것. MCP로 만든 것은 푸시가 안 된다.

## 수동 발행

대화형 세션에서는 인자가 우선한다.

```
/weekly-post hw   embedded   dev   guide
```
