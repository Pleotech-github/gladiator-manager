import socket
import sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost',5000)
print('Starting server')
serverSocket.bind(serverAddress)
serverSocket.listen(1)

while True:
    print('Waiting for client')
    connection, clientAddress = serverSocket.accept()

    try:
        print('Client connected: ' + str(clientAddress))
        while True:
            data = connection.recv(16)
            data = data.decode()
            print(data)
    finally:
        connection.close()