from crontab import CronTab
import os
import platform
import subprocess

#Importe le dossier actuel dans une variable
cwd = os.getcwd()
paquets_path = os.path.join(cwd, "Paquets.py")

#Demande à l'utilisateur à quelle heure lancer le script(ex: "8am")
heure = input("A quelle heure lancer le scan automatique? (XXam/pm): ")

#Cree la tache Cron
if platform.system() == 'Linux': 
    command = f"crontab -l | {{ cat; echo '{heure} * * * * /usr/bin/python3 {paquets_path}'; }} | crontab -"
    os.system(command)

elif platform.system() == 'Windows':
    ps_command1 = fr"$action = New-ScheduledTaskAction -Execute Paquets.py -Argument {paquets_path}"
    ps_command2 = fr"$trigger = New-ScheduledTaskTrigger -Daily -At {heure}"
    ps_command3 = fr"Register-ScheduledTask -TaskName Scan -Action $action -Trigger $trigger"
    ps_commands = f"{ps_command1}; {ps_command2}; {ps_command3}"
    print(ps_commands)
    subprocess.run(["powershell", "-Command", ps_commands])



#Confirme la bonne creation du crontab
print(f"La tache {paquets_path} a {heure} est creee")