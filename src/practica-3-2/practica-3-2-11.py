#!/usr/bin/env python3

def transform_data(clients_data:str) -> dict:
    clients = clients_data.split("\n")
    data = {}
    counter = 0
    for client in clients:
        client = client.split(";")

        if counter == 0:
            index = client
        else:
            nif = client[0]

            data[nif] = {
                index[1]: client[1],
                index[2]: client[2],
                index[3]: client[3],
                index[4]: float(client[4])
            }

        counter += 1

    return data

# Main Function
def main():
    clients_data = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    data = transform_data(clients_data)
    print(data)
    

# Program starts
if __name__ == '__main__':
    main()