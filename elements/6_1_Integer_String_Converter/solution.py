# Question: Implement a string to integer and vice versa converter
# without using int function


def convertToStr(n):
    ret = []
    if n == 0:
        return "0"
    neg = False
    if n < 0:
        neg = True
        n *= -1
    while n:
        x = n % 10
        ret.append(chr(48 + x))
        n //= 10

    return ("-" if neg else "") + "".join(ret[::-1])


def convertToInt(s):
    ret = 0
    neg = False
    for c in s:
        if c == "-":
            neg = True
        else:
            ret *= 10
            ret += ord(c) - 48

    return ret * (-1 if neg else 1)


print("Convert to STR: " + convertToStr(-500))

print("Convert to INT: " + str(convertToInt("-500") + 10))
