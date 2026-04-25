# Builder Brief — HyDip™ FMS v6
**Status:** In Brief — Full Bespoke Rebuild  
**Replaces:** `07a_HyDip_FMSv5.html` (BINNED — do not reference or copy)  
**Target file:** `07a_HyDip_FMSv6.html`  
**Branch:** `feature/hydip-fms-v6`  
**Staging link:** https://alexc-sketch.github.io/ior-prototype-v3-5/07a_HyDip_FMSv6.html  
**Global Components reference:** https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html

---

## SEO & Meta

| Field | Value |
|---|---|
| **Focus keyword** | HyDip fuel management system |
| **Secondary keywords** | fuel management system Australia, tank monitoring, fleet fuel tracking, FTC reporting |
| **Meta title** | HyDip™ Fuel Management System — Real-Time Tank Monitoring \| IOR |
| **Meta description** | HyDip™ is IOR's proprietary cloud-based fuel management system. Near real-time tank monitoring, automated reorder triggers, and compliance reporting. |

---

## Critical Architecture Rules

> **READ BEFORE WRITING A SINGLE LINE OF HTML.**

1. **Nav and footer are VERBATIM from `IOR_Utility_Template_Shell_v5.html`.** Copy them character-for-character. Do not alter a single class, link, or element. HyDip branding does NOT touch the nav or footer.
2. **HyDip bespoke branding applies to page body sections ONLY** — between the closing `</nav>` and the opening `<section class="pre-footer">`.
3. **No CSS gradients anywhere.** All backgrounds are solid full-bleed colours.
4. **`border-radius: 0` on ALL elements** — the only permitted exception is `.btn--pill` (500px) in the nav.
5. **No inline `style=` attributes** on any body element.
6. **No word "depot"** — use "local office".
7. **No operating hours** anywhere on the page.
8. **Quick Links Bar sits IMMEDIATELY BELOW the hero** — never above it.
9. **Do not modify** `ior-global.css`, `ior-global.js`, `ior-motion.js`, or `IOR_Design_System.html`.

---

## HyDip Brand Colour Tokens (page body only)

Define these as CSS custom properties inside the page `<style>` block. **Do not add them to `ior-global.css`.**

```css
:root {
  --hd-blue:    #0054A4;   /* Primary brand blue — hero background, section accents */
  --hd-yellow:  #FFB81C;   /* Primary action accent — CTA buttons only */
  --hd-dark:    #13114D;   /* Dark neutral — lead trap background, dark sections */
  --hd-white:   #FFFFFF;   /* Base neutral — card backgrounds, hero text */
  --hd-grey:    #F5F5F5;   /* Light grey — hardware cards section background */
}
```

**Button rules (page body only):**
- Primary CTA: `background: var(--hd-yellow); color: var(--hd-dark);` — sharp corners (`border-radius: 0`)
- Secondary CTA: `border: 2px solid var(--hd-white); color: var(--hd-white); background: transparent;` — sharp corners
- All page-body buttons use class prefix `btn--hd-*` to avoid polluting global styles

---

## Asset Manifest

All assets are committed to main. Use these exact paths.

| Asset | Path | Used In |
|---|---|---|
| HyDip logo (white) | `assets/icons/hydip-logo-white.svg` | Hero |
| HyDip logo (navy) | `assets/icons/hydip-logo-navy.svg` | Light sections if needed |
| Dashboard + map screenshot | `assets/images/hydip/hydip-dashboard-map-alerts.png` | Tab: GAUGE |
| HDV2 device | `assets/images/hydip/hydip-hdv2-device.png` | Hardware card 1, Tab: GAUGE |
| HFTV1 device | `assets/images/hydip/hydip-hftv1-device.png` | Hardware card 2, Tab: TRACK |
| Mobile app screenshot | `assets/images/hydip/hydip-tank-gauge-mobile.png` | Tab: TRACK or PAY |
| Refuel illustration | `assets/images/hydip/hydip-refuel-illustration.png` | Tab: DISPENSE |
| HDV2 spec PDF | `assets/pdfs/HyDip-HDV2-Specs.pdf` | Hardware card 1 download |
| HFTV1 spec PDF | `assets/pdfs/HyDip-HFTV1-Specs.pdf` | Hardware card 2 download |
| HyDip brochure PDF | `assets/pdfs/HyDip-Product-Brochure.pdf` | Lead trap download CTA |

> **Note on HDX2:** No image asset exists for HDX2. Use a placeholder `<div class="hd-device-placeholder">` with the text "HDX2 — Image coming soon" styled to match the other cards. The card still needs the spec list and the "Enquire about HDX2" CTA anchoring to the form.

---

## Page Structure — 9 Sections

### SECTION 0 — Canonical Nav (verbatim from Shell v5)
Copy the full utility bar + primary nav + mobile drawer from `IOR_Utility_Template_Shell_v5.html`. No changes whatsoever.

---

### SECTION 1 — Bespoke SaaS Hero

**Background:** `var(--hd-blue)` — solid, full-bleed. No gradient, no image overlay, no background-image.  
**Layout:** Centre-aligned copy. Single column. No 50/50 split.  
**Logo:** `hydip-logo-white.svg` above the H1, `width="160"`, `loading="eager"`.

**Eyebrow:** `FUEL MANAGEMENT SYSTEM` (small caps, `var(--hd-yellow)`)

**H1:** Fleet fuel management. Finally solved.

**Subcopy:** HyDip™ is IOR's purpose-built Fuel Management System. Real-time per-asset tracking, automated Fuel Tax Credit reporting, accounting integration, and a live fleet dashboard — all in one platform built for Australian operators.

**CTA 1 (Primary/Yellow):** `Enquire Now ↓` — anchors to `#hd-form` (the HubSpot form section)  
**CTA 2 (Outline/White):** `Customer Login` — links to `https://cloud.hydip.com` (opens in new tab, `rel="noopener noreferrer"`)

**CSS class:** `hd-hero` on the `<section>`. Centre-align all children with `text-align: center`. Max-width container `960px` centred.

---

### SECTION 2 — Quick Links Bar

**Position:** Immediately below the hero. Before any other section.  
**CSS class:** `quick-links-bar` (uses global styles from `ior-global.css`)

**Label:** `Explore:`

| Link Text | href |
|---|---|
| Customer Portal | `07c_Customer_Portal_v4.html` |
| Fuelcharge App | `07b_Fuelcharge_App_v8.html` |
| System Status ↗ | `https://status.hydip.com` (new tab) |

---

### SECTION 3 — The "Why" (Problem Statement)

**Background:** `var(--hd-white)`  
**Layout:** Centre-aligned, full-width typographic block. Max-width `800px` centred.  
**CSS class:** `hd-problem`

**Two-tone headline technique:**  
Create a reusable CSS class `.hd-two-tone` that renders the first half of the headline in `var(--hd-dark)` and the second half in `#6B7280` (grey-blue). Implementation: wrap the two parts in `<span class="hd-two-tone__dark">` and `<span class="hd-two-tone__muted">` respectively.

**H2 (two-tone):**  
`<span class="hd-two-tone__dark">Fuel management</span> <span class="hd-two-tone__muted">shouldn't be a guessing game.</span>`

**Body:** Stop relying on manual dipsticks, estimated consumption, and missing dockets. HyDip™ replaces guesswork with precision hardware and cloud-based software, giving you absolute control over who uses your fuel, when, and where.

---

### SECTION 4 — The "What" (Interactive Tabbed Solution)

**Background:** `var(--hd-grey)` (`#F5F5F5`)  
**CSS class:** `hd-tabs-section`

**Section header (H2):** A complete fuel ecosystem.

**Layout:** Horizontal tab bar across the top. Below: 50/50 split — left: copy panel, right: image panel. Clicking a tab swaps both the copy and the image. Use vanilla JS — no external libraries.

**Tab structure:**
```html
<div class="hd-tabs" role="tablist">
  <button class="hd-tab hd-tab--active" role="tab" data-tab="gauge">GAUGE</button>
  <button class="hd-tab" role="tab" data-tab="track">TRACK</button>
  <button class="hd-tab" role="tab" data-tab="dispense">DISPENSE</button>
  <button class="hd-tab" role="tab" data-tab="pay">PAY</button>
</div>
```

Active tab indicator: `border-bottom: 3px solid var(--hd-yellow)` on the active tab button.

**Tab content panels** (only active panel visible, others `display:none`):

| Tab | H3 | Body | Image |
|---|---|---|---|
| **GAUGE** | 24/7 visibility of fuel levels. | Real-time dip measurements for fuel storage tanks in any location. Remotely check tank levels, verify vendor deliveries, and automate your reordering via the HyDip Cloud platform to prevent costly stockouts. | `hydip-dashboard-map-alerts.png` |
| **TRACK** | Manage fuel to the litre. | Monitor fuel usage with highly reliable data. HyDip gives administrators 24/7 access to view and track consumption by individual vehicle, driver, or RFID tag, eliminating theft and misuse. | `hydip-tank-gauge-mobile.png` |
| **DISPENSE** | Robust and trusted dispensing. | Use industry-leading technology to authorise and track fuel. The highly customisable, weather-proof dispenser allows administrators to activate the bowser onsite or remotely at any time. | `hydip-refuel-illustration.png` |
| **PAY** | Unmanned 24/7 payments, without the broken hardware. | Turn your bulk tank into a 24/7 revenue generator for independent retail. HyDip integrates seamlessly with Fuelcharge mobile payment technology to authorise the bowser directly from a smartphone. Akin to the HyDip philosophy of simplicity, this integration eliminates the need for traditional outdoor payment terminals (OPTs). With no moving parts, no jammed receipt printers, and no weather-damaged card readers, your site stays online and keeps selling fuel without the maintenance headaches. | `hydip-hftv1-device.png` |

**JS behaviour:** On tab click — remove `hd-tab--active` from all tabs, add to clicked tab. Hide all `.hd-tab-panel`, show the matching one. No page reload, no hash change required.

---

### SECTION 5 — The "How" (Easy Onboarding Flow)

**Background:** `var(--hd-white)`  
**CSS class:** `hd-onboarding`  
**Layout:** 3-column step flow. Each column: large step number, heading, body. `border-radius: 0` on all containers.

**Section header (H2):** Easy as 1, 2, 3.

| Step | Heading | Body |
|---|---|---|
| **1** | Design your solution. | Speak to our digital team to spec the right HyDip hardware for your bulk tanks and fleet size. |
| **2** | HyDip is installed. | Our technicians deploy the hardware, whether you need standard 4G/Ethernet connectivity or remote off-grid solar setups. |
| **3** | Manage your fuel. | Log in to the cloud dashboard to manage tags, set limits, and instantly connect your data to Xero, MYOB, or SAP. |

Step numbers: large, `var(--hd-yellow)`, `font-size: 4rem`, `font-weight: 700`.

---

### SECTION 6 — Trust Block (Testimonials + Pillars)

**Background:** `var(--hd-dark)` (`#13114D`)  
**CSS class:** `hd-trust`  
**Layout:** Two rows within one section.

**Row 1 — Testimonials (split grid, 2 columns):**

Each testimonial card: white card on dark background, `border-radius: 0`, quote text, attribution.

| | Quote | Attribution |
|---|---|---|
| **Quote 1** | "IOR were a breath of fresh air... This system has made us a far better business, and I would recommend this system to anyone." | Hugh Ball, Norwood Agriculture |
| **Quote 2** | "I drive past the fuel dock on my day off and see customers using Fuelcharge to pay online. I can see the transactions and know that I'm making money even when the site is unmanned." | Chris Rippon, Tin Can Bay Marina |

**Row 2 — Pillars (3 columns):**

**Eyebrow:** WHY HYDIP?

| Pillar | Heading | Body |
|---|---|---|
| **1** | Supported. | Backed by 24/7 local technical assistance, remote diagnostics, and national installation capability. |
| **2** | Robust. | Modern, simple hardware designed for the harshest Australian environments with IP67 ratings and resilience to power fluctuations. |
| **3** | Connected. | Seamlessly links to 3G/4G, Ethernet, Wi-Fi, and GPS. Connects to 3rd party dispensers like COMPAC, SANKI, and CONTREC. |

Pillar headings: `var(--hd-yellow)`. Body text: `var(--hd-white)`.

---

### SECTION 7 — Hardware Specifications (Ungated Downloads)

**Background:** `var(--hd-grey)` (`#F5F5F5`)  
**CSS class:** `hd-hardware`  
**Layout:** 3-column card grid. White cards. `border-radius: 0`. No forms.

**Section header (H2):** Built for every environment.

**Card 1 — HDV2 Tank Gauging**

Image: `hydip-hdv2-device.png` (top of card, `object-fit: contain`, white bg)  
Title (H3): HDV2 Tank Gauging  
Specs (bullet list):
- Supports up to 4 tank level sensors (4-20mA)
- 3G, 4G, and XBee communications
- Standalone solar panel & internal battery options

CTA: `Download Specs ↓` — `href="assets/pdfs/HyDip-HDV2-Specs.pdf"` — `download` attribute — ghost/text-link style (no filled background)

**Card 2 — HFTV1 Fuel Tracking**

Image: `hydip-hftv1-device.png` (top of card, `object-fit: contain`, white bg)  
Title (H3): HFTV1 Fuel Tracking  
Specs (bullet list):
- RFID tag-based pump authorisation
- Direct integration with 3rd party dispensers
- 3G and Ethernet communication interfaces

CTA: `Download Specs ↓` — `href="assets/pdfs/HyDip-HFTV1-Specs.pdf"` — `download` attribute — ghost/text-link style

**Card 3 — HDX2 Fuel Management**

Image: `<div class="hd-device-placeholder">HDX2 — Image coming soon</div>` (styled as a grey placeholder box, same dimensions as the other card images)  
Title (H3): HDX2 Fuel Management  
Specs (bullet list):
- Direct I/O pump start/stop capabilities
- 110/240V AC or 12V DC power inputs
- NMI Approved Flow Computer

CTA: `Enquire about HDX2 ↓` — `href="#hd-form"` (anchors to the form below) — ghost/text-link style

---

### SECTION 8 — Dual-Purpose Lead Trap (Enquiry + Brochure)

**id:** `hd-form` (this is the anchor target for all "Enquire Now" CTAs)  
**Background:** `var(--hd-dark)` (`#13114D`)  
**CSS class:** `hd-lead-trap`  
**Layout:** 50/50 split. Left: copy. Right: HubSpot form embed.

**Eyebrow:** GET STARTED

**H2:** Ready to take control of your fuel?

**Body (left column):** Download the complete HyDip™ Product Brochure for detailed features, FTC claim methodology, and integration guides — or submit your details below to have an IOR digital specialist contact you directly to map out a custom telemetry solution for your sites.

**Brochure download CTA (left column):**  
`Download HyDip Brochure ↓` — `href="assets/pdfs/HyDip-Product-Brochure.pdf"` — `download` attribute — styled as `btn--hd-secondary` (white outline)

**Right column — HubSpot form embed:**
```html
<div class="hd-form-embed">
  <!-- HubSpot Form: 2DEKpUanRQ_GZw0Jd7xaN7w -->
  <script charset="utf-8" type="text/javascript" src="//js.hsforms.net/forms/embed/v2.js"></script>
  <script>
    hbspt.forms.create({
      region: "na1",
      portalId: "YOUR_PORTAL_ID",
      formId: "2DEKpUanRQ_GZw0Jd7xaN7w"
    });
  </script>
</div>
```
> **Note:** Replace `YOUR_PORTAL_ID` with the actual HubSpot portal ID when known. For the prototype, render a visible placeholder: `<div class="hd-form-placeholder">HubSpot Form: 2DEKpUanRQ_GZw0Jd7xaN7w — will load in production</div>` styled with a dashed border and white text so the placeholder is clearly visible.

---

### SECTION 9 — FAQ Accordion

**Background:** `var(--hd-white)`  
**CSS class:** `hd-faq`  
**Layout:** Standard accordion. One open at a time. Vanilla JS only.

**Section header (H2):** Frequently asked questions

| Q | A |
|---|---|
| **Q1: What is the HyDip fuel management system?** | HyDip™ is IOR's proprietary cloud-based fuel management system, designed and built in Australia for Australian operators. It combines precision hardware (tank gauges, fuel tracking units, dispensers) with a cloud platform to give businesses real-time visibility of fuel levels, usage, and transactions across all sites. |
| **Q2: How does HyDip help track fuel usage?** | HyDip Fuel Tracking devices monitor dispensing events via RFID tags, recording which vehicle or driver used fuel, how much, and when. Administrators access this data 24/7 through the HyDip Cloud dashboard, with reporting exportable to Xero, MYOB, or SAP. |
| **Q3: Who should use a fuel management system like HyDip?** | HyDip suits any Australian business with bulk fuel storage — from agricultural operations and mining sites to transport fleets, marinas, and independent fuel retailers. If you manage fuel for multiple assets or sell fuel to third parties, HyDip gives you the control and compliance tools you need. |
| **Q4: Can HyDip work with fuel storage tanks?** | Yes. HyDip's HDV2 Tank Gauging unit supports up to four tank level sensors using industry-standard 4-20mA technology, making it compatible with virtually any existing tank setup. It can be installed on diesel, unleaded, AdBlue, and aviation fuel tanks. |
| **Q5: What reporting or visibility benefits does HyDip provide?** | HyDip provides near real-time tank level visibility, automated low-stock alerts, proof-of-delivery verification, per-asset consumption reports, and automated Fuel Tax Credit (FTC) reporting data — all accessible via web, mobile, and tablet. |
| **Q6: How do I enquire about HyDip with IOR?** | Complete the enquiry form on this page and an IOR digital specialist will contact you to map out the right HyDip configuration for your sites. You can also call IOR on 1800 449 347. |

---

### SECTION 10 — Canonical Pre-footer + Footer (verbatim from Shell v5)

Copy the `<section class="pre-footer">` and `<footer>` blocks verbatim from `IOR_Utility_Template_Shell_v5.html`. No changes.

---

## Handoff Notes for Builder

### What the v5 builder got wrong (do not repeat)
1. **Hero was 50/50 split** — must be centre-aligned, single column.
2. **Used a generic 3-column "capabilities" block** — must be the interactive 4-tab component (GAUGE / TRACK / DISPENSE / PAY).
3. **Hardware was a 50/50 split** — must be a 3-column card grid with PDF download links.
4. **Missing the HubSpot form** — Section 8 (lead trap) is mandatory.
5. **Missing testimonials** — Section 6 Row 1 is mandatory.
6. **Missing the two-tone headline** — Section 3 requires the `.hd-two-tone` CSS technique.

### Golden Rules self-audit checklist (run before opening PR)
- [ ] `border-radius: 0` on ALL containers, cards, tabs, and buttons except `.btn--pill` (nav only)
- [ ] Zero CSS gradients — all backgrounds are solid `var(--hd-*)` colours
- [ ] Zero inline `style=` attributes on body elements
- [ ] Hero background is `var(--hd-blue)` solid — no overlay, no image
- [ ] Quick Links Bar is BELOW the hero, not above
- [ ] Nav and footer are verbatim from `IOR_Utility_Template_Shell_v5.html` — no changes
- [ ] HyDip branding (`--hd-blue`, `--hd-yellow`, `--hd-dark`) does NOT appear inside `<nav>` or `<footer>`
- [ ] No word "depot" anywhere
- [ ] No operating hours anywhere
- [ ] All 3 PDF download links use `download` attribute and correct `assets/pdfs/` paths
- [ ] HubSpot form placeholder is visible (dashed border, white text on dark bg)
- [ ] Tab JS works: clicking each tab shows correct copy + image
- [ ] FAQ accordion JS works: clicking a question opens/closes it
- [ ] All Support Hub links use `11_Support_Hubv5.html`
- [ ] No placeholder YouTube IDs
- [ ] `07a_HyDip_FMSv5.html` is NOT referenced anywhere in this file

### PR instructions
- Branch: `feature/hydip-fms-v6`
- File: `07a_HyDip_FMSv6.html` only — do NOT modify `00_Master_Index.html` in the PR
- PR title: `feat: HyDip FMS v6 — bespoke rebuild (centre hero, tabs, hardware cards, HubSpot form)`
- PR description: include the self-audit checklist results
