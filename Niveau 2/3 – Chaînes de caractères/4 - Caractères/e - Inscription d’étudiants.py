#!/usr/bin/env python
# -*- coding: utf-8 -*-

nom = input()

if "A" <= nom[0] <= "F":
    print(1)
elif "G" <= nom[0] <= "P":
    print(2)
else:
    print(3)
