sorozat = [-3, 5, 11, -2, 4]


def elsofeladat(sep="!"):

    i = 0

    szoveg = ""

    while i <= len(sorozat):
        if i < len(sorozat) - 1:
            szoveg += str(sorozat[i]) + sep
        elif i == len(sorozat) - 1:
            szoveg += (str(i))
        i += 1

    print(szoveg)

def beker():

    szam = 0
    while ((szam < 10 or szam >100)or(szam % 3 != 0 or szam % 2 == 0)):
        szam = int(input("Kérek egy 3-mal osztható páratlan kétjegyű számot:"))
        sorozat.append(szam)

beker()
elsofeladat("!")