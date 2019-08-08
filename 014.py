MAX = 5 * (10 ** 6) + 1
LENGTH = [0] * MAX
MAXI = [0] * MAX
LENGTH[1], MAXI[1] = 1, 1

def collatz_seq(n):
    if n <= MAX:
        res = LENGTH[n]
        if not res :
            res = LENGTH[n] = 1 + collatz_seq(3 * n + 1 if n % 2 == 1 else n // 2)
    else:
        res = 1 + collatz_seq(3 * n + 1 if n % 2 == 1 else n // 2)

    return res


for i in range(2, MAX):
    LENGTH[i] = collatz_seq(i)
    MAXI[i] = i if LENGTH[i] >= LENGTH[MAXI[i-1]] else MAXI[i-1]



T = int(input())

for _ in range(T):
    N = int(input())
    print(MAXI[N])


