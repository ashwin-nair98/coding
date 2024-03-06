# Question: Partition an array A with a pivot i such that all A[x] <= A[i] appears first


def partition(arr, i):
    start = 0
    pivot = arr[i]
    for j in range(len(arr)):
        while start < len(arr) and arr[start] < pivot:
            start += 1
        if start >= len(arr):
            break
        if arr[j] <= pivot:
            arr[start], arr[j] = arr[j], arr[start]
            start += 1
    return arr


# Test
def expect(a, b):
    result = a == b
    print("Test for " + str(a) + (" passed!" if result else " failed!"))


a = [0, 1, 2, 0, 2, 1, 1]
i = 3
res = [0, 0, 1, 2, 2, 1]

expect(a, partition(a, i))
