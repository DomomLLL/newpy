import wx
import wx.xrc
import time
from threading import Thread, Event
import socket
import struct


class Sendd(Thread):
    def __init__(self, s, getvalues, name):
        Thread.__init__(self)
        self.s = s
        self.getvalues = getvalues
        self.name = name

    def run(self):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        network = '<broadcast>'
        ntime = time.ctime()
        message = ntime + ' ' + self.name + ' say: ' + self.getvalues + '\n'
        self.s.sendto(message.encode('utf-8'),
                      (network, 1234))


class Recv(Thread):
    def __init__(self, r):
        self.r = r
        Thread.__init__(self)

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        PORT = 1234

        s.bind(('', PORT))
        print('Listening for broadcast at ', s.getsockname())

        while True:
            data, address = s.recvfrom(65535)
            print('Server received from {}:{}'.format(address, data.decode('utf-8')))
            self.r.WriteText(data.decode('utf-8'))

        # self.record.AppendText(data)


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"聊天室", pos=wx.DefaultPosition, size=wx.Size(610, 410),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.record = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(610, 200),
                                  wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer1.Add(self.record, 0, wx.ALL, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer2.SetMinSize(wx.Size(50, 20))
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"昵称", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), 0)
        bSizer2.Add(self.name, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer4.SetMinSize(wx.Size(100, 170))
        self.say = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, 160), wx.TE_MULTILINE)
        bSizer4.Add(self.say, 0, wx.ALL, 5)

        self.m_button = wx.Button(self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(-1, 160), 0)
        bSizer4.Add(self.m_button, 0, wx.ALL, 5)

        bSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)
        self.sss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connect Events
        # self.name.Bind(wx.EVT_TEXT, self.Name)
        self.m_button.Bind(wx.EVT_BUTTON, self.Send)
        recv = Recv(self.record)
        recv.setDaemon(True)
        recv.start()
        # self.record.AppendText(recv.run())
        # udp_gb_client.py

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    # def Name(self, event):
    #     data = self.name.GetValue()
    #     self.record.AppendText(data)

    def Send(self, event):
        data = self.say.GetValue()
        data1 = self.name.GetValue()
        send = Sendd(self.sss, data, data1)
        send.setDaemon(True)
        send.start()
        self.say.Clear()


def main():
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()


