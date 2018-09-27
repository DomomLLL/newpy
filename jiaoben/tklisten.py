import tkinter
import socket
from threading import Thread,Event
class Listen(Thread):
    def __init__(self,edit,sever):
        Thread.__init__(self)
        self.edit = edit
        self.sever = sever
        self.l=[]
        
    def run(self):
        while True:
            conn, addr = self.sever.accept()
            
            data = conn.recv(1024)
            self.edit.insert(tkinter.END,'来自ip{}:\n{}\n'.format(addr[0],data))
            self.l.append(data.decode('utf-8'))
            conn.close()
            
              
        
            with open(self.l[0],'a+') as f:
                f.write('{}'.format(data.decode('utf-8')))
       
          

            
            
            
        
    


class Control(Thread):
    def __init__(self,edit):
        Thread.__init__(self)
        self.event = Event()
        self.event.clear()
        self.edit = edit
    def run(self):
        sever =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sever.bind(('',5000))
        sever.listen(1)
        self.edit.insert(tkinter.END,'start listen\n')
        self.lt = Listen(self.edit,sever)
        self.lt.setDaemon(True)
        self.lt.start()
        self.event.wait()
        sever.close()
        
    def stop(self):
        self.event.set()
    
class Window:
    def __init__(self,root):
        self.root = root
        self.btnListen = tkinter.Button(root,
                                        text = 'start',
                                        command = self.Listen)
        self.btnListen.place(x=20,y=15)
        self.btnClose = tkinter.Button(root,
                                      text = 'close',
                                      command = self.Close)
        self.btnClose.place(x=120,y=15)
        self.edit = tkinter.Text(root)
        self.edit.place(y = 50)

    def Listen(self):
        self.ctrl = Control(self.edit)
        self.ctrl.setDaemon(True)
        self.ctrl.start()

    def Close(self):
        self.ctrl.stop()
        



root = tkinter.Tk()
window = Window(root)
root.mainloop()
