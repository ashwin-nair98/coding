# Question: create an array  that is the subset of a given array and
# of given size. All subsets should be equally likely
import random


def randArr(arr, k):
    for i in range(k):
        rand = random.randint(i, len(arr) - 1)
        arr[rand], arr[i] = arr[i], arr[rand]
    # Same array is modified to inlcude the answer from elements 0 -> k - 1
    return arr


arr = [3, 7, 5, 11, 45]
print("Answer for " + str(arr) + " is " + str(randArr(arr, 3)))
