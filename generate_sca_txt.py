import json

with open("sca_report.json") as f:
    data = json.load(f)

with open("sca_report.txt", "w") as f:
    for vuln in data.get("vulnerabilities", []):
        f.write(f"CVE: {vuln['cve']}, Severity: {vuln['severity']}\n")
