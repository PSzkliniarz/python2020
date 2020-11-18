def list_init(n):
    lista = []

    for i in range(n):
        lista.append(i)
    return lista


def iterative_list_swap(l, left, right):
    while left < right:
        l[left], l[right] = l[right], l[left]

        left += 1
        right -= 1

    return l

def recursive_list_swap(l, left, right):
    if left != right:
        l[left], l[right] = l[right], l[left]

        return recursive_list_swap(l, left + 1, right - 1)

    return l

list1 = list_init(30)
list2 = list1.copy()

print(list1)
print(iterative_list_swap(list1, 10, 20))
print(recursive_list_swap(list2, 10, 20))
