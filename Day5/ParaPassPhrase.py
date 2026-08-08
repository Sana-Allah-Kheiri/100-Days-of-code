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

def generateSecurePassword(lettersNo, SymbolsNo, DigitsNo):
    listOfLetters = [];
    listOfDigits = [];
    listOfSymbols = [];
    concatinatedList = [];
    finalPassWord = " ";
    
    for i in range(DigitsNo):
        newDigitASCIIcode = random.randint(48, 57);
        newDigit = chr(newDigitASCIIcode);
        listOfDigits.append(newDigit);
        
    for j in range(SymbolsNo):
        if(j%3==0):
            newSymbolASCIIcode = random.randint(33, 47);
            newSymbol = chr(newSymbolASCIIcode);
            listOfSymbols.append(newSymbol);
        elif(j%3==1):
            newSymbolASCIIcode = random.randint(58, 64);
            newSymbol = chr(newSymbolASCIIcode);
            listOfSymbols.append(newSymbol);
        else:
            newSymbolASCIIcode = random.randint(91, 96);
            newSymbol = chr(newSymbolASCIIcode);
            listOfSymbols.append(newSymbol);
    
    for k in range(lettersNo):
        if (k%2==0):
            newLetterASCIIcode = random.randint(97, 122);
            newLetter = chr(newLetterASCIIcode);
            listOfLetters.append(newLetter);
        elif(k%2==1):
            newLetterASCIIcode = random.randint(65, 90);
            newLetter = chr(newLetterASCIIcode);
            listOfLetters.append(newLetter);
            
    concatinatedList = listOfDigits + listOfSymbols + listOfLetters;
    random.shuffle(concatinatedList);
    
    for character in concatinatedList:
        finalPassWord  = finalPassWord + character;
        
    return (finalPassWord);



# Start of Script

while(retry == 1):
    print("=====================================================");
    print("Lets become unHackable forever with a strong password");
    print("=====================================================");
    
    lettersCardinality = input(" How many letters? ");
    lettersCardinality = int(lettersCardinality);
    SymbolsCardinality = input(" How many Symbols? ");
    SymbolsCardinality = int(SymbolsCardinality);
    NumbersCardinality = input(" How many Digits? ");
    NumbersCardinality = int(NumbersCardinality);
    
    print("=========== Here is your password ===========");
    print( generateSecurePassword(lettersCardinality, SymbolsCardinality, NumbersCardinality) );

    retryF();