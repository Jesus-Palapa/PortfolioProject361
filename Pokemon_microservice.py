# Name: Breanna Tran
# OSU Email: tranbre@oregonstate.edu
# Course: CS361- Software Engineering I
# Assignment 9
# Due Date: 7/31/2023

import socket
import pypokedex

port = 1800             # random port
host = '127.0.0.1'      # defined host
address = (host, port)

# Create the server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket
serverSocket.bind(address)

# Server listens for connections
serverSocket.listen(1)

# Establish connection with client
conn, addr = serverSocket.accept()  # Socket accepts request

while True:
    # Receive message from client
    try:
        input_name = conn.recv(1024).decode()

        if pypokedex.get(name=input_name):
            # Send message to the client
            conn.send('true'.encode())
    except:
        # Send message to the client indicating Pokemon not found in database
        conn.send('false'.encode())
        continue

    # Receive message from client
    message = conn.recv(1024).decode()

    if message == '1':
        response = 'Number: ' + str(pypokedex.get(name=input_name).dex) + '\n'
    elif message == '2':
        response = 'Types: '
        for i in range(0, len(pypokedex.get(name=input_name).types)):
            response = response + pypokedex.get(name=input_name).types[i] + '\n'
    elif message == '3':
        response = 'Weight: ' + str(pypokedex.get(name=input_name).weight) + ' hectograms' + '\n'
    elif message == '4':
        response = 'Height: ' + str(pypokedex.get(name=input_name).height) + ' decimeters' + '\n'
    elif message == '5':
        keys = list(pypokedex.get(name=input_name).moves.keys())
        moves_dict = pypokedex.get(name=input_name).moves
        response = ''

        for i in range(0, len(keys)):
            response = response + keys[i] + '\n'

            for j in range(0, len(moves_dict[keys[i]])):
                response = response + '   name: ' + str(moves_dict[keys[i]][j].name) + '\n      learn method: ' + \
                           str(moves_dict[keys[i]][j].learn_method) + '\n      level: ' + \
                           str(moves_dict[keys[i]][j].level) + '\n'

        print(response)
    else:
        response = 'Invalid option selected'

    # Send message to the client
    conn.send(str(response).encode())

# Close sockets
conn.close()   # Close new socket
serverSocket.close()    # Close serverSocket
