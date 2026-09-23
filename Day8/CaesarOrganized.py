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

def caesar(opCode):
    result = "";
    if (opCode == 'E' or opCode == 'e'):
        original_msg = input(" >> Type your message : ")
        shiftNumber = input(" >> Enter incremental shift key ") # this is encrypytion key
        shiftNumber = int(shiftNumber) # Be careful
    #convert string message to list of characters
        CharList = list(original_msg)
        asciiCodeList = []
        ShiftCodesList = []
        EncryptedMessageList = []
        cipher = ""
        for singleChar in CharList: #listing ascii code of each character in message
            asciiCodeList.append(ord(singleChar))
        for eachASciiCode in asciiCodeList: # heart of encryption
            eachASciiCode += shiftNumber
        ShiftCodesList.append(eachASciiCode)
        for eachShiftedCode in ShiftCodesList:
            EncryptedMessageList.append(chr(eachShiftedCode))
        #Now I convert list to a single string representing cipher
        cipher = "".join(EncryptedMessageList)
        result = cipher
    if (opCode == 'D' or opCode == 'd'):
        cipher = input(" >> Enter the cipher to get it decrypted  ")
        shiftNumber = input(" >> Enter the shared key (the shift number) ")
        shiftNumber = int(shiftNumber) # Be careful
        #convert string message to list of characters
        CharList = list(cipher)
        asciiCodeList = []
        ShiftCodesList = []
        OriginalMessageList = []
        OriginalMessage = ""
        for singleChar in CharList: #listing ascii code of each character in message
            asciiCodeList.append(ord(singleChar))
        for eachASciiCode in asciiCodeList:
            eachASciiCode -= shiftNumber
            ShiftCodesList.append(eachASciiCode)
        for eachShiftedCode in ShiftCodesList:
            OriginalMessageList.append(chr(eachShiftedCode))
        #Now I convert list to a single string representing cipher
        OriginalMessage = "".join(OriginalMessageList)
        result = OriginalMessage

    return result




# Start of Caesar Cipher script

while(retry == 1):
    print("""
+-----------------------------------------------------------------+
|  ____                              ____ _       _               |
| / ___|__ _  ___  ___  __ _ _ __   / ___(_)_ __ | |__   ___ _ __ |
|| |   / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__||
|| |__| (_| |  __/\__ \ (_| | |    | |___| | |_) | | | |  __/ |   |
| \____\__,_|\___||___/\__,_|_|     \____|_| .__/|_| |_|\___|_|   |
|                                          |_|                    |
+-----------------------------------------------------------------+
 """)   

    userChoice = input(" >> Press E to encrypt or produce a cipher , press D to decrypt or crack the cipher: ")
    result  = caesar(userChoice)
    print("Result: ",result);

    retryF();
