# ugly solution, but still pass all the test cases
# the for loop bounds can be tightened
from math import sqrt

def check_pandigit(a, b, c, l):
    pandigit = [True] * l

    for s in [a, b, c]:
        for index in range(len(s)):
            num = ord(s[index]) - 49
            if l > num >= 0 and pandigit[num]:
                pandigit[num] = False
            else:
                return False

    return not any(pandigit)


N = int(input())

product = N // 2

limit = int(sqrt(10 ** product - 1))

l = set([])
for i in range(1, limit):
    for j in range(1, 10 ** product):
        if len(str(i*j)) > product:
            break
        if check_pandigit(str(i), str(j), str(i * j), N):
            l.add(i * j)

print(sum(l))
