# Question: Replace a by two d's and remove b's


def replaceAndRemove(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == "b":
            del arr[i]
            i -= 1
            n -= 1
        elif arr[i] == "a":
            del arr[i]
            arr.append("d")
            arr.append("d")
            i -= 1
            n += 1
        i += 1
    return arr


print("Replace: " + str(replaceAndRemove(["a", "b", "c", "v"])))
