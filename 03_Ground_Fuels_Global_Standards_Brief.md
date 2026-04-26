# Builder Brief — 03_Ground_Fuels.html Global Standards Uplift

**Date:** 24 April 2026
**Repo:** `alexc-sketch/ior-prototype-v3-5`
**Branch convention:** `feat/03-ground-fuels-global-standards`
**Target file:** `03_Ground_Fuels.html`
**Reference files:**
- Baseline (page 1 verbatim, now live): https://alexc-sketch.github.io/ior-prototype-v3-5/03_Ground_Fuels.html
- Production spoke reference (03a): https://alexc-sketch.github.io/ior-prototype-v3-5/03a_Diesel_Network_v3.5.html
- Global Components reference: https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html
- Design System: https://alexc-sketch.github.io/ior-prototype-v3-5/IOR_Design_System.html

---

## Context

`03_Ground_Fuels.html` is now live as a verbatim extract of page 1 of 6 from the baseline wireframe spec. It renders correctly (the blank-page bug from a missing script block was fixed in PR #45). The page currently includes wireframe chrome (`.wf-nav`, `.ann` annotation bars, `IMAGE PLACEHOLDER` text) and uses the wireframe utility-bar, primary-nav, and footer rather than the production versions used on the spoke pages (03a–03e).

This brief covers the changes needed to bring the page up to global production standards while keeping all content and interactive blocks (FMT accordion, product selector, testimonial, FAQ, etc.) verbatim.

**Do not change any content, copy, or interactive component logic.** Only the chrome, layout wrappers, and lead-capture block are in scope.

---

## 1. Remove Wireframe Chrome

### 1.1 Wireframe nav bar (`.wf-nav`)
Remove the entire `<nav class="wf-nav">` block and its CSS rules (`.wf-nav`, `.wf-nav a`, `.wf-nav__module`, `.wf-nav__legend`, `.wf-swatch`, `.wf-swatch--std`, `.wf-swatch--dq`, `.wf-swatch--ok`).

### 1.2 Annotation bars (`.ann`)
Remove every `<div class="ann">` block from the HTML. These are the yellow/red/green annotation commentary bars. Remove the `.ann`, `.ann--dq`, `.ann--ok` CSS rules too.

### 1.3 Page badge
Remove the `<div class="page-badge">` block (the dark "MODULE 03 — PAGE 1 OF 6" header bar). Remove the `.page-badge`, `.page-badge .module-badge`, `.page-badge h2`, `.page-badge .meta` CSS rules.

### 1.4 `IMAGE PLACEHOLDER` text
Replace every `IMAGE PLACEHOLDER` text node inside image placeholder divs with an empty string. The placeholder divs themselves can stay (they provide layout space until real photography is supplied).

### 1.5 `LOGO PENDING` text
Remove any `LOGO PENDING` text nodes in the same way.

---

## 2. Replace Wireframe Header with Production Header

Copy the **utility-bar + primary-nav** block verbatim from `03a_Diesel_Network_v3.5.html` (lines 955–1008 in the current 03a file). This includes:
- `.utility-bar` with the "Australia's Remote Fuel Specialists — Since 1984" announce strip and the three utility links (Apply for an Account, Make a Payment, Contact Us)
- `.primary-nav` with the IOR logo mark, the desktop nav links (Fuel Solutions active), and the hamburger/mobile drawer

Also copy the **CSS** for these components from 03a (`.utility-bar`, `.utility-bar__inner`, `.utility-bar__brand`, `.utility-bar__actions`, `.utility-bar__link`, `.utility-bar__divider`, `.primary-nav`, `.nav-logo`, `.nav-logo__mark`, `.nav-links`, `.nav-link`, `.hamburger`, `.drawer`, etc.).

Remove the wireframe equivalents (`.utility-bar`, `.utility-announce`, `.primary-nav`, `.logo-placeholder`, `.nav-links`, `.nav-link`, `.nav-actions` as defined in the wireframe CSS).

---

## 3. Add Prototype Nav Bar

Insert the `.proto-bar` block immediately inside `<body>`, before the utility-bar. Copy it verbatim from `03a_Diesel_Network_v3.5.html` (lines 928–954). Also copy the `.proto-bar` CSS block from 03a.

The proto-bar provides "← Master Index", "Design System", and "Global Components" navigation links at the very top of the page, making it easy to navigate away during prototype review.

---

## 4. Replace Wireframe Footer with Production Footer

Copy the **pre-footer + site-footer** block verbatim from `03a_Diesel_Network_v3.5.html`. This includes:
- `.pre-footer` with the "We're here to help" heading and the three CTA buttons (Apply for an Account, Make an Enquiry, Need Help?)
- `.pre-footer__divider`
- `.site-footer` with the six-column footer nav grid (Contact, Fuel Solutions, Digital Platforms, Corporate, Quick Actions, Find a Site By State) and the legal/social strip

Also copy the CSS for these components from 03a. Remove the wireframe footer CSS and markup.

---

## 5. Restructure Lead Capture Block

The baseline has two separate blocks at the bottom of the page:
- A "Gated Asset Download" card (the `tease-capture` section with the PDF preview and bullet list on the left, and a form on the right)
- A HubSpot form embed placeholder

These should be consolidated into a single **split-layout lead-capture block** at `id="lead-capture"` per the global lead-capture pattern established on the spoke pages.

### 5.1 Structure

```html
<section class="hubspot-section" id="lead-capture" aria-labelledby="lead-capture-heading">
  <div class="hubspot-section__split">

    <!-- LEFT: asset + 3 callouts -->
    <div class="hubspot-section__asset">
      <div class="hubspot-section__eyebrow">Gated Asset</div>
      <h2 class="hubspot-section__title" id="lead-capture-heading">
        Get the Ground Fuels Capability Brochure + talk to our team.
      </h2>
      <p class="hubspot-section__sub">
        Everything you need to evaluate IOR's ground fuel solutions — network coverage, 
        on-site infrastructure, bulk delivery, HyBlue and lubricants — in one document.
      </p>
      <!-- MAX 3 callouts, single line each, no decorative bullets -->
      <ul class="hubspot-section__callouts">
        <li>Full product range overview</li>
        <li>Network coverage maps</li>
        <li>Account application guide</li>
      </ul>
      <!-- PDF preview card (keep the .tc-pdf-preview markup from baseline) -->
    </div>

    <!-- RIGHT: HubSpot form embed -->
    <div class="hubspot-section__form" data-hubspot-form="ground-fuels-hub" aria-label="Ground Fuels enquiry form">
      <!-- HubSpot embed script drops in here -->
    </div>

  </div>
</section>
```

### 5.2 CSS

Add the following to the page `<style>` block (or copy from 03a if the `.hubspot-section` rules already exist there):

```css
.hubspot-section {
  background: var(--grey-50);
  padding: var(--section-pad) 0;
  border-top: 4px solid var(--ior-blue);
}
.hubspot-section__split {
  max-width: var(--container);
  margin: 0 auto;
  padding: 0 24px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: start;
}
.hubspot-section__eyebrow {
  font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .1em; color: var(--ior-blue); margin-bottom: 12px;
}
.hubspot-section__title {
  font-size: clamp(22px, 2.5vw, 30px); font-weight: 800;
  color: var(--grey-900); margin-bottom: 16px; line-height: 1.2;
}
.hubspot-section__sub {
  font-size: 15px; color: var(--grey-700); line-height: 1.6; margin-bottom: 24px;
}
.hubspot-section__callouts {
  list-style: none; margin-bottom: 24px;
}
.hubspot-section__callouts li {
  font-size: 14px; color: var(--grey-700);
  padding: 7px 0; border-bottom: 1px solid var(--grey-100);
}
.hubspot-section__form {
  background: #fff;
  border: 1px solid var(--grey-100);
  border-top: 4px solid var(--ior-blue);
  padding: 36px;
  min-height: 320px;
}
@media (max-width: 768px) {
  .hubspot-section__split { grid-template-columns: 1fr; }
}
```

### 5.3 Downstream CTAs

Any "Download the Brochure →" or "Make an Enquiry →" CTA buttons higher up the page should point to `#lead-capture` (anchor link to the form section) rather than an external URL or a separate download page.

---

## 6. CSS Cleanup

### 6.1 No rounded corners
Confirm `--radius: 0px` is set in `:root` (it already is in the baseline). Ensure no individual element overrides this with a non-zero `border-radius`. The only permitted exceptions are `.btn--pill` (500px) and the nav logo mark (circular).

### 6.2 No gradients on hero or header
The baseline hero-banner uses `background: var(--ior-navy)` — flat colour, no gradient. This is correct. Confirm no `linear-gradient` or `radial-gradient` appears on `.hero-banner`, `.utility-bar`, or `.primary-nav`.

### 6.3 Remove unused wireframe CSS
After removing the wireframe chrome (step 1), clean up the now-orphaned CSS rules: `.wf-nav`, `.ann`, `.page-badge`, `.page-divider`, `.wf-swatch`.

---

## 7. Acceptance Criteria

Before raising a PR, the builder must confirm all of the following:

| # | Check | Expected |
|---|---|---|
| 1 | Wireframe nav bar visible | Not present |
| 2 | Annotation bars visible | Not present |
| 3 | Page badge (MODULE 03 — PAGE 1 OF 6) visible | Not present |
| 4 | IMAGE PLACEHOLDER text visible | Not present |
| 5 | Proto-bar present at top of page | Yes |
| 6 | Production utility-bar present | Yes |
| 7 | Production primary-nav present | Yes |
| 8 | Production pre-footer + site-footer present | Yes |
| 9 | FMT accordion interactive (first row open by default) | Yes |
| 10 | Product selector interactive (first panel active) | Yes |
| 11 | FAQ accordion interactive | Yes |
| 12 | Lead-capture block at `#lead-capture` | Yes |
| 13 | Lead-capture headline references gated asset | Yes |
| 14 | Max 3 callouts on lead-capture left panel | Yes |
| 15 | No `linear-gradient` on hero or header | Yes |
| 16 | No non-zero `border-radius` on image containers | Yes |
| 17 | All downstream "Download" CTAs point to `#lead-capture` | Yes |
| 18 | Page renders content (not blank) | Yes |
| 19 | PR targets `main` from named feature branch | Yes |
| 20 | No changes to `ior-global.css`, `ior-global.js`, `ior-motion.js`, `IOR_Design_System.html` | Yes |

---

## 8. Notes for Auditor

The `.tease-capture` CSS block (Scenario B gated layout) can be removed once the new `.hubspot-section__split` block is in place — they are functionally equivalent and the new pattern is the global standard. The `.tc-pdf-preview` markup inside the left column of the new block can be kept as a visual asset preview. The wireframe footer in the baseline uses `© 2025 IOR Petroleum` — the production footer uses `© 2026 IOR. All rights reserved.` — confirm the production footer copy is used after the swap.
