def max(x, y):
    if x > y:
        return x
    else:
        return y


T = int(input())

for i in range(T):
    N = int(input())
    data = [None] * N
    for j in range(N):
        data[j] = [0] * (j + 1)

    for j in range(N):
        line = input().split()
        data[j] = list(map(int, line))

    for j in range(N - 1):
        M = N - 1 - j
        for k in range(M):
            data[M - 1][k] = max(data[M][k], data[M][k + 1]) + data[M - 1][k]

    print(data[0][0])
