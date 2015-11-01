__author__ = 'Yas'
from Tkinter import *
import MySQLdb
from ttk import Frame, Button, Style
from Tkinter import Tk
import base64
import tkMessageBox as box
from PIL import Image, ImageTk
import os
import ConfigMemento
import User
'''
This is the Configuration class of the system. It verify the username and password by using config text file.
If user forgot the pass word he/she can change the new password and restore the password by restoring it.
At the 1st time user should enter the system by using username Yas and password sri.
Database password can be configure using this
'''
#Shows the Error massages
class Example():
    def onError(self):
        box.showerror("Error", "Could not Upadate")

    def onQuest(self):
        box.askquestion("Question", "Are you sure to quit?")

    def onInfo(self):
        box.showinfo("Information", "Upadate Sucessfully")
    def onInfo2(self):
        box.showinfo("Information", "Restored Sucessfully")
back=ConfigMemento.Pw_RollBack()

class conFig():
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
        cls.imglabel = Label(cls.master, image=cls.img).grid(row=0, column=4)

        cls.master.wm_title("System Configuration")
        Label(cls.master,background='#8A002E',foreground="white", text="Enter System UserName").grid(row=1)
        Label(cls.master,background='#8A002E',foreground="white", text="Enter System Password:").grid(row=2)
        Label(cls.master,background='#8A002E',foreground="white", text="Edit DB UserName").grid(row=3)
        Label(cls.master,background='#8A002E',foreground="white", text="Edit DB Passwor:").grid(row=4)
        Label(cls.master,background='#8A002E',foreground="white", text="No of Related Subjects:").grid(row=5)
        cls.e1 = Entry(cls.master)
        cls.e2 = Entry(cls.master)
        cls.e3 = Entry(cls.master)
        cls.e4 = Entry(cls.master)
        cls.e5 = Entry(cls.master)

        cls.e1.grid(row=1, column=1)
        cls.e2.grid(row=2, column=1)
        cls.e3.grid(row=3, column=1)
        cls.e4.grid(row=4, column=1)
        cls.e5.grid(row=5, column=1)

        Button(cls.master, text='Back', command=cls.Back).grid(row=7, column=0, sticky=W, pady=4)
        Button(cls.master, text='HELP', command=cls.HelpCon).grid(row=7, column=1, sticky=W, pady=4)
        Button(cls.master, text='Quit', command=cls.master.quit).grid(row=7, column=2, sticky=W, pady=4)
        Button(cls.master, text='Submit', command=cls.Fun).grid(row=7, column=3, sticky=W, pady=4)
        Button(cls.master, text='Config Model', command=cls.Fun2).grid(row=7, column=4, sticky=W, pady=4)
        Button(cls.master, text='Restore Config', command=cls.Restore).grid(row=6, column=4, sticky=W, pady=4)
    '''
    This is Write the Usernames Passwords  to the test file begin:=>
    '''
    #set username from file-------------------
    def setUserUsername(cls,user,f):
       f.write(base64.b64encode(user))
       f.write("\n")

    #set pass from file-------------------
    def setUserPassword(cls,pas,f):
       f.write(base64.b64encode(pas))
       f.write("\n")
    #set username from file-------------------
    def setSubNo(cls,SNo,f):
       f.write(SNo)
       f.write("\n")

    #set username from file-------------------
    def setDBUsername(cls,user,f):
       f.write(user)
       f.write("\n")

    #set pass from file-------------------
    def setDBPassword(cls,pas,f):
       f.write(pas)
       f.write("\n")
    '''
    This is the par which user can restore the pass word using memento design patern.
    Care taker will hanndle the restoring function
    memento class store the values
    '''
    def Restore(cls):
        t=[]
        stn=back.getState()
        print stn
        for word in stn.split():
               t.append(word)
        print t
        UserNM = str(t[2])
        PassWD = str(t[3])
        DBNM = str(t[0])
        DBWD = str(t[1])
        SNo=int(t[4])
        Us=User.User("Lecturer",str(UserNM),str(PassWD),str( SNo))
        f = open('Config.txt',"w")
        cls.setUserUsername(str(Us.getUsrNm()),f)
        cls.setUserPassword(str(Us.getPwd()),f)
        cls.setDBUsername(DBNM,f)
        cls.setDBPassword(DBWD,f)
        cls.setSubNo(str(Us.getNoSub()),f)
        cls.SetDB(DBNM,DBWD,UserNM,PassWD,SNo)
        Example().onInfo2()
        print "Restored Sucessfully"
    #setDB
    '''
    This is Write the passwords to the data base as a back ups
    '''
    def SetDB(cls,userDB,pasDB,userName,PassWd,SNo):
        name="Lecturer"
        db = MySQLdb.connect("localhost",userDB,pasDB,"marks2" )
        cursor = db.cursor()
        key="sri"
        Er=""
        state=str(userDB)+" "+str(pasDB)+" "+str(userName)+" "+str(PassWd)+" "+str(SNo)
        #This Is How The Memento class is woring
        back.addState(state)

        sql="UPDATE users set UserName='%s',PassWord=AES_ENCRYPT('%s','%s'),SNo='%d' WHERE Name='%s'"% (userName,key,PassWd,int(SNo),name);
        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
        except:
           Er="not null"
           #Rollback in case there is any error
           db.rollback()
           print "Error: unable to Inser data"
           Example().onError()
        if Er=="null":
         Example().onInfo()
        # disconnect from server
        db.close()
    '''
    GUI establishing function
    '''
    def Fun(cls):
        UserNM = cls.e1.get()
        PassWD = cls.e2.get()
        DBNM = cls.e3.get()
        DBWD = cls.e4.get()
        SNo=cls.e5.get()
        Us=User.User("Lecturer",str(UserNM),str(PassWD),str( SNo))
        f = open('Config.txt',"w")
        cls.setUserUsername(str(Us.getUsrNm()),f)
        cls.setUserPassword(str(Us.getPwd()),f)
        cls.setDBUsername(DBNM,f)
        cls.setDBPassword(DBWD,f)
        cls.setSubNo(str(Us.getNoSub()),f)
        cls.SetDB(DBNM,DBWD,UserNM,PassWD,SNo)
        if f==NONE:
            Example().onError()
        else:
            Example().onInfo()
        f.close()

root = Tk()
my_gui =conFig(root)
root.mainloop()
