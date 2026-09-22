# Full archive at Day8 folder of https://github.com/Sana-Allah-Kheiri/100-Days-of-code

import sys
import time
import random
retry = 1

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


def primeOrNot(number):
    flag = True
    if (number == 1):
        flag = False
    if (number == 2):
        flag = True
    for i in range(2, number//2):
        if(number%i==0):
            flag = False
    return flag; #If flag is True then the number is Prime, and vice versa


    


# Start of Prime Checker script

while(retry == 1):
    print("""

ooooooooo.             o8o                              oooo   o8o      .  
`888   `Y88.           `"'                              `888   `"'    .o8  
 888   .d88' oooo d8b oooo  ooo. .oo.  .oo.    .oooo.    888  oooo  .o888oo
 888ooo88P'  `888""8P `888  `888P"Y88bP"Y88b  `P  )88b   888  `888    888  
 888          888      888   888   888   888   .oP"888   888   888    888  
 888          888      888   888   888   888  d8(  888   888   888    888 .
o888o        d888b    o888o o888o o888o o888o `Y888""8o o888o o888o   "888"
                                                                           
                                                                           
                                                                           
                   .oooooo.   oooo                            oooo         
                  d8P'  `Y8b  `888                            `888         
oooo    ooo      888           888 .oo.    .ooooo.   .ooooo.   888  oooo   
 `88.  .8'       888           888P"Y88b  d88' `88b d88' `"Y8  888 .8P'    
  `88..8'        888           888   888  888ooo888 888        888888.     
   `888'         `88b    ooo   888   888  888    .o 888   .o8  888 `88b.   
    .8'           `Y8bood8P'  o888o o888o `Y8bod8P' `Y8bod8P' o888o o888o  
.o..P'                                                                     
`Y8P'                                                                      

""")   

    num = int(input("Enter a positive integer: "))

    if(primeOrNot(num)):
        print(f"{num} is Prime");
    else:
        print(f"{num} Not prime")
    
    retryF()