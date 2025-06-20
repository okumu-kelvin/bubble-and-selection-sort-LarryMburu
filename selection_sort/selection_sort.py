def selection_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        min_idx = i
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_idx]:
                min_idx = j
        unsorted_list[i], unsorted_list[min_idx] = unsorted_list[min_idx], unsorted_list[i]
    return unsorted_list
