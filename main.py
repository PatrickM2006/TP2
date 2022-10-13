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
    recommence = input("Voulez-vous continuer?: ")
    if recommence == "oui":
        return True
    elif recommence == "non":
        return False
    return restart()


while restart():

    nombre_minimum = int(input("Choisissez la borne minimale du jeu: "))
    nombre_maximum = int(input("Choisissez la borne maximale du jeu: "))
    chiffre_aleatoire = random.randint(nombre_minimum, nombre_maximum)
    nombre_essai = 0
    print("Féicitation! Vous avec choisi les bornes.")
    while (essai := int(input("Trouvez le nombre: "))) != chiffre_aleatoire:
        nombre_essai += 1
        if essai < chiffre_aleatoire:
            print("Mauvaise réponse, le nombre est plus grand ")

        elif essai > chiffre_aleatoire:
            print("Mauvaise réponse, le nombre est plus petit ")

    print("Bravo! Bonne réponse! Vous avez réussi en ", nombre_essai, " essais")
