from kit import *

AREA_DATA = [
dict(
    slug="window-tint-valley-station", name="Valley Station", place="Valley Station", city="Louisville", zips="40272",
    title="Window Tint Valley Station, Louisville | 502 Tinted",
    desc=f"Window tint and auto detailing in Valley Station, Louisville (40272). Our shop is on Valley Station Rd: HITEK ceramic tint from {P('tint_ir')}, full details from {P('full')}.",
    lede="Our shop is right here on Valley Station Road. Ceramic tint and detailing without crossing town.",
    answer=f"502 Tinted is in Valley Station, at {ADDRESS_LINE}. We install HITEK Ceramic IR and Ceramic Plus window tint (from {P('tint_ir')} "
           f"for a car) and detail cars, trucks and SUVs, from a {P('wash')} maintenance wash to paint correction.",
    local="Valley Station is home. It’s the stretch of southwest Louisville between Pleasure Ridge Park and the Ohio River, with Dixie Highway "
          "running through the middle and the river roads heading out toward Riverside, the Farnsley-Moremen Landing. If you live off Dixie, "
          "off Valley Station Road or out toward the river, we’re likely the closest tint shop to your driveway.",
    route="Most Valley Station customers are a few minutes away on surface streets, no highway needed. Drop the car off on your way somewhere and "
          "pick it up the same afternoon.",
    drive="A lot of Valley Station driving is Dixie Highway, and the low sun on Dixie sits on your passenger side both ways: east in the morning "
          "heading north, west in the evening heading south. Ceramic film on the side glass takes the heat off that side of the car, and a "
          "windshield sun strip helps with the glare.",
    picks="Most of our neighbors choose Ceramic IR on the whole car, at 35% up front and 20% behind the driver. Families with an SUV or van "
          "often go darker in back, which Kentucky allows on vehicles labeled MPV.",
    near=["Dixie Highway (US 31W)", "Valley Station Road", "Riverside, the Farnsley-Moremen Landing", "Jefferson Memorial Forest", "The Gene Snyder Freeway"],
    faqs=[("Is there a window tint shop in Valley Station?",
           f"Yes. 502 Tinted is at {ADDRESS_LINE}, and does window tint and auto detailing."),
          ("Can I drop my car off in the morning and get it back the same day?",
           "For most tint jobs and most details, yes. Shop hours vary by day, so check the hours when you book."),
          ("Do you detail cars in Valley Station?",
           f"Yes, at the shop. Interior details start at {P('interior')} and full details at {P('full')}.")]),
dict(
    slug="window-tint-pleasure-ridge-park", name="Pleasure Ridge Park", place="Pleasure Ridge Park", city="Louisville", zips="40258",
    title="Window Tint Pleasure Ridge Park (PRP) | 502 Tinted",
    desc=f"Window tint and detailing for Pleasure Ridge Park, Louisville. HITEK ceramic tint from {P('tint_ir')}, lifetime guarantee, a short drive down Dixie Highway.",
    lede="PRP is next door. A short drive down Dixie for ceramic tint, or a detail while you run errands.",
    answer=f"502 Tinted serves Pleasure Ridge Park from its shop in Valley Station, just south of PRP along Dixie Highway. We install HITEK ceramic "
           f"window tint from {P('tint_ir')} for a car and detail cars, trucks and SUVs, with starting prices posted on the site.",
    local="Pleasure Ridge Park runs along Dixie Highway north of Valley Station, around Greenwood Road and Lower Hunters Trace. It’s our closest "
          "neighbor, and a big share of our customers have a PRP address.",
    route="Head south on Dixie Highway into Valley Station. For most of PRP it’s a short drive, about ten minutes.",
    drive="PRP driving is mostly Dixie, the Gene Snyder and the Watterson, plus school pickup lines where the car sits in the sun. Ceramic tint "
          "keeps the car cooler while it sits, and blocks 99% of UV for kids in the back seat.",
    picks="Ceramic IR is the usual pick here. If your car sits in a work lot all day, Ceramic Plus is worth the step up.",
    near=["Dixie Highway (US 31W)", "Greenwood Road", "Lower Hunters Trace", "Pleasure Ridge Park High School", "I-264 (the Watterson)"],
    faqs=[("How far is 502 Tinted from Pleasure Ridge Park?",
           "We’re just south in Valley Station. For most of PRP, it’s about ten minutes down Dixie Highway."),
          ("What tint is best for kids in the back seat?",
           "Ceramic film behind the driver at 20% on a car, or darker on an SUV labeled MPV. Every shade blocks 99% of UV."),
          ("Do you do front windows only?",
           f"Yes, the front two doors start at {P('tint_front2')}, to match factory rear privacy glass.")]),
dict(
    slug="window-tint-shively-ky", name="Shively", place="Shively, KY", city="Shively", zips="40216",
    title="Window Tint Shively, KY | Ceramic Tint | 502 Tinted",
    desc=f"Window tint and auto detailing for Shively, KY. HITEK ceramic tint from {P('tint_ir')}, lifetime guarantee from HITEK. Straight down Dixie Highway.",
    lede="From Shively, it’s a straight run down Dixie Highway to ceramic tint and detailing in Valley Station.",
    answer=f"502 Tinted serves the City of Shively from its shop in Valley Station, a straight drive south on Dixie Highway. We install HITEK "
           f"Ceramic IR and Ceramic Plus tint (from {P('tint_ir')} for a car) and offer full details from {P('full')}.",
    local="Shively is its own small city inside Louisville, up Dixie Highway past Pleasure Ridge Park, and home to the old Stitzel-Weller "
          "distillery, where the Bulleit Frontier Whiskey Experience is today. A lot of Shively drivers spend their day between Dixie, "
          "the Watterson and the industrial corridors nearby.",
    route="Take Dixie Highway south through Pleasure Ridge Park into Valley Station, about 15 minutes.",
    drive="Work trucks and commuter cars that sit outside through a shift take the most heat. Ceramic Plus is built for that, with around 90% "
          "infrared rejection in every shade.",
    picks="Work trucks often get Ceramic Plus on the front doors and Ceramic IR in back. Cars usually get Ceramic IR all around.",
    near=["Dixie Highway (US 31W)", "Stitzel-Weller distillery", "I-264 (the Watterson)", "Shively City Hall"],
    faqs=[("Do you tint work trucks from Shively?",
           "Yes. Trucks are priced by window count. Pickups follow the 18% rule behind the driver."),
          ("How long is the drive from Shively?",
           "About 15 minutes south on Dixie Highway."),
          ("Can you remove old purple tint?",
           f"Yes, removal starts at {P('tint_removal')}, and you can retint the same visit.")]),
dict(
    slug="window-tint-fairdale-ky", name="Fairdale", place="Fairdale", city="Louisville", zips="40118",
    title="Window Tint Fairdale, Louisville | 502 Tinted",
    desc=f"Window tint and detailing for Fairdale, Louisville. HITEK ceramic tint from {P('tint_ir')}, shades picked for dark county roads at night.",
    lede="Fairdale drivers deal with dark, winding roads at night. We pick ceramic shades that keep the heat out and the road visible.",
    answer=f"502 Tinted serves Fairdale from its shop in nearby Valley Station. We install HITEK ceramic window tint from {P('tint_ir')} for a car "
           "and detail cars, trucks and SUVs by appointment.",
    local="Fairdale is the southern edge of Jefferson County, wrapped around Jefferson Memorial Forest, along National Turnpike and the roads "
          "out toward Bullitt County. It still feels like the country, and the driving shows it: two-lane roads, deer, and very little street lighting.",
    route="Head west across the south end of the county toward Valley Station, about 15 to 20 minutes depending on where you start.",
    drive="On unlit roads, night visibility matters more than how dark the back windows look. Kentucky already caps the front doors at 35%, and "
          "plenty of Fairdale customers go lighter than that up front. Ceramic film still cuts the heat at 50% or 70%.",
    picks="Ceramic Plus at 35% or 50% on the fronts is a popular choice here: real heat rejection, clear view at night.",
    near=["Jefferson Memorial Forest", "National Turnpike", "Fairdale High School", "The Gene Snyder Freeway"],
    faqs=[("What tint shade is best for driving at night?",
           "Lighter is better up front. 35% is the legal limit on the front doors in Kentucky; 50% or 70% ceramic keeps more light while still blocking heat."),
          ("Do you serve Fairdale?",
           "Yes. Fairdale customers drive over to our shop in Valley Station, about 15 to 20 minutes away."),
          ("Can you clean red clay and mud out of my interior?",
           f"Yes. An interior detail ({P('interior')} and up) includes shampooing carpets and mats.")]),
dict(
    slug="window-tint-okolona", name="Okolona", place="Okolona", city="Louisville", zips="40219",
    title="Window Tint Okolona, Louisville | 502 Tinted",
    desc=f"Window tint and detailing for Okolona, Louisville. HITEK ceramic tint from {P('tint_ir')} that keeps cars cool in Jefferson Mall and work lots.",
    lede="Big parking lots, long shifts, hot cars. Ceramic tint for Okolona drivers, a quick run west on the Gene Snyder.",
    answer=f"502 Tinted serves Okolona from its shop in Valley Station, about 20 minutes west on the Gene Snyder Freeway. We install HITEK "
           f"ceramic window tint from {P('tint_ir')} for a car and detail cars, trucks and SUVs.",
    local="Okolona centers on Preston Highway, from the Outer Loop and Jefferson Mall south toward the Gene Snyder, with the Ford plant and UPS a "
          "short drive away. It’s a place where cars spend a lot of time parked in big, unshaded lots.",
    route="Take the Gene Snyder west toward Dixie Highway and Valley Station, about 20 minutes.",
    drive="A car parked through an eight- or ten-hour shift soaks up heat all day. Ceramic Plus rejects around 90% of the infrared coming through "
          "the glass, so the cabin starts cooler when you get back in.",
    picks="Shift workers lean toward Ceramic Plus. Shoppers and short-commute drivers do fine with Ceramic IR.",
    near=["Preston Highway", "Outer Loop", "Jefferson Mall", "The Gene Snyder Freeway", "Fern Valley Road"],
    faqs=[("How far is 502 Tinted from Okolona?",
           "About 20 minutes west on the Gene Snyder Freeway."),
          ("Which tint keeps a car coolest in a parking lot?",
           "HITEK Ceramic Plus. It’s rated around 90% infrared rejection in every shade."),
          ("Can you tint and detail on the same day?",
           "Yes. We detail first, then tint.")]),
dict(
    slug="window-tint-hillview-ky", name="Hillview", place="Hillview, KY", city="Hillview", zips="40229",
    title="Window Tint Hillview, KY | Bullitt County | 502 Tinted",
    desc=f"Window tint and detailing for Hillview, KY in Bullitt County. HITEK ceramic tint from {P('tint_ir')}, lifetime guarantee from HITEK.",
    lede="Just over the county line in Bullitt County. Ceramic tint and detailing at our Valley Station shop.",
    answer=f"502 Tinted serves Hillview, Kentucky, from its shop in Valley Station in southwest Louisville. We install HITEK Ceramic IR and "
           f"Ceramic Plus window tint (from {P('tint_ir')} for a car) and offer full details from {P('full')}.",
    local="Hillview is the first Bullitt County city along Preston Highway once you cross the Jefferson County line. Most Hillview drivers "
          "commute north into Louisville every day, so the car gets a lot of hours in the sun.",
    route="Take the Gene Snyder west toward Dixie Highway and Valley Station, about 20 to 25 minutes.",
    drive="Daily commutes on Preston Highway and I-65 mean the same sun on the same side of the car every morning and evening. "
          "Ceramic film on the side glass takes the burn off your arm and the glare off the road.",
    picks="Ceramic IR on the whole car, with a windshield sun strip for the commute.",
    near=["Preston Highway (KY 61)", "Bullitt County line", "I-65", "The Gene Snyder Freeway"],
    faqs=[("Do you serve Hillview and Bullitt County?",
           "Yes. Hillview customers come to our shop in Valley Station, about 20 to 25 minutes away."),
          ("Is window tint law different in Bullitt County?",
           "No. Kentucky’s tint law is statewide: 35% front doors, 18% behind the driver, 8% for SUVs and vans labeled MPV."),
          ("How much is a windshield sun strip?",
           f"{P('tint_strip')}, or add it to a tint job.")]),
dict(
    slug="window-tint-shepherdsville-ky", name="Shepherdsville", place="Shepherdsville, KY", city="Shepherdsville", zips="40165",
    title="Window Tint Shepherdsville, KY | 502 Tinted",
    desc=f"Window tint and detailing for Shepherdsville, KY. HITEK ceramic tint from {P('tint_ir')} for I-65 commuters and warehouse shifts.",
    lede="I-65 commutes and long warehouse shifts. Ceramic tint that keeps Shepherdsville cars cool, a short drive up I-65.",
    answer=f"502 Tinted serves Shepherdsville from its shop in Valley Station, about 25 minutes away by I-65 and the Gene Snyder. We install "
           f"HITEK ceramic window tint from {P('tint_ir')} for a car and detail cars, trucks and SUVs.",
    local="Shepherdsville is the Bullitt County seat, on the Salt River where I-65 and KY 44 meet, and the distribution centers along I-65 "
          "keep growing. That means a lot of cars sitting in open lots for a full shift, and a lot of highway miles.",
    route="Take I-65 north to the Gene Snyder, then west to Dixie Highway and Valley Station, about 25 minutes.",
    drive="A car sitting in a warehouse lot for ten hours in July is the best argument for ceramic tint there is. Ceramic Plus is the "
          "strongest heat blocker we install.",
    picks="Ceramic Plus for warehouse and shift workers; Ceramic IR for everyone else. Many add a detail in the same trip.",
    near=["I-65", "KY 44", "Salt River", "Paroquet Springs Conference Centre", "Bullitt County Courthouse"],
    faqs=[("How far is 502 Tinted from Shepherdsville?",
           "About 25 minutes by I-65 and the Gene Snyder Freeway."),
          ("Is it worth driving from Shepherdsville for tint?",
           "If you want HITEK ceramic film with a lifetime guarantee, most customers think so. Book a detail the same day to make the trip count."),
          ("Do you tint SUVs?",
           "Yes. SUVs labeled MPV can go as dark as 8% behind the driver in Kentucky.")]),
dict(
    slug="window-tint-mount-washington-ky", name="Mount Washington", place="Mount Washington, KY", city="Mount Washington", zips="40047",
    title="Window Tint Mount Washington, KY | 502 Tinted",
    desc=f"Window tint and detailing for Mount Washington, KY. HITEK ceramic tint from {P('tint_ir')}, for family SUVs and commuters, plus full details.",
    lede="Family SUVs and long commutes into Louisville. Ceramic tint and full details for Mount Washington drivers.",
    answer=f"502 Tinted serves Mount Washington, Kentucky, from its shop in Valley Station in southwest Louisville, about 30 minutes away. We "
           f"install HITEK ceramic window tint from {P('tint_ir')} for a car and detail cars, trucks and SUVs, with prices posted online.",
    local="Mount Washington sits on US 31E in Bullitt County, a fast-growing town where a lot of families live and commute into Louisville. "
          "That means a lot of SUVs and minivans, and a lot of kids in the back seat.",
    route="Take KY 44 west to Shepherdsville and I-65 north, or Bardstown Road to the Gene Snyder, then west to Valley Station. Either way, about 30 minutes.",
    drive="Most SUVs and minivans are labeled MPV, so Kentucky lets them go as dark as 8% behind the driver. Ceramic film there keeps the "
          "third row cooler and blocks 99% of UV.",
    picks="Family SUVs: 35% Ceramic IR up front, 15% or 20% behind. Add an interior detail and it comes back like new.",
    near=["US 31E (Bardstown Road)", "KY 44", "Bullitt County", "I-65"],
    faqs=[("How dark can I tint my SUV in Kentucky?",
           "35% on the front doors. Behind the driver, 8% if the door-jamb label says MPV, which most SUVs and minivans do."),
          ("How long is the drive from Mount Washington?",
           "About 30 minutes, by KY 44 and I-65 or by Bardstown Road and the Gene Snyder."),
          ("Can you get crushed snacks out of a third row?",
           f"Yes. An interior detail starts at {P('interior')} for a car; SUVs and vans are priced after a look.")]),
dict(
    slug="window-tint-radcliff-fort-knox", name="Radcliff & Fort Knox", place="Radcliff and Fort Knox", city="Radcliff", zips="40160, 40121",
    title="Window Tint Radcliff & Fort Knox, KY | 502 Tinted",
    desc=f"Window tint and detailing for Radcliff and Fort Knox. HITEK ceramic tint from {P('tint_ir')}, HITEK’s guarantee goes with you on PCS moves. Straight up US 31W.",
    lede="Ceramic tint and detailing for Fort Knox families, straight up US 31W from the gate.",
    answer=f"502 Tinted serves Radcliff and Fort Knox from its shop in Valley Station, about 30 minutes north on US 31W (Dixie Highway). We "
           f"install HITEK ceramic window tint from {P('tint_ir')} for a car, remove old film, and "
           "detail cars, trucks and SUVs.",
    local="Radcliff sits right outside Fort Knox in Hardin County, and US 31W, the same Dixie Highway that runs past our end of Louisville, "
          "connects them. Plenty of our Hardin County customers are military families who just arrived from another state.",
    route="Take US 31W north through Fort Knox and Muldraugh into Valley Station, about 30 minutes from Radcliff.",
    drive="Military families move a lot, and a car can spend years parked in the sun on post. HITEK’s lifetime guarantee is honored at HITEK "
          "dealers nationwide, so the film’s coverage goes with you to the next duty station.",
    picks="Ceramic IR for most cars, Ceramic Plus for long drives on 31W. Saturday mornings, 8 to 1, work well around duty schedules.",
    near=["US 31W (Dixie Highway)", "Fort Knox", "General George Patton Museum", "Muldraugh", "Hardin County"],
    faqs=[("Is tint from another state legal in Kentucky?",
           "Kentucky allows 35% on the front doors and 18% behind the driver (8% on SUVs and vans labeled MPV). Other states set their own limits."),
          ("Does the HITEK warranty move with me if I get new orders?",
           "Yes. HITEK’s lifetime warranty is honored nationwide."),
          ("Are you open Saturdays?",
           "Yes, Saturday 8 AM to 1 PM. Weekday hours vary; check the hours before you drive up.")]),
dict(
    slug="window-tint-elizabethtown-ky", name="Elizabethtown", place="Elizabethtown, KY", city="Elizabethtown", zips="42701",
    title="Window Tint Elizabethtown, KY | 502 Tinted",
    desc=f"Window tint and detailing for Elizabethtown (E-town), KY. HITEK ceramic tint from {P('tint_ir')}, lifetime guarantee. Make it one trip with a detail.",
    lede="It’s a drive from E-town, so make it count: ceramic tint and a full detail in one visit.",
    answer=f"502 Tinted serves Elizabethtown from its shop in Valley Station in southwest Louisville, about 45 minutes up US 31W or I-65. We "
           f"install HITEK ceramic window tint from {P('tint_ir')} for a car and detail cars, trucks and SUVs.",
    local="Elizabethtown is the Hardin County seat, where I-65 meets the Western Kentucky and Bluegrass Parkways. E-town drivers put serious "
          "highway miles on their cars, which is where ceramic tint earns its keep.",
    route="Take US 31W north through Radcliff and Fort Knox into Valley Station, or I-65 north to the Gene Snyder. About 45 minutes either way.",
    drive="Long highway stretches mean long hours with the sun on one side of the car. Ceramic film blocks most of the infrared heat and 99% "
          "of UV without making the glass too dark to see out of at night.",
    picks="Ceramic Plus for long commutes. Since it’s a drive, most E-town customers book tint and a detail together and pick up the same day.",
    near=["I-65", "US 31W", "Western Kentucky Parkway", "Bluegrass Parkway", "Ring Road"],
    faqs=[("How far is 502 Tinted from Elizabethtown?",
           "About 45 minutes, by US 31W through Fort Knox or by I-65 and the Gene Snyder."),
          ("Can I get tint and a detail in one trip?",
           "Yes. Drop off in the morning, and we detail first and tint second."),
          ("What’s the best tint for long highway drives?",
           "HITEK Ceramic Plus, rated around 90% infrared rejection in every shade.")]),
dict(
    slug="window-tint-st-matthews", name="St. Matthews", place="St. Matthews", city="St. Matthews", zips="40207",
    title="Window Tint St. Matthews, Louisville | 502 Tinted",
    desc=f"Window tint and detailing for St. Matthews, Louisville. HITEK ceramic tint from {P('tint_ir')}, factory-look shades, paint correction from {P('enhance')}.",
    lede="Factory-look ceramic tint and paint correction for St. Matthews drivers, across town on the Watterson.",
    answer=f"502 Tinted serves St. Matthews from its shop in Valley Station, about 30 minutes across town on I-264. We install HITEK ceramic "
           f"window tint from {P('tint_ir')} for a car and offer detailing and paint correction from {P('enhance')}.",
    local="St. Matthews is the east-end city around Shelbyville Road, Mall St. Matthews and Oxmoor Center, with older neighborhoods off "
          "Frankfort Avenue. It’s across town from us, and the customers who make the drive usually want the job done exactly right.",
    route="Take I-264 (the Watterson) around to Dixie Highway, then south to Valley Station, about 30 minutes.",
    drive="Plenty of St. Matthews drivers want a light, factory look rather than dark glass. Ceramic Plus at 50% or 70% keeps the car looking "
          "stock while rejecting a large share of the heat.",
    picks="Ceramic Plus at lighter shades, and a paint enhancement to bring back gloss on darker paint.",
    near=["Shelbyville Road", "Mall St. Matthews", "Oxmoor Center", "Frankfort Avenue", "I-264 (the Watterson)"],
    faqs=[("Can I get tint without it looking dark?",
           "Yes. Ceramic film at 50% or 70% looks close to factory glass and still blocks heat and 99% of UV."),
          ("How far is 502 Tinted from St. Matthews?",
           "About 30 minutes by I-264 and Dixie Highway."),
          ("Do you do paint correction?",
           f"Yes. One-step paint enhancement starts at {P('enhance')}, two-step correction at {P('correct2')}.")]),
dict(
    slug="window-tint-jeffersontown", name="Jeffersontown", place="Jeffersontown (J-town)", city="Jeffersontown", zips="40299",
    title="Window Tint Jeffersontown (J-town), KY | 502 Tinted",
    desc=f"Window tint and detailing for Jeffersontown, KY. HITEK ceramic tint from {P('tint_ir')}, lifetime guarantee from HITEK. Via the Gene Snyder.",
    lede="J-town to Valley Station is one long run on the Gene Snyder. Ceramic tint and detailing at the other end.",
    answer=f"502 Tinted serves Jeffersontown from its shop in Valley Station, about 30 minutes west on the Gene Snyder Freeway. We install HITEK "
           f"ceramic window tint from {P('tint_ir')} for a car and detail cars, trucks and SUVs.",
    local="Jeffersontown, J-town to most people, is the east-end city along Taylorsville Road and Hurstbourne Parkway, with business parks "
          "around Blankenbaker Parkway and the Gaslight Festival every September.",
    route="Take the Gene Snyder Freeway west all the way to Dixie Highway, then into Valley Station, about 30 minutes.",
    drive="Company cars and commuters parked in business-park lots all day get the full sun through the glass. Ceramic tint keeps the "
          "cabin and the dash from cooking.",
    picks="Ceramic IR on commuter cars; Ceramic Plus for sales and service vehicles that live outside.",
    near=["Taylorsville Road", "Hurstbourne Parkway", "Blankenbaker Parkway", "The Gene Snyder Freeway"],
    faqs=[("How far is 502 Tinted from Jeffersontown?",
           "About 30 minutes on the Gene Snyder Freeway."),
          ("Do you tint company vehicles?",
           "Yes. Call or text with the vehicles and we’ll price them."),
          ("Is 20% tint legal on my front windows?",
           "No. Kentucky’s front-door limit is 35%. 20% is legal behind the driver.")]),
]


def shared(a):
    return section(split(
        f'<h2>Tint and detailing for {esc(a["name"])} drivers</h2>'
        + price_list([("tint_ir", "Full car tint, Ceramic IR", "Side windows and back glass"),
                      ("tint_plus", "Full car tint, Ceramic Plus", "HITEK’s strongest heat rejection in our lineup"),
                      ("tint_front2", "Front two doors", "To match factory rear privacy glass"),
                      ("full", "Full detail", "Interior and exterior")],
                     note="Starting prices for cars. SUVs, trucks and vans are priced by size."),
        prose("<h3>How it works</h3>",
              steps([("Get a price", f"Text {PHONE} or send the quote form with your vehicle."),
                     ("Drop off", "Bring it to the shop on Valley Station Road."),
                     ("Pick up", "Most tint jobs and details are done the same day.")])),
        "split-top"), "band-raised")


def area_page(a):
    near = "".join(f"<li>{n}</li>" for n in a["near"])
    side = (f'<ul class="facts"><li><b>Shop</b><span>{ADDRESS_LINE}</span></li>'
            f'<li><b>Getting here</b><span>{a["route"]}</span></li>'
            f'<li><b>Hours</b><span>{HOURS_SHORT}</span></li>'
            f'<li><b>Phone or text</b><span><a href="tel:{PHONE_E164}">{PHONE}</a></span></li></ul>')
    body = section(answer(a["answer"]) + split(
        prose(f"<h2>Serving {esc(a['place'])}</h2>", a["local"], a["drive"]),
        prose("<h3>What we usually recommend here</h3>", a["picks"], "<h3>Landmarks near you</h3>", f'<ul>{near}</ul>'),
        "split-top"))
    body += shared(a)
    body += section(f'<h2>Other areas we serve</h2>{area_links(exclude=a["slug"])}')
    return dict(
        slug=a["slug"], group="Service areas", crumb=a["name"], crumbs=[("Service Areas", "service-areas")],
        title=a["title"], desc=a["desc"],
        h1=f"Window tint and detailing for {esc(a['place'])}",
        lede=a["lede"], hero_side=side, proof=False,
        body=body, faqs=a["faqs"],
        service=dict(name=f"Window tint in {a['name']}", type="Automotive window tinting", brands=["HITEK"],
                     offers=PRICES["tint_ir"], area=[{"@type": "City", "name": a["city"]}]),
    )


def hub():
    groups = [
        ("Louisville and Jefferson County", ["window-tint-valley-station", "window-tint-pleasure-ridge-park", "window-tint-shively-ky",
                                              "window-tint-fairdale-ky", "window-tint-okolona", "window-tint-st-matthews", "window-tint-jeffersontown"]),
        ("Bullitt County", ["window-tint-hillview-ky", "window-tint-shepherdsville-ky", "window-tint-mount-washington-ky"]),
        ("Hardin County", ["window-tint-radcliff-fort-knox", "window-tint-elizabethtown-ky"]),
    ]
    by = {a["slug"]: a for a in AREA_DATA}
    blocks = ""
    for title, slugs in groups:
        blocks += f'<h2 style="margin-top:1.4em">{esc(title)}</h2>' + rows(
            [(by[s]["name"], by[s]["route"], f"@{s}") for s in slugs], "rows-3")
    body = section(
        answer(f"502 Tinted is at {ADDRESS_LINE}, in Valley Station in southwest Louisville. Customers come from across Louisville and "
               "Jefferson County, Bullitt County (Hillview, Shepherdsville, Mount Washington) and Hardin County (Radcliff, Fort Knox, "
               "Elizabethtown). All work is done at the shop.")
        + blocks)
    body += section(prose(
        "<h2>Same law everywhere in Kentucky</h2>",
        "Kentucky’s tint law is statewide, so it doesn’t matter which county you live in: 35% on the front doors, 18% behind the driver, "
        "8% behind the driver on SUVs and vans labeled MPV, and specific rules for the windshield.",
        "Every job is done at the shop, where we have the light, the clean bay and the tools to do it right. Most tint jobs and details are "
        "finished the same day, so even customers coming from Elizabethtown or Jeffersontown only make one trip.",
        '<a href="@kentucky-tint-laws">Kentucky tint law, explained</a>'), "band-raised")
    return dict(
        slug="service-areas", group="Service areas", crumb="Service Areas",
        title="Areas We Serve: Louisville, Bullitt & Hardin | 502 Tinted",
        desc="502 Tinted serves Louisville, Valley Station, PRP, Shively, Fairdale, Okolona, Hillview, Shepherdsville, Mount Washington, Radcliff, Fort Knox and E-town.",
        h1="Areas we serve",
        lede="Our shop is in Valley Station. Customers drive in from all over Louisville, Bullitt County and Hardin County.",
        body=body,
    )


def pages():
    return [hub()] + [area_page(a) for a in AREA_DATA]
