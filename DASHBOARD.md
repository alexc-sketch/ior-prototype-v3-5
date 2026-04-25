# IOR Prototype v5 — Project Status Dashboard

**Last Updated:** April 25, 2026
**Purpose:** A single source of truth for all builders and auditors to track what has been built, what is in review, and what is approved.

---

## 🟢 APPROVED & MERGED (Live on `main`)

These pages have passed all audits and are live. Do not modify these without a new brief.

| Page | File | Notes |
|---|---|---|
| **Regional Contacts v5** | `11b_Regional_Contactsv5.html` | Interactive SVG map, canonical footer |
| **Find a Location v5** | `11d_Find_Locationv5.html` | Storepoint map, mode switcher, download strip |
| **Make a Payment v5** | `11e_Make_Paymentv5.html` | AMEX & Visa/MC gateway cards, EFT details |
| **Privacy Policy v5** | `11f_Privacy_Policyv5.html` | Ultra-minimal utility shell, no pre-footer |

---

## 🟡 IN REVIEW (Open Pull Requests)

These PRs are currently awaiting audit. **Auditors:** Please review these next.

| PR | Feature | Branch | Status |
|---|---|---|---|
| **#81** | Leadership Bio Template v5 | `feature/leadership-bio-v5` | **Audit Complete — Ready to Merge** |
| **#80** | Regional Contacts v5 (Footer Fix) | `fix/11b-regional-contacts-global-footer` | Awaiting Audit |
| **#79** | Docs: Leadership Bio Brief | `feature/leadership-bio-brief` | Awaiting Audit |
| **#78** | Find a Location v5 (Design Upgrade) | `feature/find-location-v5-upgrade` | Awaiting Audit |
| **#72** | HyDip FMS v5 Rebuild | `feature/hydip-v5` | Awaiting Audit |

---

## 🔴 PENDING BUILD (Briefs Written, Awaiting PR)

These pages have approved briefs committed to the repo, but no builder has submitted a PR yet. **Builders:** Pick these up next.

| Page | Brief File | Target HTML File |
|---|---|---|
| **Support & Contact Hub v5** | `Builder_Brief_Support_Hub_v5.md` | `11_Support_Hubv5.html` |
| **Contact Us v5** | `Builder_Brief_Contact_Us_v5.md` | `11a_Contact_Usv5.html` |
| **Case Study Template v5** | `Builder_Brief_Case_Study_Template_v5.md` | `CS_Template_v5.html` |

---

## ⚠️ KNOWN ISSUES & BLOCKERS

1. **Support Hub v5 Confusion:** Builder 2 referenced PR #10 for the Support Hub v5 build. PR #10 was an old v3 build and has been closed. **Builder 2 must submit a new PR with `11_Support_Hubv5.html`.**
2. **Master Index Conflicts:** Builders must rebase their branches onto `main` before opening a PR to ensure they don't overwrite recent Master Index additions (like the Case Studies section).

---

*Note: This dashboard should be updated by the Auditor after every merge or new brief creation.*
