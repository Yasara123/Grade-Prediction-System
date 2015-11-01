__author__ = 'Yas'
__author__ = 'Yas'
#!/usr/bin/python

import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt2
import warnings
import unittest
def f(student,testNo):
    # Open database connection
    db = MySQLdb.connect("localhost","root","sri","marks" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM cs2202  WHERE StudentName= '%s'" % (student)

    try:
      # Execute the SQL command
      cursor.execute(sql)
      # Fetch all the rows in a list of lists.
      results = cursor.fetchall()
      row=results[0]
      i=0
      for x in row:
        if x is not None:
         i=i+1
      noTest=i-1
      row=results[0]
      aStudentName= row[0]
      test=[]
      no=[]
      for y in range(1, (noTest+1)):
       no.append(y)
      for y in range(1,noTest+1):
       test.append(int(row[y]))
          # Now print fetched result
    except:
       print "Error: unable to fecth data"
    db.close()

    warnings.simplefilter('ignore', np.RankWarning)
    x=np.array(no)
    y =np.array(test)
    #x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
   # y =np.array([aTest1, aTest2, aTest3, aTest4, aTest5, aTest6, aTest7, aTest8, aTest9, aTest10,aTest11, aTest12, aTest13, aTest14])
    z = np.polyfit(x, y, 3)
    p = np.poly1d(z)
    #p30 = np.poly1d(np.polyfit(x, y, 10))
    plt.ylim(0,100)
    plt.xlim(1,16)
    plt.plot(x, y,'b')
    plt.plot( x, p(x),'r')
    plt.ylabel('Marks 100%')
    plt.xlabel('Test Number')
    plt.title('Curve Fitting Diagram')
    #plt.plot( x, p30(x),'g')
    plt.show()

    if int(p(int(testNo))) <=100:
        print "predicted value  for ",student," is ",int(p(int(testNo)))
    else:
        print "predicted value  for ",student," is ",100


    if int(p(int(testNo))) <=100:
        return int(p(int(testNo)))
    else:
        return 100

