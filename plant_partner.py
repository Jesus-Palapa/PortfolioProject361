import socket
from urllib.request import urlopen
import json

url = "https://perenual.com/api/species-list?key=sk-yL9564c874f236cf61720&page=1"

response = urlopen(url)

data = json.loads(response.read())


port = 1800
host =  '127.0.0.1'
address = (host, port)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(address)

serverSocket.listen(1)

conn, addr = serverSocket.accept()

while True:
    input_name = conn.recv(1024).decode()
    save_plant = None
    message = 'false'
    for x in data["data"]:
        if x["common_name"].lower() == input_name.lower() or x["scientific_name"].lower() == input_name.lower():
            save_plant = x
            message = 'true'
            break

    conn.send(message.encode())

    if message == 'false':
        continue

    message = conn.recv(1024).decode()

    if message == '1':
        response = data["data"][save_plant]["scientific_name"]
    elif message == '2':
        response = data["data"][save_plant]["watering"]
    elif message == '3':
        response = data["data"][save_plant]["sunlight"]
    elif message == '4':
        response = data["data"][save_plant]["cycle"]

    # for i in range(len(data["data"])):
    #     if data["data"][i]["common_name"] == message.lower():
    #         plant_info = f'Scientific Name: {data["data"][i]["scientific_name"]}\nWatering: {data["data"][i]["watering"]}\nSunlight: {data["data"][i]["sunlight"]}\nCycle: {data["data"][i]["cycle"]}\n'
    #         response = plant_info
    #     else:
    #         response = "Plant may not be in database. Check for spelling!"


    # Send message to the client
    conn.send(str(response).encode())

# Close sockets
conn.close()  # Close new socket
serverSocket.close()  # Close serverSocket
