from pathlib import Path

path = Path("00_Client_Preview.html")
html = path.read_text(encoding="utf-8")

updates = [
    # Aviation Hub
    (
        '<div class="page-card__title">Aviation Hub</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
        '<div class="page-card__title">Aviation Hub</div>\n          <span class="badge badge--live">&#10003; Live</span>'
    ),
    (
        'href="04_Aviation_Hub_v3.5.html">View Current →',
        'href="https://alexc-sketch.github.io/ior-prototype/04_Aviation_Hub_v9.html">View Page →'
    ),
    # IOR Aviation Network — already Live, just fix the link text
    (
        'href="04a_Aviation_Network_v8.html">View Current →',
        'href="04a_Aviation_Network_v8.html">View Page →'
    ),
    # Airport Fuelling Services
    (
        '<div class="page-card__title">Airport Fuelling Services</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
        '<div class="page-card__title">Airport Fuelling Services</div>\n          <span class="badge badge--live">&#10003; Live</span>'
    ),
    (
        'href="04b_Airport_Fuelling_v3.5.html">View Current →',
        'href="https://alexc-sketch.github.io/ior-prototype/04b_Airport_Fuelling_v9.html">View Page →'
    ),
    # Also clean up the Target: text in the desc
    (
        'JIG-accredited, Aviation Gold identity, into-plane + fuel farm. Target: 04b_Airport_Fuelling_v8.html',
        'JIG-accredited, Aviation Gold identity, into-plane + fuel farm.'
    ),
    # Aviation Bulk Delivery
    (
        '<div class="page-card__title">Aviation Bulk Delivery</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
        '<div class="page-card__title">Aviation Bulk Delivery</div>\n          <span class="badge badge--live">&#10003; Live</span>'
    ),
    (
        'href="04c_Aviation_Bulk_v3.5.html">View Current →',
        'href="https://alexc-sketch.github.io/ior-prototype/04c_Aviation_Bulk_Delivery_v9.html">View Page →'
    ),
    # Aviation Oils & Lubricants
    (
        '<div class="page-card__title">Aviation Oils &amp; Lubricants</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
        '<div class="page-card__title">Aviation Oils &amp; Lubricants</div>\n          <span class="badge badge--live">&#10003; Live</span>'
    ),
    (
        'href="04d_Aviation_Oils_v3.5.html">View Current →',
        'href="https://alexc-sketch.github.io/ior-prototype/04d_Aviation_Oils_v9.html">View Page →'
    ),
]

for old, new in updates:
    if old in html:
        html = html.replace(old, new, 1)
        print(f"✅ Updated: {old[:70].strip()!r}")
    else:
        print(f"⚠️  NOT FOUND: {old[:70].strip()!r}")

path.write_text(html, encoding="utf-8")
print("\nDone.")
