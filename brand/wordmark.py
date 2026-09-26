#!/usr/bin/env python3
"""글자 로고(워드마크)와 마크+글자 조합, 공유 미리보기 원본 SVG 를 만든다.

글자는 Pretendard(ExtraBold 800)의 윤곽선을 그대로 path 로 옮긴다. 그래서 글꼴이 없는 곳
(메일, 문서, 이미지 편집기)에서도 똑같이 보인다. Pretendard 는 SIL OFL 1.1 이라 윤곽선을 로고에 써도 된다.

  pip install fonttools brotli
  python3 brand/wordmark.py <PretendardVariable dynamic-subset 폴더와 pretendard.css 가 있는 폴더>

결과: brand/src/ 의 dibrain-wordmark.svg, dibrain-lockup.svg, dibrain-lockup-dark.svg, og-default.svg
"""
import pathlib, re, sys
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "src"
FONT_DIR = pathlib.Path(sys.argv[1])
WEIGHT = 800
MARK = re.search(r'<path fill="#fff" d="([^"]+)"', (SRC / "dibrain.svg").read_text()).group(1)
BLUE, INK = "#2f6fed", "#16181d"

# pretendard.css 의 unicode-range 로 글자마다 어느 subset 파일에 있는지 찾는다
css = (FONT_DIR / "pretendard.css").read_text()
ranges = []
for block in re.findall(r"@font-face\s*{(.*?)}", css, re.S):
    url = re.search(r"url\(['\"]?([^'\")]+\.woff2)", block).group(1)
    for a, b in re.findall(r"U\+([0-9A-Fa-f]+)(?:-([0-9A-Fa-f]+))?", re.search(r"unicode-range:([^;]+)", block).group(1)):
        ranges.append((int(a, 16), int(b or a, 16), FONT_DIR / url))
_fonts = {}


def font_for(ch):
    cp = ord(ch)
    for a, b, path in ranges:
        if a <= cp <= b:
            if path not in _fonts:
                f = TTFont(path)
                if "fvar" in f:
                    f = instancer.instantiateVariableFont(f, {"wght": WEIGHT})
                _fonts[path] = f
            return _fonts[path]
    raise SystemExit(f"글자 없음: {ch!r}")


def outline(text, size, tracking):
    """text 를 size(px) 로 그린 path d 와 전체 폭, 대문자 높이를 돌려준다. 원점 = 첫 글자 기준선 왼쪽."""
    x, parts, cap = 0.0, [], None
    for ch in text:
        f = font_for(ch)
        upm = f["head"].unitsPerEm
        s = size / upm
        if cap is None:
            cap = f["OS/2"].sCapHeight * s
        gname = f.getBestCmap()[ord(ch)]
        if ch != " ":
            pen = SVGPathPen(f.getGlyphSet())
            f.getGlyphSet()[gname].draw(TransformPen(pen, (s, 0, 0, -s, x, 0)))
            parts.append(pen.getCommands())
        x += f["hmtx"][gname][0] * s + tracking * size
    return " ".join(parts), x - tracking * size, cap


def r(v):
    return round(v, 2)


# 1) 글자 로고만
word_d, word_w, cap = outline("DigitalBrain", 100, -0.02)
pad = 4
(SRC / "dibrain-wordmark.svg").write_text(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {r(-cap - pad)} {r(word_w + 2 * pad)} {r(cap + 2 * pad + 22)}">\n'
    f'<path fill="{INK}" d="{word_d}"/>\n</svg>\n')


def lockup(text_fill, mark_bg, glyph):
    """마크(높이 96) + 글자. 글자 크기는 대문자 높이가 마크 높이의 약 45% 가 되게, 세로 가운데 맞춤."""
    size = 96 * 0.45 / (cap / 100)
    d, w, c = outline("DigitalBrain", size, -0.02)
    gap = 96 * 0.26
    base = 48 + c / 2
    total = 96 + gap + w
    body = (f'<rect width="96" height="96" rx="22" fill="{mark_bg}"/><path fill="{glyph}" d="{MARK}"/>'
            f'<g transform="translate({r(96 + gap)} {r(base)})"><path fill="{text_fill}" d="{d}"/></g>')
    return total, body


for name, (tf, mb, gl) in {"dibrain-lockup.svg": (INK, BLUE, "#fff"), "dibrain-lockup-dark.svg": ("#fff", BLUE, "#fff")}.items():
    total, body = lockup(tf, mb, gl)
    (SRC / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {r(total)} 96">\n{body}\n</svg>\n')

# 2) 공유 미리보기 1200x630: 파랑 바탕, 흰 마크(파랑 글리프) + 흰 글자, 아래 한 줄 소개
total, _ = lockup("#fff", "#fff", BLUE)
scale = 1.5
lw = total * scale
x0, y0 = (1200 - lw) / 2, 230
_, body = lockup("#fff", "#fff", BLUE)
tag_d, tag_w, _ = outline("앱 · 도구 · IT 블로그", 34, -0.01)
(SRC / "og-default.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">\n'
    f'<rect width="1200" height="630" fill="{BLUE}"/>\n'
    f'<g transform="translate({r(x0)} {r(y0)}) scale({scale})">{body}</g>\n'
    f'<g transform="translate({r((1200 - tag_w) / 2)} {r(y0 + 96 * scale + 78)})"><path fill="#fff" fill-opacity="0.85" d="{tag_d}"/></g>\n'
    '</svg>\n')
print("wordmark: cap", r(cap), "width", r(word_w), "-> brand/src")
