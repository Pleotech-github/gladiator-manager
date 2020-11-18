import socket

text_bytes = 8
unicode = 'UTF-8'
port = 5050
server = socket.gethostbyname(socket.gethostname())  # place your own Ip adress here. can be found in cmd ipconfig or -
# print
adr_location = (server, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(adr_location)

"""
class Client:
    server_socket = socket.socket()
    host = socket.gethostbyname("localhost")
    port = 12345

    server_socket.connect((host, port))
    print(server_socket.recv(1024))
    server_socket.close()
"""
