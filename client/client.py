import sys
import requests

if __name__ == '__main__':


    server_ip = sys.argv[1]
    global_card_number = ""


    while True: 

        print("-- ATM actions --")
        print("Select an action")
        print("1) login")
        print("2) logout")
        print("3) listsold")
        print("4) withdrawmoney")
        print("5) depositmoney")
        print("6) unlock\n")
        selection = raw_input("Your selection is: ")
        print("")
        
        if selection == "1":
            print("Please provide: card number and pin. Use enter as a delimiter.")
            card_number = raw_input("Card number: ")
            global_card_number = card_number
            pin = raw_input("Pin: ")

            request_link = "http://" + server_ip  + ":5000/login?cardnumber=" + card_number + "&pin=" + pin
            response = requests.get(request_link)
            print(response.content)

            print("")

        elif selection == "2":
            print("Successfully disconnected from the ATM!")
            request_link = "http://" + server_ip  + ":5000/logout?cardnumber=" + global_card_number
            response = requests.get(request_link)
            print(response.content)

            print("")
        
        elif selection == "3":
            request_link = "http://" + server_ip  + ":5000/listsold?cardnumber=" + global_card_number
            response = requests.get(request_link)
            print(response.content)

            print("")

        elif selection == "4":
            print("Please introduce the amount you want to withdraw.")
            amount = raw_input("Amount: ")

            request_link = "http://" + server_ip  + ":5000/withdrawmoney?cardnumber=" + global_card_number + "&amount=" + amount
            response = requests.get(request_link)
            print(response.content) 

            print("")

        elif selection == '5':
            print("Please introduce the amount you want to deposit.")
            amount = raw_input("Amount: ")
            request_link = "http://" + server_ip  + ":5000/depositmoney?cardnumber=" + global_card_number + "&amount=" + amount
            response = requests.get(request_link)
            print(response.content)

            print("")
        
        elif selection == '6':
            print("Please introduce card number and secret password.")
            card_number = raw_input("Card number: ")
            secret_password = raw_input("Secret password: ")

            request_link = "http://" + server_ip  + ":5000/unlock?cardnumber=" + card_number + "&secretpassword=" + secret_password
            response = requests.get(request_link)
            print(response.content)

            print("")

        else:
            print("Invalid option. Please select one valid option.\n")