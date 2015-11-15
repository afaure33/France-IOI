#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbOperations = int(input())
Ingredient = [0] * 11

for loop in range(nbOperations):
    numIngredient = int(input())
    qtyIngredient = int(input())

    Ingredient[numIngredient] += qtyIngredient

for loop in range(1, 11):
    print(Ingredient[loop])
