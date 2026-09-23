#best time to buy and stock
def besttimetosell(prices):
    if not prices :
        return 0
    max_profit=0
    min_price=float('inf')
    for price in prices:
        if price<min_price:
            min_price=price
        profit=price-min_price

        max_profit=max(profit,max_profit)
    return max_profit
prices=[7,2,1,5,6,4,8]
print(besttimetosell(prices))
