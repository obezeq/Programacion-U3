#!/usr/bin/env python3

# Save person in JSON dict
def save_person(name: str, age: int, address: str, phone: str) -> dict[str, int, str, str]:
    """Save person in JSON dict"""
    person = {
        "name": name,
        "age": age,
        "address": address,
        "phone": phone
    }

    return person

# Function to ask user details and check input
def save_user_input():
    """Function to ask user details and check input"""

    # Ask Name
    name = input("What's your name? > ").title()

    # Ask & Check Age    
    try:
        age = int(input("How old are you? > "))
    except ValueError:
        print("[-] ERROR: You haven't introduced your age!")

    # Ask Address
    address = input("What's your address? > ")

    # Ask Phone Number
    phone = input("What's your phone number? > ")

    return name, age, address, phone

def main():

    # Function to ask user details and check input
    name, age, address, phone = save_user_input()

    # Save person in JSON dict
    person = save_person(name, age, address, phone)

    print(f"{person["name"]} has {person["age"]} years, and lives in {person["address"]} y su número de teléfono es {person["phone"]}.")

# Main Function
if __name__ == '__main__':
    main()