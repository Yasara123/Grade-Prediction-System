__author__ = 'Yas'
#!/usr/bin/python
import pandas
ewma = pandas.stats.moments.ewma
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import warnings
'''
This is the main funtions of the system and this have functional options. They are:
This is the 1 st algorithem which called weighted Average Regression Model
This use the predict the students result at the examination using series of CA marks
By testing with the actual data this gives more accurate prediction when data has slight variation.
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
    sql ="SELECT * FROM %s "%(code)+ "  WHERE StudentName= '%s'" % (student)

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
        plt.plot( x, y,alpha=0.4, label='Raw' )

    # take EWMA in both directions with a smaller span term
    fwd = ewma( y, span=15 ) # take EWMA in fwd direction
    bwd = ewma( y[::-1], span=15 ) # take EWMA in bwd direction
    c = np.vstack(( fwd, bwd[::-1] )) # lump fwd and bwd together
    c = np.mean( c, axis=0 ) # average

    z = np.polyfit(x, c, 3)
    p = np.poly1d(z)
    if call=="1":
        plt.plot( c, 'r')
        plt.ylabel('Marks 100%')
        plt.xlabel('Test Number')
        plt.title('Exponential Weighted Average')
        plt.show()
    return int(p(int(testNo)))