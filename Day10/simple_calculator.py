# Full archive at Day8 folder of https://github.com/Sana-Allah-Kheiri/100-Days-of-code

import sys
import time
import random
import csv
retry = 1

def exitF(): # To exit the app
    print("Exiting app after 5 seconds...");
    print("S");
    time.sleep(1)
    print("A");
    time.sleep(1)
    print("S");
    time.sleep(1)
    print("A");
    time.sleep(1)
    print("N");
    time.sleep(1)
    sys.exit("Goodbye!")

def retryF(): # To improve user experience
    retry = input(" Type 0 to exit | Type 1 to restart ");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;


def calc (operand1, operand2, opcode):
    final_result = 0.00;
    match opcode:
        case "a":
            final_result = operand1 + operand2;
        case "b":
            final_result = operand1 - operand2;
        case "c":
            final_result = operand1 * operand2;
        case "d":
            final_result = operand1 / operand2;
    final_result = round(final_result, 3)
    return (final_result);


# Start of calculator script

while(retry == 1):

    print("""
 _____________________
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|


 """)
    print("a. +")
    print("b. -")
    print("c. x")
    print("d. /")

    opCode = input("Enter operation:").lower()
    firstOperand = float(input("First operand: "))
    SecondOperand = float(input("Second operand: "))
    final_result = calc(firstOperand, SecondOperand, opCode)
    print(f"{firstOperand} {opCode} {SecondOperand} = {final_result}")
    

    retryF();