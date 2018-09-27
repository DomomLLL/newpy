import wx
class zcWindow(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,
                         title = 'my chat',
                         size = (500, 370))
        self.panel = wx.Panel(frame, -1)
        label_All = wx.StaticText(self.panel,-1,'用户名',pos=(80,100))  
        self.textName = wx.TextCtrl(self.panel, -1, style = wx.TE_MULTILINE,pos=(140,100),size=(170,30))
        label_Say = wx.StaticText(self.panel,-1,'密码',pos=(80,160))  
        self.textPasswd = wx.TextCtrl(self.panel, -1,style = wx.TE_MULTILINE,pos=(140,160),size=(170,30))      
 
        self.button_clear = wx.Button(self.panel, -1 , '注册', pos=(160,230))
        self.frame = frame


        
        frame.Show()
        return True
    
    
app = zcWindow()
app.MainLoop()
