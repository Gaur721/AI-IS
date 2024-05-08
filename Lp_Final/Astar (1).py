def accept(n):
    puz = []
    for _ in range(n):
        puz.append([val for val in input().split()])
    return puz

def print_board(board):
    for row in board:
        print(' '.join(row))

def find_space(current):
    for i, row in enumerate(current):
        for j, val in enumerate(row):
            if val == '_':
                return i, j
    return None, None

def copy_board(board):
    return [row[:] for row in board]

def shuffle(current, brow_pos, bcol_pos, move_x, move_y):
    if 0 <= move_x < len(current) and 0 <= move_y < len(current):
        temp = copy_board(current)
        temp[move_x][move_y], temp[brow_pos][bcol_pos] = temp[brow_pos][bcol_pos], temp[move_x][move_y]
        return temp
    return None

def g_score(node):
    return node[1]

def h_score(current, goal):
    return sum(current[i][j] != goal[i][j] for i in range(len(current)) for j in range(len(current)) if current[i][j] != '_')

def f_score(node, goal):
    current = node[0]
    return g_score(node) + h_score(current, goal)

def move_gen(node, goal):
    current = node[0]
    level = node[1]
    row, col = find_space(current)
    move_positions = [[row, col-1], [row, col+1], [row-1, col], [row+1, col]]
    children = []
    for move in move_positions:
        child = shuffle(current, row, col, move[0], move[1])
        if child is not None:
            c_node = [child, level + 1, 0]  # Setting fscore to 0 temporarily
            fscore = f_score(c_node, goal)
            c_node[2] = fscore
            children.append(c_node)
    return children

def goal_test(current, goal):
    return h_score(current, goal) == 0

def sort(nodes):
    nodes.sort(key=lambda x: x[2])
    return nodes

def print_closed_list(closed_list):
    print("\nClosed List:")
    for i, node in enumerate(closed_list):
        print(f"Step {i + 1}:")
        print_board(node[0])
        print(f"Level: {node[1]}")
        print(f"f-Score: {node[2]}")
        print()

def play_game(start, goal):
    level = 0
    start_node = [start, level, 0]  # Setting fscore to 0 temporarily
    fscore = f_score(start_node, goal)
    start_node[2] = fscore
    open_list = [start_node]
    closed_list = []

    while open_list:
        current_node = open_list[0]
        del open_list[0]
        current_board = current_node[0]
        closed_list.append(current_node)

        if goal_test(current_board, goal):
            print("\nGoal reached!!")
            print_closed_list(closed_list)
            break

        children = move_gen(current_node, goal)
        open_list.extend(children)
        sort(open_list)

n = int(input("Enter the board size: "))
print("\nEnter Start Configuration of board:")
start_board = accept(n)
print("\nEnter Goal Configuration of board:")
goal_board = accept(n)

play_game(start_board, goal_board)
