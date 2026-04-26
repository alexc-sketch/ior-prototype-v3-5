# BUILDER BRIEF: Customer Portal

**Target File:** `07c_Customer_Portal_v8.html`
**Replaces:** `07c_Customer_Portalv5.html`
**Vibe:** Enterprise SaaS. Clean, authoritative, data-driven.

## GLOBAL BUILD RULES (ZERO-ERROR MANDATE)
1. **Shell File:** Must be built fresh from `https://alexc-sketch.github.io/ior-prototype-v3-5/IOR_Global_Template_Shell_v4.html`. DO NOT duplicate or patch existing v3.5 or v5 HTML files.
2. **Global Components:** Reference `https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html`.
3. **No Gradients:** Backgrounds must be solid, full-bleed colours.
4. **Quick Links:** Must sit immediately below the hero banner. It is never sticky.
5. **Sharp Geometry:** `border-radius: 0` on all cards, buttons, and containers. No rounded corners.
6. **Colour Scope:** Bespoke brand colours apply to page content only. Do not alter nav, footer, or global component colours.
7. **Untouchable Files:** Do NOT modify `ior-global.css`, `ior-global.js`, `ior-motion.js`, or `IOR_Design_System.html`. Do not alter navigation structure, footer structure, or any existing component class names.

## SEO & META DATA
* **STAGING LINK:** `https://alexc-sketch.github.io/ior-prototype-v3-5/07c_Customer_Portal_v8.html`
* **FOCUS KEYWORD:** Fleet fuel management
* **SECONDARY KEYWORDS:** B2B fuel account management, enterprise fuel portal
* **META TITLE:** IOR Customer Portal — Real-Time Fuel Visibility & Control | IOR
* **META DESCRIPTION:** Every IOR account includes Customer Portal access. Real-time fuel dips, tag management, stock history, and fraud prevention. Login, apply, or request access today.
* **PERSONA:** Fleet Managers / Finance Directors / Operations Managers / Business Owners

## BRAND TONE OF VOICE
Professional, innovative, reliable, and 'adult'. Grounded, Australian, and community-focused.

## CRITICAL BUILD RULES (Portal-Specific)
* **MODAL RULE:** The 'Request Access' HubSpot form must be a pop-up modal, NOT an inline section. Delete the inline form block from the HTML. Attach modal trigger to all 'Request Access' CTAs.
* **BENTO BOX RULE:** The features section must be a 2x2 CSS Grid (Stripe/Apple style). Delete the tabbed layout from v3.5. Use `horizontal.png` and `Mobile.png` bleeding off card edges.

## COMPONENT FLOW

### Section 1 — SaaS Hero
* **Layout:** 50/50 Split (or asymmetrical 40/60). Solid, full-bleed background. No gradients.
* **Eyebrow:** IOR CUSTOMER PORTAL
* **H1:** Powerful fuel management, without the complexity.
* **Subcopy:** The IOR Customer Portal gives you complete control over your fuel — from security and compliance to budgeting and forecasting. Advanced fleet management that is fast, simple, and included out-of-the-box for all IOR account holders.
* **CTA 1:** Log in to Portal → (External Link — Primary)
* **CTA 2:** Request Access (Secondary — Triggers Pop-up Modal)
* **Visual:** `CP - Website.jpg` (the overlapping Tablet and iPhone mockup). This is a client-provided asset.

### Section 2 — Quick Links Bar
* **Placement:** Immediately below the hero. Not sticky.
* **Links:** HyDip™ | Customer Portal

### Section 3 — The 2x2 Feature Quadrant (Bento Box)
* **Layout:** 2x2 CSS Grid (`grid-template-columns: 1fr 1fr`). Inspired by Stripe.com feature grids.
* **Card 1:** Total network visibility. | Track your bulk fuel deliveries as they happen. Integrate with your HyDip™ FMS to see real-time dips and usage directly from your bulk tank, giving you full visibility and control over what was delivered versus what was pumped. | **Visual Asset:** `horizontal.png` — bleed off top-right edge of card.
* **Card 2:** Mitigate fraud instantly. | Multiple security layers mean only authorised users access your fuel. Add, suspend, or cancel RFID fuel tags in real time, adding instant protection against unauthorised use or theft. | **Visual Asset:** `Mobile.png` — bleed off bottom-right edge of card.
* **Card 3:** Understand your consumption. | Generate granular reports on all transactions. Understand exactly how much fuel is being consumed between top-ups, broken down per vehicle, per driver, or per site. | **Visual Asset:** UI snippet — cropped dashboard report view.
* **Card 4:** Smarter budgeting. | Access live terminal gate pricing, download tax-compliant invoices instantly, and utilise your historical consumption data for accurate fuel cost forecasting. | **Visual Asset:** UI snippet — invoice download screen.

### Section 4 — Three-Path Access Block
* **Path 1 — Existing User:** Already have a login? | Access your dashboard to manage deliveries, tags, and invoices instantly. | **CTA:** Log in Now (External Link)
* **Path 2 — Unregistered User:** IOR customer without a login? | Submit a request and our team will activate your portal credentials within 1 business day. | **CTA:** Request Access (Triggers Modal)
* **Path 3 — New to IOR:** Don't have an IOR account? | Apply for an IOR account today and get instant portal access upon approval. | **CTA:** Apply Now → `iorapp.applyeasy.com.au/services/introduction`

### Section 5 — HubSpot Modal (Hidden)
* **Trigger:** All 'Request Access' buttons throughout the page.
* **Headline:** Request Portal Access
* **Body:** Submit your details below. Our Customer Service Team will link your profile and email your login credentials within 1 business day.
* **Form Fields:** Company Name | First Name | Last Name | Email
* **Note:** This form triggers an automated email sequence. Confirm HubSpot form ID with client before build.

### Section 6 — Social Proof
* **Quote:** The real-time visibility we get through the IOR Portal has completely changed how we manage our fleet. We can track consumption down to the litre and suspend lost tags instantly, saving us thousands in potential theft.
* **Attribution:** (Awaiting final client testimonial — leave as placeholder)

### Section 7 — FAQ Accordion
* **Q1:** Can I access fuel transaction reporting in the portal? | **A:** Yes. You can generate and export granular reports on all fuel transactions, breaking down consumption by vehicle, driver, or site.
* **Q2:** Is the portal designed for account-based customers? | **A:** Yes, the IOR Customer Portal is an out-of-the-box solution included for all account-based customers, giving you full control over your fuel and fleet.
* **Q3:** Can I manage invoices or account details in the portal? | **A:** Absolutely. You can download current and historical tax-compliant invoices, view live pricing, and update your account details directly within the dashboard.
* **Q4:** How does the customer portal connect with IOR's digital platforms? | **A:** The Customer Portal acts as your central hub. It seamlessly integrates with platforms like HyDip™ FMS, allowing you to view real-time tank dips and usage data alongside your standard network transactions.
* **Q5:** Where do I go if I need help with the customer portal? | **A:** If you need assistance, you can visit our Help Centre for detailed guides or contact our Customer Service team on 1300 457 467.

### Section 8 — Related Content Grid
* **Layout:** Standard 3-card global component.
* **Content:** Pull Case Studies and Blog Posts relevant to fleet management and portal features.
