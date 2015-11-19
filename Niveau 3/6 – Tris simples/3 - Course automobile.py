# Les automobiles ont été numérotées selon leur ordre d'arrivée et
# la seconde ligne contient nbAutomobiles entiers : les numéros des
# automobiles au départ de la course.


def main():
    nbEchanges = 0
    echanges = ""

    nbAuto = int(input())
    numAutoDep = list(map(int, input().split()))

    for iAuto1 in range(nbAuto):
        while numAutoDep[iAuto1] != iAuto1 + 1:
            for iAuto2 in range(iAuto1, nbAuto, 1):
                if numAutoDep[iAuto2] == iAuto1 + 1:
                    numAutoDep[iAuto2], numAutoDep[iAuto2 - 1] = numAutoDep[iAuto2 - 1], numAutoDep[iAuto2]

                    nbEchanges += 1
                    echanges = echanges + str(numAutoDep[iAuto2]) + " " + str(numAutoDep[iAuto2 - 1]) + "\n"
                    break

    print(nbEchanges)
    print(echanges)


main()
