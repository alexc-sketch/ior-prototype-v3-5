# Builder Brief: Find a Location v5

**To:** Development Team  
**From:** UX Audit / Manus AI Builder  
**Date:** April 25, 2026  
**Project:** IOR Prototype v3.5  

---

## 1. File & Setup Directives

- **Target Filename:** `11d_Find_Locationv5.html`
- **Base Template:** `IOR_Utility_Template_Shell_v5.html`
- **Visual Reference:** `IOR_Wireframes (15).html#find-a-location`

### 💡 Auditor Note: The Build Strategy
This page must be built using the new `IOR_Utility_Template_Shell_v5.html` as the foundation. 
- **The Map is the Hero:** This is the ONLY page on the entire site that uses the interactive Storepoint widget. The map container must be highly responsive and touch-friendly for mobile drivers/pilots.
- **Layout Update:** Per the client brief, we are removing the "Browse by State" 3rd card from the below-map utility section. It will just be a clean 2-card layout (Fuelcharge + Fleet Account).

---

## 2. SEO & Meta Data

- **Meta Title:** Find an IOR Diesel Stop or Airport | IOR
- **Meta Description:** Find your nearest IOR diesel stop or aviation fuel location. 115+ diesel sites and 32+ airports across Australia. Search by location or corridor.
- **Target Keywords:** Find IOR diesel stop, aviation fuel locations Australia, IOR network map, fuel near me.

---

## 3. Wireframe Component Flow & Structure

*(Auditor: Please ensure the builder matches this exact top-to-bottom component flow)*

### 1. Minimal Utility Hero
- **Style:** Solid brand color (`var(--ior-navy)`).
- **Eyebrow:** NETWORK LOCATOR
- **H1:** Find an IOR Location.
- **Subcopy:** Search for diesel stops, aviation fuel sites, depots, and offices near you.
- **CTAs (2 Buttons):**
  - Primary Button: Apply Now (Links to account application)
  - Outline White Button: Register Your Interest

### 2. Quick Links Bar ("Explore:")
- **Style:** The standard sticky horizontal link bar.
- **Label:** Explore:
- **Links Required:**
  1. IOR Diesel Network
  2. IOR Aviation Network
  3. Fuelcharge
  4. Support & Contact

### 3. Interactive Map & Mode Switcher (The Core Interaction)
- **Mode Switcher (Tabs):** Directly above the map, build a 2-tab switcher: `Ground Fuels | Aviation`. (Clicking these should toggle the map data/filters if the Storepoint API allows, or simply switch the visual context).
- **Storepoint Embed:** Embed the map using a full-width, highly visible container.

**DEV INSTRUCTION — INJECT THIS EXACT SCRIPT:**
```html
<div id="storepoint-widget"></div>
<script>
window.Storepoint=window.Storepoint||{_q:[],on:function(e,c){this._q.push([e,c])}};
window.loadStorepoint=function(){new StorepointWidget('169b243d6de664','#storepoint-widget',{});};
!function(){var t=document.createElement("script");t.type="text/javascript";t.async=!0;t.src="https://widget.storepoint.co/embed.js";t.onload=function(){"function"==typeof window.loadStorepoint&&window.loadStorepoint()};document.head.appendChild(t);}();
</script>
```

### 4. Below-Map Utility Cards
- **Layout:** A clean 2-column grid (`grid-template-columns: 1fr 1fr`) sitting below the map. Do not include the State links.

**Card 1: Fuelcharge (Pay at the Pump)**
- **Icon:** 📱
- **H4:** Pay at the Pump
- **Copy:** Download Fuelcharge to find sites, unlock pumps, and pay — no account required.
- **CTAs:** ⬇ App Store | ⬇ Google Play | Learn More →

**Card 2: Fleet Account**
- **Icon:** 💳
- **H4:** Open a Fleet Account
- **Copy:** Get volume pricing, consolidated invoicing, and dedicated account support for your fleet.
- **CTA:** Apply for an Account →

### 5. Direct Download Strip (Dual Assets)
- **Layout:** Use a dark background strip (`var(--ior-navy)` or `var(--s800)`) with a split 2-column layout to house the two directory downloads.
- **Auditor Note:** Per client revision, these are **direct, minimalistic downloads**. Do NOT use a HubSpot form or gated modal. Link directly to the PDF files provided in the repository.

**Asset 1 (Left):**
- **Title:** Diesel Network Directory
- **Subcopy:** Download the complete guide including all 24/7 truck stop locations, B-double access, and amenities.
- **Asset ID:** IOR-MAR-BRO-0232
- **CTA:** Download Diesel Directory ↓ (Links directly to `IOR-MAR-BRO-0232-Diesel-Network-Directory_v20260203.pdf` with `target="_blank"`)

**Asset 2 (Right):**
- **Title:** Aviation Network Directory
- **Subcopy:** Download the complete aviation location list including Jet A-1, Avgas, and into-plane service availability.
- **Asset ID:** IOR-MAR-BRO-0332
- **CTA:** Download Aviation Directory ↓ (Links directly to `IOR-MAR-BRO-0332-Aviation-Network-Directory_v20250812-1.pdf` with `target="_blank"`)

### 6. FAQ Accordion
- **Style:** Inject the standard Global FAQ accordion component here.
- **Content:** Populate with 3-4 map-specific questions (e.g., "How do I filter for Truck Wash sites?", "Does the map show live fuel outages?").

### 7. Global Footer
- **Style:** Append the standard v4.0 6-column global footer.

---

## 4. Asset Checklist for Builder
- [x] Storepoint HTML snippet provided in brief.
- [x] Direct Asset PDFs provided in repo (`IOR-MAR-BRO-0232-Diesel-Network-Directory_v20260203.pdf` and `IOR-MAR-BRO-0332-Aviation-Network-Directory_v20250812-1.pdf`).
- [x] Base Template to Duplicate/Use: `IOR_Utility_Template_Shell_v5.html`
