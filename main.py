"""
Projet fait par Patrick Morin
29 septembre 2022
Projet: Jeu de Devinette
"""
import random


def restart():
    """
    Création de la loop pour recommencer le jeu
    Tu peux décider avec cette partie de code de soit arreter ou recommencer le jeu
    """
    recommence = input("Voulez-vous continuer?")
    if recommence == "oui":
        return True
    elif recommence == "non":
        return False
    return restart()


while restart():
    chiffre_aleatoire = random.randint(1, 100)
    nombre_essai = 0
    print("J’ai choisi un nombre au hasard entre 1 et 100. ")
    print("Quel est le nombre que j'ai choisi?")
    while (essai := int(input("Insérez un nombre entre 1 et 100 : "))) != chiffre_aleatoire:
        nombre_essai += 1
        if essai < chiffre_aleatoire:
            print("Mauvaise réponse, le nombre est plus grand ")

        elif essai > chiffre_aleatoire:
            print("Mauvaise réponse, le nombre est plus petit ")

    print("Bravo! Bonne réponse! Vous avez réussi en ", nombre_essai, " essais")
