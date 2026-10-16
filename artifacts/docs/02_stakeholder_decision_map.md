# 02 – Stakeholder and Decision Map

| ID | Stakeholder | Need or concern | Decision authority | Accountability | Human oversight responsibility | Possible harm to them |
|---|---|---|---|---|---|---|
| S1 | **Household grocery planner** (Anawin – problem owner) | Know what to cook first and how much to buy, so less food and money is wasted | **Final** decision on the weekly shopping list (approves or edits every AI quantity); decides what is cooked; can switch any food category to "rules only" | Accountable for the household food budget and for approving what is bought | Confirms items extracted from receipts before they enter the inventory; approves the shopping list – nothing is bought automatically; reviews the weekly waste report | Over- or under-buying; wasted money; loss of trust if the list is wrong |
| S2 | **Household members** (family / housemates, incl. one member with a peanut allergy) | Easy way to see what to eat first; never be told spoiled or unsafe food is fine | Decides whether to **eat or discard** an item after their own look/smell check; can override any estimate ("discard now" / "still good"); sets their own allergen profile | Accountable for checking food before eating and for logging what they use or throw away | Performs the safety check on every item marked "Check before use"; reports wrong estimates with the override button | Food poisoning from an over-estimated item; allergic reaction from an unsafe recipe |
| S3 | **App maintainer / model owner** (Anawin, developer role) | Shelf-life and quantity estimates remain accurate; data is kept private | Decides when a model version is released, rolled back, or a category is switched to rule-only mode; decides what data is kept | Accountable for model quality, data privacy and fixing reported errors | Reviews the weekly evaluation report every Sunday; investigates every "spoiled earlier than estimated" report within 48 hours | Releasing a model that is unsafe for a food category; privacy breach of receipt data |
| S4 | **External service providers** (receipt OCR service, push-notification service) | Receive correctly formatted requests | None over household decisions | Accountable for their service availability under their terms | None – their output is always validated by the app and confirmed by S1 | – (they are a dependency, not an affected party) |

## Decision rules (who decides what)

| Decision | Recommended by | Decided by | Rule |
|---|---|---|---|
| Is this item safe to eat? | App shows "Check before use" only | **S2 – the person eating it** | The app never displays "safe". High-risk foods always use the fixed conservative limit. |
| What to cook first today | AI use-first list | S1 / S2 | Recommendation only; members may ignore or override. |
| How much to buy this week | AI quantity suggestion | **S1** | 0 items saved to the shopping list without S1 approval. |
| Release / roll back a model; switch category to rules-only | Weekly evaluation report | **S3** | Automatic switch to rules-only if "spoiled early" rate > 10% for a category; S3 decides when to re-enable. |
