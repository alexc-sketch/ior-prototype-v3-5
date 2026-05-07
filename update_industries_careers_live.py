"""
Update Industries and Careers page cards in 00_Client_Preview.html to Live with correct hrefs.
Zero edits to any page files.
"""

with open('00_Client_Preview.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ── INDUSTRIES ──────────────────────────────────────────────────────────────

# Industries We Serve Hub — already Live, href already correct (08_Industries_v6.html) — no change needed

# Transport & Logistics: v6 → v9
content = content.replace(
    '<div class="page-card__title">Transport &amp; Logistics</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Diesel network, on-site, HyDip™ FMS, case study.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08c_Transport_v6.html">View Page →</a>',
    '<div class="page-card__title">Transport &amp; Logistics</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Diesel network, on-site, HyDip™ FMS, case study.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08c_Transport_v9.html">View Page →</a>'
)

# Oil & Gas: In Review v5 → Live v9
content = content.replace(
    '<div class="page-card__title">Oil &amp; Gas</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">Remote supply, on-site infrastructure, fluid logistics.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08h_Oil_Gas_v5.html">View Page →</a>',
    '<div class="page-card__title">Oil &amp; Gas</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Remote supply, on-site infrastructure, fluid logistics.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08b_Oil_Gas_v9.html">View Page →</a>'
)

# Agriculture & Harvest: In Review v5 → Live v9
content = content.replace(
    '<div class="page-card__title">Agriculture &amp; Harvest</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">Bulk delivery, seasonal supply, on-site storage.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08b_Agriculture_v5.html">View Page →</a>',
    '<div class="page-card__title">Agriculture &amp; Harvest</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Bulk delivery, seasonal supply, on-site storage.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08e_Agriculture_v9.html">View Page →</a>'
)

# Mining & Resources: In Review v5 → Live v9
content = content.replace(
    '<div class="page-card__title">Mining &amp; Resources</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">Remote-ready, high-volume, compliance, HyDip™ FMS.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08a_Mining_v5.html">View Page →</a>',
    '<div class="page-card__title">Mining &amp; Resources</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Remote-ready, high-volume, compliance, HyDip™ FMS.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08a_Mining_v9.html">View Page →</a>'
)

# Livestock: In Review v5 → Live v9
content = content.replace(
    '<div class="page-card__title">Livestock</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">Remote delivery, station storage, aviation fuels.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08e_Livestock_v5.html">View Page →</a>',
    '<div class="page-card__title">Livestock</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Remote delivery, station storage, aviation fuels.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08f_Livestock_v9.html">View Page →</a>'
)

# Commercial & General Aviation: In Review v5 → Live v9
content = content.replace(
    '<div class="page-card__title">Commercial &amp; General Aviation</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">JIG-compliant Jet A-1, Avgas, Fuelcharge self-serve.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08g_Aviation_v5.html">View Page →</a>',
    '<div class="page-card__title">Commercial &amp; General Aviation</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">JIG-compliant Jet A-1, Avgas, Fuelcharge self-serve.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08h_Aviation_v9.html">View Page →</a>'
)

# Construction & Civil: In Review v5 → Live v9
content = content.replace(
    '<div class="page-card__title">Construction &amp; Civil</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">Project-based supply, temporary storage, mobile delivery.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08d_Construction_v5.html">View Page →</a>',
    '<div class="page-card__title">Construction &amp; Civil</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Project-based supply, temporary storage, mobile delivery.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08d_Construction_v9.html">View Page →</a>'
)

# Government & Defence: In Review v5 → Live v9
content = content.replace(
    '<div class="page-card__title">Government &amp; Defence</div>\n          <span class="badge badge--review">&#9679; In Review</span>\n        </div>\n        <div class="page-card__desc">Sovereign supply, full audit trail, ISO-aligned.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08f_Government_v5.html">View Page →</a>',
    '<div class="page-card__title">Government &amp; Defence</div>\n          <span class="badge badge--live">&#10003; Live</span>\n        </div>\n        <div class="page-card__desc">Sovereign supply, full audit trail, ISO-aligned.</div>\n        <div class="page-card__footer">\n          <a class="page-card__link" href="08g_Government_v9.html">View Page →</a>'
)

# ── CAREERS ─────────────────────────────────────────────────────────────────

# Careers Hub: Pending → Live v2
content = content.replace(
    '<div class="page-card page-card--pending"><div class="page-card__top"><div class="page-card__title">Careers Hub</div><span class="badge badge--pending">Pending</span></div><div class="page-card__desc">Entry pathways, culture, benefits routing hub.</div><div class="page-card__footer"><span class="page-card__link">Coming Soon</span></div></div>',
    '<div class="page-card"><div class="page-card__top"><div class="page-card__title">Careers Hub</div><span class="badge badge--live">&#10003; Live</span></div><div class="page-card__desc">Entry pathways, culture, benefits routing hub.</div><div class="page-card__footer"><a class="page-card__link" href="10_Careers_v2.html">View Page →</a></div></div>'
)

# Entry Pathways: Pending → Live
content = content.replace(
    '<div class="page-card page-card--pending"><div class="page-card__top"><div class="page-card__title">Entry Pathways</div><span class="badge badge--pending">Pending</span></div><div class="page-card__desc">Tabbed directory — Apprentices, Graduates, School-Based, Regional.</div><div class="page-card__footer"><span class="page-card__link">Coming Soon</span></div></div>',
    '<div class="page-card"><div class="page-card__top"><div class="page-card__title">Entry Pathways</div><span class="badge badge--live">&#10003; Live</span></div><div class="page-card__desc">Tabbed directory — Apprentices, Graduates, School-Based, Regional.</div><div class="page-card__footer"><a class="page-card__link" href="10a_Entry_Pathways.html">View Page →</a></div></div>'
)

# Apprentices & Trades: Pending → Live
content = content.replace(
    '<div class="page-card page-card--pending"><div class="page-card__top"><div class="page-card__title">Apprentices &amp; Trades</div><span class="badge badge--pending">Pending</span></div><div class="page-card__desc">Step-by-step apprenticeship journey — Easy as 1, 2, 3.</div><div class="page-card__footer"><span class="page-card__link">Coming Soon</span></div></div>',
    '<div class="page-card"><div class="page-card__top"><div class="page-card__title">Apprentices &amp; Trades</div><span class="badge badge--live">&#10003; Live</span></div><div class="page-card__desc">Step-by-step apprenticeship journey — Easy as 1, 2, 3.</div><div class="page-card__footer"><a class="page-card__link" href="10c_Apprentices.html">View Page →</a></div></div>'
)

# Graduates & Interns: Pending → Live
content = content.replace(
    '<div class="page-card page-card--pending"><div class="page-card__top"><div class="page-card__title">Graduates &amp; Interns</div><span class="badge badge--pending">Pending</span></div><div class="page-card__desc">3 streams: Technology, Shared Services, Operations.</div><div class="page-card__footer"><span class="page-card__link">Coming Soon</span></div></div>',
    '<div class="page-card"><div class="page-card__top"><div class="page-card__title">Graduates &amp; Interns</div><span class="badge badge--live">&#10003; Live</span></div><div class="page-card__desc">3 streams: Technology, Shared Services, Operations.</div><div class="page-card__footer"><a class="page-card__link" href="10d_Graduates.html">View Page →</a></div></div>'
)

# School-Based & Trainees: Pending → split into two cards: School Based + Trainees
content = content.replace(
    '<div class="page-card page-card--pending"><div class="page-card__top"><div class="page-card__title">School-Based &amp; Trainees</div><span class="badge badge--pending">Pending</span></div><div class="page-card__desc">Info cards + FAQ accordion — requirements, benefits.</div><div class="page-card__footer"><span class="page-card__link">Coming Soon</span></div></div>',
    '<div class="page-card"><div class="page-card__top"><div class="page-card__title">School Based</div><span class="badge badge--live">&#10003; Live</span></div><div class="page-card__desc">School-based learning pathways — requirements, benefits.</div><div class="page-card__footer"><a class="page-card__link" href="10e_School_Based.html">View Page →</a></div></div>'
    + '<div class="page-card"><div class="page-card__top"><div class="page-card__title">Trainees</div><span class="badge badge--live">&#10003; Live</span></div><div class="page-card__desc">Trainee pathways — info cards + FAQ accordion.</div><div class="page-card__footer"><a class="page-card__link" href="10f_Trainees.html">View Page →</a></div></div>'
)

# Also need to add Meet the Team card — check if it exists, if not add after Careers Hub
if '10b_Meet_The_Team' not in content:
    content = content.replace(
        '<div class="page-card"><div class="page-card__top"><div class="page-card__title">Careers Hub</div><span class="badge badge--live">&#10003; Live</span></div><div class="page-card__desc">Entry pathways, culture, benefits routing hub.</div><div class="page-card__footer"><a class="page-card__link" href="10_Careers_v2.html">View Page →</a></div></div>',
        '<div class="page-card"><div class="page-card__top"><div class="page-card__title">Careers Hub</div><span class="badge badge--live">&#10003; Live</span></div><div class="page-card__desc">Entry pathways, culture, benefits routing hub.</div><div class="page-card__footer"><a class="page-card__link" href="10_Careers_v2.html">View Page →</a></div></div>'
        + '<div class="page-card"><div class="page-card__top"><div class="page-card__title">Meet the Team</div><span class="badge badge--live">&#10003; Live</span></div><div class="page-card__desc">Team profiles and culture.</div><div class="page-card__footer"><a class="page-card__link" href="10b_Meet_The_Team.html">View Page →</a></div></div>'
    )

print(f"Content {'modified' if original != content else 'UNCHANGED — check patterns'}.")

with open('00_Client_Preview.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved. Verifying...")

checks = [
    ('Transport v9', '08c_Transport_v9.html'),
    ('Oil & Gas v9', '08b_Oil_Gas_v9.html'),
    ('Agriculture v9', '08e_Agriculture_v9.html'),
    ('Mining v9', '08a_Mining_v9.html'),
    ('Livestock v9', '08f_Livestock_v9.html'),
    ('Aviation v9', '08h_Aviation_v9.html'),
    ('Construction v9', '08d_Construction_v9.html'),
    ('Government v9', '08g_Government_v9.html'),
    ('Careers v2', '10_Careers_v2.html'),
    ('Meet the Team', '10b_Meet_The_Team.html'),
    ('Entry Pathways', '10a_Entry_Pathways.html'),
    ('Apprentices', '10c_Apprentices.html'),
    ('Graduates', '10d_Graduates.html'),
    ('School Based', '10e_School_Based.html'),
    ('Trainees', '10f_Trainees.html'),
]

for label, href in checks:
    status = "✅" if href in content else "❌ MISSING"
    print(f"  {status} {label} → {href}")
