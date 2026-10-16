"""Records the Python / platform environment as evidence (environment_evidence.json)."""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import platform
import sys

ROOT = Path(__file__).resolve().parents[2]

evidence = {
    "recorded_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "python_version": sys.version,
    "python_executable": sys.executable,
    "implementation": platform.python_implementation(),
    "platform": platform.platform(),
    "machine": platform.machine(),
    "runner": "GitHub Actions" if os.getenv("GITHUB_ACTIONS") == "true"
              else ("Google Colab" if "COLAB_RELEASE_TAG" in os.environ else "local"),
    "git_commit": os.getenv("GITHUB_SHA", "n/a (not running in GitHub Actions)"),
    "dependencies": "Python standard library only (see requirements.txt)",
    "repository_root": str(ROOT),
}
(ROOT / "environment_evidence.json").write_text(json.dumps(evidence, indent=2), encoding="utf-8")
print(json.dumps(evidence, indent=2))
