import socket
import subprocess
from threading import Thread,Event
import queue
import time
class Send(Thread):
    def __init__(self,s,getvalues,name):
        Thread.__init__(self)
        self.s = s
        self.getvalues = getvalues
        self.name = name

    def run(self):
        self.s.bind(('',5000))
        self.s.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl_bin)
        status = s.setsockopt(IPPROTO_IP,
                              IP_ADD_MEMBERSHIP,
                              inet_aton(MYGROUP) + inet_aton(SENDERIP))
        while True:
            ntime =  time.ctime()
            s.sendto(ntime + '' + self.name + 'say: '+self.getvalues,
                     ('224.1.1.1',5000))
            

            
        
   
            
    
    
  

    
