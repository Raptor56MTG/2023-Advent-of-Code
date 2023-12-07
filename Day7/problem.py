from collections import Counter


card_values = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6,
               '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}

def poker_rating(hand: str):
    counter = sorted(Counter(hand).values())
    if counter == [5]:
        return 7
    if counter == [1, 4]:
        return 6
    if counter == [2, 3]:
        return 5
    if counter == [1, 1, 3]:
        return 4
    if counter == [1, 2, 2]:
        return 3
    if counter == [1, 1, 1, 2]:
        return 2
    if counter == [1, 1, 1, 1, 1]:
        return 1

wildcard_values = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, 'T': 10, 'Q': 11, 'K': 12, 'A': 13}

def poker_rating_wildcard(hand: str):
    counter = sorted(Counter(hand).values())
    if counter == [5]:
        return 7
    if counter == [1, 4]:
        if Counter(hand)["J"] == 1:
            return 6 + 1
        elif Counter(hand)["J"] == 4:
            return 6 + 1
        else:
            return 6
    if counter == [2, 3]:
        if Counter(hand)["J"] == 2:
            return 5 + 2
        elif Counter(hand)["J"] == 3:
            return 5 + 2
        else:
            return 5
    if counter == [1, 1, 3]:
        if Counter(hand)["J"] == 1:
            return 4 + 2
        if Counter(hand)["J"] == 3:
            return 4 + 2
        else:
            return 4
    if counter == [1, 2, 2]:
        if Counter(hand)["J"] == 2:
            return 3 + 3
        elif Counter(hand)["J"] == 1:
            return 3 + 2
        else:
            return 3
    if counter == [1, 1, 1, 2]:
        if Counter(hand)["J"] == 2:
            return 2 + 2
        elif Counter(hand)["J"] == 1:
            return 2 + 2
        else:
            return 2
    if counter == [1, 1, 1, 1, 1]:
        if Counter(hand)["J"] == 1:
            return 1 + 1
        else:
            return 1

def problem1():
    """part 1 of the problem."""
    total = 0
    hands = []
    with open('problem.txt') as file:
        for line in file.readlines():
            hand, bet = line.split()
            score = poker_rating(hand)
            hands.append((hand, score, int(bet)))
        # wtf did I do at 3 am
        hands = sorted(hands, key=lambda x:
                       sum([(card_values[i] * 10 ** (2 * j)) for j, i in enumerate(reversed(x[0]))]) ** x[1])
    for i, hand in enumerate(hands, start=1):
        total += hand[2] * i
    return total

def problem2():
    """part 2 of the problem."""
    total = 0
    hands = []
    with open('problem.txt') as file:
        for line in file.readlines():
            hand, bet = line.split()
            score = poker_rating_wildcard(hand)
            hands.append((hand, score, int(bet)))
        # wtf did I do at 3 am
        hands = sorted(hands, key=lambda x:
                       sum([(wildcard_values[i] * 10 ** (2 * j)) for j, i in enumerate(reversed(x[0]))]) ** x[1])
    for i, hand in enumerate(hands, start=1):
        total += hand[2] * i
    return total


if __name__ == '__main__':
    print(problem1())
    print(problem2())
