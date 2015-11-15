#!/usr/bin/env python
# -*- coding: utf-8

lettreMaj = input()
nbLignes = int(input())
total = 0

for loop in range(nbLignes):
    texteMaj = input()
    total += texteMaj.count(lettreMaj)

print(total)
