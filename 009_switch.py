"""
Les choix (switch / case dans Java) 

Il n'existe pas d'instruction 'switch / case' dans Java, pour effectuer des choix, il existe deux possibilités : 
    -> Recourir aux conditions if / else 
    -> Recourir aux dictionnaires 

Éditeur : Laurent REYNAUD 
Date : 06-09-2020 
"""


def creer_compte():
    print("Création d'un compte")
    compte = {}
    print("Numéro de compte :")
    cle = input()
    print("Date de création du compte :")
    valeur_date = input()
    print("Libellé de création du compte :")
    valeur_libelle = input()
    print("Montant du compte créé :")
    valeur_montant = float(input())
    compte[cle] = valeur_date, valeur_libelle, valeur_montant
    return


def afficher_compte():
    return


while True:
    print("MENU GENERAL")
    print("1- Créer un compte")
    print("2- Afficher tous les comptes")
    print("3- Rechercher un compte")
    print("4- Supprimer un compte")
    print("5- Saisir des opérations")
    print("6- Afficher les opérations")
    print("7- Sauvegarder")
    print("8- Ouvrir un fichier")
    print("9- Sortir")
    print()
    print("Votre choix ? ")
    choix_saisi = int(input())

    if choix_saisi == 1:
        creer_compte()
    if choix_saisi == 2:
        afficher_compte()
    if choix_saisi == 9:
        print("Merci et à la prochaine !")
        quit()
