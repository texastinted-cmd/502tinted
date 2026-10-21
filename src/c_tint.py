from kit import *

KRS_URL = "https://law.justia.com/codes/kentucky/chapter-189/section-189-110"
ACT_URL = "https://apps.legislature.ky.gov/law/acts/24RS/documents/0017.pdf"
HITEK_IR = "https://hitekfilms.com/product/ceramic-ir/"
HITEK_PLUS = "https://hitekfilms.com/product/ceramic-plus/"

SHADE_TABLE = table(
    ["Film shade", "How it looks", "Front doors", "Behind the driver: car or truck", "Behind the driver: SUV or van (MPV)"],
    [["70%", "Nearly clear. Heat control without a tinted look.", "Legal", "Legal", "Legal"],
     ["50%", "Light smoke. Looks factory on most cars.", "Legal", "Legal", "Legal"],
     ["35%", "Medium. The darkest you can go up front.", "Legal", "Legal", "Legal"],
     ["20%", "Dark. Hard to see in during the day.", "Too dark", "Legal", "Legal"],
     ["15%", "Darker. Matches many factory privacy glass packages.", "Too dark", "Too dark", "Legal"],
     ["5%", "Limo. Very hard to see out of at night.", "Too dark", "Too dark", "Too dark"]],
    caption="Kentucky shades by window (KRS 189.110, film rated on clear glass, 3% tolerance)")


def car():
    body = section(
        answer(f"Car window tint at 502 Tinted starts at {P('tint_ir')} for a car’s side windows and back glass in HITEK Ceramic IR, "
               f"and {P('tint_plus')} in HITEK Ceramic Plus. Kentucky limits front side windows to 35% and windows behind the driver to 18%, "
               "or 8% on SUVs and vans. Most cars take two to four hours at our shop on Valley Station Road in Louisville.")
        + split(prose(
            "<h2>What tint actually does for a Louisville car</h2>",
            "Louisville summers are hot and sticky, and a car parked through a shift at UPS or the Ford plant, or "
            "all afternoon at Jefferson Mall, is miserable by the time you get back to it. Ceramic film blocks a large share of the infrared heat coming through "
            "the glass, so the cabin heats up slower and the A/C catches up faster.",
            "It also blocks 99% of UV, which is what fades dashboards, cracks leather and burns the arm you rest on the door. "
            "It cuts glare from the low sun on the Gene Snyder and I-65 in the morning and evening. It gives you some privacy "
            "for what’s on the back seat. And it makes the car look finished.",
            "Every job here uses HITEK ceramic film with a lifetime guarantee."),
            photo("tint-hero")))
    body += section(split(
        f'<h2>Car tint prices</h2>{price_list(TINT_MENU[:3])}'
        '<p class="pl-note">Starting prices for sedans and coupes. SUVs, trucks and vans have more glass and are priced by window count. '
        'Old film? Removal is quoted separately.</p>',
        prose("<h3>What’s included</h3>",
              ticks(["Side windows and the back glass, cut for your exact car",
                     "Back glass heat-shrunk in one piece, so there are no seams across the defroster lines",
                     "Edges filed and checked in daylight before you leave",
                     "HITEK lifetime film warranty"]),
              f'Want the front doors only, to match factory rear privacy glass? That starts at {P("tint_front2")}.'),
        "split-top"), "band-raised")
    body += section(
        '<div class="band-head"><h2>Picking a shade</h2><p>Kentucky rates the film on its own, so the factory tint in your glass doesn’t count against you. '
        'This is what each shade looks like and where it’s allowed.</p></div>' + SHADE_TABLE
        + '<p class="table-note">Your door-jamb label says MPV if your SUV or van qualifies for the 8% limit behind the driver. Pickups are labeled TRUCK and follow the 18% rule. '
          '<a href="@kentucky-tint-laws">The full Kentucky tint law</a></p>')
    body += section(
        '<h2>How a tint appointment works</h2>'
        + steps([
            ("Book a time", f"Call or text {PHONE}, or send the quote form. Tell us the year, make and model, and whether there’s old film on the glass."),
            ("Drop off", "We look over the glass for chips, old adhesive and dirty seals, then clean every window inside and out."),
            ("Cut and shape", "Film is cut to your glass. The back glass is heat-shrunk so one piece follows the curve."),
            ("Install", "The film goes on the inside of the glass with a slip solution, then it’s squeegeed tight and the edges are finished."),
            ("Final check", "Every edge is checked in daylight, and you get the film, shade and care instructions on your paperwork."),
            ("Pick up and cure", "Keep the windows up for three to five days while the film cures. Some haze or small water pockets in that time is normal."),
        ]), "band-raised")
    body += section(split(
        prose("<h2>Why we only install ceramic</h2>",
              "Bargain film looks fine for a year or two, then turns purple, bubbles and has to be scraped off. Metal-based films hold up "
              "better but can interfere with phone, GPS and key fob signals. Ceramic film uses non-metal particles to block heat, so it "
              "stays the same color and doesn’t block signals.",
              "Because Kentucky caps the front doors at 35%, you can’t make the car cooler just by going darker up front. The heat "
              "rejection has to come from the film itself, which is why ceramic is the only kind we put on.",
              '<a href="@ceramic-window-tint-louisville">Compare HITEK Ceramic IR and Ceramic Plus</a>'),
        photo("tint-install")))
    faqs = [
        ("How long does car window tint take?",
         "Two to four hours for most cars. Removing old film adds time. Most customers drop off in the morning and pick up the same afternoon."),
        ("When can I roll my windows down?",
         "Wait three to five days. In cool, damp weather give it the full five. The film needs time for the slip solution to dry out behind it."),
        ("Is it normal to see haze or little bubbles after tinting?",
         "Yes, for the first several days. Those are pockets of water that evaporate as the film cures. If anything is still there after two weeks, bring it back and we’ll look."),
        ("Can I get my front doors to match my factory rear glass?",
         f"Yes. Front two doors start at {P('tint_front2')}. Factory privacy glass is dark glass, not film, so we pick a front shade that looks close."),
        ("Will tint affect my phone, GPS or key fob?",
         "Not with ceramic film. It has no metal layer, so signals pass through normally."),
        ("Do you tint trucks and SUVs?",
         "Yes. They have more glass, so they’re priced by window count. SUVs and vans labeled MPV can go darker behind the driver than cars."),
    ]
    return dict(
        slug="car-window-tint-louisville", group="Window tint", crumb="Car Window Tint",
        title=f"Car Window Tint Louisville, KY | From {P('tint_ir')} | 502 Tinted",
        desc=f"Ceramic car window tint in Louisville from {P('tint_ir')}. HITEK Ceramic IR and Ceramic Plus, lifetime guarantee, most cars same day. Valley Station shop.",
        h1="Car window tint in Louisville",
        lede="HITEK ceramic film on your side windows and back glass, cut for your car and installed at our Valley Station shop. Most cars are done the same day.",
        hero_side=pcard("Full car, Ceramic IR, from", "tint_ir", "Sedans and coupes. Side windows and back glass.",
                        ["99% UV blocked", "Cut for your exact car", "HITEK lifetime guarantee"],
                        second=("Full car, Ceramic Plus, from", "tint_plus")),
        body=body, faqs=faqs,
        service=dict(name="Car window tint", type="Automotive window tinting", brands=["HITEK"], offers=PRICES["tint_ir"],
                     alt=["Auto window tint Louisville", "Car tinting Louisville KY", "Window tinting near me"]),
    )


def ceramic():
    spec = table(
        ["", "HITEK Ceramic IR", "HITEK Ceramic Plus"],
        [["Total solar energy rejected (TSER)", "65%", "69%"],
         ["Infrared rejected (IRR)", "75%", "90%"],
         ["How HITEK describes it", "Entry-level ceramic with carbon-based technology", "True nano ceramic and IR coating technology"],
         ["UV blocked", "Up to 99%", "99%"],
         ["Shades made", "2, 5, 15, 20, 30, 35, 40, 45, 50, 70%", "5, 15, 20, 30, 35, 50, 70%"],
         ["Guarantee", "Lifetime, from HITEK", "Lifetime, from HITEK"],
         ["Car price at 502 Tinted", f"from {P('tint_ir')}", f"from {P('tint_plus')}"]],
        caption="HITEK’s headline numbers, measured at the darkest shade",
        note=f'Sources: HITEK’s spec cards and its <a href="{HITEK_IR}" rel="noopener">Ceramic IR</a> and <a href="{HITEK_PLUS}" rel="noopener">Ceramic Plus</a> pages. '
             "Ceramic Plus numbers are for HITEK’s dyed version, the one we install. They’re lab figures; your car’s glass changes the totals a little.")
    plus_rows = table(
        ["Ceramic Plus shade", "Light through (VLT)", "Solar energy rejected", "IR rejected", "Glare cut"],
        [["50", "50%", "56%", "90%", "45%"], ["35", "36%", "60%", "90%", "60%"],
         ["20", "20%", "65%", "90%", "78%"], ["5", "6%", "69%", "90%", "93%"]],
        caption="HITEK Ceramic Plus (dyed version) by shade",
        note="The 35% shade, the darkest legal front-door shade in Kentucky, still rejects 60% of solar energy. HITEK doesn’t publish this table for the 15% and 70% shades.")
    body = section(
        answer(f"Ceramic window tint uses non-metal ceramic technology to block infrared heat, so it keeps a car cooler without blocking phone "
               f"and GPS signals. 502 Tinted installs two HITEK ceramics: Ceramic IR (from {P('tint_ir')} for a car), rated 65% total solar "
               f"energy rejection and 75% infrared rejection, and Ceramic Plus (from {P('tint_plus')}), rated 69% and 90%. Both carry HITEK’s lifetime guarantee.")
        + '<h2>Ceramic IR and Ceramic Plus side by side</h2>' + film_cards(link=False) + '<div style="margin-top:28px">' + spec + '</div>')
    body += section(split(
        prose("<h2>Why heat rejection matters more than darkness in Kentucky</h2>",
              "The heat you feel on your arm through the glass is mostly infrared, not visible light. A dark basic film blocks light "
              "but lets plenty of infrared through, which is why a car with cheap limo tint can still be an oven.",
              "Kentucky’s front-door limit is 35%, so you can’t go darker up front to fight the heat. You need a film that blocks infrared "
              "at that shade. That’s the whole point of ceramic: a 35% Ceramic Plus front window rejects more solar energy than many "
              "dark non-ceramic films.",
              "It works the other way too. If you want a lighter look, a 50% or even 70% ceramic still cuts a noticeable amount of heat."),
        photo("ceramic-compare")), "band-raised")
    body += section(
        '<div class="band-head"><h2>Ceramic Plus, shade by shade</h2></div>' + plus_rows)
    body += section(
        '<h2>Which one should you get?</h2>'
        + rows([
            ("Pick Ceramic IR if…", "You want real heat and UV protection at a fair price, your car is a daily commuter, or it’s a lease you’ll turn in. "
                                     "It’s the film most of our customers choose."),
            ("Pick Ceramic Plus if…", "Your car sits outside all day, you have a black interior or a big back glass, you drive for work, or you have "
                                       "kids in the back seat in July. The extra infrared rejection is noticeable on hot days."),
            ("Mixing is fine", "Some customers put Ceramic Plus on the front doors, where the 35% limit makes heat rejection matter most, and "
                               "Ceramic IR in back. Ask and we’ll price it."),
            ("Not sure?", f"Text {PHONE} with your vehicle and how you use it, and Shane will tell you which one makes sense. No upsell needed."),
        ]), "band-raised")
    body += section(prose(
        "<h2>Ceramic vs basic dyed vs carbon tint</h2>",
        "<strong>Basic dyed film</strong> is the cheapest. Dye darkens the glass, nothing in it stops much infrared heat, and it fades "
        "toward purple over a few years in the sun.",
        "<strong>Carbon film</strong> uses carbon particles for color. It holds up better than basic dyed film and blocks more heat, "
        "but less than ceramic.",
        "<strong>Ceramic film</strong> adds ceramic technology that’s especially good at blocking infrared. HITEK builds Ceramic IR on "
        "carbon-based technology, and Ceramic Plus on a nano ceramic and IR coating. Both carry HITEK’s lifetime guarantee, which is "
        "why ceramic is all we install.",
        '<a href="@hitek-window-film-louisville">More about HITEK films</a>'))
    faqs = [
        ("Is ceramic tint worth it in Louisville?",
         "For most drivers, yes. Summers here are hot and humid, the front doors can’t be darker than 35%, and ceramic is what blocks the heat without going darker."),
        ("What’s the difference between HITEK Ceramic IR and Ceramic Plus?",
         "Both are ceramic. HITEK rates Ceramic IR at 65% total solar energy rejection and 75% infrared rejection, and Ceramic Plus at 69% and 90%. Ceramic Plus costs more and blocks more heat."),
        ("Does ceramic tint block phone signal?",
         "No. Ceramic film has no metal layer, so phone, GPS, radio and key fob signals pass through normally."),
        ("Does a lighter ceramic film still block heat?",
         "Yes. HITEK rates Ceramic Plus at its light 50% shade at 56% total solar energy rejection and 90% infrared rejection."),
        ("How long does ceramic tint last?",
         "The life of the car, under normal use. Both films carry HITEK’s lifetime guarantee."),
    ]
    return dict(
        slug="ceramic-window-tint-louisville", group="Window tint", crumb="Ceramic Tint", crumbs=[("Car Window Tint", "car-window-tint-louisville")],
        title="Ceramic Window Tint Louisville | HITEK IR vs Plus",
        desc=f"HITEK Ceramic IR vs Ceramic Plus window tint in Louisville: heat rejection, shades, prices from {P('tint_ir')} and {P('tint_plus')}, and which one fits how you drive.",
        h1="Ceramic window tint in Louisville",
        lede="Two HITEK ceramic films with a lifetime guarantee. Here’s the real difference between them and how to pick.",
        hero_side=pcard("HITEK Ceramic IR, full car, from", "tint_ir", "Sedans and coupes. SUVs and trucks priced by window count.",
                        ["No metal layer, no signal problems", "Light to dark shades", "Lifetime guarantee from HITEK"],
                        second=("HITEK Ceramic Plus, full car, from", "tint_plus")),
        body=body, faqs=faqs,
        service=dict(name="Ceramic window tint", type="Automotive window tinting", brands=["HITEK"], offers=PRICES["tint_ir"],
                     alt=["HITEK Ceramic IR", "HITEK Ceramic Plus", "Nano ceramic tint Louisville"]),
    )


def windshield():
    body = section(
        answer(f"502 Tinted installs two kinds of windshield film in Louisville: a sun strip across the top of the windshield ({P('tint_strip')}) "
               f"and clear ceramic heat film on the whole windshield (from {P('tint_windshield')}). The strip cuts glare from low sun; the full "
               "film blocks heat and 99% of UV through the biggest piece of glass in the car. Both are trimmed around the mirror mount, cameras and sensors.")
        + split(prose(
            "<h2>The sun strip</h2>",
            "The quick, simple option. A band of film across the top of the windshield, ending at the AS-1 line, the small marking "
            "on the edge of the glass near the top. On most cars the strip ends up five to six inches deep.",
            "It takes the edge off the sun when it sits low over the road, which is most of the morning and evening commute on the Gene Snyder, "
            "I-264 and the Outer Loop. We cut around the rearview mirror mount and any lane-camera or rain-sensor housing so nothing "
            "your car relies on is covered.",
            f"A sun strip is {P('tint_strip')}, or add it to a full tint job."),
            price_list([("tint_strip", "Windshield sun strip", "Down to the AS-1 line"),
                        ("tint_windshield", "Full windshield heat film", "Clear ceramic film on the whole windshield"),
                        ("tint_ir", "Add the side windows", "Full car, HITEK Ceramic IR")]), "split-top"))
    body += section(split(
        prose("<h2>Full windshield ceramic heat film</h2>",
              "The windshield is the biggest piece of glass in the car, and it faces the sun most of the day. A clear ceramic film on the "
              "inside blocks infrared heat and 99% of UV without turning the windshield dark, so the dash, the steering wheel and your arms "
              "stay cooler.",
              "It’s the upgrade people notice most on a July drive, and it pairs well with ceramic tint on the side windows.",
              ticks(["Less heat coming through the front of the car",
                     "Less fading and cracking on the dash",
                     "UV protection for your face and arms",
                     "Trimmed around the mirror mount, cameras and rain sensor"])),
        photo("windshield")), "band-raised")
    body += section(
        '<h2>How a windshield install works</h2>'
        + steps([
            ("Clean the glass", "The inside of the windshield is cleaned edge to edge, including the corners under the dash."),
            ("Shape the film", "Windshields curve in two directions, so the film is heat-shrunk on the outside of the glass to match before it goes on."),
            ("Install and trim", "The film goes on the inside and is trimmed around the mirror mount, cameras and rain sensor."),
            ("Check it in daylight", "Edges and clarity are checked before you pick up. Some haze while the film cures is normal."),
        ]))
    body += section(prose(
        "<h2>What Kentucky law says about windshields</h2>",
        "Kentucky allows a transparent strip at the top of the windshield above the AS-1 line. Since July 15, 2024, it also allows film on "
        "the whole windshield when, used together with the windshield’s glass, it lets through at least 70% of visible light and isn’t red "
        "or yellow. Windshield glass already blocks some light on its own, so the reading with film on is lower than the film’s rating.",
        '<a href="@kentucky-tint-laws">The whole Kentucky tint law</a> · <a href="@is-windshield-tint-legal-in-kentucky">Our guide to windshield tint in Kentucky</a>'),
        "band-raised")
    faqs = [
        ("How much is windshield tint?",
         f"A sun strip is {P('tint_strip')}. Clear ceramic heat film on the whole windshield starts at {P('tint_windshield')}."),
        ("Does windshield film block heat?",
         "Yes. Clear ceramic film blocks infrared heat and 99% of UV while staying light enough to see through."),
        ("Will windshield film cover my lane camera?",
         "No. We trim the strip or the full film around the mirror mount, cameras and rain sensor."),
        ("What is the AS-1 line?",
         "A marking on the edge of the windshield, set by federal standards, that shows the top of the driver’s direct view. Tint strips stop at it."),
        ("Is windshield tint legal in Kentucky?",
         "A transparent strip above the AS-1 line is allowed. Since July 15, 2024, film on the whole windshield is allowed too when the windshield with the film lets through at least 70% of light and the film isn’t red or yellow."),
    ]
    return dict(
        slug="windshield-tint-louisville", group="Window tint", crumb="Windshield Tint", crumbs=[("Car Window Tint", "car-window-tint-louisville")],
        title="Windshield Tint Louisville, KY | Strips & Heat Film",
        desc=f"Windshield tint in Louisville: sun strips for {P('tint_strip')} and clear ceramic heat film for the whole windshield from {P('tint_windshield')}. Trimmed around sensors.",
        h1="Windshield tint in Louisville",
        lede="A sun strip to cut the glare, or clear ceramic heat film on the whole windshield to cut the heat.",
        hero_side=pcard("Windshield sun strip", "tint_strip", "Down to the AS-1 line, trimmed around sensors.",
                        ["Cuts low-sun glare", "Trimmed around cameras and sensors", "Quick add-on to a tint job"],
                        second=("Full windshield heat film, from", "tint_windshield")),
        body=body, faqs=faqs,
        service=dict(name="Windshield tint", type="Windshield sun strip and windshield heat film", brands=["HITEK"], offers=PRICES["tint_strip"],
                     alt=["Windshield sun strip Louisville", "Windshield visor strip", "Clear windshield heat film", "Ceramic windshield film"]),
    )


def removal():
    body = section(
        answer(f"Window tint removal at 502 Tinted starts at {P('tint_removal')}. We take off the old film, clean every bit of adhesive off the "
               "glass, and protect the rear defroster lines on the back glass. Most removals take one to two hours, and you can get new "
               "HITEK ceramic tint installed the same visit.")
        + split(prose(
            "<h2>When old tint needs to come off</h2>",
            ticks(["<strong>It turned purple.</strong> That’s cheap film breaking down in the sun. It won’t go back.",
                   "<strong>It’s bubbling or peeling.</strong> The adhesive has failed, and the bubbles will keep growing.",
                   "<strong>You want a different shade.</strong> Lighter, darker, or the fronts matched to the back.",
                   "<strong>It was installed badly.</strong> Dirt under the film, gaps at the top edge, or seams across the back glass.",
                   "<strong>You want better film.</strong> Swapping old film for ceramic is the biggest comfort upgrade you can make to the glass."])),
            photo("removal"), "split-top"))
    body += section(
        '<h2>How we remove it without damaging anything</h2>'
        + steps([
            ("Steam and peel", "We heat the film so it lets go in large sheets instead of tearing into flakes."),
            ("Dissolve the glue", "Adhesive left on the glass is softened and wiped off, not ground off."),
            ("Protect the defroster", "On the back glass we never take a razor to the inside. Those thin lines are the rear defroster, and they scratch easily."),
            ("Clean and inspect", "The glass is cleaned and checked, and any existing defroster damage is pointed out before anything new goes on."),
        ]) + '<p class="note" style="margin-top:24px">Back glass is where most of the time goes. Old, baked-on film can take longer than a side window by a wide margin.</p>',
        "band-raised")
    body += section(split(
        prose("<h2>What changes the price</h2>",
              ticks(["How many windows have film on them",
                     "How old and brittle the film is: fresh film peels, ten-year-old film flakes",
                     "Whether the adhesive stays on the glass",
                     "Back glass size and curve"]),
              f"Removal starts at {P('tint_removal')}. Text a photo of the glass to {PHONE} and we can give you a close number before you come in."),
        prose("<h2>Retint the same day</h2>",
              f"Most customers have the new film put on right after removal. Ceramic IR starts at {P('tint_ir')} for a car, and "
              f"Ceramic Plus at {P('tint_plus')}, both with HITEK’s lifetime guarantee.",
              '<a href="@car-window-tint-louisville">Car window tint</a> · <a href="@ceramic-window-tint-louisville">Ceramic IR vs Ceramic Plus</a>'),
        "split-top"))
    faqs = [
        ("How much does tint removal cost in Louisville?",
         f"At 502 Tinted, removal starts at {P('tint_removal')}. Old, brittle film and big back glass take longer and cost more. Text a photo for a closer quote."),
        ("Will removing tint damage my rear defroster?",
         "Not when it’s done right. We steam the film off and dissolve the glue instead of scraping the inside of the back glass."),
        ("Can I remove window tint myself?",
         "Side windows, often yes, with heat and patience. The back glass is where people damage defroster lines. If the film is old and flaking, it’s usually worth having it done."),
        ("How long does tint removal take?",
         "One to two hours for most cars. The back glass takes the longest, especially with old, baked-on film."),
        ("Can you remove tint and retint on the same day?",
         "Yes. That’s how most removals are booked."),
    ]
    return dict(
        slug="tint-removal-louisville", group="Window tint", crumb="Tint Removal", crumbs=[("Car Window Tint", "car-window-tint-louisville")],
        title=f"Window Tint Removal Louisville, KY | From {P('tint_removal')} | 502 Tinted",
        desc=f"Purple, bubbling or too-dark tint? Window tint removal in Louisville from {P('tint_removal')}, glue cleaned off, defroster lines protected. Retint same day.",
        h1="Window tint removal in Louisville",
        lede="Old film off, glue gone, defroster lines intact. Then new ceramic tint the same day if you want it.",
        hero_side=pcard("Tint removal, from", "tint_removal", "Price depends on window count and how old the film is.",
                        ["Steamed off, not scraped", "Rear defroster protected", "Retint in the same visit"]),
        body=body, faqs=faqs,
        service=dict(name="Window tint removal", type="Window film removal", offers=PRICES["tint_removal"],
                     alt=["Tint removal Louisville", "Purple tint removal", "Old window tint removal"]),
    )


def hitek():
    body = section(
        answer("502 Tinted is a HITEK window film dealer in Louisville, Kentucky. We install two HITEK ceramic films: Ceramic IR, rated 65% "
               "total solar energy rejection and 75% infrared rejection, and Ceramic Plus, rated 69% and 90%. Both block real heat at the "
               "lighter shades, and both carry HITEK’s lifetime guarantee.")
        + split(prose(
            "<h2>Why HITEK</h2>",
            "A tint job is only as good as the film and the person installing it. HITEK ceramic films go on clean and "
            "come with a lifetime guarantee that’s honored across the country, not just at one shop. That matters if you move, or if you’re "
            "stationed at Fort Knox and get orders.",
            "We picked two HITEK films that block real heat even at lighter shades, which matters in Kentucky, where the front doors top out at 35%."),
            photo("hitek-rolls")))
    body += section(
        '<div class="band-head"><h2>The two HITEK films we install</h2><p>Both are ceramic, both carry HITEK’s lifetime guarantee, and both come in light to dark shades.</p></div>'
        + film_cards(), "band-raised")
    body += section(split(
        prose("<h2>HITEK Ceramic IR</h2>",
              "HITEK’s entry-level ceramic, built on carbon-based technology, and the film most of our customers choose. HITEK rates it at "
              "65% total solar energy rejection and 75% infrared rejection (740–2500 nm, at the 5% shade), and it comes in more shades than "
              "any other HITEK line: 2, 5, 15, 20, 30, 35, 40, 45, 50 and 70%.",
              f"On a car, Ceramic IR starts at {P('tint_ir')} for the side windows and back glass.",
              f'<a href="{HITEK_IR}" rel="noopener">HITEK’s Ceramic IR page</a>'),
        prose("<h2>HITEK Ceramic Plus</h2>",
              "HITEK calls it true nano ceramic and IR coating technology. The version we install is rated 90% infrared rejection at every "
              "shade HITEK measures, with total solar energy rejection from 56% at the 50% shade to 69% at the darkest. HITEK backs it with a "
              "lifetime guarantee.",
              f"On a car, Ceramic Plus starts at {P('tint_plus')}.",
              f'<a href="{HITEK_PLUS}" rel="noopener">HITEK’s Ceramic Plus page</a>'),
        "split-top"))
    body += section(prose(
        "<h2>About the lifetime guarantee</h2>",
        "HITEK’s lifetime guarantee is honored nationwide, which means any authorized HITEK dealer can look at a warranty issue, "
        "not only the shop that installed it. Keep your paperwork; it lists the film, the shade and the install date.",
        "The warranty covers the film. Damage from scratches, scraping the glass, or a window regulator that grinds the film is not a "
        "film defect. If something looks wrong in the first couple of weeks, bring it back and Shane will take a look."),
        "band-raised")
    faqs = [
        ("Is 502 Tinted a HITEK dealer?",
         "Yes. We’re a HITEK window film dealer in Louisville and install HITEK Ceramic IR and Ceramic Plus."),
        ("Is HITEK good window film?",
         "The two HITEK ceramics we install are rated 75% (Ceramic IR) and 90% (Ceramic Plus) infrared rejection, and both carry a lifetime guarantee honored at HITEK dealers nationwide."),
        ("What warranty comes with HITEK tint?",
         "HITEK’s lifetime guarantee on the film, honored nationwide."),
        ("Which HITEK film should I get?",
         "Most daily drivers choose Ceramic IR. If your car sits in the sun all day, has a dark interior or is a work vehicle, Ceramic Plus blocks more heat."),
    ]
    return dict(
        slug="hitek-window-film-louisville", group="Window tint", crumb="HITEK Films", crumbs=[("Car Window Tint", "car-window-tint-louisville")],
        title="HITEK Window Film Dealer Louisville, KY | 502 Tinted",
        desc="502 Tinted is a HITEK window film dealer in Louisville, installing HITEK Ceramic IR and Ceramic Plus. Specs, shades, prices and the lifetime guarantee.",
        h1="HITEK window film in Louisville",
        lede="We’re a HITEK dealer and install two of its ceramic films: Ceramic IR and Ceramic Plus.",
        hero_side=pcard("HITEK Ceramic IR, full car, from", "tint_ir", "Side windows and back glass on a sedan or coupe.",
                        ["Ceramic, no metal layer", "Lifetime guarantee from HITEK", "Light to dark shades"],
                        second=("HITEK Ceramic Plus, full car, from", "tint_plus")),
        body=body, faqs=faqs,
        service=dict(name="HITEK window film installation", type="Automotive window tinting", brands=["HITEK"], offers=PRICES["tint_ir"],
                     alt=["HITEK dealer Louisville", "HITEK Ceramic IR", "HITEK Ceramic Plus"]),
    )


def cost():
    tbl = table(["Service", "Starting price", "What it covers"],
                [[esc(n), f"from {P(k)}", esc(sub)] for k, n, sub in TINT_MENU],
                caption="502 Tinted window tint prices, cars, October 2026",
                note="SUVs, trucks and vans have more windows and are priced by window count. Old film removal is quoted separately.")
    body = section(
        answer(f"Window tint in Louisville at 502 Tinted costs {P('tint_ir')} and up for a car’s side windows and back glass in HITEK Ceramic IR, "
               f"{P('tint_plus')} and up in Ceramic Plus, {P('tint_front2')} and up for the front two doors, {P('tint_strip')} for a windshield "
               f"sun strip and {P('tint_removal')} and up for removing old film. SUVs and trucks cost more because they have more glass.")
        + tbl)
    body += section(split(
        prose("<h2>What changes the price</h2>",
              ticks(["<strong>How much glass.</strong> A coupe has four side windows and a back glass. A three-row SUV can have ten pieces.",
                     "<strong>Which film.</strong> Ceramic Plus blocks more heat than Ceramic IR and costs more.",
                     "<strong>Old film.</strong> Steaming off old tint and cleaning the glue is extra work, especially on the back glass.",
                     "<strong>Tricky glass.</strong> Very curved back glass, split rear windows and small vent windows take more time.",
                     "<strong>The windshield.</strong> A sun strip is quick. Full windshield heat film takes longer."])),
        prose("<h2>Why the cheapest tint costs more</h2>",
              "A low-price tint job is almost always basic dyed film with no ceramic in it. It looks fine at first, then fades purple and bubbles within a few "
              "Kentucky summers. Then you pay for removal and for tint again.",
              "Ceramic costs more once and lasts the life of the car. Spread over the years you own it, it’s the cheaper choice."),
        "split-top"), "band-raised")
    body += section(split(
        prose("<h2>Getting an exact price</h2>",
              f"Send the quote form or text {PHONE} with your year, make and model, the film you’re leaning toward, and whether there’s old tint on the glass. "
              "Shane will reply with a price during shop hours.",
              "Booking a detail too? Tell us. Tint and detailing can be done in one visit."),
        price_list(TINT_MENU[:3]), "split-top"))
    faqs = [
        ("How much does it cost to tint a car in Louisville?",
         f"At 502 Tinted, {P('tint_ir')} and up for side windows and back glass with HITEK Ceramic IR, or {P('tint_plus')} and up with Ceramic Plus."),
        ("How much is it to tint just the front windows?",
         f"Front two doors start at {P('tint_front2')} in HITEK Ceramic IR."),
        ("Why does SUV tint cost more?",
         "More windows. Many SUVs and vans also have small vent windows that take time to fit."),
        ("Is ceramic tint worth the extra cost?",
         "Usually. It blocks much more heat than basic film, and it doesn’t need replacing in a few years."),
        ("Do you charge to remove old tint?",
         f"Yes, removal starts at {P('tint_removal')} and depends on the film’s age and how many windows have it."),
    ]
    return dict(
        slug="window-tint-cost-louisville", group="Window tint", crumb="Tint Prices", crumbs=[("Car Window Tint", "car-window-tint-louisville")],
        title="Window Tint Cost in Louisville (2026 Prices) | 502 Tinted",
        desc=f"Window tint prices in Louisville for 2026: car tint from {P('tint_ir')}, front doors from {P('tint_front2')}, sun strip {P('tint_strip')}, removal from {P('tint_removal')}. What changes the price.",
        h1="How much does window tint cost in Louisville?",
        lede="Our starting prices, what moves them up or down, and how to get an exact number for your vehicle.",
        hero_side=pcard("Car tint, Ceramic IR, from", "tint_ir", "Side windows and back glass on a sedan or coupe.",
                        ["Front two doors from " + P("tint_front2"), "Windshield sun strip " + P("tint_strip"), "Removal from " + P("tint_removal")]),
        body=body, faqs=faqs,
        service=dict(name="Window tint pricing", type="Automotive window tinting", brands=["HITEK"], offers=PRICES["tint_front2"]),
    )


def law():
    by_window = table(
        ["Window", "Car or truck", "SUV or van (MPV)"],
        [["Windshield", "Strip above the AS-1 line, or clear film that keeps the windshield at 70% or more. Not red or yellow.", "Same"],
         ["Front side windows", "35% or lighter, reflectance 25% or less", "Same"],
         ["Rear side windows", "18% or lighter, reflectance 35% or less", "8% or lighter, reflectance 35% or less"],
         ["Back glass", "18% or lighter, reflectance 35% or less", "8% or lighter, reflectance 35% or less"]],
        caption="Kentucky tint limits by window, KRS 189.110 as amended July 15, 2024",
        note="Side and rear limits are for the film tested on 1/8-inch clear glass. Every percentage has a 3% tolerance. "
             "A back glass you can’t see through also requires outside mirrors on both sides.")
    hero_facts = ('<ul class="facts">'
                  '<li><b>Front doors</b><span>35% or lighter</span></li>'
                  '<li><b>Behind the driver</b><span>18% or lighter</span></li>'
                  '<li><b>SUVs and vans (MPV)</b><span>8% or lighter behind the driver</span></li>'
                  '<li><b>Windshield</b><span>Strip above AS-1, or 70%+ with the glass</span></li>'
                  '<li><b>Tolerance</b><span>3%</span></li>'
                  '<li><b>Label</b><span>Required, driver’s door jamb</span></li></ul>')
    body = section(
        answer("Under KRS 189.110, Kentucky allows window film on the front side windows if it lets through at least 35% of light, and on the "
               "windows behind the driver if it lets through at least 18%, or 8% on multipurpose passenger vehicles such as most SUVs and vans. "
               "The film is rated on clear glass with a 3% tolerance. On the windshield, a strip above the AS-1 line is allowed, and since "
               "July 15, 2024, so is film that keeps the windshield at 70% or more. Installers must put a compliance label on the driver’s door jamb.")
        + '<h2>Kentucky tint limits by window</h2>' + by_window)
    body += section('<div class="band-head"><h2>Try a shade</h2><p>Pick your vehicle and a shade for each part of the car.</p></div>' + shade_tool(),
                    "band-raised", "shade-check")
    body += section(prose(
        "<h2>The details, one at a time</h2>",
        "<h3>Front side windows</h3>",
        "The windows beside and in front of the driver need film that lets through at least 35% of visible light, with reflectance of "
        "25% or less, measured from the side without film. Kentucky tests the film on 1/8-inch clear glass, so the light already blocked by "
        "your factory glass doesn’t count against you.",
        "<h3>Windows behind the driver</h3>",
        "Every window behind the driver, including the back glass, needs film of at least 18% with reflectance of 35% or less. On a "
        "multipurpose passenger vehicle the limit drops to 8%. Look at the federal label on the driver’s door jamb: it says MPV if your "
        "vehicle qualifies. Most SUVs, crossovers and minivans do. Pickups are labeled TRUCK and use the 18% rule.",
        "Perforated window graphics on rear windows have their own rule: at least 30% light transmission, with reflectance limits measured in sections.",
        "<h3>Back glass and mirrors</h3>",
        "If the back glass is covered with anything you can’t see through, the vehicle needs outside mirrors on both sides. Every modern "
        "car has them, but it matters for older vehicles and for heavy rear graphics.",
        "<h3>The windshield (changed in 2024)</h3>",
        "Senate Bill 46, signed in March 2024, changed the windshield rules. You can have a transparent strip across the top that stays out "
        "of the AS-1 area, or film on the windshield that, used together with the windshield’s glass, has light transmission of at least 70% "
        "and isn’t red or yellow. Because the glass and film are measured together, very few films pass on most windshields. "
        '<a href="@windshield-tint-louisville">How we handle windshields</a>.',
        "<h3>Tolerance</h3>",
        "Every percentage in the law has a tolerance of plus or minus 3 percentage points.",
        "<h3>The label</h3>",
        "Installers have to give you a permanent label stating the film is compliant, with the film’s trade name and the installer’s business name. "
        "It goes on the inside of the driver’s door jamb. If a police officer has a question about your tint, that label is the first thing they’ll want to see.",
        "<h3>Penalties</h3>",
        "Kentucky treats applying film in violation of the law as a Class B misdemeanor, and the law expects non-compliant film to be removed.",
        "<h3>Medical exemptions</h3>",
        "KRS 189.110 itself doesn’t include a medical exemption. Ceramic film blocks 99% of UV even at light shades.",
        "<h3>Indiana and other states</h3>",
        "If you live across the river or just moved here, your current tint was installed under another state’s rules. Indiana and "
        "Tennessee measure and limit tint differently."))
    body += section(prose(
        "<h2>Sources</h2>",
        f'<ul><li><a href="{KRS_URL}" rel="noopener">KRS 189.110, Kentucky Revised Statutes (2024)</a></li>'
        f'<li><a href="{ACT_URL}" rel="noopener">2024 Ky. Acts ch. 17 (Senate Bill 46), effective July 15, 2024</a></li></ul>',
        '<p class="note">This page explains the statute in plain language. It isn’t legal advice. Last checked October 2026.</p>'),
        "band-raised")
    faqs = [
        ("What is the darkest legal tint in Kentucky?",
         "35% on the front side windows. Behind the driver, 18% on cars and trucks, or 8% on multipurpose passenger vehicles such as most SUVs and vans."),
        ("Is 20% tint legal in Kentucky?",
         "On windows behind the driver, yes. On the front side windows, no: the limit there is 35%."),
        ("Is 5% limo tint legal in Kentucky?",
         "No. Even on an SUV or van labeled MPV, the darkest allowed behind the driver is 8%."),
        ("Does Kentucky measure tint with the factory glass?",
         "For side and rear windows, no. The law rates the film tested on 1/8-inch clear glass. The windshield rule is different: the film is judged together with the windshield glass."),
        ("When did the Kentucky windshield tint law change?",
         "Senate Bill 46 took effect on July 15, 2024. It allows windshield film if the windshield with the film still lets through at least 70% of light."),
        ("Do I need a sticker for window tint in Kentucky?",
         "Yes. The installer must put a compliance label on the inside of the driver’s door jamb with the film’s trade name and the installer’s business name."),
        ("Is there a medical exemption for tint in Kentucky?",
         "KRS 189.110 doesn’t include one. Ceramic film blocks 99% of UV even at light shades."),
    ]
    return dict(
        slug="kentucky-tint-laws", group="Kentucky law", crumb="Kentucky Tint Law",
        title="Kentucky Tint Law 2026: Legal Limits by Window | 502 Tinted",
        desc="Kentucky window tint law (KRS 189.110) in plain English: 35% front, 18% rear, 8% for SUVs and vans, the 2024 windshield change, labels and penalties.",
        h1="Kentucky window tint law, in plain English",
        lede="What KRS 189.110 allows on each window of your car, truck or SUV, including the 2024 windshield change. Last checked October 2026.",
        hero_side=hero_facts, proof=False,
        body=body, faqs=faqs, modified=UPDATED,
    )


def pages():
    return [car(), ceramic(), windshield(), removal(), hitek(), cost(), law()]
