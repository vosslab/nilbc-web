// Integration contract: each MkDocs configuration owns its published URL prefix.
// Menu selectors follow each imported theme; galleries follow B's build_card.html
// and D's worlds.js. The D revision collection/timeline contract follows the
// shared data-block and navigation sources: data_blocks.py, worlds.js, mkdocs_d_alpha.yml.
// Search uses Material's existing accessible field and result links.
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
const dRevisions = ['d-alpha', 'd-beta', 'd-gamma'];
const dDesigns = ['d', ...dRevisions];
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

async function assertImageForwardCollection(page, base, design) {
	const home = await page.locator('.nb-home-stage').count();
	assert.equal(home, 1, design + ': homepage stage is missing');
	const trainLink = page.locator('.nb-home-stage a[href]').filter({ hasText: /^Trains$/ }).first();
	assert.ok(await trainLink.count(), design + ': homepage has no direct Trains link');
	await trainLink.click();
	assert.equal(page.url(), base + design + '/creations/trains/');
	const collection = page.locator('.nb-gallery.nb-collection');
	assert.equal(await collection.getAttribute('data-world'), 'trains');
	const photos = collection.locator('.nb-photo');
	const countText = await page.locator('.nb-collection-count').textContent();
	assert.match(countText, /^\s*\d+ photos\s*$/);
	assert.equal(Number.parseInt(countText, 10), await photos.count(), design + ': advertised collection count differs from rendered photos');

	const first = photos.first().locator('.nb-photo__link');
	const thumb = first.locator('img');
	const thumbSrc = await thumb.getAttribute('src');
	const originalHref = await first.getAttribute('href');
	assert.ok(thumbSrc && originalHref && thumbSrc !== originalHref, design + ': thumbnail does not link to a separate optimized image');
	assert.match(thumbSrc, /_thumb\.webp$/);
	const context = await page.context().browser().newContext({
		viewport: page.viewportSize(),
		reducedMotion: 'reduce',
	});
	try {
		const journeyPage = await context.newPage();
		journeyPage.setDefaultTimeout(15000);
		const requests = [];
		journeyPage.on('request', (request) => requests.push(request.url()));
		await journeyPage.goto(base + design + '/');
		const journeyTrainLink = journeyPage.locator('.nb-home-stage a[href]').filter({ hasText: /^Trains$/ }).first();
		await journeyTrainLink.click();
		const journeyCollection = journeyPage.locator('.nb-gallery.nb-collection');
		const journeyPhotos = journeyCollection.locator('.nb-photo');
		const originalHrefs = await journeyPhotos.locator('.nb-photo__link').evaluateAll((links) => links.map((link) => link.href));
		assert.ok(originalHrefs.length > 0, design + ': train collection has no original-image links');
		assert.ok(originalHrefs.every((href) => !requests.includes(href)), design + ': collection requested an original before selection');
		const reloadedFirst = journeyPhotos.first().locator('.nb-photo__link');
		const selectedOriginal = await reloadedFirst.evaluate((link) => link.href);
		await reloadedFirst.click();
		const viewer = journeyPage.getByRole('dialog', { name: 'Photo viewer' });
		await viewer.waitFor({ state: 'visible' });
		const viewerImage = viewer.locator('img');
		await viewerImage.waitFor({ state: 'visible' });
		await journeyPage.waitForFunction(({ image, href }) => image.complete && image.naturalWidth > 0 && image.src === href,
			{ image: await viewerImage.elementHandle(), href: selectedOriginal });
		const selected = await viewerImage.evaluate((image) => image.src);
		assert.equal(selected, selectedOriginal, design + ': viewer did not load the selected original image');
		assert.ok(requests.includes(selectedOriginal), design + ': selected image was not requested after opening viewer');
		const firstSrc = selected;
		await viewer.getByRole('button', { name: 'Next', exact: true }).click();
		const nextHref = await journeyPhotos.nth(1).locator('.nb-photo__link').evaluate((link) => link.href);
		await journeyPage.waitForFunction(({ image, href }) => image.complete && image.naturalWidth > 0 && image.src === href,
			{ image: await viewerImage.elementHandle(), href: nextHref });
		assert.notEqual(nextHref, firstSrc);
		await viewer.getByRole('button', { name: 'Previous', exact: true }).click();
		await journeyPage.waitForFunction(({ image, href }) => image.complete && image.naturalWidth > 0 && image.src === href,
			{ image: await viewerImage.elementHandle(), href: selectedOriginal });
		assert.equal(await viewerImage.evaluate((image) => image.src), firstSrc);
		await journeyPage.keyboard.press('Escape');
		await viewer.waitFor({ state: 'hidden' });
		assert.ok(await reloadedFirst.evaluate((node) => node === document.activeElement), design + ': focus did not return to the selected photo');
	} finally {
		await context.close();
	}
	await page.goto(base + design + '/');
	assert.ok(await page.locator('.nb-home-photos').count(), design + ': homepage photo section is missing');
	const homepageImages = await page.locator('.nb-home-photos img').evaluateAll((images) => images.map((image) => ({src: image.getAttribute('src'), href: image.closest('a')?.getAttribute('href')})));
	assert.ok(homepageImages.length > 0);
	assert.ok(homepageImages.every((image) => image.src && image.href && image.src !== image.href && /_thumb\.webp$/.test(image.src)), design + ': homepage requests full-size photo sources instead of thumbnails');
}

async function assertImageForwardTimeline(page, base, design) {
	await page.goto(base + design + '/about/');
	const timelineLink = page.locator('.md-nav--primary').getByRole('link', { name: 'Our story', exact: true }).first();
	const mobile = page.viewportSize().width === 390;
	if (mobile) {
		const drawerToggle = page.locator('.md-header__button[for="__drawer"]');
		assert.equal(await drawerToggle.count(), 1, design + ': mobile drawer toggle is missing');
		await drawerToggle.click();
		await page.locator('.md-nav--primary').waitFor({ state: 'visible' });
	} else {
		assert.ok(await timelineLink.count(), design + ': primary navigation has no Our story link');
		assert.ok(await timelineLink.isVisible(), design + ': desktop Our story navigation link is not visible');
	}
	assert.ok(await timelineLink.isVisible(), design + ': Our story navigation link is not visible');
	await timelineLink.click();
	assert.equal(page.url(), base + design + '/about/timeline/');
	assert.ok(await page.getByRole('heading', { level: 1 }).count(), design + ': timeline route has no page heading');
	const brokenImages = await page.locator('.nb-timeline img').evaluateAll((images) => images.filter((image) => !image.getAttribute('src') || image.getAttribute('src').startsWith('http')).map((image) => image.getAttribute('src')));
	assert.deepEqual(brokenImages, [], design + ': timeline photo source is not local');
	const timelineSources = await page.locator('.nb-timeline img').evaluateAll((images) => images.map((image) => image.src));
	const responses = await Promise.all(timelineSources.map(async (url) => (await page.request.get(url)).status()));
	assert.ok(responses.length > 0, design + ': timeline has no local photos');
	assert.ok(responses.every((status) => status === 200), design + ': a timeline photo asset failed to load');
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
		await page.setViewportSize({ width: 390, height: 844 });
		await page.goto(base + design + '/');
		const drawerToggle = page.locator('.md-header__button[for="__drawer"]');
		if (design === 'd-alpha') {
			assert.equal(await drawerToggle.getAttribute('role'), 'button');
			assert.equal(await drawerToggle.getAttribute('tabindex'), '0');
			assert.equal(await drawerToggle.getAttribute('aria-label'), 'Toggle navigation');
			assert.equal(await drawerToggle.getAttribute('aria-controls'), '__drawer');
			assert.equal(await drawerToggle.evaluate((toggle) => toggle.getAttribute('aria-expanded') === String(document.getElementById('__drawer').checked)), true);
			await drawerToggle.focus();
			await page.keyboard.press('Enter');
			assert.equal(await page.locator('#__drawer').isChecked(), true);
			assert.equal(await drawerToggle.getAttribute('aria-expanded'), 'true');
			await page.keyboard.press('Space');
			assert.equal(await page.locator('#__drawer').isChecked(), false);
			assert.equal(await drawerToggle.getAttribute('aria-expanded'), 'false');
			await drawerToggle.focus();
			await page.keyboard.press('Escape');
			assert.equal(await drawerToggle.evaluate((node) => node === document.activeElement), true);
			assert.equal(await page.locator('#__drawer').isChecked(), false);
			await page.keyboard.press('Space');
			assert.equal(await page.locator('#__drawer').isChecked(), true);
			assert.equal(await drawerToggle.getAttribute('aria-expanded'), 'true');
			await page.setViewportSize({ width: 1440, height: 1000 });
			await page.goto(base + design + '/');
			assert.equal(await drawerToggle.getAttribute('aria-label'), 'Toggle navigation');
			assert.equal(await drawerToggle.getAttribute('tabindex'), '-1');
			assert.equal(await page.locator('#__drawer').isChecked(), false);
			await drawerToggle.focus();
			assert.equal(await drawerToggle.evaluate((node) => node.matches(':focus')), false);
			assert.equal(await drawerToggle.evaluate((node) => node.tabIndex), -1);
			report.journeys.push('d-alpha: mobile drawer named and operable with Enter/Space and Escape focus retention; desktop hidden toggle excluded from tab order');
		}
		await page.setViewportSize({ width: 390, height: 844 });
		await page.goto(base + design + '/');
		await drawerToggle.click();
		assert.equal(await page.locator('#__drawer').isChecked(), true);
		if (design.startsWith('d-')) assert.equal(await drawerToggle.getAttribute('aria-expanded'), 'true');
		await page.locator('.md-nav--primary a.md-nav__link').filter({ hasText: /^\s*Shows\s*$/ }).first().click();
		assert.equal(page.url(), base + design + '/shows/');
		assert.equal(await page.locator('#__drawer').isChecked(), false);
		if (design.startsWith('d-')) assert.equal(await drawerToggle.getAttribute('aria-expanded'), 'false');
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
			await page.goto(base + design + '/creations/creatures/');
			const frog = page.locator('[data-photo="frog"]');
			await frog.locator('.nb-photo__link').click();
			const frogViewer = page.getByRole('dialog', { name: 'Photo viewer' });
			await frogViewer.waitFor({ state: 'visible' });
			const frogImage = frogViewer.locator('img');
			await page.waitForFunction((image) => image.complete && image.naturalWidth > 0 && image.src.endsWith('/frog.webp'), await frogImage.elementHandle());
			assert.ok((await frogImage.evaluate((image) => image.src)).endsWith('/frog.webp'));
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
		console.log('Checking search ' + design);
		await page.goto(base + design + '/');
		if (design === 'c') await page.locator('.search-open').click();
		const search = page.getByRole('textbox', { name: 'Search', exact: true });
		await search.click();
		await page.waitForFunction(() => document.querySelector('.md-search-result__meta')?.textContent.trim() === 'Type to start searching');
		// Material observes keyup events; fill() only emits an input event.
		await search.pressSequentially('Bensenville');
		const result = page.locator('.md-search-result__link').first();
		await result.waitFor({ state: 'visible' });
		await result.click();
		assert.ok(page.url().startsWith(base + design + '/shows/'), 'Search escaped its design: ' + page.url());
		report.journeys.push(design + ': search loads and opens a result within its own prefix');
	}
	for (const design of dRevisions) {
		for (const width of [390, 1440]) {
			await page.setViewportSize({ width, height: width === 390 ? 844 : 1000 });
			await page.goto(base + design + '/');
			await assertImageForwardCollection(page, base, design);
			await assertImageForwardTimeline(page, base, design);
		}
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
