#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbLivres = int(input())
titresLivres = [None]*nbLivres

for loop in range(nbLivres):
    titresLivres[loop] = input()

titresLivres.sort()

for titre in titresLivres:
    print(titre)
