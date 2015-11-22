#!/usr/bin/python
# -*- coding: utf-8 -*-


def cherche_dico_rec(L, x):
    """L tableau non vide trié dans l'ordre croissant, x un élément.
    On renvoie True si x est dans L, False sinon"""

    n = len(L)

    if n == 1:
        return L[0] == x

    m = n // 2

    if L[m] == x:
        return True
    elif L[m] < x:
        return cherche_dico_rec(L[m:], x)  # la partie gauche
    else:
        return cherche_dico_rec(L[:m], x)  # la partie droite


def main():
    nbBlocsStock = int(input())
    densiteBlocs = list(map(int, input().split()))
    nbQuestions = int(input())
    densiteBlocs.sort()

    for loop in range(nbQuestions):
        densiteDemandee = int(input())

        print(int(cherche_dico_rec(densiteBlocs, densiteDemandee)))


main()
