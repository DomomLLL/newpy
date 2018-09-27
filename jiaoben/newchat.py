import wx
import time
import socket
import queue
import threading
import subprocess


class Myapp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,
                         title = 'my chat',
                         size = (520, 450))
        panel = wx.Panel(frame, -1)
        label_All = wx.StaticText(panel,-1,'chat record',pos=(230,0))
        label_All = wx.StaticText(panel,-1,'IP',pos=(40,0))
        self.textAll = wx.TextCtrl(panel, -1, style = wx.TE_MULTILINE,size = (420,210),
                                   pos=(100,20))
        label_Say = wx.StaticText(panel,-1,'chat',pos = (240,230))  
        self.textSay = wx.TextCtrl(panel, -1,style = wx.TE_MULTILINE,
                                   size =(420,120),
                                   pos=(100,250))
        self.textIP = wx.TextCtrl(panel, -1,style = wx.TE_MULTILINE,size = (100,430),
                                  pos=(0,20))
        self.button_sent = wx.Button(panel, -1 , 'send',pos=(234,370),size=(133,-1))
        self.button_sent = wx.Button(panel, -1 , 'close',pos=(100,370),size=(133,-1))
        self.button_clear = wx.Button(panel, -1 , 'clear',pos=(370,370),size=(133,-1))
        self.Bind(wx.EVT_BUTTON, self.onSent, self.button_sent)
        self.Bind(wx.EVT_BUTTON, self.onClear, self.button_clear)

        
        frame.Show()
        return True
    def onSent(self, event):
        userinput = self.textSay.GetValue()
        self.textSay.Clear()
        inmsg = '{} youSay:{}\n'.format(time.ctime(),userinput)
        self.textAll.AppendText(inmsg)

    def onClear(self, event):
        self.textAll.Clear()

q = queue.Queue()
l=[]

def geip():
    for i in range(25):
        ip1 = '172.25.'+'%d'%i
        for j in range(254):
            ip2 = ip1 + '.%d'%j
            ping_ip = 'ping  ' + ip2
            q.put(ping_ip)
def getip():
    while True:
        ip = q.get()
        if subprocess.call(ip,shell = True)==0:
            l.append(ip)
            print('%s is connection'%ip)
        else:
            print('%s is unconnection'%ip)
        q.task_done()
qq= geip()

for x in range(10):
    
    x = threading.Thread(target = getip)
    x.setDaemon(True)
    x.start()

q.join()
print(l)


def check():
    s_check = socket.socket()
    for i in l:
        try:
            s_check.connect((i, 60008))
            print(i)
                        
        except socket.error:
            print('dasdas')



        


    

app = Myapp()
app.MainLoop()
