import sys
import time
import random
retry = 1;

def exitF(): # To exit the app
    print("Exiting app after 5 seconds...");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    sys.exit("Goodbye!")


def retryF(): # To improve user experience
    retry = input(" Type 0 to exit | Type 1 to restart ");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;

# Start of Script

while(retry == 1):
    userChoice = input(" Heads or Tails ? ");
    userChoice = userChoice.lower();
    #generating sudo-random for (1: Head) or (0: Tails)
    TossResult = random.randint(0, 1);
    #showing result of toss to user
    if (TossResult == 1):
          print("""
          █▀▀ █▀█ █ █▄░█   █░█ █▀▀ ▄▀█ █▀▄ █▀
          █▄▄ █▄█ █ █░▀█   █▀█ ██▄ █▀█ █▄▀ ▄█
                   """)
    elif(TossResult == 0):
          print("""
          
            █▀▀ █▀█ █ █▄░█   ▀█▀ ▄▀█ █ █░░ █▀
            █▄▄ █▄█ █ █░▀█   ░█░ █▀█ █ █▄▄ ▄█

          """)


    if(userChoice == "heads" and TossResult == 1):
        print(" You start the game! ");
    if(userChoice == "heads" and TossResult == 0):
            print(" I start the game! ");
    
    if(userChoice == "tails" and TossResult == 1):
            print(" I start the game! ");
    if(userChoice == "tails" and TossResult == 0):
                print(" You start the game! ");

    retryF();