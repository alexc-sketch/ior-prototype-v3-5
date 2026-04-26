# Builder Brief — Case Study Single Template v6
**Status:** In Brief
**Target file:** `09d_Case_Study_Singlev6.html`
**Branch:** `feature/cs-template-v6`
**Replaces:** `CS_Template_v5.html` (binned — do not reference)
**Shell:** `IOR_Global_Template_Shell_v4.html` (Marketing Shell — NOT Utility Shell)
**Global Components reference:** https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html

---

## Context

This is a **dynamic single case study template** that will be powered by Elementor Theme Builder + ACF in production. For the prototype, build one static HTML page using **Case Study 1 (Tin Can Bay Marina)** as the default dummy data. The structure must accommodate all three case studies without layout breakage — see the Content Migration Matrix at the end of this brief.

The three case studies that must work in this template:
1. **Tin Can Bay Marina** — standard structure, bullet list, HyDip + Fuelcharge products
2. **Flight Training Adelaide (FTA)** — uses non-standard headers ("Background", "How IOR Added Value"), no table
3. **MPC Kinetic** — includes an inline responsive table, 4 remote camps

---

## Section Architecture

### Section 1 — Dynamic Case Study Hero

**Type:** Full-bleed image hero with gradient scrim from bottom up (text legibility only — this is the ONE permitted use of a gradient in the prototype, as it is a photographic hero scrim, not a background colour gradient)

**Layout:**
```
[Full-bleed background image — ACF: Hero Background Image]
[Gradient scrim — bottom 60% of hero, black to transparent]
  Eyebrow: [ACF: Industry Category]  ← small caps, var(--ior-blue) or white
  H1: [Post Title]                   ← white, large
```

**Dummy data (Tin Can Bay):**
- Background image: `assets/images/case-studies/tin-can-bay-hero.jpg` (placeholder — use any landscape image from assets if not present)
- Eyebrow: `Marine & Ports`
- H1: `Modernising the Tin Can Bay Marina`

**CSS rules:**
```css
.cs-hero {
  position: relative;
  min-height: clamp(400px, 55vw, 650px);
  display: flex;
  align-items: flex-end;
  overflow: hidden;
}
.cs-hero__bg {
  position: absolute; inset: 0;
  background-size: cover; background-position: center;
}
.cs-hero__scrim {
  position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.75) 0%, transparent 60%);
}
.cs-hero__content {
  position: relative; z-index: 2;
  padding: clamp(40px, 6vw, 80px) clamp(20px, 5vw, 80px);
  max-width: 900px;
}
```

---

### Section 2 — Fast Facts Stat Bar

**Type:** Full-width brand colour strip

**Background:** `var(--ior-blue)` (#0355A3) solid — no gradient

**Layout:** CSS Grid, `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))` — this automatically centres 2, 3, or 4 stats without any changes to the HTML.

**Each stat card:**
```html
<div class="stat-card">
  <span class="stat-card__number">[Stat Number]</span>
  <span class="stat-card__label">[Stat Label]</span>
</div>
```

**Dummy data (Tin Can Bay):**
| Stat Number | Stat Label |
|---|---|
| 172 | Marina Berths Serviced |
| 24/7 | Unmanned Fuel Access |
| 1 | Consolidated App (Fuelcharge) |

**CSS rules:**
```css
.stat-bar {
  background: var(--ior-blue);
  padding: clamp(32px, 4vw, 56px) clamp(20px, 5vw, 80px);
}
.stat-bar__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 32px;
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}
.stat-card__number {
  display: block;
  font-size: clamp(36px, 5vw, 56px);
  font-weight: 700;
  color: #fff;
  line-height: 1;
}
.stat-card__label {
  display: block;
  font-size: 14px;
  color: rgba(255,255,255,0.8);
  margin-top: 8px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

---

### Section 3 — The Narrative (70/30 Split Layout)

**Type:** CSS Grid, `grid-template-columns: 1fr 300px` on desktop, single column on mobile

**Left column (70%) — Main Body Content:**

The WYSIWYG content area. Must include the following CSS rules to handle all three case studies without breaking:

```css
/* Responsive tables — critical for MPC Kinetic */
.cs-body .table-responsive {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 24px 0;
}
.cs-body table {
  width: 100%;
  border-collapse: collapse;
  min-width: 500px;
}
.cs-body th {
  background: var(--ior-navy);
  color: #fff;
  padding: 12px 16px;
  text-align: left;
  font-size: 14px;
}
.cs-body td {
  padding: 12px 16px;
  border-bottom: 1px solid #e5e7eb;
  font-size: 14px;
}
.cs-body tr:nth-child(even) td {
  background: #f9fafb;
}

/* Branded bullets — critical for FTA */
.cs-body ul {
  list-style: none;
  padding-left: 0;
  margin: 16px 0;
}
.cs-body ul li {
  padding-left: 20px;
  position: relative;
  margin-bottom: 8px;
  line-height: 1.6;
}
.cs-body ul li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 8px;
  width: 8px;
  height: 8px;
  background: var(--ior-blue);
}

/* Inline blockquotes — critical for MPC Kinetic */
.cs-body blockquote {
  border-left: 4px solid var(--ior-blue);
  margin: 24px 0;
  padding: 16px 20px;
  background: #f0f6ff;
  font-style: italic;
  color: var(--ior-navy);
}

/* Section headings */
.cs-body h2 {
  font-size: clamp(20px, 2.5vw, 26px);
  color: var(--ior-navy);
  margin: 32px 0 12px;
  padding-top: 8px;
  border-top: 2px solid var(--ior-blue);
}
.cs-body h2:first-child {
  margin-top: 0;
  border-top: none;
}
```

**Right column (30%) — Sticky Sidebar:**

`position: sticky; top: 100px;`

Two blocks:

**Block A — Location:**
```html
<div class="cs-sidebar__block">
  <p class="cs-sidebar__label">Location</p>
  <p class="cs-sidebar__value">[ACF: Location]</p>
</div>
```

**Block B — Products Used** (hide if empty):
```html
<div class="cs-sidebar__block">
  <p class="cs-sidebar__label">Products Used</p>
  <div class="cs-sidebar__pills">
    <span class="cs-pill">[Product 1]</span>
    <span class="cs-pill">[Product 2]</span>
    <!-- etc -->
  </div>
</div>
```

**CSS rules:**
```css
.cs-layout {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 48px;
  max-width: 1200px;
  margin: 0 auto;
  padding: clamp(40px, 5vw, 80px) clamp(20px, 5vw, 80px);
  align-items: start;
}
.cs-sidebar {
  position: sticky;
  top: 100px;
}
.cs-sidebar__block {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  padding: 20px;
  margin-bottom: 16px;
}
.cs-sidebar__label {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #6b7280;
  margin-bottom: 8px;
  font-weight: 600;
}
.cs-sidebar__value {
  font-size: 15px;
  color: var(--ior-navy);
  font-weight: 500;
}
.cs-sidebar__pills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.cs-pill {
  display: inline-block;
  padding: 6px 14px;
  background: var(--ior-blue);
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  border-radius: 500px; /* pills are explicitly permitted */
}

/* Mobile: stack layout */
@media (max-width: 768px) {
  .cs-layout {
    grid-template-columns: 1fr;
  }
  .cs-sidebar {
    position: static;
    order: -1; /* sidebar moves above body on mobile */
  }
}
```

---

### Section 4 — The Proof (Testimonial Block)

**Type:** Full-width dark block

**Background:** `var(--ior-navy)` solid

**Conditional:** Hide entire section if Testimonial Quote field is empty. In the prototype, implement this with a CSS class toggle — add `data-cs-testimonial` to the section and a JS check: if the quote `<p>` is empty, add `hidden` attribute.

**Layout:**
```html
<section class="cs-testimonial" data-cs-testimonial>
  <div class="cs-testimonial__inner">
    <span class="cs-testimonial__mark" aria-hidden="true">"</span>
    <blockquote class="cs-testimonial__quote">
      [ACF: Testimonial Quote]
    </blockquote>
    <p class="cs-testimonial__attr">
      <strong>[ACF: Author Name]</strong> — [ACF: Author Title]
    </p>
  </div>
</section>
```

**CSS rules:**
```css
.cs-testimonial {
  background: var(--ior-navy);
  padding: clamp(56px, 7vw, 96px) clamp(20px, 5vw, 80px);
  text-align: center;
}
.cs-testimonial__inner {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}
.cs-testimonial__mark {
  display: block;
  font-size: 120px;
  line-height: 0.6;
  color: var(--ior-blue);
  font-family: Georgia, serif;
  margin-bottom: 24px;
}
.cs-testimonial__quote {
  font-size: clamp(18px, 2.2vw, 24px);
  color: #fff;
  font-style: italic;
  line-height: 1.6;
  margin-bottom: 24px;
}
.cs-testimonial__attr {
  color: rgba(255,255,255,0.7);
  font-size: 14px;
}
.cs-testimonial__attr strong {
  color: #fff;
}
```

---

### Section 5 — Related Case Studies Grid

**Type:** Standard 3-card global component

**Background:** White or `#f9fafb`

**Layout:** 3-column card grid — same component as used on `09d_Case_Studies.html`

**Card content pulls from ACF: Loop Grid Excerpt** — not the post excerpt or body copy.

**Dummy data — 3 cards:**

| Card | Title | Excerpt | Category |
|---|---|---|---|
| 1 | Modernising the Tin Can Bay Marina | How IOR transformed a 172-berth marina by installing HyDip® dispensing technology and the Fuelcharge app, generating 24/7 unmanned sales. | Marine & Ports |
| 2 | IOR Supports the Next Generation of Australian Pilots | IOR partnered with Flight Training Adelaide to deliver reliable aviation fuel supply at Parafield Airport, supporting their fleet of training aircraft around the clock. | Aviation |
| 3 | Fuelling MPC Kinetic's Remote Operations | When MPC Kinetic needed a reliable fuel supply partner for remote civil and mining projects, IOR delivered a tailored bulk diesel solution with real-time monitoring. | Mining & Resources |

All three cards link to `09d_Case_Study_Singlev6.html` (self-referencing in the prototype).

---

### Section 6 — Pre-Footer + Footer

Verbatim from `IOR_Global_Template_Shell_v4.html`. No changes.

---

## Content Migration Matrix

### Case Study 1 — Tin Can Bay Marina

| Field | Value |
|---|---|
| Post Title | Modernising the Tin Can Bay Marina |
| Industry Category | Marine & Ports |
| Location | Great Sandy Strait, QLD |
| Loop Grid Excerpt | How IOR transformed a 172-berth marina by installing HyDip® dispensing technology and the Fuelcharge app, generating 24/7 unmanned sales. |
| Fast Facts | 172 / Marina Berths Serviced · 24/7 / Unmanned Fuel Access · 1 / Consolidated App (Fuelcharge) |
| Products Used | Fuelcharge · HyDip™ FMS · Self-Bunded Tanks |
| Testimonial Quote | "I drive past the fuel dock on my day off and see customers using Fuelcharge to pay online. I can see the transactions and know that I'm making money even when the site is unmanned." |
| Testimonial Author | Chris Rippon — Proprietor, Tin Can Bay Marina |

**Main Body Content (WYSIWYG):**
```html
<h2>The Challenge</h2>
<p>Tin Can Bay Marina is situated approximately 210 km north of Brisbane, at the southern end of the Great Sandy Strait. The marina currently services 172 short and long term berths, fishing charters, commercial and recreational boaters. In need of renovation and an update, Tin Can Bay Marina contacted IOR and together began working on improvements to the marina fuel facility.</p>

<h2>HyDip Fuel Management and Payment Technology</h2>
<p>IOR installed HyDip® fuel dispensing and payment technology allowing the marina to track their fuel usage and sell fuel 24/7. This technology also enables their customers to access fuel via tag on account, or via the Fuelcharge App.</p>
<p>IOR delivered a full solution:</p>
<ul>
  <li>Installed HyDip® fuel dispensing and payment technology.</li>
  <li>A new self-bunded diesel tank was installed.</li>
  <li>The underground unleaded tank was tested and recertified.</li>
  <li>New underground piping between the tanks and dispensers was installed.</li>
  <li>New wiring and electrical controls were installed.</li>
  <li>New signage, placarding &amp; safety documentation was installed around the facility.</li>
</ul>
<p>Tin Can Bay Marina can now monitor fuel sales and usage through HyDip®. Customers are also benefitting by using the Fuelcharge app which provides flexible 24/7 access to fuel even when the site is unmanned.</p>
```

---

### Case Study 2 — Flight Training Adelaide

| Field | Value |
|---|---|
| Post Title | IOR Supports the Next Generation of Australian Pilots |
| Industry Category | Aviation |
| Location | Toowoomba Wellcamp Airport, QLD |
| Loop Grid Excerpt | IOR partnered with Flight Training Adelaide to deliver reliable aviation fuel supply at Parafield Airport, supporting their fleet of training aircraft around the clock. |
| Fast Facts | 3 / Planes Refuelled Simultaneously · 55,000L / Tank Capacity · 363 / Days Operational Per Year |
| Products Used | Aviation Fuel · Aviation Network · HyDip™ FMS |
| Testimonial Quote | "We prioritise safety and efficiency in our training program so we were looking for a fuel supplier who shared those priorities and could look at different supply options to deliver a quality product. IOR have been very responsive to our needs and I am very happy with our relationship." |
| Testimonial Author | Pierre Steyn — Chief Operating Officer, FTA Queensland |

**Main Body Content (WYSIWYG):**
```html
<p>In a strong move for regional Queensland, in early 2020 the Qantas Group Pilot Training Academy was established at the Toowoomba Wellcamp Airport. IOR has assisted Academy operator Flight Training Adelaide (FTA) and Airport owner and operator Wagner Corporation in establishing and operating a state-of-the-art refuelling facility.</p>

<h2>Summary</h2>
<ul>
  <li>Proudly Australian, IOR is delighted to demonstrate its entrepreneurial and innovative capability to meet FTA's needs at the Toowoomba Wellcamp Airport facility.</li>
  <li>New facility extends IOR's long standing commitment to Toowoomba and South-West Queensland.</li>
  <li>IOR Infrastructure has drawn on over a decade's experience to develop this unique customer solution for high quality, reliable fuel storage and supply.</li>
</ul>

<h2>Background</h2>
<p>In January 2020, Qantas Group CEO Alan Joyce and Queensland Premier Annastacia Palaszczuk opened the Qantas Group Pilot Training Academy at Toowoomba's Wellcamp International Airport. The new purpose-built facility is located at the privately owned Toowoomba Wellcamp Airport.</p>
<p>Qantas appointed Flight Training Adelaide (FTA) as the training provider for the Toowoomba site. FTA is a world-class training provider for the Australian aviation industry and some of the world's leading airlines — focussed on producing future airline captains, rather than simply training students to obtain a licence.</p>

<h2>How IOR Added Value</h2>
<p>The unique aviation offering stems from IOR's commitment to partnering with customers to understand their needs, and IOR Infrastructure's extensive experience in providing value-adding, reliable and high-quality fuel management solutions.</p>
<p>IOR personnel trained the FTA staff in the use of the facility, which features a 55,000 Litre tank used 363 days per year. The facility is enhanced with IOR's proprietary fuel management technology; HyDip, providing FTA with real-time visibility on their fuel tank levels and complete oversight over fuel usage.</p>
<p>This includes the ability to monitor fuel offtake rates so that fuel deliveries may be arranged automatically, preventing the risk of stockouts.</p>
```

---

### Case Study 3 — MPC Kinetic

| Field | Value |
|---|---|
| Post Title | Fuelling MPC Kinetic's Remote Operations |
| Industry Category | Mining & Resources |
| Location | Tanami Desert, Northern Territory |
| Loop Grid Excerpt | When MPC Kinetic needed a reliable fuel supply partner for remote civil and mining projects, IOR delivered a tailored bulk diesel solution with real-time monitoring. |
| Fast Facts | 440km / Pipeline Constructed · 350+ / Workforce Supported · 4 / Remote Camps Serviced |
| Products Used | Bulk Diesel Delivery · HyDip™ FMS · Self-Bunded Tanks |
| Testimonial Quote | "The team at IOR provided the highest level of support during MPC Kinetic's construction of the Tanami Gas Pipeline. In one of the harshest regions in Australia, IOR were always there to help us overcome the challenging logistics behind fuel supply for such a remote project location. When you need a fuel supplier you can rely on, IOR are certainly the team to turn to." |
| Testimonial Author | Brendan McGuckin — Project Manager, MPC Kinetic |

**Main Body Content (WYSIWYG — includes responsive table):**
```html
<h2>About MPC Kinetic</h2>
<p>MPC Kinetic provides upstream services to the Australian energy and resources industries and have constructed more than 8,000 kilometres of new pipe networks in Australia.</p>
<p>MPC Kinetic are experts in large diametre pipeline construction for resource developers as well as state and local governments. Their team of in-house specialists has been responsible for delivering some of the longest and largest pipeline projects in the country.</p>

<h2>Tanami Natural Gas Pipeline</h2>
<p>In June 2018, MPC Kinetic was contracted to construct the 440 kilometre Tanami Natural Gas Pipeline. Presenting MPC Kinetic with their initiation into the Northern Territory, the 8-inch pipeline follows Tanami Road and passes through isolated pastoral, Aboriginal freehold, and Crown land in the middle of Australia. The workforce of 350+ team members was responsible for site preparation, logistics, construction and installation, and testing.</p>

<h2>The Challenge</h2>
<p>To safely deliver the project on time, MPC Kinetic required a fuel supplier that they could rely on to maintain supply to their isolated camps along the Tanami Road. The terrain and sheer distances between camps required a supplier with their own fleet and the flexibility to adapt to changing environments.</p>

<h2>The Solution</h2>
<p>IOR provided a comprehensive fuel supply and storage solution perfectly matched to the harsh environment. We deployed multiple self-bunded tanks across four remote camps and ensured consistent bulk diesel delivery.</p>

<div class="table-responsive">
  <table>
    <thead>
      <tr>
        <th>Location</th>
        <th>Distance from Alice Springs</th>
        <th>Storage Provided</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Camp 1</td>
        <td>150km</td>
        <td>1x 100kL, 1x 10kL Self-Bunded Tanks</td>
      </tr>
      <tr>
        <td>Camp 2</td>
        <td>260km</td>
        <td>1x 100kL, 1x 10kL Self-Bunded Tanks</td>
      </tr>
      <tr>
        <td>Camp 3</td>
        <td>375km</td>
        <td>1x 100kL, 1x 10kL Self-Bunded Tanks</td>
      </tr>
      <tr>
        <td>Camp 4</td>
        <td>500km</td>
        <td>1x 100kL, 1x 10kL Self-Bunded Tanks</td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## Golden Rules Self-Audit Checklist

The builder must complete this checklist before opening the PR. Include the completed checklist in the PR description.

| # | Check | Result |
|---|---|---|
| 1 | `border-radius: 0` on all containers, cards, layout elements (`.cs-pill` excepted — pills are explicitly permitted) | |
| 2 | Zero CSS gradients **except** the hero scrim (`.cs-hero__scrim` only — photographic legibility scrim is permitted) | |
| 3 | Zero inline `style=` on body elements | |
| 4 | Hero background is a full-bleed photograph — no solid colour hero | |
| 5 | Stat bar background is `var(--ior-blue)` solid — no gradient | |
| 6 | Testimonial background is `var(--ior-navy)` solid — no gradient | |
| 7 | Nav and footer verbatim from `IOR_Global_Template_Shell_v4.html` — no changes | |
| 8 | Proto-bar above nav with link to `00_Master_Index.html` | |
| 9 | No word "depot" in live copy | |
| 10 | No operating hours in live copy | |
| 11 | Responsive table wraps in `.table-responsive` with `overflow-x: auto` | |
| 12 | Branded blue square bullets on all `<ul>` inside `.cs-body` | |
| 13 | Sidebar is `position: sticky; top: 100px` on desktop, `position: static` on mobile | |
| 14 | Testimonial section has `data-cs-testimonial` attribute and JS hides it if quote is empty | |
| 15 | All 3 related case study cards use the Loop Grid Excerpt copy (not body copy) | |
| 16 | `lang="en"` on `<html>` tag | |
| 17 | `<meta name="description">` present | |
| 18 | Support Hub links use `11_Support_Hubv5.html` | |
| 19 | No v3.5 hrefs anywhere in the file | |
| 20 | PR includes a full-width screenshot of the live GitHub Pages preview | |

---

## Auditor Notes (for handoff)

- The hero scrim gradient is **explicitly permitted** — it is a photographic legibility treatment, not a background colour gradient. The audit tool will flag it as a warning; override this as a known false positive.
- The `.cs-pill` `border-radius: 500px` is **explicitly permitted** — product pills follow the same rule as `.btn--pill` nav CTAs.
- The sticky sidebar will not function on GitHub Pages preview on mobile — this is expected. Test sticky behaviour at desktop width only.
- The conditional testimonial hide JS is for prototype demonstration only. In production, Elementor handles this with conditional visibility on the widget.
- All three case studies must be tested by swapping the dummy data manually before submitting the PR.
