# BUILDER BRIEF: Fuelcharge App (v8.0)

**To:** Development Team
**Page:** Fuelcharge App Landing Page
**Target GitHub URL:** `07b_Fuelcharge_App_v8.html`
**Status:** ❌ CRITICAL REVISION REQUIRED (Missing Assets, Layout Errors & Form Removal)

---

## ⚙️ SEO & META DATA
**Meta Title:** Fuelcharge — Pay for Fuel Faster at 100+ IOR Sites | IOR
**Meta Description:** Fuelcharge is IOR's mobile app for cashless fuel access. No credit application. Download, register a card, and refuel at 100+ IOR sites — 24/7.

---

## 💡 AUDITOR NOTE: STRUCTURAL RULES & FRICTIONLESS UX

**The "Funky B2C SaaS" Vibe:** This page needs to look like a top-tier consumer fintech app (think Cash App or Revolut). High contrast, bold typography (Avenir Next LT Pro), and zero friction.

**NEW RULE - NO FORMS:** There are NO lead-generation forms or gated assets on this page. The only conversion actions are the App Store and Google Play buttons.

**NEW RULE - Headers:** Absolutely NO GRADIENTS in the hero or section headers. Backgrounds must be solid, full-bleed colours (e.g., solid `#13114D` for the hero).

**NEW RULE - Quick Links:** The Quick Links bar must sit underneath the hero banner, never above it.

**NEW RULE - Killed the Stat Bar:** Do not build a 4-column stat bar. The stats have been integrated contextually into the Hero and Map sections to improve page flow.

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
- **Headline (H1):** Fuel. Scan. Pay. Done.
- **Subcopy:** The ultimate pay-at-the-pump app. No credit application or account setup required. Download Fuelcharge, register a card, and refuel at our national network — 24/7, even in the most remote locations.
- **CTAs:** [App Store Badge] \| [Google Play Badge]
- **Desktop QR Label:** Scan to Download
- **Microcopy (Below Badges):** 100% free to download on iOS & Android.
- **Right Column (Asset Required):** Use `assets/images/fuelcharge/fuelcharge-screen-lytton-hero.png` (The dark blue "You are at - IOR Lytton" screen) as a floating, high-fidelity device mockup.

### 2. Quick Links Bar ("Explore:")
- **Placement:** Immediately below the Hero Banner.
- **Style:** Standard horizontal link bar. (Not sticky).
- **Links Required:** HyDip™ \| Customer Portal

### 3. Audience Flip Cards (CSS 3D Hover)
- **Layout:** 3-column grid. CSS flip on hover. `border-radius: 0` on all cards.
- **Card 1 (Vehicles & 4WD):**
  - *Front:* Vehicles & 4WD
  - *Back:* Pay for fuel faster and continue your adventure. All major caravan routes covered.
- **Card 2 (Aviation):**
  - *Front:* Aviation
  - *Back:* Pay for fuel faster and spend more time in the air. Simply select your pump and pre-authorise from your smart device.
- **Card 3 (Marine):**
  - *Front:* Marine
  - *Back:* A better solution for refuelling your vessel. Authorise marine fuel from your phone, eliminating the need to carry physical cards or cash to the dock.

### 4. Interactive Network Map Teaser (Asset Required)
- **Layout:** Full-bleed map visual or overlapping feature block.
- **Headline:** Find fuel wherever the journey takes you.
- **Body:** Access over 100+ diesel stops and 30+ airports nation-wide. Use the in-app locator to find your nearest location, check live amenity availability, and get directions right to the bowser.
- **Button:** Explore the Network Map → (Links to `11d_Find_Locationv5.html`)
- **Visual:** Use `assets/images/fuelcharge/fuelcharge-screen-australia-map.png` (The zoomed-out map of Australia with vehicle pin drops) as the hero visual for this section.

### 5. Easy-as-1-2-3 App Flow (Media Mapping)
- **Layout:** Left side Vertical Tabs, Right side dynamic media container.
- **Section Header:** Three steps to pay for fuel.
- **Tab 1 (Download & Scan):**
  - *Header:* 1. Scan the QR Code
  - *Body:* Pull up to the pump. Open Fuelcharge on your phone and scan the QR code located directly on the bowser.
  - *Media:* Embed the YouTube video: *Introducing Fuelcharge*.
- **Tab 2 (Select Fuel):**
  - *Header:* 2. Select Your Pump
  - *Body:* Choose your pump number and fuel type. Looking to top up? Simply select a pre-authorised amount above what your tank holds. You won't be charged for fuel you don't receive.
  - *Media:* Embed the YouTube video: *How to use the Fuelcharge Payment Terminal*.
- **Tab 3 (Pay & Go):**
  - *Header:* 3. Pay & Go
  - *Body:* Authorise payment in the app. Your receipt is sent instantly to your phone and email.
  - *Media (Asset Required):* Use `assets/images/fuelcharge/fuelcharge-screen-authorize-pump.png` (The "Review your order / Authorize and unlock pump" screen) floating in a device mockup.

### 6. Social Proof
- **Layout:** Blockquote with the Tin Can Bay Marina quote and logo.
- **Quote:** "I drive past the fuel dock on my day off and see customers using Fuelcharge to pay online. I can see the transactions and know that I'm making money even when the site is unmanned."
- **Attribution:** Chris Rippon - Proprietor, Tin Can Bay Marina

### 7. Frequently Asked Questions & Support
- **Style:** Standard Global FAQ accordion component.
- **Section Header:** Frequently asked questions
- **Q1:** Do I need an IOR account to use Fuelcharge?
  - *A:* No. Fuelcharge works without an IOR account — pay via credit/debit card as a casual user. For fleet operators, connect Fuelcharge to an IOR account for consolidated billing, driver controls, and HyDip™ integration.
- **Q2:** Where can I download my tax receipts?
  - *A:* All receipts are stored in the Fuelcharge app under Transaction History. You can email individual receipts or export a CSV of all transactions for a selected date range directly from the app.
- **Q3:** Is Fuelcharge available at all IOR Aviation locations?
  - *A:* Fuelcharge is available at a growing number of IOR Aviation sites. Use the in-app map or the Find a Location page on our website to check which sites are Fuelcharge-enabled before your flight.
- **Q4:** What payment methods does Fuelcharge accept?
  - *A:* Fuelcharge accepts Visa, Mastercard, American Express, and Apple Pay/Google Pay. IOR fleet account holders can also charge transactions directly to their account for consolidated monthly billing.
- **Q5:** How do I set driver spend limits for my fleet?
  - *A:* Fleet managers can set per-driver, per-day, or per-fill spend limits directly from the Fuelcharge Fleet Dashboard online. Limits take effect immediately and can be adjusted at any time.
- **Support Routing:** Need assistance? Call our support team directly on 1800 414 012 or contact us at enquiries@ior.com.au

---

## 📋 3. GLOBAL COMPONENTS & SHELL RULES

- **Nav & Footer:** Must use the canonical Utility Shell v5 components. Do not apply Fuelcharge branding to the global header or footer.
- **Golden Rules:** `border-radius: 0` on all cards and containers. No inline styles. No operating hours.
- **Reference:** [Global Components Library](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html)

---

## 🔧 4. ELEMENTOR AGENCY HANDOFF NOTES

These items are prototype placeholders in the HTML build. Each must be replaced before go-live in Elementor.

| Item | Prototype State | Elementor Action Required |
|---|---|---|
| **YouTube — Tab 1** | Placeholder ID `VIDEO_ID_1` | Replace with the real YouTube video ID for *Introducing Fuelcharge* |
| **YouTube — Tab 2** | Placeholder ID `VIDEO_ID_2` | Replace with the real YouTube video ID for *How to use the Fuelcharge Payment Terminal* |
| **QR Code** | Inline SVG placeholder pattern | Replace with a real scannable Fuelcharge download QR code — use the Elementor QR Code widget or an ACF image field |
| **App Store link** | `href="#"` | Replace with the real iOS App Store URL for Fuelcharge |
| **Google Play link** | `href="#"` | Replace with the real Google Play Store URL for Fuelcharge |
| **Flip Cards** | CSS 3D `perspective` / `rotateY` hover | Implement using the Elementor **Flip Box** widget. Override `border-radius` to `0` in the widget Advanced CSS. Do not use the default rounded style. |
| **Fuelcharge branding boundary** | `#13114D` and `#00D1CC` applied to page body sections only | Global nav (utility bar, primary nav, mobile drawer) and footer must remain canonical IOR colours — do not apply Fuelcharge brand colours to these components |
