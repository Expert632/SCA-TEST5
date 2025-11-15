import json
from pathlib import Path

report_file = Path("sca_report.json")

# Si le fichier n'existe pas
if not report_file.exists():
    print("WARNING: sca_report.json not found. Creating empty TXT report.")
    with open("sca_report.txt", "w") as f:
        f.write("No vulnerabilities found.\n")
    exit(0)

# Lecture sécurisée du fichier JSON
try:
    with report_file.open() as f:
        content = f.read().strip()
        if not content:
            data = []
        else:
            data = json.loads(content)
except json.JSONDecodeError:
    print("WARNING: sca_report.json is not valid JSON. Creating empty TXT report.")
    data = []

# Extraire les vulnérabilités
vulns = []
if isinstance(data, list):
    vulns = data
elif isinstance(data, dict):
    vulns = data.get("vulnerabilities", data.get("issues", []))

# Générer le fichier TXT
with open("sca_report.txt", "w") as f:
    if not vulns:
        f.write("No vulnerabilities found.\n")
    else:
        for v in vulns:
            cve = v.get("cve") or v.get("identifier") or "N/A"
            sev = (
                v.get("severity")
                or v.get("severity_rating")
                or v.get("vulnerability_severity")
                or "unknown"
            )
            pkg = v.get("package_name") or v.get("dependency") or "unknown"
            version = v.get("affected_version") or v.get("version") or "unknown"
            f.write(f"Package: {pkg} | Version: {version} | CVE: {cve} | Severity: {sev}\n")

print("TXT report generated successfully: sca_report.txt")
