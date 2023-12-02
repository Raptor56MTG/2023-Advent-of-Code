def problem1():
    """part 1 of the problem."""
    with open('problem.txt') as file:
        total = 0
        for line in file.readlines():
            numbers = [i for i in line if i.isdigit()]
            total += int(f'{numbers[0]}{numbers[-1]}')
        return total

def problem2():
    """part 2 of the problem."""
    numbers = {str(i): i for i in range(1, 10)}
    words = {"one": 1, "two": 2, "three": 3, "four": 4,
             "five": 5, "six": 6, "seven": 7, "eight": 8,
             "nine": 9}
    search_list = {**numbers, **words}
    with open('problem.txt') as file:
        total = 0
        for line in file.readlines():
            indexes = []
            for key in search_list.keys():
                if line.rfind(key) > -1:
                    indexes.append((key, line.rfind(key)))
                if line.find(key) > -1:
                    indexes.append((key, line.find(key)))
            sorted_index = sorted(indexes, key=lambda x: x[1])
            total += int(f"{search_list[sorted_index[0][0]]}{search_list[sorted_index[-1][0]]}")
        return total


if __name__ == '__main__':
    print(problem1())
    print(problem2())
