#By Sasan at https://github.com/Sana-Allah-Kheiri/100-Days-of-code/
# User enters a number & the app prints the name alphabet by alphabet
# Tutorial Goal is to understand that string = array = list = pointers(In C++ actually)
import sys
import time
retry = 1;

def exitF(): # To exit the app
    print("Exiting app after 3 seconds...");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    sys.exit("Goodbye!")


def retryF(): # To improve user experience
    retry = input(" Type 0 to exit | Type 1 to restart");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;
        
while(retry==1):
    userNum = input(" How old R U? ");
    sum = 0;
    for dig in userNum:
        dig = int(dig);
        sum += dig;
    print('Sum of digits = ' , sum);
    
    retryF();