sentence = input()
nbFois = 0
letter = None

for loop in range(26):
    nbFois_tmp = sentence.count(chr(65 + loop)) + sentence.count(chr(97 + loop))

    if nbFois_tmp > nbFois:
        letter = chr(65 + loop)
        nbFois = nbFois_tmp

print(letter)
