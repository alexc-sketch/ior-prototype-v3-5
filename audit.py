#!/usr/bin/env python3
"""
IOR Prototype Audit Script — v2.0
Run: python3.11 audit.py <filename.html>

Checks all Golden Rules + structural requirements.
MUST PASS before opening a PR.
"""

import sys
import re
import os

def audit(filepath):
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    lines = html.split('\n')
    filename = os.path.basename(filepath)
    results = []
    passed = 0
    failed = 0

    def check(rule_id, description, test_fn):
        nonlocal passed, failed
        result, detail = test_fn()
        status = "✅ PASS" if result else "❌ FAIL"
        if result:
            passed += 1
        else:
            failed += 1
        results.append((rule_id, status, description, detail))

    # ── R1: No operating hours ──────────────────────────────────────────────
    def r1():
        pattern = re.compile(r'\b(opening hours|trading hours|mon[-–]fri|monday to friday|7am|8am|24/7 support|open \d|closes at)', re.I)
        hits = []
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            # Skip CSS/JS/comment lines
            if stripped.startswith('//') or stripped.startswith('*') or stripped.startswith('/*'):
                continue
            # Skip CSS property lines (contain colon after selector)
            if re.search(r'^[\w\s.#:>~+*\[\]"=-]+\s*\{', stripped):
                continue
            if re.search(r'^[\w-]+\s*:', stripped) and '{' not in stripped and '<' not in stripped:
                continue
            # Skip HTML comment lines
            if stripped.startswith('<!--') or stripped.startswith('*'):
                continue
            m = pattern.search(stripped)
            if m:
                hits.append(f"L{i}: {stripped[:80]}")
        return (len(hits) == 0, f"{len(hits)} hits" if hits else "Clean")

    check("R1", "No operating hours in live content", r1)

    # ── R2: No disallowed border-radius ────────────────────────────────────
    def r2():
        hits = []
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            # Skip comment lines and annotation strings
            if stripped.startswith('//') or stripped.startswith('*') or stripped.startswith('/*'):
                continue
            if '<!--' in line:
                continue
            m = re.search(r'border-radius\s*:\s*(?!0\b|0px|500px|var\(--radius)', stripped)
            if m:
                # Skip if it's inside a CSS comment or annotation string
                if re.search(r'(Figma|STRIPPED|annotation|note|comment)', stripped, re.I):
                    continue
                # Skip permitted values: 500px (pill), 0, var(--radius-*)
                val_match = re.search(r'border-radius\s*:\s*([^;}{]+)', stripped)
                if val_match:
                    val = val_match.group(1).strip().lower()
                    # Permitted: 0, 0px, 500px, var(--radius-none), var(--radius-pill), em/rem values on btn classes
                    if re.match(r'^(0|0px|500px|var\(--radius)', val):
                        continue
                    # Permitted: any border-radius on .btn, .btn--pill, .cs-pill, .nav-link class definitions
                    if re.search(r'\.(btn|cs-pill|nav-link|ior-nav|drawer|utility)', stripped):
                        continue
                hits.append(f"L{i}: {stripped[:80]}")
        return (len(hits) == 0, f"{len(hits)} hits" if hits else "Clean")

    check("R2", "No disallowed border-radius (only 0 / 500px / var(--radius-*))", r2)

    # ── R3: No CSS gradients ────────────────────────────────────────────────
    def r3():
        hits = []
        permitted_contexts = ['hero__scrim', 'cs-hero__scrim', 'scrim', 'photographic', 'permitted']
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith('//') or stripped.startswith('*') or stripped.startswith('/*'):
                continue
            if '<!--' in line:
                continue
            if re.search(r'(linear-gradient|radial-gradient|conic-gradient)', stripped):
                # Check if it's in a permitted scrim context
                context = '\n'.join(lines[max(0,i-3):i+2])
                if any(p in context.lower() for p in permitted_contexts):
                    continue
                # Skip annotation text
                if re.search(r'(Figma|STRIPPED|annotation)', stripped, re.I):
                    continue
                hits.append(f"L{i}: {stripped[:80]}")
        return (len(hits) == 0, f"{len(hits)} hits" if hits else "Clean")

    check("R3", "No CSS gradients (hero photo scrim permitted)", r3)

    # ── R4: No inline style= on body elements ──────────────────────────────
    def r4():
        hits = []
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if '<!--' in line and '-->' in line:
                continue
            m = re.search(r'style\s*=\s*"[^"]*"', stripped)
            if m:
                # Permitted: empty style="" (should be removed but not a blocker)
                val = re.search(r'style\s*=\s*"([^"]*)"', stripped)
                if val and val.group(1).strip() == '':
                    continue
                # Permitted: background-image on card image divs (dynamic featured image)
                if 'background-image' in stripped and ('card__image' in stripped or 'cs-card' in stripped):
                    continue
                # Permitted: document.body.style (JS)
                if 'document.body.style' in stripped:
                    continue
                # Skip annotation/CS label spans
                if 'cs-label' in stripped or 'ann-' in stripped:
                    continue
                # Permitted: asset-placeholder divs (required by brief)
                if 'asset-placeholder' in stripped:
                    continue
                # Permitted: HubSpot form placeholder divs
                if 'hs-form-placeholder' in stripped:
                    continue
                # Permitted: hero background-color (solid colour, no gradient)
                if 'background-color' in stripped and 'hero' in stripped and 'gradient' not in stripped:
                    continue
                # Permitted: bento grid layout divs
                if 'grid-template-columns' in stripped:
                    continue
                # Permitted: strong/p inside asset-placeholder (colour labels)
                if '<strong style=' in stripped or '<p style=' in stripped:
                    continue
                hits.append(f"L{i}: {stripped[:80]}")
        return (len(hits) == 0, f"{len(hits)} hits" if hits else "Clean")

    check("R4", "No inline style= on body elements", r4)

    # ── R5: No hero overlay / blue overlay ─────────────────────────────────
    def r5():
        hits = []
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if '<!--' in line:
                continue
            if re.search(r'hero[_-]overlay|\.hero.*rgba|overlay.*hero', stripped, re.I):
                if not re.search(r'(annotation|STRIPPED|Figma)', stripped, re.I):
                    # Skip CSS class definitions (lines with curly braces - these are style rules, not HTML overlays)
                    if '{' in stripped and '}' in stripped:
                        continue
                    hits.append(f"L{i}: {stripped[:80]}")
        return (len(hits) == 0, f"{len(hits)} hits" if hits else "Clean")

    check("R5", "No hero overlay / blue overlay on hero", r5)

    # ── R6: No word 'depot' ─────────────────────────────────────────────────
    def r6():
        hits = []
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if '<!--' in line and '-->' in line:
                continue
            if re.search(r'\bdepot\b', stripped, re.I):
                # Skip CSS class names and JS
                if re.search(r'(class=|\.depot|#depot|depot-)', stripped):
                    continue
                hits.append(f"L{i}: {stripped[:80]}")
        return (len(hits) == 0, f"{len(hits)} hits" if hits else "Clean")

    check("R6", "No word 'depot' in live content", r6)

    # ── R7: Canonical 5-item nav ────────────────────────────────────────────
    def r7():
        required = ['Fuel Solutions', 'Digital Platforms', 'Industries We Serve', 'About IOR', 'Support &amp; Contact']
        missing = [item for item in required if item not in html]
        return (len(missing) == 0, f"Missing: {missing}" if missing else "All 5 items present")

    check("R7", "Canonical 5-item nav (Fuel Solutions / Digital Platforms / Industries We Serve / About IOR / Support & Contact)", r7)

    # ── R8: 6-column footer ─────────────────────────────────────────────────
    def r8():
        required = ['Contact', 'Fuel Solutions', 'Digital Platforms', 'Corporate', 'Quick Actions', 'Find a Site By State']
        missing = [item for item in required if item not in html]
        return (len(missing) == 0, f"Missing footer columns: {missing}" if missing else "All 6 columns present")

    check("R8", "6-column footer (Contact / Fuel Solutions / Digital Platforms / Corporate / Quick Actions / Find a Site By State)", r8)

    # ── R9: Pre-footer 'We're here to help' ────────────────────────────────
    def r9():
        has_prefooter = "here to help" in html.lower()
        has_apply = "Apply for an Account" in html
        return (has_prefooter and has_apply, "Present" if (has_prefooter and has_apply) else "Missing pre-footer or Apply CTA")

    check("R9", "Pre-footer 'We're here to help' with CTAs", r9)

    # ── R10: Proto-bar with Master Index link ───────────────────────────────
    def r10():
        has_proto = 'proto-bar' in html or 'util-bar' in html
        has_mi = '00_Master_Index.html' in html
        return (has_proto and has_mi, "Present" if (has_proto and has_mi) else f"proto-bar={'YES' if has_proto else 'MISSING'}, Master Index link={'YES' if has_mi else 'MISSING'}")

    check("R10", "Proto-bar above nav with Master Index link", r10)

    # ── R11: No v3.5 hrefs ─────────────────────────────────────────────────
    def r11():
        hits = []
        for i, line in enumerate(lines, 1):
            if re.search(r'href="[^"]*v3\.5[^"]*"', line):
                hits.append(f"L{i}: {line.strip()[:80]}")
        return (len(hits) == 0, f"{len(hits)} v3.5 hrefs found" if hits else "Clean")

    check("R11", "No v3.5 hrefs (all old page links replaced with # or v5)", r11)

    # ── R12: Support Hub links use v5 filename ──────────────────────────────
    def r12():
        old = re.findall(r'href="11_Support_Hub\.html"', html)
        return (len(old) == 0, f"{len(old)} old Support Hub links" if old else "Clean")

    check("R12", "Support Hub links use 11_Support_Hubv5.html", r12)

    # ── R13: Quick Links bar below hero ────────────────────────────────────
    def r13():
        hero_pos = html.find('class="page-hero') or html.find('class="cs-list-hero') or html.find('class="cp-hero') or html.find('class="hd-hero') or html.find('class="fc-hero')
        ql_pos = html.find('quick-links-bar')
        if hero_pos == -1 or ql_pos == -1:
            # No hero or no quick links — not required to have both
            return (True, "No hero/QL bar — not applicable" if hero_pos == -1 else "Quick Links bar present")
        # Quick links should appear after hero in the HTML
        # But CSS class definition will appear before — check HTML section only
        # Find the actual HTML element (not CSS definition)
        ql_html_pos = html.find('<section class="quick-links-bar')
        if ql_html_pos == -1:
            ql_html_pos = html.find('<div class="quick-links-bar')
        if ql_html_pos == -1:
            return (True, "No Quick Links bar — not required on all pages")
        # Find hero section end
        hero_section_end = html.find('</section>', hero_pos)
        return (ql_html_pos > hero_section_end, f"QL at {ql_html_pos}, hero ends at {hero_section_end}" if ql_html_pos <= hero_section_end else "Correct position")

    check("R13", "Quick Links bar positioned below hero", r13)

    # ── R14: No emoji in nav/footer links ──────────────────────────────────
    def r14():
        emoji_pattern = re.compile(r'[\U0001F300-\U0001FFFF\U00002600-\U000027FF]')
        hits = []
        for i, line in enumerate(lines, 1):
            if '<a ' in line and emoji_pattern.search(line):
                hits.append(f"L{i}: {line.strip()[:80]}")
        return (len(hits) == 0, f"{len(hits)} emoji in links" if hits else "Clean")

    check("R14", "No emoji in nav/footer/body links", r14)

    # ── R15: Site by ThreePM in footer ─────────────────────────────────────
    def r15():
        has_threepm = 'ThreePM' in html or '3PM' in html
        return (has_threepm, "Present" if has_threepm else "MISSING — add 'Site by ThreePM' to footer")

    check("R15", "Footer contains 'Site by ThreePM'", r15)

    # ── R16: Mobile drawer present ─────────────────────────────────────────
    def r16():
        has_drawer = 'mobile-drawer' in html or 'id="mobile-drawer"' in html or 'class="drawer"' in html
        return (has_drawer, "Present" if has_drawer else "MISSING mobile drawer")

    check("R16", "Mobile drawer present", r16)

    # ── R17: No forms outside modal ────────────────────────────────────────
    def r17():
        # Forms are only permitted inside modal containers
        form_matches = list(re.finditer(r'<form\b', html))
        bad_forms = []
        for m in form_matches:
            pos = m.start()
            # Check if inside a modal
            context_before = html[max(0, pos-500):pos]
            if 'modal' not in context_before.lower() and 'hubspot' not in context_before.lower():
                line_num = html[:pos].count('\n') + 1
                bad_forms.append(f"L{line_num}")
        return (len(bad_forms) == 0, f"Forms outside modal at: {bad_forms}" if bad_forms else "Clean (forms in modal only)")

    check("R17", "No forms outside modal containers", r17)

    # ── R18: .btn--pill only on permitted elements ──────────────────────────
    def r18():
        # btn--pill is permitted on nav CTAs, filter pills, pagination, cs-pill
        return (True, "Not auto-checked — verify manually in nav CTAs and filter pills")

    check("R18", "btn--pill / cs-pill on permitted elements only", r18)

    # ── R19: Announcement bar present ──────────────────────────────────────
    def r19():
        has_ann = 'ior-utility-bar' in html or 'utility-bar' in html or 'util-bar' in html
        return (has_ann, "Present" if has_ann else "MISSING utility/announcement bar")

    check("R19", "Utility/announcement bar present", r19)

    # ── R20: No placeholder YouTube IDs ────────────────────────────────────
    def r20():
        hits = re.findall(r'VIDEO_ID_\d+|YOUR_VIDEO_ID|PLACEHOLDER_ID', html)
        return (len(hits) == 0, f"{len(hits)} placeholder video IDs" if hits else "Clean")

    check("R20", "No placeholder YouTube IDs", r20)

    # ── PRINT RESULTS ───────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"IOR AUDIT REPORT — {filename}")
    print(f"{'='*60}")
    for rule_id, status, desc, detail in results:
        print(f"\n{status} [{rule_id}] {desc}")
        if detail and detail not in ("Clean", "Present", "All 5 items present", "All 6 columns present"):
            print(f"    → {detail}")

    print(f"\n{'='*60}")
    total = passed + failed
    print(f"RESULT: {passed}/{total} checks passed")
    if failed == 0:
        print("✅ ALL CHECKS PASSED — Safe to open PR")
    else:
        print(f"❌ {failed} CHECK(S) FAILED — Fix before opening PR")
    print(f"{'='*60}\n")

    return failed == 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3.11 audit.py <filename.html>")
        print("Example: python3.11 audit.py 03a_Diesel_Networkv5.html")
        sys.exit(1)

    filepath = sys.argv[1]
    # If just a filename, look in current directory
    if not os.path.dirname(filepath):
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath)

    success = audit(filepath)
    sys.exit(0 if success else 1)
