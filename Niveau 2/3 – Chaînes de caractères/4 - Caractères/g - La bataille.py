#!/usr/bin/env python
# -*- coding: utf-8

cardsPlayer1 = input()
cardsPlayer2 = input()
nbEgalites = 0
gagnant = "0"

for loop in range(max(len(cardsPlayer1), len(cardsPlayer2))):
    if loop+1 == len(cardsPlayer1) and loop+1 == len(cardsPlayer2):
        gagnant = "="
        nbEgalites += 1
        break
    elif loop == len(cardsPlayer1):
        gagnant = "2"
        break
    elif loop == len(cardsPlayer2):
        gagnant = "1"
        break
    else:
        if cardsPlayer1[loop] == cardsPlayer2[loop]:
            # ils continuent à jouer
            nbEgalites += 1
            # print("on continue à jouer")
        else:
            # On détermine le gagnant
            if cardsPlayer1[loop] > cardsPlayer2[loop]:
                gagnant = "2"
                break
            else:
                gagnant = "1"
                break

print(gagnant)
print(nbEgalites)

