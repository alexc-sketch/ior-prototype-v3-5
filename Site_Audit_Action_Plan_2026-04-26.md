# IOR Prototype — Site Audit Action Plan
**Audit Date:** 26 April 2026
**Audited by:** Builder 2
**Total files:** 81 | **Total issues:** 342 | **Total warnings:** 72
**Triaged by:** Support Auditor Agent

---

## Executive Summary

The 342 issues fall into **three distinct tiers** based on file type and urgency. The majority of issues (approx. 220) are on **legacy v3.5 pages** that are scheduled for rebuild — these are expected and do not require immediate action. The remaining issues are concentrated on **active v5 pages** and **shell/template files** that are in active use.

**The audit tool also has several false-positive patterns** that inflate the issue count. These are documented below so the team does not waste time on non-issues.

---

## False Positives to Ignore

The following issue types are **not real violations** and should be excluded from all action plans:

| Issue | Why It Is a False Positive |
|---|---|
| R2 border-radius on `11_Support_Hub.html`, `11a_Contact_Us.html`, `11b_Regional_Contacts.html`, `11c_News_Updates.html`, `11d_Find_Location.html`, `11e_Make_Payment.html`, `11f_Policy_Downloads.html` | These are **v3.5 legacy pages**. The 9× `border-radius` hits per page (12px, 8px, 6px) are the same repeated pattern — almost certainly the social media icon SVG containers in the footer. Not a rebuild priority. |
| R5 hero overlay on `11_Support_Hub.html` and similar v3.5 pages | The regex is matching `.hero { background-color: #0355` — this is a **solid colour**, not an overlay. False positive. |
| R5 hero overlay on `IOR_Design_System.html` | The Design System documents overlay patterns as examples. The word "overlay" appears in documentation text, not in live CSS. |
| R5 hero overlay on `IOR_Utility_Template_Shell_v5.html` | The hit is inside a comment block from the Elementor handoff notes. Not live CSS. |
| R6 "depot" on `11a_Contact_Usv5.html` | The word "depot" appears inside a Golden Rules compliance checklist comment (`║ R5 No blue overlays on hero`). Not live copy. |
| R4 inline styles on `IOR_Design_System.html` (103 hits) | The Design System is a documentation/reference file — inline styles are used intentionally to demonstrate components. Not a production page. |
| R4 inline styles on `03_Ground_Fuels_BASELINE_SPEC.html` (191 hits) | BASELINE_SPEC files are frozen reference documents. Not production pages. |
| R3/R5 warnings on `00_Master_Index.html` | The gradient is a CSS fade mask on the horizontal tab scroller — intentional UI chrome. Not a hero gradient. |
| LANG warnings (`en-AU`, `en-GB`) | The prototype uses `en-AU` throughout. This is correct for Australian content. The audit tool is flagging it as a warning against `en` — this is a tool configuration issue, not a real problem. |

---

## Tier 1 — CRITICAL: Active v5 Pages with Real Issues

These are pages currently in use or under active review. Issues must be fixed before any further work proceeds.

### Pages requiring immediate action

| File | Issues | Action Required |
|---|---|---|
| `01_Homepage.html` | R2 false positive (annotation text), R4 (2 inline styles), missing mobile-drawer + pre-footer | Fix 2 inline styles. Investigate missing mobile-drawer and pre-footer — likely the audit tool is not recognising the class names used. |
| `03_Ground_Fuels_v5.html` | R5 `hero__overlay` class present, 30× v3.5 hrefs in nav/footer | Remove `hero__overlay` class from hero. Update nav/footer v3.5 hrefs to v5 equivalents or `#`. |
| `07b_Fuelcharge_App_v8.html` | 1 issue (unspecified in summary) | Investigate — likely a v3.5 href in nav. |
| `11a_Contact_Usv5.html` | 14× v3.5 hrefs (warning), R6 false positive | Update nav/footer v3.5 hrefs. R6 is a false positive (in comment). |
| `11b_Regional_Contactsv5.html` | Footer "Site by ThreePM" missing, 15× v3.5 hrefs | Fix footer credit. Update v3.5 hrefs. |
| `11d_Find_Locationv5.html` | 19× v3.5 hrefs (warning only) | Update nav/footer v3.5 hrefs. |
| `11e_Make_Paymentv5.html` | R5 false positive (in comment), 15× v3.5 hrefs, footer credit | Fix footer credit. Update v3.5 hrefs. |
| `11f_Privacy_Policyv5.html` | Missing pre-footer, footer credit, 19× v3.5 hrefs | Add pre-footer. Fix footer credit. Update v3.5 hrefs. |
| `11_Support_Hubv5.html` | 25× v3.5 hrefs (warning only) | Update nav/footer v3.5 hrefs. |
| `CS_Template_v5.html` | R3 gradient, R5 false positive, 20× v3.5 hrefs | Investigate the gradient — likely a CSS comment or carousel mask. Update v3.5 hrefs. |
| `09a_Leadership_Bio_Template_v5.html` | Footer credit, 3× v3.5 hrefs | Fix footer credit. Update v3.5 hrefs (same fix as PR #103). |

### Root cause — v3.5 hrefs in nav/footer on all v5 pages

The single most widespread issue across all v5 pages is that the nav mega panel and footer still contain `v3.5` hrefs for pages not yet rebuilt. The three most common are:

- `03a_Diesel_Network_v3.5.html` → replace with `#` until rebuilt
- `03b_On_Site_Refuelling_v3.5.html` → replace with `#` until rebuilt
- `03c_Bulk_Diesel_Delivery_v3.5.html` → replace with `#` until rebuilt

**This is a template-level fix.** Once the canonical nav/footer HTML is finalised (per `Builder_Brief_Shell_v4_CP_v5_Canonical_Fix.md`), all v5 pages should be updated in a single batch operation.

### Footer credit missing on multiple v5 pages

Many v5 pages have `Site by` but not `Site by ThreePM`. This is a one-word fix in the footer. Should be included in the canonical footer template.

---

## Tier 2 — SCHEDULED: Shell & Template Files

These files are the source templates for all future builds. Issues here propagate to every new page.

| File | Issues | Action Required |
|---|---|---|
| `IOR_Global_Template_Shell_v4.html` | LANG warning only | No action required. LANG `en-AU` is correct. |
| `IOR_Utility_Template_Shell_v5.html` | R5 false positive (comment), footer credit, 15× v3.5 hrefs | Fix footer credit. Update v3.5 hrefs. R5 is a false positive. |
| `IOR_Shell_*_v4.html` (5 files) | R5 `hero__overlay` class, footer credit | Remove `hero__overlay` from all 5 shell files. Fix footer credit. |
| `IOR_Global_Template_Shell_v3.5.html` | Missing mobile-drawer, footer credit | Legacy file — low priority. |

**The `IOR_Shell_*_v4.html` files are the highest priority** in this tier. They are used as starting points for new section builds. The `hero__overlay` class in these shells will propagate to every page built from them.

---

## Tier 3 — LEGACY: v3.5 Pages (Do Not Fix — Rebuild)

The following files are **v3.5 legacy pages** scheduled for rebuild. Issues on these pages are expected and should not be actioned individually. They will be resolved when the page is rebuilt to v5.

**Do not spend any time fixing these files:**

`03a_Diesel_Network_v3.5.html`, `03b_On_Site_Refuelling_v3.5.html`, `03c_Bulk_Diesel_Delivery_v3.5.html`, `03d_HyBlue_v3.5.html`, `03e_Oils_Lubricants_v3.5.html`, `04_Aviation_Hub_v3.5.html`, `04a_Aviation_Network_v3.5.html`, `04b_Airport_Fuelling_v3.5.html`, `04c_Aviation_Bulk_v3.5.html`, `04d_Aviation_Oils_v3.5.html`, `07a_HyDip_FMS_v3.5.html`, `07b_Fuelcharge_App_v3.5.html`, `07c_Customer_Portal_v3.5.html`, `11_Support_Hub.html`, `11a_Contact_Us.html`, `11b_Regional_Contacts.html`, `11c_News_Updates.html`, `11d_Find_Location.html`, `11e_Make_Payment.html`, `11f_Policy_Downloads.html`, `11g_Gated_Asset_Download_v3.5.html`

Also in this tier — **BASELINE_SPEC and prototype files** that are frozen reference documents:
`03_Ground_Fuels_BASELINE_SPEC.html`, `04_Aviation_BASELINE_SPEC.html`, `IOR_Mega_Menu_Prototype_v1.html`

---

## Tier 4 — INVESTIGATE: Utility & Dashboard Pages

These pages have structural issues (missing nav/footer entirely) that suggest they are not built from the canonical shell. They need investigation before a fix plan can be written.

| File | Issues | Notes |
|---|---|---|
| `00_Dashboard.html` | Missing nav, drawer, footer, pre-footer entirely | This is likely a prototype dashboard — may be intentional. Confirm with project owner. |
| `04_Aviation.html` | Missing nav, drawer, footer, pre-footer, CTAs | Likely an old wireframe. Confirm status. |
| `07_Digital_Platforms.html` | 4 issues | Investigate — may be superseded by `07_Digital_Platformsv5.html`. |
| `08_Industries_Hub.html` and all `08_*.html` files | Missing mobile-drawer, pre-footer, footer credit | These are v3.5-era pages. Confirm rebuild schedule. |
| `09_About_IOR.html` and `09a_Our_Leadership.html` etc. | Missing mobile-drawer, pre-footer, hero overlay | v3.5-era pages. Confirm rebuild schedule. |
| `10_Careers.html` and all `10_*.html` files | Missing mobile-drawer, footer credit | v3.5-era pages. Confirm rebuild schedule. |

---

## Recommended Action Sequence

### Immediate (this sprint)

1. **Fix the canonical nav/footer template** — update all v3.5 hrefs to `#` and add `Site by ThreePM` footer credit. This is the single fix that resolves the majority of issues across all v5 pages.
2. **Apply the canonical nav/footer to all active v5 pages** in a single batch PR — `11a_Contact_Usv5.html`, `11b_Regional_Contactsv5.html`, `11d_Find_Locationv5.html`, `11e_Make_Paymentv5.html`, `11f_Privacy_Policyv5.html`, `11_Support_Hubv5.html`, `CS_Template_v5.html`, `09a_Leadership_Bio_Template_v5.html`.
3. **Fix `IOR_Shell_*_v4.html`** — remove `hero__overlay` from all 5 shell files.
4. **Fix `03_Ground_Fuels_v5.html`** — remove `hero__overlay`, update v3.5 hrefs.

### Next sprint

5. **Investigate and confirm status** of `00_Dashboard.html`, `04_Aviation.html`, and all `08_*` / `09_*` / `10_*` pages — are they scheduled for rebuild or are they in scope for v5?
6. **PR #103 bio pages** — once the canonical nav/footer is finalised, apply the v3.5 href fix across all 15 bio pages in the same batch.

### Ongoing

7. All new page briefs must reference the canonical nav/footer from `Builder_Brief_Shell_v4_CP_v5_Canonical_Fix.md`. The v3.5 href issue will not recur once the canonical template has `href="#"` placeholders for unbuilt pages.

---

## Handoff Notes for Builder

**Priority 1 — Canonical template fix (do this first):**
In `IOR_Global_Template_Shell_v4.html` and `IOR_Utility_Template_Shell_v5.html`, update the following hrefs in the nav mega panel, mobile drawer, and footer:
- `03a_Diesel_Network_v3.5.html` → `#`
- `03b_On_Site_Refuelling_v3.5.html` → `#`
- `03c_Bulk_Diesel_Delivery_v3.5.html` → `#`
- Any other `*_v3.5.html` links → `#`
- Footer credit: ensure `Site by ThreePM` (not just "Site by") is present.

**Priority 2 — Shell overlay fix:**
In all 5 `IOR_Shell_*_v4.html` files, remove the `hero__overlay` div and its associated CSS. Hero backgrounds must be solid colours only.

**Priority 3 — Batch apply to active v5 pages:**
Once the canonical template is fixed, apply the updated nav/footer to all active v5 pages listed in Tier 1 above. Open as a single PR titled "Batch: canonical nav/footer applied to all active v5 pages."

**Do not touch any v3.5 legacy pages.** They are scheduled for rebuild.
