import socket
import sys
import time

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost', 5000)
print('Connecting to server')

clientSocket.connect(serverAddress)

while True:
    try:
        message = input()
        if message == 'exit':
            print('Connection terminated')
            print('Closing window')
            clientSocket.close()
            time.sleep(2)
            sys.exit()
        else:
            clientSocket.send(str.encode(message))
    except:
        print('Error')
        sys.exit()