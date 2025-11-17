# TIC TAC TOE

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def player_input(player, board):
    while True:
        move = input(f"Player {player}, enter row and column (1-3 1-3): ")
        row, col = move.split()

        row = int(row) - 1
        col = int(col) - 1

        if row in range(3) and col in range(3):
            if board[row][col] == " ":
                return row, col
            else:
                print("That spot is taken.")
        else:
            print("Invalid move. Try again.")

def check_win(board, player):
    # Rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def play():
    board = create_board()
    player = "X"

    while True:
        display_board(board)

        row, col = player_input(player, board)
        board[row][col] = player

        if check_win(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie.")
            break

        # Switch players
        player = "O" if player == "X" else "X"

play()