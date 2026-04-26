# IOR Prototype — Pull Request

## Page Details

| Field | Value |
|---|---|
| **Page name** | <!-- e.g. Ground Fuels v5 --> |
| **File** | <!-- e.g. 03a_Diesel_Networkv5.html --> |
| **Brief** | <!-- e.g. Builder_Brief_Ground_Fuels_v5.md --> |
| **GitHub Pages preview** | <!-- https://alexc-sketch.github.io/ior-prototype-v3-5/YOUR_FILE.html --> |

---

## Audit Script Output

> **REQUIRED** — Run `python3.11 audit.py YOUR_FILE.html` and paste the full output below.
> PRs without audit output will be rejected without review.

```
PASTE AUDIT OUTPUT HERE
```

---

## Screenshot

> **REQUIRED** — Attach a full-width (1440px) screenshot of the live GitHub Pages preview showing:
> - The nav renders correctly with all 5 items
> - The hero section is visible
> - No broken images or layout errors

<!-- Drag and drop screenshot here -->

---

## Self-Audit Checklist

> Tick every item. If any item is unchecked, explain why in the notes section.

### Global Components (Non-Negotiable)
- [ ] Nav copied verbatim from `IOR_Page_Starter.html` — not modified
- [ ] Footer copied verbatim from `IOR_Page_Starter.html` — not modified
- [ ] Proto-bar present above nav with correct page name in `<span class="proto-bar__current">`
- [ ] Proto-bar links to `00_Master_Index.html`

### Golden Rules
- [ ] R1 — No operating hours in live content
- [ ] R2 — No disallowed `border-radius` (only `0` or `500px` permitted)
- [ ] R3 — No CSS gradients (hero photo scrim permitted if documented)
- [ ] R4 — No `style=` attributes on body elements (except `background-image` on card image divs)
- [ ] R5 — No hero overlay / blue overlay on hero section
- [ ] R6 — No word "depot" in live content
- [ ] R7 — Canonical 5-item nav: Fuel Solutions / Digital Platforms / Industries We Serve / About IOR / Support & Contact
- [ ] R8 — 6-column footer: Contact / Fuel Solutions / Digital Platforms / Corporate / Quick Actions / Find a Site By State
- [ ] R9 — Pre-footer "We're here to help" with 3 CTAs
- [ ] R10 — No `v3.5` hrefs anywhere in the file
- [ ] R11 — Support Hub links use `11_Support_Hubv5.html`

### Page Structure
- [ ] Quick Links bar is **below** the hero (not above)
- [ ] No forms outside modal containers
- [ ] No placeholder YouTube IDs (`VIDEO_ID_1`, `YOUR_VIDEO_ID`, etc.)
- [ ] No emoji in nav, footer, or body links
- [ ] All image assets referenced in the file exist in the repo (`assets/images/` or `assets/icons/`)
- [ ] All internal page links use correct v5/v6 filenames (not `href="#"` unless page not yet built)
- [ ] Master Index updated: card badge changed to `b-review`, QC Tracker row updated

### Copy
- [ ] All copy matches the brief exactly — no paraphrasing, no placeholder text
- [ ] All headings, subheadings, and body copy are verbatim from the brief

---

## Notes

<!-- Any known issues, permitted exceptions, or context for the auditor -->
