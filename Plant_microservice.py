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
plant_list = []
for x in range(len(data['data'])):
    plant_list.append(data["data"][x]["common_name"].lower())

port = 1800
host = '127.0.0.1'
address = (host, port)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(address)

serverSocket.listen(5)

conn, addr = serverSocket.accept()

while True:
    input_msg = conn.recv(1024).decode()
    input_msg = str(input_msg)
    plant_index = None
    message = 'false'
    # receive list from user
    if input_msg == 'list':
        list = ''
        for x in range(len(plant_list)):
            list = list + plant_list[x] + '\n'
        list = list.encode()
        conn.send(list)
        continue
    elif input_msg == 'exit':
        break
    # receive a name
    else:
        # receive random from user (issue cannot do random search after list)
        if input_msg == 'random':
            plant_index = random.randint(0, 29)
            new_plant = plant_list[plant_index]
            conn.send(new_plant.encode())

        else:
            for x in range(0, 30):
                if plant_list[x] == input_msg.lower():
                    plant_index = x
                    message = 'true'
                    conn.send(message.encode())
                    break

            if message == 'false':
                conn.send(message.encode())
                continue

        while True:
            message = conn.recv(1024).decode()

            if message == 'new':
                break
            elif message == '1':
                response = data["data"][plant_index]["scientific_name"][0]
            elif message == '2':
                response = data["data"][plant_index]["cycle"]
            elif message == '3':
                response = data["data"][plant_index]["watering"]
            elif message == '4':
                response = data["data"][plant_index]["sunlight"]
            response = str(response)
            response = response.encode()
            conn.send(response)

conn.send(input_msg.encode())
conn.close()
serverSocket.close()
