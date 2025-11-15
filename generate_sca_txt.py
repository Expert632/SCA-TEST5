import json
from pathlib import Path

report_file = Path("sca_report.json")

if not report_file.exists():
    print("ERROR: SCA report file 'sca_report.json' not found.")
    exit(1)

try:
    with report_file.open() as f:
        data = json.load(f)
except json.JSONDecodeError:
    print("ERROR: sca_report.json is not a valid JSON file.")
    exit(1)

vulns = []

if isinstance(data, list):
    vulns = data
elif isinstance(data, dict):
    vulns = data.get("vulnerabilities", data.get("issues", []))

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

            f.write(
                f"Package: {pkg} | Version: {version} | CVE: {cve} | Severity: {sev}\n"
            )
