// Export contract: marketing/nilbc_club_flyer.svg owns the artwork and live text.
// Render that same SVG for print; the PDF must stay within one US Letter page.
import assert from 'node:assert/strict';
import path from 'node:path';
import { mkdir, readFile } from 'node:fs/promises';
import { chromium } from 'playwright';
import { REPO_ROOT } from './repo_root.mjs';

const output = path.join(REPO_ROOT, 'output', 'pdf');
const svg = await readFile(path.join(REPO_ROOT, 'marketing', 'nilbc_club_flyer.svg'), 'utf8');
await mkdir(output, { recursive: true });
const browser = await chromium.launch();
try {
	const page = await browser.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 2 });
	await page.setContent(`<html><head><style>
		@page { size: letter; margin: 0; }
		html, body { margin: 0; width: 8.5in; height: 11in; }
		svg { display: block; }
	</style></head><body>${svg}</body></html>`);
	await page.evaluate(async () => {
		await document.fonts.ready;
		const image = document.querySelector('svg image');
		const probe = new Image();
		probe.src = image.href.baseVal;
		await probe.decode();
	});
	assert.equal(await page.locator('svg').count(), 1);
	assert.ok(await page.evaluate(() => document.fonts.check('700 75px "Barlow Condensed"')));
	const overflow = await page.locator('svg text').evaluateAll((texts) => texts.filter((text) => {
		const box = text.getBBox();
		return box.x < 36 || box.y < 36 || box.x + box.width > 576 || box.y + box.height > 756;
	}).map((text) => text.textContent));
	assert.deepEqual(overflow, [], 'Flyer text must stay inside the half-inch margins');
	await page.pdf({ path: path.join(output, 'nilbc_club_flyer.pdf'), preferCSSPageSize: true, printBackground: true });
	await page.screenshot({ path: path.join(output, 'nilbc_club_flyer.png') });
	console.log('Exported output/pdf/nilbc_club_flyer.pdf and PNG preview.');
} finally {
	await browser.close();
}
