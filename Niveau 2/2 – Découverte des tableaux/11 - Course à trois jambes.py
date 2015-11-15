#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbParticipants = int(input())
entiers = [0] * nbParticipants

for loop in range(nbParticipants):
    entiers[loop] = int(input())

entiers.sort()

for loop in range(int(nbParticipants / 2)):
    print(str(entiers[loop]) + " " + str(entiers[nbParticipants - loop - 1]))
