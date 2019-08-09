import itertools

N = int(input())
primes = [2, 3, 5, 7, 11, 13, 17]
l = []
for i in range(N + 1):
    l.append(i)

s = itertools.permutations(l)
nums = []
for i in s:
    num = ''
    if N >= 5 and not (i[5] == 5 or i[5] == 0):
        continue
    for j in range(N + 1):
        num = num + str(i[j])

    is_pandigit = True
    for k in range(N - 2):
        if int(num[k + 1: k + 4]) % primes[k] == 0:
            continue
        else:
            is_pandigit = False
            break
    if is_pandigit:
        nums.append(int(num))

print(sum(nums))
