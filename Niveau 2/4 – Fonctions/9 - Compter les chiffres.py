#!/usr/bin/env python
# -*- coding: utf-8 -*-


def lookandsay(number):
    result = ""

    repeat = number[0]
    number = number[1:] + " "
    times = 1

    for actual in number:
        if actual != repeat:
            result += str(times) + repeat
            times = 1
            repeat = actual
        else:
            times += 1

    return result


num = "1"

nb = int(input())

for i in range(nb):
    print(num)
    num = lookandsay(num)
