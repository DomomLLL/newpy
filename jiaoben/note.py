import wx
class MyApp(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,-1,'Note')
        p = wx.Panel(self)
        menu = wx.MenuBar()
        menu1 = wx.Menu()
        menu.Append(menu1,'菜单')
        save = menu1.Append(-1,'保存')
        dakai = menu1.Append(-1,'打开')
        self.SetMenuBar(menu)

        self.Bind(wx.EVT_MENU,self.Onsave,save)
        self.Bind(wx.EVT_MENU,self.Onopen,dakai)

    def Onsave(self, event):
        dialog = wx.FileDialog(None, 'save as', style=wx.FD_SAVE)
        dialog.ShowModal()
        path = dialog.GetPath()
        print(dialog.GetPath())
    def Onopen(self, event):
        dialog = wx.FileDialog(None, 'save as', style=wx.FD_OPEN)
        dialog.ShowModal()
        print(dialog.GetPath())


app = wx.App()
frame = MyApp()
frame.Show()
app.MainLoop()
