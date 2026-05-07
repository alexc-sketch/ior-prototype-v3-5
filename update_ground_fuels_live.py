from pathlib import Path

path = Path("00_Client_Preview.html")
html = path.read_text(encoding="utf-8")

# Define the 4 cards to update: (old_badge_class, old_badge_text, old_href, old_link_text, old_desc, new_href, new_desc)
updates = [
    # On-Site Refuelling
    (
        '<div class="page-card__title">On-Site Refuelling</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
        '<div class="page-card__title">On-Site Refuelling</div>\n          <span class="badge badge--live">&#10003; Live</span>'
    ),
    (
        'href="03b_On_Site_Refuelling_v3.5.html">View Current →',
        'href="03b_On_Site_Refuelling_v9.html">View Page →'
    ),
    # Bulk Diesel Delivery
    (
        '<div class="page-card__title">Bulk Diesel Delivery</div>\n          <span class="badge badge--review">QC Review</span>',
        '<div class="page-card__title">Bulk Diesel Delivery</div>\n          <span class="badge badge--live">&#10003; Live</span>'
    ),
    (
        'href="03c_Bulk_Diesel_Delivery_v3.5.html">View Current →',
        'href="03c_Bulk_Diesel_Delivery_v9.html">View Page →'
    ),
    # HyBlue
    (
        '<div class="page-card__title">HyBlue™ AdBlue®</div>\n          <span class="badge badge--review">QC Review</span>',
        '<div class="page-card__title">HyBlue™ AdBlue®</div>\n          <span class="badge badge--live">&#10003; Live</span>'
    ),
    (
        'href="03d_HyBlue_v3.5.html">View Page →',
        'href="03d_HyBlue_v8.html">View Page →'
    ),
    # Oils & Lubricants
    (
        '<div class="page-card__title">Oils &amp; Lubricants</div>\n          <span class="badge badge--review">QC Review</span>',
        '<div class="page-card__title">Oils &amp; Lubricants</div>\n          <span class="badge badge--live">&#10003; Live</span>'
    ),
    (
        'href="03e_Oils_Lubricants_v3.5.html">View Page →',
        'href="03e_Oils_Lubricants_v9.html">View Page →'
    ),
    # Also update the desc text to remove "Target:" references
    (
        'Mobile refuelling, wet hosing, service specs. Target: 03b_On_Site_Refuelling_v8.html',
        'Mobile refuelling, wet hosing, service specs.'
    ),
    (
        'Bulk tanker delivery, minimum orders, scheduling. Target: 03c_Bulk_Diesel_Delivery_v8.html',
        'Bulk tanker delivery, minimum orders, scheduling.'
    ),
    (
        'VDA &amp; ISO 22241 certified DEF. 5-tab supply options. Target: 03d_HyBlue_v8.html',
        'VDA &amp; ISO 22241 certified DEF. 5-tab supply options.'
    ),
    (
        'Engine oils, hydraulic fluids, greases, drum supply. Target: 03e_Oils_Lubricants_v8.html',
        'Engine oils, hydraulic fluids, greases, drum supply.'
    ),
]

for old, new in updates:
    if old in html:
        html = html.replace(old, new, 1)
        print(f"✅ Updated: {old[:60].strip()!r}")
    else:
        print(f"⚠️  NOT FOUND: {old[:60].strip()!r}")

path.write_text(html, encoding="utf-8")
print("\nDone.")
