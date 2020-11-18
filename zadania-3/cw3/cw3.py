list = [[], [4], 2, (1, 2), [3, 4], (5, 6, 7)]

sum_list = []

def sum_elem(sublist):
    sum = 0

    if type(sublist) != int:
      for el in sublist:
        sum += el
    else:
        sum = sublist

    return sum


for i in list:
    sum_list.append(sum_elem(i))

print(list)
print(sum_list)