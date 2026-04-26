# Auditor Notes: Critical Failure on Find a Location v5

**To:** Builder / Development Team
**From:** Support Auditor Agent
**Date:** April 25, 2026
**Target Page:** [11d_Find_Locationv5.html](https://alexc-sketch.github.io/ior-prototype-v3-5/11d_Find_Locationv5.html)
**Status:** **CRITICAL FAILURE — IMMEDIATE REVISION REQUIRED**

---

## 1. Executive Summary

A critical failure has been identified on the live `11d_Find_Locationv5.html` page. While the Storepoint map embed and FAQ sections are present, the page deviates significantly from the approved brief in the Hero section and the Map Toggles.

Additionally, the Dashboard (`00_Dashboard.html`) notes that the "Mode switcher removed" and a "Design upgrade PR #78 open" is pending. The live page must be brought back into compliance with the brief.

---

## 2. Critical Failures Identified

### 🚨 Failure 1: Hero Section Buttons
**Brief Requirement:**
*   Button 1 (Primary): `Apply Now`
*   Button 2 (Outline): `Register Your Interest`

**Live Page Status:**
*   The live page currently has two buttons: `Apply Now` and `Register Your Interest`. This appears to match the brief, but the Dashboard notes a "hybrid hero" design upgrade is pending in PR #78.

### 🚨 Failure 2: Map Toggles / Mode Switcher
**Brief Requirement:**
*   Map Toggles / Tabs (Above Map): `Ground Fuels` and `Aviation`

**Live Page Status:**
*   The live page **does not have** the required `Ground Fuels` and `Aviation` mode switcher tabs above the map. The Dashboard explicitly notes "Mode switcher removed" for this page. This is a critical deviation from the brief.

---

## 3. Dashboard Status Update

The [Project Status Dashboard](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Dashboard.html) has been reviewed. Here is the current status of relevant pages:

*   **Find a Location v5:** Currently marked as `LIVE`, but notes indicate "Mode switcher removed" and "Design upgrade PR #78 open".
*   **Contact Us v5 (PR #82):** Awaiting Audit.
*   **Leadership Bio Template v5 (PR #81):** Approved and ready to merge.
*   **HyDip FMS v5 Rebuild (PR #72):** Awaiting Audit.
*   **Support & Contact Hub v5:** Brief Ready, but blocked as Builder 2 has not submitted the PR.

---

## 4. Next Steps for the Builder

1.  **Restore Mode Switcher:** The `Ground Fuels` and `Aviation` mode switcher tabs must be restored above the Storepoint map on `11d_Find_Locationv5.html` to comply with the brief.
2.  **Review PR #78:** Ensure the pending design upgrade in PR #78 does not further deviate from the approved brief requirements.
3.  **Push Fixes:** Commit the corrections to the appropriate branch and notify the Auditor for re-review.
