import json
import sys
from pathlib import Path

report_file = Path("sca_report.json")

if not report_file.exists():
    print("SCA report file 'sca_report.json' not found.")
    sys.exit(1)

try:
    with report_file.open() as f:
        data = json.load(f)
except json.JSONDecodeError:
    print("sca_report.json is not a valid JSON file.")
    sys.exit(1)

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
