def findmin(arr):
    m = arr[0]
    indexm = 0
    for i in range(1, len(arr)):
        if arr[i] < m:
            m = arr[i]
            indexm = i
    return indexm

def sortm(arr):
    newarr = []
    for i in range(len(arr)):
        m = findmin(arr)
        newarr.append(arr.pop(m))
    return newarr
print(sortm([1,4,6,2,3,10]))
