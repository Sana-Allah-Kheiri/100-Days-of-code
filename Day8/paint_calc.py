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

def total_cost_calc(color, height, width, cov_rate):
    costOfEachLiter = 0.0;
    color = color.lower()
    match color:
        case "green":
            costOfEachLiter = 2.65
        case "red":
            costOfEachLiter = 1.99
        case "blue":
            costOfEachLiter = 4.89
        case "white":
            costOfEachLiter = 6.89
        case "purple":
            costOfEachLiter = 8.99
        case "pink":
            costOfEachLiter = 7.39


    toBpaintedArea = height * width;
    numberOfCans = toBpaintedArea / cov_rate;

    return (costOfEachLiter * numberOfCans)

# Start of Caesar Cipher script

while(retry == 1):
    print("""
.---------------------------------------------------------------.
|   ___      _       _       ___                ___      _      |
|  / _ \__ _(_)_ __ | |_    / __\__ _ _ __     / __\__ _| | ___ |
| / /_)/ _` | | '_ \| __|  / /  / _` | '_ \   / /  / _` | |/ __||
|/ ___/ (_| | | | | | |_  / /__| (_| | | | | / /__| (_| | | (__ |
|\/    \__,_|_|_| |_|\__| \____/\__,_|_| |_| \____/\__,_|_|\___||
'---------------------------------------------------------------'
 """)   

    print("I enable you to estimate how much money you need to paint your wall.");
    color = input("What is your favorite color: red, green, blue, white, purple, pink.")
    height = float(input("Height of wall: "))
    width = float(input("Width of wall: "))
    cov_rate = float(input("How many sqaure meters ONE can covers? "))
    totalCost = total_cost_calc(color, height, width, cov_rate)

    print(f" Total cost in USD: {round(totalCost, 2)} $ ")
    retryF()