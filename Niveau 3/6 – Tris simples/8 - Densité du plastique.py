#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys


def RechercheDico(liste, elt):
    """
    RechercheSeq(list liste, int elt) -> int
    Retourne la position de l'entier <elt> dans <liste>
    triée et -1 si <elt> ne se trouve pas dans <liste>
    """

    position = -1
    gauche = 0
    droite = len(liste) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2

        if elt == liste[milieu]:
            position = milieu
            break

        else:
            if elt < liste[milieu]:
                droite = milieu - 1
            else:
                gauche = milieu + 1

    return position


def main():
    nbBlocsStock = int(sys.stdin.readline())
    densiteBlocs = list(map(int, input().split()))
    nbQuestions = int(sys.stdin.readline())
    densiteBlocs.sort()

    for loop in range(nbQuestions):
        densiteDemandee = int(sys.stdin.readline())

        if (RechercheDico(densiteBlocs, densiteDemandee)) == -1:
            sys.stdout.write("0")
        else:
            sys.stdout.write("1")

        sys.stdout.write("\n")


main()
