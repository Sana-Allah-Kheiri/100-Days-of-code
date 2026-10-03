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

travel_log = [

    {
        "country": "Turkey",
        "noOfVisits" : 1,
        "visited_cities" : ['Istanbul' , 'Vaan' ]
    }
,
    {
        "country": "Finland",
        "noOfVisits" : 1,
        "visited_cities" : ['Helsinki']

    }
,
]

def update_travel_log (country, numOfVisits, visitedCities):
    newDic = {"country": country , "noOfVisits": numOfVisits , "visited_cities" : visitedCities }
    travel_log.append(newDic)
    return travel_log;


# Start of travel logger

while(retry == 1):

    print("""
#######                             #                                  
   #    #####    ##   #    # ###### #        ####   ####  ###### ##### 
   #    #    #  #  #  #    # #      #       #    # #    # #      #    #
   #    #    # #    # #    # #####  #       #    # #      #####  #    #
   #    #####  ###### #    # #      #       #    # #  ### #      ##### 
   #    #   #  #    #  #  #  #      #       #    # #    # #      #   # 
   #    #    # #    #   ##   ###### #######  ####   ####  ###### #    #
    """)

    visitedCountry = input(" Which country did you visit?")
    noOfVisits = int(input(f" How many times did you visit{visitedCountry}?"))
    noOfVisitedCities = int(input("How many cities did you visit?"))
    cities = [];
    for i in range(noOfVisitedCities):
        cityVisited = input("Enter name of visited city:")
        cities.append(cityVisited);
    
    travel_log = update_travel_log(visitedCountry , noOfVisits , cities)

    print(travel_log);


    retryF();
