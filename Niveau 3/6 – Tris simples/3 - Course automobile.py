#!/usr/bin/python
# -*- coding: utf-8 -*-


def bubble_sort(data):
    nbechanges = 0
    echanges = []

    n = len(data)
    swapped_elements = True

    while swapped_elements == True:
        swapped_elements = False

        for j in range(0, n - 1):
            if data[j] > data[j + 1]:
                swapped_elements = True
                data[j], data[j + 1] = data[j + 1], data[j]

                nbechanges += 1
                echanges.append(str(data[j + 1]) + " " + str(data[j]))

    return nbechanges, echanges


def main():
    nbAuto = int(input())
    numAutoDep = list(map(int, input().split()))

    data = bubble_sort(numAutoDep)

    print(data[0])
    print("\n".join(data[1]))


main()
