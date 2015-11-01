__author__ = 'Yas'
__author__ = 'Yas'
#!/usr/bin/python

import MySQLdb
#import matplotlib.pyplot as plt
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
    sql = "SELECT * FROM  cs2022  WHERE StudentName= '%s'" % (student)
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
          #aTest7 = row[7]
          #aTest8 = row[8]
         # aTest9 = row[9]
         # aTest10 = row[10]
         # aTest11 = row[11]
          #aTest12 = row[12]

          # Now print fetched result
        #  print "StudentName=%s,Test1=%d,Test2=%d,Test3=%d,Test4=%d,Test5=%d,Test6=%d,Test7=%d,Test8=%d,Test9=%d,Test10=%d,Test11=%d,Test12=%d" % \
             #    (aStudentName, aTest1, aTest2, aTest3, aTest4, aTest5, aTest6, aTest7, aTest8, aTest9, aTest10, aTest11, aTest1 )
    except:
       print "Error: unable to fecth data"
    db.close()

    warnings.simplefilter('ignore', np.RankWarning)
    #x = np.array([1,2,3,4,5,6,7,8,9,10,11])
    #y =np.array([aTest1, aTest2, aTest3, aTest4, aTest5, aTest6, aTest7, aTest8, aTest9, aTest10,aTest11])
    x = np.array([1,2,3,4,5,6])
    y =np.array([aTest1, aTest2, aTest3, aTest4, aTest5, aTest6])
    z = np.polyfit(x, y, 2)
    p = np.poly1d(z)
    #p30 = np.poly1d(np.polyfit(x, y, 10))
    #plt.ylim(0,100)
   # plt.xlim(1,16)
    #plt.plot(x, y,'b')
    #plt.plot( x, p(x),'r')
    #plt.ylabel('Marks 100%')
    #plt.xlabel('Test Number')
   # plt.title('Curve Fitting Diagram')
    #plt.plot( x, p30(x),'g')
    #plt.show()
    #print aStudentName
    #print int(p(int(testNo)))
    if int(p(int(testNo))) <=100:
        #print "predicted value  for ",student," is ",int(p(int(testNo)))
        return int(p(int(testNo)))
    else:
       # print "predicted value  for ",student," is ",100
        return 100

'''
#unit testing
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(f("120126K",13),0)
        self.assertEqual(f("120323L",13),0)
        self.assertEqual(f("120733T",13),0)
        self.assertEqual(f("120542G",13),0)
        self.assertEqual(f("120237C",13),0)
        self.assertEqual(f("120116F",13),0)
        self.assertEqual(f("120132B",13),0)
        self.assertEqual(f("120129X",13),0)
        self.assertEqual(f("120228B",13),0)
        self.assertEqual(f("120345F",13),0)

'''
'''
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(f("120006T",12),0)
        self.assertEqual(f("120026L",12),0)
        self.assertEqual(f("120028L",12),0)
        self.assertEqual(f("120029P",12),0)
        self.assertEqual(f("120111K",12),0)
        self.assertEqual(f("120427J",12),0)
        self.assertEqual(f("120526L",12),0)
        self.assertEqual(f("120594P",12),0)
'''