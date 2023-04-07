import subprocess

subprocess.run(["python3", "banner.py"])

def program1():
    print("Detection des paquets")
    subprocess.run(["python3", "Paquets.py"])

def program2():
    print("Analyse des CVE")
    subprocess.run(["python3", "Desc.py"])

def program3():
    print("Prevoir les scans")
    subprocess.run(["python3", "Auto.py"])

menu_options = {
    "1": program1,
    "2": program2,
    "3": program3,
    "q": exit
}

def display_menu():
    print("Que faire ?")
    print("1. Detection des CVE")
    print("2. Analyse des CVE")
    print("3. Programmer l'analyse")
    print("q. Quitter")

    print('-' * 100)
    print('')

    return input("Quel est votre choix: ")

while True:
    choice = display_menu()

    if choice in menu_options:
        menu_options[choice]()

    elif choice == "q":
        break

    else:
        print("Choix invalide.")
