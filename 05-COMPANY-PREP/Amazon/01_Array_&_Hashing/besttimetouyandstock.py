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
#
def best_time(prices):
    if not prices:
        return None
    min_price=float('inf')
    maximum=0

    for price in prices:
        if price<min_price:
            min_price=price
        profit=price-min_price

        maximum=max(profit,maximum)
    return maximum
while True:
    user_input=input("enter an array: ")
    if not user_input.lower=='exit':
        break

    if user_input.strip():
        print("please enter input!")
        continue
    try:
        prices=list(map(int,user_input.split()))
        print(best_time(prices))
    except ValueError:
        print("Invalid input! try again with valid input")


#
def buy_stock(prices):
    minimum_price = float('inf')
    maximum_profit = 0
    maximum_index = 0

    for i in range(len(prices)):
        if prices[i] < minimum_price:
            minimum_price = prices[i]

        profit = prices[i] - minimum_price

        if profit > maximum_profit:
            maximum_profit = profit
            maximum_index = i

    return maximum_index

while True:
    user_input=input("enter an array: ")
    if user_input.lower()=='exit':
        break

    if not user_input.strip():
        print("please enter input!")
        continue
    try:
        prices=list(map(int,user_input.split()))
        print(buy_stock(prices))
    except ValueError:
        print("Invalid input! try again with valid input")
