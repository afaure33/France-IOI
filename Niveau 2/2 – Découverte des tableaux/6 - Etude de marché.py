#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbProduits = int(input())
produits = [0] * nbProduits
nbPersonnes = int(input())

for loop in range(nbPersonnes):
    favProduit = int(input())
    produits[favProduit] += 1

for loop in range(nbProduits):
    print(produits[loop])
