import socket


class Server:
    server_socket = socket.socket()
    host = socket.gethostbyname("localhost")
    port = 12345

    server_socket.bind((host, port))
    server_socket.listen(5)
    while True:
        client, addr = server_socket.accept()
        print("Got connection from " + str(addr))
        client.send("Thank you for connecting".encode())
        client.close()

