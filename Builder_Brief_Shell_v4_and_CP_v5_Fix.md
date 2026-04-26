# Fix Brief — IOR Global Template Shell v4 + Customer Portal v5
**Priority:** Critical  
**Branch:** `fix/shell-v4-drawer-and-cp-v5`  
**Files to fix:** `IOR_Global_Template_Shell_v4.html` + `07c_Customer_Portalv5.html`  
**Reference:** `https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html`

---

## Root Cause (Read This First)

The nav transplant script introduced a **duplicate, orphaned `</nav>` + `<div class="drawer__ctas">` block** immediately before `<main id="main-content">` in both files. This is old drawer CTA markup from the previous nav that was not fully removed. Because it sits outside any drawer container, the browser renders it as a visible blue bar on the page.

The exact orphaned fragment that must be deleted from both files is:

```html
    <div class="drawer__ctas">
      <a href="#lead-capture" class="btn btn--primary" aria-label="Get in touch with IOR">Get in Touch</a>
      <a href="11d_Find_Location.html" class="btn btn--outline-white" aria-label="Find an IOR location">Find a Location</a>
    </div>
  </nav>
```

This fragment appears **once** in each file, immediately before `<main id="main-content">`. Delete it entirely.

---

## Fix 1 — Shell v4: Remove orphaned drawer fragment

**File:** `IOR_Global_Template_Shell_v4.html`

Find and delete this exact block (it appears once, just before `<main id="main-content">`):

```html
    <div class="drawer__ctas">
      <a href="#lead-capture" class="btn btn--primary" aria-label="Get in touch with IOR">Get in Touch</a>
      <a href="11d_Find_Location.html" class="btn btn--outline-white" aria-label="Find an IOR location">Find a Location</a>
    </div>
  </nav>
```

After deletion, the line immediately before `<main id="main-content">` should be the closing `</nav>` of the mobile drawer (the one that closes the `<nav class="drawer" id="mobile-drawer">` element).

**Verify:** After fix, there must be exactly **one** `</nav>` tag between the drawer open tag and `<main>`.

---

## Fix 2 — Customer Portal v5: Remove orphaned drawer fragment

**File:** `07c_Customer_Portalv5.html`

Same fix as above. Find and delete the identical orphaned block (appears once, just before `<main id="main-content">`):

```html
    <div class="drawer__ctas">
      <a href="#lead-capture" class="btn btn--primary" aria-label="Get in touch with IOR">Get in Touch</a>
      <a href="11d_Find_Location.html" class="btn btn--outline-white" aria-label="Find an IOR location">Find a Location</a>
    </div>
  </nav>
```

---

## Fix 3 — Customer Portal v5: Fix pre-footer CTA band copy

**File:** `07c_Customer_Portalv5.html`

The pre-footer section currently shows:
> "We're here to help. Talk to our team about fuel supply, account setup, or technical support."

This is the Shell v4 template placeholder copy. Replace the entire pre-footer section with the correct Customer Portal pre-footer per the original brief:

**Find** the pre-footer section (it has class `pre-footer` or `cta-band` and contains "We're here to help"):

Replace the headline, subcopy, and CTAs with:

```html
<!-- ============================================================
     PRE-FOOTER CTA BAND — Canonical IOR
============================================================ -->
<section class="pre-footer" aria-labelledby="pre-footer-heading">
  <div class="pre-footer__inner">
    <h2 class="pre-footer__heading" id="pre-footer-heading">Ready to get started?</h2>
    <p class="pre-footer__sub">Join thousands of Australian businesses managing their fuel smarter with IOR.</p>
    <div class="pre-footer__ctas">
      <a href="https://iorapp.applyeasy.com.au/services/introduction" class="btn btn--primary btn--pill" target="_blank" rel="noopener noreferrer" aria-label="Apply for an IOR account">Apply for an Account</a>
      <a href="11a_Contact_Us.html" class="btn btn--outline-white btn--pill" aria-label="Make an enquiry">Make an Enquiry</a>
      <a href="11_Support_Hubv5.html" class="btn btn--ghost-white btn--pill" aria-label="Visit the support hub">Need Help?</a>
    </div>
  </div>
</section>
```

---

## Fix 4 — Customer Portal v5: Fix Bento card images

**File:** `07c_Customer_Portalv5.html`

The Bento grid cards are using incorrect images. The correct asset mapping is:

| Card | Correct image | Current (wrong) |
|---|---|---|
| Card 1 — Total network visibility (wide, span 2) | `assets/images/customer-portal/cp-tablet-stock-history.png` | `cp-hero-device-mockup.png` |
| Card 2 — Mitigate fraud instantly (portrait, span 1) | `assets/images/customer-portal/cp-mobile-tag-management.png` | ✓ correct |
| Card 3 — Understand your consumption (square, span 1) | `assets/images/customer-portal/cp-tablet-stock-history.png` | `cp-mobile-tag-management.png` |
| Card 4 — Smarter budgeting (wide, span 2) | `assets/images/customer-portal/cp-mobile-tag-management.png` | ✓ correct |

In the HTML, find each `<img>` tag inside the `.bento__card` elements and update the `src` attributes to match the table above.

---

## Self-Audit Checklist (complete before opening PR)

- [ ] Shell v4: No visible "Get in Touch" bar on page load (before any nav interaction)
- [ ] Shell v4: Exactly one `</nav>` tag between `<nav class="drawer"` and `<main id="main-content">`
- [ ] Shell v4: Page renders with hero section immediately below the nav
- [ ] CP v5: No visible "Get in Touch" bar on page load
- [ ] CP v5: Pre-footer reads "Ready to get started?" with 3 CTAs
- [ ] CP v5: Bento Card 1 shows tablet stock history image
- [ ] CP v5: Bento Card 2 shows mobile tag management image
- [ ] CP v5: Bento Card 3 shows tablet stock history image
- [ ] CP v5: Bento Card 4 shows mobile tag management image
- [ ] Both files: All 9 Golden Rules still pass
- [ ] Both files: Nav shows Fuel Solutions / Digital Platforms / Industries We Serve / About IOR / Support & Contact
- [ ] Both files: Proto-bar routing present and links to Master Index

---

## What NOT to Change

- Do not modify `ior-global.css`, `ior-global.js`, or `ior-motion.js`
- Do not change the nav structure, mega menus, or footer
- Do not change any page body content in Customer Portal v5 (hero, features, access block, testimonial, FAQ, related content)
- Do not change the Master Index
