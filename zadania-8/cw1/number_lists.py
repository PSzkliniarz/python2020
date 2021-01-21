import random, math


def make_list(n):
    number_list = []
    for x in range(n):
        number_list.append(x)
    return number_list


def make_reverse_list(n):
    reverse_list = make_list(n)
    reverse_list.reverse()
    return reverse_list


def random_list(n):
    rand_list = make_list(n)
    random.shuffle(rand_list)
    return rand_list


def almost_sorted(n):
    almost_sorted_list = make_list(n)
    for x in range(1, n):
        if random_exchanges():
            almost_sorted_list[x], almost_sorted_list[x-1] = almost_sorted_list[x-1], almost_sorted_list[x]
    return almost_sorted_list


def random_exchanges():
    if random.randint(0, 1):
        return True
    else:
        return False


def almost_sorted_reverse(n):
    reverse_almost_sorted = almost_sorted(n)
    reverse_almost_sorted.reverse()
    return reverse_almost_sorted


def gauss_list(n):
    gauss_number_list = []
    for x in range(n):
        gauss_number_list.append(random.gauss(1, 1))
    return gauss_number_list


def sqrt_number(n):
    limit = int(math.sqrt(n))
    sqrt_numbers = []
    for x in range(n):
        sqrt_numbers.append(random.randint(0, limit))
    return sqrt_numbers


