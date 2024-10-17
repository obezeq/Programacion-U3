#!/usr/bin/env python3

prices = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

# Calc prices of a fruit
def calc_price(fruit, kg):
    price = prices[fruit] * kg
    return price

def user_input():
    try:
        fruit = input("[+] Choose a fruit: ").capitalize()
        if prices.get(fruit) == None:
            return NameError

        kg = float(input("[+] Introduce the kg amount of your fruit: ").strip().replace(' ', ''))
        
        order = [fruit, kg]
        return order
        
    except ValueError:
        return ValueError
    
    except Exception as e:
        return e

def main():
    order = user_input()
    exit()
    if order:
        fruit = order[0]
        kg = order[1]

        price = calc_price(fruit, kg)

        print(f"The price of {kg} kg of {fruit} is {price}€")

    elif order == ValueError:
        print("[-] ERROR: You haven't introduced a correct amount of kg.")

    elif order == NameError:
        print("[-] ERROR: You haven't introduced an available fruit in the stock. We only have the following stock available: ")

# Main Function
if __name__ == '__main__':
    main()