from collections import Counter


def rotate_90_degrees_cw(grid):
    new_grid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            row.append(grid[j][i])
        new_grid.append(row[::-1])
    return new_grid

def rotate_90_degrees_ccw(grid):
    for _ in range(3):
        grid = rotate_90_degrees_cw(grid)
    return grid

def move_rocks(row):
    rock_count = 0
    for i, char in enumerate(row):
        if rock_count > 0 and char == "#":
            row[i - rock_count: i] = ["O"] * rock_count
            rock_count = 0
        if char == 'O':
            rock_count += 1
            row[i] = '.'
        if rock_count > 0 and i == len(row) - 1:
            row[i - rock_count + 1: i + 1] = ["O"] * rock_count
            rock_count = 0
    return row

def problem1():
    """part 1 of the problem."""
    total = 0
    with open('problem.txt') as file:
        grid = []
        for line in file.readlines():
            row = [i for i in line.strip()]
            grid.append(row)
    # rotate grid clockwise so it is easier to work with
    rotated_grid = rotate_90_degrees_cw(grid)
    # move the rocks  
    moved_grid = [move_rocks(row) for row in rotated_grid]
    # undo the rotation to get the finished grid
    finished_grid = rotate_90_degrees_ccw(moved_grid)
    # calculate the score
    for i, row in enumerate(finished_grid):
        counts = Counter(row)
        total += (len(finished_grid) - i) * counts["O"]

    return total

def problem2():
    """part 2 of the problem."""
    total = 0
    with open('problem.txt') as file:
        grid = []
        for line in file.readlines():
            row = [i for i in line.strip()]
            grid.append(row)
    # use this to determine when stability has occured.
    looped = False
    scores = {}
    loop_threshold = 50 # guestimate, no idea how to caculate properly.
    k = 0
    while not looped:
        k += 1
        # do a full spin cycle
        for _ in range(4):
            # rotate grid clockwise so it is easier to work with
            rotated_grid = rotate_90_degrees_cw(grid)
            # move the rocks  
            moved_grid = [move_rocks(row) for row in rotated_grid]
            # update grid
            grid = moved_grid
        # calculate the score
        total = 0
        for i, row in enumerate(grid):
            counts = Counter(row)
            total += (len(grid) - i) * counts["O"]
        if total not in scores:
            scores[total] = 1
        else:
            scores[total] += 1
        for _, value in scores.items():
            if value == loop_threshold:
                looped = True
    # stability has occured, now list when it starts.
    repeat = False
    loop_modularity = {}
    while not repeat:
        k += 1
        # do a full spin cycle
        for _ in range(4):
            # rotate grid clockwise so it is easier to work with
            rotated_grid = rotate_90_degrees_cw(grid)
            # move the rocks  
            moved_grid = [move_rocks(row) for row in rotated_grid]
            # update grid
            grid = moved_grid
        total = 0
        for i, row in enumerate(grid):
            counts = Counter(row)
            total += (len(grid) - i) * counts["O"]
        if total in list(loop_modularity.values()):
            repeat = True
        else:
            loop_modularity[k] = total 
    # get starting value of loop
    start = min([key for key in list(loop_modularity.keys())])
    # get length of loop
    length = len(loop_modularity)
    # we want to see the value after this many loops
    target = 1000000000
    # subtract start value to shift to base zero, then get modularity
    modularity = (target - start) % length
    # find the index that lines up
    for key, value in loop_modularity.items():
        if key - start == modularity:
            total = value
    return total

if __name__ == '__main__':
    # print(problem1())
    print(problem2())
