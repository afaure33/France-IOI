#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbLignes, nbMots = map(int, input().split())
longueurs = [0] * 101

for loop1 in range(nbLignes):
    mots = input().split()

    for loop2 in range(nbMots):
        longueurs[len(mots[loop2])] += 1
        
for loop in range(101):
    if longueurs[loop] != 0:
        print(str(loop) + " : " + str(longueurs[loop]))
