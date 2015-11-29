#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def main():
    nbClients = int(sys.stdin.readline())
    numCartes = list(map(int, sys.stdin.readline().split()))

    s = set(numCartes)
    d = []

    for x in numCartes:
        if x in s:
            s.remove(x)
        else:
            d.append(x)

    try:
        sys.stdout.write(str(d[0]))
    except:
        sys.stdout.write("-1")


main()
