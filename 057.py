N = int(input())

numerator = 2
denominator = 1
for i in range(N):
    new_num, new_den = numerator + denominator, numerator
    if len(str(new_num)) > len(str(new_den)):
        print(i + 1)
    numerator, denominator = 2 * numerator + denominator, numerator
