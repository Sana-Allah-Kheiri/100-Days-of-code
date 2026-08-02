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

# Start of Script

while(retry == 1):
    numberOfGuests = input(" How many idle rich did you invite? ");
    numberOfGuests = int(numberOfGuests);
    ListOfGuests = [];
    for i in range(0 , numberOfGuests): #Filling guest list
        newGuestName = input(" Enter the fucking parasite name: ");
        ListOfGuests.append(newGuestName);

    random_index = random.randint(0, numberOfGuests-1);

    print(f" Mr {ListOfGuests[random_index]} is paying for the table")

    retryF();