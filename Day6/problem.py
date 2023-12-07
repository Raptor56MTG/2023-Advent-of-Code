def problem1():
    """part 1 of the problem."""
    with open('problem.txt') as file:
        total = 1
        ways = []
        times = [int(x) for x in file.readline().split(":")[1].split()]
        distances = [int(x) for x in file.readline().split(":")[1].split()]
        for time, distance in zip(times, distances):
            counter = 0
            for i in range(time):
                if i * (time - i) > distance:
                    counter += 1
            ways.append(counter)
    for way in ways:
        total *= way
    return total

def problem2():
    """part 2 of the problem."""
    with open('problem.txt') as file:
        total = 1
        ways = []
        times = [int("".join(file.readline().split(":")[1].split()))]
        distances = [int("".join(file.readline().split(":")[1].split()))]
        for time, distance in zip(times, distances):
            counter = 0
            for i in range(time):
                if i * (time - i) > distance:
                    counter += 1
            ways.append(counter)
    for way in ways:
        total *= way
    return total

if __name__ == '__main__':
    print(problem1())
    print(problem2())
