__author__ = 'Yas'
#!/usr/bin/python

import MySQLdb
import matplotlib.pyplot as plt
import unittest

def f(student,NoStd):
    # Open database connection
    db = MySQLdb.connect("localhost","root","sri","marks" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    #for i in range(len(student)):
        #sql = "SELECT * FROM cs2202 \
           #WHERE StudentName= '%s'" % (student[i])
    sql = "SELECT * FROM cs2202 \
           WHERE StudentName= '%s'" % (student[0])
    sql2 = "SELECT * FROM cs2202 \
           WHERE StudentName= '%s'" % (student[1])
    sql3 = "SELECT * FROM cs2202 \
          WHERE StudentName= '%s'" % (student[2])
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
    try:
       # Execute the SQL command
       cursor.execute(sql2)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          nStudentName= row[0]
          nTest1 = row[1]
          nTest2 = row[2]
          nTest3 = row[3]
          nTest4 = row[4]
          nTest5 = row[5]
          nTest6 = row[6]
          nTest7 = row[7]
          nTest8 = row[8]
          nTest9 = row[9]
          nTest10 = row[10]
          # Now print fetched result
          print "StudentName=%s,Test1=%d,Test2=%d,Test3=%d,Test4=%d,Test5=%d,Test6=%d,Test7=%d,Test8=%d,Test9=%d,Test10=%d" % \
                 (nStudentName, nTest1, nTest2, nTest3, nTest4, nTest5, nTest6, nTest7, nTest8, nTest9, nTest10 )
    except:
       print "Error: unable to fecth data"
    try:
       # Execute the SQL command
       cursor.execute(sql3)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          StudentName= row[0]
          Test1 = row[1]
          Test2 = row[2]
          Test3 = row[3]
          Test4 = row[4]
          Test5 = row[5]
          Test6 = row[6]
          Test7 = row[7]
          Test8 = row[8]
          Test9 = row[9]
          Test10 = row[10]
          # Now print fetched result
          print "StudentName=%s,Test1=%d,Test2=%d,Test3=%d,Test4=%d,Test5=%d,Test6=%d,Test7=%d,Test8=%d,Test9=%d,Test10=%d" % \
                 (StudentName, Test1, Test2, Test3, Test4, Test5, Test6, Test7, Test8, Test9, Test10 )
    except:
       print "Error: unable to fecth data"

    # disconnect from server
    db.close()

    plt.plot([1,2,3,4,5,6,7,8,9,10], [int((Test1+nTest1+aTest1)/3), int((Test2+nTest2+aTest2)/3), int((Test3+nTest3+aTest3)/3), int((Test4+nTest4+aTest4)/3), int((Test5+nTest5+aTest5)/3), int((Test6+nTest6+aTest6)/3),int((Test7+nTest7+aTest7)/3), int((Test8+nTest8+aTest8)/3), int((Test9+nTest9+aTest9)/3), int((Test10+nTest10+aTest10)/3)], 'g')
    plt.axis([1, 12, 0, 100])
    plt.ylabel('Marks 100%')
    plt.xlabel('Test Number')
    plt.title('Over All Bach Result in all test')
    plt.show()
    return 0
#unit testing
class MyTest(unittest.TestCase):
    def test(self):
        #self.assertEqual(f(["Padama","M.D.N Dilini","A.Y Dissanayake"],3),0)
        self.assertEqual(f(['Padama','M.D.N Dilini','A.Y Dissanayake'],3),0)