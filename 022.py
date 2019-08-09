N = int(input())

words = [""] * N

for i in range(N):
    words[i] = input()

words.sort()

Q = int(input())

for _ in range(Q):
    w = input()
    I = words.index(w)

    val = 0
    for c in w:
        val += ord(c) - 64

    print(val * (I + 1))
