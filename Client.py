import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost', 5000)
print('Connecting to server')

clientSocket.connect(serverAddress)

try:
    message = input()
    message = message.encode()
    clientSocket.send(message)
finally:
    clientSocket.close()