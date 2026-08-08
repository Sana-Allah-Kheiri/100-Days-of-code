# Full archive of 100Days OF Code in Python is at https://github.com/Sana-Allah-Kheiri/100-Days-of-code

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


def averageOfList (heightList, n):
    avrg = 0.0;
    sum = 0;
    for height in heightList:
        sum+=height;
    avrg = sum / n;
    return avrg;




# ==========================================
# Main Program
# ==========================================

while retry == 1:
    n = input(" How many students are there in your class? ");
    n = int (n);
    heights = [];
    for i in range(n):
        newHeight = input(" Enter a new height in cm: ");
        newHeight = int(newHeight);
        heights.append(newHeight);
    
    avrg = averageOfList(heights , n);
    print(f" Mean of heights in your classroom = {avrg}");

    

    retry = retryF()