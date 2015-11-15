#!/usr/bin/env python
# -*- coding: utf-8 -*-

uncrypt_grid = list(input().lower())

crypted_text = list(input())
uncrypted_text = crypted_text

for loop in range(len(uncrypted_text)):
    if uncrypted_text[loop].isalpha():
        if uncrypted_text[loop].isupper():
            uncrypted_text[loop] = uncrypt_grid[ord(uncrypted_text[loop])-ord("A")].upper()
        else:
            uncrypted_text[loop] = uncrypt_grid[ord(uncrypted_text[loop])-ord("a")]

print(''.join(uncrypted_text))


