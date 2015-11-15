#!/usr/bin/env python
# -*- coding: utf-8 -*-


def afficher_x(nbchar):
    print("X" * nbchar)


def afficher_sharp(nblines, nbcolumns):
    for loop1 in range(nblines):
        for loop2 in range(nbcolumns):
            if loop1 == 0 or loop1 == nblines - 1 or loop2 == 0 or loop2 == nbcolumns - 1:
                print("#", end="")
            else:
                print(" ", end="")

            if loop2 == nbcolumns - 1:
                print()


def afficher_at(nblines):
    for loop1 in range(nblines):
        for loop2 in range(loop1):
            if loop2 == 0:
                print("@", end="")

                if loop2 == loop1 - 1:
                    print()
            elif loop2 == loop1 - 1:
                print("@")
            else:
                if loop1 == nblines - 1:
                    print("@", end="")
                else:
                    print(" ", end="")


nbCharX = int(input())
nbLinesSharp = int(input())
nbColumnsSharp = int(input())
nbLinesAt = int(input())

afficher_x(nbCharX)
print()
afficher_sharp(nbLinesSharp, nbColumnsSharp)
print()
afficher_at(nbLinesAt + 1)
