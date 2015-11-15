#!/usr/bin/env python
# -*- coding: utf-8 -*-


def afficher_feuille(lines, cols, char):
    for loop in range(lines):
        print(char*cols)


nbLignes = int(input())
nbColonnes = int(input())
motif = input()

afficher_feuille(nbLignes, nbColonnes, motif)
