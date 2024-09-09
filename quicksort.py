def quicksort(arr):
    if 2 < len(arr):
        pivot = arr[0]
        less = []
        for item in arr[1:]:
            if item <= pivot:
                less.append(item)
        greater = []
        for item in arr[1:]:
            if item > pivot:
                greater.append(item)
        return quicksort(less) + [pivot] + quicksort(greater)
    else:
        return arr

print(quicksort([13, 2, 4, 66]))
print(quicksort(['h', 'd', 'a', 'c']))

