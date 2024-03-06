# Question: Traverse 2D array in spiral order (clockwise)


def spiralOrder(arr):
    n = len(arr)

    index = 0

    ret = []
    while index * 2 < n:
        i, j = index, index
        while j < n - index:
            ret.append(arr[i][j])
            j += 1
        j -= 1
        i += 1
        while i < n - index:
            print("Accessing: " + str(i) + ":" + str(j))
            ret.append(arr[i][j])
            i += 1
        i -= 1
        j -= 1
        while j >= index:
            ret.append(arr[i][j])
            j -= 1
        j += 1
        i -= 1
        while i > index:
            ret.append(arr[i][j])
            i -= 1
        index += 1
    return ret


i = 0
n = 4
arr = [[i := i + 1 for _ in range(n)] for __ in range(n)]

print("Original: " + str(arr))
print(str(spiralOrder(arr)))
