list1 = [1, 2, [3, 4, [5,[22,14], 6], 5], 3, 4]

def serchLevel(lista, var, lastLevel):
    noList = True
    if lastLevel:
        lista.append(var)
    else:
        for el in lista:
            if isinstance(el,list):
                noList = False
                #print("next level")
                #print(el)
                serchLevel(el,var,noList)

        if noList:
            serchLevel(lista, var,noList )


print(list1)
serchLevel(list1,9,False)
serchLevel(list1,12,False)
print(list1)