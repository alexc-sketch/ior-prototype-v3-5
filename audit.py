#!/usr/bin/env python3
"""
IOR Prototype — Pre-commit Golden Rules Audit Script
Usage: python3 audit.py <filename.html>
       python3 audit.py --all          (audit all page HTML files)

Exits with code 0 on PASS, code 1 on FAIL.
"""

import sys
import re
import os
from pathlib import Path

# ── CONFIGURATION ──────────────────────────────────────────────────────────────

# Files that are exempt from audit (templates, design system, master index)
EXEMPT_FILES = {
    'IOR_Global_Template_Shell_v4.html',
    'IOR_Utility_Template_Shell_v5.html',
    'IOR_Page_Starter.html',
    'IOR_Design_System.html',
    'IOR_Mega_Menu_Prototype_v1.html',
    '00_Master_Index.html',
    '00_Global_Components.html',
}

# Permitted gradients (exact patterns that are allowed)
PERMITTED_GRADIENTS = [
    # Hero scrim for photographic legibility (CS Template)
    r'linear-gradient\(to top.*rgba\(0,0,0',
    r'linear-gradient\(180deg.*rgba\(0,0,0',
    # Dark overlay scrim for photo heroes
    r'linear-gradient\(.*rgba\(10,34,64',
    r'linear-gradient\(.*rgba\(10,\s*34,\s*64',
    # Logo strip fade masks (white background edge treatment)
    r'linear-gradient\(to (left|right).*rgba\(255,255,255',
    # Repeating hatching pattern (annotation/placeholder only)
    r'repeating-linear-gradient',
]

# Permitted border-radius values (anything else fails R2)
PERMITTED_RADIUS = [
    r'border-radius:\s*0',
    r'border-radius:\s*var\(--radius\)',
    r'border-radius:\s*500px',   # pills only
    r'border-radius:\s*50%',     # circular avatars only
    # rx/ry on SVG elements
    r'rx="\d+"',
    r'ry="\d+"',
]

# v3.5 href patterns that should be updated to v5
V35_PATTERNS = [
    r'href="11_Support_Hub\.html"',
    r'href="11a_Contact_Us\.html"',
    r'href="11b_Regional_Contacts\.html"',
    r'href="11d_Find_Location\.html"',
    r'href="11e_Make_Payment\.html"',
    r'href="09d_Case_Studies\.html"',
    r'href="CS_Template_v5\.html"',
]

# Required global components (regex patterns)
REQUIRED_COMPONENTS = {
    'Proto-bar':       r'class="proto-bar"',
    'Nav header':      r'id="primary-nav"',
    'Fuel Solutions':  r'Fuel Solutions',
    'Digital Platforms': r'Digital Platforms',
    'Industries We Serve': r'Industries We Serve',
    'About IOR':       r'About IOR',
    'Support & Contact': r'Support &amp; Contact',
    'Customer Login CTA': r'Customer Login',
    'Apply for Account CTA': r'Apply for an Account',
    'Mobile drawer':   r'id="mobile-drawer"',
    'Pre-footer':      r'class="pre-footer"',
    'Footer':          r'class="site-footer"',
    'Footer 6 columns': r'footer-nav-grid',
    'Site by 3PM':     r'Site by 3PM',
    'Copyright 2026':  r'2026 IOR',
    'QLD state pill':  r'footer-state-pill.*>QLD<',
}

# ── AUDIT FUNCTIONS ────────────────────────────────────────────────────────────

def audit_file(filepath: str) -> dict:
    """Run all Golden Rules checks on a single HTML file."""
    path = Path(filepath)
    if not path.exists():
        return {'file': filepath, 'error': 'File not found', 'pass': False, 'issues': []}

    filename = path.name
    if filename in EXEMPT_FILES:
        return {'file': filepath, 'exempt': True, 'pass': True, 'issues': []}

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
        lines = content.splitlines()

    issues = []
    warnings = []

    # ── R1: No operating hours ──────────────────────────────────────────────
    hours_pattern = re.compile(
        r'\b(Mon(day)?[-–]Fri(day)?|Mon[-–]Sun|'
        r'(7|8|9|10|11|12)am[-–](4|5|6|7|8)pm|'
        r'(7|8|9|10|11|12):00\s*(AM|PM)[-–](4|5|6|7|8):00\s*(AM|PM)|'
        r'open\s+(7\s+days|daily)|'
        r'(7am|8am|9am|10am|11am|12pm|1pm|2pm|3pm|4pm|5pm|6pm)\s*[-–]\s*(4pm|5pm|6pm|7pm|8pm))',
        re.IGNORECASE
    )
    for i, line in enumerate(lines, 1):
        if hours_pattern.search(line):
            # Exclude CSS property names and JS variable names
            if not re.search(r'(font-family|background|padding|margin|viewport|animation|transform)', line, re.I):
                issues.append(f'R1 FAIL — Operating hours at line {i}: {line.strip()[:80]}')

    # ── R2: No disallowed border-radius ────────────────────────────────────
    radius_pattern = re.compile(r'border-radius\s*:\s*([^;}\n]+)', re.IGNORECASE)
    for i, line in enumerate(lines, 1):
        m = radius_pattern.search(line)
        if m:
            value = m.group(1).strip()
            # Check if it's a permitted value
            permitted = any(re.search(p, line, re.IGNORECASE) for p in PERMITTED_RADIUS)
            # Also permit rx/ry SVG attributes
            if not permitted and 'rx=' not in line and 'ry=' not in line:
                issues.append(f'R2 FAIL — Disallowed border-radius "{value}" at line {i}: {line.strip()[:80]}')

    # ── R3: No disallowed gradients ─────────────────────────────────────────
    gradient_pattern = re.compile(r'(linear|radial|conic)-gradient\s*\(', re.IGNORECASE)
    for i, line in enumerate(lines, 1):
        if gradient_pattern.search(line):
            permitted = any(re.search(p, line, re.IGNORECASE) for p in PERMITTED_GRADIENTS)
            if not permitted:
                issues.append(f'R3 FAIL — Disallowed gradient at line {i}: {line.strip()[:80]}')

    # ── R4: No inline style= on live UI elements ────────────────────────────
    style_attr_pattern = re.compile(r'<[^>]+\bstyle\s*=\s*["\'][^"\']*["\']', re.IGNORECASE)
    # Permitted inline styles
    permitted_style_patterns = [
        r'background-image:\s*url\(',          # card image placeholders
        r'font-size:\s*0\.',                   # sup font-size on logo
        r'style="font-size:0\.',               # sup font-size on logo
    ]
    for i, line in enumerate(lines, 1):
        if style_attr_pattern.search(line):
            permitted = any(re.search(p, line, re.IGNORECASE) for p in permitted_style_patterns)
            if not permitted:
                issues.append(f'R4 FAIL — Inline style= at line {i}: {line.strip()[:80]}')

    # ── R5: No blue overlay on hero ─────────────────────────────────────────
    blue_overlay_pattern = re.compile(
        r'(hero|banner|masthead)[^}]*background[^}]*'
        r'(rgba\(\s*3\s*,\s*85\s*,\s*163|#0355A3|var\(--ior-blue\))',
        re.IGNORECASE | re.DOTALL
    )
    # Check for overlay divs with blue background inside hero sections
    overlay_in_hero = re.compile(
        r'(hero|banner)[^<]*<[^>]+(background[^>]*#0355A3|background[^>]*var\(--ior-blue\))',
        re.IGNORECASE
    )
    for i, line in enumerate(lines, 1):
        if re.search(r'(hero|banner).*overlay|overlay.*(hero|banner)', line, re.I):
            if re.search(r'(#0355A3|var\(--ior-blue\)|rgba\(3,\s*85,\s*163)', line, re.I):
                issues.append(f'R5 FAIL — Blue overlay on hero at line {i}: {line.strip()[:80]}')

    # ── R6: No word "depot" ─────────────────────────────────────────────────
    depot_pattern = re.compile(r'\bdepot\b', re.IGNORECASE)
    for i, line in enumerate(lines, 1):
        if depot_pattern.search(line):
            # Exclude comments
            if not line.strip().startswith('//') and not line.strip().startswith('*') and '<!--' not in line:
                issues.append(f'R6 FAIL — Word "depot" at line {i}: {line.strip()[:80]}')

    # ── R7: Required global components ──────────────────────────────────────
    for component, pattern in REQUIRED_COMPONENTS.items():
        if not re.search(pattern, content, re.IGNORECASE):
            issues.append(f'R7 FAIL — Missing required component: {component}')

    # ── R8: Dual nav CTAs with btn--pill ────────────────────────────────────
    if not re.search(r'btn--pill[^"]*"[^>]*>Customer Login', content, re.IGNORECASE):
        if not re.search(r'Customer Login.*btn--pill', content, re.IGNORECASE):
            issues.append('R8 FAIL — "Customer Login" CTA missing btn--pill class')
    if not re.search(r'btn--pill[^"]*"[^>]*>Apply for an Account', content, re.IGNORECASE):
        if not re.search(r'Apply for an Account.*btn--pill', content, re.IGNORECASE):
            issues.append('R8 FAIL — "Apply for an Account" CTA missing btn--pill class')

    # ── R9: v3.5 hrefs ──────────────────────────────────────────────────────
    for pattern in V35_PATTERNS:
        matches = [(i+1, l.strip()) for i, l in enumerate(lines) if re.search(pattern, l)]
        for lineno, linetext in matches:
            issues.append(f'R9 FAIL — v3.5 href at line {lineno}: {linetext[:80]}')

    # ── ADDITIONAL CHECKS ───────────────────────────────────────────────────
    # lang attribute
    if not re.search(r'<html[^>]+lang="en"', content, re.IGNORECASE):
        warnings.append('WARN — <html> tag missing lang="en" (found lang="en-AU" or missing)')

    # ThreePM vs 3PM
    if re.search(r'Site by ThreePM', content, re.IGNORECASE):
        issues.append('FAIL — Footer credit should be "Site by 3PM" not "Site by ThreePM"')

    # Copyright year
    if re.search(r'Copyright.*202[0-4]', content, re.IGNORECASE):
        issues.append('FAIL — Copyright year should be 2026, not 2024 or earlier')

    # Pre-footer CTAs
    pf_section = re.search(r'class="pre-footer".*?</section>', content, re.DOTALL | re.IGNORECASE)
    if pf_section:
        pf_text = pf_section.group(0)
        if 'Make an Enquiry' not in pf_text:
            issues.append('FAIL — Pre-footer missing "Make an Enquiry" CTA')
        if 'Need Help?' not in pf_text:
            issues.append('FAIL — Pre-footer missing "Need Help?" CTA')

    passed = len(issues) == 0
    return {
        'file': filepath,
        'pass': passed,
        'issues': issues,
        'warnings': warnings,
        'issue_count': len(issues),
        'warning_count': len(warnings),
    }


def print_result(result: dict, verbose: bool = True):
    """Print audit result for a single file."""
    filepath = result['file']
    filename = Path(filepath).name

    if result.get('error'):
        print(f'  ERROR  {filename}: {result["error"]}')
        return

    if result.get('exempt'):
        print(f'  SKIP   {filename} (exempt file)')
        return

    status = 'PASS' if result['pass'] else 'FAIL'
    icon = '✅' if result['pass'] else '❌'
    issue_count = result.get('issue_count', 0)
    warn_count = result.get('warning_count', 0)

    print(f'\n{icon} {status}  {filename}  ({issue_count} issues, {warn_count} warnings)')

    if verbose and result['issues']:
        for issue in result['issues']:
            print(f'       {issue}')

    if verbose and result.get('warnings'):
        for warn in result['warnings']:
            print(f'       {warn}')


def main():
    args = sys.argv[1:]

    if not args:
        print(__doc__)
        sys.exit(1)

    if '--all' in args:
        # Audit all page HTML files in current directory
        html_files = sorted(Path('.').glob('*.html'))
        files_to_audit = [str(f) for f in html_files if f.name not in EXEMPT_FILES]
    else:
        files_to_audit = args

    print('=' * 60)
    print('  IOR GOLDEN RULES AUDIT')
    print('=' * 60)

    results = [audit_file(f) for f in files_to_audit]

    total = len([r for r in results if not r.get('exempt') and not r.get('error')])
    passed = len([r for r in results if r.get('pass') and not r.get('exempt')])
    failed = total - passed
    total_issues = sum(r.get('issue_count', 0) for r in results)

    for result in results:
        print_result(result, verbose=True)

    print('\n' + '=' * 60)
    print(f'  SUMMARY: {passed}/{total} files passed | {total_issues} total issues')
    print('=' * 60)

    if failed > 0:
        print(f'\n  ❌ AUDIT FAILED — {failed} file(s) have issues. Fix before opening PR.\n')
        sys.exit(1)
    else:
        print(f'\n  ✅ ALL CHECKS PASSED — safe to open PR.\n')
        sys.exit(0)


if __name__ == '__main__':
    main()
