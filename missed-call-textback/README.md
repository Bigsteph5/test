# Missed-Call Text-Back (n8n + Twilio)

When an HVAC client misses a call, the caller gets a text within seconds, before they call the next company. The owner gets a text alert, and any reply from the lead is forwarded to the owner's phone.

Import `workflow.json` into n8n. Use one copy of the workflow per client.

## What happens on a call

```
Caller ──► client's number ──(no answer)──► Twilio number ──► n8n
                                                        │
               caller hears: "Sorry we missed your call. We'll text you right now."
                                                        │
             ┌──────────────────────────────────────────┴─────────────────┐
     Text to caller (from the Twilio number)               Text to owner: "Missed call from +1816…"
             │
     Caller replies ──► Twilio ──► n8n ──► owner gets "Lead +1816… replied: my AC is out"
```

What the caller receives:
- **During business hours:** "Hi, this is Acme Heating & Cooling. Sorry we missed your call, we're with a customer. What can we help with? Reply here and we'll get right back to you."
- **After hours:** "…we're closed right now. Reply with what you need and we'll call you first thing."

Built-in safeguards:
- A caller isn't texted again within 12 hours, even if they call five times.
- Hidden or blocked caller IDs and the owner's own number are skipped.
- Twilio gets its answer before the texts are sent, so the caller never hears a delay.

## The two setup modes
Set `mode` in the **Client Config** node.

| Mode | When to use | How calls reach Twilio |
|---|---|---|
| `forward-unanswered` (default) | The client keeps the number on their trucks and Google profile. This is almost every client. | The client's carrier forwards **unanswered** calls to the Twilio number. Every call that arrives is treated as missed. |
| `twilio-number` | A brand-new business, or one willing to publish a new number. | Calls go to the Twilio number, which rings `ownerPhone` for `ringSeconds`. If nobody answers, the text goes out. |

## Setup (about 30 minutes per client)

### 1. Twilio (one-time, about $1.15/mo per number plus about $0.0083 per text)
1. Create a Twilio account and buy a **local number** in the client's area code (816 or 913 for KC).
2. **Register for A2P 10DLC** (Messaging → Regulatory Compliance). This is required for business texting in the US. Without it, carriers block or filter your texts. Register your own business as a brand, then add one campaign per client (use case: "Customer Care"; sample message: the text above). Approval takes from a few days to about 2 weeks, so **start this on day 1**.
3. Copy your **Account SID** and **Auth Token** from the Twilio console.

### 2. n8n
1. In n8n: **Workflows → Import from File → `workflow.json`**.
2. Open any Twilio node, create a **Twilio API** credential (paste the SID and token), and select it on all three Twilio nodes: *Text the Caller*, *Alert the Owner*, *Forward Reply to Owner*.
3. Edit the **Client Config** node: business name, owner's cell, hours, timezone and optional booking link.
4. Open **Twilio Webhook** and change the path from `acme-hvac/twilio` to a unique path for this client, such as `gunn-hvac/twilio`.
5. **Activate** the workflow (toggle at top right). Copy the **Production URL** from the webhook node.

> **Hosting n8n for $0:** self-host on a free-tier VM (Oracle Cloud Always Free, or Google Cloud e2-micro) with Docker. It needs a public HTTPS URL, and the `WEBHOOK_URL` setting must equal that URL. n8n Cloud is easier but paid. Once you have a few clients, a ~$5/mo VPS is fine.

### 3. Connect the Twilio number to n8n
Twilio console → Phone Numbers → your number:
- **Voice → A call comes in:** Webhook, `<Production URL>?event=voice`, HTTP POST
- **Messaging → A message comes in:** Webhook, `<Production URL>?event=sms`, HTTP POST

### 4. Forward the client's unanswered calls (for `forward-unanswered` mode)
Set **conditional call forwarding** ("forward when unanswered") on the client's line to the Twilio number. How depends on the carrier:
- **Cell phones:** most US carriers use a dial code. On Verizon it's `*71` + number. AT&T and T-Mobile often use `**61*1<number>#` (no answer) plus `**67*1<number>#` (busy). Codes change, so confirm with the carrier.
- **Office or VoIP lines** (RingCentral, Grasshopper, Google Voice, Spectrum): set "forward unanswered calls" in the admin portal.
- Set the ring time to **15–20 seconds** before forwarding.

The carrier's **voicemail is replaced**: unanswered calls go to Twilio instead. Tell the client this. It's the point of the service.

### 5. Test before you hand it over
1. Call the client's number from your phone and let it ring out.
2. Within about 10 seconds you should hear the greeting and get the text. The owner should get the alert.
3. Reply to the text. The owner should get "Lead … replied: …".
4. Call again right away. You should **not** get a second text, because of the 12-hour dedupe.

Note: the dedupe memory only works while the workflow is **active**. In manual "Test workflow" runs it always texts.

## Configuration reference (Client Config node)

| Setting | Default | Meaning |
|---|---|---|
| `mode` | `forward-unanswered` | See "The two setup modes" above |
| `businessName` | Acme Heating & Cooling | Used in the text |
| `ownerPhone` | +18165550100 | Gets alerts and forwarded replies. In `twilio-number` mode it's also the phone that rings. |
| `ringSeconds` | 15 | `twilio-number` mode only. Must be shorter than the owner's voicemail pickup, or voicemail "answers" and no text is sent. |
| `timezone` | America/Chicago | For business hours |
| `openDays`, `openHour`, `closeHour` | Mon–Sat, 7–19 | Picks the open or closed message |
| `bookingLink` | empty | Appended to the text if set |
| `dedupeHours` | 12 | Minimum time between texts to the same caller |
| `alertOwner` | true | Owner alerts and reply forwarding |
| `greeting`, `msgOpen`, `msgClosed` | see node | `{business}` and `{booking}` are filled in automatically |

## Pricing reminder
This costs you about $2–5/mo per client in Twilio fees. The playbook prices it at **+$99/mo**. Lead with "one recovered AC call pays for a year of this."

## Ideas for later
- Log every missed call and reply to a Google Sheet, which feeds the monthly results report.
- Verify Twilio request signatures for extra security.
- Send a Google review request after each job.
