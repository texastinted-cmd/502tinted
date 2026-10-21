# 502 Tinted website

www.502tinted.com: window tint and auto detailing in Valley Station, Louisville, KY.

- `site/` is the live website. The Cloudflare Worker `502tinted` deploys it with `wrangler.jsonc` on every push to `main`.
- `src/` holds the generator that writes every page (`python3 src/build.py`). Prices live in `PRICES` in `src/kit.py`.
- `assets/` holds the source styles, script, logo and Shane's photos.
- `worker/index.js` handles the quote form (`POST /api/quote`): it emails 502tinted@gmail.com through Cloudflare Email Routing and redirects to `/thank-you`. Everything else is static.
- `DEPLOY.md` covers Cloudflare, the domain, the quote form and analytics. `PHOTO-SHOT-LIST.md` lists the photo spots still waiting on a picture.

Python 3 with Pillow is the only requirement for rebuilding (`pip install pillow`).
