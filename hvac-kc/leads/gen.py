"""Generate per-lead demo sites from hvac-kc/index.html and leads.json.

Usage: python3 gen.py            -> writes leads/<slug>/index.html for every lead
Each demo removes the template's invented stats, prices-as-fact and sample reviews,
and uses only the facts recorded in leads.json (see each lead's "source").
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
TEMPLATE = (HERE.parent / "index.html").read_text()


def tel(p):
    return "+1" + re.sub(r"\D", "", p)


def esc(s):
    return html.escape(s, quote=False)


def build(L):
    s = TEMPLATE
    count = {"n": 0}

    def rep(old, new, n=1):
        c = s.count(old)
        assert c == n, f"{L['slug']}: expected {n}x, found {c}x: {old[:70]!r}"
        return s.replace(old, new)

    name, short, ph = L["name"], L["short"], L["phone"]
    em = L["emergency"]

    # Head + JSON-LD
    s = rep("<title>Kestrel Climate Co.</title>", f"<title>{esc(name)}</title>\n<meta name=\"robots\" content=\"noindex\">")
    s = rep('content="Heating, cooling and indoor air quality across the Kansas City metro, in Missouri and Kansas. 24/7 repair, dual-fuel heat pumps, furnaces and central air."',
            f'content="{esc(name)}: heating and cooling in {L["city"]}, {L["region"]} and the Kansas City area."')
    ld = {"@context": "https://schema.org", "@type": "HVACBusiness", "name": name, "telephone": tel(ph),
          "address": {"@type": "PostalAddress", "addressLocality": L["city"], "addressRegion": L["region"], "addressCountry": "US"},
          "areaServed": L["area1"]["towns"] + L["area2"]["towns"]}
    if L.get("street"):
        ld["address"]["streetAddress"] = L["street"]
        ld["address"]["postalCode"] = L.get("zip", "")
    s = re.sub(r'<script type="application/ld\+json">.*?</script>',
               '<script type="application/ld+json">\n' + json.dumps(ld, indent=2) + "\n</script>", s, count=1, flags=re.S)

    # Contact details everywhere
    s = s.replace("+18165550173", tel(ph)).replace("(816) 555-0173", ph)
    s = s.replace("Kestrel Climate Co.", esc(name)).replace("Kestrel", esc(short))

    # Preview ribbon (clearly not the business's live site)
    s = rep('<nav class="nav" id="nav">\n',
            '<nav class="nav" id="nav">\n  <div class="alert" style="background:var(--panel);color:var(--muted)">Website preview for '
            + esc(name) + ' · not the live site · prices and offers are placeholders</div>\n')

    winter_alert = "Cold nights ahead. No-heat calls answered 24/7 across the metro." if em else "Cold nights ahead. Book your furnace check before the first hard freeze."
    summer_alert = "Heat advisory season. No-cooling calls answered 24/7 across the metro." if em else "Hot days ahead. Book your AC check before the first heat wave."
    s = rep("Cold nights ahead. No-heat calls answered 24/7 across the metro.", winter_alert)
    s = rep("Heat advisory season. No-cooling calls answered 24/7 across the metro.", summer_alert)

    # Hero
    s = rep("Heating · Cooling · Air quality — Kansas City, both sides of State Line", L["eyebrow"])
    s = re.sub(r'(<p class="lede">)' + re.escape(esc(short)) + r' designs, installs and tunes whole-home climate systems.*?</p>',
               lambda m: m.group(1) + L["lede"] + "</p>", s, count=1, flags=re.S)
    s = rep('<span><b>4.9</b> from 1,860 reviews</span><span><b>90-min</b> emergency window</span><span>Licensed in MO &amp; KS</span>',
            "".join(f"<span>{m}</span>" for m in L["meta"]))

    # Ticker = this company's own services
    items = " <i></i> ".join(L["services"]) + " <i></i>"
    s = re.sub(r'(<div class="ticker-track">\s*)<span>.*?</span>\s*<span>.*?</span>',
               lambda m: m.group(1) + f"<span>{items}</span>\n    <span>{items}</span>", s, count=1, flags=re.S)

    # Offer: keep as a placeholder the owner sets
    s = rep('<small id="offerWas">Reg. $159</small>', '<small id="offerWas" style="text-decoration:none">Sample price</small>')
    s = rep("$('offerWas').textContent = 'Reg. $149';", "$('offerWas').textContent = 'Sample price';")

    # Services: remove claims we can't verify
    s = rep(", with a 12-year parts and labor warranty.", ".")
    s = rep("<li>Utility rebate filing</li>", "<li>Repair or replace advice</li>")
    s = rep("<li>Up to 97% AFUE</li>", "<li>High-efficiency furnaces</li>")
    s = rep('<span class="big mono" id="repairClock">90<small style="font-size:.35em">min</small></span>',
            '<span class="big mono" id="repairClock">' + ("24/7" if em else "Same day") + "</span>")
    s = rep("A licensed tech at your door within 90 minutes anywhere in the metro, with flat-rate pricing agreed before any work starts.",
            "Call any time, day or night. You hear the price before any work starts." if em else
            "Call and we'll get you on the schedule as fast as we can. You hear the price before any work starts.")
    s = rep("<h3>When it quits at 2 a.m.</h3>", "<h3>" + ("When it quits at 2 a.m." if em else "When it quits on you.") + "</h3>")
    c4 = L["card4"]
    s = re.sub(r'<span class="svc-tag">Light commercial</span>.*?</ul>',
               lambda m: f'<span class="svc-tag">{c4["tag"]}</span>\n        <h3>{c4["title"]}</h3>\n        <p>{c4["body"]}</p>\n        <ul>'
               + "".join(f"<li>{t}</li>" for t in c4["tags"]) + "</ul>", s, count=1, flags=re.S)

    # Proof: verified facts + real reviews only
    first = L["reviews"][0] if L["reviews"] else None
    if first:
        quote = (f'<figure class="quote rise" style="margin:0">\n        <blockquote>“{esc(first["text"])}”</blockquote>\n'
                 f'        <figcaption><b>{esc(first["who"])}</b>{esc(first["src"])}</figcaption>\n      </figure>')
    else:
        quote = ('<figure class="quote rise" style="margin:0">\n        <blockquote>Your best Google reviews go here, word for word, '
                 'with the customer\'s first name and neighborhood.</blockquote>\n'
                 '        <figcaption><b>Placeholder</b>Real reviews are added before this site goes live</figcaption>\n      </figure>')
    nums = "".join(f"<div><strong>{a}</strong><span>{b}</span></div>" for a, b in L["facts"])
    s = re.sub(r'<div class="proof">.*?<p class="sample-note">.*?</p>',
               lambda m: '<div class="proof">\n      ' + quote + '\n      <div class="nums rise">' + nums + "</div>\n    </div>\n"
               + (('    <div class="revs two">' if len(L["reviews"]) == 3 else '    <div class="revs">') + "".join(
                   f'<article class="rev rise"><div class="stars" aria-hidden="true">★★★★★</div><p>“{esc(r["text"])}”</p>'
                   f'<footer><b>{esc(r["who"])}</b> · {esc(r["src"])}</footer></article>' for r in L["reviews"][1:]) + "</div>"
                  if len(L["reviews"]) > 1 else ""), s, count=1, flags=re.S)

    # Service area
    s = rep("<h2>Both sides of State Line.</h2>", "<h2>" + ("Both sides of State Line." if {L['area1']['label'], L['area2']['label']} == {'MO', 'KS'} else "Close to home.") + "</h2>")
    s = rep("Licensed in Missouri and Kansas, with trucks based north of the river and in Johnson County, so most of the metro is inside a 30-minute drive.", L["areaLede"])

    def area_html(a):
        return (f'<div class="state-h"><b>{a["label"]}</b><span>{a["sub"]}</span></div>\n        <ul class="towns">'
                + "".join(f"<li>{esc(t)}</li>" for t in a["towns"]) + "</ul>")
    blocks = re.findall(r'<div class="state-h">.*?</ul>', s, flags=re.S)
    assert len(blocks) == 2
    s = s.replace(blocks[0], area_html(L["area1"]), 1).replace(blocks[1], area_html(L["area2"]), 1)
    s = rep("const h = new Date().getHours(), eta = h >= 7 && h < 19 ? 'today, usually within 2 hours' : 'within 90 minutes for no-heat or no-cooling calls';",
            "const eta = 'out to you: call or book below for the next opening';")
    s = rep("out.append(b, ` A technician can be there ${eta}.`);", "out.append(b, ` We can get a technician ${eta}.`);")

    # FAQ: generic answers, no invented numbers
    s = rep("For no-heat and no-cooling calls, our target is 90 minutes anywhere in the metro, day or night. Routine repairs and tune-ups are usually booked the same or next day in a two-hour arrival window.",
            f"Call {ph} and we'll give you the soonest arrival window we have." + (" Emergency service is available 24/7." if em else ""))
    s = rep("A diagnostic visit is $89, credited toward the repair if you go ahead. Comfort Club members pay nothing for the diagnostic and never pay overtime.",
            "Call for current diagnostic pricing. You hear the cost before any work starts.")
    s = rep("<p>Yes. We pull permits with your city on both sides of State Line, and file any utility rebate paperwork your new equipment qualifies for.</p>",
            "<p>Yes. We pull the permits your city requires and help with any utility rebate paperwork your new equipment qualifies for.</p>")
    s = rep("Most of our KC installs are dual-fuel", "Many Kansas City homes use dual-fuel")

    # Booking
    s = rep("A comfort advisor calls back within 15 minutes during business hours to confirm a two-hour arrival window.",
            "We call you back to confirm an arrival window. In a hurry? Call " + ph + ".")
    if L["email"]:
        s = rep("dispatch@kestrelclimate.example", L["email"])
    else:
        s = re.sub(r'\s*<div><span class="k">Email</span>.*?</div>', "", s, count=1, flags=re.S)
    s = rep('<span class="k">Call 24/7</span>', '<span class="k">' + ("Call 24/7" if em else "Call") + "</span>")
    s = rep("Office Mon–Sat 7–7 · Repair 24/7", L["hours"])
    s = rep("A comfort advisor will call", "We will call")

    # Process + plans: keep, but no invented per-company stats
    s = rep("Members get priority scheduling during heat waves and cold snaps, and never pay overtime.", "Members get priority scheduling during heat waves and cold snaps.")

    # Footer
    s = rep("Residential and light commercial HVAC across the Kansas City metro, in Missouri and Kansas.",
            f"Heating and cooling in {L['city']}, {L['region']} and the Kansas City area. {ph}")
    s = re.sub(r'<div><h4>Service area</h4><ul>.*?</ul></div>',
               "<div><h4>Service area</h4><ul>" + "".join(f"<li>{esc(t)}</li>" for t in (L["area1"]["towns"] + L["area2"]["towns"])[:6]) + "</ul></div>",
               s, count=1, flags=re.S)
    s = rep("<span>© 2026 " + esc(name) + " · Licensed in Missouri &amp; Kansas</span><span>Demo concept · fictional company · Video: Mixkit</span>",
            "<span>© 2026 " + esc(name) + "</span><span>Website preview · not the live site · Video: Mixkit</span>")
    s = rep('<div class="wordmark" aria-hidden="true">' + esc(short) + "</div>",
            '<div class="wordmark" aria-hidden="true" style="font-size:clamp(40px,10vw,160px)">' + esc(short) + "</div>")

    # Taller fixed header (preview ribbon) + long eyebrows need room
    s = rep("</style>", "@media (max-width: 700px) { #alert { display: none; } }\n.revs.two { grid-template-columns: repeat(2, minmax(0, 1fr)); }\n@media (max-width: 900px) { .revs.two { grid-template-columns: 1fr; } }\n.hero .eyebrow { line-height: 1.5; }\n.hero-grid { padding-top: 210px; }\n@media (max-width: 900px) { .hero-grid { padding-top: 200px; } }\n</style>")

    # Media lives one level up so all demos share one copy in the repo
    s = s.replace('src="media/', 'src="../../media/')
    assert "Kestrel" not in s and "555-0173" not in s, L["slug"]
    return s


if __name__ == "__main__":
    for L in json.loads((HERE / "leads.json").read_text()):
        out = HERE / L["slug"] / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(build(L))
        print("wrote", out.relative_to(HERE))
