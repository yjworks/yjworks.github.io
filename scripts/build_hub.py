#!/usr/bin/env python3
"""dibrain.dev(GitHub Pages)에 올릴 사이트를 만든다.

블로그는 blog.dibrain.dev 로 옮겼다. dibrain.dev 는 앱·도구 첫 화면이 되고,
예전 블로그 주소(dibrain.dev/2026/09/…)로 들어온 사람은 같은 경로의 새 주소로 보낸다.

  python3 scripts/build_hub.py <블로그 빌드 폴더> <출력 폴더>

- hub/ 의 첫 화면을 그대로 복사한다.
- 블로그 빌드의 모든 index.html 경로마다 새 주소로 보내는 작은 페이지를 만든다
  (canonical + meta refresh 0초 + JS). GitHub Pages 는 301 을 못 하므로 이것이 최선이다.
- RSS 는 구독기가 meta refresh 를 따르지 않으므로 블로그 피드를 그대로 복사한다.
- 이미 공유된 링크의 미리보기가 깨지지 않게 글 이미지와 기본 파일도 복사한다.
- /games/, /kids-lab/ 같은 앱 경로는 각 저장소가 내보내므로 여기서 만들지 않는다.
"""
import html, pathlib, shutil, sys

NEW = "https://blog.dibrain.dev"
blog, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
hub = pathlib.Path(__file__).resolve().parent.parent / "hub"
if out.exists():
    shutil.rmtree(out)
shutil.copytree(hub, out)

# 도구 목록을 HTML 에 직접 넣는다. 페이지가 뜬 뒤 불러오는 방식만으로는 캐시·네트워크 문제로
# 빈 칸이 될 수 있고, 검색엔진도 도구 링크를 보지 못한다. 불러오지 못하면 비워 두고 JS 가 채운다.
import json, urllib.request
cards, note = "", "곧 추가됩니다. 모든 도구는 파일을 서버로 보내지 않고 브라우저 안에서만 처리합니다."
try:
    import os
    local = os.environ.get("HUB_TOOLS_REGISTRY")   # 로컬 시험용: tools 저장소의 dist/registry.json 경로
    if local:
        tools = json.loads(pathlib.Path(local).read_text(encoding="utf-8"))
    else:
        with urllib.request.urlopen("https://dibrain.dev/tools/registry.json", timeout=15) as r:
            tools = json.load(r)
    cards = "".join(
        f'<a class="card" href="/tools/{html.escape(t["slug"])}/">'
        f'<img src="{html.escape(t.get("icon") or "")}" alt="" loading="lazy">'
        f'<div><p class="t">{html.escape(t["name"])}</p><p class="d">{html.escape(t.get("desc", ""))}</p></div></a>'
        for t in tools)
    note = f"도구 {len(tools)}개. 모든 도구는 파일을 서버로 보내지 않고 브라우저 안에서만 처리합니다. <a href=\"/tools/\">전체 목록</a>"
    print(f"hub: {len(tools)} tools baked in")
except Exception as e:
    print(f"hub: tool registry not available ({e}); JS will fill it")
idx = out / "index.html"
idx.write_text(idx.read_text(encoding="utf-8").replace("<!--TOOLS-->", cards).replace("<!--TOOLS_NOTE-->", note), encoding="utf-8")

STUB = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<title>블로그 주소가 바뀌었습니다</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={url}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>location.replace({js} + location.search + location.hash);</script>
</head><body style="font-family:sans-serif;padding:24px">
<p>블로그가 <a href="{url}">{url}</a> 로 옮겼습니다. 자동으로 이동하지 않으면 링크를 눌러 주세요.</p>
</body></html>
"""

n = 0
for page in blog.rglob("index.html"):
    rel = page.parent.relative_to(blog).as_posix()
    if rel == ".":
        continue                                   # 루트는 첫 화면
    url = f"{NEW}/{rel}/"
    dst = out / rel / "index.html"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(STUB.format(url=html.escape(url), js=repr(url)), encoding="utf-8")
    n += 1

# 피드: 구독기가 계속 새 글을 받도록 블로그 피드를 그대로 둔다(링크는 이미 blog.dibrain.dev).
for feed in ["index.xml", "en/index.xml"]:
    if (blog / feed).exists():
        (out / feed).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(blog / feed, out / feed)

# 공유된 링크 미리보기용 이미지와 기본 파일
if (blog / "images").exists():
    shutil.copytree(blog / "images", out / "images", dirs_exist_ok=True)
for f in ["favicon.svg", "favicon.ico", "favicon-16x16.png", "favicon-32x32.png",
          "apple-touch-icon.png", "safari-pinned-tab.svg", "og-default.png", "ads.txt"]:
    if (blog / f).exists():
        shutil.copy2(blog / f, out / f)

(out / "robots.txt").write_text(
    "User-agent: *\nAllow: /\n\nUser-agent: Yeti\nAllow: /\n\n"
    "Sitemap: https://dibrain.dev/sitemap.xml\nSitemap: https://dibrain.dev/tools/sitemap.xml\n"
    "Sitemap: https://blog.dibrain.dev/sitemap.xml\n",
    encoding="utf-8")
(out / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    "  <url><loc>https://dibrain.dev/</loc></url>\n"
    "</urlset>\n", encoding="utf-8")

# 404: 예전 블로그 경로처럼 보이면 블로그로, 아니면 첫 화면 안내
(out / "404.html").write_text("""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><title>페이지를 찾을 수 없습니다</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>
  var p = location.pathname;
  if (/^\\/(20\\d\\d|en|tags|categories|posts|guides|archives|search|about|privacy)(\\/|$)/.test(p))
    location.replace('""" + NEW + """' + p + location.search + location.hash);
</script></head>
<body style="font-family:sans-serif;padding:24px">
<p>페이지를 찾을 수 없습니다. <a href="/">DigitalBrain 첫 화면</a> · <a href='""" + NEW + """/'>블로그</a></p>
</body></html>
""", encoding="utf-8")

print(f"hub: {n} redirect pages -> {out}")
