player1_symbol: str = "X"
player2_symbol: str = "O"

player1_name: str = input("Please enter your name, Player 1: ")
print(f"Welcome {player1_name}! You'll be playing as 'X'.")

player2_name: str = input("Please enter your name, Player 2: ")
print(f"Welcome {player2_name}! You'll be playing as 'O'.")

game_board: list = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

for index, row in enumerate(game_board):
    print("|".join(row))
    if index < len(game_board) - 1:  # if it's not the last row
        print("-----")
