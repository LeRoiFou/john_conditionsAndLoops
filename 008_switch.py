"""
Les choix (switch / case dans Java) 

Il n'existe pas d'instruction 'switch / case' dans Java, pour effectuer des choix, il existe deux possibilités : 
    -> Recourir aux conditions if / else 
    -> Recourir aux dictionnaires 

Éditeur : Laurent REYNAUD 
Date : 06-09-2020 
"""

print("Entrez votre âge :")
age = int(input())

# Recours aux conditions :

if age < 18:
    print("mineur")
elif age > 18:
    print("majeur")
else:
    print("18 ans tout pile")

# Le code précédent est équivalent à cela en recourant aux dictionnaires

print({True: "18 ans tout pile", age < 18: "mineur", age > 18: "majeur"}[True])
