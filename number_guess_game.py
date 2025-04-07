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

# 
print("=========================== Trouve le nombre ===========================")
print("Le but de ce jeu est de deviner un nombre aléatoire entre 0 et 1000.")

# # Boucle du jeu
# while (victoire == False):
#     nombre_utilisateur = int(input("Donne-moi un entier positif : "))