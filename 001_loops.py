def multiplier(c, d, l):
    for n in range(d, l+1, 1):  # pour chaque entier (début, fin, saut)...
        print(n, "x", c, "=", n * c)
    return ""


print("Table de multiplication :")
chiffre = int(input())
print("Début de la table de multiplication :")
debut = int(input())
print("Limite de la table de multiplication :")
limite = int(input())
print(multiplier(chiffre, debut, limite))