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

class NewSub():
    tem=[]
    def getUserNm(cls):
      with open('Config.txt','r') as f:
        for line in f:
            for word in line.split():
               cls.tem.append(word)
        return cls.tem[2]
    tem2=[]
    def ReadNames(cls):
      with open('NewStudentIndex.txt','r') as f:
        for line in f:
            for word in line.split():
               cls.tem2.append(word)
      return cls.tem2

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
    def __init__(cls,master):
        cls.master=master
        cls.master.configure(background='#8A002E')
        cls.img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
        cls.imglabel = Label(cls.master, image=cls.img).grid(row=0, column=3)

        cls.master.wm_title("System Configuration")
        Label(cls.master,background='#8A002E',foreground="white", text="Enter Subject Name").grid(row=1)
        Label(cls.master,background='#8A002E',foreground="white", text="Enter Year:").grid(row=2)
        cls.e1 = Entry(cls.master)
        cls.e2 = Entry(cls.master)
        cls.e1.grid(row=1, column=1)
        cls.e2.grid(row=2, column=1)

        Button(cls.master, text='Back', command=cls.Back).grid(row=7, column=0, sticky=W, pady=4)
        Button(cls.master, text='HELP', command=cls.HelpCon).grid(row=7, column=1, sticky=W, pady=4)
        Button(cls.master, text='Quit', command=cls.master.quit).grid(row=7, column=2, sticky=W, pady=4)
        Button(cls.master, text='Create_Table', command=cls.Fun).grid(row=7, column=3, sticky=W, pady=4)
        Button(cls.master, text='Enter_Names', command=cls.Fun2).grid(row=7, column=4, sticky=W, pady=4)

    #setDB
    def CreatTable(cls,tbl):
        cls.Er="null"
        cls.user=cls.getUserNm()
        cls.pas=cls.getPass()
        # Open database connection
        cls.db = MySQLdb.connect("localhost",cls.user,cls.pas,"marks2" )
        # prepare a cursor object using cursor() method
        cls.cursor = cls.db.cursor()
        # Prepare SQL query to UPDATE required records
        cls.sql="CREATE TABLE IF NOT EXISTS %s (" \
                "StudentName VARCHAR(30)," \
                "Test1 FLOAT ," \
                "Test2 FLOAT ," \
                "Test3 FLOAT ," \
                "Test4 FLOAT ," \
                "Test5 FLOAT ," \
                "Test6 FLOAT ," \
                "Test7 FLOAT ," \
                "Test8 FLOAT ," \
                "Test9 FLOAT ," \
                "Test10 FLOAT ," \
                "Test11 FLOAT ," \
                "Test12 FLOAT ," \
                "Test13 FLOAT ," \
                "Test14 FLOAT ," \
                "Test15 FLOAT ," \
                "pred FLOAT )"%(str(tbl))
        try:
           # Execute the SQL command
           print "sql"
           cls.cursor.execute(cls.sql)
           Example().onInfo()
           # Commit your changes in the database
           cls.db.commit()
        except:
           cls.Er="not null"
           #Rollback in case there is any error
           cls.db.rollback()
           print "Error: unable to create Table"
           Example().onError()
    #setDB
    def ScanNames(cls,Tbl):
        cls.Er="null"
        cls.user=cls.getUserNm()
        cls.pas=cls.getPass()
        # Open database connection
        cls.db = MySQLdb.connect("localhost",cls.user,cls.pas,"marks2" )
        # prepare a cursor object using cursor() method
        cls.cursor = cls.db.cursor()
        # Prepare SQL query to UPDATE required records
        names=[]
        names=cls.ReadNames()
        print names
        for x in names:
            cls.sql1="INSERT INTO %s "%(str(Tbl))+"(nm, Test1, Test2, Test3, Test4, Test5, Test6,Test7, Test8, Test9, Test10,Test11, Test12,Test13, Test14, Test15, pred) VALUES ('%s',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)"%(str(x))
            try:
               # Execute the SQL command
               print cls.sql1
               cls.cursor.execute(cls.sql1)
               # Commit your changes in the database
               cls.db.commit()
            except:
               cls.Er="not null"
               #Rollback in case there is any error
               cls.db.rollback()
               print "Error: unable to EnterMarks"
               Example().onError()
        Example().onInfo()

    def Fun(cls):
        TableNm = cls.e1.get()
        Yr = cls.e2.get()
        cls.CreatTable(TableNm)
    def Fun2(cls):
        TableNm = cls.e1.get()
        cls.ScanNames(TableNm)

root = Tk()
my_gui =NewSub(root)
root.mainloop()

