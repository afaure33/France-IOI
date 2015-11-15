#!/usr/bin/env python
# -*- coding: utf-8 -*-


def gets(*types):
    return tuple([types[i](val) for i, val in enumerate(input().split(' '))])


def meters2feet(value):
    return value/0.3048


def grams2pounds(value):
    return value*0.002205


def celsius2fahrenheit(value):
    return 32+(1.8*value)


nbValeurs = int(input())


for loop in range(nbValeurs):
    valeur, unite = gets(float, str)

    if unite == "m":
        print(str(meters2feet(valeur)) + " p")
    elif unite == "g":
        print(str(grams2pounds(valeur)) + " l")
    elif unite == "c":
        print(str(celsius2fahrenheit(valeur)) + " f")
