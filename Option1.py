import pypokedex
import socket

def option1():
    """Function sets up socket to send info to by connection. User will enter name and returns data"""
    port = 1800
    host = '127.0.0.1'
    address = (host, port)

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(address)
    while True:
        poke_name = (input("Enter POKEMON NAME you want to search for or enter 0 to exit: "))
        poke_name = str(poke_name)
        clientSocket.send(poke_name.encode())
        verified_name = clientSocket.recv(1024).decode()
        if verified_name == 'true':
            print("\nPokeFax Sheet")
            print("-------------------------")
            print("Enter 1 to get pokemon number.")
            print("Enter 2 to get pokemon type.")
            print("Enter 3 to get pokemon weight.")
            print("Enter 4 to get pokemon height.")
            print("Enter 5 to get pokemon moves.")
            data_choice = input("Enter your choice here: ")
            clientSocket.send(data_choice.encode())
            print(clientSocket.recv(1024).decode())
        elif verified_name == '0':
            break
        else:
            print("\nError! Pokemon does not exist. Try checking your spelling.\n")
            break

    clientSocket.close()