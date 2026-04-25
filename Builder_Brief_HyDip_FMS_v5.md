# Builder Brief: HyDip™ FMS v5

**Page:** `07a_HyDip_FMS_v5.html`
**Template:** `IOR_Global_Template_Shell_v4.html` (Utility Shell v5 nav/footer)
**Global Components Reference:** [00_Global_Components.html](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html)

---

## ⚙️ 1. SEO & META DATA

- **Meta Title:** HyDip™ Fuel Management System | IOR
- **Meta Description:** The fuel network manager for unattended sites. See inside all your tanks, know who is using fuel, and manage your network remotely with HyDip™ HDv2 and HFT X2.
- **Focus Keyword:** HyDip Fuel Management System
- **Secondary Keywords:** Tank Gauging, Fuel Tracking, Unattended Fuel Sites, Remote Fuel Management

---

## 🎨 2. HYDIP BRAND & UI KIT

**Branding Boundary Rule:**
Bespoke HyDip branding applies to **page body sections only**. The global utility bar, primary nav, mobile drawer, pre-footer, and global footer must remain canonical IOR colours (`var(--ior-blue)`, `var(--ior-navy)`).

**HyDip Colours:**
- **HyDip Blue:** `#0072CE` (Primary brand colour)
- **HyDip Dark:** `#0A192F` (Dark backgrounds)
- **HyDip Accent:** `#FFB81C` (Gold/Yellow for alerts/highlights)

**Geometry:**
- **Strictly sharp edges.** `border-radius: 0` on all cards, containers, and buttons.
- Exception: `.btn--pill` (500px) is permitted for nav CTAs only.

---

## 🏗️ 3. SECTION-BY-SECTION SPECIFICATION

### Section 1: Quick Links Bar
- **Position:** Below hero
- **Label:** Explore:
- **Links:** Fuelcharge App · Customer Portal

### Section 2: SaaS Product-Led Hero
- **Background:** `var(--hydip-dark)` solid (no gradients)
- **Layout:** 50/50 split
- **Left Column (Copy):**
  - **Eyebrow:** FUEL MANAGEMENT SYSTEM
  - **H1:** The fuel network manager for unattended sites.
  - **Subcopy:** See inside all your tanks. Know who is using fuel. Deploy HyDip to track fuel usage by employees or build your own fuel distribution network.
  - **CTAs:** [Explore Devices ↓] (Primary) | [Contact Sales →] (Outline)
- **Right Column (Visual):**
  - **Asset:** `assets/images/hydip/hydip-dashboard-map-alerts.png`
  - **Treatment:** Bleed to right edge, sharp corners.

### Section 3: Core Capabilities (3-Column Grid)
- **Layout:** 3 equal columns, light background
- **Card 1:**
  - **Icon:** Tank/Gauge SVG
  - **Title:** See inside all your tanks.
  - **Body:** Fit HyDip Tank Gauging to your tanks to monitor your tank levels in near real time.
- **Card 2:**
  - **Icon:** User/ID SVG
  - **Title:** Know who is using fuel.
  - **Body:** Deploy HyDip Fuel Tracking devices to track fuel usage by employees or build your own fuel distribution network.
- **Card 3:**
  - **Icon:** Cloud/Sync SVG
  - **Title:** Always up to date.
  - **Body:** With live over-the-air updates, your devices always get the latest features and security patches.

### Section 4: Device Hardware Showcase (50/50 Split)
- **Background:** `var(--hydip-blue)` solid
- **Header:** There is a HyDip to suit your needs.
- **Left Column (HDv2):**
  - **Asset:** `assets/images/hydip/hydip-hdv2-device.png`
  - **Title:** HDv2 Tank Gauging
  - **Body:** Remotely monitor tank activity over 3G/4G and Ethernet networks. Fit a solar panel and battery for deployments to locations without power.
- **Right Column (HFT X2):**
  - **Asset:** `assets/images/hydip/hydip-hftv1-device.png` (Note: Using HFTv1 image as placeholder for X2)
  - **Title:** HFT X2 Fuel Tracking
  - **Body:** Remotely authorise tank dispensing transactions and monitor tank activity over 3G, 4G and Ethernet networks. Fit hoses, pumps and solenoids directly to the X2; no need for a separate dispenser controller.

### Section 5: Mobile App Feature (50/50 Split)
- **Layout:** Image left, copy right
- **Left Column (Visual):**
  - **Asset:** `assets/images/hydip/hydip-tank-gauge-mobile.png`
- **Right Column (Copy):**
  - **Title:** Manage your network from anywhere.
  - **Body:** Access live tank levels, transaction history, and system alerts directly from your smartphone. The HyDip mobile interface gives you complete control over your unattended sites, 24/7.

### Section 6: Support & Contact Routing
- **Background:** Light grey
- **Layout:** 2-column card grid
- **Card 1 (Sales):**
  - **Title:** Get in touch
  - **Body:** Ready to build your fuel network? Contact our sales team.
  - **CTA:** Call +61 1800 449 347
- **Card 2 (Support):**
  - **Title:** Technical Support
  - **Links:** [Service Status](https://status.hydip.com/) | [Documentation](https://docs.hydip.com) | Contact Support

---

## 🔧 4. ELEMENTOR AGENCY HANDOFF NOTES

| Item | Elementor Action Required |
|---|---|
| **HyDip Logos** | Use `assets/icons/hydip-logo-white.svg` for dark backgrounds and `assets/icons/hydip-logo-navy.svg` for light backgrounds. |
| **Device Images** | The device images (`hydip-hdv2-device.png`, `hydip-hftv1-device.png`) have black backgrounds. Use CSS blend modes (`mix-blend-mode: screen` or `lighten`) or remove the backgrounds in Elementor if placing on non-black sections. |
| **Service Status Link** | Ensure the Service Status link points exactly to `https://status.hydip.com/`. |
| **Documentation Link** | Ensure the Documentation link points exactly to `https://docs.hydip.com`. |
| **Branding Boundary** | Do not alter the global navigation or footer colours. They must remain canonical IOR. |
| **Geometry** | Ensure `border-radius: 0` is enforced globally across all new HyDip sections. |
