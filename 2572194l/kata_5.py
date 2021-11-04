def count_change(money, coins):
    count = 0
    for i in coins:
        if(money % i == 0):
            count += 1
    for i in coins:
        money -= i
        if(money == 0):
            count += 1
    return count