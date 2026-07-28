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
    print(" Welcome to Love Calculator !");
    
    userName = input(" What's your name? ");
    userName = userName.lower();
    
    partnerName = input(" What's their name? ");
    partnerName = partnerName.lower();
    
    concatinated_name = userName + partnerName;
    
    L_frequency = 0;
    O_frequency = 0;
    V_frequency = 0;
    E_frequency = 0;
    
    for alp in concatinated_name:
        if(alp == "l"):
            L_frequency += 1;
        if(alp == "o"):
            O_frequency += 1;
        if(alp == "v"):
            V_frequency += 1;
        if(alp == "e"):
            E_frequency += 1;        
    
    right_digit = L_frequency + O_frequency + V_frequency + E_frequency;
    
    T_frequency = 0;
    R_frequency = 0;
    U_frequency = 0;
    E_frequency = 0;
    
    
    for alp in concatinated_name: # or use count() function
        if(alp == "t"):
            T_frequency += 1;
        if(alp == "r"):
            R_frequency += 1;
        if(alp == "u"):
            U_frequency += 1;
        if(alp == "e"):
            E_frequency += 1;
    
    left_digit = T_frequency + R_frequency + U_frequency + E_frequency;
    
    compatibility_percent = (10* left_digit) + right_digit ;
    
    if (compatibility_percent < 10 or compatibility_percent > 90):
        print(f" Your score is {compatibility_percent} % , you go together like coke and mentos ");
        
    elif (compatibility_percent > 40 and compatibility_percent < 50):
        print(f" Your score is {compatibility_percent} % , you are alright together ");
        
    else:
        print(f" Your score is {compatibility_percent} %  ");
        
    retryF();