# Documents Folder

**🔗 Live demo:** https://biancabcarlson.github.io/Case-Doc-Tracker/

A lightweight, shareable checklist tracker for case documentation. Define the categories of documents a case needs, set each item's status as it moves through the case, and copy a live status summary showing what's done, what's rejected, and what's outstanding.

Each item has three states — **not collected**, **received**, and **rejected** — rather than a simple checkbox. Rejected is kept separate from not-collected on purpose: it means the customer *did* submit something, but it wasn't acceptable, so the write-up reads as "please resend this specific item" instead of a generic, confusing re-request.

Once an item is marked **Received** or **Rejected**, a small eye icon appears next to it that opens an example document in a popup (a filler ID, statement, or similar — this is a demo with no real file storage, so nothing is an actual uploaded file). Any item can also be removed entirely with the **✕** icon next to it — both icons sit on the same row as the document name, with enough space between the eye and the ✕ that they're easy to tell apart and hard to hit by accident.

Made a mistake? **Undo last change** reverses the most recent add, remove, or status change — handy if a stray click on the ✕ removes the wrong item.

Two simulated actions are available once something needs follow-up: **Send Reminder** (represents emailing the customer) and **Flag for CS Call** (represents asking a human teammate to call instead). Both ask "Are you sure...?" with an explicit confirmation step before "sending," and both are simulated — this is a demo with no backend, so nothing is actually emailed or dispatched. **Copy Summary** copies the same plain-text status summary shown on the page.

Built so the status can be shared with someone outside the investigation — e.g., a customer service rep — so they can answer "what's still needed from the customer?" without repeatedly pulling the investigator away from casework.

No fraud logic, no scoring, no prescribed methodology — just a tracking utility for a checklist you define yourself. Includes a browser-based live demo (`index.html`, linked above) that runs entirely client-side; nothing is saved, uploaded, or sent anywhere.

### Case Role

Rejecting a document is a judgment call, not routine tracking, so it's gated to the **Investigator** or **Manager** role — pick one from the selector at top right (shared across the suite via `localStorage`, `investigatorSuiteRole`). As **Analyst**, the Rejected button is disabled with a tooltip rather than hidden, so it's still clear the option exists. **Received** and **Not collected** stay open to every role, since those just record what arrived rather than judge it.

This is a browser-only, `localStorage`-based check — it demonstrates the access pattern, not a real backend permission system, and `case_doc_tracker.py` (the CLI reference) does not currently enforce the same rule.

### Case Activity

Rejecting a document logs an entry to a shared "Case Activity" feed (`investigatorSuiteActivity` in `localStorage`), visible in the sidebar here and also readable by other tools in the suite — e.g. a fraud flag resolved in the Simulated Account tool shows up in this feed without opening that tool. It updates live across open tabs.

### Privacy Mode

The "🔒 Privacy Mode" toggle (top right, shared across the suite via `localStorage`) is present here for consistency with the other tools, though this tracker's checklist items don't currently carry PII of their own.

## Other tools in this series

- [Case Calculator](https://biancabcarlson.github.io/Case-Calculator/)
- [Report Template Filler](https://biancabcarlson.github.io/Report-Template-Filler/)
- [OSINT Tool](https://biancabcarlson.github.io/OSINT-Tool/)
- [Documents Folder](https://biancabcarlson.github.io/Case-Doc-Tracker/) *(this repo)*
- [Entity Name Matcher](https://biancabcarlson.github.io/Entity-Name-Matcher/)
- [Case Timeline Builder](https://biancabcarlson.github.io/Case-Timeline-Builder/)
