# Full archive of 100Days OF Code in Python is at https://github.com/Sana-Allah-Kheiri/100-Days-of-code

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


# ==========================================
# Main Program
# ==========================================

while retry == 1:
    
    print("""
    
 _____ _           ____                
|  ___(_)________ | __ ) _   _ ________
| |_  | |_  /_  / |  _ \| | | |_  /_  /
|  _| | |/ / / /  | |_) | |_| |/ / / / 
|_|   |_/___/___| |____/ \__,_/___/___|
    
    """);

        
    for i in range(1, 101):
        if(i%5==0 and i%3==0):
            print("FizzBuzz");
        elif(i%5==0):
            print("Buzz");
            
        elif(i%3==0):
            print("Fizz");
            
        else:
            print(i);
    

    retry = retryF()
