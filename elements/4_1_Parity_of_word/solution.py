# The parity of a word is 1 if the number of 1 bits in the word is odd, else it's 0
#
# Question: Find the parity of a word?


# Solution 1
# Brute force to find all 1s
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


# Solution 2
# Instead of checking for every bit, check for last set bit
# Use x & x - 1 to remove the last set bit
def parity2(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


# Test
def expect(a, b):
    result = a == b
    print("Test for " + str(a) + (" passed!" if result else " failed!"))


print("Parity 1")
a = 0b1010
expect(0, parity(a))
a = 0b1110
expect(1, parity(a))
print("Parity 2")
a = 0b1010
expect(0, parity2(a))
a = 0b1110
expect(1, parity2(a))
