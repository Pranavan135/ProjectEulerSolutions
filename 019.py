def zeller_congruence(year, month, day):
    if month == 1:
        month = 13
        year -= 1
    elif month == 2:
        month = 14
        year -= 1
    K = year % 100
    J = year // 100
    return (day + (13 * (month + 1) // 5) + K + (K // 4) + (J // 4) + 5 * J) % 7


def compare_dates(date1, date2):
    Y1, M1, D1 = date1[0], date1[1], date1[2]
    Y2, M2, D2 = date2[0], date2[1], date2[2]

    if Y1 < Y2:
        return True
    elif Y1 == Y2:
        return M1 <= M2
    else:
        return False


def find_sundays(date1, date2):
    Y1, M1, D1 = date1[0], date1[1], date1[2]
    counter = 0
    a, b = Y1, M1

    if M1 < 12 and D1 > 1:
        b += 1
    elif M1 == 12 and D1 > 1:
        b, a = 1, a + 1

    while compare_dates([a, b, 1], date2):
        if zeller_congruence(a, b, 1) == 1:
            counter += 1
        if b == 12:
            a, b = a + 1, 1
        else:
            b += 1
    return counter


T = int(input())

for _ in range(T):
    date1 = list(map(int, input().split()))
    date2 = list(map(int, input().split()))
    print(find_sundays(date1, date2))
