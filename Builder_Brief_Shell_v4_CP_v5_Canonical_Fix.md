# Builder Brief — Shell v4 + Customer Portal v5 Canonical Fix
**Priority:** Critical — both pages are currently broken  
**Branch:** `fix/canonical-nav-footer`  
**Files:** `IOR_Global_Template_Shell_v4.html` + `07c_Customer_Portalv5.html`  
**Reference:** https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html

---

## Standing Rules (apply to every build, forever)

1. **Nav and footer are locked.** Always copy the exact HTML blocks from the `<!-- CANONICAL IOR NAVIGATION -->` and `<!-- CANONICAL IOR FOOTER -->` sections in this brief. Never write nav or footer from scratch. Never modify them.
2. **Never deviate from provided copy.** Use the exact words given. No paraphrasing, no placeholder substitutions.
3. **Design directions are final.** Do not suggest or apply visual changes without explicit approval. If you believe an enhancement is warranted, note it in the PR description and wait for approval before implementing.
4. **CTAs may be rounded.** `border-radius: 500px` on buttons is correct per the Figma spec. All other containers remain `border-radius: 0`.

---

## What Is Broken (and Why)

### Shell v4
The previous nav transplant left an **orphaned HTML fragment** outside the mobile drawer, immediately before `<main id="main-content">`. The browser renders this as a visible blue "Get in Touch" bar on page load.

### Customer Portal v5
Same orphaned fragment. Additionally: wrong pre-footer copy and wrong Bento card images.

---

## Fix 1 — Both Files: Delete Orphaned Fragment

In **both** `IOR_Global_Template_Shell_v4.html` and `07c_Customer_Portalv5.html`, find and delete this exact block (appears once in each file, immediately before `<main id="main-content">`):

```html
    <div class="drawer__ctas">
      <a href="#lead-capture" class="btn btn--primary" aria-label="Get in touch with IOR">Get in Touch</a>
      <a href="11d_Find_Location.html" class="btn btn--outline-white" aria-label="Find an IOR location">Find a Location</a>
    </div>
  </nav>
```

After deletion, the line immediately before `<main id="main-content">` must be the closing `</nav>` of the mobile drawer only.

---

## Fix 2 — Both Files: Replace Entire Nav/Header/Drawer Block

Do not patch. **Replace the entire nav block** (from the utility bar through to and including the mobile drawer closing `</nav>`) in both files with the canonical HTML below.

### Canonical Nav HTML (copy verbatim — do not modify a single character)

```html
<!-- ============================================================
     CANONICAL IOR NAVIGATION — Source: Navigation-FullWidth04 (Figma)
     DO NOT MODIFY. Copy verbatim into every page.
     Last updated: 2026-04-26
============================================================ -->

<!-- UTILITY BAR -->
<div class="ior-utility-bar">
  <div class="ior-utility-bar__inner">
    <div class="ior-utility-bar__announcement">
      <span>Announcement Message Placeholder</span>
    </div>
    <div class="ior-utility-bar__actions">
      <a href="11d_Find_Location.html" class="ior-utility-bar__link">
        <svg class="ior-utility-bar__icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M8 0C5.24 0 3 2.24 3 5c0 3.75 5 11 5 11s5-7.25 5-11c0-2.76-2.24-5-5-5zm0 6.5A1.5 1.5 0 1 1 8 3.5a1.5 1.5 0 0 1 0 3z" fill="white"/></svg>
        Find a Location
        <svg class="ior-utility-bar__chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="white" stroke-width="1.5"/></svg>
      </a>
      <a href="11e_Make_Payment.html" class="ior-utility-bar__link">
        <svg class="ior-utility-bar__icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><rect x="0" y="2" width="16" height="12" rx="0" fill="white"/><rect x="0" y="5" width="16" height="3" fill="#0355A3"/><circle cx="3" cy="11" r="1.5" fill="#0355A3"/></svg>
        Make a Payment
      </a>
      <span class="ior-utility-bar__divider" aria-hidden="true"></span>
      <a href="tel:1300457467" class="ior-utility-bar__link">
        <svg class="ior-utility-bar__icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3.5 1h3l1.5 4-2 1.5a9 9 0 0 0 3.5 3.5L11 8l4 1.5v3A1.5 1.5 0 0 1 13.5 14C6.6 14 1 8.4 1 1.5A1.5 1.5 0 0 1 2.5 0h1z" fill="white"/></svg>
        1300 457 467
      </a>
    </div>
  </div>
</div>

<!-- PRIMARY NAV -->
<header class="ior-nav" id="primary-nav" role="banner">
  <div class="ior-nav__inner">
    <a href="01_Homepage.html" class="ior-nav__logo" aria-label="IOR® home">
      <svg width="98" height="46" viewBox="0 0 97.65 45.98" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect x="0" y="12.92" width="9.27" height="31.96" fill="#231F20"/>
        <rect x="0" y="1.07" width="9.27" height="8.18" fill="#0054A4"/>
        <rect x="62.54" y="1.11" width="35.12" height="43.75" fill="#231F20"/>
        <rect x="12.39" y="0" width="47.23" height="45.98" fill="#231F20"/>
      </svg>
    </a>
    <nav class="ior-nav__menu" aria-label="Primary navigation">
      <button class="ior-nav__item" data-menu="fuel-solutions" aria-expanded="false" aria-controls="mega-fuel-solutions">
        Fuel Solutions
        <svg class="ior-nav__chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="#383838" stroke-width="1.5"/></svg>
      </button>
      <button class="ior-nav__item" data-menu="digital-platforms" aria-expanded="false" aria-controls="mega-digital-platforms">
        Digital Platforms
        <svg class="ior-nav__chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="#383838" stroke-width="1.5"/></svg>
      </button>
      <button class="ior-nav__item" data-menu="industries" aria-expanded="false" aria-controls="mega-industries">
        Industries We Serve
        <svg class="ior-nav__chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="#383838" stroke-width="1.5"/></svg>
      </button>
      <button class="ior-nav__item" data-menu="about" aria-expanded="false" aria-controls="mega-about">
        About IOR
        <svg class="ior-nav__chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="#383838" stroke-width="1.5"/></svg>
      </button>
      <button class="ior-nav__item" data-menu="support" aria-expanded="false" aria-controls="mega-support">
        Support &amp; Contact
        <svg class="ior-nav__chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="#383838" stroke-width="1.5"/></svg>
      </button>
    </nav>
    <div class="ior-nav__ctas">
      <a href="https://portal.ior.com.au" class="ior-nav__cta ior-nav__cta--outline" target="_blank" rel="noopener noreferrer" aria-label="Customer Login">
        Customer Login <span class="ior-nav__cta-arrow" aria-hidden="true">&#8594;</span>
      </a>
      <a href="https://iorapp.applyeasy.com.au/services/introduction" class="ior-nav__cta ior-nav__cta--filled" target="_blank" rel="noopener noreferrer" aria-label="Apply for an Account">
        Apply for an Account <span class="ior-nav__cta-arrow" aria-hidden="true">&#8594;</span>
      </a>
    </div>
    <button class="ior-nav__hamburger" id="hamburger-btn" aria-label="Open mobile menu" aria-expanded="false" aria-controls="mobile-drawer">
      <span></span><span></span><span></span>
    </button>
  </div>

  <!-- MEGA PANELS -->
  <div class="ior-mega" id="mega-fuel-solutions" role="region" aria-label="Fuel Solutions menu">
    <div class="ior-mega__inner">
      <div class="ior-mega__col">
        <span class="ior-mega__heading">Ground Fuels</span>
        <a href="03_Ground_Fuels.html" class="ior-mega__link">Ground Fuels Hub</a>
        <a href="03a_Diesel_Network_v3.5.html" class="ior-mega__link">IOR Diesel Stops</a>
        <a href="03b_On_Site_Refuelling_v3.5.html" class="ior-mega__link">On-Site Refuelling</a>
        <a href="03c_Bulk_Diesel_Delivery_v3.5.html" class="ior-mega__link">Bulk Diesel Delivery</a>
        <a href="03d_HyBlue_v3.5.html" class="ior-mega__link">HyBlue&#8482; AdBlue</a>
        <a href="03e_Oils_Lubricants_v3.5.html" class="ior-mega__link">Oils &amp; Lubricants</a>
      </div>
      <div class="ior-mega__col">
        <span class="ior-mega__heading">Aviation</span>
        <a href="04_Aviation_Hub_v3.5.html" class="ior-mega__link">Aviation Hub</a>
        <a href="04a_Aviation_Network_v3.5.html" class="ior-mega__link">Aviation Network</a>
        <a href="04b_Aviation_Oils_v3.5.html" class="ior-mega__link">Aviation Oils</a>
      </div>
      <div class="ior-mega__col">
        <span class="ior-mega__heading">Infrastructure</span>
        <a href="05_Equipment_Infrastructure.html" class="ior-mega__link">Equipment &amp; Infrastructure</a>
      </div>
      <div class="ior-mega__col">
        <span class="ior-mega__heading">Supply &amp; Trading</span>
        <a href="06_Supply_Trading.html" class="ior-mega__link">Supply &amp; Trading</a>
      </div>
    </div>
  </div>

  <div class="ior-mega" id="mega-digital-platforms" role="region" aria-label="Digital Platforms menu">
    <div class="ior-mega__inner">
      <div class="ior-mega__col">
        <span class="ior-mega__heading">Platforms</span>
        <a href="07_Digital_Platformsv5.html" class="ior-mega__link">Digital Platforms Hub</a>
        <a href="07a_HyDip_FMSv6.html" class="ior-mega__link">HyDip&#8482; FMS</a>
        <a href="07b_Fuelcharge_App_v8.html" class="ior-mega__link">Fuelcharge App</a>
        <a href="07c_Customer_Portalv5.html" class="ior-mega__link">Customer Portal</a>
      </div>
    </div>
  </div>

  <div class="ior-mega" id="mega-industries" role="region" aria-label="Industries We Serve menu">
    <div class="ior-mega__inner">
      <div class="ior-mega__col">
        <span class="ior-mega__heading">Industries</span>
        <a href="#" class="ior-mega__link">Transport &amp; Logistics</a>
        <a href="#" class="ior-mega__link">Agriculture</a>
        <a href="#" class="ior-mega__link">Mining &amp; Resources</a>
        <a href="#" class="ior-mega__link">Aviation &amp; Marine</a>
        <a href="#" class="ior-mega__link">Oil &amp; Gas</a>
        <a href="#" class="ior-mega__link">Construction &amp; Defence</a>
        <a href="#" class="ior-mega__link">Commercial &amp; General Business</a>
        <a href="#" class="ior-mega__link">Government &amp; Defence</a>
        <a href="#" class="ior-mega__link">Livestock</a>
      </div>
    </div>
  </div>

  <div class="ior-mega" id="mega-about" role="region" aria-label="About IOR menu">
    <div class="ior-mega__inner">
      <div class="ior-mega__col">
        <span class="ior-mega__heading">Company</span>
        <a href="09_About_IOR.html" class="ior-mega__link">About IOR</a>
        <a href="09c_Sustainability.html" class="ior-mega__link">Sustainability, HSE &amp; ESG</a>
        <a href="10_Careers.html" class="ior-mega__link">Careers</a>
      </div>
      <div class="ior-mega__col">
        <span class="ior-mega__heading">Resources</span>
        <a href="09d_Case_Studies.html" class="ior-mega__link">Case Studies</a>
        <a href="11c_News_Updates.html" class="ior-mega__link">News &amp; Updates</a>
      </div>
    </div>
  </div>

  <div class="ior-mega" id="mega-support" role="region" aria-label="Support & Contact menu">
    <div class="ior-mega__inner">
      <div class="ior-mega__col">
        <span class="ior-mega__heading">Help &amp; Support</span>
        <a href="11_Support_Hubv5.html" class="ior-mega__link">Help Centre &amp; FAQs</a>
        <a href="11a_Contact_Us.html" class="ior-mega__link">Contact Us</a>
        <a href="11b_Regional_Contacts.html" class="ior-mega__link">Regional Contacts</a>
      </div>
      <div class="ior-mega__col">
        <span class="ior-mega__heading">Quick Actions</span>
        <a href="11d_Find_Location.html" class="ior-mega__link">Find a Location</a>
        <a href="11e_Make_Payment.html" class="ior-mega__link">Make a Payment</a>
        <a href="https://iorapp.applyeasy.com.au/services/introduction" class="ior-mega__link" target="_blank" rel="noopener noreferrer">Apply for an Account</a>
      </div>
    </div>
  </div>
</header>

<!-- MOBILE DRAWER OVERLAY -->
<div class="ior-drawer-overlay" id="drawer-overlay" aria-hidden="true"></div>

<!-- MOBILE DRAWER -->
<nav class="ior-drawer" id="mobile-drawer" aria-label="Mobile navigation" aria-hidden="true">
  <div class="ior-drawer__head">
    <a href="01_Homepage.html" class="ior-drawer__logo" aria-label="IOR home">
      <svg width="80" height="38" viewBox="0 0 97.65 45.98" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect x="0" y="12.92" width="9.27" height="31.96" fill="white"/>
        <rect x="0" y="1.07" width="9.27" height="8.18" fill="#0054A4"/>
        <rect x="62.54" y="1.11" width="35.12" height="43.75" fill="white"/>
        <rect x="12.39" y="0" width="47.23" height="45.98" fill="white"/>
      </svg>
    </a>
    <button class="ior-drawer__close" id="drawer-close" aria-label="Close mobile menu">&times;</button>
  </div>
  <div class="ior-drawer__body">
    <div class="ior-drawer__item">
      <button class="ior-drawer__link" data-drawer="fs-mob" aria-expanded="false">Fuel Solutions <span aria-hidden="true">&#8250;</span></button>
      <div class="ior-drawer__sub" id="fs-mob">
        <a href="03_Ground_Fuels.html" class="ior-drawer__sub-link">Ground Fuels Hub</a>
        <a href="03a_Diesel_Network_v3.5.html" class="ior-drawer__sub-link">IOR Diesel Stops</a>
        <a href="03b_On_Site_Refuelling_v3.5.html" class="ior-drawer__sub-link">On-Site Refuelling</a>
        <a href="03c_Bulk_Diesel_Delivery_v3.5.html" class="ior-drawer__sub-link">Bulk Diesel Delivery</a>
        <a href="03d_HyBlue_v3.5.html" class="ior-drawer__sub-link">HyBlue&#8482; AdBlue</a>
        <a href="03e_Oils_Lubricants_v3.5.html" class="ior-drawer__sub-link">Oils &amp; Lubricants</a>
        <a href="04_Aviation_Hub_v3.5.html" class="ior-drawer__sub-link">Aviation Hub</a>
        <a href="05_Equipment_Infrastructure.html" class="ior-drawer__sub-link">Equipment &amp; Infrastructure</a>
        <a href="06_Supply_Trading.html" class="ior-drawer__sub-link">Supply &amp; Trading</a>
      </div>
    </div>
    <div class="ior-drawer__item">
      <button class="ior-drawer__link" data-drawer="dig-mob" aria-expanded="false">Digital Platforms <span aria-hidden="true">&#8250;</span></button>
      <div class="ior-drawer__sub" id="dig-mob">
        <a href="07_Digital_Platformsv5.html" class="ior-drawer__sub-link">Digital Platforms Hub</a>
        <a href="07a_HyDip_FMSv6.html" class="ior-drawer__sub-link">HyDip&#8482; FMS</a>
        <a href="07b_Fuelcharge_App_v8.html" class="ior-drawer__sub-link">Fuelcharge App</a>
        <a href="07c_Customer_Portalv5.html" class="ior-drawer__sub-link">Customer Portal</a>
      </div>
    </div>
    <div class="ior-drawer__item">
      <button class="ior-drawer__link" data-drawer="ind-mob" aria-expanded="false">Industries We Serve <span aria-hidden="true">&#8250;</span></button>
      <div class="ior-drawer__sub" id="ind-mob">
        <a href="#" class="ior-drawer__sub-link">Transport &amp; Logistics</a>
        <a href="#" class="ior-drawer__sub-link">Agriculture</a>
        <a href="#" class="ior-drawer__sub-link">Mining &amp; Resources</a>
        <a href="#" class="ior-drawer__sub-link">Aviation &amp; Marine</a>
        <a href="#" class="ior-drawer__sub-link">Oil &amp; Gas</a>
        <a href="#" class="ior-drawer__sub-link">Construction &amp; Defence</a>
        <a href="#" class="ior-drawer__sub-link">Commercial &amp; General Business</a>
        <a href="#" class="ior-drawer__sub-link">Government &amp; Defence</a>
        <a href="#" class="ior-drawer__sub-link">Livestock</a>
      </div>
    </div>
    <div class="ior-drawer__item">
      <button class="ior-drawer__link" data-drawer="about-mob" aria-expanded="false">About IOR <span aria-hidden="true">&#8250;</span></button>
      <div class="ior-drawer__sub" id="about-mob">
        <a href="09_About_IOR.html" class="ior-drawer__sub-link">About IOR</a>
        <a href="09c_Sustainability.html" class="ior-drawer__sub-link">Sustainability, HSE &amp; ESG</a>
        <a href="10_Careers.html" class="ior-drawer__sub-link">Careers</a>
        <a href="09d_Case_Studies.html" class="ior-drawer__sub-link">Case Studies</a>
        <a href="11c_News_Updates.html" class="ior-drawer__sub-link">News &amp; Updates</a>
      </div>
    </div>
    <div class="ior-drawer__item">
      <button class="ior-drawer__link" data-drawer="sup-mob" aria-expanded="false">Support &amp; Contact <span aria-hidden="true">&#8250;</span></button>
      <div class="ior-drawer__sub" id="sup-mob">
        <a href="11_Support_Hubv5.html" class="ior-drawer__sub-link">Help Centre &amp; FAQs</a>
        <a href="11a_Contact_Us.html" class="ior-drawer__sub-link">Contact Us</a>
        <a href="11b_Regional_Contacts.html" class="ior-drawer__sub-link">Regional Contacts</a>
        <a href="11d_Find_Location.html" class="ior-drawer__sub-link">Find a Location</a>
        <a href="11e_Make_Payment.html" class="ior-drawer__sub-link">Make a Payment</a>
      </div>
    </div>
  </div>
  <div class="ior-drawer__ctas">
    <a href="https://portal.ior.com.au" class="btn btn--primary btn--pill" target="_blank" rel="noopener noreferrer">Customer Login</a>
    <a href="https://iorapp.applyeasy.com.au/services/introduction" class="btn btn--outline-white btn--pill" target="_blank" rel="noopener noreferrer">Apply for an Account</a>
  </div>
</nav>
```

---

## Fix 3 — Both Files: Replace Entire Footer Block

Replace the entire footer (from `<footer` to `</footer>`) in both files with the canonical HTML below.

### Canonical Footer HTML (copy verbatim — do not modify a single character)

```html
<!-- ============================================================
     CANONICAL IOR FOOTER — Source: Footer08 (Figma)
     DO NOT MODIFY. Copy verbatim into every page.
     Last updated: 2026-04-26
============================================================ -->
<footer class="ior-footer" role="contentinfo">
  <div class="ior-pre-footer">
    <div class="ior-pre-footer__inner">
      <h2 class="ior-pre-footer__heading">We're here to help</h2>
      <div class="ior-pre-footer__ctas">
        <a href="https://iorapp.applyeasy.com.au/services/introduction" class="ior-pre-footer__btn ior-pre-footer__btn--filled" target="_blank" rel="noopener noreferrer">
          Apply for an Account <span aria-hidden="true">&#8594;</span>
        </a>
        <a href="11a_Contact_Us.html" class="ior-pre-footer__btn ior-pre-footer__btn--outline">
          Make an Enquiry <span aria-hidden="true">&#8594;</span>
        </a>
        <a href="11_Support_Hubv5.html" class="ior-pre-footer__btn ior-pre-footer__btn--outline">
          Need Help? <span aria-hidden="true">&#8594;</span>
        </a>
      </div>
    </div>
  </div>
  <div class="ior-footer__divider"></div>
  <div class="ior-footer__inner">
    <div class="ior-footer__col">
      <h3 class="ior-footer__heading">Contact</h3>
      <address class="ior-footer__address">
        IOR Head Office<br>
        99 Southgate Ave,<br>
        Cannon Hill, Qld 4170
      </address>
      <a href="tel:1300457467" class="ior-footer__link">Call: 1300 457 467</a>
      <a href="mailto:enquiries@ior.com.au" class="ior-footer__link">Email: enquiries@ior.com.au</a>
      <a href="11b_Regional_Contacts.html" class="ior-footer__link">Regional Contacts</a>
    </div>
    <div class="ior-footer__col">
      <h3 class="ior-footer__heading">Fuel Solutions</h3>
      <a href="03_Ground_Fuels.html" class="ior-footer__link">Ground Fuels</a>
      <a href="04_Aviation_Hub_v3.5.html" class="ior-footer__link">Aviation</a>
      <a href="05_Equipment_Infrastructure.html" class="ior-footer__link">Equipment &amp; Infrastructure</a>
      <a href="06_Supply_Trading.html" class="ior-footer__link">Supply &amp; Trading</a>
    </div>
    <div class="ior-footer__col">
      <h3 class="ior-footer__heading">Digital Platforms</h3>
      <a href="07a_HyDip_FMSv6.html" class="ior-footer__link">HyDip&#8482; FMS</a>
      <a href="07b_Fuelcharge_App_v8.html" class="ior-footer__link">Fuelcharge App</a>
      <a href="07c_Customer_Portalv5.html" class="ior-footer__link">Customer Portal</a>
    </div>
    <div class="ior-footer__col">
      <h3 class="ior-footer__heading">Corporate</h3>
      <a href="09_About_IOR.html" class="ior-footer__link">About IOR</a>
      <a href="10_Careers.html" class="ior-footer__link">Careers</a>
      <a href="09d_Case_Studies.html" class="ior-footer__link">Case Studies</a>
      <a href="09c_Sustainability.html" class="ior-footer__link">Sustainability, HSE &amp; ESG</a>
      <a href="11c_News_Updates.html" class="ior-footer__link">News &amp; Updates</a>
    </div>
    <div class="ior-footer__col">
      <h3 class="ior-footer__heading">Quick Actions</h3>
      <a href="https://iorapp.applyeasy.com.au/services/introduction" class="ior-footer__link" target="_blank" rel="noopener noreferrer">Apply for an Account</a>
      <a href="11e_Make_Payment.html" class="ior-footer__link">Make a Payment</a>
      <a href="11a_Contact_Us.html" class="ior-footer__link">Contact Us</a>
      <a href="11_Support_Hubv5.html" class="ior-footer__link">Help Centre &amp; FAQs</a>
    </div>
    <div class="ior-footer__col">
      <h3 class="ior-footer__heading">Find a Site By State</h3>
      <div class="ior-footer__states">
        <a href="11d_Find_Location.html?state=QLD" class="ior-footer__state-btn">QLD</a>
        <a href="11d_Find_Location.html?state=NSW" class="ior-footer__state-btn">NSW</a>
        <a href="11d_Find_Location.html?state=VIC" class="ior-footer__state-btn">VIC</a>
        <a href="11d_Find_Location.html?state=SA" class="ior-footer__state-btn">SA</a>
        <a href="11d_Find_Location.html?state=WA" class="ior-footer__state-btn">WA</a>
        <a href="11d_Find_Location.html?state=NT" class="ior-footer__state-btn">NT</a>
      </div>
    </div>
  </div>
  <div class="ior-footer__divider"></div>
  <div class="ior-footer__bottom">
    <p class="ior-footer__copy">
      Copyright &copy; 2026 IOR. All rights reserved.
      &nbsp;&nbsp;|&nbsp;&nbsp;
      <a href="#" class="ior-footer__legal-link">Privacy Policy</a>
      &nbsp;&nbsp;|&nbsp;&nbsp;
      <a href="#" class="ior-footer__legal-link">Terms &amp; Conditions</a>
      &nbsp;&nbsp;|&nbsp;&nbsp;
      Site by 3PM
    </p>
    <div class="ior-footer__social">
      <a href="https://www.linkedin.com/company/ior-energy" class="ior-footer__social-link" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
        <svg width="41" height="41" viewBox="0 0 41 41" fill="none"><circle cx="20.5" cy="20.5" r="20.5" fill="white"/><path d="M13 16h3v12h-3V16zm1.5-4.5a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3zM18 16h2.9v1.6h.1c.4-.8 1.4-1.6 2.9-1.6 3.1 0 3.7 2 3.7 4.7V28h-3v-6.6c0-1.6-.6-2.4-1.7-2.4-1.4 0-2 1-2 2.5V28H18V16z" fill="#0355A3"/></svg>
      </a>
      <a href="https://www.facebook.com/iorenergy" class="ior-footer__social-link" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
        <svg width="41" height="41" viewBox="0 0 41 41" fill="none"><circle cx="20.5" cy="20.5" r="20.5" fill="white"/><path d="M22 28v-7h2.4l.3-2.8H22v-1.8c0-.8.2-1.4 1.4-1.4H25V13c-.2 0-1.1-.1-2-.1-2 0-3.4 1.2-3.4 3.4v2H17V21h2.6v7H22z" fill="#0355A3"/></svg>
      </a>
      <a href="https://www.instagram.com/iorenergy" class="ior-footer__social-link" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
        <svg width="41" height="41" viewBox="0 0 41 41" fill="none"><circle cx="20.5" cy="20.5" r="20.5" fill="white"/><rect x="13" y="13" width="15" height="15" rx="4" stroke="#0355A3" stroke-width="2" fill="none"/><circle cx="20.5" cy="20.5" r="3.5" stroke="#0355A3" stroke-width="2" fill="none"/><circle cx="25" cy="16" r="1" fill="#0355A3"/></svg>
      </a>
      <a href="https://www.youtube.com/@iorenergy" class="ior-footer__social-link" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
        <svg width="41" height="41" viewBox="0 0 41 41" fill="none"><circle cx="20.5" cy="20.5" r="20.5" fill="white"/><path d="M29 17.5s-.2-1.4-.8-2c-.8-.8-1.6-.8-2-.9C23.6 14.5 20.5 14.5 20.5 14.5s-3.1 0-5.7.1c-.4.1-1.2.1-2 .9-.6.6-.8 2-.8 2S12 19 12 20.5v1.4c0 1.5.2 3 .2 3s.2 1.4.8 2c.8.8 1.8.8 2.3.9 1.7.2 7.2.2 7.2.2s3.1 0 5.7-.2c.4-.1 1.2-.1 2-.9.6-.6.8-2 .8-2s.2-1.5.2-3v-1.4c0-1.5-.2-3-.2-3zM18.5 23v-5l5.5 2.5-5.5 2.5z" fill="#0355A3"/></svg>
      </a>
    </div>
  </div>
</footer>
```

---

## Fix 4 — Customer Portal v5 Only: Fix Bento Card Images

In `07c_Customer_Portalv5.html`, update the `src` attribute on the `<img>` tags inside the `.bento__card` elements:

| Card | Correct `src` |
|---|---|
| Card 1 — Total network visibility (wide) | `assets/images/customer-portal/cp-tablet-stock-history.png` |
| Card 2 — Mitigate fraud instantly (portrait) | `assets/images/customer-portal/cp-mobile-tag-management.png` |
| Card 3 — Understand your consumption (square) | `assets/images/customer-portal/cp-tablet-stock-history.png` |
| Card 4 — Smarter budgeting (wide) | `assets/images/customer-portal/cp-mobile-tag-management.png` |

---

## Fix 5 — Customer Portal v5 Only: Add Proto-bar

The proto-bar must appear as the **very first element inside `<body>`**, before the utility bar:

```html
<!-- ─── PROTO BAR ──────────────────────────────────────────────────────── -->
<div class="proto-bar" role="navigation" aria-label="Prototype navigation">
  <div class="proto-bar__inner">
    <span class="proto-bar__label">Prototype</span>
    <div class="proto-bar__links">
      <a href="00_Master_Index.html" class="proto-bar__link">&#8592; Master Index</a>
      <span class="proto-bar__sep" aria-hidden="true"></span>
      <a href="IOR_Design_System.html" class="proto-bar__link">Design System</a>
      <span class="proto-bar__sep" aria-hidden="true"></span>
      <a href="00_Global_Components.html" class="proto-bar__link">Global Components</a>
      <span class="proto-bar__sep" aria-hidden="true"></span>
      <a href="07_Digital_Platformsv5.html" class="proto-bar__link">Digital Platforms Hub</a>
    </div>
  </div>
</div>
```

---

## Nav JavaScript

Replace the existing nav JS `<script>` block with this exact implementation:

```javascript
/* ---- Nav mega panel toggles ---- */
const navBtns = document.querySelectorAll('.ior-nav__item[data-menu]');
const megaPanels = document.querySelectorAll('.ior-mega');
navBtns.forEach(btn => {
  btn.addEventListener('click', e => {
    e.stopPropagation();
    const id = 'mega-' + btn.getAttribute('data-menu');
    const panel = document.getElementById(id);
    if (!panel) return;
    const isOpen = panel.classList.contains('ior-mega--open');
    megaPanels.forEach(p => p.classList.remove('ior-mega--open'));
    navBtns.forEach(b => b.setAttribute('aria-expanded', 'false'));
    if (!isOpen) {
      panel.classList.add('ior-mega--open');
      btn.setAttribute('aria-expanded', 'true');
    }
  });
});
document.addEventListener('click', e => {
  if (!e.target.closest('.ior-nav')) {
    megaPanels.forEach(p => p.classList.remove('ior-mega--open'));
    navBtns.forEach(b => b.setAttribute('aria-expanded', 'false'));
  }
});

/* ---- Mobile drawer ---- */
const hamburger = document.getElementById('hamburger-btn');
const drawer = document.getElementById('mobile-drawer');
const overlay = document.getElementById('drawer-overlay');
const drawerClose = document.getElementById('drawer-close');
function openDrawer() {
  drawer.classList.add('ior-drawer--open');
  overlay.classList.add('ior-drawer-overlay--open');
  drawer.removeAttribute('aria-hidden');
  hamburger.setAttribute('aria-expanded', 'true');
  document.body.style.overflow = 'hidden';
}
function closeDrawer() {
  drawer.classList.remove('ior-drawer--open');
  overlay.classList.remove('ior-drawer-overlay--open');
  drawer.setAttribute('aria-hidden', 'true');
  hamburger.setAttribute('aria-expanded', 'false');
  document.body.style.overflow = '';
}
if (hamburger) hamburger.addEventListener('click', openDrawer);
if (drawerClose) drawerClose.addEventListener('click', closeDrawer);
if (overlay) overlay.addEventListener('click', closeDrawer);

/* ---- Drawer accordion ---- */
document.querySelectorAll('.ior-drawer__link[data-drawer]').forEach(btn => {
  btn.addEventListener('click', () => {
    const sub = document.getElementById(btn.getAttribute('data-drawer'));
    if (!sub) return;
    const isOpen = sub.classList.contains('ior-drawer__sub--open');
    document.querySelectorAll('.ior-drawer__sub').forEach(s => s.classList.remove('ior-drawer__sub--open'));
    document.querySelectorAll('.ior-drawer__link[data-drawer]').forEach(b => b.setAttribute('aria-expanded', 'false'));
    if (!isOpen) {
      sub.classList.add('ior-drawer__sub--open');
      btn.setAttribute('aria-expanded', 'true');
    }
  });
});
```

---

## Self-Audit Checklist (complete before opening PR)

- [ ] No visible "Get in Touch" bar on page load in Shell v4
- [ ] No visible "Get in Touch" bar on page load in Customer Portal v5
- [ ] Nav shows exactly: Fuel Solutions / Digital Platforms / Industries We Serve / About IOR / Support & Contact
- [ ] Nav CTAs: "Customer Login →" (outline, rounded) + "Apply for an Account →" (filled, rounded)
- [ ] Footer: 6 columns — Contact / Fuel Solutions / Digital Platforms / Corporate / Quick Actions / Find a Site By State
- [ ] Footer pre-footer: "We're here to help" with 3 rounded CTAs
- [ ] CP v5 Bento Card 1: `cp-tablet-stock-history.png`
- [ ] CP v5 Bento Card 2: `cp-mobile-tag-management.png`
- [ ] CP v5 Bento Card 3: `cp-tablet-stock-history.png`
- [ ] CP v5 Bento Card 4: `cp-mobile-tag-management.png`
- [ ] Proto-bar present in both files, links to Master Index
- [ ] No inline `style=` attributes on body elements (nav/footer inline styles from Figma export must be converted to CSS classes)
- [ ] All 9 Golden Rules pass
- [ ] PR includes a screenshot of the live GitHub Pages preview at full width showing the nav renders correctly

---

## What NOT to Change

- Do not modify `ior-global.css`, `ior-global.js`, `ior-motion.js`, or `IOR_Design_System.html`
- Do not change any page body content in Customer Portal v5
- Do not change the Master Index
