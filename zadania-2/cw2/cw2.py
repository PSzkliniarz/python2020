def leapYear(year):
    leap = False

    if (year % 4 == 0) and (year % 100 != 0) or (year % 100 == 0) and (year % 400 == 0):
        leap = 1

    return leap


if leapYear(int(input("Insert year between 1900 - 100000: "))):
    print("YES. It is leap year")
else:
    print("NO. It is't leap year")