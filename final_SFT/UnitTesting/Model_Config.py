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
        box.showerror("Error", "Error : Maximum no of subjects exeed ")
    def onInfo(self):
        box.showinfo("Information", "Value Write Sucessfully")
mastert = Tk()
mastert.configure(background='#8A002E')
img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
imglabel = Label(mastert, image=img).grid(row=0, column=3)
mastert.wm_title("System Login")
Label(mastert,background='#8A002E',foreground="white", text="Enter Nuber Of Subjects:").grid(row=1)
Label(mastert,background='#8A002E',foreground="white", text="(Enter subject marks to the txt files ").grid(row=2, column=0)
Label(mastert,background='#8A002E',foreground="white", text="names data1.txt,data2,txt and maximum data3.txt)").grid(row=2, column=1)
e1 = Entry(mastert)
e1.grid(row=1, column=1)
def Fun():
    val=e1.get()
    if (int(val) ==1):

        import ReadSub1
        ReadSub1.getSub()
        ReadSub1.getSub1()
        ReadSub1.fun1()
    if (int(val) ==2):

        import ReadSub2
        ReadSub2.getSub()
        ReadSub2.getSub1()
        ReadSub2.getSub2()
        ReadSub2.fun1()
        ReadSub2.fun2()
    if (int(val) ==3):

        import Readsub3
        Readsub3.getSub()
        Readsub3.getSub1()
        Readsub3.getSub2()
        Readsub3.getSub3()
        Readsub3.fun1()
        Readsub3.fun2()
        Readsub3.fun3()
    if (int(val)>3):Example().onError()
    Example().onInfo()
    mastert.quit()
def Back():
   import os
   mastert.withdraw()
   os.system('python Config.py')

Button(mastert, text='Back', command=Back).grid(row=3, column=0, sticky=W, pady=4)
Button(mastert, text='Quit', command=mastert.quit).grid(row=3, column=2, sticky=W, pady=4)
Button(mastert, text='Submit', command=Fun).grid(row=3, column=3, sticky=W, pady=4)
mainloop( )
