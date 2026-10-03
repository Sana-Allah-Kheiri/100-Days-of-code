# Full archive at Day8 folder of https://github.com/Sana-Allah-Kheiri/100-Days-of-code

import sys
import time
import random
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


def RetrievKey(target_value, Dic):
    return (next(k for k, v in Dic.items() if v == target_value) , None)


def determineWinner(BiDic):
    winnerName = ""
    BidAmounts = [];
    for key in BiDic:
        BidAmounts.append(BiDic[key])
    max_amount = max(BidAmounts)
    for money in BiDic.values():
        if (max_amount == money):
            winnerName = RetrievKey(max_amount, BiDic)
            break;
    finaList = []
    finaList.append(winnerName)
    finaList.append(max_amount)
    return (finaList);







# Start of secret bid

while(retry == 1):
    print("""
 ____       _            _         ____  _     _ 
|  _ \ _ __(_)_   ____ _| |_ ___  | __ )(_) __| |
| |_) | '__| \ \ / / _` | __/ _ \ |  _ \| |/ _` |
|  __/| |  | |\ V / (_| | ||  __/ | |_) | | (_| |
|_|   |_|  |_| \_/ \__,_|\__\___| |____/|_|\__,_|
    """)  
    BiDic = {} #Bid Dictionary which is a two-field DataBase
    # with N records
    biddersPopulation = int(input("How many people are bidding?"))
    for i in range(biddersPopulation):
        BidderName = input("Enter name of bidder: ")
        bidAmount = float(input("How much in USD? "))
        BiDic.update({BidderName : bidAmount})

    print('*******Winner of Bid********')
    winner_bidAmount = determineWinner(BiDic)
    print(f" Winner is{winner_bidAmount[0]} who spent {winner_bidAmount[1]} USD")
    







    retryF();
