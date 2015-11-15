#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbLignes = int(input())

for lignes in range(nbLignes):
    ligne = input()

    for caracteres in range(len(ligne)-1, -1, -1):
        print(ligne[caracteres], end="")
    print()
