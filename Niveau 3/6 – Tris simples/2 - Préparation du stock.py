#!/usr/bin/env python
# -*- coding: utf-8 -*-


def doit():
    try:
        for loop1 in range(len(niveauPolutionBacsInserer)):
            if len(niveauPolutionBacs) == 0:
                niveauPolutionBacs.append(niveauPolutionBacsInserer[loop1])
                print(loop1, end=" ")
                continue
            for loop2 in range(len(niveauPolutionBacs)):
                if niveauPolutionBacsInserer[loop1] <= niveauPolutionBacs[loop2]:
                    niveauPolutionBacs.insert(loop2, niveauPolutionBacsInserer[loop1])
                    print(loop2, end=" ")
                    break
                if loop2 == len(niveauPolutionBacs) - 1:
                    niveauPolutionBacs.append(niveauPolutionBacsInserer[loop1])
                    print(loop2 + 1, end=" ")

    except:
        pass


nbBacsStock, nbBacsInserer = map(int, input().split())

niveauPolutionBacs = list(map(int, input().split()))
niveauPolutionBacs = sorted(niveauPolutionBacs)
niveauPolutionBacsInserer = list(map(int, input().split()))

doit()
print()
print(' '.join(map(str, niveauPolutionBacs)))
