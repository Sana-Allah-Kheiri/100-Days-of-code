#By https://github.com/Sana-Allah-Kheiri/100-Days-of-code

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
    retry = input(" Type 0 to exit | Type 1 to restart the game");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;
        
while(retry == 1):
    print(" Lets see if a number is an odd or even !");
    num = input(" Enter an integer : ");
    num = int(num);
    
    if (num % 2 == 0):
        print(" Even ");
        
    if (num % 2 == 1):
        print(" Odd ");
        
    retryF();