import math


def square(n):
    sq = math.sqrt(n)
    return sq.is_integer()


def is_prime(n):
    if n == 1:
        return False

    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


T = int(input())

for i in range(T):
    x = int(input())
    count = 0
    num = 1

    while x - num * num * 2 > 2:
        if is_prime(x - num * num * 2):
            count = count + 1
        num = num + 1

    print(count)
