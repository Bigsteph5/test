# How to Reach the KC Leads

Gathered 2026-11-20 from each company's Google profile and website. Call first; everything else backs up the call.

## Contact sheet

| Lead | Call | Text | Email | Online | Visit in person | Ask for |
|---|---|---|---|---|---|---|
| **Gunn Heating & Cooling** | **(816) 551-9177** (Google, verified; "Open 24 hours") | Same number, only after a call or voicemail | None published | Google profile "Contact us" button; they post on Google almost daily, so the owner checks it | No public office (service-area business based near Paola, KS) | **Jeremy** (owner, named in many reviews); Tyler also on staff |
| **R&S Contracting** | **(816) 300-1561** (Google, verified; open 24 hours) | Same number, only after a call | None published | Google profile only | No public office | **Ryan** (an owner, named in a review) |
| **Comfort Kings** | **(913) 277-9428** (main), (913) 433-0504 (second) | Their contact page says "feel free to email, call, text" | **service@comfortkingskc.com** | Contact form at comfortkings.squarespace.com/contact-us · facebook.com/comfortkingskc | No public office (Overland Park area) | The owner; **Drew** is a tech named in reviews |
| **Cool Heat KC** | **(913) 333-0493** (main), (913) 660-5179 | Not offered; call | **info@coolheatkc.com** | Contact form (linked from their site) · facebook.com/coolheatkc | **501 East Front Street, Bonner Springs, KS 66012** | **Rick Rogers** (owner, veteran) or **Tracie Rogers**; office manager **Amy Griffith** answers the office |

## Order and timing
1. **Gunn:** best lead (no site, 113 five-star reviews, already active on Google).
2. **R&S:** no site, young company that needs reviews and visibility.
3. **Cool Heat KC:** visible bugs on their current site make an easy opener. You can also drop by in person.
4. **Comfort Kings:** has a site with a contact form; pitch the redesign and the phone experience.

**When to call:** Tuesday–Thursday, **9:30–11:30 a.m. or 1:30–3:30 p.m.**
- Avoid Monday mornings (dispatch is busy with weekend backlog) and avoid calling during a cold snap or heat wave, when owners are on emergency calls.
- If you hit voicemail, leave a short message, then follow up with a text or email the same day.

**Owners are often on a job.** If someone else answers, ask: "When's the best time to catch [name] for two minutes?" Then call back exactly then.

## Scripts

### First call (no website: Gunn, R&S)
> Hi, is this Jeremy? This is [your name], I'm a web designer here in Kansas City. I'll be quick. You've got 113 five-star reviews on Google, which is outstanding, but there's no website. When people compare HVAC companies on their phone, they tap through to websites, and right now they land on your competitors' instead. I already built one for you using your real reviews. Can I text you the link? If you don't like it, no hard feelings.

For R&S, swap in: "You've got a perfect 5-star rating on Google and you're open 24/7, but there's no website…"

### First call (has a site: Cool Heat KC, Comfort Kings)
> Hi, is this Rick? This is [your name], a web designer here in KC. I was on your website and noticed the top of the page shows leftover code ("Marketing 2026-04-17…") and the Facebook link is spelled "Facebbok". Small stuff, but customers notice. I built a cleaner version with a request form and click-to-call. Can I text you the link?

### Voicemail (20 seconds)
> Hi [name], this is [your name], a web designer in Kansas City. I built a new website preview for [business] using your real Google reviews. No cost to look. I'll text you the link. My number is [your number]. Thanks!

### Text (only after they said yes, or right after your voicemail)
> Hi [name], [your name] here, the web designer who just called. Here's the website I built for [business]: [link]. It's $497 to make it yours, then $49/mo for hosting and edits. Happy to change anything. Reply STOP and I won't text again.

### Email (Comfort Kings, Cool Heat KC)
**Subject:** I rebuilt [Business]'s website (live link inside)
> Hi [name],
>
> I'm [your name], a web designer in Kansas City. I built a new version of your website using your own content and reviews: [link]
>
> What's different: a click-to-call button on every screen, an online request form that sends jobs straight to your phone, your service area by town, and it loads fast on phones.
>
> It's $497 to make it yours, then $49/month for hosting and any changes. If you don't like it, nothing owed.
>
> Can I call you Thursday morning to walk through it?
>
> [your name] · [phone] · [your business mailing address]
> If you'd rather not hear from me again, just reply "no thanks."

### In person (Cool Heat KC, Bonner Springs)
Go mid-morning on a weekday with the preview open on your phone and a printed one-page card (screenshot + QR code + price). Ask for Rick or Amy. Keep it under 5 minutes.

## Follow-up rhythm
- **Day 0:** call, then voicemail, then text or email.
- **Day 2:** second call at a different time of day.
- **Day 5:** short email or Facebook message: "Still holding your preview live, any questions?"
- **Day 10:** last touch: "Taking the preview down Friday unless you want it."

After that, delete the preview and move on.

## Rules
- **Never pitch through HomeAdvisor, Angi or Thumbtack request forms, and never send a fake service request.** Contractors pay for every lead on those platforms, so a fake request costs them money and burns your reputation.
- **Texting:** text a business cell number only after a call or voicemail, identify yourself, and honor "STOP" right away.
- **Email:** include your real name, mailing address and an easy opt-out (US CAN-SPAM rules). Don't buy email lists.
- **Facebook:** one message to the business page is fine; don't message employees' personal profiles.
- Keep every claim about their business true. The previews use only public facts and real reviews.

## Before you call: fix-ups pending
- **R&S preview isn't live yet.** Netlify's free deploy credits ran out; deploy `hvac-kc/leads/dist/rs-contracting` once they reset or after upgrading.
- **Gunn and Cool Heat KC previews have corrections waiting** (Gunn: 24/7 and its south-metro service area; Cool Heat: Bonner Springs location and email). These are rebuilt in `hvac-kc/leads/dist/` and go live on the next deploy.
- **Comfort Kings pitch correction:** their contact page *does* have a form. Pitch the phone experience, the default Squarespace address and thin content instead of "no form".
- Delete the old `kc-preview-steves` and `kc-preview-arctic-air` projects in the Netlify dashboard.
