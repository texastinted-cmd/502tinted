"""Shared constants, prices, photo slots and HTML components for the 502 Tinted site."""
import html as _html
import os

# ---------------- business facts ----------------
BASE = "https://www.502tinted.com"          # assumed domain: change here if Shane registers a different one
NAME = "502 Tinted"
OWNER = "Shane Crosier"
PHONE = "(502) 631-0419"
PHONE_E164 = "+15026310419"
EMAIL = "502tinted@gmail.com"
STREET = "5410 Valley Station Rd #108"
CITY = "Louisville"
REGION = "KY"
ZIP = "40272"
ADDRESS_LINE = "5410 Valley Station Rd #108, Louisville, KY 40272"
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=502+Tinted+5410+Valley+Station+Rd+Louisville+KY+40272"
FACEBOOK = "https://www.facebook.com/share/1cCTsX29G1/"
RATING = "5.0"
REVIEWS = "30"
UPDATED = "2026-10-21"

# (day, opens, closes) in 24h; None = closed. Mirrors the Google Business Profile.
HOURS = [
    ("Monday", "09:00", "15:00"), ("Tuesday", "09:00", "15:00"), ("Wednesday", "10:00", "17:00"),
    ("Thursday", "09:00", "15:00"), ("Friday", "09:00", "15:00"), ("Saturday", "08:00", "13:00"),
    ("Sunday", None, None),
]
HOURS_SHORT = "Mon, Tue, Thu, Fri 9–3 · Wed 10–5 · Sat 8–1"

# ---------------- prices (SAMPLE: confirm with Shane, then edit only here) ----------------
PRICES = {
    # window tint, cars; SUVs, trucks and vans are quoted by glass count
    "tint_front2": 129,      # front two doors, Ceramic IR (to match factory rear privacy glass)
    "tint_ir": 249,          # sides + back glass, HITEK Ceramic IR
    "tint_plus": 349,        # sides + back glass, HITEK Ceramic Plus
    "tint_strip": 49,        # windshield sun strip to the AS-1 line
    "tint_windshield": 199,  # full windshield clear ceramic heat film
    "tint_removal": 99,      # old film and adhesive removal, from
    # detailing, cars
    "wash": 59, "interior": 149, "exterior": 129, "full": 229, "enhance": 399, "correct2": 699,
    # add-ons
    "pet": 40, "headlight": 79, "engine": 49, "odor": 59, "stain": 40,
}

def P(key):
    return f"${PRICES[key]:,}"

DETAIL_MENU = [  # (key, name, what's included)
    ("wash", "Maintenance wash", "Foam pre-wash, hand wash, wheels and tires, towel dry, glass inside and out, quick vacuum. For cars that are already in good shape."),
    ("interior", "Interior detail", "Full vacuum including the trunk, carpets and mats shampooed, seats cleaned (leather cleaned and conditioned), dash, console, door panels, vents and glass."),
    ("exterior", "Exterior detail", "Hand wash, iron decontamination, clay bar, wheels, tires and wells, glass, and a paint sealant that protects for months."),
    ("full", "Full detail", "The interior and exterior details together. The one most people book once or twice a year."),
    ("enhance", "Paint enhancement", "Exterior detail plus a one-step machine polish that removes light swirls and brings back gloss."),
    ("correct2", "Two-step paint correction", "Compound, then polish, to remove heavier swirls and scratches. Paint thickness is checked before we start."),
]
DETAIL_ADDONS = [
    ("pet", "Pet hair removal"), ("headlight", "Headlight restoration"), ("engine", "Engine bay clean"),
    ("odor", "Odor treatment"), ("stain", "Stain extraction, per area"),
]
TINT_MENU = [  # (key, name, note)
    ("tint_front2", "Front two doors", "HITEK Ceramic IR, matched to your factory rear glass"),
    ("tint_ir", "Full car, Ceramic IR", "Side windows and back glass"),
    ("tint_plus", "Full car, Ceramic Plus", "Side windows and back glass, HITEK’s top heat rejection in our lineup"),
    ("tint_strip", "Windshield sun strip", "Down to the AS-1 line"),
    ("tint_windshield", "Full windshield heat film", "Clear ceramic film on the whole windshield"),
    ("tint_removal", "Tint removal", "Old film and glue off, rear defroster lines protected"),
]

# ---------------- places ----------------
AREAS = [  # slug, name
    ("window-tint-valley-station", "Valley Station"),
    ("window-tint-pleasure-ridge-park", "Pleasure Ridge Park"),
    ("window-tint-shively-ky", "Shively"),
    ("window-tint-fairdale-ky", "Fairdale"),
    ("window-tint-okolona", "Okolona"),
    ("window-tint-hillview-ky", "Hillview"),
    ("window-tint-shepherdsville-ky", "Shepherdsville"),
    ("window-tint-mount-washington-ky", "Mount Washington"),
    ("window-tint-radcliff-fort-knox", "Radcliff & Fort Knox"),
    ("window-tint-elizabethtown-ky", "Elizabethtown"),
    ("window-tint-st-matthews", "St. Matthews"),
    ("window-tint-jeffersontown", "Jeffersontown"),
]
AREA_NAMES_SCHEMA = ["Louisville", "Valley Station", "Pleasure Ridge Park", "Shively", "Fairdale", "Okolona",
                     "Hillview", "Shepherdsville", "Mount Washington", "Radcliff", "Fort Knox", "Elizabethtown",
                     "St. Matthews", "Jeffersontown"]

NAV = [
    ("Window Tint", "car-window-tint-louisville", [
        ("car-window-tint-louisville", "Car Window Tint"),
        ("ceramic-window-tint-louisville", "Ceramic Tint"),
        ("windshield-tint-louisville", "Windshield Tint"),
        ("tint-removal-louisville", "Tint Removal"),
        ("hitek-window-film-louisville", "HITEK Films"),
        ("window-tint-cost-louisville", "Tint Prices"),
    ]),
    ("Detailing", "auto-detailing-louisville", [
        ("auto-detailing-louisville", "Detailing Menu"),
        ("interior-detailing-louisville", "Interior Detailing"),
        ("exterior-detailing-louisville", "Exterior Detailing"),
        ("paint-correction-louisville", "Paint Correction"),
    ]),
    ("Kentucky Tint Law", "kentucky-tint-laws", []),
    ("Areas", "service-areas", [("service-areas", "All Service Areas")] + AREAS),
    ("Reviews", "reviews", []),
    ("About", "about", []),
]

# ---------------- helpers ----------------
def esc(s):
    return _html.escape(_html.unescape(s), quote=True)

def num(text, cls=""):
    """Numerals set like the logo's 502: soft heavy serif in red."""
    return f'<span class="num{(" " + cls) if cls else ""}">{text}</span>'

def btns(primary=("Get a quote", "@get-a-quote"), call=True, text=False, extra=None):
    out = [f'<a class="btn btn-red" href="{primary[1]}">{esc(primary[0])}</a>']
    if call:
        out.append(f'<a class="btn btn-line" href="tel:{PHONE_E164}">Call {PHONE}</a>')
    if text:
        out.append(f'<a class="btn btn-line" href="sms:{PHONE_E164}">Text us</a>')
    if extra:
        out.append(f'<a class="btn btn-line" href="{extra[1]}">{esc(extra[0])}</a>')
    return '<div class="btn-row">' + "".join(out) + "</div>"

def answer(text):
    """Short direct answer, written so search engines and AI assistants can quote it."""
    return f'<div class="answer"><p><strong>Short answer:</strong> {text}</p></div>'

def section(inner, cls="", sid=None):
    idattr = f' id="{sid}"' if sid else ""
    return f'<section class="band {cls}"{idattr}><div class="wrap">{inner}</div></section>'

def prose(*paras):
    return '<div class="prose">' + "".join(p if p.lstrip().startswith("<") else f"<p>{p}</p>" for p in paras) + "</div>"

def split(left, right, cls=""):
    return f'<div class="split {cls}"><div class="split-a">{left}</div><div class="split-b">{right}</div></div>'

def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def steps(items):
    """A real sequence: list of (title, body)."""
    out = "".join(f'<li><span class="step-n" aria-hidden="true">{i}</span><div><h3>{esc(t)}</h3><p>{b}</p></div></li>'
                  for i, (t, b) in enumerate(items, 1))
    return f'<ol class="steps">{out}</ol>'

def rows(items, cls=""):
    """Ruled list of (title, body, href|None). Used instead of a wall of identical cards."""
    out = []
    for it in items:
        t, b, href = (list(it) + [None])[:3]
        h = f'<a href="{href}">{esc(t)}</a>' if href else esc(t)
        out.append(f'<li><h3>{h}</h3><p>{b}</p></li>')
    return f'<ul class="rows {cls}">' + "".join(out) + "</ul>"

def table(head, body_rows, caption=None, note=None):
    cap = f"<caption>{esc(caption)}</caption>" if caption else ""
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    body = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in body_rows)
    n = f'<p class="table-note">{note}</p>' if note else ""
    return f'<div class="table-wrap"><table class="spec">{cap}<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>{n}'

def faq_html(faqs, heading="Questions we get a lot", hid="faq"):
    items = "".join(f'<details class="faq-item"><summary><h3>{esc(q)}</h3></summary><div class="faq-a"><p>{a}</p></div></details>'
                    for q, a in faqs)
    return f'<h2 id="{hid}">{esc(heading)}</h2><div class="faq">{items}</div>'

def area_links(exclude=None, prefix="Window tint in "):
    lis = "".join(f'<li><a href="@{s}">{esc(prefix)}{esc(n)}</a></li>' for s, n in AREAS if s != exclude)
    return f'<ul class="link-list">{lis}</ul>'

def hours_dl():
    def fmt(t):
        h, m = int(t[:2]), t[3:]
        suf = "AM" if h < 12 else "PM"
        h = h if h <= 12 else h - 12
        return f"{h}{'' if m == '00' else ':' + m} {suf}"
    rows_ = "".join(f'<div><dt>{d}</dt><dd>{fmt(o) + "–" + fmt(c) if o else "Closed"}</dd></div>' for d, o, c in HOURS)
    return f'<dl class="hours">{rows_}</dl>'

# ---------------- photos ----------------
# Shane's photos, prepared by photos_prep.py into assets/work/<name>-800.webp and -1600.webp.
IMG = {  # name: (alt text, object-position, short caption)
    "audi-q5-tint-red-bay": ("Black Audi Q5 with ceramic window tint in the red 502 Tinted bay, Louisville", "62% 55%", "Audi Q5"),
    "toyota-tacoma-tint-shop-front": ("Black Toyota Tacoma with HITEK ceramic tint outside 502 Tinted on Valley Station Road", "55% 62%", "Toyota Tacoma"),
    "range-rover-ceramic-tint": ("Black Range Rover with ceramic window tint inside the 502 Tinted shop", "50% 55%", "Range Rover"),
    "windshield-film-install": ("Windshield film installed on a car in the 502 Tinted bay", "50% 45%", "Windshield film"),
    "kia-sportage-tint-shop-front": ("Black Kia Sportage with fresh window tint in front of 502 Tinted", "45% 55%", "Kia Sportage"),
    "vw-tiguan-tint-hitek-bay": ("Black Volkswagen Tiguan with HITEK window tint, HITEK and 502 Tinted banners in the bay", "55% 45%", "VW Tiguan"),
    "toyota-rav4-tint-side": ("White Toyota RAV4 with dark ceramic tint, side view at 502 Tinted", "50% 55%", "Toyota RAV4"),
    "chevy-suburban-tint-hitek-bay": ("Chevrolet Suburban with ceramic tint under the HITEK American Tinter banner", "58% 50%", "Chevy Suburban"),
    "toyota-rav4-detailing-sign": ("White Toyota RAV4 under the 502 Tinted automotive detailing sign", "50% 42%", "Toyota RAV4"),
    "white-suburban-tint-red-bay": ("White Chevrolet Suburban with tinted rear glass in the red 502 Tinted bay", "45% 50%", "Chevy Suburban"),
    "vw-jetta-tint-gloss": ("Glossy black Volkswagen Jetta with window tint in the 502 Tinted shop", "50% 48%", "VW Jetta"),
    "honda-crv-tint-5410-valley-station": ("Silver Honda CR-V with window tint outside 502 Tinted, 5410 Valley Station Rd, Louisville", "45% 55%", "Honda CR-V"),
}
GALLERY = ["toyota-tacoma-tint-shop-front", "range-rover-ceramic-tint", "audi-q5-tint-red-bay", "toyota-rav4-tint-side",
           "vw-tiguan-tint-hitek-bay", "chevy-suburban-tint-hitek-bay", "white-suburban-tint-red-bay", "kia-sportage-tint-shop-front",
           "vw-jetta-tint-gloss", "honda-crv-tint-5410-valley-station"]

def srcset(name):
    return f"%ASSETS%/work/{name}-800.webp 800w, %ASSETS%/work/{name}-1600.webp 1600w"

def img(name, sizes="100vw", cls="", eager=False):
    alt, pos, _ = IMG[name]
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img class="{cls}" src="%ASSETS%/work/{name}-800.webp" srcset="{srcset(name)}" sizes="{sizes}" '
            f'width="1600" height="1200" alt="{esc(alt)}" style="object-position:{pos}" {load}>')

# Slots still waiting on a photo keep a labeled frame (listed in PHOTO-SHOT-LIST.md).
PHOTOS = {  # slot: (what to shoot, ratio, alt, image name or None)
    "tint-hero":        ("Side profile of a tinted sedan or SUV", "4/3", "", "toyota-rav4-tint-side"),
    "tint-install":     ("Film going on in the bay", "4/3", "", "vw-tiguan-tint-hitek-bay"),
    "ceramic-compare":  ("Ceramic tint on an SUV", "4/3", "", "chevy-suburban-tint-hitek-bay"),
    "windshield":       ("Windshield with a sun strip, shot from the front", "3/2", "Windshield sun strip installed to the AS-1 line", None),
    "removal":          ("Old purple or bubbling tint mid-removal", "3/2", "Removing old bubbled window tint", None),
    "hitek-rolls":      ("HITEK in the shop", "4/3", "", "chevy-suburban-tint-hitek-bay"),
    "detail-hero":      ("Foam wash on a car in the bay", "3/2", "Foam pre-wash during an auto detail in Louisville", None),
    "interior":         ("Clean front seats and dash after an interior detail", "3/2", "Interior detail with cleaned seats and dash", None),
    "interior-before":  ("Dirty carpet or seat before (pair with the after)", "1/1", "Car carpet before interior detailing", None),
    "interior-after":   ("Same carpet or seat after", "1/1", "Car carpet after interior detailing", None),
    "exterior":         ("Clay bar or iron remover bleeding purple on paint", "3/2", "Iron decontamination during an exterior detail", None),
    "correction-5050":  ("50/50 shot: half swirled, half corrected, under a light", "3/2", "Paint correction 50/50 under an inspection light", None),
    "correction-after": ("Gloss after polishing", "4/3", "", "audi-q5-tint-red-bay"),
    "about-shane":      ("Shane at the shop (natural, not posed)", "4/5", "Shane Crosier, owner of 502 Tinted", None),
    "about-shop":       ("Inside the bay", "4/3", "", "chevy-suburban-tint-hitek-bay"),
}

def photo(slot, cls="", sizes="(max-width: 960px) 100vw, 50vw"):
    desc, ratio, alt, name = PHOTOS[slot]
    if name:
        return f'<figure class="ph has-img {cls}" style="--r:{ratio}">{img(name, sizes)}</figure>'
    return (f'<figure class="ph {cls}" style="--r:{ratio}" data-slot="{slot}">'
            f'<span class="ph-mark" aria-hidden="true"></span>'
            f'<figcaption><span class="ph-k">Photo to come</span>{esc(desc)}</figcaption></figure>')

# ---------------- Google reviews (copied word for word from Shane's Google Business Profile) ----------------
GOOGLE_REVIEWS = [
    ("Jodie K.", "Tint removal and new tint",
     "I had my windows tinted at another shop and the quality of the work was terrible and the tint was hazy. I went to 502 tinted and he "
     "removed the old tint and tinted my windows. The quality of his work is top notch and I'm 100% satisfied. My only regret is not going "
     "to 502 tinted the first time."),
    ("Earl D.", "Window tint",
     "502 Tinted is awesome. They're the place to go in Louisville to get your windows tinted. High quality with affordable prices. "
     "Don't second guess when you know one of the best....502 Tinted."),
    ("Brittany B.", "Window tint",
     "They killed it! If your looking for a great price and great quality product, 502 Tinted is where ya need to go! Very fast and "
     "professional group of people! THANKS SHANE!"),
    ("Laneigh D.", "Window tint",
     "Best in the ville hands down! Such an amazing team and even better work! If you are needing your windows tinted, i highly recommend "
     "502 tinted. They will get your car looking right!"),
    ("Travis B.", "Window tint",
     "Shane and his team did excellent work on my wife’s car. Great communication through the whole process. 5 star company!"),
    ("Stephanie C.", "Window tint",
     "Great experience. The owner is extremely professional and nice. Answered all of our questions and was very accommodating. "
     "The quality of service is exceptional…"),
    ("Mike J.", "Window tint",
     "Got us in quickly and did a great job with my wife's vehicle. Using high quality materials, and looks great. I recommend 502 Tinted "
     "for all your tint needs!"),
    ("Hunter", "Window tint", "Shane did a great job on my windows!"),
]
STARS = '<span class="stars" role="img" aria-label="5 out of 5 stars">★★★★★</span>'

def review_cards(n=None):
    cards = "".join(
        f'<figure class="rv"><div class="rv-top">{STARS}<span class="rv-src">Google review</span></div>'
        f'<blockquote><p>{esc(t)}</p></blockquote><figcaption><strong>{esc(who)}</strong><span>{esc(what)}</span></figcaption></figure>'
        for who, what, t in GOOGLE_REVIEWS[:n])
    return f'<div class="rv-grid">{cards}</div>'

# ---------------- home page pieces ----------------
ICONS = {
    "star": '<path d="M12 2.8l2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z"/>',
    "shield": '<path d="M12 2.5l8 3v6c0 5-3.4 8.6-8 10-4.6-1.4-8-5-8-10v-6z"/><path d="M8.5 12l2.4 2.4 4.6-4.8"/>',
    "infinity": '<path d="M7 8.5c-2 0-3.5 1.6-3.5 3.5S5 15.5 7 15.5c3.5 0 6.5-7 10-7 2 0 3.5 1.6 3.5 3.5s-1.5 3.5-3.5 3.5c-3.5 0-6.5-7-10-7z"/>',
    "label": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
    "phone": '<path d="M6.6 3.5l2.7 3.7-1.7 2.4a12 12 0 006.8 6.8l2.4-1.7 3.7 2.7-1.2 2.9c-.3.7-1 1.1-1.8 1A17.8 17.8 0 013.4 6.5c-.1-.8.3-1.5 1-1.8z"/>',
}

def icon(name, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')

def trust_strip():
    items = [("star", f"{RATING} on Google", f"{REVIEWS} five-star reviews"),
             ("shield", "HITEK dealer", "Ceramic IR and Ceramic Plus"),
             ("infinity", "Lifetime warranty", "Nationwide, on the film"),
             ("clock", "Same-day tint", "Most cars done in a few hours")]
    lis = "".join(f'<li>{icon(i)}<div><strong>{esc(a)}</strong><span>{esc(b)}</span></div></li>' for i, a, b in items)
    return f'<section class="trust" aria-label="Why 502 Tinted"><div class="wrap"><ul>{lis}</ul></div></section>'

SERVICE_TILES = [
    ("Car window tint", "car-window-tint-louisville", "toyota-tacoma-tint-shop-front", "tint_ir", "Side windows and back glass"),
    ("Ceramic tint", "ceramic-window-tint-louisville", "range-rover-ceramic-tint", "tint_ir", "HITEK Ceramic IR and Ceramic Plus"),
    ("Windshield tint", "windshield-tint-louisville", "windshield-film-install", "tint_strip", "Sun strips and full heat film"),
    ("Tint removal", "tint-removal-louisville", "kia-sportage-tint-shop-front", "tint_removal", "Old film off, new film the same day"),
    ("Auto detailing", "auto-detailing-louisville", "toyota-rav4-detailing-sign", "wash", "Washes, interiors, full details"),
    ("Paint correction", "paint-correction-louisville", "vw-jetta-tint-gloss", "enhance", "Swirls out, gloss back"),
]

def service_tiles():
    tiles = "".join(
        f'<a class="tile" href="@{slug}">{img(name, "(max-width: 720px) 100vw, (max-width: 1100px) 50vw, 33vw", "tile-img")}'
        f'<span class="tile-body"><span class="tile-price">from {num(P(key))}</span><h3>{esc(t)}</h3>'
        f'<span class="tile-sub">{esc(sub)}</span><span class="tile-go">View {esc(t.lower())}</span></span></a>'
        for t, slug, name, key, sub in SERVICE_TILES)
    return f'<div class="tiles">{tiles}</div>'

def gallery():
    reel = ('<figure class="g-item g-reel"><video class="reel" src="%ASSETS%/work/expedition-reel.mp4" poster="%ASSETS%/work/expedition-reel-poster.webp" '
            'muted loop playsinline controls preload="none" aria-label="Walkaround video of a Ford Expedition with fresh tint at 502 Tinted"></video>'
            '<figcaption>Ford Expedition walkaround</figcaption></figure>')
    items = "".join(
        f'<figure class="g-item"><a href="%ASSETS%/work/{n}-1600.webp" data-lb>{img(n, "(max-width: 720px) 50vw, 25vw")}</a>'
        f'<figcaption>{esc(IMG[n][2])}</figcaption></figure>' for n in GALLERY)
    return (f'<div class="gallery">{reel}{items}</div>'
            '<dialog class="lb" aria-label="Photo"><img alt=""><button type="button" class="lb-x" aria-label="Close photo">×</button></dialog>')

def checker(cls=""):
    return f'<div class="checker {cls}" aria-hidden="true"></div>'

# ---------------- signature pieces ----------------
FAN = [(70, -4), (50, -15), (35, -26), (20, -37), (15, -48), (5, -59)]

def swatch_fan():
    """The hero object: a HITEK film sample deck fanned out on a light table. Overlaps stack, like real film."""
    strips = []
    for vlt, ang in FAN:
        a = round(0.97 - vlt / 100 * 0.97, 2) if vlt > 5 else 0.93
        dark = vlt <= 35
        ink = "#efedde" if dark else "#0d0d0d"
        strips.append(
            f'<g transform="translate(70 486) rotate({ang})">'
            f'<rect x="-34" y="-27" width="560" height="54" rx="9" fill="#151413" fill-opacity="{a}"/>'
            f'<rect x="-34" y="-27" width="560" height="54" rx="9" fill="none" stroke="#0d0d0d" stroke-opacity=".28"/>'
            f'<line x1="-26" y1="-25.5" x2="518" y2="-25.5" stroke="#fff" stroke-opacity=".38"/>'
            f'<text x="510" y="13" text-anchor="end" class="fan-n" fill="{ink}">{vlt}<tspan class="fan-p">%</tspan></text>'
            f'<text x="402" y="6" text-anchor="end" class="fan-l" fill="{ink}" fill-opacity=".8">Ceramic IR</text>'
            f'</g>')
    return f'''<figure class="fan">
<svg viewBox="0 0 640 560" role="img" aria-labelledby="fan-t">
<title id="fan-t">HITEK Ceramic IR film samples fanned out on a light table: 70, 50, 35, 20, 15 and 5 percent</title>
<defs><radialGradient id="lt" cx="62%" cy="38%" r="80%"><stop offset="0" stop-color="#f7f5ea"/><stop offset=".7" stop-color="#ebe8d6"/><stop offset="1" stop-color="#dcd8c3"/></radialGradient>
<radialGradient id="rv" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#d9d6cc"/><stop offset=".55" stop-color="#8a877f"/><stop offset="1" stop-color="#3a3936"/></radialGradient></defs>
<rect width="640" height="560" rx="16" fill="url(#lt)"/>
{"".join(strips)}
<circle cx="70" cy="486" r="15" fill="url(#rv)"/><circle cx="70" cy="486" r="5" fill="#2a2927"/>
</svg>
<figcaption>Kentucky allows <strong>35%</strong> on the front doors and <strong>18%</strong> behind the driver (<strong>8%</strong> on SUVs and vans).
<a href="@kentucky-tint-laws">How Kentucky measures it</a></figcaption>
</figure>'''

TOOL_SHADES = [70, 50, 35, 20, 15, 5]


def shade_tool():
    """Kentucky legality check on the studio sedan (the Texas Tinted visualizer):
    front doors and rear glass shaded independently; KRS 189.110 front 35%, behind the driver 18% or 8% for MPVs."""
    from sedan_svg import SEDAN_SVG

    def chips(group, default):
        return "".join(
            f'<button type="button" class="chip" data-group="{group}" data-vlt="{v}" aria-pressed="{"true" if v == default else "false"}">'
            f'<span class="chip-sw" style="--a:{(1 - v / 100):.2f}" aria-hidden="true"></span>{v}%</button>'
            for v in TOOL_SHADES)
    return f'''<div class="tool" data-tool>
<div class="tool-stage">{SEDAN_SVG}</div>
<div class="tool-ctl">
<fieldset class="seg"><legend>Vehicle</legend>
<label><input type="radio" name="veh" value="car" checked> Car or truck</label>
<label><input type="radio" name="veh" value="mpv"> SUV or van (MPV)</label>
</fieldset>
<div class="tool-row"><p class="tool-h" id="tf">Front doors</p><div class="chips" role="group" aria-labelledby="tf">{chips("front", 35)}</div></div>
<div class="tool-row"><p class="tool-h" id="tr">Rear doors, quarter glass and back glass</p><div class="chips" role="group" aria-labelledby="tr">{chips("rear", 20)}</div></div>
</div>
<div class="tool-out" aria-live="polite">
<p data-out="front" class="ok">35% on the front doors is legal in Kentucky.</p>
<p data-out="rear" class="ok">20% behind the driver is legal on a car or truck.</p>
<p class="tool-note">Kentucky rates the film itself (tested on clear glass), with a 3% tolerance. Your door-jamb label says MPV if your SUV or van qualifies for 8%. <a href="@kentucky-tint-laws">Read KRS 189.110 in plain English</a></p>
</div>
</div>'''


def price_list(items, note=None):
    """Dark price list with dotted leaders: items of (key, name, note)."""
    lis = "".join(f'<li><div class="pl-row"><h3 class="pl-name">{esc(n)}</h3><span class="pl-lead" aria-hidden="true"></span>'
                  f'<span class="pl-price"><small>from</small> {num(P(k))}</span></div><p>{esc(sub)}</p></li>' for k, n, sub in items)
    nt = f'<p class="pl-note">{note}</p>' if note else ""
    return f'<ul class="pl">{lis}</ul>{nt}'

def menu_card(title="Detailing menu", show_addons=True):
    """The printed menu card: ivory stock, ink type, red numerals."""
    pk = "".join(f'<li><div class="mc-row"><h3>{esc(n)}</h3><span class="mc-lead" aria-hidden="true"></span>'
                 f'<span class="mc-price"><small>from</small> {num(P(k))}</span></div><p>{esc(d)}</p></li>'
                 for k, n, d in DETAIL_MENU)
    ad = ""
    if show_addons:
        ad = ('<div class="mc-add"><h3>Add to any detail</h3><ul>' +
              "".join(f'<li><span>{esc(n)}</span><span class="mc-lead" aria-hidden="true"></span><span class="mc-price">{num(P(k))}</span></li>'
                      for k, n in DETAIL_ADDONS) + "</ul></div>")
    return f'''<div class="menu-card">
<div class="mc-head"><p class="mc-title">{esc(title)}</p><p class="mc-sub">Starting prices for cars. SUVs, trucks, vans and very dirty interiors are priced after we see them.</p></div>
<ul class="mc-list">{pk}</ul>{ad}
<p class="mc-foot">Book by phone or text: <a href="tel:{PHONE_E164}">{PHONE}</a></p>
</div>'''

def quote_form(preset=""):
    """Sample lead form. Swap the inside of .quote-slot for the GlassFlow embed when Shane's link is ready."""
    opt = lambda vals: "".join(f'<option{" selected" if v == preset else ""}>{esc(v)}</option>' for v in vals)
    pk = "".join(f"<option>{esc(n)}</option>" for _, n, _ in DETAIL_MENU)
    return f'''<div class="quote-slot" id="quote" data-glassflow-slot>
<!-- Sends to /api/quote (worker/index.js), which emails 502tinted@gmail.com. GLASSFLOW: replace this form with the embed when ready -->
<form class="qf" action="/api/quote" method="post" data-qf>
<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="qf-grid">
<label>Name<input name="name" autocomplete="name" required></label>
<label>Phone<input name="phone" type="tel" autocomplete="tel" required></label>
<label>Email <span class="opt">(optional)</span><input name="email" type="email" autocomplete="email"></label>
<label>Vehicle<input name="vehicle" placeholder="Year, make, model" required></label>
<label>Service<select name="service">{opt(["Window tint", "Detailing", "Tint and detailing", "Tint removal", "Paint correction", "Not sure yet"])}</select></label>
<label>Tint coverage<select name="coverage"><option>Full car (sides and back glass)</option><option>Front two doors</option><option>Windshield strip</option><option>Full windshield</option><option>Removal only</option><option>No tint</option></select></label>
<label>Film<select name="film"><option>Not sure, help me choose</option><option>HITEK Ceramic IR</option><option>HITEK Ceramic Plus</option></select></label>
<label>Shade<select name="shade"><option>Not sure</option><option>70%</option><option>50%</option><option>35%</option><option>20%</option><option>15%</option><option>5%</option></select></label>
<label>Detailing package<select name="detail_package"><option>No detailing</option>{pk}</select></label>
<label>Preferred day<input name="preferred_day" type="date"></label>
<label class="qf-wide">Anything else?<textarea name="message" rows="3" placeholder="Old tint to remove, pet hair, a date you need it done by"></textarea></label>
</div>
<div class="qf-foot"><button class="btn btn-red" type="submit">Send my quote request</button>
<p>Shane replies by text or call during shop hours. Rather text now? <a href="sms:{PHONE_E164}">{PHONE}</a></p></div>
<p class="qf-status" role="status" aria-live="polite"></p>
</form>
</div>'''


def pcard(label, key, sub, items, btn=("Get a quote", "@get-a-quote"), second=None):
    """Price card for interior heroes. second = (label, key) for a second starting price."""
    two = (f'<p class="pcard-k pcard-k2">{esc(second[0])}</p><p class="pcard-price pcard-price2">{num(P(second[1]))}</p>'
           if second else "")
    return (f'<aside class="pcard"><p class="pcard-k">{esc(label)}</p><p class="pcard-price">{num(P(key))}</p>{two}'
            f'<p class="pcard-sub">{sub}</p>{ticks(items)}<a class="btn btn-red" href="{btn[1]}">{esc(btn[0])}</a></aside>')


# ---------------- the two HITEK films we install (Shane's HITEK spec cards) ----------------
FILMS = [
    ("Ceramic IR", "hitek-ceramic-ir-card", 959, 423, "tint_ir",
     "HITEK Ceramic IR spec card: entry-level ceramic film with carbon-based technology, 65% TSER, 75% IRR, lifetime guarantee",
     "Entry-level ceramic film with carbon-based technology.", "65%", "75%", "2% to 70%", "Most daily drivers, commuters and leases"),
    ("Ceramic Plus", "hitek-ceramic-plus-card", 924, 371, "tint_plus",
     "HITEK Ceramic Plus spec card: true nano ceramic and IR coating technology film, 69% TSER, 90% IRR, lifetime guarantee",
     "True nano ceramic and IR coating technology.", "69%", "90%", "5% to 70%", "Cars that sit in the sun, dark interiors, work vehicles"),
]

def film_cards(link=True):
    out = []
    for name, f, w, h, key, alt, line, tser, irr, shades, best in FILMS:
        go = '<a class="btn btn-line" href="@ceramic-window-tint-louisville">Compare the two</a>' if link else ""
        out.append(
            f'<article class="film"><img src="%ASSETS%/work/{f}.webp" width="{w}" height="{h}" alt="{esc(alt)}" loading="lazy" decoding="async">'
            f'<div class="film-body"><h3>HITEK {esc(name)}</h3><p class="film-line">HITEK: “{esc(line)}”</p>'
            f'<ul class="facts"><li><b>Solar energy rejected</b><span>{tser} TSER</span></li><li><b>Infrared rejected</b><span>{irr} IRR</span></li>'
            f'<li><b>Shades</b><span>{shades}</span></li><li><b>Guarantee</b><span>Lifetime, from HITEK</span></li>'
            f'<li><b>Best for</b><span>{esc(best)}</span></li></ul>'
            f'<div class="film-foot"><span class="pl-price"><small>full car from</small> {num(P(key))}</span>{go}</div></div></article>')
    return '<div class="films">' + "".join(out) + "</div>"
