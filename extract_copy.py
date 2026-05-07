"""
Extract all visible copy verbatim from every Live-badged page.
Outputs a structured text file per page, then a combined master file.
READ-ONLY — does not modify any source files.
"""
from bs4 import BeautifulSoup, NavigableString, Comment
import re, os

LIVE_PAGES = [
    ("Homepage", "01_Homepage.html"),
    ("Fuel Solutions Hub", "02_Fuel_Solutions_Hub.html"),
    ("IOR Diesel Network", "03a_Diesel_Network_v8.html"),
    ("IOR Aviation Network", "04a_Aviation_Network_v8.html"),
    ("Digital Platforms Hub v5", "07_Digital_Platformsv5.html"),
    ("Fuelcharge App v8", "07b_Fuelcharge_App_v8.html"),
    ("Industries We Serve Hub", "08_Industries_v6.html"),
    ("Transport & Logistics", "08c_Transport_v6.html"),
    ("Our Leadership", "09a_Our_Leadershipv5.html"),
    ("Case Studies List v6", "09d_Case_Studies_v6.html"),
    ("Drew Morland — CEO", "09a_Bio_DrewMorland_v5.html"),
    ("Drew Leishman — COO", "09a_Bio_DrewLeishman_v5.html"),
    ("Adriaan Esterhuizen — CFO", "09a_Bio_AdriaanEsterhuizen_v5.html"),
    ("Nick Mackenzie — CSO", "09a_Bio_NickMackenzie_v5.html"),
    ("Bryce Morland — GM Aviation", "09a_Bio_BryceMorland_v5.html"),
    ("Chris Werfel — GM Supply", "09a_Bio_ChrisWerfel_v5.html"),
    ("Daniel Roberts — GM Ground Fuels", "09a_Bio_DanielRoberts_v5.html"),
    ("Hamish Jarrett — GM Technology", "09a_Bio_HamishJarrett_v5.html"),
    ("Nell Bond — GM Marketing", "09a_Bio_NellBond_v5.html"),
    ("Support & Contact Hub", "11_Support_Hubv5.html"),
    ("Contact Us", "11a_Contact_Usv5.html"),
    ("Regional Contacts", "11b_Regional_Contactsv5.html"),
    ("Make a Payment", "11e_Make_Paymentv5.html"),
    ("Privacy Policy", "11f_Privacy_Policyv5.html"),
]

# Tags to skip entirely (non-content)
SKIP_TAGS = {'script', 'style', 'noscript', 'meta', 'link', 'head',
             'nav', 'header', 'footer', 'svg', 'video', 'track', 'iframe'}

# Tags that signal a new heading level
HEADING_TAGS = {'h1': '# ', 'h2': '## ', 'h3': '### ', 'h4': '#### '}

# Tags that are inline (don't add newlines)
INLINE_TAGS = {'span', 'strong', 'em', 'a', 'b', 'i', 'u', 'small', 'sup', 'sub', 'mark'}

# Classes/IDs to skip (proto-bar, announcement bar, nav, footer, etc.)
SKIP_CLASSES = re.compile(
    r'proto-bar|ior-nav|ior-footer|ior-drawer|mega-menu|announcement|'
    r'cookie|breadcrumb|wf-nav|utility-bar|skip-link', re.I
)

BASE_URL = "https://alexc-sketch.github.io/ior-prototype-v3-5/"


def get_meta(soup, name):
    tag = soup.find('meta', attrs={'name': name}) or soup.find('meta', attrs={'property': name})
    return tag['content'].strip() if tag and tag.get('content') else ''


def extract_text(element, depth=0):
    """Recursively extract visible text with heading markers."""
    if isinstance(element, Comment):
        return ''
    if isinstance(element, NavigableString):
        text = str(element)
        # Strip whitespace-only strings
        if text.strip():
            return text
        return ''

    tag_name = element.name
    if not tag_name:
        return ''

    # Skip non-content tags
    if tag_name in SKIP_TAGS:
        return ''

    # Skip nav/footer/proto-bar by class or id
    classes = ' '.join(element.get('class', []))
    el_id = element.get('id', '')
    if SKIP_CLASSES.search(classes) or SKIP_CLASSES.search(el_id):
        return ''

    # Collect children text
    children_text = ''
    for child in element.children:
        children_text += extract_text(child, depth + 1)

    # Clean up whitespace
    children_text = re.sub(r'\n{3,}', '\n\n', children_text)
    children_text = children_text.strip()

    if not children_text:
        return ''

    # Apply heading markers
    if tag_name in HEADING_TAGS:
        return f"\n{HEADING_TAGS[tag_name]}{children_text}\n"

    # Block elements get newlines
    if tag_name in ('p', 'li', 'dt', 'dd', 'blockquote', 'figcaption', 'caption',
                    'th', 'td', 'label', 'div', 'section', 'article', 'aside',
                    'main', 'figure', 'address', 'pre'):
        return f"\n{children_text}\n"

    # Inline elements just return text
    return children_text


def extract_page(filepath, title, filename):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Get meta info
    page_title = soup.title.get_text(strip=True) if soup.title else title
    meta_desc = get_meta(soup, 'description') or get_meta(soup, 'og:description')
    
    # Get the body content only
    body = soup.find('body')
    if not body:
        return f"# {title}\n\n(No body content found)\n"

    raw_text = extract_text(body)
    # Clean up excessive blank lines
    cleaned = re.sub(r'\n{3,}', '\n\n', raw_text).strip()

    staging_url = f"{BASE_URL}{filename}"

    output = []
    output.append(f"{'='*80}")
    output.append(f"PAGE: {title}")
    output.append(f"{'='*80}")
    output.append(f"STAGING LINK: {staging_url}")
    output.append(f"META TITLE: {page_title}")
    output.append(f"META DESCRIPTION: {meta_desc}")
    output.append(f"{'─'*80}")
    output.append("")
    output.append(cleaned)
    output.append("")

    return '\n'.join(output)


# Run extraction
os.makedirs('/home/ubuntu/ior_copy_export', exist_ok=True)
master_parts = []
master_parts.append("IOR PROTOTYPE — LIVE PAGES COPY EXPORT")
master_parts.append("Extracted verbatim from source HTML files. Read-only. No source files modified.")
master_parts.append(f"Total pages: {len(LIVE_PAGES)}")
master_parts.append("")

for title, filename in LIVE_PAGES:
    filepath = f"/tmp/ior-prototype-v3-5/{filename}"
    if not os.path.exists(filepath):
        print(f"  ⚠️  File not found: {filename}")
        continue
    print(f"  Extracting: {title} ({filename})")
    content = extract_page(filepath, title, filename)
    # Save individual file
    safe_name = re.sub(r'[^\w\-]', '_', title)
    with open(f'/home/ubuntu/ior_copy_export/{safe_name}.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    master_parts.append(content)
    master_parts.append("\n\n")

# Write master file
master_text = '\n'.join(master_parts)
with open('/home/ubuntu/ior_copy_export/IOR_ALL_PAGES_COPY.txt', 'w', encoding='utf-8') as f:
    f.write(master_text)

print(f"\n✅ Done. Master file: /home/ubuntu/ior_copy_export/IOR_ALL_PAGES_COPY.txt")
print(f"   Size: {len(master_text):,} characters")
