import re

def problem1():
    """part 1 of the problem."""
    red = r'1[3-9]\sred|[2-9][0-9]\sred|[1-9]\d{2,}\sred'
    green = r'1[4-9]\sgreen|[2-9][0-9]\sgreen|[1-9]\d{2,}\sgreen'
    blue = r'1[5-9]\sblue|[2-9][0-9]\sblue|[1-9]\d{2,}\sblue'
    with open('problem.txt') as file:
        total = 0
        for game, line in enumerate(file.readlines(), start=1):
            if not re.search(red, line) and not re.search(green, line) and not re.search(blue, line):
                total += game
            game += 1
        return total

def problem2():
    """part 2 of the problem."""
    red = r'\d+\sred'
    green = r'\d+\sgreen'
    blue = r'\d+\sblue'
    with open('problem.txt') as file:
        total = 0
        for line in file.readlines():
            r = max([int(i.replace(' red', '')) for i in re.findall(red, line)])
            g = max([int(i.replace(' green', '')) for i in re.findall(green, line)])
            b = max([int(i.replace(' blue', '')) for i in re.findall(blue, line)])
            total += r * g * b
        return total


if __name__ == '__main__':
    print(problem1())
    print(problem2())
