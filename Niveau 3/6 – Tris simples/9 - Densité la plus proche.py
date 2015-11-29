#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from bisect import bisect_left


def takeClosest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)

    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]

    before = myList[pos - 1]
    after = myList[pos]
    
    if after - myNumber < myNumber - before:
        return after
    else:
        return before


def main():
    nbBlocsStock = int(sys.stdin.readline())
    densiteBlocs = list(map(int, input().split()))
    nbQuestions = int(sys.stdin.readline())
    densiteBlocs.sort()

    for loop in range(nbQuestions):
        densiteDemandee = int(sys.stdin.readline())

        sys.stdout.write(str(takeClosest(densiteBlocs, densiteDemandee)))
        sys.stdout.write("\n")


main()
