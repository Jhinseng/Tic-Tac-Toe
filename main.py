#  Create Tic-Tac-Toe Project
# Designed by Jinseng and niku <3 
# 6/25/2022

# Define the board
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Defining the winner of the board
def validate_board(board):
    # Horizontal Check
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != 0:
            print("Player " + str(row[0]) + " has won!")
            # same as `print(f"Player {row[0]} has won!")`
            return True

    # Vertical Check
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] and board[1][c] != 0:
            print_board(board)
            print("Player " + str(board[0][c]) + " has won!")
            return True

    # Diagonal Check
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != 0:
        print_board(board)
        print("Player " + str(board[1][1]) + " has won!")
        return True

    elif board[0][2] == board[1][1] == board[2][0] and board[1][1] != 0:
        print_board(board)
        print("Player " + str(board[1][1]) + " has won!")
        return True

    return False


# Printing the board after every turn
def print_board(board):
    print()
    for row in board:       
        for item in row:
            if item == 0:
                print(" - ", end = "")
            elif item == 1:
                print(" X ", end = "")
            elif item == 2:
                print(" O ", end = "")
        print()
    print()


# Confirming each position of the board whether it is valid or not
def validate_pos(board, x, y):
    if 0 <= x < 3 and 0 <= y < 3:
        return True
    else:
        return board[y][x] == 0 


# Our game result:
while True:
    print_board(board)

    while True:
        player1_x = int(input("X (0-based): "))
        player1_y = int(input("Y (0-based): "))
    
        
        if validate_pos(board, player1_x, player1_y):
            board[player1_y][player1_x] = 1
            break

    if validate_board(board) == True:
        # break lets you literally break outside of a loop
        break

    print_board(board)

    while True:
        player2_x = int(input("X (0-based): "))
        player2_y = int(input("Y (0-based): "))


        if validate_pos(board, player2_x, player2_y): 
            board[player2_y][player2_x] = 2
            break

    if validate_board(board) == True:
        break

