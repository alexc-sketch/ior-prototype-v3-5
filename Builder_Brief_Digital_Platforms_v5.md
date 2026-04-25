# Builder Brief: Digital Platforms Hub v5

**Target File:** `07_Digital_Platformsv5.html`
**Base Template:** `IOR_Global_Template_Shell_v4.html` (for global components)
**Status:** In Brief

---

## ⚙️ Content Collation & SEO

- **STAGING LINK:** https://alexc-sketch.github.io/ior-prototype-v3-5/07_Digital_Platformsv5.html
- **FOCUS KEYWORD:** IOR Digital Platforms
- **SECONDARY KEYWORDS:** HyDip FMS, Fuelcharge app, IOR Customer Portal, fleet fuel management
- **META TITLE:** Digital Platforms | HyDip, Fuelcharge & Customer Portal | IOR
- **META DESCRIPTION:** Manage your fleet fuel with IOR's integrated digital platforms. Explore HyDip FMS, the Fuelcharge app, and the IOR Customer Portal.

---

## 📦 Asset Manifest

All required assets have been saved to the repository. The builder must use these exact files:

**Layout Reference:**
- `assets/images/digital-platforms/digital-platforms-layout-reference.webp` (Full page layout guide)

**Component References:**
- `assets/images/digital-platforms/stats-bar-reference.png` (Stats bar layout guide)
- `assets/images/digital-platforms/bento-grid-reference.png` (Bento grid layout guide)

**UI Assets:**
- `assets/images/digital-platforms/customer-portal-ui.webp` (Customer Portal interface)
- `assets/images/digital-platforms/fuelcharge-app-location.png` (Fuelcharge app screen 1)
- `assets/images/digital-platforms/fuelcharge-app-payment.png` (Fuelcharge app screen 2)
- `assets/images/digital-platforms/fuelcharge-app-map.png` (Fuelcharge app screen 3)
- `assets/icons/fuelcharge-logo.svg` (Fuelcharge vector logo)

---

## 🏗️ Global Components & Rules

1. **Navigation & Footer:** MUST use the exact canonical utility bar, primary nav, mobile drawer, and 6-column footer from `11a_Contact_Usv5.html`. Do not alter these global elements.
2. **Golden Rules Apply:**
   - Sharp geometry only (`border-radius: 0` on all containers/buttons except `.btn--pill`).
   - No gradients (solid colours only).
   - No inline styles.
   - No operating hours in footer.
   - Word "depot" is not permitted.
3. **Global Reference:** https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html

---

## 📄 Page Structure (Based on Layout Reference)

### 1. Hero Section
- **Background:** `var(--ior-navy)` solid (no gradient, no overlay).
- **H1:** Smarter Fuel Management. End-to-End.
- **Subcopy:** IOR's digital ecosystem connects fuel management, fleet card payments, and account visibility into a single integrated platform — purpose-built for Australia's most demanding operators.
- **CTAs:** Explore HyDip™ FMS (Primary) | Fuelcharge App (Outline)
- **Visual:** Use the network node graphic from the layout reference as a background element.

### 2. Three Platforms Grid
- **Eyebrow:** OUR DIGITAL PLATFORMS
- **H2:** Three Platforms. One Connected Ecosystem.
- **Layout:** 3-column card grid.
- **Card 1 (HyDip):**
  - **Title:** Fuel Management System
  - **Copy:** Complete fuel management — per-asset tracking, automated FTC claims, Xero/MYOB integration, and real-time fleet dashboards. Purpose-built for Australian operators.
  - **Bullets:** Asset-level fuel tracking | Automated FTC claim generation | Accounting software integration
  - **CTA:** Explore HyDip™ →
- **Card 2 (Fuelcharge):**
  - **Title:** Mobile Fleet Card & Payment App
  - **Copy:** Scan-and-pay at any IOR Diesel Network stop — no account required. Full fleet card management, real-time spend tracking, and driver-level controls in your pocket.
  - **Bullets:** QR scan-and-pay at IOR stops | Fleet card management | iOS & Android
  - **CTA:** Explore Fuelcharge →
- **Card 3 (Customer Portal):**
  - **Title:** Account Self-Service Portal
  - **Copy:** Access invoices, account history, statements, and delivery documentation 24/7. Lodge enquiries, update contacts, and manage account users — all in one secure place.
  - **Bullets:** Invoices & statements | Delivery documentation | 4/7 self-service access
  - **CTA:** Explore Portal →

### 3. Seamless Integration Section
- **Layout:** 50/50 split.
- **Left Column (Visual):** Use the "Fleet Data Layer" diagram from the layout reference.
- **Right Column (Copy):**
  - **Eyebrow:** SEAMLESS INTEGRATION
  - **H2:** One Login. Full Fleet Visibility.
  - **Copy:** HyDip™, Fuelcharge, and the Customer Portal all share IOR's unified data layer. A refuel event at an IOR diesel stop via Fuelcharge automatically appears in HyDip™ dashboards, triggers FTC claims, and posts to the Portal — with zero manual entry.
  - **Bullets:** Refuel via Fuelcharge → auto-posted to HyDip™ FMS | HyDip™ delivery data → automatic invoice in Customer Portal | FTC calculations run automatically — no spreadsheets | Xero, MYOB, and SAP export from a single report screen

### 4. Stats Bar / Bento Grid (Optional/Reference)
- The builder should incorporate the design patterns from `stats-bar-reference.png` and `bento-grid-reference.png` to display key platform metrics or features, ensuring sharp geometry (`border-radius: 0`) is maintained.

### 5. Related Content Grid
- **Eyebrow:** LATEST FROM IOR
- **H2:** Innovations and insights from the team keeping Australia moving
- **Tabs:** All Case Studies | Blog Posts
- **Layout:** 3-column card grid.
- **Cards:**
  1. IOR White Sands NOW OPEN!
  2. IOR Aviation Lands in Camden!
  3. Stewart Morland Takes Top Prize at Surat Basin Energy Awards
- **CTA:** View all blog posts →

---

## 📝 Auditor Notes
- The builder must ensure the hero section strictly adheres to the `var(--ior-navy)` solid background rule (no gradients or image overlays).
- The 3-column platform cards must use sharp geometry (`border-radius: 0`). The rounded corners shown in the layout reference PDF are **not permitted** under the Golden Rules.
- All CTAs must use sharp geometry (`border-radius: 0`) unless explicitly using the `.btn--pill` class.
- The builder must use the exact canonical nav and footer from `11a_Contact_Usv5.html`.
