__author__ = 'Yas'
from Tkinter import *
from ttk import Button
from Tkinter import Tk
import base64
import tkMessageBox as box
import os
from PIL import Image, ImageTk

'''
This is the login class of the system. It verify the username and password by using config text file.
If user fogot the pass word he/she can change the new password and restore the password by restoring it.
At the 1st time user should enter the system by using username Yas and password sri
'''
#this is the class which display the error massage
class Example():
    def onError(self):
        box.showerror("Error", "Login Fail")

    def onInfo(self):
        box.showinfo("Information", "Login Sucessfully")
#this is the class for login function
class LoginWindow():
    def __init__(self, root):
        self.mastert = root
        self.mastert.configure(background='#8A002E')
        self.img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
        self.imglabel = Label(self.mastert, image=self.img).grid(row=0, column=4)
        self.mastert.wm_title("System Login")
        Label(self.mastert,background='#8A002E',foreground="white", text="Enter System UserName").grid(row=1)
        Label(self.mastert, background='#8A002E',foreground="white",text="Enter System Password:").grid(row=2)

        self.e1 = Entry(self.mastert)
        self.e2 = Entry(self.mastert)

        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        Button(self.mastert, text='Help', command=self.Help).grid(row=3, column=0, sticky=W, pady=4)
        Button(self.mastert, text='Quit', command=self.mastert.quit).grid(row=3, column=3, sticky=W, pady=4)
        Button(self.mastert, text='Submit', command=self.Fun).grid(row=3, column=4, sticky=W, pady=4)
        Button(self.mastert, text='Fogot Password', command=self.fogot).grid(row=3, column=1, sticky=W, pady=4)
    #read password from file-------------------
    def getUserUserNm(self,user):
      tem=[]
      with open('Config.txt','r') as f:
        for line in f:
            for word in line.split():
               tem.append(word)
        if tem[0]==base64.b64encode(user):
            return 1
        else:
            return 0
    #get password-----------
    def getUserPass(self,pas):
      tem=[]
      with open('Config.txt','r') as f:
        for line in f:
            for word in line.split():
               tem.append(word)
        if tem[1]==base64.b64encode(pas):
            return 1
        else:
            return 0
#this is the function for enter the system if login sucessful
    def SysLog(self):
        os.system('python win_HomeWin1.py')
#this is the function for change password
    def fogot(self):
        os.system('python Config.py')
#this is the function for verify username and password
    def Fun(self):
        self.UserNM = self.e1.get()
        self.PassWD = self.e2.get()
        user=self.getUserUserNm(self.UserNM)
        pas=self.getUserPass(self.PassWD)
        if (user==1)&(pas==1):
            Example().onInfo()
            self.mastert.withdraw()
            self.SysLog()

        else: Example().onError()

    def Help(self):
        os.system('python win3_Help.py')

#To generate the system
root = Tk()
my_gui = LoginWindow(root)
root.mainloop()