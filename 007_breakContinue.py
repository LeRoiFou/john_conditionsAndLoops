"""
Les boucles et les instructions 'break' et 'continue' 

Éditeur : Laurent REYNAUD 
Date : 27-08-2020 
"""

# Stockage des données dans une liste
emails = ["lrcompta@aol.fr", "lrcompta@free.fr", "lrcompta@sfr.fr", "lrcompta@gmail.com", "lrcompta@xxx.fr"]

# Blacklist pour certains emails à envoyer
blacklist = ["lrcompta@free.fr", "lrcompta@xxx.fr"]

for elements in emails:
    if elements in blacklist:
        print("Email", elements, "interdit, envoi impossible")
        continue
    print("Email envoyé à :", elements)
""" 
Dans le cas présent, on a recours à l'instruction 'continue' et le résultat sera le suivant : 
Email envoyé à : lrcompta@aol.fr 
Email lrcompta@free.fr interdit, envoi impossible 
Email envoyé à : lrcompta@sfr.fr 
Email envoyé à : lrcompta@gmail.com 
Email lrcompta@xxx.fr interdit, envoi impossible 
Cette fois-ci à chaque fois qu'un email de la 'blacklist' s'affiche, une message informe que l'"envoi est impossible" 
"""
