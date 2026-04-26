# Auditor Notes: Leadership Bio Template v5

**To:** Development Team
**From:** Support Auditor Agent
**Date:** April 25, 2026
**Target File:** `09a_Leadership_Bio_Template_v5.html`
**Status:** CHANGES REQUESTED — CRITICAL FAILURES DETECTED

## 1. Executive Summary

I have reviewed the live `09a_Leadership_Bio_Template_v5.html` page against the original v5 brief. While the core bio layout and ACF placeholders are present, there are two critical failures related to the global components that must be fixed immediately.

**Live Environment Link:** [09a_Leadership_Bio_Template_v5.html](https://alexc-sketch.github.io/ior-prototype-v3-5/09a_Leadership_Bio_Template_v5.html)

## 2. Critical Failures Identified

### A. Incorrect Primary Nav CTAs (Cascading Failure)
The primary navigation bar is currently displaying a single **"Get in Touch"** button.
*   **The Brief Requirement:** The page must inherit the correct v4 Global Header.
*   **The Canonical Spec:** As documented in the [Global Components](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html) reference, the primary nav must feature two distinct buttons: **Customer Login** (outline pill) and **Apply for an Account** (primary pill).
*   **Required Fix:** Update the header to use the correct dual-CTA structure. (Note: This fix has already been applied to the `IOR_Global_Template_Shell_v4.html` via PR #84, so you may simply need to pull the latest shell updates into your branch).

### B. Incorrect "Related Content" Grid
The "Latest from IOR" section below the bio is currently displaying a static 3-column grid of Case Studies.
*   **The Brief Requirement:** Section 3 of the brief explicitly states: *"CRITICAL UPDATE: The v3.5 prototype uses an outdated and broken blog grid container. You MUST delete the old version. Replacement: Inject the correct Related Content — Tabbed Grid from 00_Global_Components.html#related-content."*
*   **The Canonical Spec:** The grid must be a **Tabbed Grid** with toggle buttons for "Case Studies" and "Blog Posts", exactly as it appears in the [Global Components](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html) file.
*   **Required Fix:** Delete the current static grid and replace it with the interactive Tabbed Grid component.

## 3. Next Steps

1.  Pull the latest `main` branch to inherit the corrected Global Shell v4 nav CTAs.
2.  Replace the static Related Content grid with the canonical Tabbed Grid from the Global Components file.
3.  Push the fixes to your feature branch and notify the Auditor for re-review.

Please ensure all future builds strictly reference the canonical components at [https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html](https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html).
