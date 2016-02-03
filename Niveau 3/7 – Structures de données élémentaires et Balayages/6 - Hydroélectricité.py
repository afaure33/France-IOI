#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def main():
    slicetmp = 0

    longCentHydro, longRiviere = map(int, sys.stdin.readline().split())
    forceCourant = list(map(int, sys.stdin.readline().split()))

    maxslice = sum(forceCourant[0:0 + longCentHydro])
    slicetmp = sum(forceCourant[0:0 + longCentHydro])

    for loop in range(len(forceCourant)-longCentHydro):
        slicetmp -= forceCourant[loop]
        slicetmp += forceCourant[loop+longCentHydro]

        if slicetmp > maxslice:
            maxslice = slicetmp

    #for x in range(len(forceCourant) - longCentHydro + 1):
        #slices.append(sum(forceCourant[x:x + longCentHydro]))

    #print(max(slices))
    print(maxslice)
main()
