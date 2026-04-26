# IOR Prototype — Pull Request Checklist

> **STOP.** Before this PR can be reviewed, you must complete every item below.
> PRs without a completed checklist will be closed without review.

---

## File Details

| Field | Value |
|-------|-------|
| **File(s) changed** | <!-- e.g. 07a_HyDip_FMSv6.html --> |
| **Branch** | <!-- e.g. feature/hydip-fms-v6 --> |
| **Brief** | <!-- e.g. Builder_Brief_HyDip_FMS_v6.md --> |
| **Preview URL** | <!-- e.g. https://alexc-sketch.github.io/ior-prototype-v3-5/07a_HyDip_FMSv6.html --> |

---

## Pre-commit Audit Output

Paste the full output of `python3 audit.py YOUR_FILE.html` below:

```
[paste audit output here]
```

**Audit result:** `PASS` / `FAIL` *(delete one)*

> If FAIL: explain each issue and why it is a known false positive, or fix it before submitting.

---

## Golden Rules Checklist

### R1 — No Operating Hours
- [ ] No trading hours, opening times, or day/time ranges anywhere in the page body

### R2 — No Disallowed Border-Radius
- [ ] All containers and cards use `border-radius: 0`
- [ ] Only `.btn--pill` and `.cs-pill` / `.footer-state-pill` use `border-radius: 500px`
- [ ] No other `border-radius` values exist in the file

### R3 — No Disallowed Gradients
- [ ] No `linear-gradient`, `radial-gradient`, or `conic-gradient` in CSS
- [ ] Exception: hero scrim (`linear-gradient(to top, rgba(0,0,0,...) transparent)`) is permitted for photo heroes only

### R4 — No Inline `style=` Attributes
- [ ] Zero `style=` attributes on live UI elements in the HTML body
- [ ] Exception: `style="background-image: url(...)"` on card image divs is permitted

### R5 — No Blue Overlay on Hero
- [ ] Hero section has no `var(--ior-blue)` or `#0355A3` overlay or tint
- [ ] Hero is either: solid `var(--ior-navy)`, full-bleed photo + dark scrim, or video

### R6 — No Word "Depot"
- [ ] The word "depot" does not appear anywhere in the page content

### R7 — All Global Components Present
- [ ] Proto-bar above nav
- [ ] 5-item primary nav: Fuel Solutions / Digital Platforms / Industries We Serve / About IOR / Support & Contact
- [ ] Mobile drawer with accordion sub-menus
- [ ] Pre-footer "We're here to help" with 3 CTAs
- [ ] 6-column footer: Contact / Fuel Solutions / Digital Platforms / Corporate / Quick Actions / Find a Site By State

### R8 — Dual Nav CTAs
- [ ] "Customer Login" button with `btn--pill` class
- [ ] "Apply for an Account" button with `btn--pill` class

### R9 — No v3.5 Hrefs
- [ ] No `11_Support_Hub.html` (should be `11_Support_Hubv5.html`)
- [ ] No `11a_Contact_Us.html` (should be `11a_Contact_Usv5.html`)
- [ ] No `11b_Regional_Contacts.html` (should be `11b_Regional_Contactsv5.html`)
- [ ] No `11d_Find_Location.html` (should be `11d_Find_Locationv5.html`)
- [ ] No `11e_Make_Payment.html` (should be `11e_Make_Paymentv5.html`)

---

## Footer Checklist (recurring failures — verify every time)

- [ ] Footer uses `footer-nav-grid` structure with plain `<div>` + `<a>` — NOT `<ul>`/`<li>`
- [ ] Footer background is `var(--ior-blue)` — NOT a hardcoded hex like `#0a0a2e`
- [ ] State column uses abbreviations: `QLD / NSW / VIC / SA / WA / NT` — NOT full state names
- [ ] Legal bar reads `Site by 3PM` — NOT `Site by ThreePM`
- [ ] Copyright reads `© 2026` — NOT `© 2025`
- [ ] Pre-footer has exactly 3 CTAs: **Apply for an Account** / **Make an Enquiry** / **Need Help?**

---

## Content Checklist

- [ ] `lang="en"` on `<html>` tag (not `lang="en-AU"`)
- [ ] `<title>` updated with correct page title
- [ ] `<meta name="description">` updated (150–160 characters)
- [ ] All copy matches the brief exactly — no paraphrasing or placeholders
- [ ] No placeholder text like `[Page Title]` or `[Content here]` left in the file

---

## Master Index

- [ ] Card badge updated to `b-review` (In Review)
- [ ] Card `href` points to the correct new filename
- [ ] QC Tracker row updated to "QC in Process"

---

## Screenshot

Attach a full-width screenshot of the live GitHub Pages preview showing:
1. The nav renders correctly (5 items visible on desktop)
2. The hero section
3. At least one content section

<!-- Drag and drop screenshot here -->

---

*By submitting this PR, I confirm I have completed every item above and run the pre-commit audit script.*
