import random


def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def miller_rabin(n, k=10):
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True


N = int(input())

loop_no = 2

total_diagonal = 5
in_diagonal = 3
curr_1 = 3
curr_2 = 5
curr_3 = 7
r_1 = 2
r_2 = 4
r_3 = 6
while N <= (100 * in_diagonal / total_diagonal):
    loop_no = loop_no + 1
    r_1, r_2, r_3 = r_1 + 8, r_2 + 8, r_3 + 8
    curr_1, curr_2, curr_3 = curr_1 + r_1, curr_2 + r_2, curr_3 + r_3

    total_diagonal = total_diagonal + 4
    if miller_rabin(curr_1):
        in_diagonal = in_diagonal + 1

    if miller_rabin(curr_2):
        in_diagonal = in_diagonal + 1

    if miller_rabin(curr_3):
        in_diagonal = in_diagonal + 1

    if N > (100 * in_diagonal / total_diagonal):
        print(2 * loop_no - 1)
        break
