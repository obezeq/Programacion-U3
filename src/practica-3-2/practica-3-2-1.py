#!/usr/bin/env python3

# Currencies dict
currencies = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}

# Function to get the symbol of the selected currency
def get_symbol_currency(currency):
    try:
        symbol = currencies[currency]
        print(f"The currency of {currency} is {symbol}.")
    except:
        print("Your currency is not available.")

def main():
    currency = input("[+] Select the name of a currency: ").strip().replace(' ', '').title()
    get_symbol_currency(currency)

# Main Function
if __name__ == '__main__':
    main()