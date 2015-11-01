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
    #sql = "SELECT * FROM cs2202 WHERE StudentName= '%s'" % ("Padama")
    #sql2 = "SELECT * FROM cs2202 WHERE StudentName= '%s'" % ("M.D.N Dilini")
    #sql3 = "SELECT * FROM cs2202  WHERE StudentName= '%s'" % ("A.Y Dissanayake")
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
          aTest11 = row[11]
          aTest12 = row[12]
          aTest13 = row[13]
          aTest14 = row[14]
          # Now print fetched result
          print "StudentName=%s,Test1=%d,Test2=%d,Test3=%d,Test4=%d,Test5=%d,Test6=%d,Test7=%d,Test8=%d,Test9=%d,Test10=%d,Test11=%d,Test12=%d,Test13=%d,Test14=%d" % \
                 (aStudentName, aTest1, aTest2, aTest3, aTest4, aTest5, aTest6, aTest7, aTest8, aTest9, aTest10, aTest11, aTest12, aTest13, aTest14 )
    except:
       print "Error: unable to fecth data"
    db.close()

    warnings.simplefilter('ignore', np.RankWarning)
    x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    y =np.array([aTest1, aTest2, aTest3, aTest4, aTest5, aTest6, aTest7, aTest8, aTest9, aTest10,aTest11, aTest12, aTest13, aTest14])
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

#unit testing
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(f("Padama",15),91)
        self.assertEqual(f("M.D.N Dilini",15),100)
        self.assertEqual(f("A.Y Dissanayake",15),22)
