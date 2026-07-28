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
    retry = input(" Type 0 to exit | Type 1 to restart ");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;
        
while(retry == 1):
    print(" Welcome to rollercoaster !");
    userHeight = input(" Enter your height in cm : ");
    userHeight = int(userHeight);
    userAge = input(" Enter your age : ");
    userAge = int (userAge);
    photo_ticket = input(" Wanna photo ticket? Y/N ");
    photo_ticket = photo_ticket.lower();
    
    price = 0.0;
    if(photo_ticket == "y"):
        price += 3.0;
    elif(photo_ticket == "n"):
        price += 0.0;
        
    if (userHeight>=120):
        if (userAge < 12 ):
            price += 5.0;
            print(f" Pay {price}$ and ride the rollercoaster.");
        if (userAge>=12 and userAge<=18):
            price += 7.0;
            print(f" Pay {price}$ and ride the rollercoaster.");
        if (userAge > 18 and userAge <45):
            price += 12.0;
            print(f" Pay {price}$ and ride the rollercoaster.");
        if (userAge>=45):
            price += 0.0;
            print(f" Pay {price}$ and ride the rollercoaster.");
        
        
    if (userHeight < 120  ):
        print(" You are too short for rollercoaster! come with your parents ");
        
    retryF();