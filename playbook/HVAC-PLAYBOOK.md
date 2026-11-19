# HVAC Website Flip — 24-Hour Playbook

## The offer
"I already rebuilt your website. Here's the live link. It's yours for $497, and hosting plus edits are $49/month."

| Item | Price | Notes |
|---|---|---|
| Site handoff (setup) | $497 | Can go as low as $297 to close on the call |
| Hosting + edits | $49/mo | The recurring income. 20 clients = ~$1,000/mo |
| Upsell: missed-call text-back | +$99/mo | Auto-texts anyone whose call goes unanswered |
| Upsell: Google review requests | +$49/mo | Texts a review link after each job |

HVAC owners pay $300–$1,000+ for **one** lead from Google Ads or Angi. That number is why $497 is easy to justify.

## Hour 0–2: Build the lead list (target 40)
Search Google Maps for `hvac near <town>` and `heating and cooling <town>`, then check nearby towns. Qualify a business when it has **at least one** of these problems:
- No website at all (the Maps listing has no website link). These are the best leads.
- The site isn't usable on a phone (pinch-zoom, tiny text).
- No phone number at the top of the page, or no click-to-call button.
- The copyright says 2019 or older, or the site uses Flash-era / Wix-default design.
- The site is slow (over 5 seconds on pagespeed.web.dev).

They must also have **20+ Google reviews**. That proves they're busy and have money, and you can reuse the reviews on the demo site.

Record each lead in a sheet with these columns: Business, Owner name, Phone, Email, Town, Problem, Reviews, Demo URL, Status.

## Hour 2–8: Build 5 demos
For each of your top 5 leads, tell Claude Code:
> Customize hvac-demo/index.html for <Business>: phone <x>, towns <y>, license <z>, years in business <n>, these 3 real Google reviews: <paste>. Deploy it.

Use only real details from their Google listing. Keep the license number blank if you can't find it. Each demo gets its own preview URL.

## Hour 8–20: Outreach (volume wins)
**Order:** call first, then text, then email. Visit in person if they're within 15 minutes; it closes better than any other channel.

### Call script (30 seconds)
> Hi, is this <owner>? This is <you>. I build websites for HVAC companies here in <town>. I was looking at your Google listing. You've got <N> great reviews, but your website <isn't showing up right on phones / doesn't exist>, which means people searching "AC repair near me" are calling whoever comes up next.
>
> So I went ahead and built you a new one. It's already live. Can I text you the link? Takes 30 seconds to look at.

If they say yes, text the link right away and stay on the line:
> It has click-to-call on every page, your reviews, your service area, and a form that sends estimate requests straight to your phone. It's $497 to make it yours, and I handle hosting and changes for $49 a month. If you don't like it, you pay nothing.

### Text (when they don't pick up)
> Hi <owner>, <you> here. I build sites for local HVAC companies. I made a new website for <Business> using your Google reviews. It's live here: <link>. Yours for $497 if you want it. No obligation.

### Email subject lines
- "I rebuilt <Business>'s website (live link inside)"
- "<Business>: 612 great reviews, but customers can't find them"

## Objections
| They say | You say |
|---|---|
| "I get enough work from referrals." | "Great. Referrals still Google you before they call. This makes sure they don't call the next guy instead." |
| "I already have a website guy." | "No problem. If they're not on it, this one's ready today. Want me to send it so you can compare?" |
| "Too expensive." | "One extra AC install pays for it about 10 times over. I can do $297 to set it up today." |
| "Send me info." | "I'll text you the live link now. It's quicker than a brochure. Can I follow up Thursday at 10?" |
| "Not right now." | "Heading into furnace season is when search traffic spikes. I'll hold your demo live for 7 days." |

## Getting paid
1. Create a free Stripe account, then **Payment Links**: one link for $497 (one-time) and one for $49/month (subscription).
2. Send both links over text when they say yes.
3. After they pay: connect their domain (or buy one for ~$12), add their email to receive the form, and hand off.

## Daily targets
- **Day 1:** 40 leads, 5 demos, 40 calls/texts. Expect 0–2 closes.
- **Days 2–14:** 20 new contacts per day, 2–3 new demos per day.
- A 5–10% close rate gives **4–8 clients in 2 weeks** ≈ $2–4k up front + $200–400/mo recurring, growing every month.

## Rules
- Never claim to be affiliated with the business before they buy. The demo is a pitch, not their site.
- Take demos down if they say no.
- Don't invent reviews, licenses or awards. Use only what's public.
