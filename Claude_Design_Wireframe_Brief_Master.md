# IOR Website Rebuild — Master Claude Design Wireframe Brief

**Project:** IOR Website Rebuild (v5/v8 Architecture)
**Target AI:** Claude (Design & Wireframing)
**Objective:** Provide a comprehensive, single-source-of-truth briefing document for Claude to generate complete, production-ready HTML/CSS wireframes for every page in the IOR Master Index.

---

## 1. GLOBAL DESIGN SYSTEM & BUILD RULES

Claude must adhere to these absolute rules across all pages. Any deviation is considered a failure.

### 1.1 The Starting Point
Every page must be built using the global shell and components. Do not invent new navigation or footer structures.
*   **Global Shell:** `https://alexc-sketch.github.io/ior-prototype-v3-5/IOR_Global_Template_Shell_v4.html`
*   **Global Components:** `https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html`

### 1.2 Absolute Design Rules (Zero-Error Mandate)
*   **No Gradients:** Backgrounds must be solid, full-bleed colours. No CSS gradients in any hero or section header (photographic scrims are permitted).
*   **Sharp Geometry:** `border-radius: 0` on all cards, buttons, containers, and images. No rounded corners anywhere.
*   **Quick Links Bar:** Must sit immediately below the hero banner. It is never sticky.
*   **Colour Scope:** Bespoke brand colours apply to page content only. Do not alter the global navigation, footer, or utility bar colours.
*   **Hero Overlays:** No solid blue overlays on hero images. Use subtle dark scrims only if necessary for text legibility.
*   **Typography:** Avenir Next LT Pro. Bold (700) for headlines, Regular (400) for body copy.

### 1.3 Brand Tone of Voice
Professional, innovative, reliable, and 'adult'. Grounded, Australian, and community-focused. Avoid disjointed or overly playful branding.

---

## 2. SITE ARCHITECTURE & PAGE CATALOGUE

The site is structured into distinct silos. Claude must generate wireframes for the following pages, ensuring consistent section flow within each silo.

### 2.1 Homepage & Global Components
*   **01_Homepage.html:** The primary entry point. Features a dynamic hero, end-to-end fuel solutions routing, digital platforms teaser, and social proof.
*   **00_Global_Components.html:** The reference library for buttons, cards, accordions, and typography.

### 2.2 Hub Pages (Routing Nodes)
*   **02_Fuel_Solutions_Hub.html:** Routes to Ground Fuels, Aviation, Equipment, and Supply.
*   **07_Digital_Platformsv8.html:** Routes to HyDip FMS, Fuelcharge, and Customer Portal.
*   **08_Industries_v5.html:** Routes to the 8 core industries served by IOR.
*   **09_About_IOR.html:** Routes to Leadership, Community, Sustainability, and Case Studies.
*   **11_Support_Hubv5.html:** Routes to Contact, Locations, Payments, and Downloads.

### 2.3 Ground Fuels Silo
*   **03a_Diesel_Network_v3.5.html:** IOR Diesel Network (Map, stop finder).
*   **03b_On_Site_Refuelling_v3.5.html:** Mobile refuelling and wet hosing.
*   **03c_Bulk_Diesel_Delivery_v3.5.html:** Bulk tanker delivery.
*   **03d_HyBlue_v3.5.html:** DEF/AdBlue supply.
*   **03e_Oils_Lubricants_v3.5.html:** Engine oils and hydraulic fluids.

### 2.4 Aviation Silo (Visually Distinct)
*   **04_Aviation_Hub_v3.5.html:** Gold identity, dark charcoal hero.
*   **04a_Aviation_Network_v3.5.html:** Airstrip coverage and map.
*   **04b_Airport_Fuelling_v3.5.html:** Avgas, Jet A-1, into-plane services.
*   **04c_Aviation_Bulk_v3.5.html:** Remote airstrip bulk delivery.
*   **04d_Aviation_Oils_v3.5.html:** Piston and turbine oils.

### 2.5 Digital Platforms Silo (SaaS Vibe)
*   **07a_HyDip_FMS_v8.html:** Hardware + Software focus. Azure Blue hero, interactive tabs.
*   **07b_Fuelcharge_App_v8.html:** B2C fintech vibe. High contrast, QR codes, no forms.
*   **07c_Customer_Portal_v8.html:** Enterprise SaaS vibe. 2x2 Bento Box feature grid.

### 2.6 Industries We Serve Silo
*   **08a_Mining_v5.html:** Mining & Resources.
*   **08b_Agriculture_v5.html:** Agriculture & Harvest.
*   **08c_Transport_v5.html:** Transport & Logistics.
*   **08d_Construction_v5.html:** Construction & Civil.
*   **08e_Livestock_v5.html:** Livestock & Rural Operations.
*   **08f_Government_v5.html:** Government & Defence.
*   **08g_Aviation_v5.html:** Commercial & General Aviation.
*   **08h_Oil_Gas_v5.html:** Oil & Gas.

### 2.7 About IOR & Leadership
*   **09a_Our_Leadership.html:** Executive team directory.
*   **09a_Leadership_Bio_Template_v5.html:** Individual bio template (2-col hero, tabbed content).
*   **09b_Community.html:** Community & Giving Back.
*   **09c_Sustainability.html:** HSE & ESG.
*   **09d_Case_Studies_v6.html:** Archive list with taxonomy filter.
*   **09d_Case_Study_Singlev6.html:** Dynamic template (70/30 WYSIWYG + sticky sidebar).

### 2.8 Careers
*   **10a_Entry_Pathways.html:** Tabbed directory.
*   **10b_Apprentices.html:** Apprentices & Trades.
*   **10c_Graduates.html:** Graduates & Interns.
*   **10d_School_Based.html:** School-Based & Trainees.
*   **10e_Working_Regionally.html:** Regional life and Eromanga origin.

### 2.9 Support & Contact (Utility Shell)
*   **11a_Contact_Usv5.html:** 2-col contact grid, Zendesk form.
*   **11b_Regional_Contactsv5.html:** Interactive SVG map, state directory.
*   **11d_Find_Locationv5.html:** StorePoint map embed.
*   **11e_Make_Paymentv5.html:** Payment gateways and EFT details.
*   **11f_Policy_Downloads.html:** Categorised accordions.

---

## 3. PAGE-SPECIFIC WIREFRAME INSTRUCTIONS

When generating wireframes for specific sections, Claude must follow these structural patterns.

### 3.1 Standard Industry Page Pattern (e.g., Mining, Agriculture)
1.  **Hero:** 50/50 split. H1, subcopy, 2 CTAs. Right side is an image placeholder.
2.  **Quick Links Bar:** 4 anchor links.
3.  **The "Why" (Problem):** H2, body copy, 3-column stat bar.
4.  **The "How" (Process):** 3-step horizontal flow or interactive tabs.
5.  **The "What" (Solutions):** 2x2 Bento Box or 3-column card grid.
6.  **Social Proof:** Testimonial quote and attribution.
7.  **Lead Trap:** 50/50 split. Left side copy, right side HubSpot form placeholder.
8.  **FAQ:** Accordion component.
9.  **Related Content:** 3-card grid linking to Hub and sibling pages.

### 3.2 Digital Platforms Hub Pattern
1.  **SaaS Hero:** Overlapping device mockups (Tablet + Laptop). Solid background.
2.  **Quick Links Bar:** HyDip | Fuelcharge | Portal | FAQs.
3.  **The "Why":** Two-tone H2. Real metrics (2,400+ accounts, $18M+ FTC, $0 fees).
4.  **The "How":** 1-2-3 Ecosystem Flow.
5.  **Flip Cards:** 2-column grid with CSS 3D flip effect for HyDip and Portal.
6.  **B2C Callout:** Slim, high-contrast horizontal band for Fuelcharge app.
7.  **Trust Block:** Case study quote + routing box.
8.  **FAQ & Related Content.**

### 3.3 Customer Portal Pattern
1.  **Hero:** Asymmetrical 40/60 split. Overlapping Tablet and iPhone mockup.
2.  **Bento Box:** 2x2 CSS Grid (`grid-template-columns: 1fr 1fr`). UI snippets bleeding off card edges.
3.  **Three-Path Access:** 3-column block (Existing User, Unregistered User, New to IOR).
4.  **Modal:** 'Request Access' buttons must trigger a pop-up modal, not an inline form.

### 3.4 Fuelcharge App Pattern
1.  **Hero:** Frictionless B2C vibe. Floating device mockup. App Store/Google Play SVG badges. QR code on desktop.
2.  **Audience Flip Cards:** 3-column grid (Vehicles & 4WD, Aviation, Marine).
3.  **Network Map Teaser:** Zoomed-out map visual with CTA.
4.  **Easy-as-1-2-3 Flow:** Left side vertical tabs, right side dynamic media container (YouTube embeds or device mockups).
5.  **NO FORMS:** Do not include any lead-generation forms on this page.

### 3.5 HyDip FMS Pattern
1.  **Hero:** Centre-aligned. Full-bleed Azure Blue (`#0054A4`). Hand holding smartphone over laptop.
2.  **Interactive Tabs:** 4 horizontal tabs (Gauge, Track, Dispense, Pay) swapping content on click. Do not use a static 3-column block.
3.  **Hardware Specs:** 3-column card grid with direct PDF download links.
4.  **Lead Trap:** Dark Neutral (`#13114D`) full-width block with HubSpot form.

---

## 4. ASSET & FORM PLACEHOLDERS

Claude must use these exact HTML snippets when wireframing missing assets or forms.

**Image/Video Placeholder:**
```html
<div class="asset-placeholder" style="width: 100%; height: 100%; min-height: 400px; background-color: #f0f4f8; border: 2px dashed #0054a4; display: flex; align-items: center; justify-content: center; text-align: center; padding: 2rem;">
  <div>
    <span style="display: block; font-weight: bold; color: #0054a4; margin-bottom: 0.5rem;">ASSET REQUIRED</span>
    <span style="color: #4a5568; font-size: 0.875rem;">[Insert description of required asset here]</span>
  </div>
</div>
```

**HubSpot Form Placeholder:**
```html
<div class="hs-form-placeholder" style="background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 2rem; text-align: center;">
  <span style="display: block; font-weight: bold; color: #4a5568; margin-bottom: 0.5rem;">HUBSPOT FORM EMBED</span>
  <span style="color: #718096; font-size: 0.875rem;">Form ID: [Insert ID]</span>
</div>
```

---

## 5. CLAUDE INSTRUCTIONS

When generating a wireframe based on this brief, Claude must:
1.  Output complete, valid HTML5.
2.  Include all necessary CSS classes from the IOR Design System.
3.  Ensure the page is fully responsive (mobile, tablet, desktop).
4.  Not invent copy; use the structure and intent provided in this brief.
5.  Return only the code, ready to be saved as an `.html` file.
