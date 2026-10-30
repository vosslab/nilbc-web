/*
 * NILBC progressive enhancements.
 * 1. World filter chips on the gallery page (sections stay visible without JavaScript).
 * 2. Photo dialog: gallery links open a modal <dialog>; without JavaScript they open the image.
 * Runs once per page load (document$ fires on load and on any instant navigation).
 */

function nbSetupWorldFilter() {
	const worlds = Array.from(document.querySelectorAll(".nb-world"));
	if (worlds.length === 0 || document.querySelector(".nb-worlds-nav")) {
		return;
	}
	// the filter bar goes above the first world section
	const nav = document.createElement("div");
	nav.className = "nb-worlds-nav";
	nav.setAttribute("role", "group");
	nav.setAttribute("aria-label", "Filter photos by world");
	worlds[0].before(nav);

	// one chip per world section, plus "All worlds"; each section is named by its heading
	const options = [{ id: "all", label: "All worlds" }];
	worlds.forEach((section) => {
		const heading = section.querySelector("h2");
		section.id = `world-${heading.id}`;
		options.push({ id: section.id, label: heading.textContent.replace(/[¶#]/g, "").trim() });
	});

	const chips = options.map((option) => {
		const chip = document.createElement("button");
		chip.type = "button";
		chip.className = "nb-chip";
		chip.textContent = option.label;
		chip.dataset.world = option.id;
		chip.setAttribute("aria-pressed", option.id === "all" ? "true" : "false");
		chip.setAttribute("aria-controls", worlds.map((s) => s.id).join(" "));
		chip.addEventListener("click", () => showWorld(option.id));
		nav.appendChild(chip);
		return chip;
	});

	const status = document.createElement("p");
	status.className = "md-visually-hidden";
	status.setAttribute("role", "status");
	nav.after(status);

	function showWorld(id) {
		worlds.forEach((section) => {
			section.hidden = id !== "all" && section.id !== id;
		});
		chips.forEach((chip) => {
			chip.setAttribute("aria-pressed", chip.dataset.world === id ? "true" : "false");
		});
		const visible = document.querySelectorAll(".nb-world:not([hidden]) .nb-photo").length;
		status.textContent = `Showing ${visible} photos`;
	}
}

function nbSetupLightbox() {
	const links = document.querySelectorAll(".nb-photo__link");
	if (links.length === 0 || typeof HTMLDialogElement !== "function") return;
	let dialog = document.querySelector(".nb-lightbox");
	if (!dialog) {
		dialog = document.createElement("dialog");
		dialog.className = "nb-lightbox";
		dialog.setAttribute("aria-label", "Photo viewer");
		dialog.setAttribute("aria-describedby", "nb-viewer-caption");
		dialog.innerHTML =
			'<button type="button" class="nb-lightbox__close" aria-label="Close photo">&times;</button>' +
			'<div class="nb-lightbox__controls">' +
			'<button type="button" data-step="-1">Previous</button>' +
			'<span class="nb-lightbox__status" role="status"></span>' +
			'<button type="button" data-step="1">Next</button></div>' +
			'<p id="nb-viewer-caption"></p>' +
			'<a class="nb-lightbox__original">Open image directly</a>';
		document.body.appendChild(dialog);
	}
	const caption = dialog.querySelector("p");
	const status = dialog.querySelector("[role=status]");
	let opener = null;
	let group = [];
	let index = 0;
	function showPhoto(next) {
		index = (next + group.length) % group.length;
		const link = group[index];
		let image = dialog.querySelector("img");
		if (!image) {
			image = document.createElement("img");
			dialog.insertBefore(image, caption);
		}
		status.textContent = `Loading photo ${index + 1} of ${group.length}`;
		image.onload = () => { status.textContent = `Photo ${index + 1} of ${group.length}`; };
		image.onerror = () => { status.textContent = "Photo unavailable. Try the direct image link."; };
		image.alt = link.querySelector("img").alt;
		image.src = link.href;
		caption.textContent = link.dataset.caption;
		dialog.querySelector(".nb-lightbox__original").href = link.href;
		dialog.querySelectorAll("[data-step]").forEach((button) => {
			button.disabled = group.length < 2;
		});
	}
	dialog.querySelector(".nb-lightbox__close").onclick = () => dialog.close();
	dialog.querySelectorAll("[data-step]").forEach((button) => {
		button.onclick = () => showPhoto(index + Number(button.dataset.step));
	});
	dialog.onkeydown = (event) => {
		if (event.key === "Tab") {
			const controls = Array.from(dialog.querySelectorAll("button:not([disabled]), a[href]"));
			const first = controls[0];
			const last = controls[controls.length - 1];
			if (event.shiftKey && document.activeElement === first) {
				event.preventDefault();
				last.focus();
			} else if (!event.shiftKey && document.activeElement === last) {
				event.preventDefault();
				first.focus();
			}
		}
		if (event.key === "ArrowRight" || event.key === "ArrowLeft") {
			event.preventDefault();
			showPhoto(index + (event.key === "ArrowRight" ? 1 : -1));
		}
	};
	dialog.onclick = (event) => { if (event.target === dialog) dialog.close(); };
	dialog.onclose = () => { if (opener && opener.isConnected) opener.focus(); };
	links.forEach((link) => {
		link.onclick = (event) => {
			if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
			event.preventDefault();
			opener = link;
			const container = link.closest(".nb-show-gallery, .nb-gallery, .nb-mosaic");
			group = container ? Array.from(container.querySelectorAll(".nb-photo__link")) : [link];
			showPhoto(group.indexOf(link));
			dialog.showModal();
		};
	});
}

function nbSetupAlbums() {
	const albums = Array.from(document.querySelectorAll(".nb-show-album"));
	if (!albums.length) return;
	function revealHash(focus) {
		const album = albums.find((item) => `#${item.id}` === location.hash);
		if (!album) return;
		album.open = true;
		album.scrollIntoView({ block: "start" });
		if (focus) album.querySelector("summary").focus({ preventScroll: true });
	}
	document.querySelectorAll(".nb-album-nav a").forEach((link) => {
		link.addEventListener("click", () => {
			const album = albums.find((item) => `#${item.id}` === link.hash);
			album.open = true;
			album.querySelector("summary").focus({ preventScroll: true });
		});
	});
	window.addEventListener("hashchange", () => revealHash(true));
	revealHash(false);
}

function nbSetupTrain() {
	// the finale train holds still until it scrolls into view, so every visitor sees
	// Matchstick pull in; without JavaScript it simply runs from page load
	const train = document.querySelector(".nb-layout__train");
	if (!train || typeof IntersectionObserver !== "function") {
		return;
	}
	train.classList.add("nb-layout__train--waiting");
	const observer = new IntersectionObserver((entries) => {
		if (entries.some((entry) => entry.isIntersecting)) {
			train.classList.remove("nb-layout__train--waiting");
			observer.disconnect();
		}
	}, { threshold: 0.4 });
	observer.observe(train.parentElement);
}

function nbSetupMobileDrawer() {
	const toggle = document.querySelector('.md-header__button[for="__drawer"]');
	const drawer = document.getElementById("__drawer");
	if (!toggle || !drawer || toggle.dataset.nbKeyboardReady === "true") return;

	// Keep Material's native label/checkbox interaction; enhance it for keyboard users.
	toggle.dataset.nbKeyboardReady = "true";
	toggle.setAttribute("role", "button");
	toggle.setAttribute("tabindex", "0");
	toggle.setAttribute("aria-label", "Toggle navigation");
	toggle.setAttribute("aria-controls", "__drawer");
	const sync = () => {
		toggle.setAttribute("aria-expanded", String(drawer.checked));
		toggle.setAttribute("tabindex", window.matchMedia("(max-width: 76.1875em)").matches ? "0" : "-1");
	};
	const onViewportChange = () => sync();
	if (window.matchMedia) {
		const mobile = window.matchMedia("(max-width: 76.1875em)");
		if (mobile.addEventListener) mobile.addEventListener("change", onViewportChange);
		else if (mobile.addListener) mobile.addListener(onViewportChange);
		window.addEventListener("resize", onViewportChange);
	}
	drawer.addEventListener("change", sync);
	sync();
	toggle.addEventListener("keydown", (event) => {
		if (event.key !== " ") return;
		event.preventDefault();
		drawer.checked = !drawer.checked;
		drawer.dispatchEvent(new Event("change", { bubbles: true }));
	});
	toggle.addEventListener("click", (event) => {
		// The label's native pointer activation toggles the checkbox; only sync state here.
		queueMicrotask(sync);
	});
}

function nbInit() {
	nbSetupMobileDrawer();
	nbSetupWorldFilter();
	nbSetupLightbox();
	nbSetupAlbums();
	nbSetupTrain();
}

// Material exposes document$ for instant navigation; fall back to DOMContentLoaded
if (typeof document$ !== "undefined") {
	document$.subscribe(nbInit);
} else {
	document.addEventListener("DOMContentLoaded", nbInit);
}
