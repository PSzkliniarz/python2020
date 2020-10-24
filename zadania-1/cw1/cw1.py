pyramid1 = str()

n = int(input("Podaj nieparzystą liczbę: "))

levels = int(n / 2)

for x in range(n):
    pyramid1 += "*"

#wyśrodkuje tekst względem n znaków
print(pyramid1.center(n))

while levels > 0:
    pyramid2 = pyramid1[1:len(pyramid1) - 1]

    pyramid1 = pyramid2

    print(pyramid1.center(n))

    levels -= 1

