# Full archive at Day8 folder of https://github.com/Sana-Allah-Kheiri/100-Days-of-code

import sys
import time
import random
from random import shuffle
import csv
retry = 1

def exitF(): # To exit the app
    print("Exiting app after 5 seconds...");
    print("S");
    time.sleep(1)
    print("A");
    time.sleep(1)
    print("N");
    time.sleep(1)
    print("A");
    time.sleep(1)
    print("Allah Kheiri Developed this script");
    time.sleep(1)
    sys.exit("Goodbye!")

def retryF(): # To improve user experience
    retry = input(" Type 0 to exit | Type 1 to restart ");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;

def hardOrSoft(playerCardsInHand):
    result = True #True means Hard , False means SOFT
    for card in playerCardsInHand:
        if(card == 'A'):
            result = False
    return result

def SplitOrNOT(playerCardsInHand):
    result = False;
    if(playerCardsInHand[0] == playerCardsInHand[1]):
        result = True;
    return result;


# Beat any dealer with movie star Ben Campbell the math genius from Twenty One movie 
def BenackCampjack (playerCardsInHand, DealerUpcard ):
    cards = {"A":11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, "K":10 , "J":10 , "Q":10 }
    hint = "";
    DealerUpcard = cards[DealerUpcard]
    sumPlayer = 0;
    for cardvalue in playerCardsInHand:
        sumPlayer += cards[cardvalue]
    if (hardOrSoft(playerCardsInHand)): #If our hand is HARD
         if(sumPlayer >= 17):
             hint = "Benack Campjack: 'STAND!' "
         if((sumPlayer>= 12 and sumPlayer <= 16) and (DealerUpcard>=2 and DealerUpcard<=6)):
             hint = "Benack Campjack: 'STAND!' "
         if(sumPlayer <= 8):
             hint = "Benack Campjack: 'HIT' "
         if((sumPlayer>= 12 and sumPlayer <= 16) and ((DealerUpcard>=7 and DealerUpcard<=10) or (DealerUpcard=="A") )):
            hint = "Benack Campjack: 'STAND!' "
         if (SplitOrNOT(playerCardsInHand)):#If our cards are the same
             if ( (playerCardsInHand[0] == 8) or (playerCardsInHand[0] == "A") ):
                 hint = "Benack Campjack: 'SPLIT' "
             if( ((playerCardsInHand[0] == 2) or (playerCardsInHand[0] == 3)) and (DealerUpcard>=2 and DealerUpcard<=7) ):
                 hint = "Benack Campjack: 'SPLIT' "
             if ( (playerCardsInHand[0] == 4) and (DealerUpcard>=5 and DealerUpcard<=6) ):
                 hint = "Benack Campjack: 'SPLIT' "
             if ( (playerCardsInHand[0] == 6) and (DealerUpcard>=2 and DealerUpcard<=6) ):
                 hint = "Benack Campjack: 'SPLIT' "
             if ( (playerCardsInHand[0] == 7) and (DealerUpcard>=2 and DealerUpcard<=7) ):
                 hint = "Benack Campjack: 'SPLIT' "
             if ( (playerCardsInHand[0] == 9) and ( (DealerUpcard>=2 and DealerUpcard<=6) or (DealerUpcard>=8 and DealerUpcard<=9) ) ):
                 hint = "Benack Campjack: 'SPLIT' "
             if (playerCardsInHand[0] == 5):
                 hint = "Benack Campjack: 'Double DOWN, DONT SPLIT' "
             if (cards[playerCardsInHand[0]] == 10):
                 hint = "Benack Campjack: STAND, DONT SPLIT"
         if(sumPlayer == 11): #DOUBLE DOWN Criteria in HARD hand
             hint = "Benack Campjack: 'DOUBLE DOWN' "
         if((sumPlayer == 10) and (DealerUpcard>=2 and DealerUpcard<=9)):
             hint = "Benack Campjack: 'DOUBLE DOWN' "
         if((sumPlayer == 9) and (DealerUpcard>=3 and DealerUpcard<=6)):
             hint = "Benack Campjack: 'DOUBLE DOWN' "    
    if (hardOrSoft(playerCardsInHand) == False ): #If our hand is SOFT
         if(sumPlayer>=19):
             hint = "Benack Campjack: 'STAND!' "
         if((sumPlayer == 18) and (DealerUpcard == 2 or DealerUpcard == 7 or DealerUpcard ==8 )):
             hint = "Benack Campjack: 'STAND' "
         if (sumPlayer>=13 and sumPlayer<= 17):
             hint = " Benack Campjack: 'HIT' "
         if ((sumPlayer == 18) and (DealerUpcard==9 or DealerUpcard==10 or DealerUpcard=="A")):
             hint = "Benack Campjack: 'HIT' "
         if((sumPlayer>=13 and sumPlayer<= 18) and (DealerUpcard>=4 and DealerUpcard<= 6 ) ):
             hint = "Benack Campjack: 'DoubleDown' "
                                     
    return hint;     

         
def handoffCards(cards):
    #playerHand = ["" , ""];
    #dealerHand = ["" , ""];
    hands = {"player":[] , "dealer":[]}
    cardNames = list(cards.keys()) # 2, 3, ... , 10, K, Q, J, A
    AceLessCarDeck = cardNames.remove("A")
    #To prevent BUST in the first place
    hands["player"].append(random.choice(cardNames))
    if (hands["player"][0]=="A"):
        hands["player"].append(random.choice(AceLessCarDeck))
    else:
        hands["player"].append(random.choice(cardNames))

     
    hands["dealer"].append(random.choice(cardNames))
    if (hands["dealer"][0]=="A"):
        hands["dealer"].append(random.choice(AceLessCarDeck))
    else:
        hands["dealer"].append(random.choice(cardNames))

    return hands;
    
def showOptionsToPlayer(betAmount, playerCardsInHand, DealerUpcard ):
    optionList = ["1. Hit" , "2. Stand" , "3. Double Down" ]

    if(betAmount == 1000):
        optionList.pop("3. Double Down")

    if (SplitOrNOT(playerCardsInHand)): #RULE: You can split only if two cards in you hand are pair
        optionList.append("4. Split")

    if (DealerUpcard == "A"):
        optionList.append("5. Insurance") #RULE: You can get insurance if dealer has Ace

    return(optionList);


#def showGameResult():

def playGame ():
    gameResult = ""
    cards = {"A":11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, "K":10 , "J":10 , "Q":10 }
    print(""" 

oooooooooo.                                            oooo                    
`888'   `Y8b                                           `888                    
 888     888  .ooooo.  ooo. .oo.    .oooo.    .ooooo.   888  oooo              
 888oooo888' d88' `88b `888P"Y88b  `P  )88b  d88' `"Y8  888 .8P'               
 888    `88b 888ooo888  888   888   .oP"888  888        888888.                
 888    .88P 888    .o  888   888  d8(  888  888   .o8  888 `88b.              
o888bood8P'  `Y8bod8P' o888o o888o `Y888""8o `Y8bod8P' o888o o888o             
                                                                               
                                                                               
                                                                               
  .oooooo.                                              o8o                    
 d8P'  `Y8b                                             `"'                    
888           .oooo.   ooo. .oo.  .oo.   oo.ooooo.     oooo  .oooo.    .ooooo. 
888          `P  )88b  `888P"Y88bP"Y88b   888' `88b    `888 `P  )88b  d88' `"Y8
888           .oP"888   888   888   888   888   888     888  .oP"888  888      
`88b    ooo  d8(  888   888   888   888   888   888     888 d8(  888  888   .o8
 `Y8bood8P'  `Y888""8o o888o o888o o888o  888bod8P'     888 `Y888""8o `Y8bod8P'
                                          888           888                    
                                         o888o      .o. 88P                    
                                                    `Y888P                     
oooo                                                                           
`888                                                                           
 888  oooo                                                                     
 888 .8P'                                                                      
 888888.                                                                       
 888 `88b.                                                                     
o888o o888o                                                                    


 .oPYo. 8               8          o               8      
 8   `8 8               8          8               8      
o8YooP' 8 .oPYo. .oPYo. 8  .o      8 .oPYo. .oPYo. 8  .o  
 8   `b 8 .oooo8 8    ' 8oP'       8 .oooo8 8    ' 8oP'   
 8    8 8 8    8 8    . 8 `b.      8 8    8 8    . 8 `b.  
 8oooP' 8 `YooP8 `YooP' 8  `o.   oP' `YooP8 `YooP' 8  `o. 
:......:..:.....::.....:..::...::...::.....::.....:..::...
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                                          
ooooo          o                                          
  8            8                                          
  8   o    o  o8P .oPYo. oPYo.                            
  8   8    8   8  8    8 8  `'                            
  8   8    8   8  8    8 8                                
  8   `YooP'   8  `YooP' 8                                
::..:::.....:::..::.....:..::::                           
:::::::::::::::::::::::::::::::                           
:::::::::::::::::::::::::::::::                           

Developed by Sana-Allah Kheiri (sanaallahkheiri.dev)

    
                                     _____
         _____                _____ |6    |
        |2    | _____        |5    || o o |
        |  o  ||3    | _____ | o o || o o | _____
        |     || o o ||4    ||  o  || o o ||7    |
        |  o  ||     || o o || o o ||____9|| o o | _____
        |____Z||  o  ||     ||____S|       |o o o||8    | _____
               |____E|| o o |              | o o ||o o o||9    |
                      |____h|              |____L|| o o ||o o o|
                                  _____           |o o o||o o o|
                          _____  |K  WW|          |____8||o o o|
                  _____  |Q  ww| | /\{)|                 |____6|
           _____ |J  ww| | /\{(| | \/%%| _____
          |10 o || /\{)| | \/%%| |  %%%||A ^  |
          |o o o|| \/% | |  %%%| |_%%%>|| / \ |
          |o o o||   % | |_%%%O|        | \ / |
          |o o o||__%%[|                |  .  |
          |___0I|                       |____V|

    """)

    nickname = input(" Enter your nickname: ");
    initial_fund = 999.00
    print("""
    ⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣯ 4X1$ ⣀⣿⣿⣿⣿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣙⡛⠛⠛⢛⣋⣿⣿⣿ 4X5$⣤⡾⠿⠿⢿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣯⣉⡛⢛⣿⠿⠟⠛⠛⠿⢿⣟⠛⠛⣿4X100$⢀⣹⣿⣿⣿⣿
    ⣿⣿⣿⣿⣯⣍⡛⢻⣧1X25$⣀⣠⣿⠛⢛⣿⡛⠷⠶⠶⠾⢛⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣭⣛⣻⣯⣍⣛⣛⣛⣋⣭⣿⣛⣛⣿⣛⡻⠶⠶⢟⣛⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣬⣍⣹⣷⣬⣉⣉⣉⣩⣴⣿⣉⣙⣿⣉⡛⠛⠛⢛⣉⣿⣿⣿⣿⣿
    ⣿⣿⣿⠟⠋⠉⠉⠙⠛⢿⣍⣉⣉⣭⣴⣿⣉⣉⣿⣍⡛⠛⠛⢛⣩⣽⣿⣿⣿⣿
    ⣿⣿⣿⣦1X50$⣤⣾⣏⣉⣉⣥⣴⣿⣉⣩⣿⣍⣻⣿⠿⠿⠿⢿⣿⣿⣿⣿
    ⣿⣿⣿⢶⣬⣭⣭⣭⡶⣿⣯⣭⣭⣥⣶⣿⣿⣿⣿⣽⣯1X1000$⣿⣿⣿
    ⣿⣿⣿⠶⣦⣤⣤⣴⠶⢿⣧⣼⠋1X500$ ⢻⣿⣯⣙⡛⠛⠛⢛⣩⣿⣿⣿
    ⣿⣿⣿⠷⣦⣤⣤⣴⠶⢿⣿⣿⠷⢶⣤⣤⣤⡶⢾⣿⣯⣉⡛⠛⠛⢛⣩⣿⣿⣿
    ⣿⣿⣿⠷⢶⣤⣤⣴⠶⣿⣿⣿⡿⢶⣤⣤⣤⠶⢿⣿⣯⣍⡛⠛⠛⣛⣩⣿⣿⣿
    ⣿⣿⣿⠻⠶⠶⠶⠶⠟⣿⣿⣿⣿⣷⣶⣶⣶⣾⣿⣿⣿⣬⣉⣉⣉⣩⣥⣿⣿⣿
    ⣿⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        """)
    betAmount = int(input(f"Hi {nickname},please bet by placing the  (MAX : 1000 USD)"))
    print(f" You have bet {betAmount} USD")
    currentHands = handoffCards(cards) #Return a dictionary
    playerCardsInHand = currentHands["player"] #LIST of two cards in player hand
    dealerCardsInHand = currentHands["dealer"] #List of two cards in dealer hand
    print('*******************************************')
    print(" Your hand : ", playerCardsInHand)
    CensoredDealerHand = ['#']
    DealerUpcard = dealerCardsInHand[0]
    #DealerUpcard = int(DealerUpcard)
    CensoredDealerHand.append(DealerUpcard)
    print(" Dealer hand : ", CensoredDealerHand)



    hint = BenackCampjack(playerCardsInHand, DealerUpcard);

    print(hint);

    playerOptions = showOptionsToPlayer(betAmount, playerCardsInHand, DealerUpcard )
    print(playerOptions)

    # 1. HIT, 2. Stand, 3. Double Down, 4. Split, 5. Insurance
    player_choice = int(input("Enter your choice: "))


    if(player_choice == 2): #Player STANDS scenario: Dealer Hits here
        cardNames = cards.keys()
        cardNames = list (cardNames)
        shuffle(cardNames)
        chosen_card = random.choice(cardNames) 
        DealerHandSumB4Hit = cards[dealerCardsInHand[0]] + cards[dealerCardsInHand[1]]
        DealerHandSumAfterHit = DealerHandSumB4Hit + cards[chosen_card]
        #DealerHandSumAfterHit = int(DealerHandSumAfterHit)
        if(DealerHandSumAfterHit > 21):
            print(f"dealer sum = {DealerHandSumAfterHit}")
            gameResult = "Dealer BUSTED! You Won.";
        
        if (DealerHandSumAfterHit <= 21):
            playerSum = cards[playerCardsInHand[0]] + cards[playerCardsInHand[1]]
            if (playerSum == DealerHandSumAfterHit):
                print(f"your sum = {playerSum} and Dealer sum = {DealerHandSumAfterHit}")
                gameResult = " PUSH!";
            if (playerSum > DealerHandSumAfterHit):
                print(f"your sum = {playerSum} and Dealer sum = {DealerHandSumAfterHit}")
                gameResult = "You won, "
            if (playerSum < DealerHandSumAfterHit):
                print(f"your sum = {playerSum} and Dealer sum = {DealerHandSumAfterHit}")
                gameResult = "You lost, "



    if (player_choice == 1): # Player HITs scenario and dealer stands to keep things simple
        cardNames = cards.keys()
        cardNames = list(cardNames)
        shuffle(cardNames)
        chosen_card = random.choice(cardNames)
        playerHandSum_beforeHit = playerCardsInHand[0] + playerCardsInHand[1]
        playerHandSum_AfterHit = int(playerHandSum_beforeHit) + cards[chosen_card]
        if (playerHandSum_AfterHit>21):
            print(f"your sum = {playerHandSum_AfterHit}")
            gameResult = "BUSTED: You Lost, your sum = {playerHandSum_AfterHit}"
        
        if(playerHandSum_AfterHit<=21):
            dealerSum = dealerCardsInHand[0] + dealerCardsInHand[1]
            if(dealerSum == playerHandSum_AfterHit):
                print(f"your sum = {playerHandSum_AfterHit} , dealer sum = {dealerSum}")
                gameResult = "PUSH!, your sum = {playerHandSum_AfterHit} , dealer sum = {dealerSum}"
            if (dealerSum > playerHandSum_AfterHit):
                print(f"your sum = {playerHandSum_AfterHit} , dealer sum = {dealerSum}")
                gameResult = "You lost, your hand sum = {playerHandSum_AfterHit} and dealer sum = {dealerSum}"
            if (dealerSum < playerHandSum_AfterHit):
                print(f"your sum = {playerHandSum_AfterHit} , dealer sum = {dealerSum}")
                gameResult = "You Won, your hand sum = {playerHandSum_AfterHit} and dealer sum = {dealerSum}"
                    

    if (player_choice == 3): #Player Doubles Down and dealer stands
        betAmount *= 2;
        print(f"Your current bet is {betAmount} and you wont be able to hit again.")
        cardNames = cards.keys()
        cardNames = list(cardNames)
        shuffle(cardNames)
        chosen_card = random.choice(cardNames)
        playerHandSum_beforeHit = cards[playerCardsInHand[0]] + cards[playerCardsInHand[1]]
        playerHandSum_AfterHit = playerHandSum_beforeHit + cards[chosen_card]
        if (playerHandSum_AfterHit>21):
            print(f"your sum = {playerHandSum_AfterHit}")
            gameResult = "BUSTED: You Lost, your sum = {playerHandSum_AfterHit}"
                
        if(playerHandSum_AfterHit<=21):
            dealerSum = cards[dealerCardsInHand[0]] + cards[dealerCardsInHand[1]]
            if(dealerSum == playerHandSum_AfterHit):
                print(f"your sum = {playerHandSum_AfterHit} , dealer sum = {dealerSum}")
                gameResult = "PUSH!, your sum = {playerHandSum_AfterHit} , dealer sum = {dealerSum}"
            if (dealerSum > playerHandSum_AfterHit):
                print(f"your sum = {playerHandSum_AfterHit} , dealer sum = {dealerSum}")
                gameResult = "You lost, your hand sum = {playerHandSum_AfterHit} and dealer sum = {dealerSum}"
            if (dealerSum < playerHandSum_AfterHit):
                print(f"your sum = {playerHandSum_AfterHit} , dealer sum = {dealerSum}")
                gameResult = "You Won, your hand sum = {playerHandSum_AfterHit} and dealer sum = {dealerSum}"


    return (gameResult);

    

        





# Start Playing BlackJack with Virtual Dealer using Smart Recom System

while(retry == 1):

    result = playGame();
    print(result)

    retryF();