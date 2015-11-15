#!/usr/bin/env python
# -*- coding: utf-8 -*-

somme = 0

while True:
    try:
        nombres = list(map(int, input().split()))
        somme += sum(nombres)
    except:
        break

print(somme)

