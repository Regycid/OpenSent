import platform
import requests
import json

OS = platform.system()
Version = platform.release()
Architecture = platform.architecture()
strArchitecture = str(Architecture)
Nom_de_la_machine = platform.node()
Type_Machine = platform.machine()
MaJ = platform.version()

Informations = [Nom_de_la_machine,':', OS, Version, MaJ , strArchitecture]

def get_vulns_for_os(os_name, os_version):
    base_url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
    query_params = {
        "keyword": os_name + " " + os_version,
        "resultsPerPage": 100,
        "startIndex": 0,
        "cvssSeverity": "HIGH,MEDIUM,LOW"
    }
    response = requests.get(base_url, params=query_params)
    if response.status_code != 200:
        raise Exception("Failed to retrieve vuln data from NVD API")

    vulns = []
    data = json.loads(response.content)
    for result in data.get("result", {}).get("CVE_Items", []):
        cve_id = result.get("cve", {}).get("CVE_data_meta", {}).get("ID")
        cvss_score = result.get("impact", {}).get("baseMetricV3", {}).get("cvssV3", {}).get("baseScore")
        description = result.get("cve", {}).get("description", {}).get("description_data", [])[0].get("value")
        vulns.append({
            "cve_id": cve_id,
            "cvss_score": cvss_score,
            "description": description
        })

    return vulns

vulns = get_vulns_for_os(OS, Version)

CVE = []  
for vuln in vulns:
    ID = str(vuln["cve_id"])
    Score = str(vuln["cvss_score"])
    CVE.append(ID)
    CVE.append(Score)


with open ('information.txt', 'w') as f:
    f.write(' '.join(Informations))
    f.write("\n")
    f.write(str(CVE))
