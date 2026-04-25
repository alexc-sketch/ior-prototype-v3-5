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

## 📄 Page Structure (7 Sections)

### 1. Quick Links Bar
- **Label:** Explore:
- **Links:**
  1. HyDip FMS (anchors to `#hydip`)
  2. Fuelcharge (anchors to `#fuelcharge`)
  3. Customer Portal (anchors to `#portal`)
  4. Support & Contact (links to `11_Support_Hubv5.html`)
- **Note:** This bar is NOT sticky.

### 2. SaaS Product-Led Hero
- **Background:** `var(--ior-navy)` solid (no gradient, no overlay).
- **Layout:** 50/50 split.
- **Left Column (Copy):**
  - **Eyebrow:** DIGITAL PLATFORMS
  - **H1:** Your fleet. Your fuel. Fully connected.
  - **Subcopy:** IOR’s proprietary technology ecosystem gives you complete visibility and control over every drop of fuel, from the terminal to the tank.
  - **CTA 1 (Primary):** Explore HyDip FMS (anchors to `#hydip`)
  - **CTA 2 (Outline):** View Customer Portal (anchors to `#portal`)
- **Right Column (Imagery):**
  - Device mockups showing the HyDip tablet interface and the Customer Portal mobile view.

### 3. Two Platforms Flip Cards (HyDip & Portal)
- **Layout:** 2-column grid of interactive CSS 3D flip cards.
- **Card A: HyDip FMS**
  - **Front:** Dark navy background, teal accent. Logo/Title: HyDip FMS. Subtitle: Hardware & Software Integration.
  - **Back (on hover):** Feature list (Live tank gauging, automated FTC claims, per-asset tracking).
  - **CTA:** Learn More →
- **Card B: Customer Portal**
  - **Front:** Dark navy background, gold accent. Logo/Title: IOR Customer Portal. Subtitle: Account & Invoice Management.
  - **Back (on hover):** Feature list (Consolidated invoicing, card management, price notifications).
  - **CTA:** Learn More →

### 4. Fuelcharge B2C Callout
- **Background:** Dark band (`#1A1A2E`).
- **Branding:** Fuelcharge orange (`#FF6B2B`) accents.
- **Content:**
  - **Badge:** No account required
  - **Title:** Pay at the pump with Fuelcharge.
  - **Subcopy:** Download the app to unlock pumps and pay securely at any IOR diesel stop.
- **CTAs:** App Store ↓ | Google Play ↓

### 5. Trust & Support
- **Layout:** 2-column split.
- **Left (Testimonial):**
  - **Quote:** "The integration between HyDip and our accounting software has saved our admin team 15 hours a week in manual data entry."
  - **Attribution:** Tin Can Bay Marina
- **Right (Routing Card):**
  - **Title:** Need technical support?
  - **Subcopy:** Our in-house development and support teams are based in Brisbane and ready to help.
  - **CTA:** Visit Help Centre → (links to `11_Support_Hubv5.html`)

### 6. FAQ Accordion
- **Functionality:** Standard accessible accordion (`aria-expanded`).
- **Questions:**
  1. Do I need a fleet account to use Fuelcharge?
  2. Does HyDip integrate with Xero and MYOB?
  3. How do I order replacement fuel tags?
  4. Can I set budget alerts in the Customer Portal?
  5. Is the Customer Portal available on mobile?
  6. How do I export my Fuel Tax Credit reports?

### 7. Related Content Grid
- **Eyebrow:** LATEST FROM IOR
- **Layout:** 3-column card grid.
- **Content:** Mix of Case Studies and Blog Posts related to technology and fleet management.

---

## 📝 Auditor Notes
- The builder must ensure the hero section strictly adheres to the `var(--ior-navy)` solid background rule (no gradients or image overlays).
- The flip cards in Section 3 must use CSS transforms, not JS, for performance and accessibility.
- The Fuelcharge section (Section 4) is the only area permitted to use the `#1A1A2E` and `#FF6B2B` brand colours.
- All CTAs must use sharp geometry (`border-radius: 0`) unless explicitly using the `.btn--pill` class.
