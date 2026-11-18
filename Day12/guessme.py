# Full archive at Day12 folder of https://github.com/Sana-Allah-Kheiri/100-Days-of-code

import sys
import time
import random
import csv
retry = 1

def exitF(): # To exit the app
    print("Developed by...");
    print("Sana");
    time.sleep(1)
    print("ALLAH");
    time.sleep(1)
    print("Kheiri");
    sys.exit("Goodbye!")

def retryF(): # To improve user experience
    retry = input(" Type 0 to exit | Type 1 to restart ");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;

def rangeHint (target, guessed):
    dif = int(abs(target - guessed))
    hint = ""
    if (dif>=90 and dif<100):
        hint = "your difference is in range of [90, 100)"
    if (dif>=80 and dif<90):
        hint = "your difference is in range of [80, 90)"
    if (dif>=70 and dif<80):
        hint = "your difference is in range of [70, 80)"
    if (dif>=60 and dif<70):
        hint = "your difference is in range of [60, 70)"
    if (dif>=50 and dif<60):
        hint = "your difference is in range of [50, 60)"
    if (dif>=40 and dif<50):
        hint = "your difference is in range of [40, 50)"
    if (dif>=30 and dif<40):
        hint = "your difference is in range of [30, 40)"
    if (dif>=20 and dif<30):
        hint = "your difference is in range of [20, 30)"
    if (dif>=10 and dif<20):
        hint = "your difference is in range of [10, 20)"
    if (dif>0 and dif<10):
        hint = "your difference is in range of (0, 10)"  
    if (dif==0):
        hint = "Congrats you won!"
    return hint;

def compareHint (guessed, target):
    res = ""
    if (guessed > target):
        res = "Higher"
    if (guessed < target):
        res = "Lower"
    return res;

    

def gamePlay(difficultyLevel):
    target = random.randint(1, 100)
    #gameResult = ""; #Output of function
    initScore = 100;
    attemptNo = 0;

    if(difficultyLevel == 1):
        for i in range (20):
            guessed = int(input("Make a guess:"))
            if (guessed == target):
                print ("You won");
                break
            if (guessed != target):
                initScore -= 5;
                lowerOrHigher = compareHint (guessed, target)
                print(lowerOrHigher);
                differenceMessage = rangeHint (target, guessed)
                print(differenceMessage)
                print(f"Your current score is {initScore}")
                remainingAttempts = 20 - (i+1)
                print(f" You have {remainingAttempts} remaining attempts")


    if(difficultyLevel == 2):
            for i in range (10):
                guessed = int(input("Make a guess:"))
                if (guessed == target):
                    print ("You won");
                    break
                if (guessed != target):
                    initScore -= 10;
                    lowerOrHigher = compareHint (guessed, target)
                    print(lowerOrHigher);
                    differenceMessage = rangeHint (target, guessed)
                    print(differenceMessage)
                    print(f"Your current score is {initScore}")
                    remainingAttempts = 20 - (i+1)
                    print(f" You have {remainingAttempts} remaining attempts")        

    if(difficultyLevel == 3):
                for i in range (5):
                    guessed = int(input("Make a guess:"))
                    if (guessed == target):
                        print ("You won");
                        break
                    if (guessed != target):
                        initScore -= 20;
                        lowerOrHigher = compareHint (guessed, target)
                        print(lowerOrHigher);
                        differenceMessage = rangeHint (target, guessed)
                        print(differenceMessage)
                        print(f"Your current score is {initScore}")
                        remainingAttempts = 20 - (i+1)
                        print(f" You have {remainingAttempts} remaining attempts")
        



# Start of Game
while(retry == 1):
    print("""
    
     ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄              
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌             
▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀              
▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌                       
▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄              
▐░▌▐░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌             
▐░▌ ▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌             
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌                    ▐░▌          ▐░▌             
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌             
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌             
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀              
                                                                              
 ▄▄▄▄▄▄▄▄▄▄▄                                                                  
▐░░░░░░░░░░░▌                                                                 
▐░█▀▀▀▀▀▀▀█░▌                                                                 
▐░▌       ▐░▌                                                                 
▐░█▄▄▄▄▄▄▄█░▌                                                                 
▐░░░░░░░░░░░▌                                                                 
▐░█▀▀▀▀▀▀▀█░▌                                                                 
▐░▌       ▐░▌                                                                 
▐░▌       ▐░▌                                                                 
▐░▌       ▐░▌                                                                 
 ▀         ▀                                                                  
                                                                              
 ▄▄        ▄  ▄         ▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░▌      ▐░▌▐░▌       ▐░▌▐░░▌     ▐░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌░▌     ▐░▌▐░▌       ▐░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌▐░▌    ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  
▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀     

    """)

    print("Computer: I am thinking of a number from 1 to 100, [1, 100] ,try to guess it...")
    difficultyLevel = int(input("Choose difficulty by typing the index no: 1. Easy, 2. Medium, 3. Hard "))
    gamePlay(difficultyLevel);

    retryF();
