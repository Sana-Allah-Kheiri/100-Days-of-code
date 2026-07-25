# By SasanAce.tech on https://github.com/Sana-Allah-Kheiri | https://www.linkedin.com/in/sasanace/ | https://www.youtube.com/@sasanace
# In this project as Dr Yu told us in Python variable, we can think of 'variables' as names
# and 'phone numbers' as string variables but we will use Dictionary
# ==========================
# Console Phone Book
# ==========================
import sys
import time

retry = 1;
phone_book = {}

def exitF():
    print("Exiting app after 3 seconds...");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    sys.exit("Goodbye!")




def retryF():
    retry = input(" Type 0 to exit | Type 1 to restart");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;


while (retry == 1):
    print("\n========== PHONE BOOK ==========")
    print("1. Show contacts")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Clear phone book")
    print("6. Exit")
    print("7. Search")

    choice = input("\nChoose an option: ")

    # =============
    # Show Contacts
    # =============
    if choice == "1":

        if len(phone_book) == 0:
            print("\nPhone book is empty.")

        else:
            print("\nContacts:")

            for name, phone in phone_book.items():
                print(f"{name} : {phone}")
        retryF();

    # =============
    # Add Contact
    # =============
    elif choice == "2":

        name = input("Name: ")
        phone = input("Phone Number: ")

        phone_book[name] = phone

        print("Contact added successfully.") ;
        retryF();

    # =============
    # Modify Contact
    # =============
    elif choice == "3":

        old_name = input("Enter existing contact name: ")

        if old_name in phone_book:

            print("\n1. Change name")
            print("2. Change phone number")

            option = input("Choose: ")

            if option == "1":

                new_name = input("New name: ")

                # Copy phone number
                phone_book[new_name] = phone_book[old_name]

                # Delete old name
                del phone_book[old_name]

                print("Name updated.")

            elif option == "2":

                new_phone = input("New phone number: ")

                phone_book[old_name] = new_phone

                print("Phone number updated.")

            else:
                print("Invalid option.")

        else:
            print("Contact not found.")
        retryF();

    # =============
    # Delete Contact
    # =============
    elif choice == "4":

        name = input("Enter contact name: ")

        if name in phone_book:

            del phone_book[name]

            print("Contact deleted.")

        else:
            print("Contact not found.")
        retryF();

    # =============
    # Clear Phone Book
    # =============
    elif choice == "5":

        phone_book.clear()

        print("Phone book cleared.")
        retryF();

    # =============
    # Exit
    # =============
    elif choice == "6":
        retryF();

    
    elif choice == "7":
    # ------------------------
    # Search Contact
    # ------------------------

        keyword = input("Enter contact name to search: ").strip()

        found = False

        for name, phone in phone_book.items():

            # Case-insensitive partial search
            if keyword.lower() in name.lower():

                print(f"\n{name} : {phone}")
                found = True

        if not found:
            print("No matching contacts found.")
        retryF();
    
    
    
    
    else:
        print("Invalid choice.")
        retryF();
    

"""
What else you can add to this script? 
If you have more ideas please share via Telegram at https://t.me/sasanace
1. Sort by (Alphabetic order, Date of modify, etc) ascending or descending
2. Saving contacts to a file using JSON
3. Partial name search
4. Validating phone numbers by string length & one step forward by 
comparing them to a benchamark database of existing numbers in a Telecoms database
5. Organizing code using functional & object oriented style of coding
"""
