__author__ = 'Yas'
#!/usr/bin/python

from Tkinter import *
import MySQLdb
from ttk import Frame, Button, Style
from Tkinter import Tk
import matplotlib.pyplot as plt
import tkMessageBox as box

master = Tk()
Label(master, text="Enter Module Code:").grid(row=0)
Label(master, text="Enter Year:").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def f():
    Er="null"
    code = e1.get()
    year = e2.get()
    # Open database connection
    db = MySQLdb.connect("localhost","root","sri","marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to UPDATE required records
    sql = "SELECT StudentName FROM %s "% (code)
    cursor.execute(sql)
    results = cursor.fetchall()
    noStd=len(results)
    sql1 =  "SELECT * FROM cs2202 \
           WHERE StudentName= '%s'" % (results[0])
    cursor.execute(sql1)
    results2 = cursor.fetchall()
    i=0
    for list in results2:
        for x in list:
            if x is not None:
             i=i+1
    noTest=i-1
    test=[]
    no=[]
    for y in range(1, (noTest+1)):
        no.append(y)
    for x in range(0, (noStd)):
        test.append([])
        sql1 = "SELECT * FROM cs2202 WHERE StudentName= '%s'" % (results[x])
        cursor.execute(sql1)
        results2 = cursor.fetchall()
        row = results2[0]
        print row
        for y in range(1, (noTest+1)):
            print row[y]
            test[x].append(row[y])

    tot=[]
    summ=0
    for y in range(0, (noTest)):
        for x in range(0, (noStd)):
            summ=summ+int(test[x][y])
        tot.append(int(summ/noStd))
        summ=0
    # disconnect from server
    db.close()
    print len(tot)
    print len(no)
    plt.plot(no,tot)
    plt.axis([1, 12, 0, 100])
    plt.ylabel('Marks 100%')
    plt.xlabel('Test Number')
    plt.title('Over All Bach Result in all test')
    plt.show()
    return 0
Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='Submit', command=f).grid(row=5, column=2, sticky=W, pady=4)
mainloop( )
