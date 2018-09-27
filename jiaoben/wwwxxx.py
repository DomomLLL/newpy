import wx
import turtle
class MyApp(wx.App):

    def OnInit(self):
        frame = wx.Frame(parent = None, title = 'tools')
        panel = wx.Panel(frame, -1)
        self.button_wjx = wx.Button(panel, -1, '777', pos = (50, 50))
        self.button_sj = wx.Button(panel, -1, '666', pos = (0, 50))
        self.Bind(wx.EVT_BUTTON, self.OnButtonWjx, self.button_wjx)
        self.Bind(wx.EVT_BUTTON, self.Sj, self.button_sj)
        frame.Show()
        return True
    def Sj(self, event):
        for i in range(3):
            turtle.forward(100)
            turtle.left(120)

    def OnButtonWjx(self, event):
        for i in range(5):
            turtle.forward(100)
            turtle.right(144)
        
app = MyApp()
app.MainLoop()
