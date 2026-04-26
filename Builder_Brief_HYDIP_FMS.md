# BUILDER BRIEF: HyDip™ FMS

**Target File:** `07a_HyDip_FMS_v8.html`
**Replaces:** `07a_HyDip_FMSv6.html`
**Vibe:** Hardware + Software. Azure Blue hero. Yellow CTAs.

## GLOBAL BUILD RULES (ZERO-ERROR MANDATE)
1. **Shell File:** Must be built fresh from `https://alexc-sketch.github.io/ior-prototype-v3-5/IOR_Global_Template_Shell_v4.html`. DO NOT duplicate or patch existing v3.5 or v5 HTML files.
2. **Global Components:** Reference `https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html`.
3. **No Gradients:** Backgrounds must be solid, full-bleed colours.
4. **Quick Links:** Must sit immediately below the hero banner. It is never sticky.
5. **Sharp Geometry:** `border-radius: 0` on all cards, buttons, and containers. No rounded corners.
6. **Colour Scope:** Bespoke brand colours apply to page content only. Do not alter nav, footer, or global component colours.
7. **Untouchable Files:** Do NOT modify `ior-global.css`, `ior-global.js`, `ior-motion.js`, or `IOR_Design_System.html`. Do not alter navigation structure, footer structure, or any existing component class names.

## SEO & META DATA
* **STAGING LINK:** `https://alexc-sketch.github.io/ior-prototype-v3-5/07a_HyDip_FMS_v8.html`
* **FOCUS KEYWORD:** Fuel management system
* **SECONDARY KEYWORDS:** Real-time tank monitoring, automated reorder triggers, compliance reporting
* **META TITLE:** HyDip™ Fuel Management System — Real-Time Tank Monitoring | IOR
* **META DESCRIPTION:** HyDip™ is IOR's proprietary cloud-based fuel management system. Near real-time tank monitoring, automated reorder triggers, and compliance reporting.
* **PERSONA:** Fleet Managers / Operations Managers / Site Supervisors / Finance Directors

## BRAND TONE OF VOICE
Professional, innovative, reliable, and 'adult'. Grounded, Australian, and community-focused.

## BRAND COLOURS (HyDip-Specific)
* **Primary Blue:** `#0054A4` (Full-bleed hero background. Solid, no gradient.)
* **Action Yellow:** `#FFD700` (Primary CTA buttons only. High contrast against blue.)
* **Dark Neutral:** `#13114D` (Lead trap background, typography, dark sections.)
* **Base White:** `#FFFFFF` (Text inside blue hero, clean UI cards.)

## COMPONENT FLOW

### Section 1 — Bespoke SaaS Hero
* **Layout:** Centre-aligned copy. Full-bleed solid Azure Blue (`#0054A4`). No gradients.
* **Visual:** A hand holding a smartphone popping out over an open laptop showing the HyDip dashboard.
* **H1:** Fleet fuel management. Finally solved.
* **Subcopy:** HyDip™ is IOR's purpose-built Fuel Management System. Real-time per-asset tracking, automated Fuel Tax Credit reporting, accounting integration, and a live fleet dashboard — all in one platform built for Australian operators.
* **CTA 1:** Enquire Now (Yellow — anchors to HubSpot form)
* **CTA 2:** Customer Login (White Outline — links to HyDip login)

### Section 2 — Quick Links Bar
* **Placement:** Immediately below hero. Not sticky.
* **Links:** Customer Portal | Fuelcharge App | System Status ↗ (links to `status.hydip.com`)

### Section 3 — The 'Why' (Problem Statement)
* **H2 (Two-tone):** Fuel management shouldn't be a guessing game.
* **Body:** Stop relying on manual dipsticks, estimated consumption, and missing dockets. HyDip™ replaces guesswork with precision hardware and cloud-based software, giving you absolute control over who uses your fuel, when, and where.
* **TWO-TONE RULE:** Create a reusable CSS class for the two-tone headline. First half: Dark Navy. Second half: Grey/Blue. Apply to this H2 only.

### Section 4 — The 'What' (Interactive Tabbed Solution)
* **CRITICAL:** Do NOT use a static 3-column 'Capabilities' block. Build interactive horizontal tabs.
* **Tab 1 — GAUGE:** 24/7 visibility of fuel levels. | Real-time dip measurements for fuel storage tanks in any location. Remotely check tank levels, verify vendor deliveries, and automate your reordering via the HyDip Cloud platform to prevent costly stockouts.
* **Tab 2 — TRACK:** Manage fuel to the litre. | Monitor fuel usage with highly reliable data. HyDip gives administrators 24/7 access to view and track consumption by individual vehicle, driver, or RFID tag, eliminating theft and misuse.
* **Tab 3 — DISPENSE:** Robust and trusted dispensing. | Use industry-leading technology to authorise and track fuel. The highly customisable, weather-proof dispenser allows administrators to activate the bowser onsite or remotely at any time.
* **Tab 4 — PAY:** Unmanned 24/7 payments, without the broken hardware. | Turn your bulk tank into a 24/7 revenue generator for independent retail. HyDip integrates seamlessly with Fuelcharge mobile payment technology to authorise the bowser directly from a smartphone. No moving parts, no jammed receipt printers, no weather-damaged card readers.

### Section 5 — The 'How' (Easy Onboarding Flow)
* **Step 1:** Design your solution. | Speak to our digital team to spec the right HyDip hardware for your bulk tanks and fleet size.
* **Step 2:** HyDip is installed. | Our technicians deploy the hardware, whether you need standard 4G/Ethernet connectivity or remote off-grid solar setups.
* **Step 3:** Manage your fuel. | Log in to the cloud dashboard to manage tags, set limits, and instantly connect your data to Xero, MYOB, or SAP.

### Section 6 — Trust Block (Testimonials & Pillars)
* **Row 1 — Testimonials (Carousel or split grid):**
  * **Quote 1:** IOR were a breath of fresh air... This system has made us a far better business, and I would recommend this system to anyone. | **Attribution:** Hugh Ball | Norwood Agriculture
  * **Quote 2:** I drive past the fuel dock on my day off and see customers using Fuelcharge to pay online. I can see the transactions and know that I'm making money even when the site is unmanned. | **Attribution:** Chris Rippon | Tin Can Bay Marina
* **Row 2 — Pillars (3-column block):**
  * **Pillar 1:** Supported | WHY HYDIP? | Backed by 24/7 local technical assistance, remote diagnostics, and national installation capability.
  * **Pillar 2:** Robust | WHY HYDIP? | Modern, simple hardware designed for the harshest Australian environments with IP67 ratings and resilience to power fluctuations.
  * **Pillar 3:** Connected | WHY HYDIP? | Seamlessly links to 3G/4G, Ethernet, Wi-Fi, and GPS. Connects to 3rd party dispensers like COMPAC, SANKI, and CONTREC.

### Section 7 — Hardware Specifications (Ungated Downloads)
* **CRITICAL:** 3-column card grid on light grey background. Direct PDF download links. NO forms.
* **Card 1 — HDV2 Tank Gauging:** Supports up to 4 tank level sensors (4-20mA). 3G, 4G, and XBee communications. Standalone solar panel & internal battery options. | **CTA:** Download Specs ↓ (Direct PDF Link)
* **Card 2 — HFTV1 Fuel Tracking:** RFID tag-based pump authorisation. Direct integration with 3rd party dispensers. 3G and Ethernet communication interfaces. | **CTA:** Download Specs ↓ (Direct PDF Link)
* **Card 3 — HDX2 Integrated Management:** Direct I/O pump start/stop capabilities. 110/240V AC or 12V DC power inputs. NMI Approved Flow Computer. | **CTA:** Enquire about HDX2 ↓ (Anchors to form)

### Section 8 — Dual-Purpose Lead Trap
* **Layout:** Dark Neutral (`#13114D`) full-width block. 50/50 Split.
* **Eyebrow:** GET STARTED
* **Headline:** Ready to take control of your fuel?
* **Body:** Download the complete HyDip™ Product Brochure for detailed features, FTC claim methodology, and integration guides — or submit your details below to have an IOR digital specialist contact you directly to map out a custom telemetry solution for your sites.
* **HubSpot Form:** Form ID: `2DEKpUanRQ_GZw0Jd7xaN7w`

### Section 9 — FAQ Accordion
* **Q1:** What is the HyDip fuel management system? | **A:** HyDip™ is IOR's proprietary cloud-based Fuel Management System. It combines precision hardware (tank gauges, RFID dispensers, flow computers) with a cloud dashboard to give operators real-time visibility and control over every litre of fuel stored and dispensed.
* **Q2:** How does HyDip help track fuel usage? | **A:** HyDip assigns every fuel transaction to a specific RFID tag (vehicle, driver, or machine). Administrators can view consumption by asset, set spend limits, and export ATO-compliant reports for Fuel Tax Credit claims — all from the cloud dashboard.
* **Q3:** Who should use a fuel management system like HyDip? | **A:** Any business with bulk fuel storage — from mining camps and farms to transport depots and marinas — benefits from HyDip. It is particularly valuable for operations managing multiple sites or needing to prevent fuel theft and misuse.
* **Q4:** Can HyDip work with fuel storage tanks I already own? | **A:** Yes. HyDip™ is an agnostic telemetry solution that can be retrofitted to almost any bulk storage tank or 3rd-party dispensing bowser, including COMPAC, SANKI, and CONTREC units.
* **Q5:** What reporting or visibility benefits does HyDip provide? | **A:** HyDip provides real-time tank level dips, automated low-stock alerts, per-asset consumption reports, vendor delivery verification, and ATO-compliant FTC reporting exports — all accessible from any device.
* **Q6:** How do I enquire about HyDip with IOR? | **A:** Use the form on this page to speak with an IOR digital specialist. We will assess your site requirements and design a custom HyDip solution for your infrastructure.
