import json
import sys
from pathlib import Path

report_file = Path("sca_report.json")

if not report_file.exists():
    print("SCA report file 'sca_report.json' not found.")
    sys.exit(1)

with report_file.open() as f:
    data = json.load(f)

vulns = []

# Cas 1 : Safety renvoie directement une liste
if isinstance(data, list):
    vulns = data

# Cas 2 : Safety renvoie un objet avec une clé de type 'vulnerabilities' ou 'issues'
elif isinstance(data, dict):
    vulns = data.get("vulnerabilities", data.get("issues", []))

critical_found = False

for v in vulns:
    # Essayer différentes façons d'obtenir la sévérité
    severity = (
        v.get("severity")
        or v.get("severity_rating")
        or v.get("vulnerability_severity")
        or ""
    )
    severity = str(severity).lower()
    if severity in ("critical", "high"):
        critical_found = True
        break

if critical_found:
    print("critical vulnerabilities detected")
else:
    print("No critical vulnerabilities detected")
