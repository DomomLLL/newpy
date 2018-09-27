'''import socket
class Recv():
    def __init__(self):
       
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self):
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.s.bind(('',5000))
        while True:
            data, address = s.recvfrom(65535)
            print(data)
s = Recv()
'''
# udp_gb_server.py
'''服务端（UDP协议局域网广播）'''
# udp_gb_client.py
'''客户端（UDP协议局域网广播）'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 1060

s.bind(('', PORT))
print('Listening for broadcast at ', s.getsockname())

while True:
    data, address = s.recvfrom(65535)
    print('Server received from {}:{}'.format(address, data.decode('utf-8')))
