# Case Doc Tracker

**🔗 Live demo:** https://biancabcarlson.github.io/Case-Doc-Tracker/

A lightweight, shareable checklist tracker for case documentation. Define the categories of documents a case needs, set each item's status as it moves through the case, and copy a live status summary showing what's done, what's rejected, and what's outstanding.

Each item has three states — **not collected**, **received**, and **rejected** — rather than a simple checkbox. Rejected is kept separate from not-collected on purpose: it means the customer *did* submit something, but it wasn't acceptable, so the write-up reads as "please resend this specific item" instead of a generic, confusing re-request.

Two simulated actions are available once something needs follow-up: **Send Reminder** (represents emailing the customer) and **Flag for CS Call** (represents asking a human teammate to call instead). Both require an explicit confirmation step before "sending," and both are simulated — this is a demo with no backend, so nothing is actually emailed or dispatched.

Built so the status can be shared with someone outside the investigation — e.g., a customer service rep — so they can answer "what's still needed from the customer?" without repeatedly pulling the investigator away from casework.

No fraud logic, no scoring, no prescribed methodology — just a tracking utility for a checklist you define yourself. Includes a browser-based live demo (`index.html`, linked above) that runs entirely client-side; nothing is saved, uploaded, or sent anywhere. The "Copy Shareable Summary" text always reflects the current state of the checklist — there's no separate generate step.

## Other tools in this series

- [Case Calculator](https://biancabcarlson.github.io/Case-Calculator/)
- [Report Template Filler](https://biancabcarlson.github.io/Report-Template-Filler/)
- [OSINT Tool](https://biancabcarlson.github.io/OSINT-Tool/)
- [Case Doc Tracker](https://biancabcarlson.github.io/Case-Doc-Tracker/) *(this repo)*
- [Entity Name Matcher](https://biancabcarlson.github.io/Entity-Name-Matcher/)
- [Case Timeline Builder](https://biancabcarlson.github.io/Case-Timeline-Builder/)
