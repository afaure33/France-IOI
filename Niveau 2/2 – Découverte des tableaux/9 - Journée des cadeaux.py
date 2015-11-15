#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbHabitants = int(input())
fortunes = [0]*nbHabitants

for loop in range(nbHabitants):
    fortunes[loop] = int(input())

fortunes.sort()

if nbHabitants % 2 == 0:
    print((fortunes[int(len(fortunes)/2-0.5)] + fortunes[int(len(fortunes)/2+0.5)])/2)
else:
    print(fortunes[int(len(fortunes)/2-0.5)])
