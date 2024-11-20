# Initialize the game board with 9 empty spaces
board = [' ' for _ in range(9)]
# Function to display the current state of the board
def print_board():
    # Loop through rows (0-2, 3-5, 6-8) and print them in a neat format
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()  # Add a blank line for better readability
# Function to check if the current player has won
def check_winner(player):
    # Define all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    # Check if the player's markers match any winning combination
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False
# Function to check if the game is a draw (no empty spaces left)
def is_draw():
    return ' ' not in board
# Main function to run the game
def play_game():
    current_player = 'X'  # Player 'X' always starts
    while True:  # Game continues until there's a winner or a draw
        print_board()  # Show the current board state
        try:
            # Ask the current player for their move
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
            # Check if the chosen position is valid
            if move < 0 or move >= 9 or board[move] != ' ':
                print("Invalid move. Choose an empty spot between 1 and 9.")
                continue  # Ask again if the move is invalid
            # Place the player's marker on the board
            board[move] = current_player
            # Check if the current player has won
            if check_winner(current_player):
                print_board()
                print(f"Congratulations, Player {current_player}! You win!")
                break  # End the game
            # Check if the game is a draw
            if is_draw():
                print_board()
                print("It's a draw!")
                break  # End the game
            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'
        except (ValueError, IndexError):  # Handle invalid input
            print("Invalid input. Please enter a number between 1 and 9.")
# Start the Tic-Tac-Toe game
play_game()
