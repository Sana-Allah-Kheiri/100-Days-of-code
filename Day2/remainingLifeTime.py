#By Sasan at https://github.com/Sana-Allah-Kheiri/100-Days-of-code/
# User enters his/her age & program prints how many days , weeks & months he / she has till the age of 90
#Remember to use f-string function to print the final result
import sys
import time
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
    retry = input(" Type 0 to exit | Type 1 to restart");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;
        
while(retry==1):
    userAge = input(" How old R U ? ");
    userAge = int(userAge);
    days = 365 * (90-userAge);
    weeks = days/7
    months = (90-userAge) * 12;
    print(f'You have {days} days , {weeks} weeks & {months} months');
    
    
    
    
    
    
    retryF();