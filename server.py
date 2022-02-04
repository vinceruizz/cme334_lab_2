import socket
import sys
import os

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Socket created")

host, port = 'localhost', 1234

try:
    serverSocket.bind((host,port))
except socket.error as msg:
    print("Binding failed. Error code: " + str(msg[0]) + ", Message: " + msg[1])
    sys.exit()
print("Binding complete")

serverSocket.listen(5)
print("Socket listening.")

while (True):
    clientSocket, addr = serverSocket.accept()
    print("Connection with " + addr[0] + " established")
    data = str(clientSocket.recv(8192).decode())

    # sort the request string into a dictionary of header and body
    request = data.replace('\r', '').split('\n')
    request_head = request[0]

    request_path = request_head.split(' ')[1]

    if os.path.isfile(request_path):
        file = open(request_path, 'r')
        response = 'HTTP/1.1 200 OK\n\n' + file.read()
        clientSocket.sendall(response.encode())

    else:
        response = 'HTTP/1.1 404 NOT FOUND\n\n' + '<html><body><h1>404 Not Found</h1></body></html>'
        clientSocket.sendall(response.encode())

    clientSocket.close()
