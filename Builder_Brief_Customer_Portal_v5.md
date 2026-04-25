# Builder Brief — Customer Portal v5
**Status:** In Brief — Full Rebuild  
**Replaces:** `07c_Customer_Portal_v3.5.html` (do not reference or copy)  
**Target file:** `07c_Customer_Portal_v5.html`  
**Branch:** `feature/customer-portal-v5`  
**Staging link:** https://alexc-sketch.github.io/ior-prototype-v3-5/07c_Customer_Portal_v5.html  
**Global Components reference:** https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html

---

## SEO & Meta

| Field | Value |
|---|---|
| **Focus keyword** | Fleet fuel management |
| **Secondary keywords** | B2B fuel account management, enterprise fuel portal |
| **Meta title** | IOR Customer Portal — Real-Time Fuel Visibility & Control \| IOR |
| **Meta description** | Every IOR account includes Customer Portal access. Real-time fuel dips, tag management, stock history, and fraud prevention. Login, apply, or request access today. |

---

## Critical Architecture Rules

> **READ BEFORE WRITING A SINGLE LINE OF HTML.**

1. **Nav and footer are VERBATIM from `IOR_Utility_Template_Shell_v5.html`.** Copy them character-for-character. Do not alter a single class, link, or element. Customer Portal branding does NOT touch the nav or footer.
2. **No CSS gradients anywhere.** All backgrounds are solid full-bleed colours.
3. **`border-radius: 0` on ALL elements** — the only permitted exception is `.btn--pill` (500px) in the nav.
4. **No inline `style=` attributes** on any body element.
5. **No word "depot"** — use "local office".
6. **No operating hours** anywhere on the page.
7. **Quick Links Bar sits IMMEDIATELY BELOW the hero** — never above it.
8. **The HubSpot form is a MODAL ONLY** — no inline form section. The "Request Access" buttons trigger the modal. There is no standalone form section on the page.
9. **The Features section is a 2×2 CSS Grid (Bento Box)** — no tabs, no carousel, no accordion. Delete any tab-based layout from v3.5.
10. **Do not modify** `ior-global.css`, `ior-global.js`, `ior-motion.js`, or `IOR_Design_System.html`.

---

## Customer Portal Brand Colour Tokens (page body only)

Define these as CSS custom properties inside the page `<style>` block. **Do not add them to `ior-global.css`.**

```css
:root {
  --cp-navy:   #0A2240;   /* Portal sidebar navy — hero background, dark sections */
  --cp-blue:   #0054A4;   /* IOR brand blue — accents, active states */
  --cp-white:  #FFFFFF;   /* Card backgrounds, hero text */
  --cp-grey:   #F5F5F5;   /* Light section backgrounds */
  --cp-dark:   #13114D;   /* Dark neutral — trust/testimonial section */
}
```

**Button rules (page body only):**
- Primary CTA: `background: var(--ior-blue); color: #fff;` — sharp corners (`border-radius: 0`)
- Secondary / outline CTA: `border: 2px solid var(--ior-blue); color: var(--ior-blue); background: transparent;` — sharp corners
- All page-body buttons use class prefix `btn--cp-*` to avoid polluting global styles

---

## Asset Manifest

All assets are committed to main. Use these exact paths.

| Asset | Path | Used In |
|---|---|---|
| Hero device mockup (tablet + phone) | `assets/images/customer-portal/cp-hero-device-mockup.png` | Hero right column |
| Tablet — Stock History screen | `assets/images/customer-portal/cp-tablet-stock-history.png` | Feature Quadrant (Cards 1 & 3) |
| Mobile — Tag Management screen | `assets/images/customer-portal/cp-mobile-tag-management.png` | Feature Quadrant (Cards 2 & 4) |

**Image usage notes:**
- Hero: `cp-hero-device-mockup.png` — the overlapping tablet + iPhone composite. Place in the right column of the 50/50 hero. `object-fit: contain`. Allow it to bleed slightly off the bottom edge of the hero section for depth.
- Feature Quadrant: Crop or position the tablet and mobile screenshots creatively inside the cards. The UI should bleed off the bottom or right edge of the card (Stripe/Apple Bento style). Use `overflow: hidden` on cards to clip the bleed.

---

## Page Structure — 8 Sections + 1 Modal

### SECTION 0 — Canonical Nav (verbatim from Shell v5)
Copy the full utility bar + primary nav + mobile drawer from `IOR_Utility_Template_Shell_v5.html`. No changes whatsoever.

---

### SECTION 1 — SaaS Hero

**Background:** `var(--cp-navy)` — solid, full-bleed. No gradient, no image overlay.  
**Layout:** 50/50 split (or asymmetrical 40/60). Left: copy. Right: device mockup image.  
**CSS class:** `cp-hero` on the `<section>`.

**Eyebrow:** `IOR CUSTOMER PORTAL` (small caps, `var(--cp-blue)` or white)

**H1:** Powerful fuel management, without the complexity.

**Subcopy:** The IOR Customer Portal gives you complete control over your fuel — from security and compliance to budgeting and forecasting. Advanced fleet management that is fast, simple, and included out-of-the-box for all IOR account holders.

**CTA 1 (Primary):** `Log in to Portal →` — `href="https://portal.ior.com.au"` — opens in new tab, `rel="noopener noreferrer"`  
**CTA 2 (Outline/White):** `Request Access` — `data-modal="cp-modal"` — triggers the HubSpot modal (no href)

**Right column image:** `cp-hero-device-mockup.png` — `alt="IOR Customer Portal on tablet and mobile"` — allow bottom bleed.

---

### SECTION 2 — Quick Links Bar

**Position:** Immediately below the hero. Before any other section.  
**CSS class:** `quick-links-bar` (uses global styles from `ior-global.css`)

**Label:** `Explore:`

| Link Text | href |
|---|---|
| HyDip™ | `07a_HyDip_FMSv6.html` |
| Customer Portal | `07c_Customer_Portal_v5.html` |

---

### SECTION 3 — 2×2 Feature Quadrant (Bento Box)

**Background:** `var(--cp-grey)` (`#F5F5F5`)  
**CSS class:** `cp-features`

**Section header (H2):** Everything you need out of the box.  
**Subtext:** Manage both your fuel and your fleet in one place with real-time, powerful tools.

**Layout:** CSS Grid, `grid-template-columns: 1fr 1fr`, `grid-template-rows: auto auto`. Gap: `1.5rem`. No border-radius on cards.

**Design reference:** Stripe.com feature grids — clean white cards, bold headline, short description, UI screenshot bleeding off the card edge. See `cp-tablet-stock-history.png` and `cp-mobile-tag-management.png`.

**Card specifications:**

| Card | Position | Headline | Body | Image |
|---|---|---|---|---|
| **Card 1** | Top-left | Total network visibility. | Track your bulk fuel deliveries as they happen. Integrate with your HyDip™ FMS to see real-time dips and usage directly from your bulk tank, giving you full visibility and control over what was delivered versus what was pumped. | `cp-tablet-stock-history.png` — bleed off bottom-right |
| **Card 2** | Top-right | Mitigate fraud instantly. | Multiple security layers mean only authorised users access your fuel. Add, suspend, or cancel RFID fuel tags in real time, adding instant protection against unauthorised use or theft. | `cp-mobile-tag-management.png` — bleed off bottom |
| **Card 3** | Bottom-left | Understand your consumption. | Generate granular reports on all transactions. Understand exactly how much fuel is being consumed between top-ups, broken down per vehicle, per driver, or per site. | `cp-tablet-stock-history.png` — cropped to chart area, bleed off right |
| **Card 4** | Bottom-right | Smarter budgeting. | Access live terminal gate pricing, download tax-compliant invoices instantly, and utilise your historical consumption data for accurate fuel cost forecasting. | `cp-mobile-tag-management.png` — cropped to pricing/invoice view, bleed off bottom |

**Card HTML structure:**
```html
<div class="cp-feature-card">
  <div class="cp-feature-card__copy">
    <h3 class="cp-feature-card__title">[Headline]</h3>
    <p class="cp-feature-card__body">[Body]</p>
  </div>
  <div class="cp-feature-card__media">
    <img src="[path]" alt="[alt]" loading="lazy">
  </div>
</div>
```

Card styles: `background: var(--cp-white)`, `border-radius: 0`, `overflow: hidden`, `padding: 2rem 2rem 0 2rem`. Media div: `overflow: hidden`, image allowed to bleed.

---

### SECTION 4 — Three-Path Access Block

**Background:** `var(--cp-white)`  
**CSS class:** `cp-access`  
**Layout:** 3-column card grid. Equal width. `border-radius: 0` on all cards.

**H2:** Get connected today.  
**Subtext:** Every IOR customer is provided with a portal account. Choose your path below.

| Path | Card Heading | Body | Button | Button Action |
|---|---|---|---|---|
| **Path 1 — Existing User** | Already have a login? | Access your dashboard to manage deliveries, tags, and invoices instantly. | `Log in Now →` | `href="https://portal.ior.com.au"` — new tab |
| **Path 2 — No Login** | IOR customer without a login? | Submit a request and our team will activate your portal credentials within 1 business day. | `Request Access` | `data-modal="cp-modal"` — triggers modal |
| **Path 3 — New to IOR** | Don't have an IOR account? | Apply for an IOR account today and get instant portal access upon approval. | `Apply Now →` | `href="https://iorapp.applyeasy.com.au/services/introduction"` — new tab |

---

### SECTION 5 — HubSpot Modal (Hidden by Default)

**id:** `cp-modal`  
**CSS class:** `cp-modal-overlay` (full-screen overlay, `position: fixed`, `z-index: 9999`, `background: rgba(0,0,0,0.6)`)  
**Default state:** `display: none` — shown by JS when any `[data-modal="cp-modal"]` element is clicked.

**Modal inner panel:**  
- `background: var(--cp-white)`
- `max-width: 560px`
- `border-radius: 0`
- Close button (×) top-right corner — clicking it or clicking the overlay closes the modal

**Modal copy:**

**H2:** Request Portal Access

**Body:** Submit your details below. Our Customer Service Team will link your profile and email your login credentials within 1 business day.

**Form embed:**
```html
<div class="cp-hubspot-form">
  <!-- HubSpot Form: Company Name, First Name, Last Name, Email -->
  <!-- Triggers automated email sequence on submission -->
  <script charset="utf-8" type="text/javascript" src="//js.hsforms.net/forms/embed/v2.js"></script>
  <script>
    hbspt.forms.create({
      region: "na1",
      portalId: "YOUR_PORTAL_ID",
      formId: "YOUR_FORM_ID"
    });
  </script>
</div>
```

> **Prototype placeholder:** Render a visible placeholder form with 4 labelled input fields (Company Name, First Name, Last Name, Email) and a "Submit Request" button styled with `background: var(--cp-blue)`. Add a comment `<!-- HubSpot form will replace this in production -->`.

**JS behaviour:**
```javascript
// Open modal
document.querySelectorAll('[data-modal="cp-modal"]').forEach(btn => {
  btn.addEventListener('click', () => {
    document.getElementById('cp-modal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
  });
});
// Close modal
document.getElementById('cp-modal').addEventListener('click', (e) => {
  if (e.target === e.currentTarget || e.target.classList.contains('cp-modal__close')) {
    document.getElementById('cp-modal').style.display = 'none';
    document.body.style.overflow = '';
  }
});
```

---

### SECTION 6 — Social Proof / Testimonial

**Background:** `var(--cp-dark)` (`#13114D`)  
**CSS class:** `cp-testimonial`  
**Layout:** Full-width centred blockquote. Max-width `800px`.

**Quote:** "The real-time visibility we get through the IOR Portal has completely changed how we manage our fleet. We can track consumption down to the litre and suspend lost tags instantly, saving us thousands in potential theft."

**Attribution:** *(Awaiting final client testimonial — render as placeholder: "IOR Customer, Fleet Operations")*

---

### SECTION 7 — FAQ Accordion

**Background:** `var(--cp-white)`  
**CSS class:** `cp-faq`  
**Layout:** Standard accordion. One open at a time. Vanilla JS only. `border-radius: 0` on all elements.

**Section header (H2):** Frequently asked questions

| Q | A |
|---|---|
| **Q1: Can I access fuel transaction reporting in the portal?** | Yes. You can generate and export granular reports on all fuel transactions, breaking down consumption by vehicle, driver, or site. |
| **Q2: Is the portal designed for account-based customers?** | Yes, the IOR Customer Portal is an out-of-the-box solution included for all account-based customers, giving you full control over your fuel and fleet. |
| **Q3: Can I manage invoices or account details in the portal?** | Absolutely. You can download current and historical tax-compliant invoices, view live pricing, and update your account details directly within the dashboard. |
| **Q4: How does the customer portal connect with IOR's digital platforms?** | The Customer Portal acts as your central hub. It seamlessly integrates with platforms like HyDip™ FMS, allowing you to view real-time tank dips and usage data alongside your standard network transactions. |
| **Q5: Where do I go if I need help with the customer portal?** | If you need assistance, you can visit our Help Centre for detailed guides or contact our Customer Service team on 1300 457 467. |

---

### SECTION 8 — Trust Flow (Related Content Grid)

**Background:** `var(--cp-grey)`  
**CSS class:** `cp-related`  
**Layout:** Standard 3-card global component — case studies and related pages.

**Section header (H2):** See how IOR customers use the portal.

**Cards:**

| Card | Title | Link |
|---|---|---|
| 1 | Tin Can Bay Marina — Case Study | `#` (placeholder — case study page TBD) |
| 2 | HyDip™ Fuel Management System | `07a_HyDip_FMSv6.html` |
| 3 | Fuelcharge App | `07b_Fuelcharge_App_v8.html` |

Card style: white card, `border-radius: 0`, eyebrow label (CASE STUDY / PLATFORM), title, short description, arrow link.

---

### SECTION 9 — Canonical Pre-footer + Footer (verbatim from Shell v5)

Copy the `<section class="pre-footer">` and `<footer>` blocks verbatim from `IOR_Utility_Template_Shell_v5.html`. No changes.

---

## Handoff Notes for Builder

### What v3.5 got wrong (do not repeat)
1. **Tabbed features layout** — must be replaced with the 2×2 Bento Box CSS Grid.
2. **Inline HubSpot form section** — must be removed. Form lives in a modal only.
3. **Hero gradient** — must be solid `var(--cp-navy)`.
4. **Quick Links above hero** — must be below hero.

### Design references
- **Stripe.com** — feature grid cards with UI screenshots bleeding off the edge
- **Apple.com/ipad-pro** — asymmetric bento grid, bold short copy
- **Linear.app** — high-contrast B2B SaaS feature cards

### Golden Rules self-audit checklist (run before opening PR)
- [ ] `border-radius: 0` on ALL containers, cards, and buttons except `.btn--pill` (nav only)
- [ ] Zero CSS gradients — all backgrounds are solid `var(--cp-*)` colours
- [ ] Zero inline `style=` attributes on body elements
- [ ] Hero background is `var(--cp-navy)` solid — no overlay, no image background
- [ ] Quick Links Bar is BELOW the hero, not above
- [ ] Nav and footer are verbatim from `IOR_Utility_Template_Shell_v5.html` — no changes
- [ ] CP branding does NOT appear inside `<nav>` or `<footer>`
- [ ] No word "depot" anywhere
- [ ] No operating hours anywhere
- [ ] Feature section is a 2×2 CSS Grid — no tabs
- [ ] HubSpot form is MODAL ONLY — no inline form section on the page
- [ ] All 3 "Request Access" triggers use `data-modal="cp-modal"` — not `href`
- [ ] Modal closes on overlay click AND on × button click
- [ ] `body.overflow: hidden` set when modal opens, restored on close
- [ ] All Support Hub links use `11_Support_Hubv5.html`
- [ ] HyDip link in Quick Links uses `07a_HyDip_FMSv6.html`
- [ ] Apply Now links to `https://iorapp.applyeasy.com.au/services/introduction`
- [ ] Portal login links to `https://portal.ior.com.au`

### PR instructions
- Branch: `feature/customer-portal-v5`
- File: `07c_Customer_Portal_v5.html` only — do NOT modify `00_Master_Index.html` in the PR
- PR title: `feat: Customer Portal v5 — bespoke rebuild (2x2 bento, modal form, device hero)`
- PR description: include the self-audit checklist results
