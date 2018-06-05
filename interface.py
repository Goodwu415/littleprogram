#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import wx

class MainFace(wx.Frame):

    def __init__(self):
        ID = wx.NewId()
        wx.Frame.__init__(self, None, ID, "改变世界", size = (600,500),pos=(600,400))

        self.panel = wx.Panel(self, -1)



        self.ButtonHome()   #按钮

        self.panelIn()  # 登录信息填写
        self.faceIn() # 登录显示
        self.Bindingfun() #绑定事件


    def Assembly(self):
        self.button1 = wx.Button(self.panel2, label="Music", size=(100, 100))
        self.button2 = wx.Button(self.panel2, label="Joke", size=(100, 100))
        self.button3 = wx.Button(self.panel2, label="Paragraph", size=(100, 100))
        self.button4 = wx.Button(self.panel2, label="Journalism", size=(100, 100))
        self.button5 = wx.Button(self.panel2, label="Article", size=(100, 100))
    def manageFace(self):
        sizer = wx.FlexGridSizer(wx.HORIZONTAL)
        sizer.Add(self.button1, 1, wx.ALL, 10)

        sizer.Add(self.button2, 1, wx.ALL, 10)
        sizer.Add(self.button3, 1, wx.ALL, 10)

        sizer.Add(self.button4, 1, wx.ALL, 10)
        sizer.Add(self.button5, 1, wx.ALL, 10)
        self.panel2.SetSizer(sizer)
        sizer.Fit(self)


    def corePram(self): # 新窗口实现

        self.panel2 = wx.Panel(self, id=wx.NewId(), size=(600, 500))

        self.Assembly() #  实现button
        self.manageFace() # 实现管理button
        self.BindAssembly()

    def panelIn(self):
        self.basicLabel = wx.StaticText(self.panel, -1,"Basic Control:")
        self.textAll = wx.TextCtrl(self.panel, -1  # 用户框
                                   )

        self.pwdLabel = wx.StaticText(self.panel, -1,"Password:")

        self.textAll2 = wx.TextCtrl(self.panel, -1,  # 密码框
                                   style=wx.TE_PASSWORD)

    def ButtonHome(self):
        self.buttonx1 = wx.Button(self.panel, label="注册",size=(60,40))
        self.buttonx2 = wx.Button(self.panel, label="登录",size=(60,40))


    def faceIn(self):
        '''
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.basicLabel,0, wx.ALL, 5)
        sizer.Add( self.textAll, 0, wx.ALL, 5)
        sizer.Add(self.pwdLabel, 0, wx.ALL, 5)
        sizer.Add(self.textAll2, 0, wx.ALL, 5)
        '''

        mainSizer = wx.FlexGridSizer(cols=2, hgap = 5, vgap = 5)
        mainSizer.AddGrowableCol(1)
        mainSizer.Add(self.basicLabel,0,wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        mainSizer.Add(self.textAll,wx.ALL,10)
        mainSizer.Add(self.pwdLabel, 0,
                      wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        mainSizer.Add(self.textAll2, wx.ALL)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20),10)
        btnSizer.Add(self.buttonx1,0)
        btnSizer.Add((20, 20), 10)
        btnSizer.Add(self.buttonx2,0)
        btnSizer.Add((20,20),10)

        mainSizer.Add(btnSizer,0,wx.EXPAND|wx.BOTTOM,10)

        self.panel.SetSizer(mainSizer)


    def Bindingfun(self):
        self.Bind(wx.EVT_BUTTON, self.SingIn,     self.buttonx2)
        self.Bind(wx.EVT_BUTTON, self.newUser,    self.buttonx1)

    def BindAssembly(self):
        self.Bind(wx.EVT_BUTTON, self.Music,      self.button1)
        self.Bind(wx.EVT_BUTTON, self.Joke,       self.button2)
        self.Bind(wx.EVT_BUTTON, self.Paragraph,  self.button3)
        self.Bind(wx.EVT_BUTTON, self.Journalism, self.button4)
        self.Bind(wx.EVT_BUTTON, self.Article,    self.button5)

    def LastTime(self):
        self.face = wx.Button(self.panel3, label="主界面", size=(60, 40), pos=(2,0))

    def LastON(self):
        self.Bind(wx.EVT_BUTTON, self.oldFace, self.face)

    def oldFace(self, event):
        self.panel3.Destroy()
        self.corePram()

    def SingIn(self,event):
        pass
    def newUser(self,event):
        pass
    def Music(self,event):

        self.panel2.Destroy()
        self.panel3 = wx.Panel(self, id=wx.NewId(), size=(600, 500))
        self.LastTime()
        self.LastON()
    def Joke(self, event):
        self.panel2.Destroy()
        self.panel3 = wx.Panel(self, id=wx.NewId(), size=(600, 500))
        self.LastTime()
        self.LastON()
    def Paragraph(self, event):
        self.panel2.Destroy()
        self.panel3 = wx.Panel(self, id=wx.NewId(), size=(600, 500))

        self.LastTime()
        self.LastON()
    def Journalism(self, event):
        self.panel2.Destroy()
        self.panel3 = wx.Panel(self, id=wx.NewId(), size=(600, 500))
        self.LastTime()
        self.LastON()
    def Article(self, event):
        self.panel2.Destroy()
        self.panel3 = wx.Panel(self, id=wx.NewId(), size=(600, 500))
        self.LastTime()
        self.LastON()


    def OnExit(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()

    frame = MainFace()
    frame.Show()
    app.MainLoop()

