def problem1():
    """part 1 of the problem."""
    total = 0
    with open('problem.txt') as file:
        for line in file.readlines():
            ticket, numbers = line.split("|")
            numbers = numbers.split()
            ticket = ticket.split()
            count = 0
            for number in numbers:
                if number in ticket:
                    count += 1
            if count > 0:
                total += 2 ** (count - 1)
    return total

def problem2():
    """part 2 of the problem."""
    total = 0
    tickets = {}
    with open('problem.txt') as file:
        for i, line in enumerate(file.readlines(), start=1):
            ticket, numbers = line.split("|")
            numbers = numbers.split()
            ticket = ticket.split()
            tickets[i] = {"tickets": 1}
            count = 0
            for number in numbers:
                if number in ticket:
                    count += 1
            tickets[i]["wins"] = count
    for key, value in tickets.items():
        wins = value['wins']
        ticket = value['tickets']
        for _ in range(ticket):
            for i in range(1, wins + 1):
                tickets[key + i]["tickets"] += 1
    for value in tickets.values():
        total += value['tickets']   
    return total


if __name__ == '__main__':
    print(problem1())
    print(problem2())
