import datetime

def est_palindrome(texte):
    texte = ''.join(c.lower() for c in texte if c.isalnum())
    return texte == texte[::-1]

def salutation_au_revoir():
    heure = datetime.datetime.now().hour
    if 5 <= heure < 12:
        return "Au revoir, bonne matinée !"
    elif 12 <= heure < 18:
        return "Au revoir, bon après-midi !"
    elif 18 <= heure < 22:
        return "Au revoir, bonne soirée !"
    else:
        return "Au revoir, bonne nuit !"

def main():
    print("Bienvenue ! Saisissez un mot ou une phrase (ou tapez 'exit' pour quitter).")
    while True:
        entree = input("> ")
        if entree.lower() == "exit":
            print(salutation_au_revoir())
            break
        if est_palindrome(entree):
            print("Bien dit")
        else:
            print("Ce n'est pas un palindrome.")

if __name__ == "__main__":
    main()
