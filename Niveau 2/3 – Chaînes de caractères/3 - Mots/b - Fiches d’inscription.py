#!/usr/bin/env python
# -*- coding: utf-8 -*-

nbPersonnes = int(input())

for loop in range(nbPersonnes):
    name = input().split(" ")
    print(name[1], name[0])
