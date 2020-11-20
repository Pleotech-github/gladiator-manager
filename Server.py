import io
import socket
import _thread
import sys

import Fighting
import Team

clients = 0
sockets = []


def broadcast(data):
    for s in sockets:
        s.send(str.encode(data))


teams = []
fights = []


def initiate(c):
    if c == 1:
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        Team1 = Team.Team("The House of Horror")
        Team1.printteam()
        teams.append(Team1)
        output = new_stdout.getvalue()
        sys.stdout = old_stdout
        broadcast(output)
        print(output)
    else:
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        Team2 = Team.Team("The Brotherhood")
        Team2.printteam()
        teams.append(Team2)
        output = new_stdout.getvalue()
        sys.stdout = old_stdout
        broadcast(output)
        print(output)
    if c == 2:
        fight = Fighting.Fighting()
        fights.append(fight)


def client(clientSckt, address):
    sockets.append(clientSckt)
    try:
        print('Client connected: ' + str(address))
        initiate(clients)
        while True:
            data = clientSckt.recv(1024)
            data = data.decode()
            if sockets[fights[0].turns(False)] == clientSckt:
                old_stdout = sys.stdout
                new_stdout = io.StringIO()
                sys.stdout = new_stdout
                fights[0].start_fight(teams[0], teams[1])
                output = new_stdout.getvalue()
                sys.stdout = old_stdout
                broadcast(output)
                print(output)
            if not data:
                break
        clientSckt.close()
    except:
        print('err')


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost', 5000)
print('Starting server')
serverSocket.bind(serverAddress)
serverSocket.listen(5) # Server listes for clients that tries to call to the server

while True:
    if clients <= 1:
        print('Waiting for client')
        clientSocket, clientAddress = serverSocket.accept()
        _thread.start_new_thread(client, (clientSocket, clientAddress)) # creates so more than one client can connect.
        clients = clients + 1 
