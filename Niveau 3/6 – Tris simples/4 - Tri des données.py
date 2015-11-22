#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    nBacs = int(input())
    niveauPolutionBacs = list(map(int, input().split()))
    niveauPolutionBacs = sorted(niveauPolutionBacs)

    print(' '.join(map(str, niveauPolutionBacs)))


main()
