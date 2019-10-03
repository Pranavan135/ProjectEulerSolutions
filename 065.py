def e_cont_frac(n):
    seq = [2 * (i+1) // 3 if i%3 == 2 else 1 for i in range(n)]
    seq[0] += 1
    return seq


def contfrac_to_frac(seq):
    num, den = 1, 0
    for u in reversed(seq):
        num, den = den + num*u, num
    return num, den


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

N = int(input())
seq = e_cont_frac(N)
num, den = contfrac_to_frac(seq)

print(sum_digits(num))
