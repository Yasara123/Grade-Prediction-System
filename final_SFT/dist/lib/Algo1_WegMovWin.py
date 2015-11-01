import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import warnings
from numpy.lib.stride_tricks import as_strided
'''
This is the main funtions of the system and this have functional options. They are:
This is the 1 st algorithem which called weighted Moving Regression Model
This use the predict the students result at the examination using series of CA marks
By testing with the actual data this gives more accurate prediction when data has gradualy dicreasing variation.
So getting more accurate prediction this woud be helpful.
And also even there is few data poits it gives more accurate ptrediction
'''
# get the password from the confuguratin file
def getUserNm():
  tem=[]
  with open('Config.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  f.close()
  return tem[2]
# get the password from the confuguratin file
def getPass():
  tem=[]
  with open('Config.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  f.close()
  return tem[3]

# get preced value with the given subject
def f(student,testNo,code,call):
    user=getUserNm()
    pas=getPass()
    # Open database connection
    db = MySQLdb.connect("localhost",user,pas,"marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM %s "%(code)+"  WHERE StudentName= '%s'" % (student)

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
    if call=="1":
        plt.plot(x,y,'ro',alpha=0.3,ms=4,label='data')
        plt.xlabel('Time')
        plt.ylabel('Intensity')
    '''
    This define a moving average function
    '''
    def moving_average(x,y,step_size=0.1,bin_size=7):
        bin_centers  = np.arange(np.min(x),np.max(x)-0.5*step_size,step_size)+0.5*step_size
        bin_avg = np.zeros(len(bin_centers))

        for index in range(0,len(bin_centers)):
            bin_center = bin_centers[index]
            items_in_bin = y[(x>(bin_center-bin_size*0.5) ) & (x<(bin_center+bin_size*0.5))]
            bin_avg[index] = np.mean(items_in_bin)

        return bin_centers,bin_avg
    '''
    This is the assigment of weight to a idividual data item
    '''
    def moving_weighted_average(x, y, step_size=.1, steps_per_bin=10,weights=None):
        # This ensures that all samples are within a bin
        number_of_bins = int(np.ceil(np.ptp(x) / step_size))
        bins = np.linspace(np.min(x), np.min(x) + step_size*number_of_bins,
                           num=number_of_bins+1)
        bins -= (bins[-1] - np.max(x)) / 2
        bin_centers = bins[:-steps_per_bin] + step_size*steps_per_bin/2
		weights=np.array([1,1,1,1,1,1])
        counts, _ = np.histogram(x, bins=bins)
        vals, _ = np.histogram(x, bins=bins, weights=y)
        bin_avgs = vals / counts
        n = len(bin_avgs)
        windowed_bin_avgs = as_strided(bin_avgs,
                                       (n-steps_per_bin+1, steps_per_bin),
                                       bin_avgs.strides*2)
		#Assign weights to the system
        weighted_average = np.average(windowed_bin_avgs, axis=1, weights=weights)

        return bin_centers, weighted_average
    #plot the moving average
    bins, average = moving_average(x,y)
    if call=="1":
        plt.plot(bins, average,label='moving average')
    
    bins1, average1 = moving_weighted_average(x, y,0.1 ,len(weights),weights)
    if call=="1":
        plt.xlim(1,14)
        plt.ylim(0,100)
    z = np.polyfit(bins, average, 3)
    p = np.poly1d(z)

    print "predicted value for ",student," is ",int(p(int(testNo)))
    if call=="1":
        plt.ylabel('Marks 100%')
        plt.xlabel('Test Number')
        plt.title('Exponential Moving Average')
        plt.show()
    return int(p(int(testNo)))
