// Integration contract: each MkDocs configuration owns its published URL prefix.
// Menu selectors follow each imported theme; galleries follow B's build_card.html
// and D's worlds.js. Search uses Material's existing accessible field and result links.
// A failure blocks the combined artifact: repair relocation paths before deployment.
import assert from 'node:assert/strict';
import path from 'node:path';
import { readdir, mkdir, writeFile } from 'node:fs/promises';
import { chromium } from 'playwright';
import { REPO_ROOT } from './repo_root.mjs';
import { serveBuild } from './helper_server.mjs';

const output = path.join(REPO_ROOT, 'output_checks');
const capture = process.argv.includes('--capture');
const report = { pages: [], journeys: [], errors: [] };
const designs = [
	['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D'],
	['d-alpha', 'D\u03b1'], ['d-beta', 'D\u03b2'], ['d-gamma', 'D\u03b3'],
];
const dDesigns = ['d', 'd-alpha', 'd-beta', 'd-gamma'];
const server = await serveBuild();
let browser;

async function htmlRoutes(directory, prefix = '') {
	const routes = [];
	for (const entry of await readdir(directory, { withFileTypes: true })) {
		const relative = prefix + entry.name;
		if (entry.isDirectory()) routes.push(...await htmlRoutes(path.join(directory, entry.name), relative + '/'));
		else if (entry.name.endsWith('.html')) routes.push(relative.replace(/index\.html$/, ''));
	}
	return routes;
}

async function settle(page) {
	await page.evaluate(async () => {
		await document.fonts.ready;
		const images = [...document.images].filter((image) => image.hasAttribute('src'));
		// A complete-page check must request off-screen lazy images before decoding them.
		for (const image of images) image.loading = 'eager';
		await Promise.all(images.map((image) => image.decode()));
	});
}

try {
	await mkdir(output, { recursive: true });
	if (capture) await mkdir(path.join(output, 'screenshots'), { recursive: true });
	browser = await chromium.launch();
	const context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
	const page = await context.newPage();
	page.setDefaultTimeout(15000);
	page.on('pageerror', (error) => report.errors.push(error.message));
	page.on('requestfailed', (request) => {
		if (request.failure()?.errorText !== 'net::ERR_ABORTED') report.errors.push(request.url() + ': ' + request.failure()?.errorText);
	});
	page.on('response', (response) => {
		if (response.status() >= 400) report.errors.push(response.status() + ': ' + response.url());
	});
	const base = server.url + '/nilbc-web/';
	const checked = new Set();
	const anchors = new Map();
	const links = new Set();
	for (const [design, label] of designs) {
		console.log('Checking design ' + label);
		await page.goto(base);
		await page.getByRole('link', { name: 'Explore Design ' + label, exact: true }).click();
		assert.equal(page.url(), base + design + '/');
		const routes = await htmlRoutes(path.join(REPO_ROOT, 'output_site', design));
		for (const width of [1440, 390]) {
			await page.setViewportSize({ width, height: width === 390 ? 844 : 1000 });
			for (const route of routes) {
				const url = base + design + '/' + route;
				const response = await page.goto(url);
				assert.equal(response.status(), 200, url);
				await settle(page);
				if (design.startsWith('d-') && route === '') {
					assert.equal(await page.locator('.nb-hero__matchstick').evaluate((el) => getComputedStyle(el).animationName), 'none', 'Reduced motion must show Matchstick without an entrance delay');
				}
				assert.ok(await page.getByRole('heading', { level: 1 }).count() > 0, 'Missing page heading: ' + url);
				assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), 'Overflow: ' + url + ' at ' + width);
				const references = await page.locator('a[href], link[href], script[src], img[src]').evaluateAll((nodes) => nodes.map((node) => node.href || node.src));
				anchors.set(url, await page.locator('[id]').evaluateAll((nodes) => nodes.map((node) => node.id)));
				for (const href of references) {
					if (!href.startsWith(server.url + '/')) continue;
					assert.ok(href.startsWith(base + design + '/'), 'Escaped design prefix: ' + href + ' from ' + url);
					links.add(href);
					const resource = href.split('#')[0];
					if (!checked.has(resource)) {
						assert.equal((await page.request.get(resource)).status(), 200, 'Broken reference: ' + href);
						checked.add(resource);
					}
				}
				if (capture && route === '') await page.screenshot({ path: path.join(output, 'screenshots', design + '_' + width + '.png'), fullPage: true, animations: 'disabled' });
				report.pages.push({ design, route, width });
			}
		}
	}
	for (const href of links) {
		const url = new URL(href);
		const fragment = decodeURIComponent(url.hash.slice(1));
		url.hash = '';
		if (fragment && anchors.has(url.href)) assert.ok(anchors.get(url.href).includes(fragment), 'Missing anchor: ' + href);
	}
	report.journeys.push('All design links, complete desktop/mobile route crawl, local assets and anchors');
	await page.setViewportSize({ width: 390, height: 844 });
	for (const [design, opener, navigation, destination] of [
		['a', '.club-menu summary', 'Mobile navigation', 'VISIT/'],
		['b', '.mobile-menu summary', 'Mobile navigation', 'shows/'],
		['c', '.menu-button', 'Primary', 'shows/'],
	]) {
		await page.goto(base + design + '/');
		await page.locator(opener).click();
		await page.getByRole('navigation', { name: navigation, exact: true }).locator('a').filter({ hasText: /show/i }).first().click();
		assert.equal(page.url(), base + design + '/' + destination);
		report.journeys.push(design + ': mobile menu reaches shows');
	}
	for (const design of dDesigns) {
		await page.goto(base + design + '/');
		await page.locator('.md-header__button[for="__drawer"]').click();
		await page.locator('.md-nav--primary a.md-nav__link').filter({ hasText: /^\s*Shows\s*$/ }).first().click();
		assert.equal(page.url(), base + design + '/shows/');
		report.journeys.push(design + ': Material mobile drawer reaches shows');
	}
	await page.goto(base + 'b/builds/');
	await page.getByRole('link', { name: /^Enlarge / }).first().click();
	const gallery = page.getByRole('dialog');
	await gallery.waitFor({ state: 'visible' });
	const firstImage = await gallery.locator('img').getAttribute('src');
	await gallery.getByRole('button', { name: /Next/ }).click();
	assert.notEqual(await gallery.locator('img').getAttribute('src'), firstImage);
	await page.keyboard.press('Escape');
	await gallery.waitFor({ state: 'hidden' });
	report.journeys.push('b: gallery opens, advances and closes');
	for (const design of dDesigns) {
		await page.goto(base + design + '/creations/');
		await page.locator('.nb-photo__link').first().click();
		await page.getByRole('dialog', { name: 'Photo viewer' }).waitFor({ state: 'visible' });
		await page.getByRole('button', { name: 'Close photo' }).click();
		await page.getByRole('dialog', { name: 'Photo viewer' }).waitFor({ state: 'hidden' });
		if (design === 'd-gamma') {
			const cutout = page.locator('[data-photo="frog"]');
			assert.ok(await cutout.locator('.nb-photo-cutout').isVisible());
			await cutout.locator('a').click();
			assert.ok((await page.locator('.nb-lightbox img').getAttribute('src')).endsWith('/frog.webp'));
			await page.getByRole('button', { name: 'Close photo' }).click();
		}
		report.journeys.push(design + ': photo viewer opens and closes');
	}
	for (const design of ['d-alpha', 'd-beta', 'd-gamma']) {
		await page.goto(base + design + '/shows/gallery/');
		const albumLink = page.locator('.nb-album-nav a').last();
		await albumLink.click();
		const album = page.locator(page.url().slice(page.url().indexOf('#')));
		assert.equal(await album.getAttribute('open'), '');
		const opener = album.locator('.nb-photo__link').first();
		await opener.focus();
		await page.keyboard.press('Enter');
		const viewer = page.getByRole('dialog', { name: 'Photo viewer' });
		await viewer.waitFor({ state: 'visible' });
		const first = await viewer.locator('img').getAttribute('src');
		await viewer.getByRole('button', { name: 'Next', exact: true }).click();
		assert.notEqual(await viewer.locator('img').getAttribute('src'), first);
		await page.keyboard.press('ArrowLeft');
		assert.equal(await viewer.locator('img').getAttribute('src'), first);
		await viewer.locator('.nb-lightbox__original').focus();
		await page.keyboard.press('Tab');
		assert.ok(await viewer.getByRole('button', { name: 'Close photo' }).evaluate((node) => node === document.activeElement));
		await page.keyboard.press('Shift+Tab');
		assert.ok(await viewer.locator('.nb-lightbox__original').evaluate((node) => node === document.activeElement));
		await page.keyboard.press('Escape');
		await viewer.waitFor({ state: 'hidden' });
		assert.ok(await opener.evaluate((node) => node === document.activeElement));
		await album.locator('summary').focus();
		await page.keyboard.press('Enter');
		assert.equal(await album.getAttribute('open'), null);
		report.journeys.push(design + ': show album navigation, keyboard viewer, next/previous and focus return');
	}
	await page.setViewportSize({ width: 1440, height: 1000 });
	for (const design of ['c', ...dDesigns]) {
		await page.goto(base + design + '/');
		if (design === 'c') await page.locator('.search-open').click();
		const search = page.getByRole('textbox', { name: 'Search', exact: true });
		await search.fill('Bensenville');
		const result = page.locator('.md-search-result__link').first();
		await result.waitFor({ state: 'visible' });
		await result.click();
		assert.ok(page.url().startsWith(base + design + '/shows/'), 'Search escaped its design: ' + page.url());
		report.journeys.push(design + ': search loads and opens a result within its own prefix');
	}
	for (const design of ['d-alpha', 'd-beta', 'd-gamma']) {
		await page.goto(base + design + '/');
		await page.getByTitle('Switch to dark mode', { exact: true }).click();
		await page.waitForFunction(() => document.body.dataset.mdColorScheme === 'slate');
		await page.reload();
		await page.waitForFunction(() => document.body.dataset.mdColorScheme === 'slate');
		if (capture) {
			for (const width of [1440, 390]) {
				await page.setViewportSize({ width, height: width === 390 ? 844 : 1000 });
				await settle(page);
				await page.screenshot({ path: path.join(output, 'screenshots', design + '_' + width + '_dark.png'), fullPage: true, animations: 'disabled' });
			}
		}
		await page.getByTitle('Switch to light mode', { exact: true }).click();
		await page.waitForFunction(() => document.body.dataset.mdColorScheme === 'default');
		report.journeys.push(design + ': theme choice persists across reload and switches back');
	}
	assert.deepEqual(report.errors, [], 'Browser resource or JavaScript errors');
	console.log('PASS: ' + report.pages.length + ' desktop/mobile page checks; ' + report.journeys.length + ' integration journeys.');
} catch (error) {
	report.failure = error.stack;
	throw error;
} finally {
	await writeFile(path.join(output, 'designs_report.json'), JSON.stringify(report, null, 2) + '\n');
	await browser?.close();
	await server.close();
}
