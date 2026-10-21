"""Build the 502 Tinted static site.

  dist/site     production: clean URLs (/car-window-tint-louisville), sitemap, robots, llms.txt, Cloudflare files
  dist/preview  artifact preview: relative .html links; the quote form does not send
"""
import json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *  # noqa
import kit
import c_home, c_tint, c_detail, c_areas, c_company, c_blog

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = ("https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700"
         "&family=Barlow:ital,wght@0,400;0,500;0,600;1,400&family=Fraunces:opsz,wght,SOFT@9..144,600..900,0..100&display=swap")

# Analytics: paste IDs here when Shane has them; nothing loads while they're empty.
GA4_ID = ""
META_PIXEL_ID = ""

PAGES = []
for mod in (c_home, c_tint, c_detail, c_areas, c_company, c_blog):
    PAGES.extend(mod.pages())

RELATED = {
    "Window tint": [("car-window-tint-louisville", "Car window tint"), ("ceramic-window-tint-louisville", "Ceramic tint"),
                    ("windshield-tint-louisville", "Windshield tint"), ("tint-removal-louisville", "Tint removal"),
                    ("hitek-window-film-louisville", "HITEK films"), ("window-tint-cost-louisville", "Tint prices"),
                    ("kentucky-tint-laws", "Kentucky tint law"), ("auto-detailing-louisville", "Detailing menu")],
    "Detailing": [("auto-detailing-louisville", "Detailing menu"), ("interior-detailing-louisville", "Interior detailing"),
                  ("exterior-detailing-louisville", "Exterior detailing"), ("paint-correction-louisville", "Paint correction"),
                  ("car-window-tint-louisville", "Car window tint"), ("ceramic-window-tint-louisville", "Ceramic tint")],
    "Guides": [("kentucky-tint-laws", "Kentucky tint law"), ("ceramic-window-tint-louisville", "Ceramic tint"),
               ("windshield-tint-louisville", "Windshield tint"), ("window-tint-cost-louisville", "Tint prices"),
               ("auto-detailing-louisville", "Detailing menu"), ("get-a-quote", "Get a quote")],
    "Kentucky law": [("car-window-tint-louisville", "Car window tint"), ("ceramic-window-tint-louisville", "Ceramic tint"),
                     ("windshield-tint-louisville", "Windshield tint"), ("is-windshield-tint-legal-in-kentucky", "Is windshield tint legal in Kentucky?"),
                     ("window-tint-cost-louisville", "Tint prices"), ("get-a-quote", "Get a quote")],
    "Service areas": [("car-window-tint-louisville", "Car window tint"), ("ceramic-window-tint-louisville", "Ceramic tint"),
                      ("auto-detailing-louisville", "Detailing menu"), ("kentucky-tint-laws", "Kentucky tint law"), ("service-areas", "All service areas")],
    "Company": [("car-window-tint-louisville", "Car window tint"), ("auto-detailing-louisville", "Detailing menu"),
                ("kentucky-tint-laws", "Kentucky tint law"), ("service-areas", "Service areas"), ("get-a-quote", "Get a quote")],
}
for _p in PAGES:
    _rel = RELATED.get(_p.get("group"))
    if _rel and _p["slug"] not in ("get-a-quote", "404"):
        _lis = "".join(f'<li><a href="@{s}">{n}</a></li>' for s, n in _rel if s != _p["slug"])
        _p["body"] += f'<section class="band band-related"><div class="wrap"><h2>Keep reading</h2><ul class="link-list">{_lis}</ul></div></section>'

BY_SLUG = {p["slug"]: p for p in PAGES}

HERO_IMG = {
    "index": "audi-q5-tint-red-bay",
    "thank-you": "toyota-tacoma-tint-shop-front",
    "car-window-tint-louisville": "toyota-tacoma-tint-shop-front",
    "ceramic-window-tint-louisville": "range-rover-ceramic-tint",
    "windshield-tint-louisville": "windshield-film-install",
    "tint-removal-louisville": "kia-sportage-tint-shop-front",
    "hitek-window-film-louisville": "vw-tiguan-tint-hitek-bay",
    "window-tint-cost-louisville": "toyota-rav4-tint-side",
    "kentucky-tint-laws": "chevy-suburban-tint-hitek-bay",
    "auto-detailing-louisville": "toyota-rav4-detailing-sign",
    "interior-detailing-louisville": "white-suburban-tint-red-bay",
    "exterior-detailing-louisville": "honda-crv-tint-5410-valley-station",
    "paint-correction-louisville": "vw-jetta-tint-gloss",
    "about": "honda-crv-tint-5410-valley-station",
    "reviews": "audi-q5-tint-red-bay",
    "faq": "white-suburban-tint-red-bay",
    "contact": "honda-crv-tint-5410-valley-station",
    "get-a-quote": "toyota-tacoma-tint-shop-front",
    "service-areas": "honda-crv-tint-5410-valley-station",
    "blog": "chevy-suburban-tint-hitek-bay",
    "is-windshield-tint-legal-in-kentucky": "windshield-film-install",
    "hitek-ceramic-ir-vs-ceramic-plus": "range-rover-ceramic-tint",
    "window-tint-cure-time-louisville": "vw-jetta-tint-gloss",
}
_AREA_ROTATION = ["honda-crv-tint-5410-valley-station", "toyota-tacoma-tint-shop-front", "kia-sportage-tint-shop-front",
                  "toyota-rav4-tint-side", "toyota-rav4-detailing-sign", "range-rover-ceramic-tint"]
for _i, (_s, _n) in enumerate(AREAS):
    HERO_IMG[_s] = _AREA_ROTATION[_i % len(_AREA_ROTATION)]
for _p in PAGES:
    _p.setdefault("hero_img", HERO_IMG.get(_p["slug"]))

def url_of(slug):
    return BASE + "/" if slug == "index" else f"{BASE}/{slug}"

LINK_RE = re.compile(r'href="@([a-z0-9-]+)(#[A-Za-z0-9_-]+)?"')

def resolve(html, mode):
    def rep(m):
        slug, anchor = m.group(1), m.group(2) or ""
        if slug == "home":
            slug = "index"
        if slug not in BY_SLUG:
            raise SystemExit(f"Broken internal link: @{slug}")
        href = ("/" if slug == "index" else f"/{slug}") if mode == "prod" else f"{slug}.html"
        return f'href="{href}{anchor}"'
    html = LINK_RE.sub(rep, html)
    return html.replace("%ASSETS%", "/assets" if mode == "prod" else "assets")

# ---------------- schema ----------------
DAYS = {"Monday": "Mo", "Tuesday": "Tu", "Wednesday": "We", "Thursday": "Th", "Friday": "Fr", "Saturday": "Sa", "Sunday": "Su"}

def business_node():
    hours = {}
    for d, o, c in HOURS:
        if o:
            hours.setdefault((o, c), []).append(d)
    return {
        "@type": "AutomotiveBusiness",
        "@id": BASE + "/#business",
        "name": NAME,
        "description": ("Window tint and auto detailing shop in Valley Station, Louisville, Kentucky. HITEK dealer installing "
                        "Ceramic IR and Ceramic Plus window film, windshield sun strips and heat film, tint removal, interior and "
                        "exterior detailing and paint correction."),
        "url": BASE + "/",
        "logo": BASE + "/assets/502-tinted-logo.png",
        "image": [BASE + "/assets/502-tinted-social.jpg"] + [f"{BASE}/assets/work/{n}-1600.webp" for n in
                  ("honda-crv-tint-5410-valley-station", "toyota-tacoma-tint-shop-front", "audi-q5-tint-red-bay")],
        "telephone": "+1-502-631-0419",
        "email": EMAIL,
        "priceRange": "$$",
        "founder": {"@type": "Person", "name": OWNER, "jobTitle": "Owner"},
        "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": CITY,
                    "addressRegion": REGION, "postalCode": ZIP, "addressCountry": "US"},
        "hasMap": MAPS_URL,
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ds if len(ds) > 1 else ds[0], "opens": o, "closes": c}
            for (o, c), ds in hours.items()],
        "areaServed": [{"@type": "City", "name": n} for n in AREA_NAMES_SCHEMA],
        "sameAs": [FACEBOOK],
        "knowsAbout": ["Automotive window tint", "Ceramic window tint", "HITEK Ceramic IR", "HITEK Ceramic Plus",
                       "Kentucky window tint law (KRS 189.110)", "Windshield tint", "Tint removal", "Auto detailing",
                       "Interior detailing", "Exterior detailing", "Paint correction"],
        "brand": [{"@type": "Brand", "name": "HITEK"}],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Window tint and detailing",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": p["service"]["name"],
                                                                   "url": url_of(p["slug"])}}
                                for p in PAGES if p.get("service")],
        },
    }

def breadcrumb_node(page):
    items = [("Home", "index")] + page.get("crumbs", []) + [(page["crumb"], page["slug"])]
    return {"@type": "BreadcrumbList", "@id": url_of(page["slug"]) + "#breadcrumb",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": url_of(s)}
                                for i, (n, s) in enumerate(items)]}

def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()

def schema_graph(page):
    u = url_of(page["slug"])
    g = [business_node()]
    g.append({"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": NAME,
              "publisher": {"@id": BASE + "/#business"}} if page["slug"] == "index" else None)
    g = [x for x in g if x]
    wp = {"@type": "WebPage", "@id": u + "#webpage", "url": u, "name": page["title"], "description": page["desc"],
          "isPartOf": {"@id": BASE + "/#website"}, "about": {"@id": BASE + "/#business"},
          "dateModified": page.get("modified", UPDATED), "inLanguage": "en-US"}
    if page["slug"] != "index":
        wp["breadcrumb"] = {"@id": u + "#breadcrumb"}
        g.append(breadcrumb_node(page))
    g.append(wp)
    if page.get("service"):
        s = page["service"]
        node = {"@type": "Service", "@id": u + "#service", "name": s["name"], "serviceType": s.get("type", s["name"]),
                "description": s.get("desc", page["desc"]), "url": u, "provider": {"@id": BASE + "/#business"},
                "areaServed": s.get("area", [{"@type": "City", "name": n} for n in AREA_NAMES_SCHEMA[:8]])}
        if s.get("brands"):
            node["brand"] = [{"@type": "Brand", "name": b} for b in s["brands"]]
        if s.get("alt"):
            node["alternateName"] = s["alt"]
        if s.get("offers"):
            node["offers"] = {"@type": "Offer", "url": BASE + "/get-a-quote",
                              "priceSpecification": {"@type": "PriceSpecification", "minPrice": s["offers"], "priceCurrency": "USD"}}
        g.append(node)
    if page.get("faqs"):
        g.append({"@type": "FAQPage", "@id": u + "#faqpage",
                  "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                                 for q, a in page["faqs"]]})
    if page.get("article"):
        a = page["article"]
        g.append({"@type": "BlogPosting", "@id": u + "#article", "headline": strip_tags(page["h1"]),
                  "description": page["desc"], "datePublished": a["date"], "dateModified": a.get("modified", a["date"]),
                  "author": {"@type": "Person", "name": OWNER, "worksFor": {"@id": BASE + "/#business"}},
                  "publisher": {"@id": BASE + "/#business"}, "mainEntityOfPage": {"@id": u + "#webpage"},
                  "image": BASE + "/assets/502-tinted-social.jpg"})
    g.extend(page.get("schema_extra", []))
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":"))

# ---------------- layout ----------------
def nav_html(current):
    out = []
    for label, slug, subs in NAV:
        active = current == slug or any(current == s for s, _ in subs)
        cur = ' aria-current="page"' if current == slug else ""
        cls = ("has-sub " if subs else "") + ("is-active" if active else "")
        cls_attr = f' class="{cls.strip()}"' if cls.strip() else ""
        if subs:
            ac = ' aria-current="page"'
            sub = "".join(f'<li><a href="@{s}"{ac if s == current else ""}>{esc(n)}</a></li>' for s, n in subs)
            out.append(f'<li{cls_attr}><a href="@{slug}"{cur}>{esc(label)}</a><ul class="sub">{sub}</ul></li>')
        else:
            out.append(f'<li{cls_attr}><a href="@{slug}"{cur}>{esc(label)}</a></li>')
    return '<ul class="nav-list">' + "".join(out) + "</ul>"

def crumbs_html(page):
    if page["slug"] == "index":
        return ""
    items = [("Home", "home")] + list(page.get("crumbs", []))
    lis = "".join(f'<li><a href="@{s}">{esc(n)}</a></li>' for n, s in items)
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}<li aria-current="page">{esc(page["crumb"])}</li></ol></nav>'

def header_html(page):
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap topbar-in">
<a href="{MAPS_URL}" rel="noopener">{ADDRESS_LINE.replace(", Louisville, KY 40272", ", Louisville")}</a>
<span class="today" data-today>{HOURS_SHORT}</span>
<a href="tel:{PHONE_E164}">Call or text {PHONE}</a>
</div></div>
<header class="site-header"><div class="wrap head-in">
<a class="head-call" href="tel:{PHONE_E164}" aria-label="Call {PHONE}">{icon("phone")}</a>
<a class="logo" href="@home"><img src="%ASSETS%/502-tinted-logo-sm.webp" width="160" height="146" alt="502 Tinted, window tint and detailing in Louisville, Kentucky"></a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav"><span class="bars" aria-hidden="true"></span><span class="sr">Menu</span></button>
<nav id="nav" class="nav" aria-label="Main">{nav_html(page["slug"])}</nav>
<a class="btn btn-red head-cta" href="@get-a-quote">Get a quote</a>
</div></header>'''

def footer_html():
    tint = "".join(f'<li><a href="@{s}">{esc(n)}</a></li>' for s, n in NAV[0][2])
    det = "".join(f'<li><a href="@{s}">{esc(n)}</a></li>' for s, n in NAV[1][2])
    areas = "".join(f'<li><a href="@{s}">{esc(n)}</a></li>' for s, n in AREAS)
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div class="foot-brand">
<img src="%ASSETS%/502-tinted-logo-sm.webp" width="160" height="146" alt="" loading="lazy" class="foot-logo">
<address><a href="{MAPS_URL}" rel="noopener">5410 Valley Station Rd #108<br>Louisville, KY 40272</a><br>
<a href="tel:{PHONE_E164}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></address>
{hours_dl()}
<p><a href="{FACEBOOK}" rel="noopener">Facebook</a><span class="sep" aria-hidden="true"></span><a href="{MAPS_URL}" rel="noopener">Google reviews</a></p>
</div>
<div><p class="foot-h">Window tint</p><ul>{tint}<li><a href="@kentucky-tint-laws">Kentucky Tint Law</a></li></ul></div>
<div><p class="foot-h">Detailing</p><ul>{det}</ul><p class="foot-h">Shop</p><ul><li><a href="@about">About Shane</a></li><li><a href="@reviews">Reviews</a></li><li><a href="@faq">FAQ</a></li><li><a href="@blog">Guides</a></li><li><a href="@contact">Contact</a></li><li><a href="@get-a-quote">Get a quote</a></li></ul></div>
<div><p class="foot-h">Areas we serve</p><ul>{areas}</ul></div>
</div>
<div class="foot-bottom">
<p class="verse"><span class="fleur" aria-hidden="true"></span>“Whatever you do, work at it with all your heart.” Colossians 3:23</p>
<p>© 2026 502 Tinted, owned and operated by {OWNER}. Valley Station, Louisville, Kentucky.</p>
</div>
</div></footer>
<div class="mbar" aria-label="Quick contact"><a href="tel:{PHONE_E164}">Call</a><a href="sms:{PHONE_E164}">Text</a><a class="mbar-q" href="@get-a-quote">Get a quote</a></div>'''

def proof_html():
    return (f'<ul class="proof"><li>{STARS} <span><strong>{RATING}</strong> on Google from {REVIEWS} reviews</span></li>'
            '<li>HITEK dealer, lifetime guarantee</li><li>Same-day on most cars</li></ul>')

def hero_html(page):
    if page.get("hero"):
        return page["hero"]
    side = page.get("hero_side", "")
    cls = "hero" + (" hero-split" if side else "") + (" hero-photo" if page.get("hero_img") else "")
    bg = (f'<div class="hero-bg">{img(page["hero_img"], "100vw", "hero-img", eager=True)}</div>' if page.get("hero_img") else "")
    return f'''<section class="{cls}">{bg}<div class="wrap hero-in">
<div class="hero-copy">{crumbs_html(page)}
<h1>{page["h1"]}</h1>
<p class="lede">{page["lede"]}</p>
{page.get("hero_btns", btns())}{proof_html() if page.get("proof", True) else ""}</div>
{f'<div class="hero-side">{side}</div>' if side else ''}
</div></section>'''

def cta_band():
    return checker() + f'''<section class="band band-cta"><div class="wrap cta-in">
<div><h2>Pull up and get shaded.</h2>
<p>Most tint jobs are done the same day, and detailing is by appointment. Call, text or send a quote request, and Shane will get back to you during shop hours.</p></div>
{btns(text=True)}</div></section>'''

def body_html(page, mode):
    parts = [hero_html(page), f'<main id="main">{page["body"]}']
    if page.get("faqs") and not page.get("faq_inline"):
        parts.append(section(faq_html(page["faqs"], page.get("faq_heading", "Questions we get a lot")), "band-faq"))
    if page.get("cta", True):
        parts.append(cta_band())
    parts.append("</main>")
    html = header_html(page) + "".join(parts) + footer_html()
    if mode == "prod":
        html = re.sub(r"<!--PROD:(.*?)-->", r"\1", html, flags=re.S)
        html = re.sub(r"<!--PREVIEW-->.*?<!--/PREVIEW-->", "", html, flags=re.S)
    else:
        html = re.sub(r"<!--PROD:(.*?)-->", "", html, flags=re.S)
        html = html.replace("data-qf>", 'data-qf data-preview="1">')
        html = html.replace(f'action="https://formsubmit.co/{FORM_ID}"', 'action="#"')
    return html

def analytics_head():
    out = ""
    if GA4_ID:
        out += (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>'
                f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA4_ID}');</script>\n")
    if META_PIXEL_ID:
        out += ("<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};"
                "if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];"
                "s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');"
                f"fbq('init','{META_PIXEL_ID}');fbq('track','PageView');</script>\n")
    return out

def head_meta(page, mode):
    u = url_of(page["slug"])
    title, desc = esc(page["title"]), esc(page["desc"])
    a = "/assets" if mode == "prod" else "assets"
    robots = "noindex, follow" if page.get("noindex") else "index, follow, max-image-preview:large, max-snippet:-1"
    return f'''<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{u}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0d0d0d">
<script>try{{history.scrollRestoration="manual"}}catch(e){{}}</script>
<meta name="geo.region" content="US-KY"><meta name="geo.placename" content="Louisville">
<meta property="og:type" content="{"article" if page.get("article") else "website"}"><meta property="og:site_name" content="502 Tinted">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{u}"><meta property="og:image" content="{BASE}/assets/502-tinted-social.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="502 Tinted, window tint and detailing in Louisville, Kentucky">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{BASE}/assets/502-tinted-social.jpg">
<link rel="icon" type="image/png" sizes="48x48" href="{a}/favicon-48.png">
<link rel="apple-touch-icon" href="{a}/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{a}/site.css">
{hero_preload(page, a)}
<script type="application/ld+json">{schema_graph(page)}</script>'''

def hero_preload(page, a):
    n = page.get("hero_img")
    if not n:
        return ""
    return (f'<link rel="preload" as="image" type="image/webp" imagesrcset="{a}/work/{n}-800.webp 800w, {a}/work/{n}-1600.webp 1600w" '
            f'imagesizes="100vw" fetchpriority="high">')

def render(page, mode):
    body = body_html(page, mode)
    tail = f'<script src="{"/assets" if mode == "prod" else "assets"}/site.js" defer></script>'
    if mode == "preview" and page["slug"] == "index":
        head = head_meta(page, mode).replace(f"<title>{esc(page['title'])}</title>", "<title>502 Tinted Website</title>", 1)
        out = '<meta charset="utf-8">\n<meta name="claude:viewport-fit-sides" content="cover">\n' + head + "\n" + body + tail
    else:
        out = (f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
               f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
               f'{analytics_head() if mode == "prod" else ""}'
               f'{head_meta(page, mode)}\n</head>\n<body>\n{body}\n{tail}\n</body>\n</html>\n')
    return resolve(out, mode)

# ---------------- site files ----------------
def sitemap():
    def images(p):
        names = [p["hero_img"]] if p.get("hero_img") else []
        if p["slug"] == "index":
            names += [n for n in GALLERY if n not in names]
        return "".join(f"<image:image><image:loc>{BASE}/assets/work/{n}-1600.webp</image:loc></image:image>" for n in names)
    urls = "".join(f"<url><loc>{url_of(p['slug'])}</loc><lastmod>{p.get('modified', UPDATED)}</lastmod>{images(p)}</url>\n"
                   for p in PAGES if not p.get("noindex"))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + urls + "</urlset>\n")

BOTS = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "ClaudeBot", "Claude-SearchBot", "Claude-User",
        "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended"]
ROBOTS = ("# 502 Tinted: search engines and AI assistants are welcome to read this site.\nUser-agent: *\nAllow: /\n\n"
          + "".join(f"User-agent: {b}\nAllow: /\n" for b in BOTS) + f"\nSitemap: {BASE}/sitemap.xml\n")

def llms_txt():
    groups = {}
    for p in PAGES:
        if not p.get("noindex"):
            groups.setdefault(p.get("group", "Other"), []).append(p)
    lines = [
        "# 502 Tinted", "",
        "> 502 Tinted is a window tint and auto detailing shop in Valley Station, Louisville, Kentucky, owned and run by Shane Crosier. "
        "It is a HITEK dealer installing HITEK Ceramic IR and Ceramic Plus window film, plus windshield sun strips and windshield heat film, "
        "tint removal, interior and exterior detailing and paint correction.", "",
        "Key facts:",
        f"- Address: {ADDRESS_LINE} (Valley Station, southwest Louisville, near Dixie Highway and the Gene Snyder Freeway)",
        f"- Phone and text: {PHONE}; email {EMAIL}",
        "- Hours: Monday, Tuesday, Thursday and Friday 9 AM–3 PM; Wednesday 10 AM–5 PM; Saturday 8 AM–1 PM; closed Sunday",
        f"- Google rating: {RATING} stars from {REVIEWS} reviews (October 2026)",
        f"- Window tint: HITEK Ceramic IR from {P('tint_ir')} and HITEK Ceramic Plus from {P('tint_plus')} for a car's side windows and back glass; front two doors from {P('tint_front2')}; lifetime film warranty",
        f"- Detailing: maintenance wash from {P('wash')}, interior detail from {P('interior')}, exterior detail from {P('exterior')}, full detail from {P('full')}, paint correction from {P('enhance')}",
        "- Kentucky tint law summary: front side windows at least 35% light transmission; windows behind the driver at least 18% (8% on multipurpose passenger vehicles such as most SUVs and vans); "
        "film is rated on clear glass with a 3% tolerance; reflectance up to 25% front and 35% rear; windshield film only as a top strip above the AS-1 line or a clear film that keeps the windshield at 70% or more; "
        "installers must put a compliance label on the inside of the driver's door jamb.",
        "- Service area: Louisville (Valley Station, Pleasure Ridge Park, Shively, Fairdale, Okolona, St. Matthews, Jeffersontown), Bullitt County (Hillview, Shepherdsville, Mount Washington) and Hardin County (Radcliff, Fort Knox, Elizabethtown)",
        f"- Quote request: {BASE}/get-a-quote", "",
    ]
    for g in ["Main", "Window tint", "Detailing", "Kentucky law", "Service areas", "Guides", "Company"]:
        if g in groups:
            lines.append(f"## {g}")
            lines += [f"- [{p['title']}]({url_of(p['slug'])}): {p['desc']}" for p in groups[g]]
            lines.append("")
    return "\n".join(lines)

CF_HEADERS = """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=()

/assets/*
  Cache-Control: public, max-age=86400

/sitemap.xml
  Cache-Control: public, max-age=3600

/llms.txt
  Content-Type: text/plain; charset=utf-8
"""

def shot_list(uses):
    lines = ["# 502 Tinted photo shot list", "",
             "Shane's 12 shop photos and the Expedition video are on the site now. These spots still need a photo, mostly detailing work.",
             "Send them to Claude, or add the file in source/src/kit.py (PHOTOS) and rebuild.",
             "Shoot landscape for 3:2 and 4:3, square for 1:1, portrait for 4:5. At least 1600 px on the long side. Daylight or bright, even shop light; no harsh flash on glass.", "",
             "| Slot | What to shoot | Shape | Used on |", "| --- | --- | --- | --- |"]
    for slot, (desc, ratio, _, name) in PHOTOS.items():
        if name:
            continue
        pages = ", ".join(sorted(uses.get(slot, []))) or "(not placed yet)"
        shape = {"3/2": "3:2 landscape", "4/3": "4:3 landscape", "1/1": "1:1 square", "4/5": "4:5 portrait"}[ratio]
        lines.append(f"| `{slot}` | {desc} | {shape} | {pages} |")
    return "\n".join(lines) + "\n"

def build():
    uses = {}
    for mode, out in (("prod", "site"), ("preview", "dist/preview")):
        d = os.path.join(ROOT, out)
        shutil.rmtree(d, ignore_errors=True)
        shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(d, "assets"))
        for p in PAGES:
            html = render(p, mode)
            if mode == "prod":
                for slot in re.findall(r'data-slot="([a-z0-9-]+)"', html):
                    uses.setdefault(slot, set()).add("/" if p["slug"] == "index" else "/" + p["slug"])
            with open(os.path.join(d, p["slug"] + ".html"), "w") as fh:
                fh.write(html)
        if mode == "prod":
            for name, content in (("sitemap.xml", sitemap()), ("robots.txt", ROBOTS), ("llms.txt", llms_txt()),
                                  ("_headers", CF_HEADERS)):
                with open(os.path.join(d, name), "w") as fh:
                    fh.write(content)
    with open(os.path.join(ROOT, "PHOTO-SHOT-LIST.md"), "w") as fh:
        fh.write(shot_list(uses))
    print(f"Built {len(PAGES)} pages")

if __name__ == "__main__":
    build()
