#!/usr/bin/env python
# -*- coding: utf-8 -*-


def min2(val1, val2):
    if val1 < val2:
        return val1
    else:
        return val2


valMin = int(input())
for iVal in range(9):
    valMin = min2(valMin, int(input()))
print(valMin)
