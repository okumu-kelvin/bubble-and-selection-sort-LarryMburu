def selection_sort(lst):
    n = len(lst)  

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j 
        if min_index != i:
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp

    return lst  
