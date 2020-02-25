def checkMatrix(arr):
    result =''
    for i in range(len(arr)):
        if(arr[i][i] == 1):
            result = 1
        break
    else:
        result = 0
    return result

a = [[0, 0, 0, 1, 0],
[1, 1, 0, 0, 1],
[ 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1],
[ 0, 0, 1, 0, 0]]


way = checkMatrix(a)
if way == 0:
    print('the way is clear')
else:
    print('the way is blocked')




#
# print(len(a))

