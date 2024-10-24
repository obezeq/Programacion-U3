#!/usr/bin/env python3

# Make invoice
def get_address_invoice(payments: tuple) -> tuple:
    invoices = []
    for client in payments:
        address = client[3]
        if address not in invoices:
            invoices.append(address)

    invoices = tuple(invoices)
    return invoices

# Main Funciton
def main():
    payments = [
        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), 
        ("Jorge Russo", 7, 699, "Mirasol 218"), 
        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), 
        ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
        ("Jorge Russo", 15, 958, "Mirasol 218")
    ]

    invoices = get_address_invoice(payments)
    print("The address of the clients where each invoice should be sent to:")
    for address in invoices:
        print(f"- {address}")

# Program starts
if __name__ == '__main__':
    main()