# Full archive at https://github.com/Sana-Allah-Kheiri/100-Days-of-code

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
# Print Map
# ==========================================

def printMap(map):

    print("\n      0   1   2")
    print("    +---+---+---+")

    for row in range(3):
        print(f" {row}  | {map[row][0]} | {map[row][1]} | {map[row][2]} |")
        print("    +---+---+---+")


# ==========================================
# Random treasure putting function
# ==========================================
def putTreasure(map):
    row = random.randint(0,2);
    column = random.randint(0,2);
    map[row][column] = "🏆"
    return map;

# =================================================
# Checking whether user guesses the location or not
# =================================================
def isRightLocation(map, guess):
    i1 = guess[0]
    i1 = int(i1)
    j1 = guess[1]
    j1 = int(j1)
    result = False;
    for i in range(3):
        for j in range(3):
            if (map[i][j] == "🏆" and i==i1 and j==j1):
                result = True;
    return result;

# =================================================
# Putting X in guessed location by player
# =================================================
def putX (guess , map):
    i1 = guess[0]
    i1 = int(i1)
    j1 = guess[1]
    j1 = int(j1)
    map[i1][j1] = "X"




# ==========================================
# Main Script
# ==========================================

while retry == 1:

    print("""  

.----..-..-. .-..----.    .-----..-. .-..----.       
} |__}{ ||  \{ |} {-. \   `-' '-'{ {_} |} |__}       
} '_} | }| }\  {} '-} /     } {  | { } }} '__}       
`--'  `-'`-' `-'`----'      `-'  `-' `-'`----'       
.-----..---. .----.  .--.   .----..-. .-..---. .----.
`-' '-'} }}_}} |__} / {} \ { {__-`| } { |} }}_}} |__}
  } {  | } \ } '__}/  /\  \.-._} }\ `-' /| } \ } '__}
  `-'  `-'-' `----'`-'  `-'`----'  `---' `-'-' `----'               

       """);

    treasureMap = [ ["⬜" , "⬜" , "⬜"],
                    ["⬜" , "⬜" , "⬜"],
                    ["⬜" , "⬜" , "⬜"] ]
    printMap(treasureMap); # Print the whole map
    putTreasure(treasureMap); # Sudo-randomly putting treasure somewhere in the above maze
    userGuess = input(" Guess the location of treasure by entering two-digit number eg: 00 for first row and first column ");
    printMap(treasureMap)
    putX(userGuess, treasureMap);
    if (isRightLocation == True):
        print(" You got it!")
        printMap(treasureMap)
    else:
        print("Not quite right!")
        printMap(treasureMap)

    
    


    retry = retryF()

    if retry == 0:
        exitF()