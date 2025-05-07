def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    # Check for draw
    for row in board:
        if ' ' in row:
            return None
    return 'Draw'  # No winer

def minimax(board, is_maximizing):
    result = check_winner(board)
    if result == 'X':
        return 1
    elif result == 'O':
        return -1
    elif result == 'Draw':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board, is_maximizing):
    best_score = -float('inf') if is_maximizing else float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                symbol = 'X' if is_maximizing else 'O'
                board[i][j] = symbol
                score = minimax(board, not is_maximizing)
                board[i][j] = ' '
                if is_maximizing and score > best_score:
                    best_score = score
                    best_move = (i, j)
                elif not is_maximizing and score < best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Example usage
if __name__ == "__main__":
    # Example board: X's turn
    board = [
        ['X', ' ', 'O'],
        [' ', 'X', 'O'],
        [' ', ' ', ' ']
    ]
    best_move = find_best_move(board, is_maximizing=True)
    print(f"Best move for X: {best_move}")  # Output: (2, 2)