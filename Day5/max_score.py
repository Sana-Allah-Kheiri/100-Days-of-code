# Full archive of 100Days OF Code in Python is at https://github.com/Sana-Allah-Kheiri/100-Days-of-code

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


def maxOfList (ScoreList):
    maxVal = 0.0;
    for score in ScoreList:
        if(score>maxVal):
            maxVal = score;
    
    return maxVal;




# ==========================================
# Main Program
# ==========================================

while retry == 1:
    n = input(" How many scores?");
    n = int(n);
    scoreList = [];
    for i in range(n):
        newScore = input(" Enter a new score: ");
        newScore = float(newScore);
        scoreList.append(newScore);

    print(" MAX score is : " , maxOfList(scoreList))

    retry = retryF()