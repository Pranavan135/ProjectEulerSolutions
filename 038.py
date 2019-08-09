numbers = list(map(int, input().split()))

N = numbers[0]
K = numbers[1]

pan8 = [18, 78, 1728, 1764, 1782, 1827, 2178, 2358, 2718, 2817, 3564, 3582, 4176, 4356]
pan9 = [9, 192, 219, 273, 327, 6729, 6792, 6927, 7269, 7293, 7329, 7692, 7923, 7932, 9267, 9273, 9327]

if K == 8:
    for i in range(len(pan8)):
        if pan8[i] < N:
            print(pan8[i])
elif K == 9:
    for i in range(len(pan9)):
        if pan9[i] < N:
            print(pan9[i])
