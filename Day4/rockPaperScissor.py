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


def print_rock():
    rock = r"""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
    """
    print(rock)


def print_paper():
    paper = r"""
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
    """
    print(paper)


def print_scissors():
    scissors = r"""
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
    """
    print(scissors)


# Start of Script

while(retry == 1):
    userChoice = input(" Type 0 for rock | 1 for paper | 2 for Scissor ");
    print("You chose: ", userChoice);
    userChoice = int(userChoice);
    match userChoice: #print ASCII art of user choice
            case 0:
                print_rock();
            case 1:
                print_paper();
            case 2:
                print_scissors();



    computerChoice = random.randint(0, 2);
    print("Computer chose: ", computerChoice);

    match computerChoice: #print ASCII art of computer choice
        case 0:
            print_rock();
        case 1:
            print_paper();
        case 2:
            print_scissors();




    if (userChoice == computerChoice):
        print("Its a Draw !");
        
    elif(computerChoice == 0 and userChoice == 1):
        print(" You won !");
        
    elif(computerChoice == 1 and userChoice == 0):
            print(" Computer won !");
            
    elif(computerChoice == 0 and userChoice == 2):
                print(" Computer won !");
                
    elif(computerChoice == 2 and userChoice == 0):
                print(" You won !");
                
    elif(computerChoice == 1 and userChoice == 2):
                print(" You won !");
                
    elif(computerChoice == 2 and userChoice == 1):
                print(" Computer won !");
                
    else:
           print("Invalid input! ");


    retryF();
