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

def isLeapYear(year):
    #year = input(" Enter year to determine if its leap or not : ")
    year = int(year)
    determiner = False;
        
    if(year%4 == 0):
      determiner = True;
      if(year%100 == 0):
         determiner = False; # Like 1800 , 1900 , 2100 , 2200 , 2300 , 2500 are NOT Leap
         if (year%400==0):
            determiner = True; # Like 2000 and 2400 are leap years
    return (determiner)

def DayCounter(year, month):
    noOfDaysInMonth = 30;
    if (isLeapYear(year)):
        monthDic = {1 : 31, 2 : 29 , 3 : 31 , 4 : 30 , 5 : 31 , 
                    6 : 30 , 7 : 31 , 8 : 31 , 9 : 30 , 10 : 31 , 11 : 30 , 12 : 31}
        noOfDaysInMonth = monthDic[month]
    
    else:
        monthDic = {1 : 31, 2 : 28 , 3 : 31 , 4 : 30 , 5 : 31 , 
                            6 : 30 , 7 : 31 , 8 : 31 , 9 : 30 , 10 : 31 , 11 : 30 , 12 : 31}
        noOfDaysInMonth = monthDic[month]

    return noOfDaysInMonth


# Start of day counter

while(retry == 1):
    year = int(input("Input year: "))

    print(""" 
    1. Jan
    2. Feb
    3. March
    4. April
    5. May
    6. June
    7. July
    8. Aug
    9. Sep
    10.Oct
    11.Nov
    12.Dec

    """)

    month = int(input("Enter month number from above list:"))

    finalResult = DayCounter(year, month);
    
    print(f"The month: {month} in year {year} has {finalResult} days")
    

    retryF();
