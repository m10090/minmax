import math

def minimax(board, depth, maximizing_player):
    if check_winner(board, 'X'):
        return -10
    elif check_winner(board, 'O'):
        return 10
    elif is_board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = -math.inf
        for move in range(9):
            if board[move] == ' ':
                board[move] = 'O'
                eval = minimax(board, depth + 1, False)
                board[move] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in range(9):
            if board[move] == ' ':
                board[move] = 'X'
                eval = minimax(board, depth + 1, True)
                board[move] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def is_board_full(board):
    return not any(cell == ' ' for cell in board)

def find_best_move(board):
    best_move = -1
    best_eval = -math.inf
    for move in range(9):
        if board[move] == ' ':
            board[move] = 'O'
            eval = minimax(board, 0, False)
            board[move] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = move
    return best_move

def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

def main():
    board = [' '] * 9
    print("Initial Board:")
    print_board(board)

    while not check_winner(board, 'X') and not check_winner(board, 'O') and not is_board_full(board):
        user_move = int(input("Enter your move (0-8): "))
        if board[user_move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[user_move] = 'X'
        print("After your move:")
        print_board(board)

        if not check_winner(board, 'X') and not is_board_full(board):
            print("Computer is thinking...")
            computer_move = find_best_move(board)
            board[computer_move] = 'O'
            print("After computer's move:")
            print_board(board)

    if check_winner(board, 'X'):
        print("You win!")
    elif check_winner(board, 'O'):
        print("Computer wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()

