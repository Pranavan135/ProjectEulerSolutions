T = int(input())

for _ in range(T):
    n = int(input()) // 2 + 1
    print((4 * n - 3 + 10 * n * (n - 1) + 16 * n * (n + 1) * (2 * n + 1) // 6 - 24 * n * (n + 1) + 32 * n) % (
                10 ** 9 + 7))
