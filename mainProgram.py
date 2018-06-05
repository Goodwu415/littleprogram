#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import wx

from interface import MainFace

class MainProgram(MainFace):
    user = ''
    pad = ''

    # def __init__(self, user, password, *argv):
    #
    #     self.user = user
    #     self.password = password
    #     self.phone = argv
    #     self.verification()

    def newOrold(self):
        pass
        # if id == 1:
        #     self.registerUser()
        #
    def registerUser(self):  #新用户注册
        with open('test.txt','a') as d:
            data = self.user +':' +self.pad + '\n'
            d.write(data)
            print("成功写入")
            d.close()

    def openUserBase(self): # 打开数据库
        with open('test.txt', 'r') as s:
            data = s.read()
            s.close()
        return data

    def verification(self): #登录验证
        data = self.openUserBase()
        user1 = data[0:data.rfind(':')]
        pa = data[data.rfind(':')+1:]
        if user1 == self.user:
            if pa == self.pad:
                print("成功登录")
                return True
            else:
                print("密码错误")
                return False
        else:
            print("用户名不存在或密码错误")
            return False

    def newUserIn(self): #新用户登录
        print("登录成功")

    def SingIn(self,event):
        self.user = self.textAll.GetValue()
        self.pad = self.textAll2.GetValue()
        if self.user:
            if self.pad:

                if self.verification():
                    self.panel.Destroy()
                    self.corePram()
                else:
                    print("Again input")
            else:
                print("请输入密码")
        else:
            print("用户名不能为空")
        print(self.user, self.pad)

    def newUser(self,event):
        self.user = self.textAll.GetValue()
        self.pad = self.textAll2.GetValue()
        if self.user:
            if self.pad:
                self.registerUser()
                self.newUserIn()
                self.panel.Destroy()
                self.corePram()
            else:
                print("请输入密码")
        else:
            print("用户名不能为空")

def main():

    app = wx.App()
    frame = MainProgram()
    frame.Show()
    app.MainLoop()

   #app1 = MainProgram(app.user, app.pad)
#   app1.verification()



    # n = input("登录：1 注册：2")
    # if n == '2':
    #     user = input("用户名")
    #     password = input('密码')
    #     phone = input("手机号码")
    #     app = MainProgram(user,password, phone)
    #     app.registerUser()
    #     app.newUserIn()
    # elif n== '1':
    #     user = input("用户名")
    #     password = input('密码')
    #     app = MainProgram(user, password)
    #     app.openUserBase()
    #


main()

