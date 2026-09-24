#!/usr/bin/env python3
"""DigitalBrain 글 이미지 생성기. 외부 사진 없이 글의 검증된 수치로 카드를 그린다.

  python3 scripts/postimg.py cover   spec.json out.png   # 1200x630 커버 카드 (OG 이미지 겸용)
  python3 scripts/postimg.py compare spec.json out.png   # 두 제품 수치 비교 막대 차트

의존: pillow (`pip install pillow`), scripts/fonts/NotoSansKR-{400,700}.ttf (SIL OFL)
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONTS = Path(__file__).resolve().parent / "fonts"
BG, TILE, BORDER = (29, 30, 32), (40, 41, 45), (58, 59, 63)
FG, SEC, TER, ACCENT = (232, 232, 234), (160, 161, 165), (110, 111, 116), (47, 111, 237)

# 주제별 액센트. 36장이 전부 같은 파랑이면 목록에서 한 틀로 찍어낸 티가 난다.
# spec 의 "accent" 에 아래 키를 넣으면 그 색을 쓴다. 없으면 기본 파랑.
ACCENTS = {
    "laptop":    (47, 111, 237),
    "phone":     (109, 90, 230),
    "appliance": (14, 147, 132),
    "wearable":  (194, 65, 12),
    "sbc":       (3, 105, 161),
    "robot":     (185, 28, 28),
    "github":    (100, 116, 139),
    "ai":        (161, 98, 7),
    "brief":     (71, 85, 105),
}
W, H = 1200, 630
SITE = "dibrain.dev"

def font(weight, size):
    return ImageFont.truetype(str(FONTS / f"NotoSansKR-{weight}.ttf"), size)

def wrap(draw, text, f, max_w):
    """단어 단위로 줄바꿈하되, 한 단어가 너무 길면 글자 단위로 자른다."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial; continue
        if cur: lines.append(cur); cur = ""
        if draw.textlength(word, font=f) <= max_w:
            cur = word; continue
        for ch in word:                       # 긴 단어(한글 붙어쓰기)는 글자 단위
            if draw.textlength(cur + ch, font=f) <= max_w: cur += ch
            else: lines.append(cur); cur = ch
    if cur: lines.append(cur)
    return lines

def fit(draw, text, f, max_w):
    """넘치면 말줄임표로 자른다."""
    if draw.textlength(text, font=f) <= max_w: return text
    while text and draw.textlength(text + "…", font=f) > max_w: text = text[:-1]
    return text.rstrip() + "…"

def mark(draw, x, y, size=44):
    """헤더와 같은 D 마크."""
    draw.rounded_rectangle([x, y, x + size, y + size], radius=size * 0.22, fill=ACCENT)
    f = font(700, int(size * 0.68))
    tw = draw.textlength("D", font=f)
    draw.text((x + (size - tw) / 2, y + size * 0.08), "D", font=f, fill=(255, 255, 255))

def brand(draw, x, y):
    mark(draw, x, y)
    draw.text((x + 58, y + 2), "DigitalBrain", font=font(700, 34), fill=FG)

def cover(spec, out):
    """커버 카드. 제목은 넣지 않는다.

    제목은 목록과 글 상단에 이미 큰 글씨로 나온다. 카드에까지 넣으면 같은 문장이 두 번
    보이고, 36장이 전부 '제목 슬라이드' 한 틀로 읽힌다. 카드가 보여줄 것은 이 블로그가
    실제로 파는 것 - 출처로 확인된 수치다.
    """
    accent = ACCENTS.get(spec.get("accent", ""), ACCENT)
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    pad = 72
    brand(d, pad, 56)
    if spec.get("date"):
        f = font(400, 24); tw = d.textlength(spec["date"], font=f)
        d.text((W - pad - tw, 66), spec["date"], font=f, fill=SEC)

    # 킥커: 주제 색을 쓰는 유일한 텍스트
    if spec.get("kicker"):
        d.text((pad, 150), spec["kicker"], font=font(700, 30), fill=accent)

    # 수치: 이 카드의 주인공. 크게, 최대 4개.
    stats = spec.get("stats", [])[:4]
    if stats:
        n = len(stats); gap = 20
        tw_ = (W - pad * 2 - gap * (n - 1)) // n
        top, height = 252, 262
        for i, st in enumerate(stats):
            x = pad + i * (tw_ + gap)
            d.rounded_rectangle([x, top, x + tw_, top + height], radius=14, fill=TILE, outline=BORDER)
            d.rectangle([x, top + 18, x + 5, top + height - 18], fill=accent)  # 왼쪽 액센트 바(모서리 곡선 피해 안쪽으로)
            for vs in (58, 50, 44, 38, 32, 27):
                vf = font(700, vs)
                if d.textlength(st["value"], font=vf) <= tw_ - 52: break
            d.text((x + 26, top + 74), st["value"], font=vf, fill=FG)
            lf = font(400, 21)
            for ln_i, ln in enumerate(wrap(d, st.get("label", ""), lf, tw_ - 52)[:2]):
                d.text((x + 26, top + 168 + ln_i * 29), ln, font=lf, fill=SEC)

    f = font(400, 20); tw = d.textlength(SITE, font=f)
    d.text((W - pad - tw, H - 48), SITE, font=f, fill=TER)
    img.save(out, optimize=True)

def compare(spec, out):
    rows = spec["rows"]; n = len(rows)
    h = 200 + n * 92 + 90
    img = Image.new("RGB", (W, h), BG); d = ImageDraw.Draw(img)
    pad = 72
    brand(d, pad, 52)
    d.text((pad, 128), spec["title"], font=font(700, 40), fill=FG)
    # 범례 (오른쪽 위)
    lf = font(400, 22); lx = W - pad
    for name, col in ((spec["b"], TER), (spec["a"], ACCENT)):
        tw = d.textlength(name, font=lf); lx -= tw
        d.text((lx, 62), name, font=lf, fill=SEC); lx -= 30
        d.rounded_rectangle([lx, 68, lx + 18, 86], radius=4, fill=col); lx -= 26
    y = 200
    label_w, bar_x = 300, pad + 300
    bar_w = W - pad - bar_x - 130
    for r in rows:
        d.text((pad, y + 22), r["label"], font=font(400, 24), fill=SEC)
        mx = max(float(r["a"]), float(r["b"])) or 1.0
        unit = r.get("unit", "")
        for k, (val, col, dy) in enumerate(((r["a"], ACCENT, 0), (r["b"], TER, 34))):
            w_ = int(bar_w * float(val) / mx)
            d.rounded_rectangle([bar_x, y + dy, bar_x + max(w_, 6), y + dy + 24], radius=6, fill=col)
            txt = f"{val:g}{unit}" if isinstance(val, (int, float)) else f"{val}{unit}"
            d.text((bar_x + w_ + 14, y + dy - 2), txt, font=font(700 if k == 0 else 400, 22), fill=FG if k == 0 else SEC)
        y += 92
        d.line([pad, y - 14, W - pad, y - 14], fill=BORDER, width=1)
    if spec.get("note"):
        d.text((pad, h - 60), spec["note"], font=font(400, 20), fill=TER)
    f = font(400, 20); tw = d.textlength(SITE, font=f)
    d.text((W - pad - tw, h - 60), SITE, font=f, fill=TER)
    img.save(out, optimize=True)

if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("cover", "compare"):
        sys.exit(__doc__)
    spec = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    Path(sys.argv[3]).parent.mkdir(parents=True, exist_ok=True)
    (cover if sys.argv[1] == "cover" else compare)(spec, sys.argv[3])
    print("wrote", sys.argv[3])
