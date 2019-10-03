from math import sqrt, floor

T = int(input())

for _ in range(T):
    t_n = int(input())
    n = (-1 + sqrt(1 + 8 * t_n)) / 2

    if floor(n) == n:
        print(int(n))
    else:
        print(-1)
