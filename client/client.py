import sys
import requests

if __name__ == '__main__':

    while True: 
        
        print("-- ATM actions --")
        print("Select an action")
        print("1) login")
        print("2) logout")
        print("3) listsold")
        print("4) getmoney")
        print("5) putmoney")
        print("6) unlock")
        print("7) exit\n")
        selection = raw_input("Your selection is: ")
        print("")
        
        if selection == '1':
            print("Please provide: card number and pin. Use enter as a delimiter.")
            card_number = raw_input('Card number: ')
            pin = raw_input('Pin: ')

            print()
        elif selection == '2':
            print("Successfully disconnected from the ATM!")

            print()
        elif selection == '3':
            print()

        elif selection == '4':
            print("Please introduce the amount you want to withdraw.")
            amount = raw_input('Amount: ')

            print()
        elif selection == '5':
            print("Please introduce the amount you want to deposit.")
            amount = raw_input('Amount: ')

            print()
        elif selection == '6':
            print("Please introduce card number and secret password.")
            card_number = raw_input('Card number: ')
            secret_password = raw_input('Secret password: ')

            print()
        elif selection == '7':
            print("Thank you for your time.")
            break            

        else:
            print("Invalid option. Please select one valid option.\n")