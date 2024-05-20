def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        opor = arr[0]
        back = [i for i in arr if i < opor]
        forward = [i for i in arr if i > opor]
        return quicksort(back) + [opor] + quicksort(forward)

print(quicksort([2, 4, 1, 5, 90, 100]))
