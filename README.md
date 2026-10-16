# MCI1014 Assignment 1 – Use-First Food Assistant

**Course:** MCI1014 Artificial Intelligence in Software Engineering (Session 2025/2026 II)  
**Student:** Anawin Chorungreang A/L E Phwan · **Student ID:** KCA26006 
**Submission:** Friday 23 October 2026, 12:00 PM via KALAM

## 1. Case study

**Problem:** my household (4 people, one shared fridge, Kelantan) regularly throws away perishable food – vegetables, bread, opened milk and leftovers – because nobody knows what is close to spoiling, and we buy duplicates at the weekend shop.

**Recommendation:** a *hybrid* Use-First Food Assistant. Deterministic safety rules (printed dates, conservative limits for high-risk foods, allergen filter) stay in control; AI is used only to estimate days left for undated items and to suggest weekly quantities. Every decision to buy, eat or discard stays with a person. The non-AI alternative (fridge whiteboard + FIFO + calendar reminder) is kept as the fallback.

## 2. Where to find each artifact

```
README.md                                  case, run instructions, AI-use declaration
requirements.txt                           no third-party packages (standard library only)
.github/workflows/artifact-check.yml       automated quality gate (GitHub Actions)
artifacts/
  docs/01_problem_statement.md             problem, owner, users, decision, value, harm, non-AI option
  docs/02_stakeholder_decision_map.md      4 stakeholders, authority, accountability, oversight
  docs/03_user_stories_acceptance.md       3 stories, 8 Given-When-Then criteria
  docs/04_quality_scenarios.md             5 scenarios + trade-off decision
  docs/05_lightweight_architecture.md      diagram, components, oversight points, rationale
  docs/06_decision_record.md               ADR-001 (hybrid, recommend-and-confirm)
  risks/risk_register.csv                  7 risks
  traceability/traceability_matrix.csv     8 trace rows (evidence -> requirement -> component -> risk -> control -> verification)
  tools/environment_check.py               records Python / platform evidence
  tools/validate_artifacts.py              local / Colab / CI validator
```

> `.github/` sits at the repository root (not inside `artifacts/`) because GitHub Actions only reads workflows from there.

## 3. How to run the checks

Requires Python 3.10 or newer. No `pip install` is needed.

**Local (Windows / macOS / Linux)** – from the repository folder:

```bash
python artifacts/tools/environment_check.py
python artifacts/tools/validate_artifacts.py
```

Expected last line: `PASS: all required artifacts meet the completeness and traceability checks`. The first command writes `environment_evidence.json`.

**Google Colab** – new notebook, one cell:

```python
!git clone https://github.com/anawin8-oss/mci1014-assignment1-food-waste.git
%cd mci1014-assignment1-food-waste
!python artifacts/tools/environment_check.py
!python artifacts/tools/validate_artifacts.py
```

**GitHub Actions** – every push runs the `artifacts-check` workflow. Open the **Actions** tab: a green tick means the validator passed on that commit. The run also uploads `quality-gate-evidence` (environment JSON + validation output).

**What the validator checks:** all files present; no placeholders; Table 1 minimums (≥3 stakeholders, ≥3 stories with measurable Given-When-Then, ≥4 quality scenarios incl. human-centred, architecture with diagram, oversight and rationale, ≥4 risks with Low/Medium/High ratings); and that every risk, story, scenario and component is linked in the traceability matrix. A green run proves completeness and consistency, not that the engineering judgement is correct.

## 4. Generative AI use declaration

**Tool:** Claude (Anthropic), Claude desktop app (Cowork mode), 14–16 October 2026.
**How it was used:** as a drafting assistant working from the official Assignment 1 brief and rubric. The problem, evidence, personal context and all final decisions are mine; every AI output below was reviewed before it was kept.

| # | Date | Prompt (accurate summary) | AI output | What I adopted / changed | Justification |
|---|---|---|---|---|---|
| 1 | 14 Oct | Asked for guidance on completing Assignment 1, using the brief and rubric in my course folder. | Summarised the task and rubric; asked me to choose a problem domain, a way of working and my GitHub experience. | I chose **food waste in my own household** and asked for drafts that I would review. | The problem is one I experience at home, so I can supply real evidence for it. |
| 2 | 14 Oct | Asked for draft artifacts (problem statement, stakeholder map, user stories, quality scenarios, architecture, ADR, risk register, traceability matrix) for that problem. | Drafts recommending a hybrid design: deterministic safety rules plus AI only for undated items and quantities. | Adopted the hybrid recommendation and structure. Replaced the example evidence with my own dated incidents (milk, cheese, bread, rice), set the location to Kelantan and added my details. | Rules-first design keeps food-safety decisions out of the AI; the AI is used only where the non-AI alternative fails. |
| 3 | 14 Oct | Asked for the validator, environment check and GitHub Actions workflow. | Extended the Week 2 validator with Table 1 minimum counts and cross-reference checks; workflow records the environment and uploads evidence. | Adopted. | The quality gate now checks traceability (every risk, story, scenario and component linked), not only that files exist. |
| 4 | 16 Oct | Asked to check my edits to the problem statement and README and align the other artifacts. | Reformatted my incidents into a dated table with a summary, added a 7-day baseline plan, and updated names in the stakeholder map and ADR. | Adopted after checking that the incident details match my records. | Keeps all artifacts consistent with my own evidence. |
| 5 | 16 Oct | Asked for help writing this declaration clearly and professionally. | Restructured the declaration into this table. | Adopted after confirming every row is accurate. | The assignment requires prompts, outputs and justification to be declared. |

**My own contribution:** selected the problem from my household's experience; supplied the waste incidents, costs and context; reviewed and edited the artifacts; created and maintained the GitHub repository and ran the automated quality gate.

## 5. Limitations

This is a proposal and quality gate, not a working app. Thresholds (0.70 confidence, 30% reduction, 10% spoiled-early rate) are initial targets to be confirmed in a 4-week pilot.
