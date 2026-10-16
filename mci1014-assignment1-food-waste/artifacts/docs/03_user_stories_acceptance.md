# 03 – User Stories and Acceptance Criteria

## US-01 – Household grocery planner (S1)

**As the** household grocery planner, **I want** a daily use-first list and a weekly shopping-quantity suggestion that I must approve, **so that** we cook food before it spoils and stop buying duplicates.

**Value link:** discarded items per week reduced by at least 30%; 0 duplicate purchases.

| AC | Given | When | Then (observable / measurable) |
|---|---|---|---|
| AC-01 | the inventory contains items with an estimated 2 days or fewer remaining | the daily reminder runs at 8:00 pm | 100% of those items appear on the use-first list, sorted by days left (fewest first), each showing estimated date, confidence and one-line reason; notification received by 8:05 pm |
| AC-02 | an item has a printed expiry date | its date is calculated | the displayed date equals the printed date and is **never later** than it (verified by unit test on 20 dated items: 0 later) |
| AC-03 | at least 4 weeks of consumption history exist | the planner opens the shopping suggestion on Saturday | every perishable shows a suggested quantity; an item already in stock with 3 or more days left is shown as "Already have"; the list is saved **only** after the planner taps Approve (0 items saved or ordered automatically) |

## US-02 – Household member (S2)

**As a** household member, **I want** to see which items need a safety check and log what I use or throw away in two taps, **so that** I do not eat spoiled or unsafe food and the record stays accurate.

**Value link:** prevents food-safety and allergy harm; accurate log feeds the model.

| AC | Given | When | Then (observable / measurable) |
|---|---|---|---|
| AC-04 | an item is in a high-risk category (raw meat, seafood, cooked rice, dairy, leftovers) **or** its AI confidence is below 0.70 | the item is displayed | it is labelled "Check before use", shows the fixed conservative rule date (not the AI date), and the word "safe" never appears (0 occurrences in UI text tests) |
| AC-05 | a member opens an item | they tap "Used" or "Discarded" (+ reason) | the event is saved in 2 taps or fewer and appears in the household log within 5 seconds with member name and time |
| AC-06 | a member's profile lists a peanut allergy | recipe ideas are generated for the use-first list | 0 suggested recipes contain peanut ingredients (verified with a test set of 30 recipes incl. 5 with peanut) |

## US-03 – App maintainer / model owner (S3)

**As the** app maintainer, **I want** a weekly evaluation that compares estimated dates with what actually happened, **so that** I can detect and stop unreliable estimates before they cause harm.

**Value link:** keeps AI estimates trustworthy; supports the release and rollback decision.

| AC | Given | When | Then (observable / measurable) |
|---|---|---|---|
| AC-07 | at least 4 weeks of used/discarded events exist | the evaluation job runs on Sunday 9:00 pm | a report shows, per category, mean absolute error (days) and the "spoiled earlier than estimated" rate, delivered by 9:30 pm; 100% of recommendations in the log carry a model version |
| AC-08 | the "spoiled earlier than estimated" rate for any category is above 10% | the weekly evaluation completes | that category is switched to rules-only mode automatically and the maintainer is notified within 24 hours; the switch is recorded in the decision log |
