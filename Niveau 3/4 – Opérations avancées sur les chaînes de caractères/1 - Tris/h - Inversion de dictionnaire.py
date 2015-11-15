#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbMots = int(input())
couplesMots = [None]*nbMots

for loop in range(nbMots):
    premier, second = input().split()
    couplesMots[loop] = second + " " + premier

couplesMots.sort()

for loop in range(nbMots):
    print(couplesMots[loop])