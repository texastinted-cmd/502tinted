# 502 Tinted website: going live on Cloudflare

The `site` folder is the complete website: 36 pages (including `404.html` and a `thank-you` page), `sitemap.xml`, `robots.txt`, `llms.txt` and `_headers`.
There's no old site, so there are no redirects to set up.

**Domain:** the site is built for `https://www.502tinted.com`. If Shane registers a different domain, change `BASE` at the top of
`src/kit.py`, rebuild (see the last section), and upload again. Every canonical link, the sitemap and Google's business data use it.

## 1. Get the domain onto Cloudflare

- **Buying it new:** Cloudflare dashboard → **Domain Registration** → **Register Domains** → search `502tinted.com`. It lands on Cloudflare automatically.
- **Already bought elsewhere:** **Add a domain** → enter it → Free plan → at the registrar, replace the nameservers with the two Cloudflare gives you.
  Keep any existing **MX** and **TXT** records if the domain already has email on it.

### During setup: don't block AI crawlers

Cloudflare blocks AI crawlers by default on new domains. That stops ChatGPT, Claude, Perplexity and Grok from reading the site.

- When setup asks about **Block AI training bots**, choose **Do not block**.
- Turn **off** **Instruct AI bot traffic with robots.txt** (managed robots.txt), so the site's own `robots.txt` is used.
- Later, under the domain's **AI Crawl Control**, set search and assistant crawlers to **Allow**.
- Leave **Bot Fight Mode** off.

## 2. Upload the site

1. **Workers & Pages** → **Create** → **Pages** → **Upload assets**.
2. Project name: `502tinted`. Drag in the **`site` folder** (not this whole package). Deploy.
3. Click around the `502tinted.pages.dev` preview. Clean URLs work automatically: `/car-window-tint-louisville` serves `car-window-tint-louisville.html`.

Prefer a Worker (like Texas Tinted's)? Install Node.js, open a terminal in this folder, run `npx wrangler login`, then `npx wrangler deploy`.
The included `wrangler.jsonc` deploys the `site` folder and shows the styled 404 page for missing URLs.

## 2b. How it deploys now: GitHub → Cloudflare Workers Builds

The Cloudflare Worker **502tinted** is connected to the GitHub repo `texastinted-cmd/502tinted`. Every push to `main` runs
`npx wrangler deploy`, which reads `wrangler.jsonc` and publishes the `site` folder (missing pages show `404.html`).
Build history: Cloudflare dashboard → Workers & Pages → 502tinted → Deployments / Builds.

## 3. Connect the domain

1. In the project → **Custom domains** → add `www.502tinted.com`, then `502tinted.com`.
2. Send the bare domain to `www`: **Rules** → **Redirect Rules** → create a rule: hostname equals `502tinted.com` → redirect to
   `https://www.502tinted.com${http.request.uri.path}`, status **301**, **Preserve query string** on.
3. **SSL/TLS** → **Full (strict)**, and turn on **Always Use HTTPS**.

## 4. Turn on the quote form

The form on `/get-a-quote` and `/contact` is a standard form post to FormSubmit (free, no account), which emails each request to
**502tinted@gmail.com** as a table and then sends the visitor to `/thank-you`.

1. After the site is live, send one test request from the form.
2. That first time, FormSubmit shows its own page asking to confirm the email, and emails 502tinted@gmail.com an **Activate Form** link
   (check Spam and Promotions too). Shane clicks it once.
3. Send a second test. It should land on the site's thank-you page, and the request should arrive in Gmail.
4. Optional: the activation email includes a random alias string. Paste it into `FORM_ID` in `src/kit.py` and rebuild,
   so the Gmail address isn't in the page source.

**GlassFlow later:** the form sits inside `<div class="quote-slot" data-glassflow-slot>` with a `GLASSFLOW` comment. Replace the `<form>`
in `quote_form()` in `src/kit.py` with the GlassFlow embed (or point the "Get a quote" buttons at the GlassFlow link), rebuild, upload.

## 5. The day it goes live

1. **Google Business Profile:** set the website to `https://www.502tinted.com/`. Keep the name, address and phone exactly as on the site:
   502 Tinted, 5410 Valley Station Rd #108, Louisville, KY 40272, (502) 631-0419. Add the services with the same starting prices.
2. **Google Search Console:** add the domain (Cloudflare can add the verification record), submit `https://www.502tinted.com/sitemap.xml`,
   and request indexing for the home, car tint, ceramic tint, detailing, Kentucky tint law and Valley Station pages.
3. **Bing Webmaster Tools:** import from Search Console. Bing feeds ChatGPT search and Copilot.
4. **Facebook:** put the website link in the page's About section.
5. Open `https://www.502tinted.com/robots.txt` and `/llms.txt` in a browser. Both should show this site's own text.

## 6. Analytics (optional)

Nothing is tracking yet. When Shane has a Google Analytics 4 ID or a Meta Pixel ID, paste them into `GA4_ID` / `META_PIXEL_ID`
near the top of `src/build.py` and rebuild. They load only on the live build.

## 7. Photos

Shane's 12 shop photos and the Ford Expedition walkaround video are on the site (in `site/assets/work`, resized, with location data stripped).
On phones, the video plays muted behind the headline on the home page; on computers the Audi Q5 photo from the red bay is the header.
A few spots, mostly detailing (interior before/after, a paint correction 50/50, a sun strip, a portrait of Shane), still show a labeled frame.
`PHOTO-SHOT-LIST.md` lists them. Send those photos to Claude and they'll be placed for you.

## 8. Prices

All prices are samples until Shane confirms them. They live in one place: `PRICES` in `src/kit.py`. Change a number there,
rebuild, and every page, the schema data and `llms.txt` update together.

## Updating the site

This repo is connected to the Cloudflare Worker `502tinted`. Every push to `main` redeploys the site within a minute or two.

To change something: edit the content in `src/` (prices are in `PRICES` in `src/kit.py`), run `python3 src/build.py` to regenerate `site/`,
then commit and push. Or ask Claude to make the change.
