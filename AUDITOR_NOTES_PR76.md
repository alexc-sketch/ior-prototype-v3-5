# Auditor Notes: Privacy Policy v5 (PR #76)

**To:** Builder / Development Team
**From:** Support Auditor Agent
**Date:** April 25, 2026
**Target PR:** [PR #76 — feat: 11f_Privacy_Policyv5.html](https://github.com/alexc-sketch/ior-prototype-v3-5/pull/76)
**Status:** **FAIL — REVISIONS REQUIRED**

---

## 1. Executive Summary

The new Privacy Policy v5 page (`11f_Privacy_Policyv5.html`) successfully implements the ultra-minimal utility shell design and includes the full approved legal copy. The page correctly omits the Quick Links Bar and FAQ accordion as specified in the brief.

However, the PR **fails** the audit on two critical structural counts: the `<main>` element is missing entirely, and the pre-footer CTA band was not removed. Additionally, the Master Index was not updated in the PR diff. The merge is blocked until these issues are resolved.

---

## 2. Golden Rules & QA Audit Results

| Rule | Category | Status | Auditor Notes |
| :--- | :--- | :--- | :--- |
| **R1** | Design | **PASS** | No rounded corners found. `border-radius: 0` is correctly applied. |
| **R2** | Design | **PASS** | No gradients or blue overlays detected. |
| **R3** | Design | **PASS** | No inline `style="..."` attributes found in the HTML body. |
| **R4** | Design | **PASS** | Hero background uses `var(--ior-navy)` correctly. |
| **R5** | Content | **PASS** | No operating hours found in the global footer. |
| **R6** | Content | **PASS** | The banned word "depot" is not used anywhere in the file. |
| **R7** | Components | **PASS** | All global components (Utility Bar, Primary Nav, Mobile Drawer, Global Footer) are present. |
| **R8** | Components | **PASS** | Nav CTAs correctly use the `.btn--pill` class. |
| **R9** | Components | **PASS** | Protected core files remain untouched. |

---

## 3. UX & Dev QC Observations

### A. Structural Validation (Dev QC)
*   **`<main>` Element Missing (FAIL):** The `<main id="main-content">` tag is completely missing from the document. The `<section class="utility-hero">` and `<section class="legal-section">` must be wrapped inside a `<main>` element, which should sit immediately after the mobile drawer closing tags.

### B. Brief Compliance (Ultra-Minimal Shell)
*   **No Quick Links Bar:** **PASS**. The Quick Links Bar has been correctly removed.
*   **No FAQ Accordion:** **PASS**. The FAQ accordion has been correctly removed.
*   **No Pre-footer (FAIL):** The pre-footer CTA band is still present in the document. The brief explicitly requested an ultra-minimal shell with "no pre-footer". This section must be removed.
*   **Legal Content:** **PASS**. The Privacy Act and Australian Privacy Principles references are present.

### C. Master Index Protocol
*   **Card Addition (FAIL):** The Master Index (`00_Master_Index.html`) was not updated in this PR diff. A new card for `11f_Privacy_Policyv5.html` must be added to the Master Index with an `IN REVIEW` badge.

---

## 4. Required Fixes for Merge Approval

Please implement the following corrections and push to the `feature/privacy-policy-v5` branch:

1.  **Structural Nesting:** Add the missing `<main id="main-content">` tag. It should open after the mobile drawer `</nav>` and close before the global `<footer>`.
2.  **Remove Pre-footer:** Delete the pre-footer CTA band section to comply with the ultra-minimal shell brief.
3.  **Update Master Index:** Add a new card for `11f_Privacy_Policyv5.html` to `00_Master_Index.html` and ensure it has the `<span class="badge b-review">v5 — In Review</span>` status visual.

Once these changes are pushed, the Auditor will re-run the checks.
