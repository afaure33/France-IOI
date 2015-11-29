#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def main():
    nbCaracteres = int(sys.stdin.readline())

    caracteres = sys.stdin.readline()

    if caracteres[0] == "(" and caracteres[len(caracteres) - 2] == ")" and caracteres.count("(") == caracteres.count(
            ")"):
        print(1)
    else:
        print(0)


main()
