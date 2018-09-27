import socket
import threading

HOST = '192.168.122.1'                 # Symbolic name meaning all available interfaces
PORT = 6000             # Arbitrary non-privileged port
def send(sock,addr):
    i_say =''
    while i_say != 'bye':
        i_say = input('i say:')
        sock.sendto(i_say.encode('utf8'),addr)

def recv(sock):
    while True:
        other_say,addr = sock.recvfrom(1024)
        print('{} say >> {}'.format(addr[0],other_say.decode('utf8')))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    ipaddr = input('ip youwantsay')
    addr = (ipaddr,50000)
    t1 = threading.Thread(target = send,args = (s,addr))
    t1.setDaemon(True)
    t1.start()
    t2 = threading.Thread(target = recv,args=(s,))
    t2.setDaemon(True)
    t2.start()

    t1.join()
    t2.join()

