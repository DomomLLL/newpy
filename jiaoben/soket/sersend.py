import socket

HOST = '172.25.11.192'    # The remote host
PORT = 5000     # The same port as used by the server
path = 'ser.py'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(path.encode('utf-8'))
    data = s.recv(1024)
print('Received', repr(data))

with open(path) as f:
    r = f.readlines()
for i in r:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(i.encode('utf-8'))
        data = s.recv(1024)
    print('Received', repr(data))
