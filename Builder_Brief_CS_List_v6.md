# Builder Brief — Case Studies List v6
**Status:** In Brief
**Target file:** `09d_Case_Studies_v6.html`
**Branch:** `feature/cs-list-v6`
**Replaces:** `09d_Case_Studies.html` (binned — do not reference)
**Shell:** `IOR_Global_Template_Shell_v4.html` (Marketing Shell — NOT Utility Shell)
**Global Components reference:** https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html

---

## SEO & Meta

| Field | Value |
|---|---|
| `<title>` | IOR Case Studies \| Fuel Solutions in Action \| IOR |
| `<meta name="description">` | Explore IOR case studies: MPC Kinetic Tanami Pipeline, Flight Training Adelaide, Tin Can Bay Marina, and more. Real results for Australian industry. |
| Focus keyword | Commercial fuel case studies |
| Secondary keywords | Enterprise fuel supply examples, refuelling projects |

---

## Context

This is the **Case Studies archive list page** — the index page that lists all case studies with filtering. It pairs directly with the single case study template (`09d_Case_Study_Singlev6.html`). The two pages must be visually consistent — both use the Marketing Shell, both use `var(--ior-navy)` heroes.

In production this page is powered by Elementor's Loop Grid + Taxonomy Filter widgets querying the Case Studies Custom Post Type. In the prototype, build 3 static cards using the dummy data from the Content Migration Matrix below.

---

## Section Architecture

### Section 1 — Marketing Hero

**Background:** `var(--ior-navy)` solid — **no gradient, no image, no overlay**

**Layout:** Centre-aligned, single column

```html
<section class="cs-list-hero">
  <div class="cs-list-hero__inner">
    <p class="eyebrow">PROJECTS & SOLUTIONS</p>
    <h1>Case Studies.</h1>
    <p class="subcopy">Real-world examples of how we partner with heavy industry, aviation, and commercial fleets to overcome complex fuel and logistics challenges across Australia.</p>
  </div>
</section>
```

**CSS rules:**
```css
.cs-list-hero {
  background: var(--ior-navy);
  padding: clamp(64px, 8vw, 120px) clamp(20px, 5vw, 80px);
  text-align: center;
}
.cs-list-hero__inner {
  max-width: 760px;
  margin: 0 auto;
}
.cs-list-hero .eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ior-blue);
  margin-bottom: 16px;
}
.cs-list-hero h1 {
  font-size: clamp(40px, 6vw, 72px);
  font-weight: 800;
  color: #fff;
  line-height: 1.05;
  margin-bottom: 20px;
}
.cs-list-hero .subcopy {
  font-size: clamp(16px, 1.8vw, 19px);
  color: rgba(255,255,255,0.8);
  line-height: 1.6;
  max-width: 640px;
  margin: 0 auto;
}
```

---

### Section 2 — Quick Links Bar

**Position:** Immediately below the hero — **not sticky**

**Label:** Explore:

**Links:**
1. Our Leadership → `09b_Our_Leadershipv5.html`
2. Community & Giving Back → `#` (not yet built)
3. Sustainability, HSE & ESG → `#` (not yet built)
4. News & Updates → `11c_News_Updates.html`

**CSS rules:** Use the standard `.quick-links-bar` component from the Global Components reference. No custom styling.

```html
<section class="quick-links-bar">
  <div class="quick-links-bar__inner">
    <span class="quick-links-bar__label">Explore:</span>
    <nav class="quick-links-bar__links" aria-label="Section quick links">
      <a href="09b_Our_Leadershipv5.html">Our Leadership</a>
      <a href="#">Community &amp; Giving Back</a>
      <a href="#">Sustainability, HSE &amp; ESG</a>
      <a href="11c_News_Updates.html">News &amp; Updates</a>
    </nav>
  </div>
</section>
```

---

### Section 3 — Taxonomy Filter Bar

**Position:** Immediately above the Loop Grid, inside the grid section container

**Style:** Clean row of toggle buttons — active state uses `var(--ior-blue)` fill, inactive uses white fill with `var(--ior-navy)` border

**Categories (in order):**
- Show All *(active by default)*
- Agriculture
- Aviation
- Marine & Ports
- Mining & Resources
- Transport & Logistics

**Behaviour:** In the prototype, implement with vanilla JS. Clicking a filter button adds `data-filter="[category]"` to the grid container and hides cards whose `data-category` attribute does not match. "Show All" removes the filter and shows all cards.

**HTML:**
```html
<div class="cs-filter-bar" role="group" aria-label="Filter case studies by industry">
  <button class="cs-filter-btn is-active" data-filter="all">Show All</button>
  <button class="cs-filter-btn" data-filter="agriculture">Agriculture</button>
  <button class="cs-filter-btn" data-filter="aviation">Aviation</button>
  <button class="cs-filter-btn" data-filter="marine-ports">Marine &amp; Ports</button>
  <button class="cs-filter-btn" data-filter="mining-resources">Mining &amp; Resources</button>
  <button class="cs-filter-btn" data-filter="transport-logistics">Transport &amp; Logistics</button>
</div>
```

**CSS rules:**
```css
.cs-filter-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 40px;
}
.cs-filter-btn {
  padding: 10px 20px;
  border: 2px solid var(--ior-navy);
  background: #fff;
  color: var(--ior-navy);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
  border-radius: 500px; /* filter pills — explicitly permitted */
}
.cs-filter-btn:hover,
.cs-filter-btn.is-active {
  background: var(--ior-blue);
  border-color: var(--ior-blue);
  color: #fff;
}
```

**JS (vanilla — add to page `<script>` block):**
```javascript
(function() {
  const filterBtns = document.querySelectorAll('.cs-filter-btn');
  const cards = document.querySelectorAll('.cs-card[data-category]');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      filterBtns.forEach(b => b.classList.remove('is-active'));
      this.classList.add('is-active');
      const filter = this.dataset.filter;
      cards.forEach(card => {
        if (filter === 'all' || card.dataset.category === filter) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
})();
```

---

### Section 4 — Case Studies Loop Grid

**Background:** `#f9fafb` (var(--grey-50) or equivalent light grey)

**Layout:** 3-column CSS Grid on desktop, 2-column on tablet, 1-column on mobile

**Pagination:** In the prototype, show all 3 cards. Add a disabled "Next Page →" button below the grid as a UI placeholder.

**Card structure:**

```html
<article class="cs-card" data-category="[category-slug]">
  <a href="09d_Case_Study_Singlev6.html" class="cs-card__image-link">
    <div class="cs-card__image" style="background-image: url('[hero image path]')"></div>
  </a>
  <div class="cs-card__body">
    <p class="cs-card__eyebrow">[Industry Category] &nbsp;|&nbsp; [Location]</p>
    <h3 class="cs-card__title"><a href="09d_Case_Study_Singlev6.html">[Post Title]</a></h3>
    <p class="cs-card__excerpt">[Loop Grid Excerpt]</p>
    <a href="09d_Case_Study_Singlev6.html" class="cs-card__cta">Read Case Study &rarr;</a>
  </div>
</article>
```

**CSS rules:**
```css
.cs-grid-section {
  background: #f9fafb;
  padding: clamp(48px, 6vw, 80px) clamp(20px, 5vw, 80px);
}
.cs-grid-section__inner {
  max-width: 1200px;
  margin: 0 auto;
}
.cs-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
}
.cs-card {
  background: #fff;
  border: 1px solid #e5e7eb;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.cs-card__image {
  height: 220px;
  background-size: cover;
  background-position: center;
}
.cs-card__body {
  padding: 24px;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.cs-card__eyebrow {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--ior-blue);
  margin-bottom: 10px;
}
.cs-card__title {
  font-size: 18px;
  font-weight: 700;
  color: var(--ior-navy);
  line-height: 1.3;
  margin-bottom: 12px;
}
.cs-card__title a {
  color: inherit;
  text-decoration: none;
}
.cs-card__title a:hover {
  color: var(--ior-blue);
}
.cs-card__excerpt {
  font-size: 14px;
  color: #4b5563;
  line-height: 1.6;
  flex: 1;
  margin-bottom: 20px;
}
.cs-card__cta {
  font-size: 14px;
  font-weight: 600;
  color: var(--ior-blue);
  text-decoration: none;
  margin-top: auto;
}
.cs-card__cta:hover {
  text-decoration: underline;
}

/* Pagination */
.cs-pagination {
  text-align: center;
  margin-top: 48px;
}
.cs-pagination__btn {
  padding: 12px 28px;
  border: 2px solid var(--ior-navy);
  background: #fff;
  color: var(--ior-navy);
  font-size: 14px;
  font-weight: 600;
  cursor: not-allowed;
  opacity: 0.45;
  border-radius: 500px; /* pagination pill — explicitly permitted */
}

/* Responsive */
@media (max-width: 900px) {
  .cs-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .cs-grid { grid-template-columns: 1fr; }
}
```

---

## Dummy Data — 3 Case Study Cards

### Card 1 — Tin Can Bay Marina

| Field | Value |
|---|---|
| `data-category` | `marine-ports` |
| Hero image | `assets/images/case-studies/tin-can-bay-hero.jpg` (use any landscape placeholder if not present) |
| Eyebrow | Marine & Ports &nbsp;\|&nbsp; Great Sandy Strait, QLD |
| Title | Modernising the Tin Can Bay Marina |
| Excerpt | How IOR transformed a 172-berth marina by installing HyDip® dispensing technology and the Fuelcharge app, generating 24/7 unmanned sales. |
| Link | `09d_Case_Study_Singlev6.html` |

---

### Card 2 — Flight Training Adelaide

| Field | Value |
|---|---|
| `data-category` | `aviation` |
| Hero image | `assets/images/case-studies/fta-hero.jpg` (use any landscape placeholder if not present) |
| Eyebrow | Aviation &nbsp;\|&nbsp; Toowoomba Wellcamp Airport, QLD |
| Title | IOR Supports the Next Generation of Australian Pilots |
| Excerpt | IOR partnered with Flight Training Adelaide to deliver reliable aviation fuel supply at Parafield Airport, supporting their fleet of training aircraft around the clock. |
| Link | `09d_Case_Study_Singlev6.html` |

---

### Card 3 — MPC Kinetic

| Field | Value |
|---|---|
| `data-category` | `mining-resources` |
| Hero image | `assets/images/case-studies/mpc-kinetic-hero.jpg` (use any landscape placeholder if not present) |
| Eyebrow | Mining & Resources &nbsp;\|&nbsp; Tanami Desert, Northern Territory |
| Title | Fuelling MPC Kinetic's Remote Operations |
| Excerpt | When MPC Kinetic needed a reliable fuel supply partner for remote civil and mining projects, IOR delivered a tailored bulk diesel solution with real-time monitoring. |
| Link | `09d_Case_Study_Singlev6.html` |

---

### Section 5 — Pre-Footer + Footer

Verbatim from `IOR_Global_Template_Shell_v4.html`. No changes.

---

## Golden Rules Self-Audit Checklist

Complete this checklist and include it in the PR description.

| # | Check | Result |
|---|---|---|
| 1 | `border-radius: 0` on all containers, cards, layout elements (`.cs-filter-btn`, `.cs-pagination__btn` excepted — pills explicitly permitted) | |
| 2 | Zero CSS gradients — hero is `var(--ior-navy)` solid, no scrim | |
| 3 | Zero inline `style=` on body elements (card image `background-image` inline style is permitted — it simulates the Elementor dynamic tag) | |
| 4 | Hero background is `var(--ior-navy)` solid — no image, no gradient | |
| 5 | Quick Links Bar is **below** the hero — not sticky | |
| 6 | Taxonomy filter bar is **above** the grid — not sticky | |
| 7 | Nav and footer verbatim from `IOR_Global_Template_Shell_v4.html` — no changes | |
| 8 | Proto-bar above nav with link to `00_Master_Index.html` | |
| 9 | No word "depot" in live copy | |
| 10 | No operating hours in live copy | |
| 11 | All 3 cards have correct `data-category` attribute matching filter slug | |
| 12 | Filter JS works — clicking each category hides non-matching cards | |
| 13 | "Show All" restores all 3 cards | |
| 14 | Pagination "Next Page →" button is present but visually disabled (`opacity: 0.45`, `cursor: not-allowed`) | |
| 15 | Card eyebrow shows `[Industry Category] | [Location]` — both fields present | |
| 16 | Card excerpt uses Loop Grid Excerpt copy — not body copy | |
| 17 | All card links point to `09d_Case_Study_Singlev6.html` | |
| 18 | No v3.5 hrefs anywhere in the file | |
| 19 | Support Hub links use `11_Support_Hubv5.html` | |
| 20 | PR includes a full-width screenshot of the live GitHub Pages preview showing the filter bar and at least 2 cards | |

---

## Auditor Notes (for handoff)

- The `style="background-image: url(...)"` on `.cs-card__image` divs is an **explicitly permitted inline style** — it simulates the Elementor dynamic featured image tag. This is the only permitted inline style in the file. The audit tool will flag it; override as a known exception.
- The `.cs-filter-btn` and `.cs-pagination__btn` `border-radius: 500px` are **explicitly permitted** — filter pills and pagination pills follow the same rule as `.btn--pill` nav CTAs.
- The filter JS must be tested with all 5 category filters before submitting the PR. Each filter must hide the correct cards and "Show All" must restore all 3.
- In production, the Elementor Taxonomy Filter widget handles all filtering logic. The vanilla JS in this prototype is for demonstration only.
- If no hero image assets exist for the case studies, use any landscape image from `assets/images/` as a placeholder. The image path is not audited — only the structure is.
