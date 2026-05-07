from pathlib import Path

path = Path("00_Client_Preview.html")
html = path.read_text(encoding="utf-8")

updates = [
    # Equipment & Infrastructure Hub — badge + href
    (
        '<div class="page-card__title">Equipment &amp; Infrastructure Hub</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
        '<div class="page-card__title">Equipment &amp; Infrastructure Hub</div>\n          <span class="badge badge--live">&#10003; Live</span>'
    ),
    (
        'href="05_Equipment_Infrastructure.html">View Page →',
        'href="https://alexc-sketch.github.io/ior-prototype/05_Equipment_Infrastructure_v8.html">View Page →'
    ),
    # Fuel Storage Tanks — remove pending class, add link, update badge
    (
        '<div class="page-card page-card--pending">\n        <div class="page-card__top">\n          <div class="page-card__title">Fuel Storage Tanks</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">Above-ground and underground storage tank solutions.</div>\n        <div class="page-card__footer">\n          <span class="page-card__link">Coming Soon</span>\n        </div>\n      </div>',
        '<div class="page-card">\n        <div class="page-card__top">\n          <div class="page-card__title">Fuel Storage Tanks</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Above-ground and underground storage tank solutions.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="https://alexc-sketch.github.io/ior-prototype/05a_Fuel_Storage_Tanks_v8.html">View Page →</a>\n        </div>\n      </div>'
    ),
    # Frac Tanks — remove pending class, add link, update badge
    (
        '<div class="page-card page-card--pending">\n        <div class="page-card__top">\n          <div class="page-card__title">Frac Tanks</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">Portable frac tank hire and delivery for remote sites.</div>\n        <div class="page-card__footer">\n          <span class="page-card__link">Coming Soon</span>\n        </div>\n      </div>',
        '<div class="page-card">\n        <div class="page-card__top">\n          <div class="page-card__title">Frac Tanks</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Portable frac tank hire and delivery for remote sites.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="https://alexc-sketch.github.io/ior-prototype/05b_Frac_Tanks_v8.html">View Page →</a>\n        </div>\n      </div>'
    ),
    # Supply & Trading Hub — badge + href
    (
        '<div class="page-card__title">Supply &amp; Trading Hub</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
        '<div class="page-card__title">Supply &amp; Trading Hub</div>\n          <span class="badge badge--live">&#10003; Live</span>'
    ),
    (
        'href="06_Supply_Trading.html">View Page →',
        'href="https://alexc-sketch.github.io/ior-prototype-v3-5/06_Supply_Trading_v8.html">View Page →'
    ),
    # Lytton & Port Bonython — remove pending class, add link, update badge
    (
        '<div class="page-card page-card--pending">\n        <div class="page-card__top">\n          <div class="page-card__title">Lytton &amp; Port Bonython</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">Terminal infrastructure — Lytton QLD and Port Bonython SA.</div>\n        <div class="page-card__footer">\n          <span class="page-card__link">Coming Soon</span>\n        </div>\n      </div>',
        '<div class="page-card">\n        <div class="page-card__top">\n          <div class="page-card__title">Lytton &amp; Port Bonython</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Terminal infrastructure — Lytton QLD and Port Bonython SA.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="https://alexc-sketch.github.io/ior-prototype/06a_Terminals_v8.html">View Page →</a>\n        </div>\n      </div>'
    ),
    # Eromanga Refinery — remove pending class, add link, update badge
    (
        '<div class="page-card page-card--pending">\n        <div class="page-card__top">\n          <div class="page-card__title">Eromanga Refinery</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">Australia\'s only inland refinery — Eromanga, QLD.</div>\n        <div class="page-card__footer">\n          <span class="page-card__link">Coming Soon</span>\n        </div>\n      </div>',
        '<div class="page-card">\n        <div class="page-card__top">\n          <div class="page-card__title">Eromanga Refinery</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Australia\'s only inland refinery — Eromanga, QLD.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="https://alexc-sketch.github.io/ior-prototype-v3-5/06b_Eromanga_v8.html">View Page →</a>\n        </div>\n      </div>'
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
