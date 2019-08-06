T = int(input())
for _ in range(T):
    n = int(input().strip())
    n = n - 1
    x1 = n // 3
    x2 = n // 5
    x3 = n // 15
    s = (3 * x1 * (x1 + 1) // 2) + (5 * x2 * (x2 + 1) // 2) - (15 * x3 * (x3 + 1) // 2)
    print(s)
