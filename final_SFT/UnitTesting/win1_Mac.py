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
        box.showerror("Error", "No Of Subjects Exceed Maximun Limits ")




mastert = Tk()
mastert.configure(background='#8A002E')
img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
imglabel = Label(mastert, image=img).grid(row=0, column=3)
mastert.wm_title("System Login")
Label(mastert,background='#8A002E',foreground="white", text="Enter No Dependent Subjects:").grid(row=1)

e1 = Entry(mastert)


e1.grid(row=1, column=1)



def SysLog1():
    os.system('python win_Mac_sub1.py')

def SysLog2():
    os.system('python win_Mac_sub2.py')
def SysLog3():
    os.system('python win_Mac_sub3.py')
def Fun():
    subNo = e1.get()
    if (int(subNo)==1):
        mastert.withdraw()
        SysLog1()
    if (int(subNo)==2):
        mastert.withdraw()
        SysLog2()
    if (int(subNo)==3):
        mastert.withdraw()
        SysLog3()
    else: Example().onError()

Button(mastert, text='Quit', command=mastert.quit).grid(row=4, column=2, sticky=W, pady=4)
Button(mastert, text='Submit', command=Fun).grid(row=4, column=3, sticky=W, pady=4)
mainloop( )

