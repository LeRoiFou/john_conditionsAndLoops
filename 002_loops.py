option = "o"
while option == "o":
    date = input("Date : ")
    libelle = input("Libelle : ")
    montant = float(input("Montant : "))
    option = input("Nouvelle saisie (o/n) ? ")
print("Date :", date)
print("Libellé :", libelle)
print("Montant :", montant, "€")
