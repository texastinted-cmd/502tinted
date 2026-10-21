from kit import *

MAP_EMBED = ('<!--PROD:<iframe class="map" title="Map to 502 Tinted, 5410 Valley Station Rd, Louisville" loading="lazy" '
             'referrerpolicy="no-referrer-when-downgrade" '
             'src="https://www.google.com/maps?q=5410+Valley+Station+Rd+%23108,+Louisville,+KY+40272&amp;output=embed"></iframe>-->')


def about():
    body = section(split(
        prose("<h2>The shop</h2>",
              f"502 Tinted is a window tint and auto detailing shop in Valley Station, in southwest Louisville. It’s owned and run by "
              f"{OWNER}. The name is the area code, and the fleur-de-lis in the logo is the one you see all over this city.",
              "We do two things: HITEK ceramic window tint and detailing, from a maintenance wash to two-step "
              "paint correction. Keeping the list short is on purpose. It’s how the work stays good.",
              f"Customers come from Valley Station and Pleasure Ridge Park, from across Louisville, and from Bullitt and Hardin County. "
              f"The shop has a {RATING}-star Google rating from {REVIEWS} reviews."),
        photo("about-shane")))
    body += section(
        '<h2>How Shane runs it</h2>'
        + rows([
            ("Ceramic film only", "No bargain film that turns purple. Every tint job is HITEK Ceramic IR or Ceramic Plus, with HITEK’s lifetime guarantee."),
            ("Clean installs", "Film cut to your glass, edges finished tight, and every window checked in daylight before you pick up."),
            ("Prices in the open", "Starting prices for tint and detailing are posted on this site, so you know the number before you call."),
            ("Straight answers", "If a scratch won’t polish out, you’ll hear that before any work starts."),
        ]), "band-raised")
    body += section(split(
        photo("about-shop"),
        prose("<h2>Faith and work</h2>",
              "Shane is a Christian, and he tries to run the shop the way Colossians 3:23 puts it: whatever you do, work at it with all "
              "your heart. In practice that means honest prices, careful work and treating your car like it’s his own.",
              "You won’t get a sermon with your tint. You’ll get a clean job and a straight answer.")))
    body += section(prose(
        "<h2>Why one shop for tint and detailing</h2>",
        "Tint and detailing overlap more than people think. Film goes on the inside of the glass, so the cleaner the glass, the door panels "
        "and the seals are, the cleaner the install. Doing both under one roof means the car gets detailed first and tinted second, and you "
        "only drop it off once.",
        "It also means one person is responsible for the whole car. If something about the tint or the detail isn’t right, there’s no "
        "finger-pointing between two businesses. Text Shane and he’ll handle it.",
        '<a href="@car-window-tint-louisville">Window tint</a> · <a href="@auto-detailing-louisville">Detailing menu</a> · <a href="@kentucky-tint-laws">Kentucky tint law</a>'))
    body += section(
        '<div class="split split-top"><div><h2>Visit the shop</h2>'
        + '<ul class="facts">'
          f'<li><b>Address</b><span><a href="{MAPS_URL}" rel="noopener">{ADDRESS_LINE}</a></span></li>'
          f'<li><b>Phone or text</b><span><a href="tel:{PHONE_E164}">{PHONE}</a></span></li>'
          f'<li><b>Email</b><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>'
          f'<li><b>Owner</b><span>{OWNER}</span></li>'
          '<li><b>Films</b><span>HITEK dealer: Ceramic IR, Ceramic Plus</span></li>'
          '</ul></div><div><h2>Hours</h2>' + hours_dl() + btns() + '</div></div>', "band-raised")
    return dict(
        slug="about", group="Company", crumb="About",
        title="About 502 Tinted | Shane Crosier, Valley Station Louisville",
        desc=f"502 Tinted is a window tint and detailing shop in Valley Station, Louisville, run by owner {OWNER}. HITEK dealer, posted prices, 5.0 on Google.",
        h1="About 502 Tinted",
        lede=f"A Louisville tint and detailing shop, owned and run by {OWNER} on Valley Station Road.",
        body=body,
        schema_extra=[{"@type": "AboutPage", "@id": BASE + "/about#aboutpage", "url": BASE + "/about",
                       "mainEntity": {"@id": BASE + "/#business"}}],
    )


def reviews():
    body = section(
        f'''<div class="rv-head"><div class="rating">{num(RATING)}<div>{STARS}<p>{REVIEWS} reviews on Google</p></div></div>
<h2>Straight from Google</h2></div>
<p class="note" style="margin:-8px 0 28px">Word for word from 502 Tinted’s Google Business Profile. First name and last initial only.</p>
{review_cards()}
{btns(("Read all reviews on Google", MAPS_URL), call=False, extra=("Facebook", FACEBOOK))}''')
    body += section(split(
        photo("about-shop"),
        prose("<h2>Had your car done here?</h2>",
              "A review helps more than you’d think. Most people find a tint shop by searching, and reviews are what they read first.",
              steps([("Open Google Maps", "Search for 502 Tinted, Louisville."),
                     ("Tap Reviews", "Then tap Write a review."),
                     ("Say what you had done", "Mention the service, like ceramic tint or a full detail, and the vehicle. That helps the next person.")]))),
        "band-raised")
    body += section(prose(
        "<h2>What you can expect</h2>",
        ticks([f"Starting prices posted online: tint from {P('tint_ir')}, details from {P('wash')}",
               "HITEK ceramic film only, with a nationwide lifetime warranty",
               "Clean edges, every window checked before you pick up",
               "A straight answer when something can’t be done, before any work starts",
               "Most tint jobs and details finished the same day"]),
        f"Something not right after your appointment? Text {PHONE}. Shane would rather fix it than read about it."))
    return dict(
        slug="reviews", group="Company", crumb="Reviews",
        title=f"502 Tinted Reviews | {RATING} Stars on Google | Louisville",
        desc=f"502 Tinted has a {RATING}-star Google rating from {REVIEWS} reviews. Read what Louisville drivers say about the window tint and the work.",
        h1="502 Tinted reviews", lede=f"{RATING} stars on Google from {REVIEWS} reviews, all written by customers.",
        body=body, proof=False,
    )


FAQ_GROUPS = [
    ("Window tint", [
        ("How much is window tint at 502 Tinted?",
         f"{P('tint_ir')} and up for a car’s side windows and back glass in HITEK Ceramic IR, {P('tint_plus')} and up in Ceramic Plus, and {P('tint_front2')} and up for the front two doors. SUVs and trucks are priced by window count."),
        ("What films do you use?",
         "HITEK Ceramic IR and HITEK Ceramic Plus. Both are ceramic, with no metal layer, and carry a nationwide lifetime warranty."),
        ("How long does tint take?", "Two to four hours for most cars, longer if old film has to come off."),
        ("When can I roll the windows down?", "After three to five days. Give it the full five in cool or damp weather."),
        ("Do you remove old tint?", f"Yes, from {P('tint_removal')}, with the rear defroster protected. Most customers retint the same visit."),
    ]),
    ("Kentucky tint law", [
        ("What’s the darkest legal tint in Kentucky?",
         "35% on the front side windows; 18% behind the driver on cars and trucks; 8% behind the driver on SUVs and vans labeled MPV."),
        ("Is windshield tint legal in Kentucky?",
         "A strip above the AS-1 line is. Since July 15, 2024, film on the whole windshield is too, if the windshield with film still lets through at least 70% of light."),
        ("Do I need a tint sticker in Kentucky?",
         "Yes. Installers must put a compliance label on the inside of the driver’s door jamb."),
        ("Does factory glass count toward Kentucky’s limits?",
         "Not for side and rear windows. Kentucky rates the film on clear glass. The windshield is judged with its glass."),
    ]),
    ("Detailing", [
        ("How much is a full detail?", f"From {P('full')} for a car. SUVs, trucks and vans are priced after a look."),
        ("How long does a full detail take?", "Four to six hours for a typical car."),
        ("Do you do paint correction?", f"Yes. One-step paint enhancement from {P('enhance')}, two-step correction from {P('correct2')}."),
        ("Can you remove pet hair?", f"Yes, as an add-on ({P('pet')}) to an interior or full detail."),
    ]),
    ("Booking and the shop", [
        ("Where is 502 Tinted?", f"{ADDRESS_LINE}, in Valley Station in southwest Louisville."),
        ("What are your hours?", "Monday, Tuesday, Thursday and Friday 9 AM to 3 PM; Wednesday 10 AM to 5 PM; Saturday 8 AM to 1 PM; closed Sunday."),
        ("How do I book?", f"Call or text {PHONE}, or send the quote form on this site. Shane replies during shop hours."),
        ("Can I get tint and a detail on the same day?", "Yes. We detail first, then tint."),
        ("Who owns 502 Tinted?", f"{OWNER}."),
    ]),
]


def faq_hub():
    body = "".join(section(faq_html(qs, title, f"faq-{i}"), "band-raised" if i % 2 else "") for i, (title, qs) in enumerate(FAQ_GROUPS))
    return dict(
        slug="faq", group="Company", crumb="FAQ",
        title="Window Tint & Detailing FAQ | 502 Tinted Louisville",
        desc="Answers about window tint prices, HITEK films, Kentucky tint law, detailing, hours and booking at 502 Tinted in Valley Station, Louisville.",
        h1="Questions and answers",
        lede="Tint, Kentucky law, detailing and booking. If your question isn’t here, text it to us.",
        body=body, faqs=[q for _, qs in FAQ_GROUPS for q in qs], faq_inline=True, proof=False,
    )


def contact():
    body = section(split(
        f'''<h2>Call, text or stop by</h2>
<ul class="facts">
<li><b>Address</b><span><a href="{MAPS_URL}" rel="noopener">{ADDRESS_LINE}</a></span></li>
<li><b>Phone or text</b><span><a href="tel:{PHONE_E164}">{PHONE}</a></span></li>
<li><b>Email</b><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>
<li><b>Facebook</b><span><a href="{FACEBOOK}" rel="noopener">502 Tinted on Facebook</a></span></li>
</ul>
<h3 style="margin-top:28px">Hours</h3>{hours_dl()}
<p class="note">Texting is the fastest way to reach Shane during the day. Send your vehicle and what you want done.</p>
{MAP_EMBED}<!--PREVIEW--><p><a class="map-link" href="{MAPS_URL}" rel="noopener">Open in Google Maps</a></p><!--/PREVIEW-->''',
        '<h2>Send a quote request</h2>' + quote_form(), "split-top"))
    body += section(prose(
        "<h2>Finding the shop</h2>",
        "We’re in Valley Station in southwest Louisville, a few minutes from Dixie Highway (US 31W) and the Gene Snyder Freeway. "
        "From Shively and Pleasure Ridge Park, head south on Dixie. From Okolona, Fairdale or Jeffersontown, take the Gene Snyder west. "
        "From Radcliff and Fort Knox, come north on US 31W.",
        '<a href="@service-areas">All the areas we serve</a>'), "band-raised")
    return dict(
        slug="contact", group="Company", crumb="Contact",
        title="Contact 502 Tinted | Valley Station, Louisville, KY",
        desc=f"Contact 502 Tinted at 5410 Valley Station Rd #108, Louisville. Call or text {PHONE}, or email. Hours, directions and a quote form.",
        h1="Contact 502 Tinted", lede=f"Call or text {PHONE}, or send a quote request below.",
        hero_btns="", body=body, proof=False, cta=False,
    )


def quote():
    body = section(split(
        '<h2>Tell us about your vehicle</h2>' + quote_form(),
        prose("<h2>What happens next</h2>",
              steps([("Shane reads it", "Quote requests come straight to the shop."),
                     ("You get a price", "By text or call during shop hours, with the film, shade or package that fits."),
                     ("Pick a day", "Drop off at the shop. Most tint jobs and details are done the same day.")]),
              "<h3>Starting prices</h3>",
              price_list([("tint_ir", "Car tint, Ceramic IR", "Side windows and back glass"),
                          ("tint_plus", "Car tint, Ceramic Plus", "Side windows and back glass"),
                          ("full", "Full detail", "Interior and exterior"),
                          ("interior", "Interior detail", "Carpets, seats, plastics, glass")]),
              f'Rather talk? Call or text <a href="tel:{PHONE_E164}">{PHONE}</a>.'),
        "split-top"))
    return dict(
        slug="get-a-quote", group="Company", crumb="Get a Quote",
        title="Get a Window Tint or Detailing Quote | 502 Tinted",
        desc=f"Request a window tint or auto detailing quote from 502 Tinted in Louisville. Car tint from {P('tint_ir')}, full details from {P('full')}. Reply by text.",
        h1="Get a quote", lede=f"Send your vehicle and what you want done. Shane replies by text or call during shop hours. Rather text now? <a href=\"sms:{PHONE_E164}\">{PHONE}</a>",
        hero_btns="", body=body, proof=False, cta=False,
    )


def thank_you():
    body = section(split(
        prose("<h2>What happens next</h2>",
              steps([("Shane reads your request", "It comes straight to the shop’s email."),
                     ("You get a price", "By text or call during shop hours."),
                     ("Pick a day", "Most tint jobs and details are done the same day.")]),
              f'Need an answer sooner? Call or text <a href="tel:{PHONE_E164}">{PHONE}</a>.'),
        f'<h2>Shop hours</h2>{hours_dl()}<p><a href="{MAPS_URL}" rel="noopener">{ADDRESS_LINE}</a></p>',
        "split-top"))
    return dict(slug="thank-you", group="Company", crumb="Thank you", title="Thanks for your request | 502 Tinted",
                desc="Your quote request was sent to 502 Tinted. Shane will text or call you back during shop hours.",
                h1="Thanks, your request is in",
                lede="Shane will text or call you back during shop hours with a price.",
                hero_btns=btns(("Back to the home page", "@home"), call=True), body=body, noindex=True, proof=False, cta=False)


def not_found():
    body = section(f'''<div class="lost">{num("404")}
<h1>We can’t find that page</h1>
<p class="lede">It may have moved. These are the pages people look for most:</p>
<ul class="link-list" style="margin-top:28px">
<li><a href="@car-window-tint-louisville">Car window tint</a></li>
<li><a href="@ceramic-window-tint-louisville">Ceramic tint</a></li>
<li><a href="@auto-detailing-louisville">Detailing menu</a></li>
<li><a href="@kentucky-tint-laws">Kentucky tint law</a></li>
<li><a href="@window-tint-cost-louisville">Tint prices</a></li>
<li><a href="@get-a-quote">Get a quote</a></li>
</ul></div>''')
    return dict(slug="404", group="Company", crumb="Page not found", title="Page not found | 502 Tinted",
                desc="This page doesn’t exist. Find window tint, detailing and Kentucky tint law pages at 502 Tinted.",
                h1="Page not found", lede="", body=body, noindex=True, proof=False,
                hero_btns="", hero=" ")


def pages():
    return [about(), reviews(), faq_hub(), contact(), quote(), thank_you(), not_found()]
