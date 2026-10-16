# 06 – Architecture Decision Record

## ADR-001: Hybrid "rules guard the AI" with recommend-and-confirm

**Status:** Accepted (14 Oct 2026)  
**Decider:** Anawin (S1 planner and S3 maintainer)

### Context

The household throws away perishable food every week (see 01_problem_statement.md). Many items have no printed date, and the right purchase quantity depends on how fast the household actually eats. Mistakes can cause food poisoning or allergic reactions, so safety must not depend on an uncertain estimate.

### Options considered

| Option | Description | Result |
|---|---|---|
| A. Non-AI only | Whiteboard / spreadsheet FIFO list with printed dates and calendar reminder | **Kept as fallback.** Simple and safe but cannot estimate undated items or adapt quantities; manual upkeep is usually abandoned. |
| B. Fully automatic AI | AI decides dates, marks food "safe/unsafe", and orders groceries automatically | **Rejected.** Unsafe for high-risk food; removes the human decision on eating and buying; mistakes cost money. |
| C. Hybrid (selected) | Rules handle printed dates, high-risk foods and allergens; AI only estimates undated low-risk items and suggests quantities; humans confirm at H1–H3 | **Selected.** |

### Decision

Option C. The Safety Rule Engine (ARCH-05) always overrides the AI model (ARCH-06). The AI provides recommendations with confidence and reason; items below 0.70 confidence or in high-risk categories are labelled "Check before use". Nothing is bought or discarded automatically.

### Consequences

- **Positive:** safety harms are controlled by deterministic rules; humans keep decision authority; a working non-AI fallback exists.
- **Negative / accepted:** less waste reduction on high-risk foods (conservative dates); the household must log used/discarded events for the model to learn; 4 weeks of data needed before quantity suggestions are useful.

### Review trigger

Revisit this ADR if (a) the pilot misses the 30% reduction target after 4 weeks, (b) the "spoiled early" rate exceeds 10% for any category for two consecutive weeks, or (c) high-risk items make up more than half of discarded items.
