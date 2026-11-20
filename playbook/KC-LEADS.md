# Kansas City HVAC Leads — Round 1

Collected 2026-11-20 from web search, directory listings and each company's own website where one exists.
**Verify every phone number and rating on Google Maps before you call.** Conflicts are flagged below.

## The 5 demos (in `hvac-kc/leads/<folder>/`)

| # | Business | Area | Phone | Website today | Why they need you | Demo folder |
|---|---|---|---|---|---|---|
| 1 | **Gunn Heating & Cooling** | KC metro (BuildZoom lists Paola, KS) | (816) 551-9177 | **None found** | Verified Google profile: 5.0★ from 113 reviews, and no website. **Best lead.** | `gunn-heating-cooling` |
| 2 | **Comfort Kings Heating and Cooling** | Overland Park, KS | (913) 277-9428 | comfortkings.squarespace.com | Their site lives on a default Squarespace address, with only ~475 words on the home page and two phone numbers. (Correction: the Contact page does have a form.) They have 30+ years of history and strong reviews to feature. | `comfort-kings` |
| 3 | **Cool Heat KC** | Shawnee, KS | (913) 333-0493 | coolheatkc.com (WordPress) | The live site shows leftover text "Marketing 2026-04-17T09:17:16+00:00" in the menu area and a "Facebbok" typo. The browser title is a 120-character keyword string. No request form. Veteran-owned, Mitsubishi Diamond Elite. | `cool-heat-kc` |
| 4 | **R&S Contracting LLC** | Kansas City + eastern/northern metro | (816) 300-1561 | **None** (uses Google's free business page) | Verified Google profile, 5.0★, open 24/7, HVAC + refrigeration + electrical + plumbing. Only 6 reviews: pitch the site as the way to grow. | `rs-contracting` |

⚠️ **Notes:**
- Gunn: BuildZoom shows (816) 557-9177, but the verified Google profile shows (816) 551-9177, so use the Google number. HomeAdvisor says no emergency service, so the demo makes no 24/7 claim.
- Steve's: the "4.9★ / 517 reviews" figure came from an aggregator and is no longer shown in the demo.
- Arctic Air: the 4.8★ / 696-review figure is Birdeye's total across sources, and the demo labels it that way.

## Where each demo's reviews come from
- **Gunn:** 3 reviews copied word for word from the verified Google Business Profile (John James, Kellsi Proctor, Melissa Hatfield).
- **Steve's:** 3 reviews from stevesheatingkc.com (Michelle M., Harry K., Nancy). The site doesn't label their source.
- **Arctic Air:** 1 review from Birdeye (Kevin W.). Their Google profile wasn't reachable from here, so add 2 Google reviews yourself if you pitch them.
- **Comfort Kings / Cool Heat KC:** reviews from their own sites (Comfort Kings labels theirs "via Google").

## Readiness scan (2026-11-20, live URLs)
| Check | Result |
|---|---|
| Lighthouse (phone, Gunn) | Performance **93**, Accessibility **100**, Best practices **100**, SEO 60 (only because previews are deliberately hidden from Google; 100 once launched) |
| Load speed (phone) | First paint 1.3 s, main content 2.0 s, layout shift 0.004 |
| Page weight | ~5 MB on phone (was ~29 MB before video compression) |
| Errors | 0 console errors, 0 broken requests on all 5 sites, desktop and phone |
| Phone layout | No sideways scroll on any site; call button visible; phone number in header |
| Request form | Test submission arrived in Netlify (Gunn), then deleted |
| Known cosmetic | Netlify shows a "Powered by Netlify" badge bottom-right on free sites; the phone call bar was reshaped so it doesn't collide |

## Live preview links (Netlify, your account)
| Business | Preview |
|---|---|
| Gunn Heating & Cooling | https://kc-preview-gunn.netlify.app |
| Comfort Kings Heating and Cooling | https://kc-preview-comfort-kings.netlify.app |
| Cool Heat KC | https://kc-preview-cool-heat.netlify.app |
| R&S Contracting | https://kc-preview-rs-contracting.netlify.app (**not deployed yet**: Netlify credits used up) |

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

## Retired: Steve's and Arctic Air
Both have working websites (stevesheatingkc.com, arcticairkc.com). Their demo data is kept in `hvac-kc/leads/leads-retired.json`.
**Their previews are still live** (kc-preview-steves, kc-preview-arctic-air), because Netlify blocked the takedown deploy (credits used up). Delete both projects in the Netlify dashboard: Project configuration → Delete project.

## Replacement search (2026-11-20): what was checked
Only one well-reviewed KC HVAC company verifiably has no website. Everyone else checked has one:
Bellis H&C (bellis-hc.com), On the Spot (kansascityhvac.com), Eric Kjelshus Energy (ericsenergy.com), KC Prestige HVAC (kcprestigehvac.com), TJ's (tjshvac.com), Hometown Heroes (hometownheroeskc.com), HVAC Cowboys (site listed on Angi), Dad's (dadscoolair.com), McIntosh (mcintosh-hc.com).
Not usable: Kelly CAN H&C (license shows expired, no reviews), Dave & Kelly's (no phone found), 24h H&C (no phone or reviews).

**Fastest way to find more:** on your phone, search Google Maps for "furnace repair" or "HVAC" in a KC suburb, open each listing, and look for one with no **Website** button. Those listings show an "Add website" prompt to the owner, and they're your best leads.
