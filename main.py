#################################### LE JEU DE MATH ##################################

import random

NOMBRE_MIN: int = 1
NOMBRE_MAX: int = 10
NB_QUESTIONS: int = 4


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
    reponse_str = input(f"Calculez: {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a+b
    if o == 1:
        calcul = a*b
    if reponse_int == calcul:
        return True
    else:
        return False

nb_points = 0

for i in range(0, NB_QUESTIONS):
    print(f"Question n°{i+1} sur {NB_QUESTIONS} : ")
    if poser_question():
        print("Réponse correcte")
        nb_points += 1
    else :
        print("Réponse incorrecte")
    print()

print(f"Votre note est {nb_points}/{NB_QUESTIONS}")

moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS:
    print("Exellent !")
elif nb_points == 0:
    print("Révisez vous maths !")
elif nb_points > moyenne:
    print("Pas mal")
else:
    print("Peut mieux faire")
