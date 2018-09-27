
import socket

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 60017            # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    s.sendto(b'bnm,',(HOST,50017))
    data, addr = s.recvfrom(1024)
    print(b'data',data)
    print(b'addr',addr)
    s.close()
