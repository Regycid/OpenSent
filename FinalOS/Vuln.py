import requests

#Ouvre le fichier de versions et cree celui de vulnerabilites
with open("version.txt", "r") as file, open("vulns.txt", "w") as output_file:
    output_file.write(f"Package,Version,CVE,Severity\n")
    print(f"Package,Version,CVE,Severity")    
    for line in file:
        #Separe les lignes en champs et verifie qu'il y en a 2
        package_info = line.strip().split(" ")
        if len(package_info) < 2:
            print(f"Paquet invalide: {line}")
            continue

        #Passe le nom et la version de paquet dans les variables pour les remplacer dans l'url MITRE
        package_name = package_info[0]
        package_version = package_info[-1]
        url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?keyword={package_name} {package_version}&resultsPerPage=20"
        response = requests.get(url)

        #Verifie que la reponse est valide et exporte les resultats
        if response.status_code == 200 and any(char.isdigit() for char in package_version):
            results = response.json()["result"]["CVE_Items"]
            for result in results:
                cve_id = result["cve"]["CVE_data_meta"]["ID"]
                try:
                    cve_severity = result["impact"]["baseMetricV3"]["cvssV3"]["baseSeverity"]
                except KeyError:
                    cve_severity = None
                output_file.write(f"{package_name},{package_version},{cve_id},{cve_severity}\n")
                print(f"{package_name},{package_version},{cve_id},{cve_severity}")
        else:
            print(f"Pas d'information pour {package_info[0]} {package_info[1]}")
