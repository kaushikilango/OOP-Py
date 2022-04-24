def sell_buy(x):
    max_cost = 0
    for i in range(0, len(x)):
        for j in range(i+1, len(x)):
            if (x[i] < x[j] and x[j] - x[i] > max_cost):
                max_cost = x[j] - x[i]
    return max_cost


print(sell_buy([7, 1, 5, 3, 6, 4]))
