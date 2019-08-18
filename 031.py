def total_num_ways(limit, coins):
    ways = [0] * (limit + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, limit + 1):
            ways[j] += ways[j - coin]
    return ways


mod = 10 ** 9 + 7
N = 10 ** 5
coins = [1, 2, 5, 10, 20, 50, 100, 200]

ways = total_num_ways(N, coins)

T = int(input())

for _ in range(T):
    print(ways[int(input())] % mod)
