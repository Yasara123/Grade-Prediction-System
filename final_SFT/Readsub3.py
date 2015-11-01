from Tkinter import *
import MySQLdb
from ttk import Frame, Button, Style
from Tkinter import Tk
import base64
import tkMessageBox as box
from PIL import Image, ImageTk
'''
This is the class for hidden marcov model which ralate to 3 previous subject  of the system.
This reads the calculated proberbility value in the text file at the configeration level
This is the class which create the model relationship
starting probabilities are assign to the state equal brobabilities Ex: [0.25, 0.25,0.25, 0.25]
Emmission proberbilities are assign more more gerneral way. It is if 2nd prediction is much closer of same to the second prediction
'''
sub=[]
sub1=[]
sub2=[]
sub3=[]
NoStd=40
CA=0
CB=0
CC=0
CF=0
#----------------------------------------------------------
def getSub1():
  co=0
  with open('data1.txt','r') as f:
    for line in f:
        co=co+1
        for word in line.split():
           sub1.append(word)
  #NoStd= co-1
#----------------------------------------------------------
def getSub2():
  with open('data2.txt','r') as f:
    for line in f:
        for word in line.split():
           sub2.append(word)
#----------------------------------------------------------
def getSub3():
  with open('data4.txt','r') as f:
    for line in f:
        for word in line.split():
           sub3.append(word)
#----------------------------------------------------------
def getSub():
  with open('data3.txt','r') as f:
    for line in f:
        for word in line.split():
           sub.append(word)
#----------------------------------------------------------
def fun1():
    CAA=0
    CAB=0
    CAC=0
    CAF=0
    CBA=0
    CBB=0
    CBC=0
    CBF=0
    CCA=0
    CCB=0
    CCC=0
    CCF=0
    CFA=0
    CFB=0
    CFC=0
    CFF=0
    for i in range(0,NoStd):

        if sub1[i]=='A':
            #for j in range(0,NoStd):
                if sub[i]=='A':
                    CAA=int(int(CAA)+1)
                if sub[i]=='B':
                        CAB=int(int(CAB)+1)
                if sub[i]=='C':
                        CAC=int(int(CAC)+1)
                if sub[i]=='F':
                        CAF=int(int(CAF)+1)
           # print "A"
            #print i
        if sub1[i]=='B':
                #for j in range(0,NoStd):
                if sub[i]=='A':
                    CBA=int(int(CBA)+1)
                if sub[i]=='B':
                    CBB=int(int(CBB)+1)
                if sub[i]=='C':
                    CBC=int(int(CBC)+1)
                if sub[i]=='F':
                    CBF=int(int(CBF)+1)
              #  print "B"
                #print i
        if sub1[i]=='C':
                #for j in range(0,NoStd):
                if sub[i]=='A':
                    CCA=CCA+1
                if sub[i]=='B':
                    CCB=CCB+1
                if sub[i]=='C':
                    CCC=CCC+1
                if sub[i]=='F':
                    CCF=CCF+1
               # print "C"
              #  print i
        if sub1[i]=='F':
                if sub[i]=='A':
                    CFA=CFA+1
                if sub[i]=='B':
                    CFB=CFB+1
                if sub[i]=='C':
                    CFC=CFC+1
                if sub[i]=='F':
                    CFF=CFF+1

              #  print i
        #elif sub[i]=='C':
               # CC=CC+1
        #elif sub[i]=='F':
               # CF=CF+1
    f = open('sub1Prob.txt',"w")
    if (int(CAA)+int(CBA)+int(CCA)+int(CFA))!=0:
        f.write(str((float(CAA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write(" ")
        f.write(str((float(CBA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write(" ")
        f.write(str((float(CCA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write(" ")
        f.write(str((float(CFA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    if (int(CAB)+int(CBB)+int(CCB)+int(CFB))!=0:
        f.write(str((float(CAB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write(" ")
        f.write(str((float(CBB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write(" ")
        f.write(str((float(CCB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write(" ")
        f.write(str((float(CFB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    if (int(CAC)+int(CBC)+int(CCC)+int(CFC))!=0:
        f.write(str((float(CAC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write(" ")
        f.write(str((float(CBC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write(" ")
        f.write(str((float(CCC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write(" ")
        f.write(str((float(CFC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    if (int(CAF)+int(CBF)+int(CCF)+int(CFF))!=0:
        f.write(str((float(CAF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write(" ")
        f.write(str((float(CBF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write(" ")
        f.write(str((float(CCF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    f.close()
    print "Sub 1 Prob Write"
#----------------------------------------------------------
def fun2():
    CAA=0
    CAB=0
    CAC=0
    CAF=0
    CBA=0
    CBB=0
    CBC=0
    CBF=0
    CCA=0
    CCB=0
    CCC=0
    CCF=0
    CFA=0
    CFB=0
    CFC=0
    CFF=0
    for i in range(0,NoStd):

        if sub2[i]=='A':
            #for j in range(0,NoStd):
                if sub[i]=='A':
                    CAA=int(int(CAA)+1)
                if sub[i]=='B':
                        CAB=int(int(CAB)+1)
                if sub[i]=='C':
                        CAC=int(int(CAC)+1)
                if sub[i]=='F':
                        CAF=int(int(CAF)+1)
           # print "A"
            #print i
        if sub2[i]=='B':
                #for j in range(0,NoStd):
                if sub[i]=='A':
                    CBA=int(int(CBA)+1)
                if sub[i]=='B':
                    CBB=int(int(CBB)+1)
                if sub[i]=='C':
                    CBC=int(int(CBC)+1)
                if sub[i]=='F':
                    CBF=int(int(CBF)+1)
              #  print "B"
                #print i
        if sub2[i]=='C':
                #for j in range(0,NoStd):
                if sub[i]=='A':
                    CCA=CCA+1
                if sub[i]=='B':
                    CCB=CCB+1
                if sub[i]=='C':
                    CCC=CCC+1
                if sub[i]=='F':
                    CCF=CCF+1
               # print "C"
              #  print i
        if sub2[i]=='F':
                if sub[i]=='A':
                    CFA=CFA+1
                if sub[i]=='B':
                    CFB=CFB+1
                if sub[i]=='C':
                    CFC=CFC+1
                if sub[i]=='F':
                    CFF=CFF+1

              #  print i
        #elif sub[i]=='C':
               # CC=CC+1
        #elif sub[i]=='F':
               # CF=CF+1
    f = open('sub2Prob.txt',"w")
    if (int(CAA)+int(CBA)+int(CCA)+int(CFA))!=0:
        f.write(str((float(CAA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write(" ")
        f.write(str((float(CBA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write(" ")
        f.write(str((float(CCA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write(" ")
        f.write(str((float(CFA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    if (int(CAB)+int(CBB)+int(CCB)+int(CFB))!=0:
        f.write(str((float(CAB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write(" ")
        f.write(str((float(CBB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write(" ")
        f.write(str((float(CCB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write(" ")
        f.write(str((float(CFB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    if (int(CAC)+int(CBC)+int(CCC)+int(CFC))!=0:
        f.write(str((float(CAC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write(" ")
        f.write(str((float(CBC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write(" ")
        f.write(str((float(CCC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write(" ")
        f.write(str((float(CFC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    if (int(CAF)+int(CBF)+int(CCF)+int(CFF))!=0:
        f.write(str((float(CAF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write(" ")
        f.write(str((float(CBF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write(" ")
        f.write(str((float(CCF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    f.close()
    print "Sub 2 Prob Write"
#----------------------------------------------------------
def fun3():
    CAA=0
    CAB=0
    CAC=0
    CAF=0
    CBA=0
    CBB=0
    CBC=0
    CBF=0
    CCA=0
    CCB=0
    CCC=0
    CCF=0
    CFA=0
    CFB=0
    CFC=0
    CFF=0
    for i in range(0,NoStd):

        if sub3[i]=='A':
            #for j in range(0,NoStd):
                if sub[i]=='A':
                    CAA=int(int(CAA)+1)
                if sub[i]=='B':
                        CAB=int(int(CAB)+1)
                if sub[i]=='C':
                        CAC=int(int(CAC)+1)
                if sub[i]=='F':
                        CAF=int(int(CAF)+1)
           # print "A"
            #print i
        if sub3[i]=='B':
                #for j in range(0,NoStd):
                if sub[i]=='A':
                    CBA=int(int(CBA)+1)
                if sub[i]=='B':
                    CBB=int(int(CBB)+1)
                if sub[i]=='C':
                    CBC=int(int(CBC)+1)
                if sub[i]=='F':
                    CBF=int(int(CBF)+1)
              #  print "B"
                #print i
        if sub3[i]=='C':
                #for j in range(0,NoStd):
                if sub[i]=='A':
                    CCA=CCA+1
                if sub[i]=='B':
                    CCB=CCB+1
                if sub[i]=='C':
                    CCC=CCC+1
                if sub[i]=='F':
                    CCF=CCF+1
               # print "C"
              #  print i
        if sub3[i]=='F':
                if sub[i]=='A':
                    CFA=CFA+1
                if sub[i]=='B':
                    CFB=CFB+1
                if sub[i]=='C':
                    CFC=CFC+1
                if sub[i]=='F':
                    CFF=CFF+1

              #  print i
        #elif sub[i]=='C':
               # CC=CC+1
        #elif sub[i]=='F':
               # CF=CF+1
    f = open('sub3Prob.txt',"w")
    if (int(CAA)+int(CBA)+int(CCA)+int(CFA))!=0:
        f.write(str((float(CAA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write(" ")
        f.write(str((float(CBA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write(" ")
        f.write(str((float(CCA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write(" ")
        f.write(str((float(CFA))/(int(CAA)+int(CBA)+int(CCA)+int(CFA))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    if (int(CAB)+int(CBB)+int(CCB)+int(CFB))!=0:
        f.write(str((float(CAB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write(" ")
        f.write(str((float(CBB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write(" ")
        f.write(str((float(CCB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write(" ")
        f.write(str((float(CFB))/(int(CAB)+int(CBB)+int(CCB)+int(CFB))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    if (int(CAC)+int(CBC)+int(CCC)+int(CFC))!=0:
        f.write(str((float(CAC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write(" ")
        f.write(str((float(CBC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write(" ")
        f.write(str((float(CCC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write(" ")
        f.write(str((float(CFC))/(int(CAC)+int(CBC)+int(CCC)+int(CFC))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    if (int(CAF)+int(CBF)+int(CCF)+int(CFF))!=0:
        f.write(str((float(CAF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write(" ")
        f.write(str((float(CBF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write(" ")
        f.write(str((float(CCF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFF))/(int(CAF)+int(CBF)+int(CCF)+int(CFF))))
        f.write("\n")
    else:
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write(" ")
        f.write(str(0.25))
        f.write("\n")
    f.close()
    print "Sub 3 Prob Write"

def getprob(obs):
  tem=[]
  with open('sub1Prob.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  with open('sub2Prob.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  with open('sub3Prob.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  sp=[[float(tem[0]),float(tem[1]),float(tem[2]),float(tem[3]),float(tem[16]),float(tem[17]),float(tem[18]),float(tem[19]),float(tem[32]),float(tem[33]),float(tem[34]),float(tem[35])],[float(tem[4]),float(tem[5]),float(tem[6]),float(tem[7]),float(tem[20]),float(tem[21]),float(tem[22]),float(tem[23]),float(tem[36]),float(tem[37]),float(tem[38]),float(tem[39])],[float(tem[8]),float(tem[9]),float(tem[10]),float(tem[11]),float(tem[24]),float(tem[25]),float(tem[26]),float(tem[27]),float(tem[40]),float(tem[41]),float(tem[42]),float(tem[43])],[float(tem[12]),float(tem[13]),float(tem[14]),float(tem[15]),float(tem[28]),float(tem[29]),float(tem[30]),float(tem[31]),float(tem[44]),float(tem[45]),float(tem[46]),float(tem[47])]]
  import Model_hhdn3
  Model_hhdn3.f(obs,sp)


