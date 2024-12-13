def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: arrays with 1 or no elements are already sorted

    # Choose the pivot (last element in this case)
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elements smaller than or equal to the pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than the pivot

    # Recursion on the left and right subarrays
    return quick_sort(left) + [pivot] + quick_sort(right)

# Test
unsorted_array = [10, 80, 30, 90, 40, 50, 70]
sorted_array = quick_sort(unsorted_array)
print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)
