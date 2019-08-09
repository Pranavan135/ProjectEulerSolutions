def is_palindrome(n):
    return str(n) == str(n)[::-1]


def reverse_and_add(number):
    reverse = int(str(number)[::-1])
    return reverse + number


def count(limit):
    d = {0: 1}

    for i in range(1, limit + 1):
        if is_palindrome(i):
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            continue
        else:
            r = i
            for j in range(60):
                r = reverse_and_add(r)
                if is_palindrome(r):
                    if r in d:
                        d[r] += 1
                    else:
                        d[r] = 1
                    break
    return d


N = int(input())

counts = count(N)

print(max(counts, key=counts.get), max(counts.values()))
