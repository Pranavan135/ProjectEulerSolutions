LIMIT = 28124
SUM = [1] * LIMIT
SUM[1] = 0

for i in range(2, LIMIT):
    for j in range(2 * i, LIMIT, i):
        SUM[j] += i

abundant = []
desired = [0] * LIMIT

for i in range(12, LIMIT):
    if i < SUM[i]:
        abundant.append(i)
        desired[i] = 1

for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        number = abundant[i] + abundant[j]
        if number < LIMIT:
            desired[number] = 1
        else:
            break

T = int(input())

for _ in range(T):
    N = int(input())
    if N >= LIMIT:
        print('YES')
    else:
        print("YES") if desired[N] else print("NO")
