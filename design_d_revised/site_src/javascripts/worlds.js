/*
 * NILBC progressive enhancements.
 * 1. World filter chips on the gallery page (sections stay visible without JavaScript).
 * 2. Show albums reveal static thumbnail previews; visit links lead to upcoming shows.
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
	nbSetupAlbums();
	nbSetupTrain();
}

// Material exposes document$ for instant navigation; fall back to DOMContentLoaded
if (typeof document$ !== "undefined") {
	document$.subscribe(nbInit);
} else {
	document.addEventListener("DOMContentLoaded", nbInit);
}
