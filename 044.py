import math

numbers = list(map(int, input().split()))

N = numbers[0]
K = numbers[1]


def natural_number(p_m):
    n = (1 + math.sqrt(1 + 24 * p_m)) / 6
    return n.is_integer()


loc = [False] * (N + K)

for i in range(K + 1, N + 1):
    p_n = int(i * (3 * i - 1) / 2)
    p_n_k = int((i - K) * (3 * (i - K) - 1) / 2)

    if natural_number(p_n - p_n_k) or natural_number(p_n + p_n_k):
        print(p_n)
