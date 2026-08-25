# BEST TIME TO BUY AND SELL STOCK

'''Given an array of stock prices, choose one day to buy
and a future day to sell.
Find the maximum profit possible.
If no profit is possible, return 0.

Example:
[7,1,5,3,6,4] → 5
[7,6,4,3,1] → 0'''

#
from re import M


def MaxProfit(prices):
    minPrice=prices[0]
    maxProfit=0
    for price in prices:
        if price<minPrice:
            minPrice=price
        Profit=price - minPrice
        maxProfit=max(maxProfit,Profit)
    return maxProfit
prices=list(map(int,input("enter an array").split()))
print(MaxProfit(prices))
