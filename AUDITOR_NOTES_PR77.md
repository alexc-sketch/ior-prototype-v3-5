# Auditor Notes: Find a Location v5 (PR #77)

**To:** Builder / Development Team
**From:** Support Auditor Agent
**Date:** April 25, 2026
**Target PR:** [PR #77 — feat: 11d_Find_Locationv5.html](https://github.com/alexc-sketch/ior-prototype-v3-5/pull/77)
**Status:** **FAIL — REVISIONS REQUIRED**

---

## 1. Executive Summary

The new Find a Location v5 page (`11d_Find_Locationv5.html`) successfully implements the Storepoint map embed, the mode switcher, and the PDF download strip. The page structure is sound, and it passes all 9 Golden Rules and all 8 of the builder's QA checks.

However, the PR **fails** the audit due to a regression in the Master Index (`00_Master_Index.html`). The builder's notes state "No change (card already in main from previous push)", but the PR diff shows that the `11d_Find_Locationv5.html` card was actually **removed** and reverted back to the old `11d_Find_Location.html` card. The merge is blocked until the Master Index is corrected.

---

## 2. Golden Rules & QA Audit Results

| Rule | Category | Status | Auditor Notes |
| :--- | :--- | :--- | :--- |
| **R1** | Design | **PASS** | No rounded corners found. `border-radius: 0` is correctly applied. |
| **R2** | Design | **PASS** | No gradients or blue overlays detected. |
| **R3** | Design | **PASS** | No inline `style="..."` attributes found in the HTML body. |
| **R4** | Design | **PASS** | Hero background uses `var(--ior-navy)` correctly. |
| **R5** | Content | **PASS** | No operating hours found anywhere on the page or in the footer. |
| **R6** | Content | **PASS** | The banned word "depot" is not used anywhere in the file. |
| **R7** | Components | **PASS** | All global components (Utility Bar, Primary Nav, Mobile Drawer, Global Footer) are present. |
| **R8** | Components | **PASS** | Nav CTAs correctly use the `.btn--pill` class. |
| **R9** | Components | **PASS** | Protected core files remain untouched. |

---

## 3. UX & Dev QC Observations

### A. Structural Validation (Dev QC)
*   **`<main>` Nesting:** **PASS**. The `<main>` element is correctly nested outside the mobile drawer.
*   **Quick Links Bar:** **PASS**. The Quick Links Bar is present and correctly configured without `position: sticky`.

### B. Brief Compliance
*   **Storepoint Map:** **PASS**. The embed token `169b243d6de664` is present.
*   **Mode Switcher:** **PASS**. The Ground Fuels and Aviation tab buttons are present.
*   **Utility Cards:** **PASS**. Both the Fuelcharge and Fleet Account cards are present.
*   **Download Strip:** **PASS**. Both the Diesel and Aviation PDF download links are present and point to the correct filenames.
*   **FAQ Accordion:** **PASS**. The 4 required FAQ questions are present.

### C. Master Index Protocol (FAIL)
*   **Card Regression:** The PR diff shows that the `11d_Find_Locationv5.html` card (with the `v5 — In Review` badge) was removed from `00_Master_Index.html`, and the old `11d_Find_Location.html` card (with the `Pending` badge) was restored. This is a regression. The Master Index must point to the new v5 file.

---

## 4. Required Fixes for Merge Approval

Please implement the following correction and push to the `feature/find-location-v5` branch:

1.  **Update Master Index:** Revert the regression in `00_Master_Index.html`. Ensure the card for Find a Location points to `11d_Find_Locationv5.html` and displays the `<span class="badge b-review">v5 — In Review</span>` badge.

Once this change is pushed, the Auditor will approve the merge.
