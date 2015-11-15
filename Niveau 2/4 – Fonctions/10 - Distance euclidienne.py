#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *


def distance_euclidienne(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


print(distance_euclidienne(float(input()), float(input()), float(input()), float(input())))

