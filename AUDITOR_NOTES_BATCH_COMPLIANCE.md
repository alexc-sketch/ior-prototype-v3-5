# Auditor Notes: Pre-PR Batch Compliance Audit

**To:** Builder 2 / Development Team  
**From:** Support Auditor Agent  
**Date:** April 25, 2026  
**Target:** All HTML pages in `ior-prototype-v3-5` repository  

---

## 1. Executive Summary

Thank you for the update on the batch fix operation. Before you open your Pull Request, I have run a comprehensive compliance audit across all 65 HTML pages in the repository (excluding canonical shells and protected files).

The audit checked two specific criteria against the canonical `IOR_Global_Template_Shell_v4.html` spec:
1.  **Nav CTAs:** Must contain dual CTAs ("Customer Login" + "Apply for an Account") with correct `.btn--pill` classes.
2.  **Footer CSS:** The `.site-footer` CSS block must use `background: var(--ior-blue)` and the `.footer-nav-grid` must use `grid-template-columns: repeat(6, 1fr)`.

### Current Audit Results
*   **Total Pages Checked:** 65
*   **Nav CTAs:** 16 PASS / 48 FAIL or WARN
*   **Footer CSS:** 35 PASS / 29 FAIL

---

## 2. Key Findings & Required Fixes

### A. The "Get in Touch" Remnant (Nav CTAs)
The most common failure (39 pages) is that the old single "Get in Touch" button is still present in the `.nav-ctas` block. Your fix script needs to ensure it completely replaces the inner HTML of the `.nav-ctas` div with the dual canonical buttons.

**Example failing pages:**
*   `03_Ground_Fuels_v5.html`
*   `07_Digital_Platforms_v4.html`
*   `11b_Regional_Contactsv5.html`
*   All 5 `IOR_Shell_*_v4.html` industry shells

### B. The Missing Pill Class (Nav CTAs)
Several pages (9 pages) have the correct "Customer Login" and "Apply for an Account" text, but the buttons are missing the `.btn--pill` class (and sometimes `.btn--outline`).

**Example failing pages:**
*   `01_Homepage.html`
*   `02_Fuel_Solutions_Hub.html`
*   `03_Ground_Fuels.html`
*   All 6 `10_*` Careers pages

### C. The Legacy Footer CSS (Footer)
While you noted that the footer HTML was replaced correctly, 29 pages still have legacy footer CSS in their `<style>` blocks. These pages are failing because their `.site-footer` background is set to `#0A1929` or `var(--ior-navy)`, and their grid is not `repeat(6, 1fr)`.

**Example failing pages:**
*   `11_Support_Hub.html`
*   `11a_Contact_Us.html`
*   `11d_Find_Location.html`
*   `07a_HyDip_FMS_v3.5.html`

---

## 3. Next Steps for the Builder

1.  **Refine your fix script:** Ensure it targets the `.site-footer` and `.footer-nav-grid` CSS blocks specifically, as the comment structures vary across older pages.
2.  **Run your batch fix:** Apply the fixes across all failing pages.
3.  **Open the PR:** Once you are confident the fixes are applied, push to your branch and open the PR. I will re-run this exact audit script against your PR branch to verify compliance before approving the merge.

We look forward to reviewing the clean batch PR!
