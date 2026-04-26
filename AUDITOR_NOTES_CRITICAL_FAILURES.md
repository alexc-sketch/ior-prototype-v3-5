# Auditor Notes: Critical Failures Report

**To:** Builder 2 / Development Team
**From:** Support Auditor Agent
**Date:** April 25, 2026
**Status:** CRITICAL FAILURES DETECTED — IMMEDIATE ACTION REQUIRED

---

## 1. Executive Summary

A comprehensive audit of the live prototype environment has revealed a cascading structural failure originating from the `IOR_Global_Template_Shell_v4.html` file, alongside isolated failures on the Contact Us v5 page and the Master Index.

Because all spoke pages inherit their global components from the shell files, the incorrect navigation CTAs in the Global Shell v4 have propagated across the entire prototype.

The Auditor has proactively applied the necessary fixes to the core files in a new PR. You must review and merge these fixes immediately, and then regenerate any affected spoke pages.

---

## 2. Critical Failure 1: Incorrect Primary Nav CTAs

**Affected File:** `IOR_Global_Template_Shell_v4.html` (and all derived pages)
**Severity:** CRITICAL (Cascading)

**The Issue:**
The primary navigation in the Global Shell v4 was using a single `"Get in Touch"` button. This violates the canonical Figma specification documented in `00_Global_Components.html`, which strictly requires two specific pill buttons:
1.  **Customer Login** (Outline Pill)
2.  **Apply for an Account** (Primary Pill)

**The Fix Applied:**
The Auditor has updated the `<div class="nav-ctas">` block in `IOR_Global_Template_Shell_v4.html` to match the exact Figma specification.

**Required Action for Builder:**
Because this shell file is the source of truth, **every single page** that was built using the old shell must have its `<header>` block updated to match the new canonical nav CTAs.

---

## 3. Critical Failure 2: Incorrect Footer on Contact Us v5

**Affected File:** `11a_Contact_Usv5.html`
**Severity:** HIGH

**The Issue:**
The `11a_Contact_Usv5.html` page is using an incorrect, legacy footer variant. It does not match the canonical 6-column footer found in `IOR_Global_Template_Shell_v4.html`.

**Required Action for Builder:**
You must replace the entire `<footer>` block in `11a_Contact_Usv5.html` with the canonical footer from `IOR_Global_Template_Shell_v4.html`. The footer must use the `var(--ior-blue)` background and the `repeat(6, 1fr)` grid layout.

---

## 4. Critical Failure 3: Missing Utility Shell v5 in Master Index

**Affected File:** `00_Master_Index.html`
**Severity:** MEDIUM

**The Issue:**
The `IOR_Utility_Template_Shell_v5.html` file exists and is being used as the base for pages like the Support Hub and Regional Contacts, but it is completely missing from the Master Index.

**The Fix Applied:**
The Auditor has added a new card for `IOR_Utility_Template_Shell_v5.html` to the "Templates & Shells" section of the Master Index, ensuring it is visible and accessible for QA.

---

## 5. Next Steps

1.  Review the Auditor's PR containing the fixes for the Global Shell v4 nav CTAs and the Master Index.
2.  Merge the PR to `main`.
3.  Open a new PR to fix the footer on `11a_Contact_Usv5.html`.
4.  Audit all other live pages to ensure they are using the updated nav CTAs from the new Global Shell v4.
