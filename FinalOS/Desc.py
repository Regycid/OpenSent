import requests
import csv
import matplotlib.pyplot as plt

# Ouvrir le fichier CSV
with open('vulns.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    packages = {}
    
    # Lire les données ligne par ligne
    for row in csv_reader:
        package = row['Package']
        cve = row['CVE']
        
        # Ajouter les cves pour chaque paquet
        if package not in packages:
            packages[package] = 1
        else:
            packages[package] += 1
    
    # Créer le diagramme à barres
    plt.bar(packages.keys(), packages.values())
    plt.xlabel('Paquets')
    plt.ylabel('Nombre de CVEs')
    plt.title('Reporting de vulnérabilités')
    plt.savefig('plot.png')
    plt.show()


# Lecture du fichier texte
with open('vulns.txt', 'r') as file:
    data = file.readlines()

# Traitement des données
rows = []
for line in data:
    row = line.strip().split(',')
    rows.append(row)

# Écriture des données dans le fichier CSV
with open('packages.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open('packages.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=',')
    data = [row for row in reader]

# Comptage des vulnérabilités par niveau de gravité
severity_counts = {}
for row in data:
    severity = row['Severity']
    if severity in severity_counts:
        severity_counts[severity] += 1
    else:
        severity_counts[severity] = 1

# Affichage du graphique

colors = {'CRITICAL': 'red', 'HIGH': 'orange', 'MEDIUM': 'yellow', 'LOW': 'green', 'None': 'gray'}
fig, ax = plt.subplots()
ax.bar(severity_counts.keys(), severity_counts.values(), color=[colors[s] for s in severity_counts.keys()])
ax.set_xlabel('Niveau de gravité')
ax.set_ylabel('Nombre de vulnérabilités')
ax.set_title('Répartition des vulnérabilités par niveau de gravité')
plt.show()
plt.savefig('graphique.png')




#recupere les informations de la CVE sous forme de Json
def get_cve_info(cve_id):
    url = f"https://services.nvd.nist.gov/rest/json/cve/1.0/{cve_id}"
    response = requests.get(url)
    if response.status_code == 200:
        cve_info = response.json()['result']['CVE_Items'][0]['cve']
        return cve_info
    else:
        return None

#extrait la description et l'affiche si le champ n'est pas vide
def descriptions(cve_id):
    cve_info = get_cve_info(cve_id)
    if cve_info is not None:
        description = cve_info['description']['description_data'][0]['value']
        print(f"{description}")
    else:
        print(f"Aucune information trouvee pour {cve_id}.")

#Lis les CVE dans le fichier
with open('vulns.txt') as f:
    for line in f:
        fields = line.strip().split(',')
        if len(fields) >= 3:
            cve_id = fields[2]
            cve_sev = fields[3]
            print('-' * 50)
            print(f"{cve_id} (severity : {cve_sev}): ")
            descriptions(cve_id)
            print('-' * 50)
            print(' ')
        else:
            print(f"{len(fields)} champs manquants: {line.strip()}")

