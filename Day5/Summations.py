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


def summA (n):
    return ( (n*(n+1) / 2) )
    
def summB (n):
    return ( (n*(n+1)*(2*n+1)) / 2 )
    
def summC (n):
    return ( (n*n*(n+1)*(n+1)) / 4 )
    
def summD (n):
    return (n*n);
    
def summE (n):
    return(n*(n+1));
    



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
    print(" Which of the following summations do you want to calculate?");
    print(" a) 1 + 2 + 3 + ... + n = ? ");
    print(" b) 1^2 + 2^2 + 3^2 + ... + n^2 = ? ");
    print(" c) 1^3 + 2^3 + 3^3 + ... + n^3 = ?");
    print(" d) 1 + 3 + 5 + ... + (2n-1) = ?");
    print(" e) 2 + 4 + 6 + ... +  2n = ?");
    userChoiceList = input("a  b  c  d  e ?").split();
    n = input(" Enter length of summation or n: ")
    n = int(n);
    for choice in userChoiceList:
        if (choice == "a" or choice == "A"):
            result = summA (n);
            print(f"1 + 2 + 3 + ... + {n} = {result}");
            
        if (choice == "b" or choice == "B"):
            sumB = summB(n);
            print(f"1^2 + 2^2 + 3^2 + ... + {n} ^ 2 = {sumB}");
            
        if (choice == "c" or choice == "C"):
            sumC = summC(n);
            print(f"1^3 + 2^3 + 3^3 + ... + {n} ^ 3 = {sumC}");
            
        if (choice == "d" or choice == "D"):
            sumD = summD(n);
            print(f"1 + 3 + 5 + ... + (2{n}-1) = {sumD}");
            
        if (choice == "e" or choice == "E"):
            sumE = summE(n);
            print(f"2 + 4 + 6 + ... +  2{n} = {sumE}");
        
    
    

    retry = retryF()