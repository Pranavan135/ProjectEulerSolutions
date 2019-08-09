val = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600]


def find_string(pos):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    str = []
    for i in range(13):
        index = pos // val[12 - i]
        pos %= val[12 - i]
        str.append(chars[index])
        chars.remove(chars[index])

    return ''.join(str)


T = int(input())

for _ in range(T):
    print(find_string(int(input()) - 1))
