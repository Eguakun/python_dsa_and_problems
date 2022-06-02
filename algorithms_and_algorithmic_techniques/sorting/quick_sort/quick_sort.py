from algorithms_and_algorithmic_techniques.helpers import get_a_list as g


# Divide and conquer algoirthm
# Running Time - worst case O(n^2)
# - O(n * log(n)) average and best case

# Quicksort steps:
# - 1. Chose pivot element (Usually first, last, or random)
# - 2a. Stores elements less than pivot in left subarray
# - 2b. Stores elements greater than pivot in right subarray
# - 3. Call quicksort recursively on left subarray


def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


my_list = g.generate_random_list(10)
print(my_list)

quicksort(my_list, 0, len(my_list) - 1)
print(my_list)