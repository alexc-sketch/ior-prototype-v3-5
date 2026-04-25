# Builder Brief: Contact Us (v5.0)

**To:** Development & Design Team  
**From:** UX Audit / Manus AI Builder  
**Date:** April 25, 2026  
**Project:** IOR Prototype v3.5  

---

## 1. Document Metadata & SEO Directives

**STAGING LINK:** `11a_Contact_Usv5.html` (To be built)  
**GLOBAL COMPONENTS REFERENCE:** [Global Components](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html)  
**FOCUS KEYWORD:** Contact IOR  
**SECONDARY KEYWORDS:** Fuel company contact Australia, commercial enquiries  
**META TITLE:** Contact IOR | 1300 457 467 | IOR  
**META DESCRIPTION:** Contact IOR for fuel supply, account enquiries, support, and careers. Phone: 1300 457 467. Email: enquiries@ior.com.au. Locally-based 24/7 team.  

---

## 2. The Build Strategy (Using the Utility Shell)

Please build this page using the new `IOR_Utility_Template_Shell_v5.html` as the foundation.

- **KEEP:** The Global Header, Proto-Bar, Mobile Drawer, and 6-column Footer must remain intact.
- **REMOVE:** Because this is the Contact page, remove the "Still have questions?" global routing box from the bottom.
- **REPLACE:** Replace the removed routing box with a full-width callout routing users to the Regional Contacts page instead.

---

## 3. Wireframe Component Flow & Structure

Please ensure the build matches this exact top-to-bottom component flow and linking logic:

### 1. Minimal Utility Hero (Inherited from Utility Shell)
- **Style:** Solid brand color (`var(--ior-navy)`). No heavy videos.
- **Eyebrow:** GET IN TOUCH
- **H1:** Contact Us.
- **Subcopy:** For general enquiries, account questions, delivery information, or anything else — our local team responds within one business day.
- **CTAs (2 Buttons):** 
  - Primary Button: 📞 1300 457 467 (Link: `tel:1300457467`)
  - Outline White Button: Send a Message (Anchor Link: `#zendesk-form`)

### 2. Quick Links Bar ("Explore:")
- **Style:** The standard sticky horizontal link bar.
- **Label:** Explore:
- **Links Required:** 
  1. Help Centre & FAQs
  2. Regional Contacts
  3. Make a Payment
  4. Find a Location

### 3. Two-Column Contact Section (The Core Interaction)
- **Visual Reference:** Look at `06_Support_and_Utility.html#contact-us`. This must be a clean split-screen grid (`grid-template-columns: 1fr 1.5fr`).

**Left Column (HQ & Contact Info):**
- **Section Header:** Get in Touch
- **Phone Element:** 1300 457 467 | Mon–Fri · 7am–5pm AEST
- **Email Element:** enquiries@ior.com.au
- **Head Office Element:** IOR Petroleum Pty Ltd, 155 Cannon Hill Esplanade, Cannon Hill QLD 4170. Include a static Google Maps placeholder image and a "📍 Open in Google Maps →" text link.
- **Postal Address Element:** PO Box 6234, Upper Mount Gravatt QLD 4122.
- **After-Hours Emergency (Highlighted Block):** Highlight this block (e.g., pale yellow/amber background). 
  - **Title:** After-Hours Emergency
  - **Body:** For urgent after-hours supply emergencies, call 1300 457 467 and select the emergency option.

**Right Column (Zendesk Support Form):**
- **Anchor ID:** Ensure this right-hand column container has `id="zendesk-form"` so the hero button can anchor to it.
- **Section Header:** Send Us a Message
- **Form Note/Intro:** This form routes directly to our Zendesk Support queue. You can expect a response within one business day.
- **Form Field Labels:**
  - First Name
  - Last Name
  - Company Name
  - Email Address
  - Phone Number
  - State / Territory (Dropdown)
  - Enquiry Category (Dropdown)
  - Message (Textarea)
- **Submit Button:** Submit Enquiry →
- **Note to Devs:** This is a Zendesk integration, not a HubSpot lead capture form.

### 4. Regional Contacts Routing CTA
- **Style:** A clean, full-width callout strip below the 2-column grid.
- **Body Copy:** Looking for a specific local office or regional manager?
- **Button:** Find your Regional Contact → (Links to `11b_Regional_Contactsv5.html`)

### 5. Pre-Footer ("We're here to help")
- **Style:** Inherited from the Utility Shell.

### 6. Global Footer
- **Style:** Append the standard v4.0 6-column global footer to close out the page.

---

## 4. Asset Checklist for Builder

Please ensure you have access to the following before beginning:
- [x] Design HTML (`06_Support_and_Utility.html`) purely for layout referencing of the split 2-column contact grid.
- [x] Base Template to Duplicate/Use: `IOR_Utility_Template_Shell_v5.html`

---

## 5. Auditor Notes

- **Navigation:** All pages derived from a shell file must always use the navigation (utility bar and main navigation) and footer components provided in the shell file. The shell file should be considered the definitive template for these elements.
- **Metadata:** Verify the SEO metadata is correctly injected into the `<head>`.
- **Routing Box:** Ensure the "Still have questions?" global routing box is removed from this specific page and replaced with the Regional Contacts callout.
- **Brand Rules:** Ensure the word "depot" is strictly avoided in the Regional Contacts callout copy (use "local office" instead, as provided in the brief).
