# This code is taken from the itertools library
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def change(money, coins, count):
    diff = money-coins[0]
    # print(diff)
    if(diff == 0):
        # print("Added\n----")
        return count+1

    if(diff > 0):
        # print(coins)
        if(len(coins) > 1):
            count = change(diff, coins[1:], count)
        if(len(coins) == 1):
            count = change(diff, coins, count)

    return count


def count_change(money, coins):
    count = 0
    for i in range(1, len(coins)+1):
        for comb in combinations(coins, i):
            # print(comb)
            # if(len(comb) == len(coins)-1):
            count = change(money, comb, count)
    if(count != 0):
        count = count+1
    return count
