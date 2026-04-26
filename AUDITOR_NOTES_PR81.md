# Auditor Notes: Leadership Bio Template v5 (PR #81)

**To:** Builder / Development Team
**From:** Support Auditor Agent
**Date:** April 25, 2026
**Target PR:** [PR #81 — feat: Leadership Bio Template v5](https://github.com/alexc-sketch/ior-prototype-v3-5/pull/81)
**Status:** **FAIL — REVISIONS REQUIRED**

---

## 1. Executive Summary

The builder has successfully implemented the Leadership Bio Template (`09a_Leadership_Bio_Template_v5.html`) based on the Global Shell v4. The component flow matches the brief, the ACF placeholder comments are correctly implemented, and the Master Index has been updated with the new 15-card Leadership Bios section.

However, the PR fails the audit on one specific Golden Rule violation.

---

## 2. Audit Findings

### 🚨 R5 Violation: Operating Hours Text
The builder's QA notes state "No operating hours anywhere", but the automated audit detected a violation in the global footer:
*   **Line 752:** `<a href="#" class="footer-legal__link">Site by 3PM</a>`

The string "3PM" triggers the strict regex check for operating hours/time schedules. While this is a credit link and not actual operating hours, it violates the strict "no time references" rule.

**Required Fix:** Rephrase the credit link to avoid the "PM" string (e.g., "Site by ThreePM" or remove the credit entirely if not required by the design system).

---

## 3. Verification Checklist

| Check | Status | Auditor Notes |
| :--- | :--- | :--- |
| **R1 (border-radius)** | **PASS** | No rounded corners found. |
| **R2 (No gradients)** | **PASS** | No gradients found. |
| **R3 (No inline styles)** | **PASS** | No inline styles found in the body. |
| **R4 (Hero background)** | **PASS** | No video, no rgba overlay. Pre-footer correctly uses `--ior-navy`. |
| **R5 (No operating hours)** | **FAIL** | "3PM" found in footer credit link. |
| **R6 (No banned words)** | **PASS** | "depot" is not used. |
| **R7 (Global components)** | **PASS** | Utility bar, primary nav, mobile drawer, and 6-col footer are intact. |
| **R8 (Nav CTA)** | **PASS** | Uses `.btn--pill`. |
| **R9 (Protected files)** | **PASS** | No global CSS/JS files modified. |
| **Brief Compliance** | **PASS** | All 5 sections present. ACF placeholders and conditional comments are correct. |
| **Master Index** | **PASS** | Leadership Bios section added with 15 cards (1 template + 14 leaders) and `b-review` badges. |
| **Structural Nesting** | **PASS** | `<main>` element correctly nested outside the mobile drawer. |

---

## 4. Next Steps for the Builder

1.  **Fix the R5 Violation:** Update the "Site by 3PM" text in the footer of `09a_Leadership_Bio_Template_v5.html` to remove the "PM" string.
2.  **Push the Fix:** Commit the change to the `feature/leadership-bio-v5` branch.
3.  **Notify Auditor:** The PR will be re-audited and approved for merge once this single issue is resolved.
