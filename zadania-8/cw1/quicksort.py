import number_lists as nl
import time


def pivoting(tab, start, end):
    i = (start - 1)
    x = tab[end]

    for j in range(start, end):
        if tab[j] <= x:

            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[end] = tab[end], tab[i + 1]
    return i + 1


def quickSortIterative(tab, end, start=0):

    size = end - start + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = start
    top = top + 1
    stack[top] = end

    while top >= 0:

        end = stack[top]
        top = top - 1
        start = stack[top]
        top = top - 1

        p = pivoting(tab, start, end)

        if p - 1 > start:
            top = top + 1
            stack[top] = start
            top = top + 1
            stack[top] = p - 1

        if p + 1 < end:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = end


def quicksort_all_lists(string_n):
    functions_list = ['nl.make_list', 'nl.make_reverse_list', 'nl.random_list', 'nl.almost_sorted',
                       'nl.almost_sorted_reverse', 'nl.gauss_list', 'nl.sqrt_number']

    quicksort_n = string_n - 1

    string_n = "(" + str(string_n) + ")"
    for x in range(len(functions_list)):

        result = eval(functions_list[x] + string_n)
        current_list = list(result)
        print(current_list)

        time_start = time.time()
        quickSortIterative(current_list, quicksort_n)
        time_end = time.time()

        print(current_list)
        print(functions_list[x], 'czas wykonania dla n=', string_n, ' : ', time_end - time_start, '\n')


if __name__ == '__main__':

    n = 200
    quicksort_all_lists(n)