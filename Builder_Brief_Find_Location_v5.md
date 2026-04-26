Global Components Reference: https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html

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

- **Staging Link:** `https://alexc-sketch.github.io/ior-prototype-v3-5/11d_Find_Locationv5.html`
- **Meta Title:** Find an IOR Diesel Stop or Airport | IOR
- **Meta Description:** Find your nearest IOR diesel stop or aviation fuel location. 115+ diesel sites and 32+ airports across Australia. Search by location or corridor.
- **Focus Keyword:** Find IOR diesel stop
- **Secondary Keywords:** aviation fuel locations Australia, IOR network map, fuel near me

---

## 3. Wireframe Component Flow & Structure

*(Auditor: Please ensure the builder matches this exact top-to-bottom component flow)*

### 1. Utility Hero — "Canopy Overhang" Treatment
- **Style:** Solid brand color (`var(--ior-navy)`) background.
- **Layout:** 2-column split (Left: Copy, Right: Map Overlay + Image).
- **Left Column (Copy):**
  - **Eyebrow:** NATIONAL FUEL NETWORK
  - **H1:** Find fuel for your fleet or flight.
  - **Subcopy:** Search our integrated network of 24/7 diesel truck stops and aviation refuelling locations across Australia.
  - **CTAs (2 Buttons):**
    - Primary Button: Apply Now (Links to account application)
    - Outline White Button: Register Your Interest
- **Right Column (Map Overlay):**
  - Use `assets/icons/Map2.svg` (Australia map with white dots) as a decorative background graphic or positioned element behind the hero image.
- **Hero Image (Canopy Overhang):**
  - Use `assets/images/Charlton-HERO-IORcopy.webp`.
  - **Crucial Design Detail:** The image must be positioned using negative margin (e.g., `margin-bottom: -80px`) or absolute positioning so that the canopy roof physically "sticks out" and overlaps the section below it. This breaks the boxed-in feel and adds depth.

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
- **Branding:** Use official Fuelcharge branding (dark `#1A1A2E` background, orange `#FF6B2B` accents).
- **Eyebrow:** FUELCHARGE
- **H4:** Pay at the Pump
- **Copy:** Download Fuelcharge to find sites, unlock pumps, and pay — no account required.
- **CTAs:** ⬇ App Store | ⬇ Google Play | Learn More → (Ghost/Text Link)

**Card 2: Fleet Account**
- **Eyebrow:** CUSTOMER PORTAL
- **H4:** Open a Fleet Account
- **Copy:** Get volume pricing, consolidated invoicing, and dedicated account support for your fleet.
- **CTA:** Apply for an Account →

### 5. Gated Download Strip (Dual Assets)
- **Layout:** Use a dark background strip (`var(--ior-navy)`) with a split 2-column layout to house the two directory downloads.
- **Auditor Note:** These are **gated downloads**. Do NOT link directly to PDFs. The buttons must trigger a HubSpot form (use `href="#"` and a `<!-- HUBSPOT FORM TRIGGER -->` comment for the builder).

**Asset 1 (Left):**
- **Icon:** Full fuel pump SVG (`assets/icons/icon-fuel-pump.svg`)
- **Title:** Diesel Network Directory
- **Subcopy:** Download the complete guide including all 24/7 truck stop locations, B-double access, and amenities.
- **CTA:** Download Diesel Directory ↓ (Triggers HubSpot Form)

**Asset 2 (Right):**
- **Icon:** Airplane SVG (`assets/icons/icon-airplane.svg`)
- **Title:** Aviation Network Directory
- **Subcopy:** Download the complete aviation location list including Jet A-1, Avgas, and into-plane service availability.
- **CTA:** Download Aviation Directory ↓ (Triggers HubSpot Form)

### 6. FAQ Accordion
- **Style:** Inject the standard Global FAQ accordion component here.
- **Content:** Populate with 4 map-specific questions (e.g., "How do I filter for Truck Wash sites?", "Can I access IOR locations without a fleet account?").

### 7. Global Footer
- **Style:** Append the canonical v5 6-column global footer (from `11a_Contact_Usv5.html`).

---

## 4. Asset Checklist for Builder
- [x] Storepoint HTML snippet provided in brief.
- [x] Hero Image: `assets/images/Charlton-HERO-IORcopy.webp`
- [x] Map Overlay: `assets/icons/Map2.svg`
- [x] Base Template to Duplicate/Use: `IOR_Utility_Template_Shell_v5.html`
