import json

with open("sca_report.json") as f:
    data = json.load(f)

critical_found = any(v['severity'] == "high" for v in data.get("vulnerabilities", []))

if critical_found:
    print("critical vulnerabilities detected")
else:
    print("No critical vulnerabilities detected")
