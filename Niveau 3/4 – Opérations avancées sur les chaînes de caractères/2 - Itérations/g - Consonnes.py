#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import ascii_lowercase

voyelles = "aeiouy"

for c in ascii_lowercase:
    if c not in voyelles:
        print(c, end=' ')
