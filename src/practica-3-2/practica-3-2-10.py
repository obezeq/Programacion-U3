#!/usr/bin/env python

# Dependencies
import os

# ───────────────────────────────────────────────────────────────────────────────────────────────────
#GENERAL FUNCTIONS

# Refresh Function
def refresh():
    os.system('cls') if os.name == 'nt' else os.system('clear')

# ───────────────────────────────────────────────────────────────────────────────────────────────────
# DIEGO'S BUSINESS MANAGER FUNCTIONS

# Add Client
def add_client(clients: dict, checked_data: dict) -> dict:
    try:
        nif = checked_data[0]
        if checked_data[5]:
            preferred = "Yes"
        else:
            preferred = "No"
        clients[nif] = {
            "name": checked_data[1],
            "address": checked_data[2],
            "phone": checked_data[3],
            "email": checked_data[4],
            "preferred": preferred
        }

        input(f"\nClient {nif} Added successfully. Press [ENTER] to continue")

        return clients
    
    except Exception as e:
        print(f"\n[-] UNEXPECTED ERROR (Closing program):\n{e}\n")
        exit()

def remove_client(clients: dict, checked_nif: dict) -> dict:
    try:
        clients.pop(checked_nif)

        input(f"\nClient {checked_nif} Added successfully. Press [ENTER] to continue")

        return clients
    
    except Exception as e:
        print(f"\n[-] UNEXPECTED ERROR (Closing program):\n{e}\n")
        exit()

def show_client(clients: dict, nif: dict):
    try:
        client = clients[nif]
    except:
        print(f"\n[-] Client {nif} not found.\n")
        input("> Press [ENTER] to continue.")
    else:
        try:
            print("─────────────────────────────────")
            print(f"    CLIENT {nif} DATA")
            print("─────────────────────────────────")
            print(f"- NIF: {nif}")
            print(f"- Name: {client["name"]}")
            print(f"- Address: {client["address"]}")
            print(f"- Phone Number: {client["phone"]}")
            print(f"- Email: {client["email"]}")
            print(f"- Preferred: {client["preferred"]}\n")
        except Exception as e:
            print(f"\n[-] UNEXPECTED ERROR (Closing program):\n{e}\n")
            exit()


def show_clients(clients: dict):
    try:
        refresh()
        print("┌─────────────────────────────────┐")
        print("│      CLIENTS' INFORMATION       │")
        print("└─────────────────────────────────┘\n")

        for client in clients:
            show_client(clients, client)
        
        input("\n > PRESS [ENTER] to continue.")

    except Exception as e:
        print(f"\n[-] UNEXPECTED ERROR (Closing program):\n{e}\n")
        exit()

def show_preferred_clients(clients: dict):
    try:
        refresh()
        print("┌──────────────────────────────────┐")
        print("│  PREFERRED CLIENTS' INFORMATION  │")
        print("└──────────────────────────────────┘\n")

        for client in clients:
            preferred = clients[client]["preferred"]
            if preferred == "Yes":
                refresh()
                show_client(clients, client)

        input("\n > PRESS [ENTER] to continue.")

    except Exception as e:
        print(f"\n[-] UNEXPECTED ERROR (Closing program):\n{e}\n")
        exit()

# ───────────────────────────────────────────────────────────────────────────────────────────────────
# MENU FUNCTIONS

# Check Add Client
def check_add_client(nif: str, name: str, address: str, phone: str, email: str, preferred: str) -> (dict | list):

    # Check & Format NIF
    checked_nif = check_nif(nif)
    if checked_nif:
        nif = checked_nif
    else:
        return[False, "NIF"]

    # Format NAME
    name = name.title()

    # Check Phone
    phone = phone.replace(' ', '')
    if len(phone) < 3 or len(phone) > 20:
        return [False, "Phone Number"]

    # Check Email
    if email.find(' ') != -1 or email.find('@') == -1 or email.split('@')[1].find('.') == -1:
        return [False, "Email"]
    
    # Check & Format Preferred
    preferred = preferred.replace(' ', '').lower()
    if preferred == 'y' or preferred == 'yes' or preferred == 's' or preferred == 'si':
        preferred = True
    elif preferred == 'n' or preferred == 'no':
        preferred = False
    else:
        return [False, "Preferred"]

    return (nif, name, address, phone, email, preferred)

# Check NIF Data
def check_nif(nif: str) -> (dict | bool):

    if len(nif) == 9 or len(nif) == 10:
        nif = nif.upper()
        return nif
    else:
        return False

# Menu Handler
def menu_handler(clients: dict, option: int):
    """Menu handler function:
    (1) Check each menu option
    (2) Check/format user input for each. 
    (3) If everything is okay: STARTS OPTION FUNCTION. Else: it asks to introduce the details again.
    """
    
    bad_format = True
    while bad_format:
        refresh()

        # ADD CLIENT OPTION
        if option == 1:
            print("─────────────────────────────────")
            print("           ADD CLIENT")
            print("─────────────────────────────────")
            nif = input("[+] Client's NIF: ").strip()
            name = input("[+] Client's Name: ").strip()
            address = input("[+] Client's Address: ").strip()
            phone = input("[+] Client's Phone: ").strip()
            email = input("[+] Client's Email: ").strip()
            preferred = input("[+] Preferred? (Y/n): ").strip()

            checked_data = check_add_client(nif, name, address, phone, email, preferred)

            if checked_data[0] == False:
                where_error = checked_data[1]
                checked_data = checked_data[0]
                print(f"\n[-] ERROR: You haven't introduced the correct format in {where_error}")
                input("> Press [ENTER] to try again.")
            else:
                bad_format = False
                clients = add_client(clients, checked_data)

        # REMOVE CLIENT OPTION
        elif option == 2:
            print("─────────────────────────────────")
            print("           REMOVE CLIENT")
            print("─────────────────────────────────")
            nif = input("[+] Client's NIF: ").strip()
            checked_nif = check_nif(nif)
            if checked_nif:
                bad_format = False
                clients = remove_client(clients, checked_nif)
            else:
                print("[-] ERROR: You have introduced an incorrect NIF format.")
                input("> Press [ENTER] to try again.")

        elif option == 3:
            print("─────────────────────────────────")
            print("           SHOW CLIENT")
            print("─────────────────────────────────")
            nif = input("[+] Client's NIF: ").strip()
            checked_nif = check_nif(nif)
            if checked_nif:
                bad_format = False
                show_client(clients, checked_nif)
                input("> Press [ENTER] to continue.")
            else:
                print("[-] ERROR: You have introduced an incorrect NIF format.")
                input("> Press [ENTER] to try again.")

        elif option == 4:
            bad_format = False
            show_clients(clients)

        elif option == 5:
            bad_format = False
            show_preferred_clients(clients)

        elif option == 6:
            bad_format = False
            return False

    return clients


# Check Menu Option
def check_menu(option: str) -> (int | bool):
    option = option.strip().replace(' ', '').lower()

    if option == "one" or option == "addclient" or option == "1":
        return 1
    elif option == "two" or option == "deleteclient" or option == "2":
        return 2
    elif option == "three" or option == "showclient" or option == "3":
        return 3
    elif option == "four" or option == "listallclients" or option == "4":
        return 4
    elif option == "five" or option == "listpreferredclients" or option == "5":
        return 5
    elif option == "zero" or option == "exit" or option == "0":
        return -1
    else:
        return False

# Menu Page
def menu(clients: dict):
    option = True
    while option:
        refresh()
        print("─────────────────────────────────")
        print("    DIEGO'S BUSINESS MANAGER")
        print("─────────────────────────────────")
        print("[0] EXIT")
        print("[1] Add client")
        print("[2] Delete client")
        print("[3] Show client")
        print("[4] List all clients")
        print("[5] List preferred clients")
        print("─────────────────────────────────")
        option = input("~> ")
        option = check_menu(option)
        if option == -1:
            option = False
        elif option > 0:
            clients = menu_handler(clients, option)
            if clients == -1:
                option = False
        else:
            option = True
            print("\n[-] ERROR: You have introduced an incorrect option.")
            input("> Press [ENTER] to try again")

# ───────────────────────────────────────────────────────────────────────────────────────────────────

# Main function
def main():
    clients = {}
    menu(clients)

# Program starts
if __name__ == '__main__':
    main()