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
    print(" Welcome to Pizza cashier machine !");
    
    pizza_size = input(" What size of pizza do you order? Type 'S' 'M' or 'L' ");
    pizza_size = pizza_size.lower();
    #print(pizza_size)
    
    pep_or_not = input(" Do you want Pepperoni? Y/N ");
    pep_or_not = pep_or_not.lower();
    #print(pep_or_not);
    
    extra_cheese = input(" Wanna extra cheese? Y/N ");
    extra_cheese = extra_cheese.lower();
    #print(extra_cheese);
    total_bill = 0.0;
    match pizza_size:
        case "s":
            total_bill += 15.0;
        case "m":
            total_bill += 20.0;
        case "l":
            total_bill += 25.0;
            
    if(pep_or_not == "y"):
        if(pizza_size == "s"):
            total_bill += 2.0;
        if(pizza_size == "m" or pizza_size == "l"):
            total_bill += 3.0;
            
    if (extra_cheese == "y"):
        total_bill += 1.0;
        
    print (f" Your final bill is: {total_bill} $")
        
    retryF();