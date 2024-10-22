#!/usr/bin/env python3

# Dependencies
import os

# Refresh function
def refresh():
    os.system('cls') if os.name == 'nt' else os.system('clear')

# New invoice function
def new_invoice(invoices: dict, cost: str, owes: float) -> list[dict, float]:
    """New invoice function, returns new invoice if correct else return False if error"""
    if invoices == {}:
        n_invoice = 1
    else:
        last_invoice = int(list(invoices)[-1])
        n_invoice = last_invoice + 1

    try:
        cost = round(float(cost), 2)
        invoices[n_invoice] = cost

        owes += cost

        return (invoices, owes)
    except ValueError:
        return False

# Pay invoice function and returns the new invoices dict without the paid invoice
def pay_invoice(invoices: dict, n_invoice: str, owes: float, paid: float) -> list[dict, float, float]:
    """Pay invoice function and returns the new invoices dict without the paid invoice"""

    n_invoice = n_invoice.strip().replace(' ', '').replace('-', '').replace('(', '').replace(')', '').replace("'", '').replace('"', '')

    if invoices == {}:
        return {}
    else:
        try:
            n_invoice = int(n_invoice)

            current_paid = invoices.get(n_invoice)
            current_paid = float(current_paid)
            paid += current_paid
            owes -= current_paid

            invoices.pop(n_invoice)

            return (invoices, owes, paid)
        except:
            return False

# Handle each option introduced by user input, and handle it, exit it, or return False if option is not found
def options_handler(option: str, invoices: dict, owes: float, paid: float) -> any:
    """Handle each option introduced by user input, and handle it, exit it, or return False if option is not found"""

    option = option.strip().replace(' ', '').replace('[', '').replace(']', '')
    if option == "1":
        refresh()

        cost = input("What's the cost of the invoice? $")
        
        checked_invoice = new_invoice(invoices, cost, owes)
        if type(checked_invoice) == tuple:
            invoices = checked_invoice[0]    
            owes = checked_invoice[1]
            refresh()
            return (invoices, owes, paid)
        else:
            return -1

    elif option == "2":
        refresh()
        print("--------------------------")
        print("SELECT THE INVOICE TO PAY:")
        print("--------------------------")
        if invoices == {}:
            print("You don't have any invoices. Press [ENTER] to continue")
            input()
            refresh()
            return (invoices, owes, paid)
        else:
            for invoice in invoices:
                print(f"({invoice}) = ${invoices.get(invoice):.2f}")
            n_invoice = input("~> ")

            checked_invoice = pay_invoice(invoices, n_invoice, owes, paid)
            if type(checked_invoice) == tuple:
                invoices = checked_invoice[0]
                owes = checked_invoice[1]
                paid = checked_invoice[2]
                refresh()
                return (invoices, owes, paid)
            else:
                return -2

    elif option == "3":
        return False
    else:
        return -3

# Menu function to handle all user inputs and choices in the invoice manager
def menu(invoices: dict, owes: float, paid: float):
    """Menu function to handle all user inputs and choices in the invoice manager"""

    handle_option = True

    while handle_option:
        print("─────────────────────────────────")
        print("    DIEGO'S INVOICE MANAGER")
        print("─────────────────────────────────")
        print(f"- Paid so far: ${paid:.2f}")
        print(f"- You owe: ${owes:.2f}")
        print("─────────────────────────────────")
        print("\n[1] Add new invoice")
        print("[2] Pay existence invoice")
        print("[3] Exit\n")

        option = input("~> ")
        handle_option = options_handler(option, invoices, owes, paid)
        if type(handle_option) == tuple:
            invoices = handle_option[0]
            if invoices == {}:
                handle_option = {0}
                invoices = {}

            owes = handle_option[1]
            paid = handle_option[2]

        elif type(handle_option) == int:
            if handle_option == -1:
                print("\n[-] ERROR: You haven't introduced a correct cost for the invoice.\n")
                print("> Press [ENTER] to continue")
                input()
                refresh()
            elif handle_option == -2:
                print("\n[-] ERROR: You haven't introduced a correct invoice number.\n")
                print("> Press [ENTER] to continue")
                input()
                refresh()
            elif handle_option == -3:
                print("\n[-] ERROR: You haven't introduced a correct option!\n")
                print("> Press [ENTER] to continue")
                input()
                refresh()
            else:
                invoices = handle_option[0]
                owes = handle_option[1]
                paid = handle_option[2]
        else:
            exit()

# Main function
def main():

    refresh()

    invoices = {}
    owes = 0
    paid = 0
    
    menu(invoices, owes, paid)

# Program starts
if __name__ == '__main__':
    main()