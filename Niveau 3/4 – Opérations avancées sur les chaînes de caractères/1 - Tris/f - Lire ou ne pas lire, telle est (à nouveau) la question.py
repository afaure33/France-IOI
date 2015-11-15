#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbLivres = int(input())
titresLivres = [None]*nbLivres

count = 0

for loop in range(nbLivres):
    titresLivres[loop] = input()

    count += 1

    if loop == 0:
        print(titresLivres[loop])
        count = 0
    elif titresLivres[loop] > titresLivres[loop-count]:
        print(titresLivres[loop])
        count = 0