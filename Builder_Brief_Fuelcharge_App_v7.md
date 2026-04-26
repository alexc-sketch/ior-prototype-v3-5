# BUILDER BRIEF: Fuelcharge App (v7.0)

**To:** Development Team
**Page:** Fuelcharge App Landing Page
**Target GitHub URL:** `07b_Fuelcharge_App_v7.html`
**Status:** ❌ CRITICAL REVISION REQUIRED (Missing Assets, Layout Errors & Form Removal)

---

## 💡 AUDITOR NOTE: STRUCTURAL RULES & MISSING ASSETS

**The "Funky B2C SaaS" Vibe:** This page needs to look like a top-tier consumer fintech app (think Cash App or Revolut). High contrast, bold typography (Avenir Next LT Pro), and zero friction.

**NEW RULE - NO FORMS:** There are NO lead-generation forms or gated assets on this page. Do not include any HubSpot forms. The only conversion actions are the App Store and Google Play buttons.

**NEW RULE - Headers:** Absolutely NO GRADIENTS in the hero or section headers. Backgrounds must be solid, full-bleed colours (e.g., solid `#13114D` for the hero).

**NEW RULE - Quick Links:** The Quick Links bar must sit underneath the hero banner, never above it.

**MISSING ASSET CORRECTION:** The previous build failed because it omitted the client's provided app screenshots and YouTube videos. Map the assets exactly as outlined in Section 2 below.

---

## 🎨 1. FUELCHARGE BRAND & UI KIT (Strict Rules)

| Category | Element Name | Value / Specification | Usage Notes |
|---|---|---|---|
| **Typography** | Primary Font Family | Avenir Next LT Pro | Must inherit the new IOR master font (do not use Ubuntu/Inter). |
| **Typography** | Font Weights | 700 (Bold), 400 (Regular) | Use 700 for all Headlines/H1/H2 and buttons. Use 400 for body copy. |
| **Colors** | Primary Dark | `#13114D` | Use for the hero (solid, full-bleed), dark mode sections, and primary text. |
| **Colors** | Fuelcharge Teal | `#00D1CC` | Core brand identifier. Use for icons, active tabs, and UI highlights. |
| **Colors** | Base Neutrals | `#FFFFFF`, `#FCFCED` | Use White for cards and `#FCFCED` for alternating section strips. |
| **Buttons & CTAs** | Primary Conversion | App Store & Google Play | No text buttons for downloads. Use official black SVG badges. |

---

## 🏗️ 2. EXACT COMPONENT & ASSET MAPPING

### 1. Frictionless B2C App Hero
- **Layout:** 50/50 Split. Full-bleed solid background (`#13114D`). No gradients.
- **Left Column:** Hook copy + App Store/Google Play badges + Desktop QR Code.
- **Right Column (Asset Required):** Use `assets/images/fuelcharge/fuelcharge-screen-lytton-hero.png` (The dark blue "You are at - IOR Lytton" screen) as a floating, high-fidelity device mockup.

### 2. Quick Links Bar ("Explore:")
- **Placement:** Immediately below the Hero Banner.
- **Style:** Standard horizontal link bar. (Not sticky).
- **Links Required:** HyDip™ \| Customer Portal

### 3. Scale & Proof Bar
- **Style:** High-contrast metric strip (`#FCFCED` background).
- **Metrics:** 100+ Diesel Stops \| 30+ Airports \| iOS & Android \| $0 Cost.

### 4. Audience Flip Cards (CSS 3D Hover)
- **Layout:** 3-column grid (Vehicles & 4WD \| Aviation \| Marine). CSS flip on hover.

### 5. Interactive Network Map Teaser (Asset Required)
- **Layout:** Full-bleed map visual or overlapping feature block.
- **Visual:** Use `assets/images/fuelcharge/fuelcharge-screen-australia-map.png` (The zoomed-out map of Australia with vehicle pin drops) as the hero visual for this section.

### 6. Easy-as-1-2-3 App Flow (Media Mapping)
- **Layout:** Left side Vertical Tabs, Right side dynamic media container.
- **Tab 1 Media:** Embed the YouTube video: *Introducing Fuelcharge*.
- **Tab 2 Media:** Embed the YouTube video: *How to use the Fuelcharge Payment Terminal*.
- **Tab 3 Media (Asset Required):** Use `assets/images/fuelcharge/fuelcharge-screen-authorize-pump.png` (The "Review your order / Authorize and unlock pump" screen) floating in a device mockup.

### 7. Social Proof
- **Layout:** Blockquote with the Tin Can Bay Marina quote and logo.

### 8. FAQ Accordion & Support Routing
- **Style:** Standard Global FAQ accordion component.
- **Support Routing:** Text block beneath the FAQs directing users to the phone number and email.

---

## 📋 3. GLOBAL COMPONENTS & SHELL RULES

- **Nav & Footer:** Must use the canonical Utility Shell v5 components. Do not apply Fuelcharge branding to the global header or footer.
- **Golden Rules:** `border-radius: 0` on all cards and containers. No inline styles. No operating hours.
- **Reference:** [Global Components Library](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html)
