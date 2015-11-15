#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ligne_caracteres(caractere, longueur):
    for iCol in range(longueur):
        print(caractere, end="")
    print()

longueurDentelle = int(input())

ligne_caracteres("X", longueurDentelle)
ligne_caracteres("#", longueurDentelle)
ligne_caracteres("i", longueurDentelle)
