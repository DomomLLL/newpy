import wx
import time

class Myapp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,
                         title = 'my chat',
                         size = (520, 450))
        panel = wx.Panel(frame, -1)
        label_All = wx.StaticText(panel,-1,'chat record')

        self.textAll = wx.TextCtrl(panel, -1, style = wx.TE_MULTILINE)
        label_Say = wx.StaticText(panel,-1,'chat')  
        self.textSay = wx.TextCtrl(panel, -1,style = wx.TE_MULTILINE)
    
        self.button_sent = wx.Button(panel, -1 , 'send')
        self.button_clear = wx.Button(panel, -1 , 'clear')
        self.Bind(wx.EVT_BUTTON, self.onSent, self.button_sent)
        self.Bind(wx.EVT_BUTTON, self.onClear, self.button_clear)

        btnSizer = wx.BoxSizer()
        btnSizer.Add(self.button_clear, proportion=0)
        btnSizer.Add(self.button_sent, proportion=0)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(label_All, proportion=0, flag= wx.ALIGN_CENTER)

        mainSizer.Add(self.textAll, proportion=1, flag=wx.EXPAND)
        mainSizer.Add(label_Say, proportion=0, flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textSay, proportion=0, flag=wx.EXPAND )
       
        mainSizer.Add(btnSizer, proportion=0, flag=wx.ALIGN_CENTER)
        panel.SetSizer(mainSizer)
        frame.Show()
        return True
    def onSent(self, event):
        userinput = self.textSay.GetValue()
        self.textSay.Clear()
        inmsg = '{} youSay:{}\n'.format(time.ctime(),userinput)
        self.textAll.AppendText(inmsg)

    def onClear(self, event):
        self.textAll.Clear()
        
app = Myapp()
app.MainLoop()

