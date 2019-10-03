# Disclaimer - Long source code ahead
# This passes all the test cases, this can be done better.

cardsD = ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD']
cardsH = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH']
cardsC = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC']
cardsS = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS']

cards = cardsD + cardsH + cardsC + cardsS

s1 = 'Player 1'
s2 = 'Player 2'


def card_no(card):
    return cards.index(card)


def check_royal_flush(hand):
    return (hand[4] % 13 == 12) and (hand[4] - hand[3] == 1) and (hand[3] - hand[2] == 1) and (
                hand[2] - hand[1] == 1) and (hand[1] - hand[0] == 1)


def check_straight_flush(hand):
    return (hand[4] % 13 >= 4) and (hand[4] - hand[3] == 1) and (hand[3] - hand[2] == 1) and (
                hand[2] - hand[1] == 1) and (hand[1] - hand[0] == 1)


def check_four_of_a_kind(hand):
    counter = [0] * 13
    for num in hand:
        counter[num % 13] += 1

    return 4 in counter


def check_full_house(hand):
    counter = [0] * 13
    for num in hand:
        counter[num % 13] += 1

    return 3 in counter and 2 in counter


def check_flush(hand):
    return range_check(0, 12, hand) or range_check(13, 25, hand) or range_check(26, 38, hand) or range_check(39, 51,
                                                                                                             hand)


def range_check(start, end, hand):
    for i in range(len(hand)):
        if start <= hand[i] <= end:
            continue
        else:
            return False
    return True


def check_straight(hand):
    for i in range(len(hand)):
        hand[i] = hand[i] % 13

    hand.sort()

    res = [0, 1, 2, 3, 12] == hand
    return check_straight_flush(hand) or res


def check_three_of_a_kind(hand):
    counter = [0] * 13
    for num in hand:
        counter[num] += 1
    return 3 in counter


def check_two_pairs(hand):
    counter = [0] * 13
    for num in hand:
        counter[num] += 1
    return counter.count(2) == 2


def check_one_pair(hand):
    counter = [0] * 13
    for num in hand:
        counter[num] += 1

    return 2 in counter


def hand_status(hand):
    if check_royal_flush(hand):
        return 10
    elif check_straight_flush(hand):
        return 9
    elif check_four_of_a_kind(hand):
        return 8
    elif check_full_house(hand):
        return 7
    elif check_flush(hand):
        return 6
    elif check_straight(hand):
        return 5
    elif check_three_of_a_kind(hand):
        return 4
    elif check_two_pairs(hand):
        return 3
    elif check_one_pair(hand):
        return 2
    else:
        return 1


def tie_breaker_1(first_hand, second_hand):
    for i in range(len(first_hand)):
        if first_hand[4 - i] == second_hand[4 - i]:
            continue
        else:
            if first_hand[4 - i] > second_hand[4 - i]:
                print(s1)
                return
            else:
                print(s2)
                return


def tie_breaker_2(first_hand, second_hand):
    counter1 = [0] * 13
    for num in first_hand:
        counter1[num % 13] += 1

    counter2 = [0] * 13
    for num in second_hand:
        counter2[num % 13] += 1

    if counter1.index(2) > counter2.index(2):
        print(s1)
        return
    if counter1.index(2) < counter2.index(2):
        print(s2)
        return

    counter1.remove(2)
    counter2.remove(2)

    for i in range(len(counter1)):
        if counter1[11 - i] == counter2[11 - i]:
            continue
        else:
            if counter1[11 - i] > counter2[11 - i]:
                print(s1)
                return
            else:
                print(s2)
                return


def tie_breaker_3(first_hand, second_hand):
    counter1 = [0] * 13
    for num in first_hand:
        counter1[num % 13] += 1

    counter2 = [0] * 13
    for num in second_hand:
        counter2[num % 13] += 1

    pairs1 = [i for i, e in enumerate(counter1) if e == 2]
    pairs2 = [i for i, e in enumerate(counter2) if e == 2]

    if counter1[pairs1[1]] > counter2[pairs2[1]]:
        print(s1)
        return
    if counter1[pairs1[1]] < counter2[pairs2[1]]:
        print(s2)
        return

    if counter1[pairs1[0]] > counter2[pairs2[0]]:
        print(s1)
        return
    if counter1[pairs1[0]] < counter2[pairs2[0]]:
        print(s2)
        return

    if counter1.index(1) > counter2.index(1):
        print(s1)
        return
    if counter1.index(1) < counter2.index(1):
        print(s2)
        return


def tie_breaker_4(first_hand, second_hand):
    counter1 = [0] * 13
    for num in first_hand:
        counter1[num % 13] = counter1[num % 13] + 1

    counter2 = [0] * 13
    for num in second_hand:
        counter2[num % 13] = counter2[num % 13] + 1

    if counter1.index(3) > counter2.index(3):
        print(s1)
        return
    if counter1.index(3) < counter2.index(3):
        print(s2)
        return

    counter1.remove(3)
    counter2.remove(3)

    for i in range(len(counter1)):
        if counter1[11 - i] == counter2[11 - i]:
            continue
        else:
            if counter1[11 - i] > counter2[11 - i]:
                print(s1)
                return
            else:
                print(s2)
                return


def tie_breaker_5(first_hand, second_hand):
    r1, r2 = 0, 0
    if first_hand == [0, 1, 2, 3, 12]:
        r1 = 3
    else:
        r1 = max(first_hand)

    if second_hand == [0, 1, 2, 3, 12]:
        r2 = 3
    else:
        r2 = max(second_hand)

    if r1 > r2:
        print(s1)
    else:
        print(s2)


def tie_breaker_7(first_hand, second_hand):
    counter1 = [0] * 13
    for num in first_hand:
        counter1[num % 13] = counter1[num % 13] + 1

    counter2 = [0] * 13
    for num in second_hand:
        counter2[num % 13] = counter2[num % 13] + 1

    if counter1.index(3) > counter2.index(3):
        print(s1)
        return
    if counter1.index(3) < counter2.index(3):
        print(s2)
        return

    if counter1.index(2) > counter2.index(2):
        print(s1)
        return
    if counter1.index(2) < counter2.index(2):
        print(s2)
        return


def tie_breaker_8(first_hand, second_hand):
    counter1 = [0] * 13
    for num in first_hand:
        counter1[num % 13] = counter1[num % 13] + 1

    counter2 = [0] * 13
    for num in second_hand:
        counter2[num % 13] = counter2[num % 13] + 1

    if counter1.index(4) > counter2.index(4):
        print(s1)
        return
    if counter1.index(4) < counter2.index(4):
        print(s2)
        return

    if counter1.index(1) > counter2.index(1):
        print(s1)
        return
    if counter1.index(1) < counter2.index(1):
        print(s2)
        return


T = int(input())

for j in range(T):
    line = input().split()
    hand1 = [0] * 5
    hand2 = [0] * 5
    for i in range(5):
        hand1[i] = card_no(line[i])
        hand2[i] = card_no(line[5 + i])

    hand1.sort()
    hand2.sort()

    score1 = hand_status(hand1)
    score2 = hand_status(hand2)

    if score1 == score2:
        if score1 == 8:
            tie_breaker_8(hand1, hand2)
        elif score1 == 7:
            tie_breaker_7(hand1, hand2)
        elif score1 == 5:
            tie_breaker_5(hand1, hand2)
        elif score1 == 4:
            tie_breaker_4(hand1, hand2)
        elif score1 == 3:
            tie_breaker_3(hand1, hand2)
        elif score1 == 2:
            tie_breaker_2(hand1, hand2)
        else:
            tie_breaker_1(hand1, hand2)
    else:
        if score1 > score2:
            print(s1)
        else:
            print(s2)
