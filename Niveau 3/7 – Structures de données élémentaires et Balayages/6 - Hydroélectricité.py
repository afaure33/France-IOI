#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# def sublists(lst, n):
#     return (lst[i:i+n] for i in range(len(lst) - n + 1))
#
# def max_sublist_sum(lst, n):
#     return max(sum(sub) for sub in sublists(lst, n))


def main():
    longCentHydro, longRiviere = map(int, sys.stdin.readline().split())
    forceCourant = list(map(int, sys.stdin.readline().split()))

    slices = (forceCourant[x:x + longCentHydro] for x in range(len(forceCourant) - longCentHydro + 1))

    print(max(map(sum,slices)))
    # sys.stdout.write(str(max_sublist_sum(forceCourant, longCentHydro)))

    slices = (forceCourant[x:x + longCentHydro] for x in range(len(forceCourant) - longCentHydro + 1))
main()
