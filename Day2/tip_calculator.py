#By Sasan at https://github.com/Sana-Allah-Kheiri/100-Days-of-code/
# User enters a bill price, tip percentage & the app prints the name alphabet by alphabet
# Tutorial Goal is to understand that string = array = list = pointers(In C++ actually)
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
    retry = input(" Type 0 to exit | Type 1 to restart");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;
        
while(retry==1):
    bill_total_price = input("Total bill price in USD : ");
    bill_total_price = float(bill_total_price);
    population = input("How many people are there?");
    population = float(population);
    tip_percent = input("How much of total bill is for tip? 1. 10% 2. 12% 3. 15%");
    tip_percent = int(tip_percent);
    if(tip_percent == 1):
        print( "Share of each = " , round((1.1*bill_total_price)/population , 2) );
    if(tip_percent == 2):
        print( "Share of each = " , round((1.12*bill_total_price)/population , 2) );
    if(tip_percent == 3):
        print( "Share of each = " , round( (1.15*bill_total_price)/population , 2) );
    
    
    retryF();