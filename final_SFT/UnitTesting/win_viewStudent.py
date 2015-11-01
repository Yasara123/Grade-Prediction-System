__author__ = 'Yas'
from Tkinter import *
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import warnings
from PIL import Image, ImageTk
import os
import numpy
master = Tk()
master.configure(background='#8A002E')
img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
imglabel = Label(master, image=img).grid(row=0, column=3)
master.wm_title("Student Progress")

Label(master,background='#8A002E',foreground="white", text="Enter your name").grid(row=1)
Label(master,background='#8A002E',foreground="white", text="Module code:").grid(row=2) # cs2202
e1 = Entry(master)
e4 = Entry(master)
e1.grid(row=1, column=1)
e4.grid(row=2, column=1)
def getUserNm():
  tem=[]
  with open('Config.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  f.close()
  return tem[2]
#get password
def getPass():
  tem=[]
  with open('Config.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  f.close()
  return tem[3]

def plot():
    student = e1.get()#"Padama"
    code = e4.get()# cs2202
    user=getUserNm()
    pas=getPass()
    #print code,student
    # Open database connection
    db = MySQLdb.connect("localhost",user,pas,"marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM  %s"%(code)+" WHERE StudentName='%s'"%(student)
    try:
         # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        test=[]
        index=[]
        for row in results:
            aStudentName= row[0]
            if len(row)>2:
                aTest1 = row[1]
                test.append(aTest1)
                index.append(1)
            if len(row)>3:
                aTest2 = row[2]
                test.append(aTest2)
                index.append(2)
            if len(row)>4:
                aTest3 = row[3]
                test.append(aTest3)
                index.append(3)
            if len(row)>5:
                aTest4 = row[4]
                test.append(aTest4)
                index.append(4)
            if len(row)>6:
                aTest5 = row[5]
                test.append(aTest5)
                index.append(5)
            if len(row)>7:
                aTest6 = row[6]
                test.append(aTest6)
                index.append(6)
            if len(row)>8:
                aTest7 = row[7]
                test.append(aTest7)
                index.append(7)
            if len(row)>9:
                aTest8 = row[8]
                test.append(aTest8)
                index.append(8)
            if len(row)>10:
                aTest9 = row[9]
                test.append(aTest9)
                index.append(9)
            if len(row)>11:
                aTest10 = row[10]
                test.append(aTest10)
                index.append(10)
            if len(row)>12:
                aTest11 = row[11]
                test.append(aTest11)
                index.append(11)
            if len(row)>13:
                aTest12 = row[12]
                test.append(aTest12)
                index.append(12)
            if len(row)>14:
                aTest13 = row[13]
                test.append(aTest13)
                index.append(13)
            if len(row)>15:
                aTest14= row[14]
                test.append(aTest14)
                index.append(14)
            if len(row)>16:
                aTest15 = row[15]
                test.append(aTest15)
                index.append(15)

    except:
        print "Error: unable to fecth data"
    db.close()
    warnings.simplefilter('ignore', np.RankWarning)
    x = np.array(index)
    y = np.array( test)
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(numpy.arange(1,15,1.0))
    ax.set_yticks(numpy.arange(0,110.,5.0))
    plt.plot(x, y,'b')
    plt.ylim(0,120)
    plt.xlim(1,15)
    plt.title(aStudentName+"'s Progress")
    plt.grid()
    plt.show()
#----------------------------------------
def back():
   master.withdraw()
   os.system('python win_StudentData.py')

#----------------------------------------
Button(master, text='Back', command=back).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='plot', command=plot).grid(row=3, column=2, sticky=W, pady=4)
mainloop( )
