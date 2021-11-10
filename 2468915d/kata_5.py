def count_change(money, coins):
    count = 0

    for n in range(len(coins)):

        for c in coins[n:]:
            if money-coins[n] % c == 0:
                count += 1

    return count
