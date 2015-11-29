#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def main():
    produitsPile = []

    nbOperations = int(sys.stdin.readline())

    for loop in range(nbOperations):
        tmp = list(map(int, sys.stdin.readline().split()))

        # Il s'agit d'un achat
        if tmp[0] > 0:
            # On ajoute tmp[0] produits avec la date tmp[1]
            for loop in range(tmp[0]):
                produitsPile.append(tmp[1])
        # Il s'agit d'une vente
        else:
            # On enlève tmp[0] produits avec la date tmp[1]
            for loop in range(tmp[0] * -1):
                produitsPile.pop()

    sys.stdout.write(str(min(produitsPile)))


main()
