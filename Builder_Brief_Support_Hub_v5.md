# Builder Brief: Support & Contact Hub (v5.0)

**To:** Development & Design Team  
**From:** UX Audit / Manus AI Builder  
**Date:** April 25, 2026  
**Project:** IOR Prototype v3.5  

---

## 1. Document Metadata & SEO Directives

**STAGING LINK:** `11_Support_Hubv5.html` (To be built)  
**GLOBAL COMPONENTS REFERENCE:** [Global Components](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html)  
**FOCUS KEYWORD:** IOR support  
**SECONDARY KEYWORDS:** Fuel account support, general enquiries  
**META TITLE:** Support & Contact | IOR  
**META DESCRIPTION:** Get support from IOR's locally-based customer service team. General enquiries, account support, regional contacts, and payment assistance.  

---

## 2. The Build Strategy (Using the Utility Shell)

Please build this page using the new `IOR_Utility_Template_Shell_v5.html` as the foundation.

- **KEEP:** The Global Header, Proto-Bar, Mobile Drawer, and 6-column Footer must remain intact.
- **KEEP:** Because this is the Hub (the gateway to all other utility pages), ensure you keep the Pre-Footer ("We're here to help") CTA band.
- **REMOVE:** Remove the "Still have questions?" global routing box from the bottom of the page (as this page *is* the answer to that question).

**Page Objective:** Customers need fast-lane access to support without navigating the full site. The Support hub deflects high-friction tasks and routes users to the right contact.

---

## 3. Wireframe Component Flow & Structure

Please ensure the build matches this exact top-to-bottom component flow and linking logic:

### 1. Minimal Utility Hero (Inherited from Utility Shell)
- **Style:** Solid brand color (`var(--ior-navy)`). No heavy videos.
- **Eyebrow:** SUPPORT & CONTACT
- **H1:** We're Here to Help.
- **Subcopy:** Find the quickest way to get in touch, find your answers, or access your documents. IOR's support team is available Monday–Friday, 7am–5pm AEST.
- **CTAs (2 Buttons):** 
  - Primary Button: 📞 1300 457 467 (Link: `tel:1300457467`)
  - Outline White Button: Submit an Enquiry (Links to `11a_Contact_Usv5.html`)

### 2. Quick Links Bar ("Explore:")
- **Style:** The standard horizontal link bar.
- **Label:** Explore:
- **Links Required:** 
  1. Fuel Solutions
  2. Digital Platforms
  3. Industries We Serve
  4. About IOR

### 3. Quick Contact Strip (Fast-Lane Information)
- **Visual Reference:** See `06_Support_and_Utility.html#support-hub` (the blue 3-column strip under the hero).
- **Style:** A full-width `var(--ior-blue)` strip breaking down the 3 core contact methods.
- **Column 1 (Phone):** 📞 1300 457 467 | Mon–Fri · 7am–5pm AEST
- **Column 2 (Email):** ✉️ enquiries@ior.com.au | Response usually within 1 business day
- **Column 3 (Address):** 📍 Cannon Hill, QLD 4170 | IOR Head Office

### 4. Support Routing Grid (The Core Hub)
- **Visual Reference:** See `06_Support_and_Utility.html#support-hub` (the "How Can We Help?" section).
- **Style:** A 2x2 grid of clean, white interactive cards sitting on a `var(--grey-50)` background.
- **Section Header:** How Can We Help?

**The 4 Primary Cards:**
1. **Contact Us**
   - Title: Contact Us
   - Body: Submit a general enquiry, request a quote, or log a service ticket. Our local customer service team is ready to assist.
   - Link text: Submit an Enquiry → (Links to `11a_Contact_Usv5.html`)
2. **Help Centre & FAQs**
   - Title: Help Centre & FAQs
   - Body: Search our comprehensive knowledge base for quick answers to common account, billing, and operational questions.
   - Link text: Browse Knowledge Base → (External Link to Zendesk portal)
3. **Regional Contacts**
   - Title: Regional Contacts
   - Body: Find your local IOR office and speak directly with your regional ground fuel or aviation representative.
   - Link text: Find a Local Rep → (Links to `11b_Regional_Contactsv5.html`) *(Note: The word "depot" is strictly avoided here per brand rules).*
4. **Make a Payment**
   - Title: Make a Payment
   - Body: Pay your IOR fuel account invoice securely online via credit card or view instructions for Electronic Funds Transfer (EFT).
   - Link text: Pay Securely Online → (Links to `11e_Make_Paymentv5.html`)

### 5. Secondary Utility Links
- **Style:** Below the 2x2 grid, include a clean 2-column layout for the remaining essential utility links.
- **Card 1: Customer Portal**
   - Title: Customer Portal Login
   - Body: Log into your secure portal to access your live account balance, download recent invoices, statements, and view delivery documentation 24/7.
   - Link text: Log in to Portal → (External link to IOR Portal)
- **Card 2: Forms & Downloads**
   - Title: Policy & Form Downloads
   - Body: Access essential company policies, Safety Data Sheets (SDS), account applications, and direct debit forms.
   - Link text: View All Downloads → (Links to `11f_Policy_Downloadsv5.html`)

### 6. Pre-Footer ("We're here to help")
- **Style:** Inherited from the Global Shell. Keep this standard CTA band to catch anyone who scrolls past the routing grid.

### 7. Global Footer
- **Style:** Append the standard v4.0 6-column global footer to close out the page.

---

## 4. Asset Checklist for Builder

Please ensure you have access to the following before beginning:
- [x] Design HTML & SVGs (Use `06_Support_and_Utility.html` purely for layout reference).
- [x] Base Template to Duplicate/Use: `IOR_Utility_Template_Shell_v5.html`

---

## 5. Auditor Notes

- **Navigation:** All pages derived from a shell file must always use the navigation (utility bar and main navigation) and footer components provided in the shell file. The shell file should be considered the definitive template for these elements.
- **Metadata:** Verify the SEO metadata is correctly injected into the `<head>`.
- **Routing Box:** Ensure the "Still have questions?" global routing box is removed from this specific page.
