T = int(input())

D = 10 ** 9 + 7

for _ in range(T):
    numbers = list(map(int, input().split()))
    M, N = numbers[0], numbers[1]
    numerator, denominator = 1, 1
    for i in range(N):
        numerator, denominator = numerator * (M + i + 1), denominator * (i + 1)

    print((numerator // denominator) % D)
