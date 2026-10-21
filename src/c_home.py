from kit import *


def home():
    hero = f'''<section class="hero hero-photo home-hero">
<div class="hero-bg">{img("audi-q5-tint-red-bay", "100vw", "hero-img", eager=True)}
<video class="hero-reel" muted loop playsinline preload="none" poster="%ASSETS%/work/expedition-reel-poster.webp" data-src="%ASSETS%/work/expedition-reel.mp4" aria-hidden="true"></video></div>
<div class="wrap hero-in"><div class="hero-copy">
<h1>Window tint and auto detailing in Louisville, KY</h1>
<p class="lede">HITEK ceramic tint from {P("tint_ir")} and full details from {P("full")}, at our shop on Valley Station Road. Every tint job carries HITEK’s lifetime guarantee.</p>
<div class="btn-row hero-btns"><a class="btn btn-ivory" href="tel:{PHONE_E164}">Call {PHONE}</a><a class="btn btn-red" href="@get-a-quote">Get a quote</a><a class="btn btn-line" href="#services">View services</a></div>
<p class="hero-rating">{STARS}<span><strong>{RATING}</strong> on Google from {REVIEWS} reviews</span></p>
</div></div>
</section>
{checker()}
{trust_strip()}'''

    services = f'''<div class="band-head"><h2>Tint and detailing on Valley Station Road</h2>
<p>Ceramic window tint, windshield film, tint removal and detailing, with the starting price on every service.</p></div>
{service_tiles()}'''

    reviews = f'''<div class="rv-head"><div class="rating">{num(RATING)}<div>{STARS}<p>{REVIEWS} reviews on Google</p></div></div>
<h2>What Louisville drivers say</h2></div>
{review_cards(6)}
<div class="btn-row">{f'<a class="btn btn-red" href="{MAPS_URL}" rel="noopener">Read all reviews on Google</a>'}<a class="btn btn-line" href="@reviews">More reviews</a></div>'''

    work = f'''<div class="band-head"><h2>Recent work</h2>
<p>Straight from the bay on Valley Station Road. Tap a photo to see it bigger, or follow along on <a href="{FACEBOOK}" rel="noopener">Facebook</a>.</p></div>
{gallery()}'''

    tint = split(
        swatch_fan(),
        f'''<h2>Window tint prices</h2>
<p class="note">Starting prices for cars. SUVs, trucks and vans have more glass and are priced by the window count.</p>
{price_list(TINT_MENU)}
<h3 style="margin-top:32px">Two HITEK ceramic films</h3>
{rows([("Ceramic IR", "HITEK’s entry-level ceramic: 65% of solar energy and 75% of infrared heat rejected, light to dark. The right choice for most daily drivers.", "@ceramic-window-tint-louisville"),
       ("Ceramic Plus", "HITEK’s nano ceramic with an IR coating: 69% of solar energy and 90% of infrared rejected. Worth it if your car sits in the sun all day or you drive for work.", "@ceramic-window-tint-louisville")], "rows-1")}
<p class="note">Both carry HITEK’s lifetime guarantee. <a href="@window-tint-cost-louisville">What changes the price</a> · <a href="@hitek-window-film-louisville">About HITEK</a></p>''',
        "split-top")

    menu = f'''<div class="band-head"><h2>Detailing, priced up front</h2>
<p>The same menu we use at the counter. Call or text if your vehicle needs something that isn’t on it.</p></div>
{menu_card()}'''

    tool = f'''<div class="band-head"><h2>Check your shade against Kentucky law</h2>
<p>Kentucky changed its tint law in 2024. Pick a shade for the front and the back, and pick your vehicle type: SUVs and vans can go darker behind the driver than cars can.</p></div>
{shade_tool()}'''

    why = f'''<h2>Why drivers come to Valley Station for tint</h2>
{rows([
    ("Ceramic film only", "No bargain film that turns purple and bubbles in a few summers. Every film we install is a HITEK ceramic with a lifetime guarantee."),
    ("Clean installs", "Film cut to your glass, edges finished tight, and every window checked in daylight before you pick up."),
    ("Same-day tint", "Most cars are in and out the same day. Drop it off in the morning and pick it up that afternoon."),
    ("Prices on the page", f"Tint from {P('tint_ir')}, details from {P('wash')}. You know the starting number before you call."),
    ("The owner picks up", "Call or text and you talk to Shane. He quotes every job and stands behind the work."),
    ("Tint and detailing together", "Book both and the car gets cleaned first, which means cleaner glass under the film."),
], "rows-3")}'''

    owner = split(
        photo("about-shop"),
        f'''<h2>Owned and run by Shane Crosier</h2>
{answer(f"502 Tinted is a window tint and auto detailing shop at {ADDRESS_LINE}, in Valley Station near Dixie Highway. "
        f"Shane Crosier and his team install HITEK Ceramic IR and Ceramic Plus window film (car tint from {P('tint_ir')}), "
        f"and offer interior, exterior and full details from {P('wash')} plus paint correction. Open Monday to Saturday; call or text {PHONE}.")}
<p>Clean installs, fair prices and straight answers. That’s the whole approach, and it’s why the reviews read the way they do.</p>
<p><a href="@about">More about Shane and the shop</a></p>''')

    areas = f'''<div class="band-head"><h2>Where our customers drive in from</h2>
<p>We’re in Valley Station in southwest Louisville, close to Dixie Highway and the Gene Snyder. Customers come from all over Louisville, Bullitt County and Hardin County.</p></div>
{area_links()}'''

    faqs = [
        ("How much is window tint at 502 Tinted?",
         f"Tinting a car’s side windows and back glass starts at {P('tint_ir')} with HITEK Ceramic IR and {P('tint_plus')} with HITEK Ceramic Plus. "
         f"Front two doors only start at {P('tint_front2')}. SUVs, trucks and vans are priced by the number of windows."),
        ("What’s the darkest legal tint in Kentucky?",
         "35% on the front side windows. Behind the driver, 18% on cars and trucks, or 8% on SUVs and vans labeled as multipurpose passenger vehicles (MPV) on the door jamb."),
        ("How long does window tint take?",
         "Most cars take two to four hours. Removing old film adds time. Most customers drop off in the morning and pick up the same day."),
        ("Do you offer detailing and tint on the same day?",
         "Yes. Book both and we detail first so the glass is as clean as possible before the film goes on. Call or text to plan the timing."),
        ("Where is 502 Tinted?",
         f"{ADDRESS_LINE}. That’s in Valley Station in southwest Louisville, a few minutes from Dixie Highway (US 31W) and the Gene Snyder Freeway."),
        ("What are your hours?",
         "Monday, Tuesday, Thursday and Friday 9 AM to 3 PM, Wednesday 10 AM to 5 PM, Saturday 8 AM to 1 PM. Closed Sunday."),
    ]

    body = (section(services, "", "services") + section(reviews, "band-raised band-reviews") + section(work)
            + section(tint, "band-raised") + section(menu) + section(tool, "band-raised", "shade-check")
            + section(why) + section(owner, "band-raised") + section(areas))
    return dict(
        slug="index", group="Main", crumb="Home", hero=hero,
        title="Window Tint & Detailing Louisville, KY | 502 Tinted",
        desc=f"HITEK ceramic window tint from {P('tint_ir')} and auto detailing in Valley Station, Louisville. Lifetime guarantee, rated 5.0 on Google. Call or text {PHONE}.",
        h1="Window tint and auto detailing in Louisville, KY", lede="",
        body=body, faqs=faqs,
    )


def pages():
    return [home()]
