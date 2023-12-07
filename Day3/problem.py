def problem1():
    """part 1 of the problem."""
    numbers = [str(x) for x in range(0, 10)]
    number_storage = []
    character_storage = []
    number, total, start, end = "", 0, 0, 0
    with open('problem.txt') as file:
        for i, line in enumerate(file.read().splitlines()):
            for j, character in enumerate(line):
                # build number
                if character in numbers:
                    if number == "":
                        start = (i, j)
                    number += character
                # store number
                if character not in numbers and number != "":
                    end = (i, j-1)
                    number_storage.append((number, (start[0], end[0]), (start[1], end[1])))
                    number = ""
                # store character
                if character not in numbers and character != ".":
                    character_storage.append((character, i, j))
            # store number at end of line
            if number != "":
                end = (i, j-1)
                number_storage.append((number, (start[0], end[0]), (start[1], end[1])))
                number = ""
        # compare numbers and character locations
        for number in number_storage:
            x_range = [i for i in range(number[1][0] - 1, number[1][1] + 2)]
            y_range = [i for i in range(number[2][0] - 1, number[2][1] + 2)]
            touching = False
            for character in character_storage:
                if character[1] in x_range and character[2] in y_range:
                    print(number, character[1], x_range, character[2], y_range)
                    touching = True
            if touching:
                total += int(number[0])
    return total

def problem2():
    """part 2 of the problem."""
    numbers = [str(x) for x in range(0, 10)]
    number_storage = []
    character_storage = []
    number, total, start, end = "", 0, 0, 0
    with open('problem.txt') as file:
        for i, line in enumerate(file.read().splitlines()):
            for j, character in enumerate(line):
                # build number
                if character in numbers:
                    if number == "":
                        start = (i, j)
                    number += character
                # store number
                if character not in numbers and number != "":
                    end = (i, j-1)
                    number_storage.append((number, (start[0], end[0]), (start[1], end[1])))
                    number = ""
                # store gear
                if character == "*":
                    character_storage.append((character, i, j))
            # store number at end of line
            if number != "":
                end = (i, j-1)
                number_storage.append((number, (start[0], end[0]), (start[1], end[1])))
                number = ""
        # compare numbers and character locations
        for character in character_storage:
            x_range = [i for i in range(character[1] - 1, character[1] + 2)]
            y_range = [i for i in range(character[2] - 1, character[2] + 2)]
            gears = []
            for number in number_storage:
                if ((number[1][0] in x_range or number[1][1] in x_range)
                    and (number[2][0] in y_range or number[2][1] in y_range)):
                    gears.append(int(number[0]))
            if len(gears) == 2:
                total += gears[0] * gears[1]
            gears = []
    return total


if __name__ == '__main__':
    print(problem1())
    print(problem2())
