from pathlib import Path
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
s=(R/'exports/20261029-玩家招式图-07/check-browser.cjs').read_text(encoding='utf-8')
s=s.replace("!result.title.endsWith('（正背面待核／上中下段待核）')", "result.title.includes('正背面待核')")
s=s.replace("!v.title.includes('（正背面待核／上中下段待核）')", "v.title.includes('正背面待核')||!v.title.includes('可避')&& !v.title.includes('无命中段')")
s=s.replace("await page.evaluate(()=>select(44));await page.screenshot", """await page.evaluate(()=>select(44));
const headings=await page.locator('#drawer-body .variant h4').allTextContents();
if(!headings[0].includes('正面')||!headings[1].includes('背面')||!headings[0].includes('下潜／左侧闪／右侧闪'))throw Error('sample quadrant or mask');
if(!await page.locator('#drawer-body').innerText().then(t=>t.includes('0.2秒')&&t.includes('互列为同键输入栈兄弟')))throw Error('input caveat');
await page.evaluate(()=>select(16));if(!await page.locator('#drawer-body').innerText().then(t=>t.includes('短按轻击松开·变体')||t.includes('短按重击松开·变体')))throw Error('Alt display');
await page.evaluate(()=>select(44));await page.screenshot""",1)
s=s.replace("'name annotations retain unknown status'", "'verified front/back names and per-window avoid config; height limits retained','Alt same-gesture caveat'")
(O/'check-browser.cjs').write_text(s,encoding='utf-8')
