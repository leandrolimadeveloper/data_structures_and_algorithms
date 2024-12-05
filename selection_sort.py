def selection_sort(arr):
    n = len(arr)
    
    # Traverse the entire array
    for i in range(n):
        # Find the smallest element in the remaining subarray
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the smallest element with the first unsorted element
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Test the algorithm
unsorted_array = [64, 25, 12, 22, 11]
print("Original Array:", unsorted_array)

sorted_array = selection_sort(unsorted_array)
print("Sorted Array:", sorted_array)
