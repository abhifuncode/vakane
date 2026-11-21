# -*- coding: utf-8 -*-
"""Static site generator. Run from anywhere:  python3 src/build.py
Output goes to ../site (open site/index.html, or deploy that folder)."""
import os
import shutil
from html import escape as e

from data import BRAND, CATEGORIES, SERVICES, COUNTRIES, ARTICLES, TEAM, FAQ_HOME
from templates import KINDS

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(ROOT), "site")
FORM_ENDPOINT = ""  # e.g. "https://formspree.io/f/xxxx" — leave empty to use the visitor's mail app

CAT = {c["slug"]: c for c in CATEGORIES}
SVC = {s["slug"]: s for s in SERVICES}
for c in CATEGORIES:
    c["items"] = [s for s in SERVICES if s["cat"] == c["slug"]]

# ---------------------------------------------------------------- icons
ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M2 8h12M9 3l5 5-5 5"/></svg>'
CHEV = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M2 4l4 4 4-4"/></svg>'
CHECK = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="10" cy="10" r="8.2"/><path d="M6.5 10.2l2.3 2.3 4.7-4.9"/></svg>'
SEARCH = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="9" cy="9" r="6.5"/><path d="M14 14l4 4"/></svg>'
ICONS = [
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 5.5 3.8 9S14.5 18.5 12 21c-2.5-2.5-3.8-5.5-3.8-9S9.5 5.5 12 3z"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
]
LOGO = ('<img class="logo-mark" src="assets/logo-mark.png" alt="" width="77" height="40">'
        '<span class="logo-text"><img src="assets/logo-word.png" alt="Vakane" width="100" height="17"><small>Engineering</small></span>')
LOGO_FOOTER = '<img class="logo-full" src="assets/logo-light.png" alt="Vakane Engineering" width="132" height="90">'
WA = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.2-.3-.3-.5-.4z"/></svg>'


def href(slug):
    return "index.html" if slug == "index" else slug + ".html"


# ---------------------------------------------------------------- layout
def header(active=""):
    def nl(slug, label):
        cls = " active" if active == slug else ""
        return '<div class="nav-item"><a class="nav-link%s" href="%s">%s</a></div>' % (cls, href(slug), label)

    about_links = [
        ("about", "Our story", "Who we are and how we work"),
        ("team", "Leadership", "The people behind every project"),
        ("clients", "Clients & industries", "Sectors we serve"),
        ("partners", "Certification partners", "Labs, bodies and networks"),
        ("recognition", "Recognition", "Accreditations and memberships"),
        ("offices", "Offices", "Where to find us"),
    ]
    about = "".join('<a href="%s">%s<small>%s</small></a>' % (href(s), l, d) for s, l, d in about_links)
    left = "".join('<a href="%s"><span class="num">%s</span><b>%s</b></a>' % (href(c["slug"]), c["num"], e(c["name"])) for c in CATEGORIES[:5])
    right = "".join('<a href="%s"><span class="num">%s</span><b>%s</b></a>' % (href(c["slug"]), c["num"], e(c["name"])) for c in CATEGORIES[5:])
    right += '<a href="%s"><span class="num">→</span><b>Country guides</b></a>' % href("countries")
    mega = ('<div class="dropdown mega"><div>%s</div><div>%s</div>'
            '<div class="mega-feature"><span class="eyebrow">Not sure?</span><h4>Find the right certificate in one call.</h4>'
            '<p>Tell us your product and target market. We will map every approval you need.</p>'
            '<a class="link-arrow" href="contact.html">Ask an expert %s</a></div></div>') % (left, right, ARROW)

    def drop(slug_set, label, inner):
        cls = " active" if active in slug_set else ""
        return ('<div class="nav-item has-drop"><button class="nav-link%s" aria-expanded="false">%s %s</button>%s</div>'
                % (cls, label, CHEV, inner))

    about_set = {s for s, _, _ in about_links}
    svc_set = {"services", "countries"} | set(CAT)
    nav = (nl("index", "Home") + drop(about_set, "About", '<div class="dropdown">%s</div>' % about)
           + drop(svc_set, "Services", mega) + nl("countries", "Countries") + nl("insights", "Insights") + nl("contact", "Contact")
           + '<a class="btn btn-primary mobile-cta" href="contact.html">Get a free quote %s</a>' % ARROW)
    return """
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="container">
  <div class="tb-left">Product, ISO &amp; export certification — India and 50+ markets</div>
  <div class="tb-right"><a href="tel:{tel}">{phone}</a><a href="mailto:{email}">{email}</a></div>
</div></div>
<header class="header"><div class="container">
  <a class="logo" href="index.html" aria-label="{name} home">{logo}</a>
  <nav class="nav" aria-label="Main">{nav}</nav>
  <a class="btn btn-primary btn-sm header-cta" href="contact.html">Get a free quote {arrow}</a>
  <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
</div></header>""".format(tel=BRAND["phone"].replace(" ", ""), phone=BRAND["phone"], email=BRAND["email"],
                          name=BRAND["name"], logo=LOGO, nav=nav, arrow=ARROW)


def footer():
    cats = "".join('<li><a href="%s">%s</a></li>' % (href(c["slug"]), e(c["name"])) for c in CATEGORIES[:5])
    cats2 = "".join('<li><a href="%s">%s</a></li>' % (href(c["slug"]), e(c["name"])) for c in CATEGORIES[5:])
    pop = ["bis-certification", "bis-crs", "ce-marking", "iso-9001", "ul-certification", "fda-food-registration", "wpc-eta", "epr-registration"]
    popl = "".join('<li><a href="%s">%s</a></li>' % (href(s), e(SVC[s]["name"])) for s in pop)
    socials = "".join('<a href="%s" aria-label="%s">%s</a>' % (u, k, k) for k, u in BRAND["socials"].items())
    return """
<footer class="footer"><div class="container">
  <div class="footer-top">
    <div class="footer-about">
      <a class="logo logo-footer" href="index.html">{logo}</a>
      <p>An independent certification and compliance partner helping businesses reach regulated markets faster — with one team from first question to final certificate.</p>
      <div class="socials">{socials}</div>
    </div>
    <div><h4>Services</h4><ul>{cats}</ul></div>
    <div><h4>&nbsp;</h4><ul>{cats2}<li><a href="countries.html">Country guides</a></li></ul></div>
    <div><h4>Popular</h4><ul>{popl}</ul></div>
    <div><h4>Contact</h4><ul>
      <li><a href="tel:{tel}">{phone}</a></li>
      <li><a href="mailto:{email}">{email}</a></li>
      <li>{address}</li>
      <li><a href="about.html">About us</a></li>
      <li><a href="insights.html">Insights</a></li>
    </ul></div>
  </div>
  <div class="footer-big">{name}.</div>
  <div class="footer-bottom">
    <div>© <span data-year>2026</span> {legal}. All rights reserved.</div>
    <nav><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="sitemap.html">Sitemap</a></nav>
  </div>
</div></footer>
<a class="wa-float" href="https://wa.me/{wa}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{wa_icon}</a>
""".format(logo=LOGO_FOOTER, name=BRAND["name"], socials=socials, cats=cats, cats2=cats2, popl=popl,
           tel=BRAND["phone"].replace(" ", ""), phone=BRAND["phone"], email=BRAND["email"],
           address=e(BRAND["address"]), legal=e(BRAND["legal"]), wa=BRAND["whatsapp"], wa_icon=WA)


def page(slug, title, desc, content, active=""):
    full_title = "%s — %s" % (title, BRAND["name"]) if slug != "index" else "%s — %s" % (BRAND["name"], BRAND["tagline"])
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#FAFAF8">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta property="og:image" content="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
{header}
<main id="main">
{content}
</main>
{footer}
<script src="assets/main.js" defer></script>
</body>
</html>""".format(title=e(full_title), desc=e(desc), header=header(active or slug), content=content, footer=footer())
    with open(os.path.join(OUT, href(slug)), "w", encoding="utf-8") as f:
        f.write(html)
    PAGES.append((slug, title))


PAGES = []


# ---------------------------------------------------------------- components
def crumbs(*parts):
    out = ['<a href="index.html">Home</a>']
    for p in parts:
        out.append('<span aria-hidden="true">/</span>')
        out.append('<a href="%s">%s</a>' % (href(p[0]), e(p[1])) if p[0] else '<span>%s</span>' % e(p[1]))
    return '<nav class="crumbs" aria-label="Breadcrumb">%s</nav>' % "".join(out)


def img(name, alt="", cls="", sizes="(max-width: 960px) 100vw, 50vw", eager=False):
    return ('<img class="%s" src="assets/img/%s-sm.webp" srcset="assets/img/%s-sm.webp 820w, assets/img/%s.webp 1600w" sizes="%s" alt="%s" loading="%s" decoding="async">'
            % (cls, name, name, name, sizes, e(alt), "eager" if eager else "lazy"))


def gear_svg(cls="gear-spin", teeth=12):
    import math
    pts = []
    R, r = 100, 84
    for i in range(teeth):
        a0 = 2 * math.pi * i / teeth
        step = 2 * math.pi / teeth
        for frac, rad in ((0.0, r), (0.18, r), (0.26, R), (0.5, R), (0.58, r)):
            a = a0 + step * frac
            pts.append("%.1f,%.1f" % (110 + rad * math.cos(a), 110 + rad * math.sin(a)))
    return ('<svg class="%s" viewBox="0 0 220 220" aria-hidden="true"><polygon points="%s" fill="none" stroke="currentColor" stroke-width="1.2"/>'
            '<circle cx="110" cy="110" r="52" fill="none" stroke="currentColor" stroke-width="1.2"/>'
            '<circle cx="110" cy="110" r="14" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>' % (cls, " ".join(pts)))


def page_hero(crumb, eyebrow, h1, lead, side="", image=None):
    if image:
        inner = ('<div class="page-hero-grid"><div><span class="eyebrow">%s</span><h1 class="hero-title">%s</h1><p class="lead">%s</p></div>%s</div>'
                 % (e(eyebrow), h1, lead, side)) if side else (
                 '<span class="eyebrow">%s</span><h1 class="hero-title">%s</h1><p class="lead">%s</p>' % (e(eyebrow), h1, lead))
        return ('<section class="page-hero hero-img"><div class="ph-bg" data-parallax="0.18">%s</div><div class="ph-shade"></div>%s'
                '<div class="container">%s%s</div></section>' % (img(image, "", "kb", "100vw", True), gear_svg("gear-spin ph-gear"), crumb, inner))
    if side:
        return ('<section class="page-hero"><div class="container">%s<div class="page-hero-grid"><div>'
                '<span class="eyebrow">%s</span><h1>%s</h1><p class="lead">%s</p></div>%s</div></div></section>'
                % (crumb, e(eyebrow), h1, lead, side))
    return ('<section class="page-hero"><div class="container">%s<span class="eyebrow">%s</span><h1>%s</h1>'
            '<p class="lead">%s</p></div></section>' % (crumb, e(eyebrow), h1, lead))


def faq_block(items):
    return '<div class="faq">%s</div>' % "".join(
        '<details><summary>%s<span class="pm" aria-hidden="true"></span></summary><div class="a">%s</div></details>' % (e(q), e(a))
        for q, a in items)


def cta_band(title="Ready when you are.", text="Tell us what you make and where you want to sell it. You'll have a clear plan, timeline and fixed quote within one business day."):
    return """<div class="cta-band"><div class="container"><div class="cta-inner reveal">
  <div class="cta-bg" data-parallax="0.12">{img}</div>
  <div><h2>{t}</h2><p>{x}</p></div>
  <div class="cta-actions"><a class="btn btn-accent2" href="contact.html">Get a free quote {a}</a><a class="btn btn-ghost" href="tel:{tel}">Call {phone}</a></div>
</div></div></div>""".format(t=title, x=e(text), a=ARROW, tel=BRAND["phone"].replace(" ", ""), phone=BRAND["phone"],
                             img=img("cta-welding", "", "", "100vw"))


def enquiry_form(compact=False, preset=""):
    opts = "".join('<option%s>%s</option>' % (" selected" if preset == c["name"] else "", e(c["name"])) for c in CATEGORIES)
    org = "" if compact else '<div class="field"><label for="f-org">Company</label><input id="f-org" name="company" autocomplete="organization"></div>'
    msg_rows = "" if compact else ' rows="5"'
    return """<form class="form" data-endpoint="{ep}" data-mailto="{mail}" novalidate>
  <div class="form-row">
    <div class="field"><label for="f-name">Full name *</label><input id="f-name" name="name" required autocomplete="name"></div>
    <div class="field"><label for="f-phone">Phone *</label><input id="f-phone" name="phone" type="tel" required autocomplete="tel"></div>
  </div>
  <div class="form-row">
    <div class="field"><label for="f-email">Work email *</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
    {org}
    {svc}
  </div>
  {svc2}
  <div class="field"><label for="f-msg">What do you need certified?</label><textarea id="f-msg" name="message"{rows} placeholder="Product, target market, timeline…"></textarea></div>
  <button class="btn btn-primary" type="submit">Send enquiry {a}</button>
  <p class="form-note">We reply within one business day. Your details are never shared.</p>
  <div class="form-success" role="status">Thank you — your enquiry is on its way. A specialist will contact you within one business day.</div>
</form>""".format(ep=FORM_ENDPOINT, mail=BRAND["email"], org=org,
                  svc=('<div class="field"><label for="f-svc">Service</label><select id="f-svc" name="service"><option value="">Select a service</option>%s</select></div>' % opts) if compact else "",
                  svc2=("" if compact else '<div class="field"><label for="f-svc">Service of interest</label><select id="f-svc" name="service"><option value="">Select a service</option>%s</select></div>' % opts),
                  rows=msg_rows, a=ARROW)


def svc_card(s):
    tags = "|".join(s["tags"])
    top = s["region"] or CAT[s["cat"]]["name"]
    tl = s["timeline"]
    return ('<a class="svc" href="%s" data-name="%s" data-tags="%s"><div class="top"><span>%s</span><span>%s</span></div>'
            '<h3>%s</h3><div class="full">%s</div><p>%s</p><span class="link-arrow">Learn more %s</span></a>'
            % (href(s["slug"]), e((s["name"] + " " + s["full"] + " " + s["region"] + " " + " ".join(s["tags"])).lower()), e(tags),
               e(top), e(tl), e(s["name"]), e(s["full"]), e(s["blurb"]), ARROW))


def steps_block(steps):
    return '<div class="steps">%s</div>' % "".join(
        '<div class="step reveal"><div class="k">%s</div><h3>%s</h3><p>%s</p></div>' % (k, t, x) for k, t, x in steps)


HOW = [
    ("01", "Tell us what you make", "Share your product, site or service and the markets you want to reach."),
    ("02", "Get a clear plan", "A written roadmap with every approval, the timeline and a fixed quote — within one business day."),
    ("03", "We do the heavy lifting", "Documents, testing, applications, audits and regulator queries — managed by one dedicated specialist."),
    ("04", "Certified, and kept that way", "We track renewals, surveillance audits and rule changes so your certificates never lapse."),
]
WHY = [
    ("One accountable specialist", "A single named expert owns your project from start to finish. No hand-offs, no repeating yourself."),
    ("Fixed, transparent pricing", "Professional fees, lab fees and government fees itemised upfront. What we quote is what you pay."),
    ("Speed without shortcuts", "Pre-checked documents and the right lab first time mean fewer queries and faster grants."),
    ("Every market, one partner", "Indian, European, American, Gulf and African approvals coordinated by the same team."),
    ("Real-time updates", "Weekly status reports and a direct line to your specialist — on WhatsApp, email or phone."),
    ("Long-term care", "Renewal reminders, model additions and regulatory alerts long after the certificate arrives."),
]
INDUSTRIES = [("Electronics & IT", "ind-electronics"), ("Electrical & lighting", "ind-electrical"), ("Machinery", "ind-machinery"),
              ("Automotive & EV", "ind-automotive"), ("Medical devices", "ind-medical"), ("Pharma & AYUSH", "ind-pharma"),
              ("Food & beverage", "ind-food"), ("Textiles & apparel", "ind-textiles"), ("Chemicals", "ind-chemicals"),
              ("Construction & steel", "ind-construction"), ("Consumer goods & export", "ind-consumer"), ("Software & SaaS", "ind-saas")]

CAT_IMG = {
    "management-system-certification": "cat-msys", "industry-specific-certification": "cat-industry",
    "product-certification": "cat-product", "customer-compliance-audit": "cat-audit", "business-process-training": "cat-training",
    "accreditation": "cat-accreditation", "inspection-services": "cat-inspection", "compliance-reports": "cat-report",
    "information-security": "cat-security",
}
ARTICLE_IMG = {"bis-vs-isi-explained": "cat-product", "ce-marking-in-six-steps": "ind-electronics", "preparing-for-iso-stage-2": "cat-msys",
               "cbam-for-indian-exporters": "ind-construction", "soc2-vs-iso27001": "cat-security", "epr-plastic-packaging": "ind-consumer"}
KEYWORD_IMG = [
    (("food", "fssai", "haccp", "fssc", "brcgs", "kosher", "halal", "eat right", "globalg", "organic", "proterra", "fairtrade"), "ind-food"),
    (("medical", "device", "510", "drug", "cosmetic", "cdsco", "ayush", "icmed", "who", "nabh", "15189", "gmp", "sfda", "health canada"), "ind-medical"),
    (("textile", "gots", "oeko", "grs", "leather", "slcp", "higg", "scope cert", "sedex", "smeta", "bsci"), "ind-textiles"),
    (("automotive", "vehicle", "iatf", "e-mark", "ais", "aerospace", "as9100"), "ind-automotive"),
    (("machinery", "pressure", "atex", "scheme-x", "pellet", "pallet", "esd"), "ind-machinery"),
    (("chemical", "reach", "kkdik", "rohs"), "ind-chemicals"),
    (("cable", "electrical", "ul ", "etl", "csa", "vde", "nema", "basec", "kitemark"), "ind-electrical"),
    (("steel", "weld", "construction", "bre", "cares", "fire", "vds", "fm global", "wras", "dinplus", "cbam", "carbon", "lca"), "ind-construction"),
    (("telecom", "tec", "wireless", "wpc", "fcc", "electronics", "crs", "kc mark", "ccc", "bis certification", "it security"), "ind-electronics"),
    (("saso", "saber", "soncap", "kucas", "nom", "eac", "gulf", "emirates", "export", "pvoc", "container", "shipment"), "export-port"),
]


def service_image(s):
    hay = (" ".join([s["name"], s["full"], s["blurb"]] + s["tags"]) + " ").lower()
    if s["cat"] in ("product-certification", "industry-specific-certification", "customer-compliance-audit"):
        for keys, im in KEYWORD_IMG:
            if any(k in hay for k in keys):
                return im
    return CAT_IMG[s["cat"]]


def split_words(text, start=0):
    out = []
    for i, w in enumerate(text.split(" ")):
        out.append('<span class="w"><span style="--i:%d">%s</span></span>' % (start + i, w))
    return " ".join(out)


# ---------------------------------------------------------------- pages
def build_home():
    n_services = len(SERVICES)
    marks = ["BIS", "ISI Mark", "BIS CRS", "CE Marking", "UKCA", "UL", "FCC", "US FDA", "ISO 9001", "ISO 27001", "ISO 14001", "HACCP",
             "FSSC 22000", "SASO", "EAC", "CCC", "WPC", "EPR", "SOC 2", "NABL", "SMETA", "GOTS"]
    marquee = "".join("<span>%s</span>" % m for m in marks) * 2
    cats = "".join("""<a class="scard reveal spot" href="{h}"><div class="scard-img">{im}<span class="scard-num">{n}</span></div>
<div class="scard-body"><h3>{t}</h3><p>{s}</p><div class="scard-foot"><span class="count">{c} services</span><span class="arrow">{a}</span></div></div></a>""".format(
        h=href(c["slug"]), n=c["num"], a=ARROW, t=e(c["name"]), s=e(c["short"]), c=len(c["items"]),
        im=img(CAT_IMG[c["slug"]], c["name"], "", "(max-width: 640px) 100vw, (max-width: 960px) 50vw, 33vw")) for c in CATEGORIES)
    popular = ["bis-certification", "isi-mark", "bis-crs", "ce-marking", "iso-9001", "iso-27001", "ul-certification", "fda-food-registration",
               "wpc-eta", "epr-registration", "saso-saber", "haccp", "soc-2", "nabl-accreditation", "smeta-audit", "carbon-footprint"]
    chips = "".join('<a class="chip reveal" href="%s">%s %s</a>' % (href(s), e(SVC[s]["name"]), ARROW) for s in popular)
    why = "".join('<div class="feature reveal"><div class="ic">%s</div><div><h3>%s</h3><p>%s</p></div></div>' % (ICONS[i % 6], t, x)
                  for i, (t, x) in enumerate(WHY))
    inds = "".join('<a class="itile reveal" href="services.html">%s<span class="itile-n">%02d</span><span class="itile-t">%s</span></a>'
                   % (img(im, n, "", "(max-width: 640px) 50vw, 25vw"), i + 1, e(n)) for i, (n, im) in enumerate(INDUSTRIES))
    posts = "".join(post_card(a) for a in ARTICLES[:3])
    countries = "".join('<a class="chip chip-glass" href="%s">%s</a>' % (href("country-" + c[0]), e(c[1])) for c in COUNTRIES[:10])
    steps = "".join('<div class="step reveal"><div class="k">%s</div><h3>%s</h3><p>%s</p></div>' % x for x in HOW)
    content = """
<section class="hero hero-home">
  <div class="hero-glow" aria-hidden="true"></div>
  <div class="container hero-grid">
    <div class="hero-copy">
      <span class="eyebrow fade-in" style="--i:0">Certification &amp; compliance partner</span>
      <h1 class="split-words">{h1a} <em>{h1b}</em> {h1c}</h1>
      <p class="lead fade-in" style="--i:6">BIS, ISO, CE, FDA and {n}+ other approvals — scoped, managed and delivered by one specialist engineering team, so you can get to market and stay there.</p>
      <div class="hero-actions fade-in" style="--i:7">
        <a class="btn btn-primary magnetic" href="contact.html">Get a free assessment {a}</a>
        <a class="btn btn-ghost" href="services.html">Explore services</a>
      </div>
      <div class="hero-trust fade-in" style="--i:8">
        <div><strong data-count="{n}" data-suffix="+">0</strong>certification schemes</div>
        <div><strong data-count="{cc}">0</strong>country guides</div>
        <div><strong data-count="24" data-suffix="h">0</strong>response to every enquiry</div>
      </div>
    </div>
    <div class="collage" data-tilt>
      {gear}
      <div class="c-main reveal-img">{im_main}</div>
      <div class="c-sub reveal-img" style="--d:.35s">{im_sub}</div>
      <div class="c-tag reveal-img" style="--d:.55s">{im_tag}</div>
      <div class="badge b1" data-depth="18">
        <span class="b-ic">{check}</span><div><b>Documents verified</b><small>Technical file · 42 items</small></div>
      </div>
      <div class="badge b2" data-depth="-14">
        <div class="b-row"><b>Lab testing</b><small>In progress</small></div>
        <div class="bar"><span></span></div>
      </div>
      <div class="badge b3" data-depth="10">
        <span class="b-ic amber">{check}</span><div><b>Certificate issued</b><small>Ready to ship</small></div>
      </div>
      <div class="sparks" aria-hidden="true">{sparks}</div>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee}</div></div>

<section><div class="container">
  <div class="section-head"><div><span class="eyebrow">What we do</span><h2 class="split-on-view">Nine practices. One point of contact.</h2></div>
  <p class="reveal">From a single product mark to a full management system, every engagement is run by specialists who do nothing else.</p></div>
  <div class="scard-grid" data-stagger>{cats}</div>
</div></section>

<section class="section-sm bg-surface"><div class="container split">
  <div><span class="eyebrow">Most requested</span><h2 class="h2" style="margin-top:14px">Popular certifications</h2>
  <p class="muted" style="margin-top:16px">Jump straight to the guide you need — or browse the full catalogue of {n}+ services.</p>
  <a class="link-arrow" href="services.html">View all services {a}</a></div>
  <div class="chips" data-stagger>{chips}</div>
</div></section>

<section class="bg-ink how">
  <div class="how-bg" data-parallax="0.15">{im_how}</div>
  <div class="container" style="position:relative">
  <div class="section-head"><div><span class="eyebrow">How it works</span><h2>From question to certificate in four steps.</h2></div>
  <p>A simple, predictable process — whichever certification you need.</p></div>
  <div class="steps-wrap"><div class="steps-line"><span></span></div><div class="steps" data-stagger>{steps}</div></div>
</div></section>

<section><div class="container split why">
  <div class="sticky">
    <span class="eyebrow">Why {brand}</span><h2 class="h2" style="margin-top:14px">A calmer way to get certified.</h2>
    <p class="lead" style="margin-top:20px">Certification is rarely hard because of the standard. It's hard because of unclear requirements, slow labs and silent regulators. We remove that friction.</p>
    <div class="why-media reveal-img"><div class="why-img" data-parallax="-0.08">{im_why}</div>
      <div class="why-card"><strong data-count="1">0</strong><span>named specialist from first call to final certificate</span></div></div>
  </div>
  <div class="features" data-stagger>{why}</div>
</div></section>

<section class="section-sm bg-warm"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Industries</span><h2>Built for regulated products.</h2></div>
  <p class="reveal">Deep, hands-on experience across the sectors where compliance decides who gets to sell.</p></div>
  <div class="itile-grid" data-stagger>{inds}</div>
</div></section>

<section class="band">
  <div class="band-bg" data-parallax="0.22">{im_port}</div>
  <div class="container band-inner">
    <span class="eyebrow">Export compliance</span>
    <h2 class="split-on-view">Shipping abroad? We know the paperwork at the other end.</h2>
    <p class="reveal">Country-by-country guidance for {cc} markets — from CE and UL to SASO, SONCAP and EAC.</p>
    <div class="chips reveal">{countries}</div>
    <a class="btn btn-light reveal" href="countries.html">All country guides {a}</a>
  </div>
</section>

<section><div class="container">
  <div class="section-head"><div><span class="eyebrow">Insights</span><h2>Plain-English guides.</h2></div>
  <a class="link-arrow" href="insights.html">All articles {a}</a></div>
  <div class="post-grid" data-stagger>{posts}</div>
</div></section>

<section class="bg-warm quote-sec"><div class="container split">
  <div>
    <span class="eyebrow">Free assessment</span><h2 class="h2" style="margin-top:14px">Tell us what you make. We'll map every approval.</h2>
    <p class="lead" style="margin-top:20px">Within one business day you'll have the approvals you need, a realistic timeline and a fixed, itemised quote.</p>
    <ul class="checklist" style="margin-top:28px">
      <li>{check}<span>No obligation, no cost for the assessment</span></li>
      <li>{check}<span>Professional, lab and government fees itemised</span></li>
      <li>{check}<span>One named specialist for your whole project</span></li>
    </ul>
  </div>
  <div class="card quote-card reveal">{form}</div>
</div></section>

<section><div class="container split">
  <div><span class="eyebrow">FAQ</span><h2 class="h2" style="margin-top:14px">Questions we hear every day.</h2>
  <p class="muted" style="margin-top:16px">Can't find your answer? <a href="contact.html" style="text-decoration:underline">Ask us directly</a>.</p></div>
  {faq}
</div></section>
{cta}
""".format(n=n_services, cc=len(COUNTRIES), a=ARROW, check=CHECK, form=enquiry_form(compact=True), marquee=marquee, cats=cats, chips=chips,
           steps=steps, brand=BRAND["name"], why=why, inds=inds, posts=posts, faq=faq_block(FAQ_HOME), cta=cta_band(), countries=countries,
           h1a=split_words("Certification,", 1), h1b=split_words("without", 2), h1c=split_words("the guesswork.", 3),
           gear=gear_svg("gear-spin hero-gear"), sparks="".join('<i style="--a:%ddeg;--t:%.2fs"></i>' % (200 + k * 14, 0.9 + (k % 4) * 0.35) for k in range(10)),
           im_main=img("hero-laser", "Laser cutting machine cutting sheet metal with sparks", "kb", "(max-width: 960px) 100vw, 40vw", True),
           im_sub=img("hero-lab", "Scientist testing samples in a laboratory", "", "(max-width: 960px) 50vw, 20vw", True),
           im_tag=img("hero-inspect", "Engineer inspecting equipment in a factory", "", "(max-width: 960px) 40vw, 15vw", True),
           im_how=img("about-engineers", "", "", "100vw"), im_why=img("about-cnc", "CNC machining workshop", "", "(max-width: 960px) 100vw, 45vw"),
           im_port=img("export-port", "", "", "100vw"))
    page("index", "Home", "Independent certification and compliance consultants for BIS, ISI, ISO, CE, UL, FDA and %d+ approvals in India and worldwide." % n_services, content)


def post_card(a):
    return ('<a class="post reveal spot" href="%s"><div class="post-img">%s</div><div class="post-body"><div class="meta"><span class="tag">%s</span><span>%s</span><span>·</span><span>%s read</span></div>'
            '<h3>%s</h3><p>%s</p><span class="link-arrow">Read article %s</span></div></a>'
            % (href(a["slug"]), img(ARTICLE_IMG.get(a["slug"], "cat-msys"), a["title"], "", "(max-width: 640px) 100vw, 33vw"),
               e(a["tag"]), e(a["date"]), e(a["read"]), e(a["title"]), e(a["excerpt"]), ARROW))


def build_services_index():
    blocks = ""
    for c in CATEGORIES:
        links = "".join('<a href="%s">%s<span>%s</span></a>' % (href(s["slug"]), e(s["name"]), e(s["region"] or s["timeline"] or ""))
                        for s in c["items"])
        blocks += ('<div class="cat-block reveal"><div><span class="eyebrow">%s</span><h2>%s</h2><p>%s</p>'
                   '<a class="link-arrow" href="%s">Overview %s</a></div><div class="cat-links">%s</div></div>'
                   % (c["num"], e(c["name"]), e(c["short"]), href(c["slug"]), ARROW, links))
    content = page_hero(crumbs((None, "Services")), "Services", "Everything you need to sell with confidence.",
                        "%d services across nine practices — covering product marks, management systems, audits, accreditation, inspection, ESG and cyber security." % len(SERVICES), image="hero-laser")
    content += '<section style="padding-top:24px"><div class="container">%s</div></section>' % blocks
    content += cta_band("Not sure where to start?", "Most clients come to us with a product and a deadline. We'll work out the rest together.")
    page("services", "Services", "All certification, compliance, audit, inspection and training services.", content)


def build_category(c):
    items = c["items"]
    tags = []
    for s in items:
        for t in s["tags"]:
            if t not in tags:
                tags.append(t)
    toolbar = ""
    if len(items) > 12:
        chips = '<button class="chip active" data-filter-tag="all">All</button>' + "".join(
            '<button class="chip" data-filter-tag="%s">%s</button>' % (e(t), e(t)) for t in tags)
        toolbar = ('<div class="toolbar"><label class="search">%s<input data-filter-input type="search" placeholder="Search %d certifications…" aria-label="Search"></label></div>'
                   '<div class="chips" style="margin:-12px 0 32px">%s</div>' % (SEARCH, len(items), chips))
    cards = "".join(svc_card(s) for s in items)
    k = KINDS[c["kind"] if c["kind"] in KINDS else "intl"]
    steps = [(str(i + 1).zfill(2), t, x) for i, (_, t, x) in enumerate(k["steps"][:4])] if c["kind"] != "product" else HOW
    side = ('<div class="card facts"><dl><div><dt>Services</dt><dd>%d</dd></div><div><dt>Response</dt><dd>Within one business day</dd></div>'
            '<div><dt>Pricing</dt><dd>Fixed, itemised quote</dd></div><div><dt>Support</dt><dd>One named specialist</dd></div></dl></div>' % len(items))
    content = page_hero(crumbs(("services", "Services"), (None, c["name"])), "Practice " + c["num"], e(c["name"]), e(c["intro"]), side, image=CAT_IMG[c["slug"]])
    content += """<section><div class="container">
  <div class="section-head"><div><span class="eyebrow">Catalogue</span><h2>{h}</h2></div><p>Choose a service to see requirements, documents, process and timelines.</p></div>
  {tb}<div class="svc-grid" data-filter-list>{cards}</div><div class="empty">No matches. Try a different search, or <a href="contact.html" style="text-decoration:underline">ask us</a> — we likely cover it.</div>
</div></section>
<section class="bg-ink"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Our approach</span><h2>How we work.</h2></div><p>Clear stages, clear owners, no surprises.</p></div>
  {steps}
</div></section>
{cta}""".format(h="Services in this practice", tb=toolbar, cards=cards, steps=steps_block(steps), cta=cta_band())
    page(c["slug"], c["name"], c["short"], content)


def build_service(s):
    c = CAT[s["cat"]]
    k = KINDS[s["kind"]]
    name = s["name"]
    facts = [("Category", c["name"])]
    if s["region"]:
        facts.append(("Market", s["region"]))
    if s["timeline"]:
        facts.append(("Typical time", s["timeline"]))
    if s["validity"]:
        facts.append(("Validity", s["validity"]))
    facts.append(("Who it's for", s["who"]))
    side = '<div class="card facts"><dl>%s</dl></div>' % "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (e(a), e(b)) for a, b in facts)
    hero = page_hero(crumbs(("services", "Services"), (c["slug"], c["name"]), (None, name)), s["full"], e(name), e(s["blurb"]), side, image=service_image(s))

    overview = """<section><div class="container split">
  <div class="sticky"><span class="eyebrow">Overview</span><h2 class="h2" style="margin-top:14px">What is {n}?</h2>
    <div class="side-img reveal-img">{im}</div></div>
  <div class="prose">
    <p>{blurb}</p>
    <p><strong>Who needs it:</strong> {who}</p>
    <p>Requirements vary with the product, its intended use and where it will be sold. That is why every {brand} engagement starts with a short scoping call: we confirm whether {n} applies to you, which standard or scheme governs it, and the most efficient route to approval — before you commit to any testing or fees.</p>
    <p>From there, a dedicated specialist manages the entire process — documentation, testing, applications, audits and every question from the issuing body — and keeps you updated weekly until the certificate is in your hands.</p>
    <div class="hero-actions" style="margin-top:28px"><a class="btn btn-primary" href="contact.html">Get a quote for {n} {a}</a></div>
  </div>
</div></section>""".format(n=e(name), blurb=e(s["blurb"]), who=e(s["who"]), brand=BRAND["name"], a=ARROW,
                                    im=img(service_image(s), name, "", "(max-width: 960px) 100vw, 40vw"))

    benefits = "".join('<div class="feature reveal"><div class="ic">%s</div><div><h3>%s</h3><p>%s</p></div></div>' % (ICONS[i % 6], e(t), e(x))
                       for i, (t, x) in enumerate(k["benefits"]))
    benefits_sec = """<section class="bg-surface"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Benefits</span><h2>Why it matters.</h2></div><p>What {n} does for your business beyond ticking a box.</p></div>
  <div class="features">{b}</div>
</div></section>""".format(n=e(name), b=benefits)

    docs = "".join('<li>%s<span>%s</span></li>' % (CHECK, e(d)) for d in k["docs"])
    depends = "".join('<li>%s<span>%s</span></li>' % (CHECK, e(d)) for d in k["depends"])
    docs_title = k.get("docs_title", "Documents required")
    docs_sec = """<section><div class="container split">
  <div><span class="eyebrow">{dt}</span><h2 class="h2" style="margin-top:14px">{dt}.</h2>
  <p class="muted" style="margin-top:16px">A typical checklist. Your specialist will send a version tailored to your exact product and situation.</p>
  <div class="card" style="padding:26px;margin-top:32px"><h3 style="font-size:17px;margin-bottom:14px">Scope and effort depend on</h3><ul class="checklist">{dep}</ul></div></div>
  <ul class="checklist">{docs}</ul>
</div></section>""".format(dt=e(docs_title), dep=depends, docs=docs)

    tl = "".join('<div class="tl reveal"><div class="when">%s</div><div class="dot"></div><div class="body"><h3>%s</h3><p>%s</p></div></div>' % (e(w), e(t), e(x))
                 for w, t, x in k["steps"])
    process = """<section class="bg-warm"><div class="container split">
  <div class="sticky"><span class="eyebrow">Process</span><h2 class="h2" style="margin-top:14px">How we get you there.</h2>
  <p class="muted" style="margin-top:16px">Indicative timeline. Actual timing depends on sample readiness, lab capacity and the issuing body.</p></div>
  <div class="timeline">{tl}</div>
</div></section>""".format(tl=tl)

    faqs = [(q.replace("{name}", name), a.replace("{name}", name)) for q, a in k["faq"]]
    faq = """<section><div class="container split">
  <div><span class="eyebrow">FAQ</span><h2 class="h2" style="margin-top:14px">Common questions about {n}.</h2></div>
  {f}
</div></section>""".format(n=e(name), f=faq_block(faqs))

    related = [x for x in c["items"] if x["slug"] != s["slug"]]
    same_tag = [x for x in related if set(x["tags"]) & set(s["tags"])]
    rel = (same_tag + [x for x in related if x not in same_tag])[:3]
    rel_sec = ""
    if rel:
        rel_sec = """<section class="bg-surface"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Related</span><h2>You may also need.</h2></div><a class="link-arrow" href="{h}">All {c} {a}</a></div>
  <div class="svc-grid">{cards}</div>
</div></section>""".format(h=href(c["slug"]), c=e(c["name"].lower()), a=ARROW, cards="".join(svc_card(x) for x in rel))
    content = hero + overview + benefits_sec + docs_sec + process + faq + rel_sec + '<div style="height:112px"></div>' + cta_band(
        "Let's get your %s sorted." % e(name))
    page(s["slug"], "%s — %s" % (name, s["full"]), s["blurb"], content, active=s["cat"])


def build_countries():
    cards = "".join('<a class="country reveal" href="%s"><span class="code">%s</span><div><h3>%s</h3><small>%s</small></div></a>'
                    % (href("country-" + slug), code, e(nm), "%d related services" % len(rel) if rel else "Guidance available")
                    for slug, nm, code, _, rel in COUNTRIES)
    content = page_hero(crumbs(("services", "Services"), (None, "Country guides")), "Country guides", "Selling abroad? Start here.",
                        "Each export market has its own regulators, marks and paperwork. Pick a country to see what typically applies — then let us confirm it for your product.", image="export-port")
    content += '<section><div class="container"><div class="country-grid">%s</div></div></section>' % cards + cta_band(
        "Exporting to a market not listed?", "We support approvals in more than 50 countries. Tell us where you are headed.")
    page("countries", "Country guides", "Certification requirements by export market.", content, active="countries")
    for slug, nm, code, text, rel in COUNTRIES:
        cards = "".join(svc_card(SVC[r]) for r in rel if r in SVC)
        body = ('<section><div class="container"><div class="section-head"><div><span class="eyebrow">Key approvals</span><h2>Services for %s.</h2></div>'
                '<p>Typical requirements. Exact obligations depend on your product category and HS code.</p></div><div class="svc-grid">%s</div></div></section>'
                % (e(nm), cards)) if cards else (
                '<section><div class="container prose"><p>Requirements in %s change frequently and depend heavily on product category. '
                'Contact us with your product details and we will confirm the current approval route, the local body involved and a realistic timeline.</p>'
                '<a class="btn btn-primary" href="contact.html">Ask about %s %s</a></div></section>' % (e(nm), e(nm), ARROW))
        side = ('<div class="card facts"><dl><div><dt>Market</dt><dd>%s</dd></div><div><dt>Code</dt><dd>%s</dd></div>'
                '<div><dt>Services</dt><dd>%d listed</dd></div></dl></div>' % (e(nm), code, len(rel)))
        content = page_hero(crumbs(("countries", "Country guides"), (None, nm)), "Country guide", "Certification for %s" % e(nm), e(text), side, image="export-port") + body + cta_band(
            "Shipping to %s soon?" % e(nm))
        page("country-" + slug, "Certification for %s" % nm, text, content, active="countries")


def build_insights():
    content = page_hero(crumbs((None, "Insights")), "Insights", "Notes from the certification desk.",
                        "Practical, jargon-free guides on product approvals, ISO standards, ESG and security — written by the people who do the work.", image="cat-training")
    content += '<section><div class="container"><div class="post-grid">%s</div></div></section>' % "".join(post_card(a) for a in ARTICLES)
    content += cta_band("Have a question we haven't covered?")
    page("insights", "Insights", "Guides and updates on certification and compliance.", content, active="insights")
    for a in ARTICLES:
        body = ""
        for t, x in a["body"]:
            body += "<%s>%s</%s>" % (t, e(x), t)
        others = [o for o in ARTICLES if o["slug"] != a["slug"]][:3]
        content = page_hero(crumbs(("insights", "Insights"), (None, a["tag"])), "%s · %s · %s read" % (a["tag"], a["date"], a["read"]),
                            e(a["title"]), e(a["excerpt"]), image=ARTICLE_IMG.get(a["slug"], "cat-msys"))
        content += '<div class="article-body"><div class="container"><article class="prose">%s</article></div></div>' % body
        content += ('<section class="bg-surface"><div class="container"><div class="section-head"><div><span class="eyebrow">Keep reading</span><h2>More insights.</h2></div></div>'
                    '<div class="post-grid">%s</div></div></section><div style="height:112px"></div>' % "".join(post_card(o) for o in others))
        content += cta_band()
        page(a["slug"], a["title"], a["excerpt"], content, active="insights")


def build_about():
    values = [
        ("01", "Clarity first", "We explain requirements in plain language and put every cost in writing before work starts."),
        ("02", "Ownership", "One specialist owns your project. If something stalls, they chase it — not you."),
        ("03", "Integrity", "We never promise outcomes that only a regulator can decide, and we never cut corners to hit a date."),
    ]
    v = "".join('<div class="value reveal"><div class="k">%s</div><h3>%s</h3><p>%s</p></div>' % x for x in values)
    content = page_hero(crumbs((None, "About")), "Our story", "We make compliance the easy part of growing.",
                        "%s is an independent certification and compliance partner. We help manufacturers, importers, exporters and service businesses get the approvals they need — and keep them." % BRAND["name"], image="about-cnc")
    content += """<section><div class="container split">
  <div class="sticky"><span class="eyebrow">Why we exist</span><h2 class="h2" style="margin-top:14px">Good products shouldn't wait on paperwork.</h2></div>
  <div class="prose">
    <p>Every year, excellent products sit in warehouses because a certificate is missing, a lab report was rejected or an application went unanswered. Founders and plant heads lose weeks deciphering portals and standards that were never written for them.</p>
    <p>We started {b} to fix that. Our team brings together product certification engineers, ISO lead auditors, food-safety experts, ESG analysts and security professionals under one roof. Whatever you need certified, there is someone here who does exactly that, every day.</p>
    <h2>How we are different</h2>
    <ul>
      <li><strong>Scoping before selling.</strong> We tell you what you actually need — including when you need less than you thought.</li>
      <li><strong>One team, many markets.</strong> Indian, European, North American, Gulf and African approvals from a single partner.</li>
      <li><strong>Fixed quotes.</strong> Our fee, lab fees and government fees itemised separately and agreed upfront.</li>
      <li><strong>We stay.</strong> Renewals, surveillance audits, new models and regulatory changes handled long after the first certificate.</li>
    </ul>
    <p>We are a consulting and facilitation firm. Certificates are issued by regulators and accredited certification bodies; our job is to make sure you are ready, your file is right and nothing stalls along the way.</p>
  </div>
</div></section>
<section class="bg-surface"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Values</span><h2>What we stand for.</h2></div></div>
  <div class="values">{v}</div>
</div></section>
<section class="bg-ink"><div class="container">
  <div class="section-head"><div><span class="eyebrow">By the numbers</span><h2>Built for breadth.</h2></div></div>
  {steps}
</div></section>
{cta}""".format(b=BRAND["name"], v=v, cta=cta_band(),
                steps=steps_block([(str(len(SERVICES)) + "+", "Services", "Across product, system, audit, accreditation, ESG and security."),
                                   ("9", "Practices", "Each led by a specialist who works only in that field."),
                                   (str(len(COUNTRIES)), "Country guides", "Covering the export markets our clients ask about most."),
                                   ("1", "Point of contact", "A named specialist for every project, start to finish.")]))
    page("about", "About us", "Who we are, what we believe and how we work.", content)


def build_team():
    m = "".join('<div class="member reveal"><div class="ph">Photo</div><h3>Name Surname</h3><div class="role">%s</div><p>%s</p></div>' % (e(r), e(d)) for r, d in TEAM)
    content = page_hero(crumbs(("about", "About"), (None, "Leadership")), "Leadership", "The people behind every certificate.",
                        "Engineers, auditors and regulatory specialists who have spent their careers on the details that get products approved.", image="about-engineers")
    content += '<section><div class="container"><div class="team-grid">%s</div></div></section>' % m
    content += cta_band("Want to work with us?", "We are always looking for experienced auditors, engineers and compliance specialists.")
    page("team", "Leadership", "Meet the leadership team.", content, active="team")


def build_clients():
    inds = "".join('<a class="itile reveal" href="services.html">%s<span class="itile-n">%02d</span><span class="itile-t">%s</span></a>'
                   % (img(im, n, "", "(max-width: 640px) 50vw, 25vw"), i + 1, e(n)) for i, (n, im) in enumerate(INDUSTRIES))
    logos = "".join("<div>Client logo</div>" for _ in range(12))
    content = page_hero(crumbs(("about", "About"), (None, "Clients")), "Clients & industries", "Trusted by makers of regulated products.",
                        "From first-time exporters to listed manufacturers, our clients share one thing: products that must meet a standard before they can be sold.", image="ind-food")
    content += '<section><div class="container"><div class="section-head"><div><span class="eyebrow">Clients</span><h2>Who we work with.</h2></div></div><div class="logo-wall">%s</div></div></section>' % logos
    content += '<section class="bg-warm"><div class="container"><div class="section-head"><div><span class="eyebrow">Industries</span><h2>Sectors we serve.</h2></div></div><div class="itile-grid" data-stagger>%s</div></div></section><div style="height:112px"></div>' % inds
    content += cta_band()
    page("clients", "Clients & industries", "Industries and clients we serve.", content, active="clients")


def build_partners():
    groups = [
        ("Accredited certification bodies", "We work with IAF-member accredited certification bodies for ISO and sector-scheme audits, and help you choose one whose accreditation your customers recognise."),
        ("Recognised testing laboratories", "Our lab network includes NABL-accredited and regulator-recognised labs in India, and ILAC-accredited labs overseas for international schemes."),
        ("Notified & approved bodies", "For CE, UKCA and other third-party schemes we coordinate with notified and approved bodies across Europe and the UK."),
        ("Local representatives & agents", "Where markets require a local agent, importer of record or authorised representative, we arrange vetted partners."),
        ("Inspection & audit networks", "Qualified inspectors and auditors across India's manufacturing clusters for inspections, social audits and factory evaluations."),
        ("Technology partners", "Compliance and GRC platforms that automate evidence collection for security and ESG programmes."),
    ]
    feats = "".join('<div class="feature reveal"><div class="ic">%s</div><div><h3>%s</h3><p>%s</p></div></div>' % (ICONS[i % 6], e(t), e(x)) for i, (t, x) in enumerate(groups))
    content = page_hero(crumbs(("about", "About"), (None, "Partners")), "Certification partners", "The right body, the right lab, first time.",
                        "Choosing the wrong lab or certification body is the most expensive mistake in certification. Our partner network means you never have to guess.", image="hero-lab")
    content += '<section><div class="container"><div class="features">%s</div></div></section>' % feats + cta_band()
    page("partners", "Certification partners", "Our network of labs, certification bodies and partners.", content, active="partners")


def build_recognition():
    items = [("Accreditation", "Add your accreditations here"), ("Membership", "Industry association memberships"),
             ("Award", "Awards and industry recognition"), ("Approval", "Approvals and empanelments")]
    v = "".join('<div class="value reveal"><div class="k">%02d</div><h3>%s</h3><p>%s</p></div>' % (i + 1, e(t), e(d)) for i, (t, d) in enumerate(items))
    content = page_hero(crumbs(("about", "About"), (None, "Recognition")), "Recognition", "Credentials that back our work.",
                        "Our accreditations, memberships and the recognition our team has earned along the way.", image="cat-accreditation")
    content += '<section><div class="container"><div class="values" style="grid-template-columns:repeat(2,1fr)">%s</div></div></section>' % v + cta_band()
    page("recognition", "Recognition", "Accreditations, memberships and awards.", content, active="recognition")


def build_offices():
    content = page_hero(crumbs(("about", "About"), (None, "Offices")), "Offices", "Local presence, global reach.",
                        "Headquartered in Mumbai, with partner offices and representatives in our key export markets.", image="cat-msys")
    offices = [("Head office", "Mumbai, India", BRAND["address"]), ("Registered office", "Mumbai, India", BRAND["reg_address"]),
               ("Partner office", "Dubai, UAE", "Address to be added"), ("Partner office", "London, UK", "Address to be added")]
    cards = "".join('<div class="value reveal"><span class="eyebrow">%s</span><h3>%s</h3><p>%s</p></div>' % (e(t), e(c), e(a)) for t, c, a in offices)
    content += '<section><div class="container"><div class="values" style="grid-template-columns:repeat(2,1fr)">%s</div></div></section>' % cards + cta_band()
    page("offices", "Offices", "Where to find us.", content, active="offices")


def build_contact():
    content = page_hero(crumbs((None, "Contact")), "Contact", "Let's talk about what you need certified.",
                        "Send us a few details and a specialist will reply within one business day with the approvals you need, a timeline and a fixed quote.", image="hero-inspect")
    content += """<section><div class="container contact-grid">
  <div>
    <dl class="contact-list">
      <div><dt>Phone</dt><dd><a href="tel:{t1}">{p1}</a><br><a href="tel:{t2}">{p2}</a></dd></div>
      <div><dt>Email</dt><dd><a href="mailto:{em}">{em}</a><br><a href="mailto:{se}">{se}</a></dd></div>
      <div><dt>WhatsApp</dt><dd><a href="https://wa.me/{wa}" target="_blank" rel="noopener">Chat with us</a></dd></div>
      <div><dt>Head office</dt><dd>{ad}</dd></div>
      <div><dt>Registered</dt><dd>{ra}</dd></div>
      <div><dt>Hours</dt><dd>{hr}</dd></div>
    </dl>
  </div>
  <div class="card quote-card"><h3>Send an enquiry</h3><p>The more you tell us, the more precise our first reply will be.</p>{form}</div>
</div></section>""".format(t1=BRAND["phone"].replace(" ", ""), p1=BRAND["phone"], t2=BRAND["phone2"].replace(" ", ""), p2=BRAND["phone2"],
                           em=BRAND["email"], se=BRAND["sales_email"], wa=BRAND["whatsapp"], ad=e(BRAND["address"]),
                           ra=e(BRAND["reg_address"]), hr=e(BRAND["hours"]), form=enquiry_form())
    page("contact", "Contact us", "Get a free certification assessment and fixed quote.", content)


def build_legal():
    privacy = [("p", "This policy explains how %s collects and uses information submitted through this website." % BRAND["legal"]),
               ("h2", "Information we collect"), ("p", "When you submit an enquiry we collect your name, contact details, company and the details of your request. We do not sell personal information."),
               ("h2", "How we use it"), ("p", "We use your information only to respond to your enquiry, provide our services and send updates you have asked for."),
               ("h2", "Your rights"), ("p", "You may ask us to access, correct or delete your personal data at any time by writing to %s." % BRAND["email"])]
    terms = [("p", "By using this website you agree to these terms."),
             ("h2", "Information only"), ("p", "Content on this site is general guidance and not legal advice. Regulatory requirements change; always confirm requirements for your specific product."),
             ("h2", "Our role"), ("p", "%s is a consulting and facilitation firm. Certificates, licences and registrations are issued by the relevant regulator or accredited body." % BRAND["name"]),
             ("h2", "Contact"), ("p", "Questions about these terms can be sent to %s." % BRAND["email"])]
    for slug, title, body in [("privacy", "Privacy policy", privacy), ("terms", "Terms of use", terms)]:
        html = "".join("<%s>%s</%s>" % (t, e(x), t) for t, x in body)
        content = page_hero(crumbs((None, title)), "Legal", title, "Last updated November 2026.") + '<div class="article-body"><div class="container"><div class="prose">%s</div></div></div>' % html
        page(slug, title, title, content)


def build_404_and_sitemap():
    content = page_hero("", "Error 404", "This page has moved on.", "The page you were looking for doesn't exist. Try our services or get in touch.")
    content += '<section style="padding-top:0"><div class="container hero-actions"><a class="btn btn-primary" href="index.html">Back home %s</a><a class="btn btn-ghost" href="services.html">All services</a></div></section>' % ARROW
    page("404", "Page not found", "Page not found", content)
    links = "".join('<a href="%s">%s</a>' % (href(s), e(t)) for s, t in PAGES)
    content = page_hero(crumbs((None, "Sitemap")), "Sitemap", "Every page, in one place.", "%d pages." % (len(PAGES) + 1))
    content += '<section style="padding-top:24px"><div class="container"><div class="cat-links" style="columns:3">%s</div></div></section>' % links
    page("sitemap", "Sitemap", "All pages on this website.", content)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
    build_home()
    build_about(); build_team(); build_clients(); build_partners(); build_recognition(); build_offices()
    build_services_index()
    for c in CATEGORIES:
        build_category(c)
    for s in SERVICES:
        build_service(s)
    build_countries()
    build_insights()
    build_contact()
    build_legal()
    build_404_and_sitemap()
    # sitemap.xml for search engines (set your domain)
    domain = "https://shivpradatt-hub.github.io/vakane/"  # change when you connect your own domain
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for s, _ in PAGES:
            if s != "404":
                f.write("  <url><loc>%s%s</loc></url>\n" % (domain, href(s)))
        f.write("</urlset>\n")
    print("Built %d pages into %s" % (len(PAGES), OUT))


if __name__ == "__main__":
    main()
