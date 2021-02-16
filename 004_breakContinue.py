"""
Les boucles et les instructions 'break' et 'continue' 
-> Complément sur l'instruction 'break' : tuto GRAVEN - 5_Boucles-23 
-> Complément sur l'instruction 'continue' : tuto GRAVEN - 5_Boucles-22 

Éditeur : Laurent REYNAUD 
Date : 27-08-2020 
"""

for i in range(0, 15):
    if i == 2:
        break
    print(i)
"""Ce programme affichera seulement 0, 1 étant donné que lorsque i vaudra 2 la boucle s’arrêtera automatiquement à  
cause du fameux break. """

for i in range(0, 15):
    for j in range(10, 20):
        print(i, j)
        break
"""Cette fois-ci le programme s'arrêtera à la seconde boucle, il n'affichera donc que les valeurs de 0 à 14 de la  
première boucle (le chiffre 15 est exclus) et uniquement la valeur 10 pour la deuxième boucle """

for i in range(0, 15):
    if i % 2 != 0:
        continue
    print(i)
"""Le mot-clé continue n’arrête pas la boucle mais permet de passer simplement au prochain tour de boucle"""
