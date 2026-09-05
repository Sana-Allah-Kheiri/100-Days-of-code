# Full archive at https://github.com/Sana-Allah-Kheiri/100-Days-of-code

import sys
import time
import random
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

def RandomCategoryGenerator(): # To generate a random category
    categories = ["Animals", "Fruits", "Countries", "Colors"];
    random.shuffle(categories)
    random_index = random.randint(0,3)
    return categories[random_index]

def RandomWordGenerator(category):
    randomWord = "";
    animals = ["lion" , "cat" , "lizard" , "cow" , "seal" ]
    fruits = ["apple" , "orange" , "peach" , "cucumber" , "cherry"]
    countries = ["USA", "Canada" , "Italy" , "Japan" , "England"]
    colors = ['green' , 'blue' , 'red' , 'purple' , 'pink']
    random.shuffle(animals)
    random.shuffle(fruits)
    random.shuffle(countries)
    random.shuffle(colors)
    match category:
        case "Animals":
            randomWord = random.choice(animals)
        case "Fruits":
            randomWord = random.choice(fruits)
        case "Countries":
            randomWord = random.choice(countries)
        case "Colors":
            randomWord = random.choice(colors)
    return randomWord;

def printHangASCII (attemptNo):
    match attemptNo:
        case 0:
            print("""
                ############
                #          
                #
                #
                #
              =====
             """)
        case 1:
            print("""
                ############
                #          O
                #
                #
                #
              =====
             """)
        case 2:
            print("""
                ############
                #          O
                #          |
                #          | 
                #
              =====
            """)
        case 3:
            print("""
                ############
                #          O
                #          |/
                #          | 
                #
              =====
            """)
        case 4:
            print("""
                ############
                #          O
                #         \|/
                #          | 
                #
              =====
            """)
        case 5:
            print("""
                ############
                #          O
                #         \|/
                #          | 
                #         /
              =====
             """)
        case 6:
            print("""
                ############
                #          O FUCK YOU!!!
                #         \|/
                #          | 
                #         / \ 
              =====
            """)

def currentScore (attemptNo):
    scoree = 0
    match attemptNo:
        case 0:
            scoree = 100
        case 1:
            scoree = 80
        case 2:
            scoree = 60
        case 3:
            scoree = 40
        case 4:
            scoree = 20
        case 5:
            scoree = 10
        case 6:
            scoree = 0
    return(scoree)

def CheckGuess (guessedletter , targetWord):
    found_flag = False
    for letter in targetWord:
        if (letter == guessedletter):
            found_flag = True
    return found_flag

def hintPrint (guessedletter, targetWord, n, hintSequence):
    for j in range(n):
        if (targetWord[j] == guessedletter):
            hintSequence[j] = guessedletter
    finalHint = " ".join(hintSequence) #converting list to string
    return finalHint

    



# Start of Script

while(retry == 1): #game retry
    attemptNo = 0;
    score = 100
    guessedletter = ""
    hintCategory = RandomCategoryGenerator() #Generate category
    targetWord = RandomWordGenerator(hintCategory) #generate word based on category
    targetWord = targetWord.lower(); #make all letters lower-case
    n = len(targetWord)
    hintSequence = []
    for i in range(n):
        hintSequence.append("_ ")
          
    print("***********")
    print(hintCategory)
    print("***********")
    
    while (attemptNo <= 5): # Controlling hangman life
        score = currentScore(attemptNo)
        print(f" Life = {score} out of 100")
        printHangASCII(attemptNo)
        guessedLetter = input(" Guess a letter : ");
        if (CheckGuess(guessedLetter, targetWord)):
            hintPhrase = hintPrint(guessedLetter, targetWord, n, hintSequence) 
            print(hintPhrase)
        else:
            attemptNo +=1;

    printHangASCII(attemptNo)
    if (targetWord == hintPhrase):
        print(f"Congrats you won! You score is {score}")
    retryF();
