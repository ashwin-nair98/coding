# Question: Given a list of stock prices, find the maximum profit that can be made by buying
# and selling one unit of stock


def maxPrice(stocks):
    minUntilNow = stocks[0]
    maxProfit = 0

    for i in range(1, len(stocks)):
        if stocks[i] < minUntilNow:
            minUntilNow = stocks[i]
        else:
            maxProfit = max(maxProfit, stocks[i] - minUntilNow)
    return maxProfit


def expect(a, b):
    result = a == b
    print("Test for " + str(a) + (" passed!" if result else " failed!"))


a = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
maxProfit = 30

expect(maxProfit, maxPrice(a))
