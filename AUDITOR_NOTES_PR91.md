# Auditor Notes: PR #91 — Support & Contact Hub v5

**To:** Builder / Development Team  
**From:** Support Auditor Agent  
**Date:** 25 Apr 2026  
**PR:** alexc-sketch/ior-prototype-v3-5 #91  
**Branch:** `feature/support-hub-v5` → `main`  
**File:** `11_Support_Hubv5.html`

---

## Verdict: FAIL — 3 Fixes Required

The build is structurally sound and the section inventory is complete. However, 3 issues must be resolved before merge. None are architectural — all are targeted text/attribute changes.

---

## Failures

### Fix 1 — Pre-footer CTA label (R8 / Brand)

**Location:** Line 734  
**Issue:** The second pre-footer CTA reads **"Get in Touch"**. This label is not canonical for the pre-footer band. Per the Global Components reference, the two pre-footer CTAs are **"Apply for an Account"** + **"Contact IOR"** (or a page-appropriate equivalent such as "Contact Us").

"Get in Touch" is acceptable as a body-copy link label, but must not appear as a standalone CTA button — it is too generic and conflicts with the canonical nav CTA set.

**Current:**
```html
<a href="11a_Contact_Usv5.html" class="btn btn--outline-white" aria-label="Contact IOR">Get in Touch <span class="btn__arrow" aria-hidden="true"></span></a>
```

**Required:**
```html
<a href="11a_Contact_Usv5.html" class="btn btn--outline-white" aria-label="Contact IOR">Contact Us <span class="btn__arrow" aria-hidden="true"></span></a>
```

---

### Fix 2 — `lang` attribute (S2 / Structural)

**Location:** Line 2  
**Issue:** The `<html>` element uses `lang="en-AU"`. The canonical value across all prototype pages is `lang="en"`. This is a minor but consistent structural rule — all pages must match.

**Current:**
```html
<html lang="en-AU">
```

**Required:**
```html
<html lang="en">
```

---

### Fix 3 — Footer agency credit (Brand / Whitelist)

**Location:** Line 820  
**Issue:** The footer credit reads `Site by 3PM`. Per the established whitelist, the canonical phrasing is `Site by ThreePM` (to avoid regex false positives in future automated audits). All other v5 pages use "ThreePM".

**Current:**
```html
Site by 3PM
```

**Required:**
```html
Site by ThreePM
```

---

## False Positives Resolved

The automated script flagged 3 additional items that are **not violations** after manual review:

| Flag | Reason Cleared |
|------|---------------|
| R9a/b/c — ior-global.css/js/motion.js not linked | All prototype pages are **self-contained** — CSS and JS are inlined. No external file references are used across any v5 page. This is by design. Not a violation. |
| B3 — Hero eyebrow "SUPPORT & CONTACT" | The eyebrow reads `Support &amp; Contact` (HTML-encoded). The brief spec says "SUPPORT & CONTACT". The CSS applies `text-transform: uppercase` via `.eyebrow` class, so the rendered output is correct. Not a violation. |

---

## Observations (Non-Blocking)

1. **`11c_News_Updates.html`** appears in the mega-nav and mobile drawer (lines 485, 563). This is the v3.5 filename — no v5 equivalent exists yet. This is acceptable as a placeholder link and is consistent with all other pages in the prototype. No action required.

2. **`11f_Policy_Downloadsv5.html`** is referenced in the Secondary Utility Links card (line 719). Note: the actual file on main is `11f_Privacy_Policyv5.html` (Privacy Policy), not a Policy Downloads page. The builder may have intended to link to `11f_Policy_Downloads.html` (the v3.5 downloads page). **Recommend builder confirms** the correct target for this card — it should likely point to `11f_Policy_Downloads.html` until a v5 downloads page is built.

3. **Pre-footer heading** reads "Ready to get started?" — the brief spec says "Ready to get started?" and the Global Components canonical is "Ready to take control of your fuel?" For a support hub page, "Ready to get started?" is contextually appropriate and acceptable. No change required.

---

## What Passed (33/36 checks)

All Golden Rules R1–R8 pass (R8c "Get in Touch" is in the pre-footer, not the nav — see Fix 1). All structural checks pass except `lang`. All brief sections are present and correctly implemented: hero, quick links bar, contact strip (3-col, `var(--ior-blue)`), 2×2 routing grid, secondary utility links, pre-footer, 6-col footer. Operating hours correctly stripped. "Still have questions?" routing box correctly absent.

---

## Required Changes Summary

| # | File | Line | Change |
|---|------|------|--------|
| 1 | `11_Support_Hubv5.html` | 734 | Pre-footer CTA: `Get in Touch` → `Contact Us` |
| 2 | `11_Support_Hubv5.html` | 2 | `lang="en-AU"` → `lang="en"` |
| 3 | `11_Support_Hubv5.html` | 820 | `Site by 3PM` → `Site by ThreePM` |

**Builder: apply all 3 fixes on the same branch (`feature/support-hub-v5`) and push. No new PR required — I will re-audit on the updated branch.**
