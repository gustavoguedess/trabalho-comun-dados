import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)

sock.bind(server_address)


# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    connection, client_address = sock.accept()

#%%
import socket

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(('www.python.org', 80))

def servidor():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), 1234))
    serversocket.listen(5)
servidor()