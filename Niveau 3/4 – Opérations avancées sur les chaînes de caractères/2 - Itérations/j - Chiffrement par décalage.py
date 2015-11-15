def main():
    nbpages = int(input())

    for idPage in range(2, nbpages + 1):
        page = input()

        if idPage % 2 == 0:
            decalage = -3 * idPage
        else:
            decalage = 5 * idPage

        for idCaractere in range(len(page)):
            caractere = page[idCaractere]

            if caractere.isalpha():
                ismaj = caractere.isupper()

                if ismaj:
                    caractere = caractere.lower()

                numero = (ord(caractere) - ord("a") + decalage) % 26
                caractere = chr(numero + ord("a"))

                if ismaj:
                    caractere = caractere.upper()

            print(caractere, end="")

        print()

main()
