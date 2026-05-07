"""
Extract all visible copy from all Live pages for E-E-A-T audit.
Reads local files where possible, fetches remote URLs for pages in other repos.
Zero edits to source files.
"""
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup
import urllib.request

BASE_DIR = Path("/tmp/ior-prototype-v3-5")
BASE_URL = "https://alexc-sketch.github.io/ior-prototype-v3-5/"

LIVE_PAGES = [
    ("Homepage", "01_Homepage.html"),
    ("Fuel Solutions Hub", "02_Fuel_Solutions_Hub.html"),
    ("Digital Platforms Hub v5", "07_Digital_Platformsv5.html"),
    ("Industries We Serve Hub", "08_Industries_v6.html"),
    ("Support & Contact Hub", "11_Support_Hubv5.html"),
    ("Ground Fuels Hub", "03_Ground_Fuels_v8.html"),
    ("IOR Diesel Network", "03a_Diesel_Network_v8.html"),
    ("On-Site Refuelling", "03b_On_Site_Refuelling_v9.html"),
    ("Bulk Diesel Delivery", "03c_Bulk_Diesel_Delivery_v9.html"),
    ("HyBlue™ AdBlue®", "03d_HyBlue_v8.html"),
    ("Oils & Lubricants", "03e_Oils_Lubricants_v9.html"),
    ("Aviation Hub", "https://alexc-sketch.github.io/ior-prototype/04_Aviation_Hub_v9.html"),
    ("IOR Aviation Network", "04a_Aviation_Network_v8.html"),
    ("Airport Fuelling Services", "https://alexc-sketch.github.io/ior-prototype/04b_Airport_Fuelling_v9.html"),
    ("Aviation Bulk Delivery", "https://alexc-sketch.github.io/ior-prototype/04c_Aviation_Bulk_Delivery_v9.html"),
    ("Aviation Oils & Lubricants", "https://alexc-sketch.github.io/ior-prototype/04d_Aviation_Oils_v9.html"),
    ("Equipment & Infrastructure Hub", "https://alexc-sketch.github.io/ior-prototype/05_Equipment_Infrastructure_v8.html"),
    ("Fuel Storage Tanks", "https://alexc-sketch.github.io/ior-prototype/05a_Fuel_Storage_Tanks_v8.html"),
    ("Frac Tanks", "https://alexc-sketch.github.io/ior-prototype/05b_Frac_Tanks_v8.html"),
    ("Supply & Trading Hub", "https://alexc-sketch.github.io/ior-prototype-v3-5/06_Supply_Trading_v8.html"),
    ("Lytton & Port Bonython", "https://alexc-sketch.github.io/ior-prototype/06a_Terminals_v8.html"),
    ("Eromanga Refinery", "https://alexc-sketch.github.io/ior-prototype-v3-5/06b_Eromanga_v8.html"),
    ("Fuelcharge App v8", "07b_Fuelcharge_App_v8.html"),
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
    ("Contact Us", "11a_Contact_Usv5.html"),
    ("Regional Contacts", "11b_Regional_Contactsv5.html"),
    ("Find a Location", "https://alexc-sketch.github.io/ior-prototype-v3-5/11d_Find_Locationv5.html"),
    ("Make a Payment", "11e_Make_Paymentv5.html"),
    ("Privacy Policy", "11f_Privacy_Policyv5.html"),
]

SKIP_TAGS = {"script", "style", "noscript", "svg", "path", "meta", "link", "head"}
SKIP_CLASSES = {"proto-bar", "nav", "footer", "breadcrumb", "wf-nav", "ior-nav", "site-footer", "pre-footer"}

def get_html(href):
    if href.startswith("http"):
        try:
            req = urllib.request.Request(href, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                return r.read().decode("utf-8", errors="replace")
        except Exception as e:
            return None
    else:
        local = BASE_DIR / href
        if local.exists():
            return local.read_text(encoding="utf-8")
        return None

def extract_copy(html):
    soup = BeautifulSoup(html, "html.parser")
    
    # Get meta title and description
    title = soup.find("title")
    meta_desc = soup.find("meta", attrs={"name": "description"})
    title_text = title.get_text(strip=True) if title else ""
    desc_text = meta_desc.get("content", "") if meta_desc else ""
    
    # Remove non-content elements
    for tag in soup.find_all(SKIP_TAGS):
        tag.decompose()
    for cls in SKIP_CLASSES:
        for el in soup.find_all(class_=re.compile(cls, re.I)):
            el.decompose()
    # Remove proto-bar, nav, footer by id or role
    for el in soup.find_all(["nav", "footer", "header"]):
        el.decompose()
    for el in soup.find_all(id=re.compile("nav|footer|proto|header", re.I)):
        el.decompose()
    
    # Extract headings and paragraphs
    body = soup.find("body") or soup
    lines = []
    for el in body.find_all(["h1","h2","h3","h4","h5","p","li","blockquote","figcaption","label","span","div"]):
        # Only get direct text, skip deeply nested duplicates
        text = el.get_text(" ", strip=True)
        if len(text) > 20 and text not in lines:
            lines.append(text)
    
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for line in lines:
        clean = re.sub(r'\s+', ' ', line).strip()
        if clean and clean not in seen and len(clean) > 20:
            seen.add(clean)
            unique.append(clean)
    
    return {
        "meta_title": title_text,
        "meta_desc": desc_text,
        "copy": unique
    }

results = {}
for name, href in LIVE_PAGES:
    print(f"  Extracting: {name}...", end=" ", flush=True)
    html = get_html(href)
    if html:
        data = extract_copy(html)
        data["href"] = href
        results[name] = data
        print(f"✅ ({len(data['copy'])} blocks)")
    else:
        results[name] = {"href": href, "meta_title": "", "meta_desc": "", "copy": [], "error": "Could not fetch"}
        print("⚠️  Could not fetch")

# Save to JSON for audit processing
out = Path("/home/ubuntu/eeat_copy_data.json")
out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\n✅ Saved to {out}")
