import math


# Print the board in a readable format
def print_board(board):
    for row in board:
        print(row)
    print("\n" + "-" * 10 + "\n")  # Separate each board with a line


# Check for the winner or draw
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return board[0][2]

    # Check for empty spaces (still ongoing)
    for row in board:
        for cell in row:
            if cell == '_':
                return None  # Game is still ongoing

    return 'Draw'  # No empty spaces, it's a draw


# Minimax algorithm to find the best move
def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == 'X':
        return 1
    if winner == 'O':
        return -1
    if winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    score = minimax(board, False)
                    board[i][j] = '_'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    score = minimax(board, True)
                    board[i][j] = '_'
                    best_score = min(score, best_score)
        return best_score


# Find the best possible move for the AI
def find_best_move(board):
    best_move = None
    best_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                move_score = minimax(board, False)
                board[i][j] = '_'
                if move_score > best_score:
                    best_score = move_score
                    best_move = (i, j)
    return best_move


# Main function to play Tic-Tac-Toe
def play_tic_tac_toe():
    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

    print("Initial Board:")
    print_board(board)

    while True:
        # AI (X) makes its move
        best_move = find_best_move(board)
        if best_move:
            board[best_move[0]][best_move[1]] = 'X'
        else:
            break

        print("AI (X) makes move:")
        print_board(board)

        winner = check_winner(board)
        if winner:
            if winner == 'Draw':
                print("The game is a Draw!")
            else:
                print(f"{winner} wins!")
            break

        # Player (O) makes their move
        while True:
            try:
                row = int(input("Enter row (0-2) for 'O': "))
                col = int(input("Enter col (0-2) for 'O': "))

                # Validate if the row and column are within range (0, 1, or 2)
                if row not in range(3) or col not in range(3):
                    print("Invalid input! Please enter a number between 0 and 2.")
                    continue

                if board[row][col] == '_':
                    board[row][col] = 'O'
                    break
                else:
                    print("Cell already taken. Choose another!")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        print("Player (O) makes move:")
        print_board(board)

        winner = check_winner(board)
        if winner:
            if winner == 'Draw':
                print("The game is a Draw!")
            else:
                print(f"{winner} wins!")
            break


# Run the game
play_tic_tac_toe()
