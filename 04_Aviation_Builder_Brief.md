# Builder Brief: Aviation Module (04) & Lead Capture Pivot

**Project:** IOR Prototype v3.5
**Module:** 04 Aviation
**Author:** Manus AI
**Date:** April 2026

This brief outlines the extraction of the Aviation module from its monolithic wireframe spec into standalone spoke pages, mirroring the successful process used for Ground Fuels (03). It also introduces a strategic pivot for lead generation and gated assets, which must be applied to the new Aviation pages and back-ported to the existing Ground Fuels pages.

---

## 1. Strategic Pivot: Lead Capture & Gated Assets

Following a recent WIP meeting with the client, the dedicated `/download/` landing page pattern has been cancelled. The client has built smart HubSpot forms capable of handling both general enquiries and gated asset requests simultaneously from a single form.

### 1.1 The Anchor Link Update

All Call-to-Action (CTA) buttons on service and industry pages that previously linked to a separate download or enquiry page must now use an anchor link pointing to the form section at the bottom of the current page.

**Action:** Update the `href` on these buttons.
**Example:** `<a href="#lead-capture" class="btn btn--primary">Download Brochure</a>`

### 1.2 Dynamic Silo Theming

The contact/form container at the bottom of the page must feel native to the specific silo it sits in. The wrapper around the HubSpot form must utilise global CSS variables to shift colour based on the page type.

**Action:** Apply the `data-silo` attribute and corresponding CSS variables.
- **Ground Fuels:** Use `var(--ior-blue)` for accents and borders.
- **Aviation:** Use `var(--av-gold)` and dark slate for accents. (Note: The design system currently uses `--aviation-gold`; ensure `--av-gold` is aliased or use the existing variable).
- **Supply & Trading / Equipment:** Follow their respective silo colour palettes.

### 1.3 HubSpot Form Mapping

Embed scripts must be mapped according to the page category using the specific form IDs provided by the client.

**Ground Fuels Pages:**
- **Form URL:** `https://7b3kb1.share-ap1.hsforms.com/2DEKpUanRQ_GZw0Jd7xaN7w`
- **Applies to:** Diesel Network, On-Site, Bulk, AdBlue, Oils & Lubes, Transport & Logistics.

**Aviation Pages:**
- **Form URL:** `https://7b3kb1.share-ap1.hsforms.com/2fLXb3qo4TP-CkWPoB5TYMQ`
- **Applies to:** Aviation Network, Airport Services, Aviation Bulk, Commercial Aviation, GA.

### 1.4 Required HTML Structure (The Lead Capture Block)

The contact container at the bottom of service pages must follow a split-layout structure (text/callouts on the left, form on the right), using the HyDip™ FMS Product Sheet design as a structural reference only.

**Content Rules for the Lead Capture Block:**
1. **Contextual Messaging:** The headline and sub-copy must dynamically reference both the general enquiry context and the specific gated asset for that page. For example, on the Aviation Network page, the headline should read "Get the Aviation Network Directory + talk to our team" rather than a generic "Let's get your business moving."
2. **Minimalistic Callouts:** The bullet list on the left side of the split must be minimalistic. Use a maximum of three short callouts, single line each, with no decorative bullets. The language must be tight and direct.

**HTML Structure Example:**

```html
<section id="lead-capture" class="lead-capture-section fade-up" data-silo="[dynamic-silo-name]" style="padding: 80px 0; background: var(--grey-50);">
  <div class="container" style="max-width: 1200px; margin: 0 auto; background: #fff; border-top: 4px solid var(--silo-accent-color, #0355A3); border-radius: 8px; box-shadow: var(--shadow-md); padding: 48px; display: grid; grid-template-columns: 1fr 1fr; gap: 48px;">
    
    <!-- Left Column: Contextual Messaging & Minimalistic Callouts -->
    <div class="lead-capture__content">
      <span class="eyebrow" style="color: var(--silo-accent-color, #0355A3);">FREE DOWNLOAD & ENQUIRY</span>
      <h2 style="font-size: 32px; font-weight: 800; color: var(--grey-900); margin-bottom: 16px;">[Dynamic Headline: Asset Name + Enquiry]</h2>
      <p style="font-size: 16px; color: var(--grey-700); margin-bottom: 32px;">[Dynamic Sub-copy: Briefly explain what the user gets and how the team can help.]</p>
      
      <ul class="lead-capture__callouts" style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px;">
        <li style="font-size: 15px; color: var(--grey-800); display: flex; align-items: center; gap: 8px;">
          <span style="width: 8px; height: 8px; background: var(--silo-accent-color, #0355A3); display: inline-block;"></span>
          [Minimalistic Callout 1]
        </li>
        <li style="font-size: 15px; color: var(--grey-800); display: flex; align-items: center; gap: 8px;">
          <span style="width: 8px; height: 8px; background: var(--silo-accent-color, #0355A3); display: inline-block;"></span>
          [Minimalistic Callout 2]
        </li>
        <li style="font-size: 15px; color: var(--grey-800); display: flex; align-items: center; gap: 8px;">
          <span style="width: 8px; height: 8px; background: var(--silo-accent-color, #0355A3); display: inline-block;"></span>
          [Minimalistic Callout 3]
        </li>
      </ul>
    </div>

    <!-- Right Column: HubSpot Form -->
    <div class="lead-capture__form-wrapper" style="background: var(--grey-50); padding: 32px; border-radius: 8px; border: 1px solid var(--grey-100);">
      <script charset="utf-8" type="text/javascript" src="//js.hsforms.net/forms/embed/v2.js"></script>
      <script>
        hbspt.forms.create({
          region: "ap1",
          portalId: "YOUR_PORTAL_ID",
          formId: "DYNAMIC_FORM_ID_BASED_ON_SILO"
        });
      </script>
    </div>
    
  </div>
</section>
```

---

## 2. Aviation Module (04) Extraction

The current `04_Aviation.html` is a monolithic wireframe spec containing five distinct pages. These must be extracted into standalone files, following the exact process used for Ground Fuels.

### 2.1 Source Material

Always use the explicitly provided baseline file (`04_Aviation.html`) as the working source. Ignore any existing fabricated files in the repository.

### 2.2 Target Files

Extract the five pages into the following standalone files:

| Page | Title | Target Filename | Anchor |
|---|---|---|---|
| 1 | Aviation Hub | `04_Aviation_Hub_v3.5.html` | `#aviation-hub` |
| 2 | IOR Aviation Network | `04a_Aviation_Network_v3.5.html` | `#aviation-network` |
| 3 | Airport Fuelling Services | `04b_Airport_Fuelling_v3.5.html` | `#airport-fuelling-services` |
| 4 | Aviation Bulk Delivery | `04c_Aviation_Bulk_v3.5.html` | `#aviation-bulk-delivery` |
| 5 | Aviation Oils & Lubricants | `04d_Aviation_Oils_v3.5.html` | `#aviation-oils-lubricants` |

### 2.3 Extraction Rules

1. **Faithful Rebuild:** Extract the content verbatim from the baseline spec. Do not fabricate filler copy, new heroes, or new testimonials.
2. **Global Components:** Utilise global elements such as header (desktop and mobile), footer (desktop and mobile), case study/blog containers, logo carousel, and quick links. Reference the [Global Components](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html) guide.
3. **Design System Compliance:**
   - **No rounded corners:** Default to square corners on every image, thumbnail, and media frame. The only permitted radius is `.btn--pill { border-radius: 500px; }`.
   - **No gradients:** The global site header must use flat solid colours only. Gradients should not be used on hero imagery.
   - **Aviation Theme:** Use Aviation Gold (`#D98300`) for accents, replacing the IOR Blue used in Ground Fuels.
4. **Lead Capture Integration:** Implement the new split-layout lead capture block (Section 1.4) at the bottom of each extracted page, using the Aviation HubSpot form ID and theming. Ensure the copy dynamically references the page's specific gated asset (e.g., `IOR-MAR-BRO-0332-Aviation-Network-Directory_v20250812-1.pdf` for the Aviation Network page). Update all relevant CTAs to anchor to `#lead-capture`.
5. **Annotation Removal:** Ensure no wireframe annotations (`.ann`, `.wf-nav`, `LOGO PENDING`, etc.) leak into the production files.
6. **Prototype Nav Bar:** Include the dev/admin `.proto-bar` at the top of each page, providing return links to the Master Index, Design System, and Global Components.

### 2.4 Monolithic Spec Retirement

Once the standalone pages are built and verified:

1. **Backup:** Copy the original `04_Aviation.html` to `04_Aviation_BASELINE_SPEC.html` for internal reference.
2. **Redirect:** Overwrite `04_Aviation.html` with a clean redirect page.
3. **Mapping:** Map the legacy hash anchors (`#aviation-hub`, `#aviation-network`, etc.) to their new standalone filenames via client-side JavaScript.
4. **Fallback:** Provide a default redirect to `02_Fuel_Solutions_Hub.html#aviation` and a `meta http-equiv="refresh"` fallback.

---

## 3. Back-porting to Ground Fuels (03)

The new split-layout lead capture pattern must be retroactively applied to the recently built Ground Fuels spoke pages (`03a` through `03e`).

**Action:**
1. Replace the existing HubSpot placeholder with the new split-layout lead capture block (Section 1.4).
2. Apply the Ground Fuels HubSpot form ID and `var(--ior-blue)` theming.
3. Ensure the copy dynamically references the page's specific gated asset (e.g., the Diesel Network Brochure for `03a`).
4. Update all "Download Brochure" or "Enquire Now" CTAs on these pages to anchor to `#lead-capture`.

---

## 4. Development Workflow

1. **Branching:** Never commit directly to the main branch. Always work on a named branch (e.g., `feat/04-aviation-extraction`).
2. **Codebase Restrictions:** Do not modify `ior-global.css`, `ior-global.js`, `ior-motion.js`, or `IOR_Design_System.html` unless explicitly authorised. Do not alter navigation, footer structure, or component classes.
3. **Quality Assurance:** Act as an HTML auditor, UX mapping auditor, and content auditor. Ensure zero issues in builds before opening a pull request.
4. **Master Index:** Update `00_Master_Index.html` to ensure all Aviation cards link correctly to the new standalone pages.
5. **Review:** Open a pull request and provide a link for the user to view the environment, along with notes for the auditor.
