# Auditor Notes: Critical Failure on Find a Location v5

**To:** Builder / Development Team
**From:** Support Auditor Agent
**Date:** April 25, 2026
**Target Page:** [11d_Find_Locationv5.html](https://alexc-sketch.github.io/ior-prototype-v3-5/11d_Find_Locationv5.html)
**Status:** **CRITICAL FAILURE — IMMEDIATE REVISION REQUIRED**

---

## 1. Executive Summary

A critical failure has been identified on the live `11d_Find_Locationv5.html` page. Following the updated brief (which removed the requirement for the mode switcher toggle), a clean comparison of the live page against the brief reveals a significant deviation in the **Below-Map Utility Cards** section.

---

## 2. Critical Failure Identified

### 🚨 Failure: Missing Buttons in Utility Cards
**Brief Requirement (Section 4: Below-Map Utility Cards):**
*   **Card 1 (Fuelcharge App):** Must contain three specific links/buttons:
    *   Button 1: `App Store ↓`
    *   Button 2: `Google Play ↓`
    *   Button 3 (Ghost/Text Link): `Learn More →`
*   **Card 2 (Fleet Account):** Must contain one specific button:
    *   Button: `Apply for an Account →`

**Live Page Status:**
*   **Card 1 (Fuelcharge App):** The live page only has two links: `↓ App Store` and `↓ Google Play`. The third required link, `Learn More →`, is completely missing.
*   **Card 2 (Fleet Account):** The live page has the button `Apply for an Account →`, which is correct.

The omission of the `Learn More →` link on the Fuelcharge card is a critical failure against the approved brief.

---

## 3. Dashboard Status Update

The [Project Status Dashboard](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Dashboard.html) has been reviewed. Here is the current status of relevant pages:

*   **Find a Location v5:** Currently marked as `LIVE`. Notes indicate "Design upgrade PR #78 open".
*   **Contact Us v5 (PR #82):** Awaiting Audit.
*   **Leadership Bio Template v5 (PR #81):** Approved and ready to merge.
*   **HyDip FMS v5 Rebuild (PR #72):** Awaiting Audit.
*   **Support & Contact Hub v5:** Brief Ready, but blocked as Builder 2 has not submitted the PR.

---

## 4. Next Steps for the Builder

1.  **Restore Missing Link:** The `Learn More →` ghost/text link must be added to the Fuelcharge App card in the Below-Map Utility Cards section to comply with the brief.
2.  **Review PR #78:** Ensure the pending design upgrade in PR #78 includes this missing link and does not further deviate from the approved brief requirements.
3.  **Push Fixes:** Commit the corrections to the appropriate branch and notify the Auditor for re-review.
