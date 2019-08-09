import itertools


def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


l1 = []
s1 = itertools.permutations([1, 2, 3, 4])
for i in s1:
    number = i[0] * 1000 + i[1] * 100 + i[2] * 10 + i[3]
    if is_prime(number):
        l1.append(number)

max1 = max(l1)

s2 = itertools.permutations([1, 2, 3, 4, 5, 6, 7])
l2 = []
for i in s2:
    number = i[0] * 1000000 + i[1] * 100000 + i[2] * 10000 + i[3] * 1000 + i[4] * 100 + i[5] * 10 + i[6]
    if is_prime(number):
        l2.append(number)

max2 = max(l2)

T = int(input())

for i in range(T):
    x = int(input())
    if len(str(x)) <= 3:
        print(-1)
    elif 7 > len(str(x)) > 4:
        print(max1)
    elif len(str(x)) > 7:
        print(max2)
    elif len(str(x)) == 4:
        if l1[0] > x:
            print(-1)
        elif max1 <= x:
            print(max1)
        else:
            count = -1
            for j in range(len(l1)):
                if l1[j] > x:
                    count = j - 1
                    break

            print(l1[count])
    elif len(str(x)) == 7:
        if l2[0] > x:
            print(max1)
        elif max2 <= x:
            print(max2)
        else:
            count = -1
            for j in range(len(l2)):
                if l2[j] > x:
                    count = j - 1
                    break

            print(l2[count])
