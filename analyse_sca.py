import json
from pathlib import Path
import sys

report_file = Path("sca_report.json")

if not report_file.exists():
    print("No SCA report found. Exiting.")
    sys.exit(0)

try:
    with report_file.open() as f:
        content = f.read().strip()
        if not content:
            data = []
        else:
            data = json.loads(content)
except json.JSONDecodeError:
    data = []

vulns = []
if isinstance(data, list):
    vulns = data
elif isinstance(data, dict):
    vulns = data.get("vulnerabilities", data.get("issues", []))

critical_found = False
for v in vulns:
    severity = (
        v.get("severity")
        or v.get("severity_rating")
        or v.get("vulnerability_severity")
        or ""
    )
    if str(severity).lower() in ("critical", "high"):
        critical_found = True
        break

if critical_found:
    print("critical vulnerabilities detected")
else:
    print("No critical vulnerabilities detected")
