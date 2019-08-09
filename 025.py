fib = [1, 1]

i = 2
while True:
    next_fib_no = fib[i - 1] + fib[i - 2]
    fib.append(next_fib_no)
    i += 1
    if len(str(next_fib_no)) == 5000:
        break

desired = [0] * 5001
k = 0
for i in range(1, 5001):
    while i != len(str(fib[k])):
        k += 1
    desired[i] = k + 1

for _ in range(int(input())):
    print(desired[int(input())])
