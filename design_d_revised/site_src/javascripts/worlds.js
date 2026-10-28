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
	if (links.length === 0 || typeof HTMLDialogElement !== "function") {
		return;
	}
	let dialog = document.querySelector(".nb-lightbox");
	if (!dialog) {
		dialog = document.createElement("dialog");
		dialog.className = "nb-lightbox";
		dialog.setAttribute("aria-label", "Photo viewer");
		// the <img> is added on first open so the page never holds an image without a source
		dialog.innerHTML =
			'<button type="button" class="nb-lightbox__close" aria-label="Close photo">&times;</button>' +
			"<p></p>";
		document.body.appendChild(dialog);
		dialog.querySelector(".nb-lightbox__close").addEventListener("click", () => dialog.close());
		// clicking the backdrop (the dialog box itself, not its children) closes it
		dialog.addEventListener("click", (event) => {
			if (event.target === dialog) {
				dialog.close();
			}
		});
	}
	const caption = dialog.querySelector("p");
	let opener = null;
	dialog.addEventListener("close", () => {
		if (opener) {
			opener.focus();
		}
	});

	links.forEach((link) => {
		if (link.dataset.ready === "1") {
			return;
		}
		link.dataset.ready = "1";
		link.addEventListener("click", (event) => {
			event.preventDefault();
			opener = link;
			const thumb = link.querySelector("img");
			let image = dialog.querySelector("img");
			if (!image) {
				image = document.createElement("img");
				dialog.insertBefore(image, caption);
			}
			image.src = link.href;
			image.alt = thumb.alt;
			caption.textContent = link.dataset.caption;
			dialog.showModal();
		});
	});
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

function nbInit() {
	nbSetupWorldFilter();
	nbSetupLightbox();
	nbSetupTrain();
}

// Material exposes document$ for instant navigation; fall back to DOMContentLoaded
if (typeof document$ !== "undefined") {
	document$.subscribe(nbInit);
} else {
	document.addEventListener("DOMContentLoaded", nbInit);
}
