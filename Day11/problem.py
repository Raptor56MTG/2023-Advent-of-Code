def problem1():
    """part 1 of the problem."""
    total = 0
    with open('problem.txt') as file:
        grid = []
        stars = []
        rows = []
        columns = []
        for line in file.readlines():
            grid.append([i for i in line.strip()])
        for i, row in enumerate(grid):
            # find empty rows
            if "#" not in row:
                rows.append(i)
            # append stars
            for j, char in enumerate(row):
                if char == "#":
                    stars.append((i, j))
        # find empty columns
        for i in range(len(grid[0])):
            column = [grid[j][i] for j in range(len(grid))]
            if "#" not in column:
                columns.append(i)
    # check distances between each point
    for i, star1 in enumerate(stars):
        check = stars[i + 1:]
        for star2 in check:
            x1 = min(star1[0], star2[0])
            x2 = max(star1[0], star2[0])
            y1 = min(star1[1], star2[1])
            y2 = max(star1[1], star2[1])     
            x_dist = 0
            y_dist = 0
            for row in rows:
                if x1 < row < x2:
                    x_dist += 1
            for col in columns:
                if y1 < col < y2:
                    y_dist += 1
            total += x2 - x1 + y2 - y1 + x_dist + y_dist
    return total

def problem2():
    """part 2 of the problem."""
    total = 0
    with open('problem.txt') as file:
        grid = []
        stars = []
        rows = []
        columns = []
        for line in file.readlines():
            grid.append([i for i in line.strip()])
        for i, row in enumerate(grid):
            # find empty rows
            if "#" not in row:
                rows.append(i)
            # append stars
            for j, char in enumerate(row):
                if char == "#":
                    stars.append((i, j))
        # find empty columns
        for i in range(len(grid[0])):
            column = [grid[j][i] for j in range(len(grid))]
            if "#" not in column:
                columns.append(i)
    # check distances between each point
    for i, star1 in enumerate(stars):
        check = stars[i + 1:]
        for star2 in check:
            x1 = min(star1[0], star2[0])
            x2 = max(star1[0], star2[0])
            y1 = min(star1[1], star2[1])
            y2 = max(star1[1], star2[1])     
            x_dist = 0
            y_dist = 0
            for row in rows:
                if x1 < row < x2:
                    x_dist += 999999 
            for col in columns:
                if y1 < col < y2:
                    y_dist += 999999
            total += x2 - x1 + y2 - y1 + x_dist + y_dist
    return total

if __name__ == '__main__':
    print(problem1())
    print(problem2())
