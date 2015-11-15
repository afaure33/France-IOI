#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_nb_amour(name):
    nbamour = 0
    for loop in range(len(name)):
        nbamour += ord(name[loop])-65

    if nbamour < 10:
        return nbamour
    else:
        return get_sum(nbamour)


def get_sum(number):
    number = str(number)

    while int(number) >= 10:
        number_tmp = 0
        for loop in range(len(str(number))):
            digit = int(number[loop])
            number_tmp += digit
        number = str(number_tmp)

    return number

prenom1, prenom2 = input().split()

print(get_nb_amour(prenom1), get_nb_amour(prenom2))
