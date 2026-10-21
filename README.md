# 502 Tinted website

www.502tinted.com: window tint and auto detailing in Valley Station, Louisville, KY.

- `site/` is the live website. Cloudflare serves this folder as is, with no build command. Every push to `main` redeploys it.
- `src/` holds the generator that writes every page (`python3 src/build.py`). Prices live in `PRICES` in `src/kit.py`.
- `assets/` holds the source styles, script, logo and Shane's photos.
- `DEPLOY.md` covers Cloudflare, the domain, the quote form and analytics. `PHOTO-SHOT-LIST.md` lists the photo spots still waiting on a picture.

Python 3 with Pillow is the only requirement for rebuilding (`pip install pillow`).
