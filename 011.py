N = 20

numbers = [[0] * N for i in range(N)]

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        numbers[i][j] = l[j]

maxi = 0

for i in range(N - 3):
    for j in range(N - 3):
        val1 = numbers[i][j] * numbers[i][j + 1] * numbers[i][j + 2] * numbers[i][j + 3]
        val2 = numbers[i][j] * numbers[i + 1][j] * numbers[i + 2][j] * numbers[i + 3][j]
        val3 = numbers[i][j] * numbers[i + 1][j + 1] * numbers[i + 2][j + 2] * numbers[i + 3][j + 3]
        val4 = numbers[i][N - j - 1] * numbers[i + 1][N - j - 2] * numbers[i + 2][N - j - 3] * numbers[i + 3][N - j - 4]

        if val1 > maxi:
            maxi = val1
        if val2 > maxi:
            maxi = val2
        if val3 > maxi:
            maxi = val3
        if val4 > maxi:
            maxi = val4

for i in range(17, 20):
    for j in range(N - 3):
        val1 = numbers[i][j] * numbers[i][j + 1] * numbers[i][j + 2] * numbers[i][j + 3]
        val2 = numbers[j][i] * numbers[j + 1][i] * numbers[j + 2][i] * numbers[j + 3][i]
        if val1 > maxi:
            maxi = val1
        if val2 > maxi:
            maxi = val2

print(maxi)
