T = int(input())

boundaries = [9]

for i in range(1, 18):
    boundaries.append(boundaries[len(boundaries) - 1] + (10 ** (i + 1) - 10 ** i) * (i + 1))

for i in range(T):
    numbers = list(map(int, input().split()))
    s = 1
    for j in range(len(numbers)):
        temp = -1
        for k in range(len(boundaries)):
            if numbers[j] <= boundaries[k]:
                temp = k
                break
        if k == 0:
            s = s * numbers[j]
        else:
            tot = boundaries[temp] - boundaries[temp - 1]
            a = (numbers[j] - boundaries[temp - 1]) // (k + 1)
            b = (numbers[j] - boundaries[temp - 1]) % (k + 1)
            if b == 0:
                desired = 10 ** k - 1 + a
                s = s * int(str(desired)[len(str(desired)) - 1])
            else:
                desired = 10 ** k + a
                s = s * int(str(desired)[b - 1])

    print(s)
