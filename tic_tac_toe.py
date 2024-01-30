def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner(board, player):
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[row][col] == player for row in range(3)) for col in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def is_board_full(board):   
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter row and column (0, 1, or 2) separated by space: ").split())

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already occupied. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
