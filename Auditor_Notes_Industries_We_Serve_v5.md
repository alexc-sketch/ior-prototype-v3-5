# Auditor Notes — Industries We Serve (v5)

**Date:** 27 April 2026
**Prepared by:** Lead (Manus)
**Sprint:** Industries We Serve — Post-Merge QA Pass
**Commit:** `76853db` on `main`
**Branch:** `main` (merged from `feat/industries-we-serve-v5` via PR #112)

---

## 1. Automated Audit Results

All 9 pages passed the full 20-check `audit.py` suite. No failures remain.

| Page | File | Lines | Audit |
|------|------|-------|-------|
| Industries We Serve Hub | `08_Industries_v5.html` | 846 | ✅ 20/20 |
| Mining & Resources | `08a_Mining_v5.html` | 1,391 | ✅ 20/20 |
| Agriculture & Harvest | `08b_Agriculture_v5.html` | 1,399 | ✅ 20/20 |
| Transport & Logistics | `08c_Transport_v5.html` | 1,402 | ✅ 20/20 |
| Construction & Civil | `08d_Construction_v5.html` | 1,474 | ✅ 20/20 |
| Livestock | `08e_Livestock_v5.html` | 1,393 | ✅ 20/20 |
| Government & Defence | `08f_Government_v5.html` | 1,414 | ✅ 20/20 |
| Commercial & General Aviation | `08g_Aviation_v5.html` | 1,392 | ✅ 20/20 |
| Oil & Gas | `08h_Oil_Gas_v5.html` | 1,472 | ✅ 20/20 |

### Audit Rules Checked (20/20 per page)

| Rule | Description |
|------|-------------|
| R1 | No operating hours in live content |
| R2 | No disallowed border-radius (only `0` / `500px` / `var(--radius-*)`) |
| R3 | No CSS gradients (hero photo scrim permitted) |
| R4 | No inline `style=` on body elements |
| R5 | No hero overlay / blue overlay on hero |
| R6 | No word 'depot' in live content |
| R7 | Canonical 5-item nav (Fuel Solutions / Digital Platforms / Industries We Serve / About IOR / Support & Contact) |
| R8 | 6-column footer (Contact / Fuel Solutions / Digital Platforms / Corporate / Quick Actions / Find a Site By State) |
| R9 | Pre-footer 'We're here to help' with CTAs |
| R10 | Proto-bar above nav with Master Index link |
| R11 | No v3.5 hrefs (all old page links replaced with `#` or v5) |
| R12 | Support Hub links use `11_Support_Hubv5.html` |
| R13 | Quick Links bar positioned below hero |
| R14 | No emoji in nav/footer/body links |
| R15 | Footer contains 'Site by ThreePM' |
| R16 | Mobile drawer present |
| R17 | No forms outside modal containers |
| R18 | `btn--pill` / `cs-pill` on permitted elements only *(manual check required — see below)* |
| R19 | Utility/announcement bar present |
| R20 | No placeholder YouTube IDs |

---

## 2. Manual Checks Required

The following items are **not covered by `audit.py`** and require a human visual review:

### 2a. Hero Images (All 9 Pages)
All hero right-split panels currently display a blue dashed `ASSET REQUIRED` placeholder. These must be replaced with final photography before client handoff. See `Asset_Brief_Industries_We_Serve.md` for full specifications.

### 2b. HubSpot Form Embeds (All 9 Pages)
All lead-trap sections contain a grey `HUBSPOT FORM EMBED` placeholder. These must be replaced with live HubSpot embed codes by the integration team.

### 2c. R18 — `btn--pill` Usage (Manual)
`audit.py` does not auto-check R18. Auditor should visually confirm that `btn--pill` and `cs-pill` classes appear only on:
- Primary/secondary CTA buttons in the nav
- Filter pills on list/hub pages

They must **not** appear on body text links, footer links, or breadcrumbs.

### 2d. Section Heading Consistency
The 7 sub-agent-built pages (08a–08g, excluding 08d Construction and 08h Oil & Gas which were built directly) use varied h2 heading labels for equivalent sections. The auditor should check whether the client requires consistent section naming across all industry pages (e.g., "The Why / The How / The What" vs. "The Challenge / Our Process / Our Solutions"). This is a content decision, not a code issue.

| Page | Section 3 Heading | Section 4 Heading | Section 5 Heading |
|------|-------------------|-------------------|-------------------|
| Mining | The How | The What | — |
| Agriculture | The "Why" | The "How" | The "What" |
| Transport | The Challenge | Our Simple Process | Integrated Solutions |
| Construction | The "Why" | The "How" | The "What" (Bento Box) |
| Livestock | How We Help | Our Solutions | — |
| Government | The "Why" | The "How" | The "What" |
| Aviation | Reliable Fuel Supply is Critical | How IOR Supports You | Our Aviation Fuel Services |
| Oil & Gas | The "Why" | The "How" | The "What" (Bento Box) |

### 2e. Cross-Link Verification (Visual)
All 8 sub-pages now link back to `08_Industries_v5.html` (hub) and to 2 sibling industry pages via the Related Content section. Auditor should click through each related card on the live preview to confirm all links resolve correctly.

### 2f. Mobile Responsiveness
The automated audit confirms the mobile drawer is present, but does not test responsive layout. Auditor should check each page at 375px, 768px, and 1280px breakpoints. Key areas to check:
- Industry routing grid (4-col → 2-col → 1-col)
- Stat bar (horizontal → vertical stack)
- Hero split (side-by-side → stacked)

---

## 3. Known Limitations / Out of Scope

- **Oil & Gas page** (`08h_Oil_Gas_v5.html`) does not appear in the Industries Hub routing grid — it is linked from the hub's Related Content section only. If a dedicated card is required, the hub grid needs to be updated from 8 to 9 cards.
- **General Aviation** and **Commercial Aviation** currently share the same page (`08g_Aviation_v5.html`). If these are to be split into two separate pages, a new brief is required.
- **Copy accuracy** has not been independently verified against the source `IOR_Builders_Package_v2.docx`. The auditor should spot-check 2–3 key claims per page against the source document.

---

## 4. Live Preview Links

| Page | URL |
|------|-----|
| Industries Hub | https://alexc-sketch.github.io/ior-prototype-v3-5/08_Industries_v5.html |
| Mining & Resources | https://alexc-sketch.github.io/ior-prototype-v3-5/08a_Mining_v5.html |
| Agriculture & Harvest | https://alexc-sketch.github.io/ior-prototype-v3-5/08b_Agriculture_v5.html |
| Transport & Logistics | https://alexc-sketch.github.io/ior-prototype-v3-5/08c_Transport_v5.html |
| Construction & Civil | https://alexc-sketch.github.io/ior-prototype-v3-5/08d_Construction_v5.html |
| Livestock | https://alexc-sketch.github.io/ior-prototype-v3-5/08e_Livestock_v5.html |
| Government & Defence | https://alexc-sketch.github.io/ior-prototype-v3-5/08f_Government_v5.html |
| Commercial & General Aviation | https://alexc-sketch.github.io/ior-prototype-v3-5/08g_Aviation_v5.html |
| Oil & Gas | https://alexc-sketch.github.io/ior-prototype-v3-5/08h_Oil_Gas_v5.html |
| Master Index | https://alexc-sketch.github.io/ior-prototype-v3-5/00_Master_Index.html |
| Global Components | https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html |

---

## 5. Supporting Files in Repo

| File | Purpose |
|------|---------|
| `Asset_Brief_Industries_We_Serve.md` | Photography requirements for all 9 hero images |
| `audit.py` | Automated 20-rule code audit script |
| `Builder_Brief_INDUSTRIES_WE_SERVE_HUB.md` | Hub page brief |
| `Builder_Brief_MINING_and_RESOURCES.md` | Mining page brief |
| `Builder_Brief_AGRICULTURE_and_HARVEST.md` | Agriculture page brief |
| `Builder_Brief_TRANSPORT_and_LOGISTICS.md` | Transport page brief |
| `Builder_Brief_CONSTRUCTION_and_CIVIL.md` | Construction page brief |
| `Builder_Brief_LIVESTOCK.md` | Livestock page brief |
| `Builder_Brief_GOVERNMENT_and_DEFENCE.md` | Government page brief |
| `Builder_Brief_COMMERCIAL_and_GENERAL_AVIATION.md` | Aviation page brief |
| `Builder_Brief_OIL_and_GAS.md` | Oil & Gas page brief |
