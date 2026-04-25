# Builder Brief: Utility Shell & Make a Payment (v5.0)

**To:** Development & Design Team  
**From:** UX Audit / Manus AI Builder  
**Date:** April 25, 2026  
**Project:** IOR Prototype v3.5  

---

## 1. Document Metadata & SEO Directives

**STAGING LINK:** [Make a Payment v5](https://alexc-sketch.github.io/ior-prototype-v3-5/11e_Make_Paymentv5.html)  
**GLOBAL COMPONENTS REFERENCE:** [Global Components](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html)  
**FOCUS KEYWORD:** IOR Make a payment  
**SECONDARY KEYWORDS:** Pay fuel account online, secure payment  
**META TITLE:** Make a Payment | IOR  
**META DESCRIPTION:** Pay your IOR fuel account online. Fast, secure, and simple. Access the payment portal here.  

---

## 2. Part 1: Create a Dedicated "Utility Shell" (Prerequisite)

We are establishing a new master template for all functional, task-based pages. This new Utility Shell will be the starting point for pages like Make a Payment, Contact Us, and Policy & Downloads.

**Source File:** Duplicate `IOR_Global_Template_Shell_v4.html` and save it as `IOR_Utility_Template_Shell_v5.html`.

### How to build the Utility Shell:

1. **KEEP:** 
   - The Proto-Bar
   - The Global Header / Mega Menus (sticky)
   - The Mobile Drawer
   - The Pre-Footer ("We're here to help")
   - The Global 6-column Footer

2. **REMOVE:** 
   - Strip out all heavy marketing components from the body.
   - Remove the Full-Bleed Video Hero, the Stat Bar, the Logo Carousel, the 1-2-3 Steps, the large HubSpot Lead Capture block, and the "Latest from IOR" Trust Flow (Blog/Case Study grid).

3. **MODIFY (The Hero):** 
   - Replace the heavy video hero with a Minimal Utility Hero. 
   - It should be a solid `var(--ior-navy)` background container with dynamic slots for an Eyebrow, H1, and Subcopy.

4. **ADD:** 
   - Keep the Global FAQ Routing box ("Still have questions?") at the bottom, just above the Pre-Footer.

By doing this, you now have two perfect starting points: The Global Shell (for heavy marketing & service hubs) and the Utility Shell (for fast, distraction-free functional pages).

---

## 3. Part 2: Make a Payment Page Build

**Target File:** `11e_Make_Paymentv5.html` (Built using the new Utility Shell)

### Page Objective
A strictly utilitarian, frictionless page. The user is here to do one thing: pay their bill. The design must be clean, highly secure-looking, and free of marketing fluff.

### Wireframe Component Flow & Structure

Please build the page using this exact top-to-bottom component flow:

#### 1. Minimal Utility Hero (Inherited from Shell)
- **Style:** Keep it slim and distraction-free using the new Utility Shell hero format.
- **Eyebrow:** SECURE ONLINE PAYMENT
- **H1:** Make a payment.
- **Subcopy:** Pay your IOR fuel account online. Fast, secure, and simple. Have your account and invoice details ready.
- **Primary CTA:** None needed in the hero (the action is directly below).

#### 2. Quick Links Bar ("Explore:")
- **Style:** The standard horizontal link bar from global components.
- **Label:** Explore:
- **Links Required:** 
  1. Contact Us (Links to `/support-contact/contact-us/`)
  2. Help Centre & FAQs (Links to `/support-contact/`)
  3. Regional Contacts (Links to `/support-contact/regional-contacts/`)
  4. Find a Location (Links to `/locations/`)

#### 3. Payment Information & Gateway Links (The Core Interaction)
- **Visual Reference:** Look at `06_Support_and_Utility.html#make-a-payment` for layout inspiration, but strictly follow the asset/exclusion rules below.
- **Header (H2):** Pay via our secure portal.
- **Body Copy:** Access the IOR secure payment gateway to settle your account via credit card. All transactions are encrypted and processed securely.
- **Bullet Points (What you need):**
  - Your IOR Account Number
  - Your Invoice Reference Number
  - A valid Credit or Debit Card
- **The Payment Gateway Buttons:** You must build clear, highly visible routing buttons/cards for the two payment gateways.
  - Use the provided AMEX SVG/PNG paired with the AMEX Payment Link.
  - Use the provided Visa/Mastercard SVG/PNG paired with the Visa/MC Payment Link.
- **Primary CTA (Button):** Proceed to Secure Payment → (Dev Note: Link this to your external Stripe/payment gateway).
- **Alternative Payment Methods:** Include a small accordion or secondary text block below the button.
  - *EFT Details:* "To pay via Electronic Funds Transfer, please refer to the BSB and Account Number printed at the bottom of your IOR invoice."
- **Client Feedback Integration:** The client explicitly stated they liked the "View your invoices in the Customer Portal" component from the previous design. You MUST include this block (e.g., as a secondary card or clean callout box below the payment links) to cross-pollinate traffic to the portal.

#### 🚨 STRICT EXCLUSION RULES
DO NOT include the security text block from the old utility file. Remove the following text completely:
- [Remove] 🔒 256-bit TLS SSL encryption
- [Remove] ✓ PCI DSS Compliant payment gateway
- [Remove] ✓ Card details are never stored by IOR
- [Remove] Powered by [ Payment Gateway Name ]
- [Remove] Operating hours
- [Remove] Rounded corners on image/logo boxes

#### 4. Support Contact CTA
- **Style:** Use a standard split-screen or full-width call-to-action block.
- **Header (H2):** Need help with your account?
- **Copy:** If you have questions regarding your invoice, require a copy of a past statement, or need to update your direct debit details, our local accounts team is ready to assist.
- **Buttons:** 
  - Primary Button: Call Accounts: 1300 457 467
  - Secondary Button (btn--outline): Email Accounts Team (Links to `accounts@ior.com.au`)

#### 5. "Still Have Questions?" Block (Inherited from Shell)
- **Header (H4):** Still have questions?
- **Copy:** Submit an enquiry to our local team or search our full knowledge base.
- **Buttons:** Browse Help Centre | Ask us here →

#### 6. Global Footer (Inherited from Shell)
- **Style:** The standard v4.0 6-column global footer closes out the page.

---

## 4. Designer Notes (Elementor Build Strategy)

- **Trust Factors:** Because this is a payment page, ensure the design feels airtight. Use exact spacing, strict alignments, and subtle borders.
- **Icons:** Use recognizable, trustworthy icons (e.g., a subtle lock icon next to the "Proceed to Secure Payment" button).
- **Distraction-Free:** Keep the content strictly to the point. Do not add related blog posts or marketing cross-sells to this page.
- **Navigation:** All pages derived from a shell file must always use the navigation (utility bar and main navigation) and footer components provided in the shell file. The shell file should be considered the definitive template for these elements.

---

## 5. Asset Checklist for Builder

Please ensure you have downloaded and are referencing the following files provided for this ticket:
- [x] Design HTML & SVGs
- [x] Design PDF
- [x] AMEX PNG & SVG + AMEX Link
- [x] Visa/Mastercard PNG & SVG + Visa/MC Link
- [x] Base Template to Duplicate/Use: `IOR_Utility_Template_Shell_v5.html`
