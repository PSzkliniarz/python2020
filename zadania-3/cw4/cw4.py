def roma(str):
    lenght = len(str)
    sum = 0

    roman = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sufix = ['V', 'X', 'L', 'C', 'D', 'M']

    i = 0
    while i < lenght:
        if i + 1 < lenght and str[i+1] in sufix and (str[i] not in sufix or roman[str[i]] < roman[str[i+1]]):
            sum += (roman[str[i+1]] - roman[str[i]])
            i += 2
        else:
            sum += roman[str[i]]
            i += 1

    return sum


print(roma("XXXVIII"))
print(roma("XLIV"))
print(roma("CMXLVIII"))