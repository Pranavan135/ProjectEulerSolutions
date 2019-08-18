fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def check_digit_factorial(num):
    fact_sum = 0
    str_num = str(num)

    for i in range(len(str_num)):
        fact_sum += fact[int(str_num[i])]

    return fact_sum % num == 0


s = 0
for i in range(10, int(input())):
    if check_digit_factorial(i):
        s += i

print(s)
