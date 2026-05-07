"""
Update 00_Client_Preview.html:
- Set 8 approved pages to badge--live / ✓ Live
- Update hrefs for Diesel Network, Aviation Network, Industries Hub, Transport to v8/v6 URLs
"""

with open('00_Client_Preview.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ── 1. Homepage — already Live, just normalise symbol if needed ────────────
content = content.replace(
    '<div class="page-card__title">Homepage</div>\n          <span class="badge badge--live">Live</span>',
    '<div class="page-card__title">Homepage</div>\n          <span class="badge badge--live">&#10003; Live</span>'
)

# ── 2. Fuel Solutions Hub — already Live ──────────────────────────────────
# (no change needed, already badge--live ✓ Live)

# ── 3. Digital Platforms Hub v5 — In Review → Live ────────────────────────
# Appears twice: once in "All Pages" section, once in "Digital Platforms" module
content = content.replace(
    '<div class="page-card__title">Digital Platforms Hub v5</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
    '<div class="page-card__title">Digital Platforms Hub v5</div>\n          <span class="badge badge--live">&#10003; Live</span>'
)

# ── 4. Industries We Serve Hub — In Review → Live (All Pages section) ─────
content = content.replace(
    '<div class="page-card__title">Industries We Serve Hub</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
    '<div class="page-card__title">Industries We Serve Hub</div>\n          <span class="badge badge--live">&#10003; Live</span>'
)

# ── 5. IOR Diesel Network — QC Review → Live + fix href to v8 ─────────────
content = content.replace(
    '<div class="page-card__title">IOR Diesel Network</div>\n          <span class="badge badge--review">QC Review</span>',
    '<div class="page-card__title">IOR Diesel Network</div>\n          <span class="badge badge--live">&#10003; Live</span>'
)
content = content.replace(
    'href="03a_Diesel_Network_v3.5.html">View Page →',
    'href="03a_Diesel_Network_v8.html">View Page →'
)
# Also fix the desc note
content = content.replace(
    '115+ unmanned 24/7 diesel stops. Network map, RFID account, 1-2-3 flow. Target: 03a_Diesel_Network_v8.html',
    '115+ unmanned 24/7 diesel stops. Network map, RFID account, 1-2-3 flow.'
)

# ── 6. IOR Aviation Network — In Review → Live + fix href to v8 ───────────
content = content.replace(
    '<div class="page-card__title">IOR Aviation Network</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
    '<div class="page-card__title">IOR Aviation Network</div>\n          <span class="badge badge--live">&#10003; Live</span>'
)
content = content.replace(
    'href="04a_Aviation_Network_v3.5.html">View Current →',
    'href="04a_Aviation_Network_v8.html">View Page →'
)

# ── 7. Fuelcharge App v8 — In Review → Live ───────────────────────────────
content = content.replace(
    '<div class="page-card__title">Fuelcharge App v8</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
    '<div class="page-card__title">Fuelcharge App v8</div>\n          <span class="badge badge--live">&#10003; Live</span>'
)

# ── 8. Industries Hub (Digital Platforms module section) — In Review → Live + fix href ──
content = content.replace(
    '<div class="page-card__title">Industries Hub</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
    '<div class="page-card__title">Industries Hub</div>\n          <span class="badge badge--live">&#10003; Live</span>'
)
content = content.replace(
    'href="08_Industries_v5.html">View Page →',
    'href="08_Industries_v6.html">View Page →'
)

# ── 9. Transport & Logistics — In Review → Live + fix href ────────────────
content = content.replace(
    '<div class="page-card__title">Transport &amp; Logistics</div>\n          <span class="badge badge--review">&#9679; In Review</span>',
    '<div class="page-card__title">Transport &amp; Logistics</div>\n          <span class="badge badge--live">&#10003; Live</span>'
)
content = content.replace(
    'href="08c_Transport_v5.html">View Page →',
    'href="08c_Transport_v6.html">View Page →'
)

# ── Count changes ─────────────────────────────────────────────────────────
if content == original:
    print("WARNING: No changes made — check find strings match exactly")
else:
    changes = sum(1 for a, b in zip(original.splitlines(), content.splitlines()) if a != b)
    print(f"Changes applied. Approx {changes} lines modified.")

with open('00_Client_Preview.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done.")
