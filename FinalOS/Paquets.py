import subprocess
import platform

#Declaration des variables pour les commandes à utiliser et le fichier d'export
linux_command = ['dpkg', '-l']
windows_command = ['powershell.exe',r'Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |  Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table -AutoSize']
output_file = 'installed_packages.txt'

#Verifie l'os et dirige le resultat des commandes dans output
if platform.system() == 'Linux':
    process = subprocess.Popen(linux_command, stdout=subprocess.PIPE)
elif platform.system() == 'Windows':
    process = subprocess.Popen(windows_command, stdout=subprocess.PIPE)
else:
    print('Unsupported platform')
    exit()

output, error = process.communicate()

#Ecriture de l'output dans le fichier défini
with open(output_file, 'w', encoding='cp1252') as packfile:
    packfile.write(output.decode('cp1252'))

subprocess.run(["python3", "Version.py"])