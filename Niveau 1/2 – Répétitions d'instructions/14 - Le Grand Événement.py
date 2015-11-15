from robot import *

for loop1 in range(9):
    droite()

for loop2 in range(4):
    haut()
    for loop21 in range(8):
        gauche()
    haut()
    for loop22 in range(8):
        droite()

haut()
for loop3 in range(9):
    gauche()
for loop4 in range(9):
    bas()
