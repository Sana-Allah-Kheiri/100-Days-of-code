# Full archive at Day12 folder of https://github.com/Sana-Allah-Kheiri/100-Days-of-code

import sys
import time
import random
import csv
retry = 1

def exitF(): # To exit the app
    print("Developed by...");
    print("Sana");
    time.sleep(1)
    print("ALLAH");
    time.sleep(1)
    print("Kheiri");
    sys.exit("Goodbye!")

def retryF(): # To improve user experience
    retry = input(" Type 0 to exit | Type 1 to restart ");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;


def playHigherLower():
    answerState = True
    score = 0;
    #scoreRecords = []
    SearchStats = {'cleaner': 1_220_000 , 'Porsche':2_740_000, 'SnowBoard':550_000, 
       'Stolen Generation': 18_100 , 'William Shakespeare': 550_000,
        'Heart Disease': 135_000, 'Hicham El Guerrouj':12_100, 
         'Domestic Abuse': 33_100, 'Love Island': 1_500_000 , 
          'PostTraumatic Stress Disorder': 4_400 , 'Aretha Franklin': 368_000,
           'The Sims': 1_830_000 , 'Peter Key': 246_000 , 'Sports Direct':5_000_000 ,
            'Beagle' : 1_500_000 , 'Lost':673_000 , 'Anorexia':550000 , 'Top Gear':673_000 ,
             'Warren Harding': 22_200 , 'Bruce Springsteen': 673_000 , 'Lays': 368_000 ,
              'Daft Punk' : 673_000 , 'Hong Kong': 1_500_000 , 'VolleyBall':673_000 ,
               'Monaco Grand Prix' : 49_500 , 'Rosa Parks': 450_000 , 'iPhone7': 11_100_000 ,
                'Vienna' : 450_000 , 'Prince Charles' : 550_000 , 'Milgram Experiment' : 49_500 ,
                 'Uber' : 20_400_000 , 'Mini Cooper' : 1_500_000  }
    while (answerState):
        listOfKeyWords = list (SearchStats.keys())

        InitialKeyWord2Shown = random.choice(listOfKeyWords)
        statOnQuestion = SearchStats[InitialKeyWord2Shown]

        print(f"{InitialKeyWord2Shown} has {statOnQuestion:,} search volume")

        listOfKeyWords.remove(InitialKeyWord2Shown)
        SecondKeywordList = listOfKeyWords
        SecondKeywordList = list(SecondKeywordList)
        SecondKeyword2Bguessed = random.choice(SecondKeywordList)
        print(f"Do you think {SecondKeyword2Bguessed} has lower, equal or higher volume?")
        userAnswer = input("Press L for lower, H for Higher, E for equal : ").lower()
        correctAnswer = ""
        secondStat2Bguessed = SearchStats[SecondKeyword2Bguessed]
        if (statOnQuestion > secondStat2Bguessed):
            correctAnswer = "l";
            #scoreRecords.append(score)
        if (statOnQuestion < secondStat2Bguessed):
            correctAnswer = "h";
        if (statOnQuestion == secondStat2Bguessed):
            correctAnswer = "e";
        #Evaluating answer state
        if (userAnswer == correctAnswer):
            answerState = True
        if (userAnswer != correctAnswer):
            answerState = False
            print(f"{SecondKeyword2Bguessed} has {secondStat2Bguessed:,} searches")

            
    if(answerState == False):
        #bestscore = max(scoreRecords)
        print(f"Game over")
    

    



# Start of Game
while(retry == 1):
    print("""

            __  ___       __              __                           
   / / / (_)___ _/ /_  ___  _____/ /   ____ _      _____  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/ /   / __ \ | /| / / _ \/ ___/
 / __  / / /_/ / / / /  __/ /  / /___/ /_/ / |/ |/ /  __/ /    
/_/ /_/_/\__, /_/ /_/\___/_/  /_____/\____/|__/|__/\___/_/     
        /____/                                                 

    """)

    playHigherLower()
   
    retryF();
