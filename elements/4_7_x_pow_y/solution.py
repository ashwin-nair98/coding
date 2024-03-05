# Question: Find x^y

# x^y = x2^y/2 or x * x2^y/2
def power(x, y):
    result = 1.0
    power = y
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result


# Test
def expect(a, b):
    result = a == b
    print("Test for " + str(a) + " : " + (" passed!" if result else " failed!"))


x, y = 2, 3
expect(8, power(x, y))
x, y = 3, 3
expect(27, power(x, y))
x, y = 4, 3
expect(64, power(x, y))
