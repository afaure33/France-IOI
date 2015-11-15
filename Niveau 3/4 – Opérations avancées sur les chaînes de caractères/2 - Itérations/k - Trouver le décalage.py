#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_most_frequent_letter(data):
    nbtimes = 0
    mostfrequentletter = "e"

    for idLetter in range(26):
        nbtimes_tmp = data.count(chr(65+idLetter)) + data.count(chr(97+idLetter))

        if nbtimes_tmp > nbtimes:
            mostfrequentletter = chr(97+idLetter)
            nbtimes = nbtimes_tmp

    return mostfrequentletter


def decrypt_text(data, gap):
    decrypted_text = ""

    for idchar in range(len(data)):
        char = data[idchar]

        if char.isalpha():
            ismaj = char.isupper()

            if ismaj:
                char = char.lower()

            numero = (ord(char) - ord("a") + gap) % 26
            char = chr(numero + ord("a"))

            if ismaj:
                char = char.upper()

        decrypted_text += char

    return decrypted_text


def main():
    text = input()

    print(decrypt_text(text, int(ord("e") - ord(find_most_frequent_letter(text)))))

main()
