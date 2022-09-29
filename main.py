
"""
PROJET FAIT PAR PATRICK MORIN
29 SEPTEMBRE 2022
PROJET: JEU DE DEVINETTE
"""
import random

chiffre_aleatoire = random.randint(1, 100)

print("J’ai choisi un nombre au hasard entre 1 et 100. ")
print("Quel est le nombre que j'ai choisi?")
nombre_essai=0

def restart():
    recommence = input("Voulez-vous continuer?")
    if recommence == ("oui"):
        return True
    elif recommence == ("non"):
        return False
    return restart()

while restart():
        while essai != chiffre_aleatoire:
            essai = int(input("Insérez un nombre entre 1 et 100 : "))
            print(essai)
            nombre_essai += 1

            if essai < chiffre_aleatoire :
                print ("Mauvaise réponse, le nombre est plus grand ")

            elif essai > chiffre_aleatoire :
                print ("Mauvaise réponse, le nombre est plus petit ")

        print(f"Bravo! Bonne réponse! Vous avez réussi en {nombre_essai} essais" )