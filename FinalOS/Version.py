import subprocess
import platform
import re

with open('version.txt','w') as versionFile:
#Ouvre le fichier des paquets et sépare chaque ligne et champs
    with open('installed_packages.txt', 'r') as f:
        for line in f:
            if platform.system() == 'Linux': 
#Si le 3eme champ existe, le defini dans version et ne conserve que les . et chiffres et affiche les infos
                fields = line.split()
                if len(fields) > 2:
                    version = fields[2]
                    version = version.split('+')[0]
                    version = ''.join([c for c in version if c.isdigit() or c == '.']) 
                    print(fields[1], ':'.join(fields), version, file = versionFile)

            elif platform.system() == 'Windows':
                fields = re.split('\s{2,}', line)
                if len(fields) > 2:
                    version = fields[1]
#Affiche le nom du paquet et sa version 
                    
                    print(':'.join(fields[0:1]), version, file = versionFile)
subprocess.run(["python3", "Vuln.py"])