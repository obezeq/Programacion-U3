#!/usr/bin/env python3

prices = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

# Calc prices of a fruit
def calc_price(fruit: str, kg: float) -> float:
    price = round((prices[fruit] * kg), 2)
    return price

# Check user input
def user_input():
    try:
        fruit = input("[+] Choose a fruit: ").capitalize()
        if prices.get(fruit) == None:
            name_error = "[-] ERROR: You haven't introduced an available fruit in the stock. We only have the following stock available:"
            for p in prices:
                name_error += f"\n- {p}"
            raise NameError(name_error)

        kg = float(input("[+] Introduce the kg amount of your fruit: ").strip().replace(' ', ''))
        
        order = [fruit, kg]
        return order

    except ValueError:
        return ValueError("[-] ERROR: You haven't introduced a correct amount of kg.")

    except Exception as e:
        return e

def main():
    order = user_input()

    if type(order) == list:
        fruit = order[0]
        kg = order[1]
        price = calc_price(fruit, kg)
        
        print(f"The price of {kg} kg of {fruit} is {price}€")

    else:
        print(order)
            

# Main Function
if __name__ == '__main__':
    main()