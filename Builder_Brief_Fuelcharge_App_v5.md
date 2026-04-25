# Builder Brief: Fuelcharge App v5

**Target File:** `07b_Fuelcharge_App_v5.html`
**Base Template:** `IOR_Global_Template_Shell_v4.html` (for global components)
**Status:** In Brief

---

## ⚙️ Content Collation & SEO

- **STAGING LINK:** https://alexc-sketch.github.io/ior-prototype-v3-5/07b_Fuelcharge_App_v5.html
- **FOCUS KEYWORD:** Fuelcharge australia
- **SECONDARY KEYWORDS:** Fuelcharge app, fleet fuel card, cardless fleet fuel payment, pay at pump app Australia
- **META TITLE:** Fuelcharge — Pay for Fuel Faster at 115+ IOR Sites | IOR
- **META DESCRIPTION:** Fuelcharge is IOR's mobile app for cashless fuel access. No credit application. Download, register a card, and refuel at 115+ IOR sites — 24/7, even in remote locations.

---

## 📦 Asset Manifest

All required assets have been saved to the repository. The builder must use these exact files:

**Layout & Component References:**
- `assets/images/fuelcharge/fuelcharge-layout-reference-1.png` (Section layout guide)
- `assets/images/fuelcharge/fuelcharge-layout-reference-2.png` (Section layout guide)
- `assets/images/fuelcharge/fuelcharge-stats-reference.webp` (Stats bar reference)

**UI Assets:**
- `assets/images/fuelcharge/fuelcharge-hero-mockup.webp` (Hero device mockup)
- `assets/images/fuelcharge/fuelcharge-app-screen-location.png` (App screen: Location)
- `assets/images/fuelcharge/fuelcharge-app-screen-payment.png` (App screen: Payment)
- `assets/images/fuelcharge/fuelcharge-app-screen-map.png` (App screen: Map)
- `assets/images/fuelcharge/fuelcharge-ui-screen-1.svg` (UI vector 1)
- `assets/images/fuelcharge/fuelcharge-ui-screen-2.svg` (UI vector 2)
- `assets/images/fuelcharge/fuelcharge-ui-screen-3.svg` (UI vector 3)
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

## 🎨 Brand & UI Kit (The "Funky B2C SaaS" Strategy)

This page needs to look like a top-tier consumer fintech app (high contrast, zero friction).

- **Typography:** Avenir Next LT Pro (700 for headlines/buttons, 400 for body). Must inherit the new IOR master font.
- **Primary Dark (Background):** `#13114D` (Use for dark mode sections).
- **Fuelcharge Teal (Accent):** `#00D1CC` (Use for icons, active tabs, numbers, UI highlights).
- **Action Blue:** `#0355A3` (Use for standard secondary buttons/links).
- **Base Neutrals:** `#FFFFFF` (White) and `#FCFCED` (Off-White for alternating strips).
- **Primary Conversion:** App Store & Google Play Badges ONLY. Never use text buttons for app downloads.
- **QR Code:** Place a scannable QR code next to the App Store badges on Desktop views.

---

## 📄 Page Structure (9 Sections)

### 1. Quick Links Bar
- **Label:** Explore:
- **Links:** HyDip™ | Customer Portal
- **Note:** Standard horizontal link bar. Not sticky.

### 2. Frictionless B2C App Hero
- **Layout:** 50/50 Split.
- **Left Column (The Hook):**
  - **H1:** Fuel. Scan. Pay. Done.
  - **Subcopy:** The ultimate pay-at-the-pump app. No credit application or account setup required. Download Fuelcharge, register a card, and refuel at 115+ IOR sites — 24/7, even in the most remote locations.
  - **CTAs:** [App Store Badge] | [Google Play Badge]
  - **QR Code Label:** Scan to Download
- **Right Column (The Product):**
  - High-res mockup of an iPhone angled slightly (`fuelcharge-hero-mockup.webp`).

### 3. Scale & Proof Bar
- **Style:** High-contrast metric strip (`#FCFCED` background).
- **Metrics:**
  - 115+ | IOR network stops
  - 24/7 | Unmanned Access
  - iOS & Android | Free download
  - $0 | Cost to download & use

### 4. Audience Flip Cards
- **Layout:** 3-column grid (`grid-template-columns: 1fr 1fr 1fr`).
- **Interaction:** CSS 3D Flip effect on mouse hover.
- **Card 1 (Vehicles):**
  - **Front:** Vehicles & 4WD
  - **Back:** Don’t get stuck without access to fuel. Arrive in remote locations at any time of day or night and refuel securely at participating diesel stops. No paper receipts. No credit card machines.
- **Card 2 (Aircraft):**
  - **Front:** Aviation
  - **Back:** Save time refuelling by authorising the bowser from the cockpit. Hang up the nozzle and your transaction is stored immediately against your profile. Access our growing GA network 24/7.
- **Card 3 (Boats):**
  - **Front:** Marine
  - **Back:** A better solution for refuelling your vessel. Authorise marine fuel from your phone, eliminating the need to carry physical cards or cash to the dock.

### 5. Network Map Teaser
- **Headline:** Find fuel wherever the journey takes you.
- **Body:** Use the in-app locator to find your nearest diesel stop or airport, check live amenity availability, and get directions.
- **Button:** Explore the Network Map → (Links to `11d_Find_Locationv5.html`)

### 6. Easy-as-1-2-3 App Flow
- **Layout:** Split section. Left side: Vertical Tabbed Accordion. Right side: YouTube video embeds.
- **Section Header:** Three steps to pay for fuel.
- **Tab 1: Download & Scan**
  - **Header:** 1. Scan the QR Code
  - **Body:** Pull up to the pump. Open Fuelcharge on your phone. Scan the QR code on the bowser.
  - **Media:** Embed "Introducing Fuelcharge" video.
- **Tab 2: Select Fuel**
  - **Header:** 2. Select Your Pump
  - **Body:** Choose your pump number and fuel type. Fill up as much as you need — fill the tank or set a specific dollar amount.
  - **Media:** Embed "How to use the Fuelcharge Payment Terminal" video.
- **Tab 3: Pay & Fill Up**
  - **Header:** 3. Pay & Go
  - **Body:** Authorise payment in the app via credit card or IOR fleet account. Your receipt is sent instantly to your phone and email.

### 7. Social Proof
- **Layout:** Blockquote with the Tin Can Bay Marina logo.
- **Quote:** "I drive past the fuel dock on my day off and see customers using Fuelcharge to pay online. I can see the transactions and know that I'm making money even when the site is unmanned."
- **Attribution:** Chris Rippon, Proprietor, Tin Can Bay Marina

### 8. The "Fleet Trap" (B2B Setup Guide)
- **Style:** Dark mode block (`#13114D`) at the bottom of the page.
- **Eyebrow:** FOR FLEET MANAGERS
- **Headline:** Download the Fuelcharge Fleet Setup Guide.
- **Body:** Want to connect Fuelcharge to your IOR fleet account? Download our guide to learn how to add drivers, set spend limits, connect HyDip™ FMS, and activate consolidated billing within 24 hours.
- **Form Action:** Triggers HubSpot form to download PDF.

### 9. Frequently Asked Questions
- **Style:** Standard Global FAQ accordion component.
- **Section Header:** Frequently asked questions
- **Support Routing:** Still need help? Email our support team at info@fuelcharge.com.au.

---

## 📝 Auditor Notes
- **The Golden Rule:** The primary conversion action is downloading the app. There must be no lead-generation forms above the fold.
- **The Fleet Trap:** The "Download Fleet Setup Guide" form is strictly for B2B Fleet Managers and must remain at the bottom of the page (Section 8) so it doesn’t interrupt the retail user's download journey.
- **Branding:** The bespoke Fuelcharge branding (`#13114D` and `#00D1CC`) applies ONLY to the page body. The global navigation and footer must remain canonical IOR branding.
- **Geometry:** All containers and cards must use sharp geometry (`border-radius: 0`). The rounded corners shown in the layout reference images are **not permitted**.
