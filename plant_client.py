# Name: Jesus Palapa
# OSU Email: palapcj@oregonstate.edu
# Course: CS361- Software Engineering I

import socket

port = 3000
host =  '127.0.0.1'
address = (host, port)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(address)

while True:
    user_input = input("Enter {list, random, name, exit}:")
    clientSocket.send(user_input.encode())
    response = clientSocket.recv(1024).decode()

    if response == 'false':
        print("Plant not in database")
    elif response == 'true':
        print("What plant info would you like to see?")
        print("1. Scientific Name")
        print("2. Watering")
        print("3. Sunlight")
        print("4. Cycle")
        user_input = input("Enter Option: ")
        user_input = str(user_input)
        clientSocket.send(user_input.encode())
        print(clientSocket.recv(1024).decode())
    else:
        if response == 'exit':
            break
        print(response)



clientSocket.close()