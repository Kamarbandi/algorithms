arr = [3,5,6,1,2,7,4]

def mergerSort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = mergerSort(arr[:middle])
    right = mergerSort(arr[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result


print(mergerSort(arr))
