"""Artifact quality gate for MCI1014 Assignment 1.

Checks that every required artifact exists, contains no placeholders, meets
the minimum counts in Table 1 of the assignment, and that the risk register,
traceability matrix, stories and architecture reference each other.
Standard library only. Exit code 0 = PASS, 1 = NEEDS WORK.
"""
from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[2]          # repository root
ART = ROOT / "artifacts"

REQUIRED = {
    "README.md": ROOT / "README.md",
    "problem statement": ART / "docs/01_problem_statement.md",
    "stakeholder map": ART / "docs/02_stakeholder_decision_map.md",
    "user stories": ART / "docs/03_user_stories_acceptance.md",
    "quality scenarios": ART / "docs/04_quality_scenarios.md",
    "architecture": ART / "docs/05_lightweight_architecture.md",
    "decision record": ART / "docs/06_decision_record.md",
    "risk register": ART / "risks/risk_register.csv",
    "traceability matrix": ART / "traceability/traceability_matrix.csv",
    "workflow": ROOT / ".github/workflows/artifact-check.yml",
}
PLACEHOLDERS = ["TODO-VERIFY", "Replace this row", "Insert your diagram here", "TBD"]
RISK_COLS = ["risk_id", "risk_description", "affected_stakeholder", "consequence",
             "likelihood", "impact", "control", "owner", "evidence"]
TRACE_COLS = ["trace_id", "problem_evidence", "requirement", "architecture_component",
              "risk_id", "control", "planned_verification"]
LEVELS = {"Low", "Medium", "High"}

problems = []
texts = {}


def need(cond, msg):
    if not cond:
        problems.append(msg)


# 1. presence, size, placeholders
for name, path in REQUIRED.items():
    rel = path.relative_to(ROOT)
    if not path.exists():
        problems.append(f"MISSING: {rel}")
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    texts[name] = text
    need(len(text) >= 200, f"TOO SHORT: {rel}")
    for marker in PLACEHOLDERS:
        need(marker not in text, f'PLACEHOLDER: {rel} contains "{marker}"')

# 2. content minimums from Table 1
ps = texts.get("problem statement", "")
for section in ["Problem description", "Problem owner", "Affected users", "Decision",
                "Observable value", "Possible harm", "Non-AI alternative"]:
    need(section.lower() in ps.lower(), f"PROBLEM: section '{section}' not found")

sm = texts.get("stakeholder map", "")
stakeholders = set(re.findall(r"\|\s*(S\d+)\s*\|", sm))
need(len(stakeholders) >= 3, f"STAKEHOLDERS: found {len(stakeholders)}, need at least 3")
for word in ["authority", "accountab", "oversight"]:
    need(word in sm.lower(), f"STAKEHOLDERS: '{word}' not described")

us = texts.get("user stories", "")
stories = set(re.findall(r"US-\d+", us))
need(len(stories) >= 3, f"STORIES: found {len(stories)}, need at least 3")
ac_rows = re.findall(r"\|\s*(AC-\d+)\s*\|([^|]+)\|([^|]+)\|([^|]+)\|", us)
need(len(ac_rows) >= 3, "STORIES: need Given/When/Then acceptance rows")
for ac, given, when, then in ac_rows:
    need(all(x.strip() for x in (given, when, then)), f"STORIES: {ac} has an empty Given/When/Then cell")
    need(re.search(r"\d", then) is not None, f"STORIES: {ac} 'Then' has no measurable number")

qs = texts.get("quality scenarios", "")
scen = re.findall(r"\|\s*(QS-\d+)\s*\|\s*\**([^|*]+)", qs)
need(len(scen) >= 4, f"QUALITY: found {len(scen)} scenarios, need at least 4")
need(any("human" in a.lower() for _, a in scen), "QUALITY: no human-centred operation scenario")
need(len({a.strip().lower() for _, a in scen if 'human' not in a.lower()}) >= 3,
     "QUALITY: need at least 3 other quality attributes")
need("trade-off" in qs.lower(), "QUALITY: trade-off decision missing")

arch = texts.get("architecture", "")
components = set(re.findall(r"ARCH-\d+", arch))
need(len(components) >= 4, "ARCHITECTURE: fewer than 4 ARCH components")
need("```mermaid" in arch, "ARCHITECTURE: diagram (mermaid) missing")
need("oversight" in arch.lower(), "ARCHITECTURE: human oversight points missing")
need("rationale" in arch.lower(), "ARCHITECTURE: design rationale missing")


# 3. CSV checks
def read_csv(name, cols, minimum):
    path = REQUIRED[name]
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        need(reader.fieldnames == cols, f"COLUMNS: {name} must be {cols}")
        rows = list(reader)
    need(len(rows) >= minimum, f"ROWS: {name} has {len(rows)}, needs at least {minimum}")
    for i, row in enumerate(rows, start=2):
        if None in row or any(v is None or not str(v).strip() for v in row.values()):
            problems.append(f"INCOMPLETE: {name} row {i} (empty cell or extra comma)")
    return rows


risks = read_csv("risk register", RISK_COLS, 4)
traces = read_csv("traceability matrix", TRACE_COLS, 4)

for r in risks:
    for col in ("likelihood", "impact"):
        need(r.get(col, "").strip() in LEVELS, f"RISK: {r.get('risk_id')} {col} must be Low/Medium/High")

# 4. cross-references (evidence chain)
risk_ids = {r["risk_id"].strip() for r in risks if r.get("risk_id")}
traced_risks = {r["risk_id"].strip() for r in traces if r.get("risk_id")}
traced_text = " ".join(" ".join(v for v in r.values() if v) for r in traces)
for rid in sorted(risk_ids - traced_risks):
    problems.append(f"TRACE: risk {rid} is not in the traceability matrix")
for rid in sorted(traced_risks - risk_ids):
    problems.append(f"TRACE: matrix refers to unknown risk {rid}")
for cid in sorted(set(re.findall(r"ARCH-\d+", traced_text)) - components):
    problems.append(f"TRACE: matrix refers to unknown component {cid}")
for sid in sorted(stories):
    need(sid in traced_text, f"TRACE: story {sid} is not in the traceability matrix")
for qid, _ in scen:
    need(qid in traced_text, f"TRACE: scenario {qid} is not in the traceability matrix")

if problems:
    print("NEEDS WORK")
    for p in problems:
        print("-", p)
    sys.exit(1)

print("PASS: all required artifacts meet the completeness and traceability checks")
print(f"  stakeholders={len(stakeholders)} stories={len(stories)} acceptance_criteria={len(ac_rows)} "
      f"scenarios={len(scen)} components={len(components)} risks={len(risks)} traces={len(traces)}")
