#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import deque


def main():
    produitsPile = deque()
    nbOperations = int(sys.stdin.readline())

    for loop in range(nbOperations):
        operation = list(map(int, sys.stdin.readline().split()))

        # Il s'agit d'un achat
        if operation[0] > 0:
            # On ajoute tmp[0] produits avec la date tmp[1]
            for loop in range(operation[0]):
                produitsPile.append(operation[1])
        # Il s'agit d'une vente
        else:
            for loop in range(operation[0] * -1):
                produitsPile.popleft()

    sys.stdout.write(str(min(produitsPile)))


main()
