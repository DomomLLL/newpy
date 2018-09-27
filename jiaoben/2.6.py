import wx
class Iif(wx.Frame):
    def init__(self,parent = None,id = -1):
        wx.Frame.__init__(self,parent,id,'Frame with Button',
                          size = (300,100))
        panel = wx.Panel(self)
        button  = wx.Button(panel,label='确认',pos=(125,10),
                            size = (50,50))
        self.Bind(wx.EVT_BUTTON,self.Cm,button)
        self.Bind(wx.EVT_CLOSE,self.C)

        

    def C(self,event):
        self.Destroy()

    def Cm(self,event):
        self.Close(True)

app = wx.App()
frame = Iif()
frame.Show()
app.MainLoop()


