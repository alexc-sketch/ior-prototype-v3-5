"""
Update 4 Digital Platforms cards in 00_Client_Preview.html to Live with correct hrefs.
- Digital Platforms Hub v5 → 07_Digital_Platformsv5.html (already Live, href already correct — no change needed)
- HyDip™ FMS v11 → v14: 07a_HyDip_FMSv14.html
- Fuelcharge App v8 → v9: 07b_Fuelcharge_App_v9.html
- Customer Portal v8 → v12: 07c_Customer_Portal_v12.html (set to Live, remove pending class)
"""

with open('00_Client_Preview.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# 1. HyDip FMS: v11 → v14 (appears once in Digital Platforms section)
content = content.replace(
    '<div class="page-card__title">HyDip™ FMS v11</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Interactive tabs (GAUGE/TRACK/DISPENSE/PAY), hardware cards, HubSpot form.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="07a_HyDip_FMSv11.html">View Page →</a>',
    '<div class="page-card__title">HyDip™ FMS v14</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Interactive tabs (GAUGE/TRACK/DISPENSE/PAY), hardware cards, HubSpot form.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="07a_HyDip_FMSv14.html">View Page →</a>'
)

# 2. Fuelcharge App: v8 → v9
content = content.replace(
    '<div class="page-card__title">Fuelcharge App v8</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">B2C fintech SaaS style. Audience flip cards, 1-2-3 flow, no forms.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="07b_Fuelcharge_App_v8.html">View Page →</a>',
    '<div class="page-card__title">Fuelcharge App v9</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">B2C fintech SaaS style. Audience flip cards, 1-2-3 flow, no forms.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="07b_Fuelcharge_App_v9.html">View Page →</a>'
)

# 3. Customer Portal: pending/In Review → Live v12
content = content.replace(
    '<div class="page-card page-card--pending">\n        <div class="page-card__top">\n          <div class="page-card__title">Customer Portal v8</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">2×2 Bento Box, Request Access modal, 3-path access block. Target: 07c_Customer_Portal_v8.html</div>\n        <div class="page-card__footer">\n          <span class="page-card__link">In Build Queue</span>\n        </div>\n      </div>',
    '<div class="page-card">\n        <div class="page-card__top">\n          <div class="page-card__title">Customer Portal v12</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">2×2 Bento Box, Request Access modal, 3-path access block.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="07c_Customer_Portal_v12.html">View Page →</a>\n        </div>\n      </div>'
)

changes = sum(1 for a, b in zip(original, content) if a != b)
print(f"Changes applied. Content {'modified' if original != content else 'UNCHANGED — check patterns'}.")

with open('00_Client_Preview.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved.")

# Verify
import re
for title, href in [
    ('HyDip™ FMS v14', '07a_HyDip_FMSv14.html'),
    ('Fuelcharge App v9', '07b_Fuelcharge_App_v9.html'),
    ('Customer Portal v12', '07c_Customer_Portal_v12.html'),
]:
    if title in content and href in content:
        print(f"  ✅ {title} → {href}")
    else:
        print(f"  ❌ MISSING: {title} / {href}")
