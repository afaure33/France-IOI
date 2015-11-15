#!/usr/bin/env python
# -*- coding: utf-8 -*-


def demander_code(code):
    code_entre = 0
    while code_entre != code:
        code_entre = int(input("Entrez le code : "))
        print()

demander_code(4242)
print("Premier code bon.")
demander_code(2121)
print("Bravo.")
