MAX = 5 * (10 ** 5) + 1
SUM = [1] * MAX

for i in range(2, MAX):
    for j in range(2 * i, MAX, i):
        SUM[j] += i

AMICABLE_SUM = [0] * MAX

for i in range(2, MAX):
    if i != SUM[i] < MAX and i == SUM[SUM[i]]:
        AMICABLE_SUM[i] = AMICABLE_SUM[i - 1] + i
    else:
        AMICABLE_SUM[i] = AMICABLE_SUM[i - 1]

T = int(input())

for _ in range(T):
    print(AMICABLE_SUM[(int(input()))])
