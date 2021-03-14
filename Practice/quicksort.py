# From "Algorithms Notes for Professionals"
# Quicksort is a sorting algorithm that picks an element ("the pivot") and reorders the array forming two partitions
# such that all elements less than the pivot come before it and all elements greater come after. The algorithm is then
# applied recursively to the partitions until the list is sorted.

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print (quicksort([3,6,8,10,1,2,1]))