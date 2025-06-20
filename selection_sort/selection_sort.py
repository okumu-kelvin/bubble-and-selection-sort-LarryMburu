def selection_sort(arr):
    # Make a copy to avoid modifying the original list
    sorted_list = arr[:]

    n = len(sorted_list)
    for i in range(n):
        # Assume the current position holds the smallest value
        min_index = i
        # Search for the smallest value in the remaining unsorted part
        for j in range(i + 1, n):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j
        # Swap the found minimum element with the current element
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]

    return sorted_list
