#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    nBacs = int(input())
    valeurs = list(map(int, input().split()))
    valeurs.sort()

    print(' '.join(map(str, valeurs)))


main()
