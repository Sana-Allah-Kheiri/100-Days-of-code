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
    year = input(" Enter year to determine if its leap or not : ")
    year = int(year)
    determiner = False;
    
    if(year%4 == 0):
        determiner = True;
        if(year%100 == 0):
            determiner = False; # Like 1800 , 1900 , 2100 , 2200 , 2300 , 2500 are NOT Leap
            if (year%400==0):
                determiner = True; # Like 2000 and 2400 are leap years
            
    #------------------
    # Printing result
    # -----------------
    
    if( determiner==True ):
        print(f" {year} is leap year ");
    if(determiner == False):
        print(f" {year} is NOT leap year ");
        
    retryF();