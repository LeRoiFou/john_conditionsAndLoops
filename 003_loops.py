"""
Ce programme permet d'une part à l'utilisateur de crééer un mot de passe et d'autre part d'avoir 5 essais pour saisir 
le bon mot de passe 
Éditeur : Laurent REYNAUD 
Date : 19-07-2020 
"""

mdp_cree = input("Mot de passe à définir : ")
mdp_saisie = ""
nbresaisie = 5

while mdp_saisie != mdp_cree and nbresaisie > 0:
    mdp_saisie = input("Mot de passe : ")
    nbresaisie -= 1
    if mdp_saisie != mdp_cree:
        print("Erreur de saisie, vous n'avez plus que", nbresaisie, "essais")

if mdp_saisie != mdp_cree:
    print("Interdiction d'accéder au fichier - appel de la police en cours...")
else:
    print("Fichier ouvert")
