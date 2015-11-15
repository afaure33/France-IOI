#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbPositions = int(input())
positions = [0] * nbPositions

nbChgtPositions = int(input())

for loop in range(nbPositions):
    positions[loop] = int(input())

for loop in range(nbChgtPositions):
    position1 = int(input())
    position2 = int(input())

    positions[position1], positions[position2] = positions[position2], positions[position1]

for loop in range(nbPositions):
    print(positions[loop])
