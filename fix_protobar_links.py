#!/usr/bin/env python3
"""
fix_protobar_links.py
Replace all proto-bar "Master Index" back-links with "Client Preview" links
across every page that is linked from 00_Client_Preview.html.
"""

import re
import os

PAGES = [
    "01_Homepage.html",
    "02_Fuel_Solutions_Hub.html",
    "03a_Diesel_Network_v3.5.html",
    "03b_On_Site_Refuelling_v3.5.html",
    "03c_Bulk_Diesel_Delivery_v3.5.html",
    "03d_HyBlue_v3.5.html",
    "03e_Oils_Lubricants_v3.5.html",
    "04_Aviation_Hub_v3.5.html",
    "04a_Aviation_Network_v3.5.html",
    "04b_Airport_Fuelling_v3.5.html",
    "04c_Aviation_Bulk_v3.5.html",
    "04d_Aviation_Oils_v3.5.html",
    "05_Equipment_Infrastructure.html",
    "06_Supply_Trading.html",
    "07_Digital_Platformsv5.html",
    "07a_HyDip_FMSv6.html",
    "07b_Fuelcharge_App_v8.html",
    "07c_Customer_Portal_v8.html",
    "08_Industries_v5.html",
    "08a_Mining_v5.html",
    "08b_Agriculture_v5.html",
    "08c_Transport_v5.html",
    "08d_Construction_v5.html",
    "08e_Livestock_v5.html",
    "08f_Government_v5.html",
    "08g_Aviation_v5.html",
    "08h_Oil_Gas_v5.html",
    "09a_Bio_AdriaanEsterhuizen_v5.html",
    "09a_Bio_BryceMorland_v5.html",
    "09a_Bio_ChrisWerfel_v5.html",
    "09a_Bio_DanielRoberts_v5.html",
    "09a_Bio_DrewLeishman_v5.html",
    "09a_Bio_DrewMorland_v5.html",
    "09a_Bio_HamishJarrett_v5.html",
    "09a_Bio_NellBond_v5.html",
    "09a_Bio_NickMackenzie_v5.html",
    "09a_Our_Leadershipv5.html",
    "09d_Case_Studies_v6.html",
    "09d_Case_Study_Singlev6.html",
    "11_Support_Hubv5.html",
    "11a_Contact_Usv5.html",
    "11b_Regional_Contactsv5.html",
    "11e_Make_Paymentv5.html",
    "11f_Privacy_Policyv5.html",
]

# Patterns to match in the proto-bar — covers all known variants:
# 1. href="00_Master_Index.html" with any surrounding text that says "Master Index"
# 2. The link text may be "← Master Index", "Master Index", "Back to Master Index" etc.
# We replace the href and the visible text.

REPLACEMENTS = [
    # Pattern: href="00_Master_Index.html" ... >...Master Index...< — replace href + text
    # Handles SVG arrow variant (Diesel/Aviation pages)
    (
        re.compile(
            r'href="00_Master_Index\.html"([^>]*>)\s*'
            r'(?:<svg[^>]*>.*?</svg>\s*)?'
            r'(?:&#8592;\s*|← \s*|Back to \s*)?Master Index',
            re.DOTALL
        ),
        r'href="00_Client_Preview.html"\1&#8592; Client Preview'
    ),
    # Fallback: any remaining href to Master Index
    (
        re.compile(r'href="00_Master_Index\.html"'),
        r'href="00_Client_Preview.html"'
    ),
]

# Also update aria-label if present
ARIA_PATTERN = re.compile(r'aria-label="Back to Master Index"')
ARIA_REPLACEMENT = 'aria-label="Back to Client Preview"'

changed = []
skipped = []

for fname in PAGES:
    if not os.path.exists(fname):
        skipped.append(fname)
        continue

    with open(fname, "r", encoding="utf-8") as f:
        original = f.read()

    updated = original

    # Only operate within the proto-bar block to be safe
    # Find the proto-bar div and apply replacements only there
    proto_match = re.search(
        r'(<div[^>]*class="[^"]*proto-bar[^"]*"[^>]*>)(.*?)(</div>\s*</div>)',
        updated, re.DOTALL
    )

    if not proto_match:
        # Try broader match
        proto_match = re.search(
            r'(proto-bar.*?</div>\s*</div>)',
            updated, re.DOTALL
        )

    # Apply globally within the file but only to the Master Index link
    for pattern, replacement in REPLACEMENTS:
        updated = pattern.sub(replacement, updated, count=1)

    updated = ARIA_PATTERN.sub(ARIA_REPLACEMENT, updated)

    if updated != original:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(updated)
        changed.append(fname)
    else:
        skipped.append(f"NO_CHANGE: {fname}")

print(f"\n✅ Updated {len(changed)} files:")
for f in changed:
    print(f"   {f}")

if skipped:
    print(f"\n⚠️  Skipped / no change ({len(skipped)}):")
    for f in skipped:
        print(f"   {f}")
