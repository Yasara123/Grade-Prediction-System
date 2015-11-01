__author__ = 'Yas'
from Tkinter import *
import MySQLdb
from ttk import Frame, Button, Style
from Tkinter import Tk
import base64
import tkMessageBox as box
import os
from PIL import Image, ImageTk

class Example():
    def onError(self):
        box.showerror("Error", "Login Fail")

    def onInfo(self):
        box.showinfo("Information", "Login Sucessfully")


mastert = Tk()
mastert.configure(background='#8A002E')
img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
imglabel = Label(mastert, image=img).grid(row=0, column=3)
mastert.wm_title("System Login")
Label(mastert,background='#8A002E',foreground="white", text="Enter System UserName").grid(row=1)
Label(mastert, background='#8A002E',foreground="white",text="Enter System Passwor:").grid(row=2)

e1 = Entry(mastert)
e2 = Entry(mastert)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

#read password from file-------------------
def getUserUserNm(user):
  tem=[]
  with open('Config.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
    if tem[0]==base64.b64encode(user):
        return 1
    else:
        return 0
#get password
def getUserPass(pas):
  tem=[]
  with open('Config.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
    if tem[1]==base64.b64encode(pas):
        return 1
    else:
        return 0

def SysLog():
    os.system('python win_HomeWin1.py')


def Fun():
    UserNM = e1.get()
    PassWD = e2.get()
    user=getUserUserNm(UserNM)
    pas=getUserPass(PassWD)
    if (user==1)&(pas==1):
        Example().onInfo()
        mastert.withdraw()
        SysLog()

    else: Example().onError()



Button(mastert, text='Quit', command=mastert.quit).grid(row=3, column=2, sticky=W, pady=4)
Button(mastert, text='Submit', command=Fun).grid(row=3, column=3, sticky=W, pady=4)
mainloop( )
