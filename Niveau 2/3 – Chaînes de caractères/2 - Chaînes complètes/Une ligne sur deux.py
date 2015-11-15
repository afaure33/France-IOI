#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbLignes = int(input())

for loop in range(nbLignes):
    ligne = input()

    if loop % 2 == 0:
        print(ligne)
