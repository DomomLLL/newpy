import socket
def check():
    s_check = socket.socket()
    for i in range(255):
        c_ip = '172.25.'+'%d'%i
        for j in range(254):
            fip = c_ip +'.%d'%j
            try:
                s_check.connect((c_ip, 60008))
                print(c_ip)
                        
            except socket.error:
                print('dasdas')
a  =check()
