#!/usr/bin/env python3

# Convert price to the correct format and return False if got an ERROR
def check_price(price: str) -> (float | bool):
    try:
        price = round(float(price), 2)
        return price
    except ValueError:
        return False
    
# Function to check if user wants to exit the shop
def check_exit_shop(i: str) -> bool:
    i = i.strip().replace(' ', '').replace("'", "").lower()
    if i == "exit":
        return True
    else:
        return False

# Shopping function
def shopping(cart: dict) -> dict:

    shop = False
    while not shop:

        article = input("[+] What's the article you want to add? ")
        if check_exit_shop(article):
            shop = True
        else:
            price = False
            while not price:
                price = check_price(input(f"[+] What's the price of the {article}? "))
                if price == False:
                    print("[-] ERROR: You haven't introduced a correct price!\n")
                else:
                    cart[article] = price

# Main Function
def main():

    cart = {}
    
    print("────────────────────────────")
    print("WELCOME TO THE DIEGO'S MALL")
    print("────────────────────────────")
    print("Introduce: 'EXIT' whenever you want to stop shopping")
    
    cart = shopping(cart)

# Start Program
if __name__ == '__main__':
    main()