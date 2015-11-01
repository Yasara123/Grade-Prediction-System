__author__ = 'Yas'
from Tkinter import *
import MySQLdb
from ttk import Frame, Button, Style
from Tkinter import Tk
import base64
import tkMessageBox as box
from PIL import Image, ImageTk
import os


class Example():
    def onError(self):
        box.showerror("Error", "Could not Create Table")

    def onQuest(self):
        box.askquestion("Question", "Are you sure to quit?")

    def onInfo(self):
        box.showinfo("Information", "Upadate Sucessfully")

class ViewWarnings():
    tem=[]
    names=[]
    def getUserNm(cls):
      with open('Config.txt','r') as f:
        for line in f:
            for word in line.split():
               cls.tem.append(word)
        return cls.tem[2]
    def getPass(cls):
        return cls.tem[3]
    def HelpCon(cls):
        os.system('python HelpConfig.py')
    def Fun2(cls):
        import os
        cls.master.withdraw()
        os.system('python Model_Config.py')
    def Back(cls):
       import os
       cls.master.withdraw()
       os.system('python win_HomeConfig.py')
    #setDB
    def ReadTable(cls):
        cls.Er="null"
        cls.user=cls.getUserNm()
        cls.pas=cls.getPass()
        # Open database connection
        cls.db = MySQLdb.connect("localhost",cls.user,cls.pas,"marks2" )
        # prepare a cursor object using cursor() method
        cls.cursor = cls.db.cursor()
        # Prepare SQL query to UPDATE required records
        cls.sql="SELECT * FROM warnings"
        try:
          # Execute the SQL command
          cls.cursor.execute(cls.sql)
         # Fetch all the rows in a list of lists.
          results = cls.cursor.fetchall()
          for row in results:
              cls.names.append(row)
        except:
           cls.Er="not null"
           #Rollback in case there is any error
           cls.db.rollback()
           print "Error: unable to create Table"
           Example().onError()
        return cls.names

    def __init__(cls,master):
        cls.master=master
        cls.master.configure(background='#8A002E')
        cls.img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
        cls.imglabel = Label(cls.master, image=cls.img).grid(row=0, column=3)
        cls.master.wm_title("System Configuration")
        cls.names=cls.ReadTable()
        Label(cls.master,background='#8A002E',foreground="white",font=("Purisa", 12), text="Subject|    Student Name|   Marks(%) ").grid(row=1, column=0)
        i=2
        for x in cls.names:
            Label(cls.master,background='#8A002E',foreground="white",font=("Purisa", 16), text=x).grid(row=int(i), column=0)
            i=i+1
        Button(cls.master, text='Back', command=cls.Back).grid(row=7, column=0, sticky=W, pady=4)
        Button(cls.master, text='HELP', command=cls.HelpCon).grid(row=7, column=1, sticky=W, pady=4)
        Button(cls.master, text='Quit', command=cls.master.quit).grid(row=7, column=2, sticky=W, pady=4)

root = Tk()
my_gui =ViewWarnings(root)
root.mainloop()

