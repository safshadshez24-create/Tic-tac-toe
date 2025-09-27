import random

# Print the board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Check for a win
def check_win(board, player):
    win_combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a]==board[b]==board[c]==player for a,b,c in win_combos)

# Check for draw
def check_draw(board):
    return all(space != " " for space in board)

# Computer chooses a move randomly
def computer_move(board):
    available = [i for i,space in enumerate(board) if space==" "]
    return random.choice(available)

def play_game():
    board = [" "] * 9
    human = "X"
    computer = "O"

    print("Welcome to Tic Tac Toe! You are X. Computer is O.")
    print_board(board)

    while True:
        # Human turn
        try:
            move = int(input("Your move (1-9): ")) - 1
            if board[move] != " ":
                print("That spot is already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Choose a number 1–9.")
            continue

        board[move] = human
        print_board(board)

        if check_win(board, human):
            print("🎉 You win! 🎉")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # Computer turn
        print("Computer's move...")
        comp_move = computer_move(board)
        board[comp_move] = computer
        print_board(board)

        if check_win(board, computer):
            print("💻 Computer wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()