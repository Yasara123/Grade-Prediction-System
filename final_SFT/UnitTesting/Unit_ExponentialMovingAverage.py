__author__ = 'Yas'
import MySQLdb
#import matplotlib.pyplot as plt
import numpy as np
import warnings
from numpy.lib.stride_tricks import as_strided
import unittest
def f(student,testNo):
    # Open database connection
    db = MySQLdb.connect("localhost","root","sri","marks" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM  cs2022  WHERE StudentName= '%s'" % (student)
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
          #aTest7 = row[7]
          #aTest8 = row[8]
          #aTest9 = row[9]
          #aTest10 = row[10]
         # aTest11 = row[11]
          #aTest12 = row[12]

          # Now print fetched result
          #print "StudentName=%s,Test1=%d,Test2=%d,Test3=%d,Test4=%d,Test5=%d,Test6=%d,Test7=%d,Test8=%d,Test9=%d,Test10=%d,Test11=%d,Test12=%d" % \
               #  (aStudentName, aTest1, aTest2, aTest3, aTest4, aTest5, aTest6, aTest7, aTest8, aTest9, aTest10, aTest11, aTest12)
    except:
       print "Error: unable to fecth data"

    db.close()

    warnings.simplefilter('ignore', np.RankWarning)
    #x = np.array([1,2,3,4,5,6,7,8,9,10,11])
    #y =np.array([aTest1, aTest2, aTest3, aTest4, aTest5, aTest6, aTest7, aTest8, aTest9, aTest10,aTest11])
    x = np.array([1,2,3,4,5,6])
    y =np.array([aTest1, aTest2, aTest3, aTest4, aTest5, aTest6])
    #plt.plot(x,y,'ro',alpha=0.3,ms=4,label='data')
    #plt.xlabel('Time')
    #plt.ylabel('Intensity')

    #define a moving average function
    def moving_average(x,y,step_size=0.1,bin_size=7):
        bin_centers  = np.arange(np.min(x),np.max(x)-0.5*step_size,step_size)+0.5*step_size
        bin_avg = np.zeros(len(bin_centers))

        for index in range(0,len(bin_centers)):
            bin_center = bin_centers[index]
            items_in_bin = y[(x>(bin_center-bin_size*0.5) ) & (x<(bin_center+bin_size*0.5))]
            bin_avg[index] = np.mean(items_in_bin)

        return bin_centers,bin_avg
    def moving_weighted_average(x, y, step_size=.1, steps_per_bin=10,weights=None):
        # This ensures that all samples are within a bin
        number_of_bins = int(np.ceil(np.ptp(x) / step_size))
        bins = np.linspace(np.min(x), np.min(x) + step_size*number_of_bins,
                           num=number_of_bins+1)
        bins -= (bins[-1] - np.max(x)) / 2
        bin_centers = bins[:-steps_per_bin] + step_size*steps_per_bin/2

        counts, _ = np.histogram(x, bins=bins)
        vals, _ = np.histogram(x, bins=bins, weights=y)
        bin_avgs = vals / counts
        n = len(bin_avgs)
        windowed_bin_avgs = as_strided(bin_avgs,
                                       (n-steps_per_bin+1, steps_per_bin),
                                       bin_avgs.strides*2)

        weighted_average = np.average(windowed_bin_avgs, axis=1, weights=weights)

        return bin_centers, weighted_average
    #plot the moving average
    bins, average = moving_average(x,y)
    #plt.plot(bins, average,label='moving average')
    weights=np.array([0,1,1,1,1,5])

    bins1, average1 = moving_weighted_average(x, y,0.1 ,len(weights),weights)
    #plt.xlim(1,14)
    #plt.ylim(0,100)
    z = np.polyfit(bins, average, 3)
    p = np.poly1d(z)
    #plt.ylabel('Marks 100%')
   # plt.xlabel('Test Number')
    #plt.title('Exponential Moving Average')
    #plt.show()
    #print aStudentName
    #print int(p(int(testNo)))
    #return int(p(int(testNo)))
    if int(p(int(testNo))) <=100:
        #print "predicted value  for ",student," is ",int(p(int(testNo)))
        return int(p(int(testNo)))
    else:
        #print "predicted value  for ",student," is ",100
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