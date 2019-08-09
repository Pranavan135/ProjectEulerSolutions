numbers = list(map(int, input().split()))

N = numbers[0]
K = numbers[1]

list = [1] * 2

count = 0
i = 1
while i + 1 <= N:
    list_new = [0] * (i + 2)
    list_new[0] = 1
    list_new[i + 1] = 1
    for j in range(i):
        x = list[j] + list[j + 1]
        if x > K:
            list_new[j + 1] = K + 1
            count = count + 1
        else:
            list_new[j + 1] = x
    list = list_new
    i = i + 1
print(count)
