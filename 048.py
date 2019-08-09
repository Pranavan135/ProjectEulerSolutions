N = int(input())
M = 10 ** 10
s = sum(pow(n, n, M) for n in range(1, N + 1))
print(s % M)
