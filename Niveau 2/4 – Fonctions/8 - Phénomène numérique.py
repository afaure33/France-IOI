#!/usr/bin/env python
# -*- coding: utf-8 -*-


def afficher_suite(number):
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1

        print(int(number), end=" ")


terme = int(input())
afficher_suite(terme)
