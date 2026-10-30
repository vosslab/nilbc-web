# Gamma visual correction

## Design direction

Gamma is a field guide for curious visitors and builders: evidence leads into orientation, then a clear next action. The homepage gives one real exhibit photograph an editorial position beside the club welcome, then puts visit/join actions and themed destinations immediately after it. Collections remain dense, date-ordered photo workbenches; shows separate planning, visiting, archive, and logbook tasks; membership is a compact invitation; standards are a reference; and the history reads as a timeline. Interface styling never labels itself as design metadata.

## Cascade and composition changes

The earlier styling layered overrides over the inherited photo frame and the base template's generic `page.meta.art` hero. Those rules did not remove the upstream frame treatment and banner, so inner pages repeated their title and delayed useful content. Gamma now omits the `photo-frames.css` import and suppresses the generic artwork banner in its own template branch. The remaining visual rules are gamma-specific. The shared homepage markup places `.nb-home-photos` before and outside `.nb-home-stage`; gamma therefore composes those actual sibling blocks without relying on a descendant selector or moving focus/content order. The homepage keeps only its lead photograph in the early editorial slot; the full photo gallery remains reachable from its link.

The Join page's actual `mailto:` application path is styled as a primary action; no new form, invented endpoint, or operational promise was added. A gamma-only template callout is placed immediately after the intro paragraph, using the same email target. The actual copy retains stated dues/eligibility. Gamma's active navigation state uses dark text and a strong underline. Gallery, event data, dates, counts, and native viewer interactions are retained. Reduced-motion and dark-scheme rules remain supported.

## Verification

- `source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_gamma.yml --site-dir output_checks/gamma_correction/d-gamma` — passed (MkDocs emitted its upstream Material/MkDocs 2.0 warning).
- `node output_checks/gamma_correction_probe.mjs` — passed 6 route/viewport responses (200), zero page errors, and no horizontal overflow at 390px or 1440px. Screenshots captured for homepage 390×844/1440×1000, Join 390×844, Shows 1440×1000, Trains 390×844, and timeline 1440×1000. Visual inspection confirmed both home CTAs above fold on mobile and the membership email action immediately after the intro.
- Screenshots: `output_checks/gamma_correction/home-390.png`, `home-1440.png`, `join-390.png`, `shows-1440.png`, `trains-390.png`, `timeline-1440.png`.
- Residual: this bounded run did not exercise gallery dialog controls, search, theme switching, or automated accessibility audits; alpha/beta and shared data were not changed.

## Scope and limits

Only gamma config/template/styles and this report are intended deliverables. The workspace has unrelated pre-existing edits from parallel work; they were not modified by this correction. Static content remains shared with alpha/beta and is not changed here.
