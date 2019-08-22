from math import log2

N = int(input())

TRACKED = [False] * (N + 1)

numbers = []
bound = int(log2(N))
diff_powers = set([])
current = 0
for i in range(1, bound + 1):
    current = current + 1
    for j in range(2, N + 1):
        val = i * j
        if val not in diff_powers:
            diff_powers.add(val)
    numbers.append(len(diff_powers))

diffs = 0

for i in range(2, N + 1):
    if not TRACKED[i]:
        a = i
        counter = 0
        while a <= N:
            TRACKED[a] = True
            a = a * i
            counter += 1
        diffs = diffs + numbers[counter - 1]

print(diffs)

