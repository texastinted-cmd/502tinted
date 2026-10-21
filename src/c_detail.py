from kit import *

TIMES = table(
    ["Package", "Starting price", "Typical time in the shop"],
    [["Maintenance wash", f"from {P('wash')}", "About an hour"],
     ["Interior detail", f"from {P('interior')}", "2–4 hours"],
     ["Exterior detail", f"from {P('exterior')}", "2–3 hours"],
     ["Full detail", f"from {P('full')}", "4–6 hours, drop off in the morning"],
     ["Paint enhancement", f"from {P('enhance')}", "Most of a day"],
     ["Two-step paint correction", f"from {P('correct2')}", "One to two days"]],
    caption="Detailing packages for cars",
    note="Times are for a typical car in average condition. Very dirty interiors, pet hair and large SUVs take longer.")


def hub():
    body = section(
        answer(f"502 Tinted details cars, trucks and SUVs at its shop at {ADDRESS_LINE}. Packages start at {P('wash')} for a maintenance wash, "
               f"{P('interior')} for an interior detail, {P('exterior')} for an exterior detail and {P('full')} for a full detail, with paint "
               f"correction from {P('enhance')}. Detailing is by appointment; call or text {PHONE}.")
        + '<div class="band-head"><h2>Packages and prices</h2><p>What each package includes, and where it starts.</p></div>'
        + menu_card())
    body += section(
        '<div class="band-head"><h2>How long each detail takes</h2><p>So you can plan your day around the drop-off.</p></div>' + TIMES,
        "band-raised")
    body += section(split(
        prose("<h2>Detailing for Kentucky weather</h2>",
              "Louisville is hard on cars in every season. Winter brine and road salt sit in the wheel wells and on the lower doors. "
              "Spring pollen in the Ohio Valley turns dark paint yellow in a day. Summer brings bugs from every highway drive and sap from "
              "parking under trees, and fall leaves stain paint if they sit wet.",
              "A good exterior detail strips all of that off, decontaminates the paint, and adds a sealant so the next round washes off "
              "easier. An interior detail gets the salt stains out of the carpet and the crumbs out of the seat tracks.",
              "Twice a year is a good rhythm for most cars: once after winter, once before it."),
        photo("detail-hero")))
    body += section(
        '<h2>Pick the right detail</h2>'
        + rows([
            ("Interior detail", "For the inside: carpets, seats, plastics, glass. Pet hair, kids, a commute’s worth of coffee.", "@interior-detailing-louisville"),
            ("Exterior detail", "For the paint, wheels and glass: wash, decontamination, clay and sealant.", "@exterior-detailing-louisville"),
            ("Full detail", f"Both, in one visit, from {P('full')}. The most popular choice, especially before selling a car.", None),
            ("Paint correction", "For swirls, haze and scratches you can see in the sun. One-step or two-step machine polishing.", "@paint-correction-louisville"),
        ]), "band-raised")
    body += section(split(
        prose("<h2>Detail and tint in one visit</h2>",
              "If you’re tinting too, book them together. We detail first, so the glass is as clean as it will ever be when the film goes on, "
              "and you only drop the car off once.",
              f'<a href="@car-window-tint-louisville">Car window tint from {P("tint_ir")}</a>'),
        prose("<h2>What we need from you</h2>",
              ticks(["Take out anything you want to keep: car seats, gym bags, the stuff under the seats",
                     "Tell us about stains, smells or pet hair when you book, so we plan the time",
                     "Let us know about any paint damage or touch-up spots before a polish"])),
        "split-top"))
    faqs = [
        ("How much does a car detail cost in Louisville?",
         f"At 502 Tinted, a full detail starts at {P('full')} for a car. Interior-only starts at {P('interior')}, exterior-only at {P('exterior')}, and a maintenance wash at {P('wash')}."),
        ("How long does a full detail take?",
         "Four to six hours for a typical car. Drop it off in the morning and pick it up in the afternoon."),
        ("Do you detail SUVs and trucks?",
         "Yes. They have more surface and more interior, so they’re priced after we see them."),
        ("How often should I get my car detailed?",
         "A full detail twice a year suits most cars, with maintenance washes in between. Cars that sit outside or carry pets need it more often."),
    ]
    return dict(
        slug="auto-detailing-louisville", group="Detailing", crumb="Auto Detailing",
        title=f"Auto Detailing Louisville, KY | Full Detail From {P('full')}",
        desc=f"Car detailing in Valley Station, Louisville: maintenance wash {P('wash')}, interior {P('interior')}, exterior {P('exterior')}, full detail {P('full')}, paint correction {P('enhance')}. Book by text.",
        h1="Auto detailing in Louisville",
        lede="Hand washes, deep interiors, clay and sealant, and machine polishing, with the prices posted. By appointment at our shop on Valley Station Road.",
        hero_side=pcard("Full detail, from", "full", "Interior and exterior, for a car. SUVs and trucks quoted after a look.",
                        [f"Maintenance wash from {P('wash')}", f"Interior from {P('interior')}", f"Exterior from {P('exterior')}"],
                        btn=("Book a detail", "@get-a-quote")),
        body=body, faqs=faqs,
        service=dict(name="Auto detailing", type="Car detailing", offers=PRICES["wash"],
                     alt=["Car detailing Louisville", "Full detail Louisville KY", "Detailing near me"]),
    )


def interior():
    body = section(
        answer(f"An interior detail at 502 Tinted starts at {P('interior')} for a car. It includes a full vacuum with the trunk, shampooed carpets "
               "and mats, cleaned seats (leather cleaned and conditioned), the dash, console, door panels and vents, and the glass. Pet hair "
               f"removal ({P('pet')}), stain extraction ({P('stain')} per area) and odor treatment ({P('odor')}) are add-ons.")
        + split(prose(
            "<h2>What’s in an interior detail</h2>",
            ticks(["<strong>Vacuum, everywhere.</strong> Under the seats, the seat tracks, between the console and the seats, and the trunk.",
                   "<strong>Carpets and mats.</strong> Shampooed and extracted, which is how winter salt stains come out.",
                   "<strong>Seats.</strong> Cloth is cleaned and extracted. Leather is cleaned with a leather-safe cleaner and conditioned so it doesn’t dry out.",
                   "<strong>Hard surfaces.</strong> Dash, console, cup holders, door panels and vents, cleaned and finished without a greasy shine.",
                   "<strong>Glass.</strong> Inside and out, including the top edge of the side windows that hides under the seal."])),
            photo("interior"), "split-top"))
    body += section(
        '<div class="band-head"><h2>Before and after</h2><p>A pair of photos from the same car will go here.</p></div>'
        + f'<div class="pair">{photo("interior-before")}{photo("interior-after")}</div>', "band-raised")
    body += section(split(
        prose("<h2>Add-ons for the tough ones</h2>",
              price_list([("pet", "Pet hair removal", "Dog hair woven into carpet takes its own tools and time"),
                          ("stain", "Stain extraction, per area", "Coffee, juice, makeup, the mystery spot on the back seat"),
                          ("odor", "Odor treatment", "For smoke, pets and spills that soaked in")])),
        prose("<h2>When an interior detail makes sense</h2>",
              "After winter, when the carpets are crusted with salt. Before selling or trading in a car, when the interior is most of "
              "the first impression. After a road trip with kids or dogs. Or when you just want the car to feel new again.",
              "If you’re tinting the windows too, book the interior first. Clean glass and a clean door panel mean a cleaner tint job.",
              f'<a href="@auto-detailing-louisville">See the full detailing menu</a>'),
        "split-top"))
    faqs = [
        ("How much is an interior detail in Louisville?",
         f"At 502 Tinted, an interior detail starts at {P('interior')} for a car. Pet hair, heavy stains and large SUVs cost more."),
        ("How long does an interior detail take?",
         "Two to four hours for most cars. Heavy pet hair or stains can add time."),
        ("Can you get salt stains out of carpet?",
         "Usually, yes. Shampooing and hot-water extraction dissolves the white salt lines that build up over a Kentucky winter."),
        ("Can you remove smoke smell?",
         f"A full interior detail plus odor treatment ({P('odor')}) takes care of most smells. Years of heavy smoking may need more than one round."),
        ("Do you clean leather seats?",
         "Yes. Leather is cleaned with a pH-safe cleaner and conditioned."),
    ]
    return dict(
        slug="interior-detailing-louisville", group="Detailing", crumb="Interior Detailing", crumbs=[("Auto Detailing", "auto-detailing-louisville")],
        title=f"Interior Car Detailing Louisville, KY | From {P('interior')}",
        desc=f"Interior car detailing in Louisville from {P('interior')}: carpets shampooed, seats and leather cleaned, salt stains, pet hair and odor. Valley Station shop.",
        h1="Interior car detailing in Louisville",
        lede="Carpets shampooed, seats cleaned, every crack vacuumed. The inside of your car, reset.",
        hero_side=pcard("Interior detail, from", "interior", "For a car. SUVs, vans and very dirty interiors quoted after a look.",
                        ["Carpets and mats shampooed", "Leather cleaned and conditioned", "Glass, vents and door panels"],
                        btn=("Book an interior detail", "@get-a-quote")),
        body=body, faqs=faqs,
        service=dict(name="Interior car detailing", type="Car interior cleaning", offers=PRICES["interior"],
                     alt=["Interior detail Louisville", "Car interior cleaning Louisville KY"]),
    )


def exterior():
    body = section(
        answer(f"An exterior detail at 502 Tinted starts at {P('exterior')} for a car: a hand wash, iron decontamination, a clay bar treatment, "
               "wheels, tires and wheel wells, glass, and a paint sealant that protects for months. It removes the bonded grime a regular wash "
               "leaves behind, so the paint feels smooth and stays cleaner longer.")
        + split(prose(
            "<h2>The steps, in order</h2>",
            steps([
                ("Wheels first", "Wheels, tires and wheel wells are cleaned before the paint, so brake dust doesn’t splash onto clean panels."),
                ("Foam and hand wash", "A foam pre-wash loosens dirt, then a hand wash with clean mitts takes it off."),
                ("Iron decontamination", "An iron remover dissolves brake dust and rail dust embedded in the paint. It turns purple as it works."),
                ("Clay bar", "Clay pulls out what’s left: tree sap specks, overspray and road film. Afterward the paint feels like glass."),
                ("Dry and seal", "The car is dried with clean towels and air, then sealed. The sealant makes water bead and dirt release."),
                ("Glass and tires", "Glass is cleaned inside and out and tires are dressed to a satin finish, not a sling-everywhere shine."),
            ])), photo("exterior"), "split-top"))
    body += section(split(
        prose("<h2>Why decontamination matters here</h2>",
              "Run your hand over the hood after a wash. If it feels gritty, that’s contamination bonded to the paint: iron from brake dust "
              "and rail lines, tree sap, and road film from salt and brine. Washing alone doesn’t remove it.",
              "Leaving it there dulls the paint and makes it harder for any wax or sealant to stick. Removing it is what turns a wash into a detail."),
        prose("<h2>Need more than clean?</h2>",
              "If the paint is swirled or hazy in the sun, a sealant won’t hide that. A machine polish will. Our paint enhancement adds a "
              f"one-step polish to the exterior detail, from {P('enhance')}.",
              '<a href="@paint-correction-louisville">About paint correction</a>'),
        "split-top"), "band-raised")
    body += section(prose(
        "<h2>Keeping it clean afterward</h2>",
        ticks(["Wash every two weeks or so, more in pollen season and winter",
               "Use two buckets and a clean mitt, never a dirty sponge or a brush wash",
               "Rinse off salt as soon as the roads dry out, especially the lower doors and wheel wells",
               f"Book a maintenance wash ({P('wash')}) between details if you don’t have time"]),
        f'<a href="@auto-detailing-louisville">See the full detailing menu</a>'))
    faqs = [
        ("How much is an exterior detail in Louisville?",
         f"At 502 Tinted, an exterior detail starts at {P('exterior')} for a car. SUVs and trucks are priced after a look."),
        ("What’s the difference between a car wash and an exterior detail?",
         "A wash removes loose dirt. An exterior detail also removes bonded contamination with iron remover and clay, cleans the wheels and wells properly, and seals the paint."),
        ("How long does a paint sealant last?",
         "Months, not years. Washing habits, weather and whether the car sleeps outside all change how long it lasts."),
        ("Will an exterior detail remove swirl marks?",
         "No. Swirls are scratches in the clear coat. Removing them takes machine polishing, which is our paint enhancement or paint correction."),
    ]
    return dict(
        slug="exterior-detailing-louisville", group="Detailing", crumb="Exterior Detailing", crumbs=[("Auto Detailing", "auto-detailing-louisville")],
        title=f"Exterior Car Detailing Louisville, KY | From {P('exterior')}",
        desc=f"Exterior car detailing in Louisville from {P('exterior')}: hand wash, iron decontamination, clay bar, wheels and wells, paint sealant. Valley Station shop.",
        h1="Exterior car detailing in Louisville",
        lede="Hand wash, decontamination, clay and sealant. Paint that feels smooth and stays clean longer.",
        hero_side=pcard("Exterior detail, from", "exterior", "For a car. SUVs and trucks quoted after a look.",
                        ["Iron decontamination and clay", "Wheels, tires and wells", "Paint sealant"],
                        btn=("Book an exterior detail", "@get-a-quote")),
        body=body, faqs=faqs,
        service=dict(name="Exterior car detailing", type="Car exterior detailing", offers=PRICES["exterior"],
                     alt=["Exterior detail Louisville", "Clay bar and sealant Louisville"]),
    )


def correction():
    body = section(
        answer(f"Paint correction is machine polishing that removes a thin layer of clear coat to take out swirl marks, haze and light scratches. "
               f"At 502 Tinted, a one-step paint enhancement starts at {P('enhance')} and a two-step correction (compound, then polish) starts "
               f"at {P('correct2')} for a car. Paint thickness is checked before polishing, and deep scratches that go through the clear coat "
               "can’t be polished out.")
        + split(prose(
            "<h2>What paint correction fixes</h2>",
            "Look at your car under a gas-station light or in direct sun. The fine circular scratches you see are swirl marks, usually "
            "from automatic car washes, dirty towels and dry wiping. They make paint look dull and gray, especially on black and dark colors.",
            "Polishing levels the clear coat so light reflects cleanly again. The color looks deeper and the reflection gets sharp.",
            ticks(["Swirl marks and spider-webbing", "Haze and dullness", "Light scratches that don’t catch a fingernail",
                   "Water spot etching", "Holograms left by bad buffing"])),
            photo("correction-5050")))
    body += section(
        '<div class="band-head"><h2>One step or two?</h2></div>'
        + table(["", "Paint enhancement", "Two-step paint correction"],
                [["Starting price", f"from {P('enhance')}", f"from {P('correct2')}"],
                 ["What it does", "One polishing pass with a finishing polish", "A cutting compound pass, then a finishing polish"],
                 ["Typical result", "Light swirls gone, gloss back, deeper defects improved", "Most swirls and light scratches removed"],
                 ["Best for", "Newer cars, light swirls, before selling", "Dark colors, heavy swirls, the car you’re keeping"],
                 ["Time", "Most of a day", "One to two days"],
                 ["Includes", "Full exterior detail and sealant", "Full exterior detail and sealant"]],
                note="Both start with an exterior detail and decontamination, because you can’t polish dirty paint."),
        "band-raised")
    body += section(
        '<h2>How it’s done</h2>'
        + steps([
            ("Wash and decontaminate", "The full exterior detail first: wash, iron remover, clay. Polishing grit into paint makes things worse."),
            ("Measure and inspect", "Paint thickness is checked with a gauge, and the paint is inspected under strong light to map the defects."),
            ("Test spot", "A small section is polished to find the least aggressive combination of pad and polish that does the job."),
            ("Polish panel by panel", "Each panel is polished, wiped and checked under the light before moving on."),
            ("Protect", "A sealant goes on at the end. Freshly polished paint has nothing on it, so it needs protection."),
        ]))
    body += section(split(
        prose("<h2>What it can’t fix</h2>",
              "If a scratch catches your fingernail, it’s probably through the clear coat, and no amount of polishing removes it safely. "
              "The same goes for rock chips, peeling clear coat and failed paint. We’ll tell you what will and won’t come out before we start.",
              "Polishing removes a tiny amount of clear coat every time. That’s why we measure first and use the least aggressive approach."),
        photo("correction-after")), "band-raised")
    faqs = [
        ("How much does paint correction cost in Louisville?",
         f"At 502 Tinted, a one-step paint enhancement starts at {P('enhance')} and a two-step correction at {P('correct2')} for a car. Larger vehicles and very soft or damaged paint cost more."),
        ("How long does paint correction last?",
         "The correction is permanent until new swirls are put in. Careful washing with clean mitts and towels keeps it looking good for years."),
        ("Will paint correction remove scratches?",
         "Light scratches and swirls, yes. Scratches that catch a fingernail are usually through the clear coat and need paint work."),
        ("Is paint correction safe for my paint?",
         "Done right, yes. We measure paint thickness first and use the least aggressive polish that does the job."),
        ("What’s the difference between paint enhancement and paint correction?",
         "Enhancement is one polishing step that brings back gloss and takes out light swirls. Two-step correction cuts first, then polishes, for a deeper result."),
    ]
    return dict(
        slug="paint-correction-louisville", group="Detailing", crumb="Paint Correction", crumbs=[("Auto Detailing", "auto-detailing-louisville")],
        title=f"Paint Correction Louisville, KY | From {P('enhance')} | 502 Tinted",
        desc=f"Swirl mark removal and paint correction in Louisville: one-step enhancement from {P('enhance')}, two-step correction from {P('correct2')}. Paint measured first.",
        h1="Paint correction in Louisville",
        lede="Machine polishing that takes out swirl marks and haze, so the paint reflects like it should. Measured first, polished panel by panel.",
        hero_side=pcard("Paint enhancement, from", "enhance", "One-step polish plus a full exterior detail, for a car.",
                        ["Paint thickness checked first", "Panel-by-panel under inspection light", "Sealed when finished"],
                        btn=("Get a paint correction quote", "@get-a-quote"), second=("Two-step correction, from", "correct2")),
        body=body, faqs=faqs,
        service=dict(name="Paint correction", type="Paint correction and machine polishing", offers=PRICES["enhance"],
                     alt=["Swirl mark removal Louisville", "Paint polishing Louisville KY", "Paint enhancement"]),
    )


def pages():
    return [hub(), interior(), exterior(), correction()]
