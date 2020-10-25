pyramid = str()
n = int(input("Podaj nieparzystą liczbę: "))

levels = int(n / 2)

for x in range(n):
    pyramid += "*"


while levels >= 0:

    print(pyramid.center(n))

    pyramid = pyramid[1:len(pyramid) - 1]

    levels -= 1

