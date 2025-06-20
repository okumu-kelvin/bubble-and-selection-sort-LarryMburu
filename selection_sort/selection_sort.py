def selection_sort(unsorted_list):
    n = len(unsorted_list)  

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j 
        if min_index != i:
            temp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[min_index]
            unsorted_list[min_index] = temp

    return unsorted_list  
