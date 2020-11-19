import socket
import _thread


def client(clientSckt, address):
    try:
        print('Client connected: ' + str(address))
        while True:
            data = clientSckt.recv(16)
            data = data.decode()
            print(data)
            if not data:
                break
        clientSckt.close()
    except:
        print('Error')

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost',5000)
print('Starting server')
serverSocket.bind(serverAddress)
serverSocket.listen(5)

while True:
    print('Waiting for client')
    clientSocket, clientAddress = serverSocket.accept()
    _thread.start_new_thread(client, (clientSocket, clientAddress))
