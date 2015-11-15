#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbLivres = int(input())
maxLength = 0

for loop in range(nbLivres):
    titre = input()

    if len(titre) > maxLength:
        maxLength = len(titre)
        print(titre)
