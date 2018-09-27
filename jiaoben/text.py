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
        
text = User()

for i in text.f():
    print(i)


import wx
class Login(wx.Frame):
   def __init__(self):
      super(Login, self).__init__(None)
      self.InitUI()
   def InitUI(self):
      self.SetSize((300,250))
      self.SetTitle(u'用户登录')

      #创建一个大的panel并且设置为垂直布局
      p = wx.Panel(self)
      vbox=wx.BoxSizer(wx.VERTICAL)

      #标题
      title=wx.StaticText(p,label=u'用户登录',style=wx.ALIGN_CENTRE)
      vbox.Add(title,0,wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 20)

      #创建一个账号的ubox水平布局并嵌套到vbox
      ubox=wx.BoxSizer(wx.HORIZONTAL)
      ulabel = wx.StaticText(p, label = u'账号：')
      ubox.Add(ulabel)
      ubox.Add([10,10],0)
      self.utext = wx.TextCtrl(p)
      ubox.Add(self.utext)

      vbox.Add(ubox,0,wx.ALIGN_CENTER)#嵌套到vbox

      #密码同上
      pbox=wx.BoxSizer(wx.HORIZONTAL)
      plabel = wx.StaticText(p, label =  u'密码：')
      pbox.Add(plabel)
      pbox.Add([10,10],0)

      self.ptext = wx.TextCtrl(p)
      pbox.Add(self.ptext)

      vbox.Add(pbox,0,wx.ALIGN_CENTER)#嵌套到vbox


      btnbox=wx.BoxSizer(wx.HORIZONTAL)
      btn01 = wx.Button(p,label=u'确认',size=(50,30))
      btnbox.Add(btn01,1,wx.ALL,10)

      btn02 = wx.Button(p,label=u'取消',size=(50,30))
      btnbox.Add(btn02,1,wx.ALL,10)

      vbox.Add(btnbox,0,wx.ALIGN_CENTER)#嵌套到vbox


      #绑定确认按钮事件
      self.Bind(wx.EVT_BUTTON, self.OnSubmit, btn01)
      #绑定取消按钮事件
      self.Bind(wx.EVT_BUTTON, self.OnCancel, btn02)


      p.SetSizer(vbox)
      self.Centre()
      self.Show(True)#设置窗口可见


   def OnSubmit(self,event):
      if self.utext.GetValue()=='test'and self.ptext.GetValue()=='test':
         dlg = wx.MessageDialog(None, u"登录成功", u"提示", wx.YES_NO)
         if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
         dlg.Destroy()
      else:
         err=wx.MessageDialog(None, u"登录失败，用户名或密码错误", u"提示", wx.YES_NO)
         print(0)
         if err.ShowModal() == wx.ID_YES:
            err.Destroy()


   def OnCancel(self,event):
      self.Close(True)


      #嵌套的关系：
      #window - panel - vbox - {label, hbox(label, text), hbox(btn, btn) }

app = wx.App()
frame = Login()
frame.Show()
app.MainLoop()
