#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbCharrettes = int(input())
poids = [0]*nbCharrettes

for loop in range(nbCharrettes):
    poids[loop] = float(input())

moyenne = sum(poids) / len(poids)

for loop in range(nbCharrettes):
    print(-(poids[loop]-moyenne))
