T = int(input())

for _ in range(T):
    numbers = list(map(int, input().split()))
    N, K = numbers[0], numbers[1]

    NUM  = input()
    maxi = 0
    for i in range(N-K+1):
        s = NUM[i:i+K]
        mul = 1

        for j in range(len(s)):
            mul *= int(s[j])
        if mul > maxi:
            maxi = mul

    print(maxi)
