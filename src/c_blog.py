from kit import *

DATE = "2026-10-21"
KRS_URL = "https://law.justia.com/codes/kentucky/chapter-189/section-189-110"
ACT_URL = "https://apps.legislature.ky.gov/law/acts/24RS/documents/0017.pdf"


def meta():
    return f'<p class="post-meta">By {OWNER}, owner of 502 Tinted · Updated October 21, 2026</p>'


def windshield_post():
    body = section(prose(
        answer("Partly. Kentucky has always allowed a tinted strip across the top of the windshield, above the AS-1 line. Since July 15, 2024, "
               "it also allows film on the whole windshield if the windshield with the film still transmits at least 70% of visible light and "
               "the film isn’t red or yellow (KRS 189.110(2)). The 70% is measured with the windshield glass, not the film alone."),
        "<h2>What changed in 2024</h2>",
        "Before 2024, Kentucky allowed only a strip at the top of the windshield. Senate Bill 46 changed that. It was signed in March 2024 "
        "and took effect on July 15, 2024. It added a second option: sunscreening material applied to the windshield, when used together "
        "with the windshield’s safety glass, is legal if it has light transmission of at least 70% and isn’t red or yellow.",
        "That one phrase, “in conjunction with the safety glazing materials of the windshield,” is the part people miss. For the side "
        "windows, Kentucky rates the film by itself on clear glass. For the windshield, the film and the glass are judged together.",
        "<h2>Glass and film together</h2>",
        "A windshield on its own doesn’t let all the light through. Many new windshields transmit somewhere around 75–88%, and acoustic or "
        "solar windshields can be lower. Add a film and the two multiply, so the windshield reads lower than the film’s own rating.",
        "<h2>The sun strip</h2>",
        "A strip across the top of the windshield is allowed on any car, as long as it stays above the AS-1 line. You can find that line yourself: "
        "look along the side edges of the windshield for a small “AS-1” marking, usually near the top. The strip has to end at or above it.",
        "A strip is cheap, quick, and it takes care of the worst glare, the sun sitting just above the road on a morning or evening drive.",
        "<h2>Windshield film at 502 Tinted</h2>",
        f"We install sun strips ({P('tint_strip')}) and clear ceramic heat film for the whole windshield (from {P('tint_windshield')}). "
        "The strip cuts glare; the full film cuts heat and UV through the biggest piece of glass in the car. Both are trimmed around the "
        "mirror mount, cameras and rain sensor.",
        '<a href="@windshield-tint-louisville">Windshield tint at 502 Tinted</a> · <a href="@kentucky-tint-laws">The full Kentucky tint law</a>',
        "<h3>Sources</h3>",
        f'<ul><li><a href="{KRS_URL}" rel="noopener">KRS 189.110 (2024)</a></li><li><a href="{ACT_URL}" rel="noopener">2024 Ky. Acts ch. 17 (SB 46)</a></li></ul>',
        '<p class="note">This is a plain-language explanation, not legal advice.</p>'))
    faqs = [
        ("Can I tint my whole windshield in Kentucky?",
         "Yes, since July 15, 2024, if the windshield with the film still lets through at least 70% of light and the film isn’t red or yellow."),
        ("Is the 70% measured with the windshield glass?",
         "Yes. For the windshield, Kentucky judges the film together with the windshield’s glass, unlike the side windows, where the film is rated on its own."),
        ("Where is the AS-1 line?",
         "Look for a small AS-1 marking on the side edges of the windshield near the top. A tint strip must stay above it."),
    ]
    return dict(
        slug="is-windshield-tint-legal-in-kentucky", group="Guides", crumb="Is Windshield Tint Legal in Kentucky?",
        crumbs=[("Guides", "blog")],
        title="Is Windshield Tint Legal in Kentucky? (2026 Guide)",
        desc="Kentucky’s 2024 windshield tint change explained: the AS-1 sun strip, the 70% rule measured with the glass, why most 70% films fail, and what to ask a shop.",
        h1="Is windshield tint legal in Kentucky?",
        lede="Yes, with conditions. The 2024 change allows full-windshield film, but the 70% rule is tighter than it sounds.",
        hero_btns=meta(), proof=False, body=body, faqs=faqs, article={"date": DATE},
    )


def ir_vs_plus_post():
    body = section(prose(
        answer(f"For most daily drivers, HITEK Ceramic IR ({P('tint_ir')} and up for a car) is enough. Pick Ceramic Plus ({P('tint_plus')} and up) "
               "if your car sits in the sun all day, has a black interior, carries kids in the back in summer, or is a work vehicle. HITEK rates "
               "Ceramic Plus at 90% infrared and 69% total solar energy rejection, and Ceramic IR at 75% and 65%."),
        "<h2>The short version</h2>",
        "Both films are ceramic, neither interferes with your phone, and both carry HITEK’s lifetime guarantee. The difference is how "
        "much heat they stop: HITEK rates Ceramic IR at 75% infrared rejection and Ceramic Plus at 90%. That matters because Kentucky caps "
        "the front doors at 35%, so the film has to do the work, not the darkness.",
        film_cards(),
        "<h2>Six drivers, six answers</h2>",
        "<h3>The commuter with a garage</h3>",
        "Car sleeps inside, drives 20 minutes each way. Ceramic IR. You’ll feel the difference on the drive home and the extra heat "
        "rejection of Plus would mostly go unused.",
        "<h3>The shift worker</h3>",
        "Car sits in a UPS, Ford or warehouse lot for ten hours. Ceramic Plus. The longer a car bakes, the more the extra infrared rejection matters.",
        "<h3>The parent</h3>",
        "Kids in the back, summer camp pickups, a big back glass on an SUV. Ceramic Plus behind the driver at least. If the SUV is labeled MPV, "
        "Kentucky allows down to 8% back there, and every shade blocks 99% of UV.",
        "<h3>The work truck</h3>",
        "Parked at job sites all day, windows down a lot. Ceramic Plus on the front doors, where the 35% limit means heat rejection has to "
        "come from the film, and Ceramic IR in back is a smart split.",
        "<h3>The lease</h3>",
        "Turning it in within three years. Ceramic IR. Good comfort, good price, and it looks clean when it goes back.",
        "<h3>The black interior</h3>",
        "Black leather and a dark dash soak up heat. Ceramic Plus. This is the car where the difference is easiest to feel with your hand.",
        "<h2>What the extra cost works out to</h2>",
        f"Ceramic Plus starts ${PRICES['tint_plus'] - PRICES['tint_ir']} more than Ceramic IR on a car. "
        f"Keep the car five years and that’s about ${(PRICES['tint_plus'] - PRICES['tint_ir']) / 5:.0f} a year, or roughly "
        f"${(PRICES['tint_plus'] - PRICES['tint_ir']) / 60:.2f} a month. For a car that lives outside, that’s an easy call. For a garage-kept "
        "commuter, the money might be better spent on a detail.",
        "<h2>You can mix them</h2>",
        "Some customers put Ceramic Plus on the front doors and Ceramic IR on the rest. The fronts are where the driver sits and where Kentucky "
        "limits the shade, so that’s where the stronger film earns the most. Ask and we’ll price it.",
        '<a href="@ceramic-window-tint-louisville">Full specs for both films</a> · <a href="@window-tint-cost-louisville">Tint prices</a>'))
    faqs = [
        ("Is HITEK Ceramic Plus better than Ceramic IR?",
         "It blocks more heat: HITEK rates Ceramic Plus at 90% infrared and 69% total solar energy rejection, and Ceramic IR at 75% and 65%. Both are ceramic with a lifetime guarantee."),
        ("Is Ceramic Plus worth the extra money?",
         "For cars that sit in the sun all day, dark interiors and work vehicles, usually yes. For garage-kept commuters, Ceramic IR is often enough."),
        ("Can I put different films on different windows?",
         "Yes. Ceramic Plus on the front doors and Ceramic IR in back is a common split."),
    ]
    return dict(
        slug="hitek-ceramic-ir-vs-ceramic-plus", group="Guides", crumb="Ceramic IR vs Ceramic Plus", crumbs=[("Guides", "blog")],
        title="HITEK Ceramic IR vs Ceramic Plus: Which to Choose",
        desc="HITEK Ceramic IR or Ceramic Plus? A decision guide for Louisville drivers: commuters, parents, shift workers, work trucks, leases and black interiors.",
        h1="HITEK Ceramic IR vs Ceramic Plus: which should you get?",
        lede="Both are good ceramic films. The right one depends on where your car sits and who rides in it.",
        hero_btns=meta(), proof=False, body=body, faqs=faqs, article={"date": DATE},
    )


def cure_post():
    body = section(prose(
        answer("Window tint usually needs three to five days to cure in Louisville, and up to a week or more in cold, damp winter weather. "
               "In hot, dry summer weather it can be closer to two or three days. Keep the windows rolled up during that time. Haze and small "
               "water pockets while it cures are normal and go away on their own."),
        "<h2>Why tint needs to cure</h2>",
        "Film goes on with a slip solution so it can be positioned and squeegeed tight. A thin layer of that moisture stays behind the film "
        "and has to evaporate through it. Until it does, the adhesive hasn’t fully bonded, and rolling the window down can catch the edge and peel it.",
        "<h2>Louisville weather, season by season</h2>",
        table(["Season", "Typical cure time", "Why"],
              [["Summer", "2–3 days", "Heat and sun drive the moisture out fast"],
               ["Spring and fall", "3–5 days", "Mild days, cool nights and rain slow it down"],
               ["Winter", "5–10 days", "Cold and damp air keep moisture in the film longer"]],
              note="Parking in the sun helps. A garage in winter slows it down. Ceramic film cures the same way other films do."),
        "<h2>What’s normal in the first week</h2>",
        ticks(["A hazy or cloudy look, especially in the morning",
               "Small water pockets or blisters that shrink day by day",
               "A slight streaky look at certain angles while it dries"]),
        "<h2>What isn’t normal</h2>",
        ticks(["Bubbles that are still there after two weeks",
               "Specks of dirt or hair trapped under the film",
               "An edge that lifts or peels",
               "A gap at the top edge of a side window that you weren’t told about"]),
        f"If you see any of those, text a photo to {PHONE} and bring it back. That’s what the follow-up is for.",
        "<h2>Taking care of new tint</h2>",
        ticks(["Keep the windows up for three to five days, longer in winter",
               "Don’t clean the inside of the glass for the first week",
               "After that, use an ammonia-free glass cleaner and a soft microfiber towel",
               "Be careful with seat belt buckles, rings and ice scrapers on the inside of the glass",
               "The rear defroster is safe to use once the film has cured"]),
        f'<a href="@car-window-tint-louisville">Car window tint at 502 Tinted</a> · <a href="@get-a-quote">Get a quote</a>'))
    faqs = [
        ("How long before I can roll down my windows after tint?",
         "Three to five days in most Louisville weather, and up to a week or more in a cold, damp winter."),
        ("Is it normal for new tint to look hazy?",
         "Yes. Haze and small water pockets are normal while the film cures and fade over several days."),
        ("Can I wash my car after getting tint?",
         "Yes, the outside. Wait a week before cleaning the inside of the tinted glass, then use an ammonia-free cleaner."),
    ]
    return dict(
        slug="window-tint-cure-time-louisville", group="Guides", crumb="Tint Cure Time", crumbs=[("Guides", "blog")],
        title="How Long Does Window Tint Take to Cure in Louisville?",
        desc="Window tint cure time in Louisville by season: 2–3 days in summer, 3–5 in spring and fall, up to 10 in winter. What’s normal and how to care for new tint.",
        h1="How long does window tint take to cure in Louisville?",
        lede="Three to five days most of the year, longer in winter. Here’s what’s normal, what isn’t, and how to take care of new film.",
        hero_btns=meta(), proof=False, body=body, faqs=faqs, article={"date": DATE},
    )


POSTS = [windshield_post, ir_vs_plus_post, cure_post]


def hub(posts):
    lis = "".join(f'<li><h2><a href="@{p["slug"]}">{esc(p["h1"])}</a></h2><p>{esc(p["desc"])}</p></li>' for p in posts)
    body = section(f'<ul class="post-list">{lis}</ul>')
    return dict(
        slug="blog", group="Guides", crumb="Guides",
        title="Window Tint & Detailing Guides | 502 Tinted Louisville",
        desc="Plain-English guides on Kentucky tint law, windshield tint, HITEK ceramic films and tint care from 502 Tinted in Louisville.",
        h1="Guides", lede="Plain answers to the questions we get at the shop.",
        body=body, proof=False,
    )


def pages():
    posts = [f() for f in POSTS]
    return [hub(posts)] + posts
