T = int(input())

for _ in range(T):
    N = int(input())
    val = 2 ** N
    s = str(val)
    summation = 0
    for i in range(len(s)):
        summation += int(s[i])

    print(summation)
