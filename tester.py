def bubbleSort(arr):
    l = len(arr)

    for i in range(l):
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [12,6,45,4654,132,48,987,1]

bubbleSort(arr);

for i in range(len(arr)):
    print("%d" % arr[i]),
