import time
import socket
import queue
import threading
import subprocess

q = queue.Queue()
l=[]

def geip():
    for i in range(255):
        ip1 = '172.25.'+'%d'%i
        for j in range(254):
            ip2 = ip1 + '.%d'%j
            ping_ip = 'ping -c 1 ' + ip2
            q.put(ping_ip)
def getip():
    while True:
        ip = q.get()
        if subprocess.call(ip,shell = True)==0:
            l.append(ip)
        else:
            print('%s is unconnection'%ip)
        q.task_done()
qq= geip()

for x in range(100):
    
    x = threading.Thread(target = getip)
    x.setDaemon(True)
    x.start()

q.join()
print(l)
