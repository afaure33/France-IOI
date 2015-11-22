#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


###############
# MA SOLUTION #
###############
def main():
    nbBacs = int(input())
    bacs = []

    for loop in range(nbBacs):
        tmp1, tmp2 = input().split()
        bacs.append([int(tmp2), int(tmp1)])

    bacs.sort()

    for loop in range(nbBacs):
        print(bacs[loop][1], bacs[loop][0])


##############
# CORRECTION #
##############
def main2():
    nbBacs = int(input())
    bacs = [list(map(int, sys.stdin.readline().split())) for _ in range(nbBacs)]
    bacs.sort(key=lambda bac: (bac[1], bac[0]))

    for bac in bacs:
        print(*bac)


main()
