#!/usr/bin/env python3

import os

# Convert price to the correct format and return False if got an ERROR
def check_price(price: str) -> float:
    """Convert price to the correct format and return False if got an ERROR"""
    try:
        price = round(float(price), 2)
        return price
    except ValueError:
        return False
    
# Check if user wants to exit the shop
def check_exit_shop(i: str) -> bool:
    i = i.strip().replace(' ', '').replace("'", "").replace('"', '').lower()
    if i == "exit":
        return True
    else:
        return False

# Shopping function
def shopping(cart: dict) -> dict:

    shop = False
    while not shop:

        article = input("\n[+] What's the article you want to add? ").capitalize()
        if check_exit_shop(article):
            shop = True
        else:
            price = False
            while not price:
                price = input(f"[+] What's the price of the {article}? ")
                if check_exit_shop(price):
                    shop = True
                    price = True
                else:
                    price = check_price(price)
                    if price:
                        cart[article] = price
                    else:
                        print("[-] ERROR: You haven't introduced a correct price!\n")
                        
    return cart

# Create ticket for the shopping cart
def ticket(cart: dict):
    total = 0
    for i in cart:
        print(f"- {i} = {cart[i]:.2f}€")
        total += cart[i]
        
    print("---------------------------------")
    print(f"Total: {total:.2f}€")
    print("---------------------------------")
    print("Thanks for your purchase!")
    print("69% COUPON CODE: 'DIEGOPONMEUN10'")
    print("---------------------------------")
    
# Main Function
def main():

    cart = {}
    os.system("cls") if os.name == "nt" else os.system("clear")
    print("─────────────────────────────────")
    print("   WELCOME TO THE DIEGO'S MALL")
    print("─────────────────────────────────")
    print("Introduce: 'EXIT' whenever you want to stop shopping")
    
    cart = shopping(cart)
    os.system("cls") if os.name == "nt" else os.system("clear")
    print("\n─────────────────────────────────")
    print("DIEGO'S MALL TICKET")
    print("─────────────────────────────────")
    if cart == {}:
        print("> Your cart is empty")
    else:
        print("> You have added the following items with prices to the cart:")
        ticket(cart)

# Start Program
if __name__ == '__main__':
    main()