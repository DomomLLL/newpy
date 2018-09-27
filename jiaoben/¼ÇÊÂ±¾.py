import wx
class CreateMenu():
    def __init__(self, parent):
        self.menu = wx.MenuBar()
        self.menu1 = wx.Menu()
        self.menu2 = wx.Menu()
        self.menu3 = wx.Menu()
        self.menu.Append(self.menu1,'File')
        self.menu.Append(self.menu2,'Edit')
        self.menu.Append(self.menu3,'Help')
        self.save = self.menu1.Append(-1,'保存')
        self.open = self.menu1.Append(-1,'打开')
        self.undo = self.menu2.Append(-1,'undo')
        self.redo = self.menu2.Append(-1,'redo')
        self.cut = self.menu2.Append(-1,'cut')
        self.copy = self.menu2.Append(-1,'copy')
        self.paste = self.menu2.Append(-1,'paste')
        parent.SetMenuBar(self.menu)

class MyApp(wx.App):
    def OnInit(self):
        self.file = ''
        self.width = 640
        self.height = 480
        self.frame = wx.Frame(parent = None,
                              title = 'Note',
                              size = (self.width,self.height))
        self.panel = wx.Panel(self.frame,-1)
        self.menu = CreateMenu(self.frame)
        self.text = wx.TextCtrl(self.panel, -1, pos = (2, 2),
                                size=(self.width-10, self.height-50),
                                style=wx.TE_MULTILINE|wx.HSCROLL)
        
        self.Bind(wx.EVT_MENU,self.onOpen,self.menu.open)
        self.Bind(wx.EVT_MENU,self.onSave,self.menu.save)                      
        self.Bind(wx.EVT_MENU,self.onUndo,self.menu.undo) 
        self.Bind(wx.EVT_MENU,self.onRedo,self.menu.redo)
        self.Bind(wx.EVT_MENU,self.onCut,self.menu.cut) 
        self.Bind(wx.EVT_MENU,self.onCopy,self.menu.copy) 
        self.Bind(wx.EVT_MENU,self.onPaste,self.menu.paste)
        self.Bind(wx.EVT_RIGHT_DOWN, self.onRClick)

        self.frame.Show()
        return True

    def onOpen(self,event):
        dlg = wx.FileDialog(None,'Note',style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            print('onOpen')
            self.file_name = dlg.GetPath()
            with open(self.file_name) as f:
                self.text.Clear()
                self.text.WriteText(f.read())
        
        
    def onSave(self,event):
        if self.file == '':
            dlg = wx.FileDialog(None,'Note', style = wx.FD_SAVE)
            if dlg.ShowModal() == wx.ID_OK:
                self.file_name = dlg.GetPath()
                self.text.SaveFile(self.file_name)
            
        else:
            self.text.SaveFile(self.file)
        
    def onRedo(self,event):
        pass
    def onUndo(self,event):
        pass
    def onCut(self,event):
        pass
    def onCopy(self,event):
        pass
    def onPaste(self,event):
        pass
    def onRClick(self,event):
        pos = (event.GetX(),event.GetY())
        self.panel.PopupMenu(self.menu.menu_file, pos)





        

        
app = wx.App()
frame = MyApp()
app.MainLoop()
