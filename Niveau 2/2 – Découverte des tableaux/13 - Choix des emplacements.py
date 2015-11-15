#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbEmplacements = int(input())
emplacements = [0]*nbEmplacements

for loop in range(nbEmplacements):
    # On demande le numéro du marchand qui sera à cet emplacement
    emplacements[loop] = int(input())

emplacements2 = sorted(emplacements)

for loop in range(nbEmplacements):
    # On veut le numéro de l'emplacement de chaque marchand
    print(emplacements.index(emplacements2[loop]))
