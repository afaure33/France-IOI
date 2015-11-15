#!/usr/bin/env python
# -*- coding: utf-8 -*-

titres = [None] * 6
auteurs = [None] * 6

for loop in range(6):
    auteurs[loop] = input()
    titres[loop] = input()

for loop in range(6):
    print(titres[loop])
    print(auteurs[loop])
