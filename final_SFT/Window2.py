__author__ = 'Yas'
from Tkinter import *
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import warnings

master = Tk()
master.geometry("350x100+300+300")
Label(master, text="Enter your name").grid(row=0)
Label(master, text="Module code:").grid(row=1) # cs2202
e1 = Entry(master)
e4 = Entry(master)
e1.grid(row=0, column=1)
e4.grid(row=3, column=1)
def plot():
    student = e1.get()#"Padama"
    code = e4.get()# cs2202
    print code,student
    # Open database connection
    db = MySQLdb.connect("localhost","root","sri","marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM  %s  WHERE StudentName='%s'"%(code,student)
    try:
         # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            aStudentName= row[0]
            aTest1 = row[1]
            aTest2 = row[2]
            aTest3 = row[3]
            aTest4 = row[4]
            aTest5 = row[5]
            aTest6 = row[6]
            aTest7 = row[7]
            aTest8 = row[8]
            aTest9 = row[9]
            aTest10 = row[10]
            # Now print fetched result
            print "StudentName=%s,Test1=%d,Test2=%d,Test3=%d,Test4=%d,Test5=%d,Test6=%d,Test7=%d,Test8=%d,Test9=%d,Test10=%d" % \
             (aStudentName, aTest1, aTest2, aTest3, aTest4, aTest5, aTest6, aTest7, aTest8, aTest9, aTest10 )
    except:
        print "Error: unable to fecth data"
    db.close()
    warnings.simplefilter('ignore', np.RankWarning)
    x = np.array([1,2,3,4,5,6,7,8,9,10])
    y = np.array( [aTest1, aTest2, aTest3, aTest4, aTest5, aTest6, aTest7, aTest8, aTest9, aTest10])
    plt.plot(x, y,'b')
    plt.show()
Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='plot', command=plot).grid(row=5, column=2, sticky=W, pady=4)
mainloop( )
