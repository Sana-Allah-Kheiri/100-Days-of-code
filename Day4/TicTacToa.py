import random
import sys
import time

retry = 1


# ==========================================
# Exit Function
# ==========================================

def exitF():
    print("Exiting app after 5 seconds...")
    for i in range(5):
        time.sleep(1)
        print("*")

    sys.exit("Goodbye!")


# ==========================================
# Retry Function
# ==========================================

def retryF():
    while True:
        try:
            retry = int(input("\nType 0 to exit | Type 1 to restart: "))
            if retry in (0, 1):
                return retry
            print("Please enter only 0 or 1.")
        except ValueError:
            print("Please enter a valid number.")


# ==========================================
# Print Board
# ==========================================

def printBoard(board):

    print("\n      0   1   2")
    print("    +---+---+---+")

    for row in range(3):
        print(f" {row}  | {board[row][0]} | {board[row][1]} | {board[row][2]} |")
        print("    +---+---+---+")


# ==========================================
# Check Winner
# ==========================================

def checkWinner(board):

    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Main diagonal
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    # Secondary diagonal
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


# ==========================================
# Draw Check
# ==========================================

def isDraw(board):

    for row in board:
        if " " in row:
            return False

    return True


# ==========================================
# Computer Move
# ==========================================

def computerMove(board, computerChoice):

    available = []

    for row in range(3):
        for col in range(3):

            if board[row][col] == " ":
                available.append([row, col])

    move = random.choice(available)

    board[move[0]][move[1]] = computerChoice


# ==========================================
# User Move
# ==========================================

def playerMove(board, player):

    while True:

        move = input(f"{player}, enter row and column (example 12): ")

        if len(move) != 2 or not move.isdigit():
            print("Invalid input.")
            continue

        row = int(move[0])
        col = int(move[1])

        if row not in range(3) or col not in range(3):
            print("Indexes must be between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That location is already occupied.")
            continue

        board[row][col] = player

        break


# ==========================================
# Game Function
# ==========================================

def playGame():

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    while True:

        userChoice = input("Choose X or O: ").upper()

        if userChoice in ["X", "O"]:
            break

        print("Please choose only X or O.")

    if userChoice == "X":
        computerChoice = "O"
        currentPlayer = "X"
    else:
        computerChoice = "X"
        currentPlayer = "X"      # X always starts

    while True:

        printBoard(board)

        if currentPlayer == userChoice:

            playerMove(board, userChoice)

        else:

            print("\nComputer is thinking...\n")
            time.sleep(1)

            computerMove(board, computerChoice)

        winner = checkWinner(board)

        if winner:

            printBoard(board)

            if winner == userChoice:
                print("\nCongratulations! You won!")
            else:
                print("\nComputer wins!")

            break

        if isDraw(board):

            printBoard(board)

            print("\nIt's a draw!")

            break

        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"


# ==========================================
# Main Program
# ==========================================

while retry == 1:

    print("""  

 _    _      _                           ___         ________   
| |  | |    | |                          | |        |_   ___|    
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___     | |  _  ___ 
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | | | |/ __|
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | | | | (__ 
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    \_/ |_|\___|
                                                                  
                                                                  
 _____            _____                                           
|_   _|          |_   _|                                          
  | | __ _  ___    | | ___   __ _                                 
  | |/ _` |/ __|   | |/ _ \ / _` |                                
  | | (_| | (__    | | (_) | (_| |                                
  \_/\__,_|\___|   \_/\___/ \__,_|                                

   """);

    playGame()

    retry = retryF()

    if retry == 0:
        exitF()