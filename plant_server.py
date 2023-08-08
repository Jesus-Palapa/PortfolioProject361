# Name: Jesus Palapa
# OSU Email: palapcj@oregonstate.edu
# Course: CS361- Software Engineering I

import socket
import random
from urllib.request import urlopen
import json

url = "https://perenual.com/api/species-list?key=sk-rwOm64d0581d8e9511720&page=1"

response = urlopen(url)
raw_data = response.read()
data = json.loads(raw_data)

port = 3000
host =  '127.0.0.1'
address = (host, port)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(address)

serverSocket.listen(5)

conn, addr = serverSocket.accept()

while True:
    # first message received
    input_msg = conn.recv(1024).decode()
    input_msg = str(input_msg)
    # always creates a plant list at every call; avoids errors in search later on
    plant_list = []
    for x in range(len(data['data'])):
        plant_list.append(data["data"][x]["common_name"].lower())
    # saves plant matched, for use when data returned
    save_plant = None
    message = 'false'
    # receive list from user, send back list created
    if input_msg == 'list':
        plant_list = str(plant_list)
        plant_list = plant_list.encode()
        conn.send(plant_list)
        continue
    # receive random from user, return random plant name
    elif input_msg == 'random':
        plant_random = random.randint(0, 29)
        new_plant = plant_list[plant_random]
        conn.send(new_plant.encode())
        continue
    # receive exit from user, terminates socket
    elif input_msg == 'exit':
        break
    # receive a common name from user, iterate through list, save location if found, return true to confirm plant name valid
    else:
        for x in range(0,30):
            plant_found = plant_list[x]
            if plant_found == input_msg.lower():
                save_plant = x
                message = 'true'
                break
        conn.send(message.encode())
        # restarts loop if plant not found in database
        if message == 'false':
            continue
        message = conn.recv(1024).decode()
        # continues to second message received, returns appropriate data
        if message == '1':
            response = data["data"][save_plant]["scientific_name"]
        elif message == '2':
            response = data["data"][save_plant]["watering"]
        elif message == '3':
            response = data["data"][save_plant]["sunlight"]
        elif message == '4':
            response = data["data"][save_plant]["cycle"]
        response = str(response)
        response = response.encode()
        conn.send(response)

conn.send(input_msg.encode())
conn.close()
serverSocket.close()
