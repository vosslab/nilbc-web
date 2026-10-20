/* Progressive enhancement: ordinary image links work without JavaScript. */
const gallery = document.querySelector('.gallery-dialog');
if (gallery && typeof gallery.showModal === 'function') {
	const links = [...document.querySelectorAll('.gallery-link')];
	const image = gallery.querySelector('.dialog-image');
	const title = gallery.querySelector('#gallery-title');
	const caption = gallery.querySelector('.dialog-caption');
	const count = gallery.querySelector('.dialog-count');
	const previous = gallery.querySelector('.dialog-previous');
	const next = gallery.querySelector('.dialog-next');
	let opener;
	let currentIndex = 0;

	function showImage(index) {
		if (index < 0 || index >= links.length) return;
		currentIndex = index;
		const link = links[index];
		const original = link.querySelector('img');
		image.src = link.href;
		image.alt = original.alt;
		// ASVS 1.2.1: captions and labels use text rather than HTML insertion.
		title.textContent = link.dataset.title;
		caption.textContent = original.alt;
		count.textContent = `${index + 1} of ${links.length}`;
		previous.disabled = index === 0;
		next.disabled = index === links.length - 1;
		// A control becoming disabled must not strand keyboard focus.
		if (document.activeElement === previous && previous.disabled) next.focus();
		if (document.activeElement === next && next.disabled) previous.focus();
	}

	links.forEach((link, index) => {
		link.addEventListener('click', (event) => {
			if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
			event.preventDefault();
			opener = link;
			showImage(index);
			gallery.showModal();
		});
	});
	previous.addEventListener('click', () => showImage(currentIndex - 1));
	next.addEventListener('click', () => showImage(currentIndex + 1));
	gallery.addEventListener('keydown', (event) => {
		if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
			event.preventDefault();
			showImage(currentIndex + (event.key === 'ArrowRight' ? 1 : -1));
		}
	});
	gallery.querySelector('.dialog-close').addEventListener('click', () => gallery.close());
	gallery.addEventListener('click', (event) => {
		const bounds = gallery.getBoundingClientRect();
		if (event.target === gallery && (event.clientX < bounds.left || event.clientX > bounds.right
			|| event.clientY < bounds.top || event.clientY > bounds.bottom)) gallery.close();
	});
	gallery.addEventListener('close', () => opener?.focus());
}

const menu = document.querySelector('.mobile-menu');
if (menu) {
	const summary = menu.querySelector('summary');
	menu.addEventListener('keydown', (event) => {
		if (event.key === 'Escape' && menu.open) {
			menu.open = false;
			summary.focus();
		}
	});
	document.addEventListener('click', (event) => {
		if (menu.open && !menu.contains(event.target)) menu.open = false;
	});
	menu.addEventListener('focusout', (event) => {
		if (event.relatedTarget && !menu.contains(event.relatedTarget)) menu.open = false;
	});
}
