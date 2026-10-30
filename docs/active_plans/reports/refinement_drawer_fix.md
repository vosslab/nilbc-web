# Drawer key fix

## Change

The shared D revision drawer handler now intercepts Space only. It prevents the
browser default and toggles the checkbox once, then the existing `change`
listener updates `aria-expanded`. Enter remains with Material's native label
activation. That matters because the label has `role="button"`: Chromium emits
a trusted click for Enter, and manually toggling in `keydown` as well toggles
the checkbox twice. Pointer activation remains native. Escape focus behavior
and desktop `tabindex="-1"` handling are unchanged.

## Verification

Built alpha, beta, and gamma independently with strict MkDocs builds:

```bash
source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_alpha.yml
source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_beta.yml
source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_gamma.yml
```

A targeted Playwright Chromium probe loaded each built revision at 390 px and
sent real Enter and Space key presses. All three passed: Enter opened the
drawer; Space closed and reopened it with `aria-expanded` in sync; a pointer
click opened it; Escape retained focus with the drawer closed; and at 1280 px
the toggle had `tabindex="-1"`.

The full repository Playwright suite was not run; its owner maintains the
separate test file.
