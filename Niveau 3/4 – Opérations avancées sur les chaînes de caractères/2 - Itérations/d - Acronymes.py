#!/usr/bin/env python
# -*- coding: utf-8 -*-

acronyme = input().lower()
nbLivres = int(input())

for loop in range(nbLivres):
    titre = input().lower().split()

    indiceMot = 0
    firstLetterCorrect = 0

    if len(titre) == len(acronyme):
        for letter in acronyme:
            if letter == titre[indiceMot][0]:
                firstLetterCorrect += 1
            indiceMot += 1

        if firstLetterCorrect == len(acronyme):
            print(' '.join(titre).title())

