# Kansas City HVAC Leads — Round 1

Collected 2026-11-20 from web search, directory listings and each company's own website where one exists.
**Verify every phone number and rating on Google Maps before you call.** Conflicts are flagged below.

## The 5 demos (in `hvac-kc/leads/<folder>/`)

| # | Business | Area | Phone | Website today | Why they need you | Demo folder |
|---|---|---|---|---|---|---|
| 1 | **Steve's Heating & Cooling** | Riverside, MO (4252 NW Riverside St) | (816) 436-8475 | **None found** | Family-owned since 1979 with a reported 4.9★ from ~517 Google reviews, but no website. Customers searching "furnace repair Northland" find competitors instead. | `steves-heating-cooling` |
| 2 | **Gunn Heating & Cooling** | KC metro (BuildZoom lists Paola, KS) | (816) 551-9177 ⚠️ | **None found** | 5.0★ from 103 Google reviews and no website. | `gunn-heating-cooling` |
| 3 | **Arctic Air Heating & Cooling** | Gladstone, MO (6708 N Oak Trafficway) | (816) 436-1000 ⚠️ | **None confirmed** | Lennox Premier Dealer, family owned, no website found. | `arctic-air-gladstone` |
| 4 | **Comfort Kings Heating and Cooling** | Overland Park, KS | (913) 277-9428 | comfortkings.squarespace.com | Their site lives on a default Squarespace address, has no request form and only ~475 words, and shows two phone numbers. They have 30+ years of history and strong reviews to feature. | `comfort-kings` |
| 5 | **Cool Heat KC** | Shawnee, KS | (913) 333-0493 | coolheatkc.com (WordPress) | The live site shows leftover text "Marketing 2026-04-17T09:17:16+00:00" in the menu area and a "Facebbok" typo. The browser title is a 120-character keyword string. No request form. Veteran-owned, Mitsubishi Diamond Elite. | `cool-heat-kc` |

⚠️ **Phone conflicts:**
- Gunn: Google shows (816) 551-9177; BuildZoom shows (816) 557-9177. HomeAdvisor says they don't offer emergency service, so the demo makes no 24/7 claim.
- Arctic Air: BBB shows (816) 436-1000; another listing shows 1-816-587-4000. Founding year conflicts (1975 vs 2010), so the demo omits it.
- Steve's: the 517-review count comes from an aggregator (ServiceAgent). Check Google before quoting it. The demo shows "4.9★ on Google" only.

## Live preview links (Netlify, your account)
| Business | Preview |
|---|---|
| Steve's Heating & Cooling | https://kc-preview-steves.netlify.app |
| Gunn Heating & Cooling | https://kc-preview-gunn.netlify.app |
| Arctic Air Heating & Cooling | https://kc-preview-arctic-air.netlify.app |
| Comfort Kings Heating and Cooling | https://kc-preview-comfort-kings.netlify.app |
| Cool Heat KC | https://kc-preview-cool-heat.netlify.app |

Request forms are on (Netlify Forms). Submissions land in your Netlify dashboard under each project's Forms tab. Delete a project if the owner says no.

Redeploy after edits: change `hvac-kc/leads/leads.json` → `python3 hvac-kc/leads/gen.py` → `hvac-kc/leads/build_dist.sh <folder>` → deploy that `dist/<folder>`.

## What each demo contains
- Real name, phone, town and service area, plus facts from their own site or listings (see `source` in `hvac-kc/leads/leads.json`).
- Reviews **only** where the company publishes them itself (Comfort Kings, Cool Heat KC). Steve's, Gunn and Arctic Air show a clearly marked placeholder. Paste 3 real Google reviews in before pitching, or tell the owner you'll add them.
- No invented stats. Offers, plan prices and the tune-up price are marked "Sample price" and the top bar says "Website preview · not the live site · prices and offers are placeholders".
- `noindex` so Google won't index a preview.

## Checked and skipped (already have good sites)
- **Air Care Heating & Cooling** (Shawnee): agency-built site (RYNO), mobile-ready, booking form, current copyright. Not a fit.
- **Lakeside Heating and Cooling** (Lee's Summit): solid WordPress site with 3 forms. Low priority.

## Backup leads (not yet checked)
- **TJ's Heating & Cooling**, Independence (13879 E 35th St Ct S). Since 1995, no website found, but only ~2 Yelp reviews. Phone not found.
- **Dad's Heating and Cooling**, Blue Springs (114 NW 3rd St). Site at www.dadscoolair.com, not audited (host blocked here).
- **McIntosh Heating & Cooling**, Independence (since 1943). Site www.mcintosh-hc.com, not audited.
- Others to research: Shawnee Heating & Cooling (Lenexa, since 1983), Patriot Heating & AC (Shawnee), City Wide Heating & Cooling (KCK), Heartland Quality (Lee's Summit), Town & Country (Lenexa).

## Call order
1. Steve's (no site, most reviews)
2. Gunn (no site, perfect rating)
3. Comfort Kings (weak site, real reviews already in the demo)
4. Cool Heat KC (visible bugs on the current site make an easy opener)
5. Arctic Air (verify phone first)

## Opener tailored to "no website" leads
> Hi, is this the owner? I'm a web designer here in Kansas City. You've got a 4.9 on Google, which is great, but when I searched for you there's no website. People who don't call straight from Maps end up on a competitor's site. I built you one already. Can I text you the link? If you don't like it, it costs you nothing.

## Opener for Cool Heat KC
> I was on your website and noticed the top of the page shows some leftover code text, "Marketing 2026-04-17…", and the Facebook link is spelled "Facebbok." Small things, but customers notice. I built a cleaner version with an online request form. Can I text you the link?
