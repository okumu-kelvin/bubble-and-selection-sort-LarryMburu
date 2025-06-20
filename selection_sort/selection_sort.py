def selection_sort(unsorted_list):
    unsorted = unsorted_list[:]
    n = len(unsorted)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if unsorted[j] < unsorted[min_index]:
                min_index = j
        if min_index != i:ts
            unsorted[i], unsorted[min_index] = unsorted[min_index], unsorted[i]

    return unsorted
