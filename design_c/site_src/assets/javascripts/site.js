(function () {
	var button = document.querySelector(".menu-button");
	var panel = document.querySelector(".nav-panel");
	if (!button || !panel) {
		return;
	}

	function setOpen(open) {
		button.setAttribute("aria-expanded", open ? "true" : "false");
		panel.classList.toggle("is-open", open);
	}

	button.addEventListener("click", function () {
		var open = button.getAttribute("aria-expanded") === "true";
		setOpen(!open);
	});

	document.addEventListener("keydown", function (event) {
		if (event.key === "Escape" && button.getAttribute("aria-expanded") === "true") {
			setOpen(false);
			button.focus();
		}
	});
})();
