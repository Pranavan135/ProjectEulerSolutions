N = int(input())

I = []
O = [[0 for j in range(N)] for i in range(N)]

for _ in range(N):
    I.append(list(map(int, input().split(' '))))

for i in range(N):
    O[i][0] = I[i][0]

for j in range(1, N):
    O[0][j] = O[0][j - 1] + I[0][j];
    for i in range(1, N):
        O[i][j] = min(O[i][j - 1], O[i - 1][j]) + I[i][j]
    for i in range(N - 2, -1, -1):
        O[i][j] = min(O[i + 1][j] + I[i][j], O[i][j])

print(min([row[N - 1] for row in O]))
