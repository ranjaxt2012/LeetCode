prices = [12, 3, 10, 6, 15]


def profit(stock_prices):
    # Start minimum price marker at first price
    min_stock_price = stock_prices[0]
    print "min_stock_price", min_stock_price

    # Start off with a profit of zero
    max_profit = 0

    for price in stock_prices:
        # Check to set the lowest stock price so far
        # print (min_stock_price, price)
        min_stock_price = min(min_stock_price, price)
        # print "min_stock_price at Min ", min_stock_price

        # Check the current price against our minimum for a profit
        # comparison against the max_profit
        comparison_profit = price - min_stock_price
        # print "comparison_profit", comparison_profit

        # Compare against our max_profit so far
        max_profit = max(max_profit, comparison_profit)
        # print max_profit

    return max_profit


def profit2(priceList):
    Stock_Min = prices[0]
    Profit = 0
    for price in priceList:
        TM = min(Stock_Min, price)
        if TM < Stock_Min:
            Stock_Min = TM

        TP = (price - Stock_Min)
        # print TP
        if TP > Profit:
            Profit = TP
    # print Stock_Min
    return Profit


print profit(prices)
print profit2(prices)


def process_list(list):
    RP = 1

    for i in list:
        RP = RP * i
    return RP


def MultiplyListWithMissingElement(list):
    out = []

    for i in range(len(list)):
        list.pop[i]
        out.append(process_list(list))

    return out


def MultiplyListWithMissingElement2(mylist):
    Total_product = 1
    Out = []

    for i in mylist:
        Total_product = Total_product * i

    print Total_product

    for i in mylist:
        Out.append(Total_product / i)
    return Out


def sqrt_number(array_between):
    for number in range(array_between[0], array_between[1], 1):
        possible_squrt_number = number // 2

        for i in range(possible_squrt_number, 1, -1):
            if (i * i) == number:
                return i

array_between = [9, 24]
print (sqrt_number(array_between))


mylist = [1, 2, 3, 4]
# print MultiplyListWithMissingElement(mylist)
print MultiplyListWithMissingElement2(mylist)
