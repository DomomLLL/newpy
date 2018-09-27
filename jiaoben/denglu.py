import wx
import sqlite3
class User():
    def __init__(self):
        self.coon = sqlite3.connect('denglu')
        self.cur = self.coon.cursor()
    def i(self,name, passwd):
        self.cur.execute("insert into message values('{}','{}')".format(name,passwd))
        self.coon.commit()

    def f(self):
        self.user_passwd = self.cur.execute("select * from message")
        return self.cur.fetchall()
    
    def __del__(self):
        self.cur.close()
        self.coon.close()

class zcWindow(wx.App,wx.Frame):
    def OnInit(self):
        frame = wx.Frame(parent = None,
                         title = '注册',
                         size = (500, 370))
        self.panel = wx.Panel(frame, -1)
        label_All = wx.StaticText(self.panel,-1,'用户名',pos=(80,100))  
        self.textName = wx.TextCtrl(self.panel, -1, style = wx.TE_MULTILINE,pos=(140,100),size=(170,30))
        label_Say = wx.StaticText(self.panel,-1,'密码',pos=(80,160))  
        self.textPasswd = wx.TextCtrl(self.panel, -1,style = wx.TE_MULTILINE,pos=(140,160),size=(170,30))      
 
        self.button_clear = wx.Button(self.panel, -1 , '注册', pos=(160,230))
        self.frame = frame

        self.Bind(wx.EVT_BUTTON,self.zc, self.button_clear)
        
        frame.Show()
        return True
    def zc(self, event):
        new_user = User()
        get_name = self.textName.GetValue()
        get_passwd = self.textPasswd.GetValue()
        new_user.i(get_name,get_passwd)
    
        
    
class MainWindow(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,
                         title = '登录',
                         size = (500, 370))
        self.panel = wx.Panel(frame, -1)
        label_All = wx.StaticText(self.panel,-1,'用户名',pos=(80,100))  
        self.textName = wx.TextCtrl(self.panel, -1, style = wx.TE_MULTILINE,pos=(140,100),size=(170,30))
        label_Say = wx.StaticText(self.panel,-1,'密码',pos=(80,160))  
        self.textPasswd = wx.TextCtrl(self.panel, -1,style = wx.TE_MULTILINE,pos=(140,160),size=(170,30))      
        self.button_sent = wx.Button(self.panel, -1 , '登录', pos=(100,260))
        self.button_clear = wx.Button(self.panel, -1 , '注册', pos=(230,260))
        self.frame = frame

        self.Bind(wx.EVT_BUTTON, self.onClick,self.button_clear)
        self.Bind(wx.EVT_BUTTON, self.camein, self.button_sent)
        
        frame.Show()
        return True
    
    
    def onClick(self, event):
        dialog = zcWindow()
        

    def camein(self,event):
        p = User()
        g = p.f()
        get_name = format(self.textName.GetValue())
        get_passwd = self.textPasswd.GetValue()
        l = (get_name,get_passwd)
        for i in g:
            if  i == l:
                T = 1
            else:
                T = 0
        if T == 1:
            print('success')
        else:
            print('fail')
        
        
     
app = MainWindow()
app.MainLoop()

