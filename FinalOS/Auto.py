from crontab import CronTab
import os

#Importe le dossier actuel dans une variable
cwd = os.getcwd()
paquets_path = os.path.join(cwd, "Paquets.py")

#Demande à l'utilisateur à quelle heure lancer le script(ex: "17:30")
time_of_day = input("A quelle heure lancer le scan automatique? (HH:MM): ")

#Cree la tache Cron
command = f"crontab -l | {{ cat; echo '{time_of_day} * * * * /usr/bin/python3 {paquets_path}'; }} | crontab -"
os.system(command)

#Confirme la bonne creation du crontab
print(f"La tache cron {paquets_path} a {time_of_day} est creee")

