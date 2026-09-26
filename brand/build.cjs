/*
 * 브랜드 원본(src/*.svg)에서 각 사이트·앱이 쓰는 PNG·ICO 를 만든다.
 *
 *   NODE_PATH=<playwright 가 설치된 node_modules> node brand/build.cjs
 *
 * 결과는 brand/dist/<이름>/ 에 생긴다(git 에 올리지 않음). 각 저장소에는 여기서 필요한 파일만 복사한다.
 * 렌더링은 Chromium(Playwright)으로 하고, ICO 는 Python Pillow 로 묶는다.
 */
const { chromium } = require('playwright');
const { execFileSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

const SRC = path.join(__dirname, 'src');
const DIST = path.join(__dirname, 'dist');
const NAMES = ['dibrain', 'kids-lab', 'games', 'ai-shot'];

async function render(page, svgFile, size, out) {
  const svg = fs.readFileSync(path.join(SRC, svgFile), 'utf8').replace(/width="\d+" height="\d+"/, `width="${size}" height="${size}"`);
  await page.setViewportSize({ width: size, height: size });
  await page.setContent(`<!doctype html><html><body style="margin:0;background:transparent">${svg}</body></html>`);
  await page.screenshot({ path: out, omitBackground: true, clip: { x: 0, y: 0, width: size, height: size } });
}

(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({ deviceScaleFactor: 1 });
  for (const name of NAMES) {
    const out = path.join(DIST, name);
    fs.mkdirSync(out, { recursive: true });
    fs.copyFileSync(path.join(SRC, `${name}.svg`), path.join(out, 'icon.svg'));
    // 둥근 모서리 아이콘: 브라우저 탭·목록용. 홈 화면용은 모서리 없이 꽉 채운 maskable 과 apple-touch-icon.
    for (const s of [16, 32, 48, 192, 512]) await render(page, `${name}.svg`, s, path.join(out, `icon-${s}.png`));
    await render(page, `${name}-maskable.svg`, 512, path.join(out, 'maskable-512.png'));
    await render(page, `${name}-maskable.svg`, 192, path.join(out, 'maskable-192.png'));
    await render(page, `${name}-maskable.svg`, 180, path.join(out, 'apple-touch-icon.png'));
    execFileSync('python3', ['-c', `
from PIL import Image
imgs = [Image.open('${out}/icon-%d.png' % s).convert('RGBA') for s in (16, 32, 48)]
imgs[2].save('${out}/favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)], append_images=imgs[:2])
`]);
  }
  fs.copyFileSync(path.join(SRC, 'dibrain-mono.svg'), path.join(DIST, 'dibrain', 'mono.svg'));
  await page.setViewportSize({ width: 1200, height: 630 });
  await page.setContent(`<!doctype html><html><body style="margin:0">${fs.readFileSync(path.join(SRC, 'og-default.svg'), 'utf8')}</body></html>`);
  await page.screenshot({ path: path.join(DIST, 'dibrain', 'og-default.png'), clip: { x: 0, y: 0, width: 1200, height: 630 } });
  await browser.close();
  console.log('brand: built', NAMES.join(', '), '->', DIST);
})();
