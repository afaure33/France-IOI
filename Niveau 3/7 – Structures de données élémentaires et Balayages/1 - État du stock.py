#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def main():
    nbTypesProduits = int(sys.stdin.readline())
    nbProduits = list(map(int, sys.stdin.readline().split()))
    nbOperations = int(sys.stdin.readline())

    for loop in range(nbOperations):
        tmp = list(map(int, sys.stdin.readline().split()))

        nbProduits[tmp[0] - 1] += tmp[1]

    sys.stdout.write(" ".join(str(x) for x in nbProduits))


main()
