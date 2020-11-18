import socket
import threading

text_bytes = 8  # Number of bytes
unicode = 'UTF-8'
port = 12345
ip_server = socket.gethostbyname(socket.gethostname())# Gets the information about client pc
adr_location = (ip_server, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # connects to the internet through TCP socket(SOCK_STREAM)


def client_operation(connect, adr):  # connects link between clients and server
    print(f"New connection {adr} joined")

    linked = True
    while linked:
        linked_text_length = connect.recv(text_bytes).decode(
            unicode)  # the amount of bytes that are being send to the client
    if linked_text_length:
        linked_text_length = int(linked_text_length)
        message = connect.recv(linked_text_length).decode(unicode)
        print(f"({adr}) {message}")
        # maybe add disconnection option?
        connect.close()


def client_running():  # Handling of connections to the server
    server.listen() #server listening for connections
    while True:
        connect, adr = server.accept()  # This will store the address from where it came from while store it as a object
        thread = threading.Thread(target=client_operation(), args=(connect, adr)) # allowing for more clients
        thread.start()
        print(f"Number of connected {threading.active_count() - 1}") # checks for number of clients connected to server

print("Server connection found")

"""
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
"""
