# 01 – AI System Problem Statement

**Student:** Anawin Chorungreang A/L E Phwan  
**Proposed application:** Use-First Food Assistant (household food-waste reduction)

## Problem description

In my household (4 people sharing one fridge, Kelantan), perishable food is regularly thrown away because nobody knows what is close to spoiling. Fresh vegetables, bread, opened milk and leftovers are pushed to the back of the fridge, forgotten, and discovered only after they have spoiled. At the same time we keep buying the same items again at the weekend shop because there is no shared view of what is already at home. Hot and humid weather shortens the life of fresh produce, and many of these items (loose vegetables, leftovers, opened packs) have **no printed expiry date** at all.

## Evidence of the problem (own records)

| Date | Item thrown away | Reason | Est. cost (RM) |
|---|---|---|---|
| 21 February 2026 | Pack of cheese slices (most of the pack) | Not finished in time – mould | 5.00 |
| 28 September 2026 | Opened milk | Not finished after opening – left in the fridge | 6.00 |
| 12 October 2026 | Bread (half loaf) | Mould – a second loaf was bought before the first was finished | 2.50 |
| 12 October 2026 | Cooked rice leftovers | Left more than 2 days – unsure if still safe | 1.50 |

**Summary:** 4 recorded incidents, about **RM 15.00** of food discarded. These are the incidents I can date with certainty; smaller items (e.g. vegetables) were not recorded, so the real amount is likely higher. The incidents show the three causes the application must address: **forgotten opened items** (milk, cheese), **duplicate purchases** (bread) and **uncertainty about safety** (cooked rice).

**Baseline for the pilot:** before the pilot starts, every discarded item is logged for 7 days (date, item, reason, cost). This baseline week is the reference for the value targets below.

## Problem owner

**Household grocery planner (me, Anawin)** – decides what to buy each weekend and what to cook during the week, and is accountable for the household food budget.

## Affected users

- Household members (family / housemates) who cook, eat and throw away food.
- A household member with a food allergy, who could be harmed by an unsafe recipe suggestion.
- The app maintainer (me, in a developer role) who is responsible for the AI model and the household's data.

## Decision or task to support

1. **Daily:** which items should be cooked or eaten *first* (use-first list), and which items need a *safety check* before use.
2. **Weekly:** how much of each perishable item to buy at the weekend shop.

The application only **recommends**. A person always makes the final decision to eat, cook, buy or discard.

## Observable value (pilot of 4 weeks, compared with the baseline week)

- Number of perishable items discarded per week reduced by **at least 30%**.
- At least **80%** of items shown on the use-first list are marked "used" before their estimated date.
- **0** duplicate purchases of an item that is already in stock and not yet due (checked from the inventory log).
- Logging an item as used or discarded takes **2 taps or fewer**.

## Possible harm

- **Food safety:** if the app over-estimates shelf life, someone may eat spoiled food (e.g. cooked rice, chicken, dairy) and become ill.
- **Allergy:** a recipe suggestion may include an allergen for a household member.
- **Money:** a wrong quantity suggestion causes over-buying (more waste) or under-buying (extra trips).
- **Privacy:** receipt photos show the store, time and partial card details.
- **Over-reliance:** members stop using their own judgement ("the app said it was fine").

## Non-AI alternative

A **fridge whiteboard / shared spreadsheet** listing every item with its purchase date and printed expiry date, kept in first-in-first-out order, plus a phone calendar reminder every evening and a fixed weekly shopping list.

## Trade-off: why an AI-enabled application may be appropriate

| Need | Non-AI alternative | AI-enabled option |
|---|---|---|
| Packaged items with a printed date | Works well (simple, reliable) | Not needed – rules handle this |
| Fresh produce, opened packs, leftovers (no printed date) | Cannot estimate; relies on memory | Estimates remaining days from category, storage, purchase date and our own discard history |
| How much to buy | Fixed list ignores how fast we really eat things | Learns weekly consumption and suggests quantities |
| Effort to keep updated | Manual writing; abandoned after a few days | Receipt scan fills the list; 2-tap logging |

**Recommendation:** a **hybrid** design. Deterministic rules (printed dates, fixed conservative limits for high-risk foods, allergen filter) stay in control of safety; the AI is used **only** where the non-AI option fails – estimating days left for undated items and suggesting quantities. If the 4-week pilot does not reach the 30% reduction target, the household returns to the non-AI whiteboard method, which is also the fallback whenever the AI is unavailable.
