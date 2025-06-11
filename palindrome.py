import datetime

def est_palindrome(texte):
    texte_filtre = ''.join(c.lower() for c in texte if c.isalnum())
    return texte_filtre == texte_filtre[::-1]

def miroir(texte):
    return texte[::-1]

def salutation_bonjour():
    heure = datetime.datetime.now().hour
    if 5 <= heure < 18:
        return "Bonjour !"
    else:
        return "Bonsoir !"

def salutation_au_revoir():
    heure = datetime.datetime.now().hour
    if 5 <= heure < 18:
        return "Au revoir, bonne journée !"
    else:
        return "Au revoir, bonne soirée !"

def main():
    print(salutation_bonjour())
    print("Saisissez un mot ou une phrase (ou tapez 'exit' pour quitter).")
    while True:
        entree = input("> ")
        if entree.lower() == "exit":
            print(salutation_au_revoir())
            break
        print(miroir(entree))
        if est_palindrome(entree):
            print("Bien dit !")

if __name__ == "__main__":
    main()


