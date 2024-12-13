function quickSort(arr) {
    // Base case: arrays with 0 or 1 element are already sorted
    if (arr.length <= 1) {
        return arr
    }

    const pivot = arr[arr.length - 1]
    const left = [] // Elements smaller than or equal to the pivot
    const right = [] // Elements greater than the pivot

    // Partition the array into subarrays
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] <= pivot) {
            left.push(arr[i])
        } else {
            right.push(arr[i])
        }
    }

    // Recursively sort the subarrays and combine the result
    return [...quickSort(left), pivot, ...quickSort(right)]
}

// Test the algorithm
const unsortedArray = [10, 15, 23, 25, 22, 69, 80, 100, 45, 85, 38]
console.log('Unsorted array', unsortedArray)

const sortedArray = quickSort(unsortedArray)
console.log('Sorted array', sortedArray)