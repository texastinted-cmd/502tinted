"""Bundle the whole site into ONE self-contained HTML file for sharing (text, email, AirDrop).

Built to work even where a phone previews the file without running scripts (iPhone Messages, Mail and Files previews):
- every page is in the document; CSS :target shows one at a time (links go to #p-<slug>), no JavaScript needed
- each photo is embedded once, as a CSS variable, and painted as a background, so the file stays small
- the menu opens with a checkbox, the FAQ uses <details>; the shade checker and form come alive where scripts run
Output: dist/502-tinted-website-preview.html
"""
import base64, html as H, io, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import build
from PIL import Image

ROOT = build.ROOT
ASSETS = os.path.join(ROOT, "assets")
OUT = os.path.join(ROOT, "dist", "502-tinted-website-preview.html")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

VARS = {}  # asset path -> css variable name

def var_for(path):
    if path not in VARS:
        VARS[path] = "--a" + str(len(VARS))
    return VARS[path]

def data_uri(path, max_w=None, q=70):
    full = os.path.join(ASSETS, path)
    if max_w and path.endswith(".webp"):
        im = Image.open(full)
        if im.width > max_w:
            im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
        buf = io.BytesIO(); im.save(buf, "WEBP", quality=q, method=6)
        return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()
    mime = {"webp": "image/webp", "png": "image/png", "jpg": "image/jpeg"}[path.rsplit(".", 1)[1]]
    return f"data:{mime};base64," + base64.b64encode(open(full, "rb").read()).decode()

ATTR = re.compile(r'([a-zA-Z-]+)="([^"]*)"')

def img_to_span(m):
    attrs = dict(ATTR.findall(m.group(0)))
    src = attrs.get("src", "")
    if not src.startswith("assets/"):
        return m.group(0)
    path = src[len("assets/"):].replace("-800.webp", "-1600.webp")
    cls = ("im " + attrs.get("class", "")).strip()
    style = f"background-image:var({var_for(path)})"
    pos = re.search(r"object-position:([^;\"]+)", attrs.get("style", ""))
    if pos:
        style += f";background-position:{pos.group(1)}"
    alt = attrs.get("alt", "")
    role = f' role="img" aria-label="{alt}"' if alt else ' aria-hidden="true"'
    return f'<span class="{cls}" style="{style}"{role}></span>'

def page_html(p, sedan):
    slug = p["slug"]
    h = build.resolve(build.body_html(p, "preview"), "preview")
    h = h.replace('<a class="skip" href="#main">Skip to content</a>', "")
    h = re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"', lambda m: f'href="#p-{m.group(1)}"', h)
    if slug != "index":
        h = re.sub(r'href="#(?!p-)[^"]*"', f'href="#p-{slug}"', h)
    # gallery: no lightbox in the file; the walkaround video becomes its still frame
    h = re.sub(r'<a href="assets/work/[^"]+" data-lb>(.*?)</a>', r"\1", h, flags=re.S)
    h = re.sub(r'<dialog class="lb".*?</dialog>', "", h, flags=re.S)
    h = re.sub(r'<video class="reel"[^>]*></video><figcaption>[^<]*</figcaption>',
               '<img src="assets/work/expedition-reel-poster.webp" alt="Ford Expedition with fresh tint at 502 Tinted">'
               '<figcaption>Walkaround video plays on the live site</figcaption>', h)
    h = re.sub(r'<video class="hero-reel"[^>]*></video>',
               '<img class="hero-reel" src="assets/work/expedition-reel-poster.webp" alt="">', h)
    h = re.sub(r"<img [^>]*>", img_to_span, h)
    h = h.replace('href="assets/sedan.webp"', f'href="{sedan}"')
    # menu without scripts: a checkbox per page
    h = re.sub(r'<button class="nav-toggle"[^>]*>(.*?)</button>',
               lambda m: f'<input type="checkbox" class="nav-check" id="nc-{slug}" hidden><label class="nav-toggle" for="nc-{slug}" aria-label="Menu">{m.group(1)}</label>', h, flags=re.S)
    h = h.replace('name="veh"', f'name="veh-{slug}"')
    h = h.replace('action="#"', f'action="#p-{slug}" method="get"').replace('method="post" data-qf', 'data-qf')
    h = re.sub(r'<a ([^>]*)href="(https?://[^"]+)"', r'<a \1href="\2" target="_blank"', h)
    left = re.findall(r'(?:src|href|poster|data-src)="assets/[^"]+"', h)
    assert not left, (slug, left[:3])
    return f'<div class="pg" id="p-{slug}">{h}</div>'

SHARE_CSS = """
.pg { display: none; }
.pg:target, #p-index { display: block; }
body:has(.pg:target:not(#p-index)) #p-index { display: none; }
.im { display: block; background-size: cover; background-repeat: no-repeat; background-position: center; }
.logo .im { width: 72px; height: 66px; background-size: contain; }
.foot-logo.im { width: 120px; height: 110px; background-size: contain; background-position: left center; }
.hero-bg .im { position: absolute; inset: 0; }
.tile .im { position: absolute; inset: 0; z-index: -2; }
.ph .im, .g-item .im { width: 100%; height: 100%; }
.g-reel .im { position: absolute; inset: 0; }
.film > .im { width: 100%; aspect-ratio: 959 / 423; background-size: contain; background-color: #000; }
.nav-check:checked ~ .nav { display: block; }
.nav-check:checked ~ .nav-toggle .bars { background: transparent; }
.nav-check:checked ~ .nav-toggle .bars::before { top: 0; transform: rotate(45deg); }
.nav-check:checked ~ .nav-toggle .bars::after { top: 0; transform: rotate(-45deg); }
label.nav-toggle { cursor: pointer; }
.share-note { background: var(--red); color: var(--ivory); text-align: center; font-size: .9rem; padding: 8px 16px; margin: 0; }
@media (max-width: 720px) { .logo .im { width: 60px; height: 55px; } }
"""

def main():
    build.build()
    sedan = data_uri("sedan.webp")
    pages = "".join(page_html(p, sedan) for p in build.PAGES)
    roots = []
    for path, v in VARS.items():
        big = "work/" in path and path.endswith("-1600.webp")
        roots.append(f'{v}:url("{data_uri(path, max_w=1200 if big else None, q=66)}");')
    fleur = data_uri("fleur.png")
    css = open(os.path.join(ASSETS, "site.css")).read().replace('url("fleur.png")', f'url("{fleur}")')
    js = open(os.path.join(ASSETS, "site.js")).read()
    titles = json.dumps({p["slug"]: H.unescape(p["title"]) for p in build.PAGES}, ensure_ascii=False)
    title_js = ("<script>(function(){var t=" + titles + ";function s(){var h=location.hash.slice(3);document.title=t[h]||t['index'];}"
                "window.addEventListener('hashchange',s);s();})();</script>")
    out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0d0d0d">
<title>502 Tinted Website Preview</title>
<link rel="icon" type="image/png" href="{data_uri('favicon-48.png')}">
<link rel="stylesheet" href="{build.FONTS}">
<style>:root{{{"".join(roots)}}}</style>
<style>{css}{SHARE_CSS}</style>
</head>
<body>
<p class="share-note">Website preview for 502 Tinted. The live site will be at www.502tinted.com.</p>
{pages}
<script>{js}</script>
{title_js}
</body>
</html>
"""
    with open(OUT, "w") as fh:
        fh.write(out)
    print(f"{OUT}: {os.path.getsize(OUT) / 1e6:.1f} MB, {len(build.PAGES)} pages, {len(VARS)} embedded images")

if __name__ == "__main__":
    main()
