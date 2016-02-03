from robot import *

for loop in range(10):
    for loop2 in range(loop+1):
        droite()

    ramasser()

    for loop3 in range(loop+1):
        gauche()

    deposer()