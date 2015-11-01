__author__ = 'Yas'
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import warnings
import pandas, numpy as np
ewma = pandas.stats.moments.ewma
import unittest
def f(student,testNo):
    # Open database connection
    db = MySQLdb.connect("localhost","root","sri","marks" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM cs2022  WHERE StudentName= '%s'" % (student)
    #sql = "SELECT * FROM cs2202  WHERE StudentName= '%s'" % ("Padama")
    #sql2 = "SELECT * FROM cs2202 WHERE StudentName= '%s'" % ("M.D.N Dilini")
    #sql3 = "SELECT * FROM cs2202 WHERE StudentName= '%s'" % ("A.Y Dissanayake")
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
         # aTest7 = row[7]
         # aTest8 = row[8]
         # aTest9 = row[9]
         # aTest10 = row[10]
         # aTest11 = row[11]
         # aTest12 = row[12]

          # Now print fetched result
          #print "StudentName=%s,Test1=%d,Test2=%d,Test3=%d,Test4=%d,Test5=%d,Test6=%d,Test7=%d,Test8=%d,Test9=%d,Test10=%d,Test11=%d,Test12=%d" % \
              #   (aStudentName, aTest1, aTest2, aTest3, aTest4, aTest5, aTest6, aTest7, aTest8, aTest9, aTest10, aTest11, aTest12)
    except:
       print "Error: unable to fecth data"

    db.close()

    warnings.simplefilter('ignore', np.RankWarning)
   # x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
   # y =np.array([aTest1, aTest2, aTest3, aTest4, aTest5, aTest6, aTest7, aTest8, aTest9, aTest10,aTest11, aTest12])
    x = np.array([1,2,3,4,5,6])
    y =np.array([aTest1, aTest2, aTest3, aTest4, aTest5, aTest6])
    #plt.plot( x, y,alpha=0.4, label='Raw' )

    # take EWMA in both directions with a smaller span term
    fwd = ewma( y, span=15 ) # take EWMA in fwd direction
    bwd = ewma( y[::-1], span=15 ) # take EWMA in bwd direction
    c = np.vstack(( fwd, bwd[::-1] )) # lump fwd and bwd together
    c = np.mean( c, axis=0 ) # average

    z = np.polyfit(x, c, 3)
    p = np.poly1d(z)

    #plt.plot( c, 'r')
    #plt.ylabel('Marks 100%')
   # plt.xlabel('Test Number')
    #plt.title('Exponential Weighted Average')
    #plt.show()

    #print int(p(int(testNo)))
    if int(p(int(testNo))) <=100:
        #print "predicted value  for ",student," is ",int(p(int(testNo)))
        return int(p(int(testNo)))
    else:
        #print "predicted value  for ",student," is ",100
        return 100


    #return int(p(int(testNo)))

#unit testing
'''
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
        self.assertEqual(f("120006T",7),0)
        self.assertEqual(f("120010B",7),0)
        self.assertEqual(f("120025B",7),0)
        self.assertEqual(f("120028L",7),0)
        self.assertEqual(f("120195T",7),0)
        self.assertEqual(f("120128T",7),0)
        self.assertEqual(f("120132B",7),0)
        self.assertEqual(f("120162P",7),0)
        self.assertEqual(f("120165D",7),0)
        self.assertEqual(f("120182C",7),0)
'''