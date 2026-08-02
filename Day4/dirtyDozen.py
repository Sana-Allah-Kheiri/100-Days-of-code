import sys
import time
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
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print(" Welcome to Dirty Dozen checker robot.");
    print ("I help you find out which vegetables and which fruits are affected by pesticide");
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

    dirtyVegs = ["spinach" , "kale" , "tomatoes" , "celery" , "potatoes"]
    dirtyFruits = ["strawBerries" , "nectarine" , "apple" , "grapes" , "peaches" , "cherries" , "pears"]
    dirtyDozen = [dirtyFruits , dirtyVegs]


    userChoice = input(" Type 0 for list of dirty fruits | 1 for vegetables ")
    userChoice = int(userChoice)
    match userChoice:
        case 0:
            print(" List of dirty fruits: " , dirtyDozen[0] );
        case 1:
            print(" List of dirty vegetables: " , dirtyDozen[1] );






    retryF();