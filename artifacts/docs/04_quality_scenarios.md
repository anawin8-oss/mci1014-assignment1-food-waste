# 04 – Quality Attribute Scenarios

| ID | Attribute | Source / Stimulus | Environment | Expected response | Measure / threshold | Rationale |
|---|---|---|---|---|---|---|
| QS-01 | **Human-centred operation** | AI estimate for an item has confidence below 0.70, or the item is high-risk (raw meat, seafood, cooked rice, dairy, leftovers) | Normal daily use | Item marked "Check before use" with conservative rule date and reason; member must choose "Use", "Discard" or "Still good"; overrides are logged | 100% of such items show the label; 0 UI texts say "safe"; 100% of overrides logged with member and time | The person eating the food remains the decision-maker for safety (harm: food poisoning) |
| QS-02 | **Reliability** | Daily 8:00 pm use-first reminder is due | Phone offline or notification service down | Reminder retried every 15 minutes for 2 hours; if still not delivered, an in-app banner appears on next open | At least 29 of 30 days delivered by 8:05 pm in the pilot; 0 days with neither notification nor banner | A missed reminder is exactly the original failure (forgotten food) |
| QS-03 | **Robustness** | Receipt line cannot be matched (abbreviation such as "KGKUNG 1KG", blurry photo, new product) | Weekly shop scanned | Line goes to a "Needs label" list for the planner; it is never guessed into the inventory | At least 90% of lines correctly matched on a test set of 20 own receipts; 100% of unmatched lines shown to the planner; 0 unconfirmed items in the inventory | OCR and item matching are error-prone; wrong items corrupt both the list and the training data |
| QS-04 | **Security / privacy** | Receipt photo contains store name, time and last 4 card digits | Receipt uploaded for OCR | Only item, quantity, price and date are kept; photo deleted after extraction; data visible only to household accounts | Photo deleted within 1 minute of extraction; audit after 24 h finds 0 stored images; 0 card digits in the database | Purchase data is personal; collecting the minimum needed reduces privacy harm |
| QS-05 | **Reproducibility** | Maintainer retrains the model weekly | Same data snapshot and random seed | Retraining produces the same model and the same estimates; model version, data snapshot date and seed are recorded | Two runs on the same snapshot give identical estimates for 100% of a 50-item test set; every recommendation carries a model version | Needed to investigate wrong estimates and to roll back safely |

## Trade-off decision

**Tension:** *Safety (conservative dates)* versus *waste reduction (longer, more accurate AI dates)*.

**Selected option:** For high-risk categories, the fixed conservative rule date is always used and the AI estimate is shown only as information. The AI date is used for low-risk produce and bread when confidence is 0.70 or higher.

**Quality protected:** Human-centred safety (QS-01) – nobody is told a risky food lasts longer than the conservative rule.

**Cost accepted:** Some high-risk food will be flagged earlier than necessary, so the waste reduction for those categories will be smaller than a pure AI approach could achieve.

**Key assumption:** Most of our waste is low-risk produce and bread, so the 30% reduction target can still be reached. *Check after week 2 of the pilot: if high-risk categories make up more than half of the discarded items, revisit this decision (ADR-001).*
