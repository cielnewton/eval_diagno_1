from random import randint

taille = randint(8, 16)
# print("Taille initiale:", taille)

mot_de_pass = ""
obligatoire = ""

alphabet = "abcdefghijklmnopqrstuvwxyz"
special = "@#$%&"

# Génération des caractères obligatoires
indice_lettre1 = randint(0, 25)
indice_lettre2 = randint(0, 25)
indice_special = randint(0, len(special) - 1)
chiffre = randint(0, 9)  # Utilise tous les chiffres de 0 à 9

# Construire les caractères obligatoires
obligatoire = alphabet[indice_lettre1] + alphabet[indice_lettre2].upper() + str(chiffre) + special[indice_special]

# print("Obligatoire:", obligatoire)
mot_de_pass = obligatoire

# Compléter le mot de passe jusqu'à atteindre la longueur souhaitée
for _ in range(taille - 4):  # Taille ajustée pour inclure les caractères obligatoires
    typede = randint(1, 3)
    if typede == 1:
        aleatoire = randint(0, 25)
        maj_min = randint(0, 1)
        if maj_min == 0:
            mot_de_pass += alphabet[aleatoire].upper()
        else:
            mot_de_pass += alphabet[aleatoire]
    elif typede == 2:
        aleatoire = randint(0, len(special) - 1)
        mot_de_pass += special[aleatoire]
    else:
        aleatoire = randint(0, 9)
        mot_de_pass += str(aleatoire)

print(mot_de_pass)
print("Taille:", len(mot_de_pass))
