from math import gcd


def problem1():
    """part 1 of the problem."""
    total = 0
    with open('problem.txt') as file:
        moves = file.readline()
        moves = moves.strip()
        file.readline()
        graph = {}
        for line in file.readlines():
            char_removal = ["=", "(", ",", ")"]
            for char in char_removal:
                line = line.replace(char, "")
            line = line.split()
            graph[line[0]] = {"L": line[1], "R": line[2]}
        start = "AAA"
        while start != "ZZZ":
            for move in moves:
                start = graph[start][move]
                total += 1
    return total

def problem2():
    """part 2 of the problem."""
    with open('problem.txt') as file:
        moves = file.readline()
        moves = moves.strip()
        file.readline()
        graph = {}
        for line in file.readlines():
            char_removal = ["=", "(", ",", ")"]
            for char in char_removal:
                line = line.replace(char, "")
            line = line.split()
            graph[line[0]] = {"L": line[1], "R": line[2]}
        
    steps = []
    for node, _ in graph.items():
        if node[-1] == 'A':
            start = node
            count = 0
            while start[-1] != "Z":
                for move in moves:
                    start = graph[start][move]
                    count += 1
            steps.append(count)

    # use LCM and GCD to find the least common multiple. This will tell us
    # where all of the cycles will line up.
    lcm = None
    for i, _ in enumerate(steps[:-1]):
        prior_lcm = int((steps[i] * steps[i + 1]) / gcd(steps[i], steps[i + 1]))
        if lcm is None:
            lcm = int(prior_lcm)
        else:
            lcm = int((lcm * prior_lcm) / gcd(lcm, prior_lcm))
    return lcm


if __name__ == '__main__':
    print(problem1())
    print(problem2())
