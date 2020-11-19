import socket
import sys
import time
import _thread


def listener(sc):
    while True:
        data = clientSocket.recv(1024)
        print(data.decode('utf-8'))


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost', 5000)
print('Connecting to server')
clientSocket.connect(serverAddress)
_thread.start_new_thread(listener, (clientSocket,))


while True:
    try:
        message = input()
        if message == '':
            message = ' '
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