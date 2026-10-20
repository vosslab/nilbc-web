import http from 'node:http';
import path from 'node:path';
import { readFile } from 'node:fs/promises';
import { REPO_ROOT } from './repo_root.mjs';

const types = {
	'.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript',
	'.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp',
	'.svg': 'image/svg+xml', '.ttf': 'font/ttf', '.woff2': 'font/woff2',
	'.json': 'application/json', '.ico': 'image/x-icon', '.txt': 'text/plain',
};

export async function serveBuild(directory = path.join(REPO_ROOT, 'output_site')) {
	const root = path.resolve(directory);
	const server = http.createServer(async (request, response) => {
		let pathname;
		try {
			pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
		} catch {
			response.writeHead(400).end('Invalid path');
			return;
		}
		// Serve the same artifact at root and the GitHub Pages project prefix.
		if (pathname.startsWith('/nilbc-web/')) pathname = pathname.slice('/nilbc-web'.length);
		if (pathname.endsWith('/')) pathname += 'index.html';
		const file = path.resolve(root, `.${pathname}`);
		// ASVS 1.2.2: decoded request paths must remain within the static build.
		if (!file.startsWith(`${root}${path.sep}`)) {
			response.writeHead(403).end('Forbidden');
			return;
		}
		try {
			const content = await readFile(file);
			response.writeHead(200, { 'Content-Type': types[path.extname(file)] ?? 'application/octet-stream' });
			response.end(content);
		} catch (error) {
			response.writeHead(error.code === 'ENOENT' ? 404 : 500).end('Not available');
		}
	});
	await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
	return {
		url: `http://127.0.0.1:${server.address().port}`,
		close: () => new Promise((resolve, reject) => server.close((error) => error ? reject(error) : resolve())),
	};
}
