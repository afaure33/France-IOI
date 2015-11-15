#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbLivres = int(input())
longueurMinimale = int(input())

for loop in range(nbLivres):
    titre = input()
    resume = input()

    if len(resume) < longueurMinimale:
        print(titre)
