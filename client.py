import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Socket creation failed. Error code: " + str(msg[0]) + ", Message: " + msg[1])
    sys.exit()
print("Socket created")

host, port = sys.argv[1], int(sys.argv[2])

s.connect((host, port))
print("Successfully connected")
request = 'GET ' + sys.argv[3] + ' HTTP/1.1'
s.sendto((request.encode()), (sys.argv[1], int(sys.argv[2])))
response = s.recv(8192).decode()
print(response)
print("Terminating connection")
s.close()
