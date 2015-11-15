#!/usr/bin/env python
# -*- coding: utf-8 -*-


def demander_code():
    code_entre = 0
    while code_entre != 4242:
        code_entre = int(input("Entrez le code : "))
        print()

demander_code()
print("Encore une fois.")
demander_code()
print("Bravo.")
