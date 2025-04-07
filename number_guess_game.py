# Importation des bibliothèques
import random


# Initialisation du nombre à deviner
nombre_a_deviner = random.randint(0, 1000)

# Initialisation de la réponse de l'utilisateur
nombre_utilisateur = -1

# boolean de sortie
victoire = False

# Compteur d'essai de l'utilisateur
cpt_essai = 0

# Messages d'introduction
print("=========================== Trouve le nombre ===========================")
print("Le but de ce jeu est de deviner un nombre aléatoire entre 0 et 1000.")

# Boucle du jeu
while (victoire == False):
    nombre_utilisateur = int(input("Donne-moi un entier positif : "))
    if (nombre_utilisateur < nombre_a_deviner):
        print("Le nombre a deviné est plus grand.")
        cpt_essai += 1
    elif (nombre_utilisateur > nombre_a_deviner):
        print("Le nombre a deviné est plus petit.")
        cpt_essai += 1
    else:
        print("Bravo, vous avez trouvé le nombre à deviner.")
        print("Le nombre a deviné était ",nombre_a_deviner)
        print("Vous l'avez trouvé en", cpt_essai,"essai(s)")
        victoire = True