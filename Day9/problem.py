def problem1():
    """part 1 of the problem."""
    total = 0
    with open('problem.txt') as file:
        for line in file.readlines():
            row = [[int(i) for i in line.split()]]
            while row[-1][-1] != 0:
                row.append([row[-1][i + 1] - row[-1][i] for i, _ in enumerate(row[-1][:-1])])
            total += sum([i[-1] for i in row])
    return total

def problem2():
    """part 2 of the problem."""
    total = 0
    with open('problem.txt') as file:
        for line in file.readlines():
            row = [[int(i) for i in line.split()]]
            while row[-1][-1] != 0:
                row.append([row[-1][i + 1] - row[-1][i] for i, _ in enumerate(row[-1][:-1])])
            total += sum([r[0] * (-1) ** i for i, r in enumerate(row)])
    return total

if __name__ == '__main__':
    print(problem1())
    print(problem2())
