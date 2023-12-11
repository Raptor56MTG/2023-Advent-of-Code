def movement(c: str, current_location: tuple, previous_location: tuple):
    """Determine how to move throughout the grid."""

    # NOTE THAT IT WORKS LIKE THIS:
    # START  = (Y, X)
    # RIGHT  = (Y, X + 1)
    # LEFT   = (Y, X - 1)
    # TOP    = (Y - 1, X)
    # BOTTOM = (Y + 1, X)

    if c == "|" and previous_location[0] > current_location[0]:
        # UP
        return (current_location[0] - 1, current_location[1])
    if c == "|" and previous_location[0] < current_location[0]:
        # DOWN
        return (current_location[0] + 1, current_location[1]) 

    if c == "-" and previous_location[1] > current_location[1]:
        # LEFT 
        return (current_location[0], current_location[1] - 1)
    if c == "-" and previous_location[1] < current_location[1]:
        # RIGHT
        return (current_location[0], current_location[1] + 1)
 
    if c == "7" and previous_location[0] > current_location[0]:
        # LEFT 
        return (current_location[0], current_location[1] - 1) 
    if c == "7" and previous_location[1] < current_location[1]:
        # DOWN
        return (current_location[0] + 1, current_location[1])

    if c == "F" and previous_location[0] > current_location[0]:
        # RIGHT 
        return (current_location[0], current_location[1] + 1) 
    if c == "F" and previous_location[1] > current_location[1]:
        # DOWN
        return (current_location[0] + 1, current_location[1])
    
    if c == "L" and previous_location[0] < current_location[0]:
        # RIGHT 
        return (current_location[0], current_location[1] + 1)
    if c == "L" and previous_location[1] > current_location[1]:
        # UP
        return (current_location[0] - 1, current_location[1]) 
        
    if c == "J" and previous_location[0] < current_location[0]:
        # LEFT
        return (current_location[0], current_location[1] - 1)
    if c == "J" and previous_location[1] < current_location[1]:
        # UP 
        return (current_location[0] - 1, current_location[1]) 

def problem1():
    """part 1 of the problem."""

    # load in grid
    grid = []
    with open('problem.txt') as file:
        for line in file.readlines():
            grid.append([c for c in line.strip()])

    # find starting point
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "S":
                current_location = (i, j)
                break

    # generate possible moves
    possible_moves = []
    possible_moves.append((current_location[0] + 1, current_location[1], "bottom"))
    possible_moves.append((current_location[0] - 1, current_location[1], "top"))
    possible_moves.append((current_location[0], current_location[1] + 1, "right"))
    possible_moves.append((current_location[0], current_location[1] - 1, "left"))

    # determine valid moves
    valid_moves = []
    for move in possible_moves:
        if move[0] >= 0 and move[1] >= 0 and move[0] < len(grid) and move[1] < len(grid[0]):
            if move[2] == "top" and grid[move[0]][move[1]] in ["|", "7", "F"]:
                valid_moves.append((move[0], move[1]))
            if move[2] == "bottom" and grid[move[0]][move[1]] in ["|", "J", "L"]:
                valid_moves.append((move[0], move[1]))
            if move[2] == "right" and grid[move[0]][move[1]] in ["-", "7", "J"]:
                valid_moves.append((move[0], move[1]))
            if move[2] == "left" and grid[move[0]][move[1]] in ["-", "F", "L"]:
                valid_moves.append((move[0], move[1]))
    
    # make first move, and then start to iterate.
    previous_location = current_location
    current_location = valid_moves[0]
    move_count = 1
    while grid[current_location[0]][current_location[1]] != "S":
        character = grid[current_location[0]][current_location[1]]
        next_move = movement(character, current_location, previous_location)
        move_count += 1
        previous_location = current_location
        current_location = next_move
    return move_count // 2

def problem2():
    """part 2 of the problem."""

    # number of squares inscribed inside the pipeline
    total = 0

    # load in grid
    grid = []
    with open('problem.txt') as file:
        for line in file.readlines():
            grid.append([c for c in line.strip()])

    # find starting point
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "S":
                current_location = (i, j)
                break

    # generate possible moves
    possible_moves = []
    possible_moves.append((current_location[0] + 1, current_location[1], "bottom"))
    possible_moves.append((current_location[0] - 1, current_location[1], "top"))
    possible_moves.append((current_location[0], current_location[1] + 1, "right"))
    possible_moves.append((current_location[0], current_location[1] - 1, "left"))

    # determine valid moves
    valid_moves = []
    for move in possible_moves:
        if move[0] >= 0 and move[1] >= 0 and move[0] < len(grid) and move[1] < len(grid[0]):
            if move[2] == "top" and grid[move[0]][move[1]] in ["|", "7", "F"]:
                valid_moves.append((move[0], move[1]))
            if move[2] == "bottom" and grid[move[0]][move[1]] in ["|", "J", "L"]:
                valid_moves.append((move[0], move[1]))
            if move[2] == "right" and grid[move[0]][move[1]] in ["-", "7", "J"]:
                valid_moves.append((move[0], move[1]))
            if move[2] == "left" and grid[move[0]][move[1]] in ["-", "F", "L"]:
                valid_moves.append((move[0], move[1]))
    
    # make first move, and then start to iterate.
    previous_location = current_location
    current_location = valid_moves[0]
    moves_made = [current_location]
    while grid[current_location[0]][current_location[1]] != "S":
        character = grid[current_location[0]][current_location[1]]
        next_move = movement(character, current_location, previous_location)
        previous_location = current_location
        current_location = next_move
        moves_made.append(current_location)
    
    # iterate through all of the tiles and determine if they have been locked in.
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            # exclude pipe pieces and border pieces
            if ((i, j) not in moves_made and i > 0 and j > 0
                and i < len(grid) - 1 and j < len(grid[0]) - 1):
                # grab all the pipe pieces that are J, L, |.
                # This uses the logic related to jordan curves and counting
                # if the number of times the curve appears an odd or even
                # number of times to determine if a space is inside or outside the curve.
                # Shoutout to this video from topology in college
                # https://www.youtube.com/watch?v=hnds9-GmwkM
                left_grid = [grid[i][x] for x in range(0, j)]
                left_terms = []
                for x, term in enumerate(left_grid):
                    if (i, x) in moves_made and term in ['J', 'L', '|']:
                        left_terms.append(term)    
                if len(left_terms) % 2 == 1:
                    grid[i][j] = "I"
                    total += 1  
                else:
                    grid[i][j] = "O" 

    with open("output.txt", "w") as f:
        for row in grid:
            for char in row:
                f.write(char)
            f.write("\n")

    return total    


if __name__ == '__main__':
    print(problem1())
    print(problem2())
