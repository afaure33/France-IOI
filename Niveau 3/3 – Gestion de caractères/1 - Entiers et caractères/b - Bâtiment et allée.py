#!/usr/bin/env python
# -*- coding: utf-8 -*-

nomAuteur = input()
ageFilsAine = int(input())

print(ord(nomAuteur[0]) - 64, chr(ageFilsAine + 64), sep="")
