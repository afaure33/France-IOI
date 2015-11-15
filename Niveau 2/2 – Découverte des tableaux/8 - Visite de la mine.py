#!/usr/bin/env python
# -*- coding: utf-8 -*-

deplacementInverse = [0, 2, 1, 3, 5, 4]

nbDeplacements = int(input())
chemin = [0] * nbDeplacements

for numero in range(nbDeplacements):
    chemin[numero] = int(input())

for numero in range(nbDeplacements - 1, -1, -1):
    deplacement = chemin[numero]
    print(deplacementInverse[deplacement])
