#!/usr/bin/env python
# -*- coding: utf-8

bookTitle = input()
bookAuthor = input()

# for char in 'AEIOUY ':
#   bookTitle = bookTitle.replace(char, '')
#   bookAuthor = bookAuthor.replace(char, '')

bookTitle = ''.join(c for c in bookTitle if c not in 'AEIOUY ')
bookAuthor = ''.join(c for c in bookAuthor if c not in 'AEIOUY ')

print(bookTitle)
print(bookAuthor)
