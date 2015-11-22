#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    nbElements = int(input())
    elements = []

    for loop in range(nbElements):
        elements.append(input())

    elements.sort()

    for loop in range(nbElements):
        print(elements[loop])


main()
