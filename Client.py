import socket


class Client:
    server_socket = socket.socket()
    host = socket.gethostbyname("localhost")
    port = 12345

    server_socket.connect((host, port))
    print(server_socket.recv(1024))
    server_socket.close()
