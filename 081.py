N = int(input())

I = []
for i in range(N):
    I.append(list(map(int, input().split(' '))))

M = [[0 for x in range(N)] for y in range(N)]

M[0][0] = I[0][0]

for i in range(1, N):
    M[0][i] = M[0][i - 1] + I[0][i]
    M[i][0] = M[i - 1][0] + I[i][0]

for i in range(1, N):
    for j in range(1, N):
        M[i][j] = min(M[i - 1][j], M[i][j - 1]) + I[i][j]

print(M[N - 1][N - 1])
