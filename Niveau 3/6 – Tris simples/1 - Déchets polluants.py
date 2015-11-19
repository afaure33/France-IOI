#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    nbBacsStock, nbBacsCamionMax = map(int, input().split())
    niveauPolutionBacs = list(map(int, input().split()))

    for loop in range(nbBacsCamionMax):
        print(max(niveauPolutionBacs), end=" ")
        niveauPolutionBacs.remove(max(niveauPolutionBacs))


main()
