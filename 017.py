T = int(input())
list1 = ['Billion', 'Million', 'Thousand', 'Hundred']
list2 = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
list3 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
list4 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
for i in range(T):
    N = int(input())

    number = ''

    i = 0
    while N > 0:
        a = N // 1000
        b = N % 1000
        str = ''
        j = 0
        prev_y = -1
        while b > 0:
            x = b // 10
            y = b % 10
            if y != 0:
                if j == 0:
                    str = list3[y - 1] + ' ' + str
                elif j == 1:
                    if y == 1:
                        str = list4[prev_y]
                    else:
                        str = list2[y - 1] + ' ' + str
                elif j == 2:
                    str = list3[y - 1] + ' ' + list1[3] + ' ' + str
            b = x
            j = j + 1
            prev_y = y

        if str.strip():
            if i == 0:
                number = str.strip()
            if i == 1:
                number = str.strip() + ' ' + list1[2] + ' ' + number
            if i == 2:
                number = str.strip() + ' ' + list1[1] + ' ' + number
            if i == 3:
                number = str.strip() + ' ' + list1[0] + ' ' + number
            number = number.strip()
        i = i + 1
        N = a
    print(number)
