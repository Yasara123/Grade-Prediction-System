from Tkinter import *
import MySQLdb
from ttk import Frame, Button, Style
from Tkinter import Tk
import base64
import tkMessageBox as box
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
sub=[]
sub1=[]
sub2=[]
NoStd=40
CA=0
CB=0
CC=0
CF=0
#----------------------------------------------------------
def getSub1():
  #Software ENG result of a batch
  with open('NewSub.txt','r') as f:
    for line in f:
        for word in line.split():
           sub1.append(word)
#----------------------------------------------------------
def getSub():
    #OOP marks of previous batch
  with open('PreSub1.txt','r') as f:
    for line in f:
        for word in line.split():
           sub.append(word)
#----------------------------------------------------------
def fun1():
    CAA1=0
    CAA2=0
    CAA3=0
    CAB1=0
    CAB2=0
    CAB3=0
    CAC1=0
    CAC2=0
    CAC3=0
    CAF=0
    CBA1=0
    CBA2=0
    CBA3=0
    CBB1=0
    CBB2=0
    CBB3=0
    CBC1=0
    CBC2=0
    CBC3=0
    CBF=0
    CCA1=0
    CCA2=0
    CCA3=0
    CCB1=0
    CCB2=0
    CCB3=0
    CCC1=0
    CCC2=0
    CCC3=0
    CCF=0
    CFA1=0
    CFA2=0
    CFA3=0
    CFB1=0
    CFB2=0
    CFB3=0
    CFC1=0
    CFC2=0
    CFC3=0
    CFF=0
    for i in range(0,NoStd):
        if sub1[i]=="A":
            #for j in range(0,NoStd):
            if sub[i]=="A+":
                CAA1=int(int(CAA1)+1)
            if sub[i]=="A":
                CAA2=int(int(CAA2)+1)
            if sub[i]=="A-":
                CAA3=int(int(CAA3)+1)
            if sub[i]=="B+":
                CAB1=int(int(CAB1)+1)
            if sub[i]=="B":
                CAB2=int(int(CAB2)+1)
            if sub[i]=="B-":
                CAB3=int(int(CAB3)+1)
            if sub[i]=="C+":
                CAC1=int(int(CAC1)+1)
            if sub[i]=="C":
                CAC2=int(int(CAC2)+1)
            if sub[i]=="C-":
                CAC3=int(int(CAC3)+1)
            if sub[i]=="F":
                CAF=int(int(CAF)+1)
        if sub1[i]=='B':
                #for j in range(0,NoStd):
            if sub[i]=="A+":
                CBA1=int(int(CBA1)+1)
            if sub[i]=="A":
                CBA2=int(int(CBA2)+1)
            if sub[i]=="A-":
                CBA3=int(int(CBA3)+1)
            if sub[i]=="B+":
                CBB1=int(int(CBB1)+1)
            if sub[i]=="B":
                CBB2=int(int(CBB2)+1)
            if sub[i]=="B-":
                CBB3=int(int(CBB3)+1)
            if sub[i]=="C+":
                CBC1=int(int(CBC1)+1)
            if sub[i]=="C":
                CBC2=int(int(CBC2)+1)
            if sub[i]=="C-":
                CBC3=int(int(CBC3)+1)
            if sub[i]=='F':
                CBF=int(int(CBF)+1)
              #  print "B"
                #print i
        if sub1[i]=='C':
                #for j in range(0,NoStd):
                if sub[i]=="A+":
                    CCA1=CCA1+1
                if sub[i]=="A":
                    CCA2=CCA2+1
                if sub[i]=="A-":
                    CCA3=CCA3+1
                if sub[i]=="B+":
                    CCB1=CCB1+1
                if sub[i]=="B":
                    CCB2=CCB2+1
                if sub[i]=="B-":
                    CCB3=CCB3+1
                if sub[i]=="C+":
                    CCC1=CCC1+1
                if sub[i]=="C":
                    CCC2=CCC2+1
                if sub[i]=="C-":
                    CCC3=CCC3+1
                if sub[i]=='F':
                    CCF=CCF+1
               # print "C"
              #  print i
        if sub1[i]=='F':
                if sub[i]=="A+":
                    CFA1=CFA1+1
                if sub[i]=="A":
                    CFA2=CFA2+1
                if sub[i]=="A-":
                    CFA3=CFA3+1
                if sub[i]=="B+":
                    CFB1=CFB1+1
                if sub[i]=="B":
                    CFB2=CFB2+1
                if sub[i]=="B-":
                    CFB3=CFB3+1
                if sub[i]=="C+":
                    CFC1=CFC1+1
                if sub[i]=="C":
                    CFC2=CFC2+1
                if sub[i]=="C-":
                    CFC3=CFC3+1
                if sub[i]=='F':
                    CFF=CFF+1
    f = open('sub1Test.txt',"w")
    if (int(CAA1)+int(CAA2)+int(CAA3)+int(CAB1)+int(CAB2)+int(CAB3)+int(CAC1)+int(CAC2)+int(CAC3)+int(CAF))!=0:
        f.write(str((float(CAA1))/(int(CAA1)+int(CAA2)+int(CAA3)+int(CAB1)+int(CAB2)+int(CAB3)+int(CAC1)+int(CAC2)+int(CAC3)+int(CAF))))
        f.write(" ")
        f.write(str((float(CAA2))/(int(CAA1)+int(CAA2)+int(CAA3)+int(CAB1)+int(CAB2)+int(CAB3)+int(CAC1)+int(CAC2)+int(CAC3)+int(CAF))))
        f.write(" ")
        f.write(str((float(CAA3))/(int(CAA1)+int(CAA2)+int(CAA3)+int(CAB1)+int(CAB2)+int(CAB3)+int(CAC1)+int(CAC2)+int(CAC3)+int(CAF))))
        f.write(" ")
        f.write(str((float(CAB1))/(int(CAA1)+int(CAA2)+int(CAA3)+int(CAB1)+int(CAB2)+int(CAB3)+int(CAC1)+int(CAC2)+int(CAC3)+int(CAF))))
        f.write(" ")
        f.write(str((float(CAB2))/(int(CAA1)+int(CAA2)+int(CAA3)+int(CAB1)+int(CAB2)+int(CAB3)+int(CAC1)+int(CAC2)+int(CAC3)+int(CAF))))
        f.write(" ")
        f.write(str((float(CAB3))/(int(CAA1)+int(CAA2)+int(CAA3)+int(CAB1)+int(CAB2)+int(CAB3)+int(CAC1)+int(CAC2)+int(CAC3)+int(CAF))))
        f.write(" ")
        f.write(str((float(CAC1))/(int(CAA1)+int(CAA2)+int(CAA3)+int(CAB1)+int(CAB2)+int(CAB3)+int(CAC1)+int(CAC2)+int(CAC3)+int(CAF))))
        f.write(" ")
        f.write(str((float(CAC2))/(int(CAA1)+int(CAA2)+int(CAA3)+int(CAB1)+int(CAB2)+int(CAB3)+int(CAC1)+int(CAC2)+int(CAC3)+int(CAF))))
        f.write(" ")
        f.write(str((float(CAC3))/(int(CAA1)+int(CAA2)+int(CAA3)+int(CAB1)+int(CAB2)+int(CAB3)+int(CAC1)+int(CAC2)+int(CAC3)+int(CAF))))
        f.write(" ")
        f.write(str((float(CAF))/(int(CAA1)+int(CAA2)+int(CAA3)+int(CAB1)+int(CAB2)+int(CAB3)+int(CAC1)+int(CAC2)+int(CAC3)+int(CAF))))
        f.write("\n")
    else:
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write("\n")
        #--------------------------------------------
    if (int(CBA1)+int(CBA2)+int(CBA3)+int(CBB1)+int(CBB2)+int(CBB3)+int(CBC1)+int(CBC2)+int(CBC3)+int(CBF))!=0:
        f.write(str((float(CBA1))/(int(CBA1)+int(CBA2)+int(CBA3)+int(CBB1)+int(CBB2)+int(CBB3)+int(CBC1)+int(CBC2)+int(CBC3)+int(CBF))))
        f.write(" ")
        f.write(str((float(CBA2))/(int(CBA1)+int(CBA2)+int(CBA3)+int(CBB1)+int(CBB2)+int(CBB3)+int(CBC1)+int(CBC2)+int(CBC3)+int(CBF))))
        f.write(" ")
        f.write(str((float(CBA3))/(int(CBA1)+int(CBA2)+int(CBA3)+int(CBB1)+int(CBB2)+int(CBB3)+int(CBC1)+int(CBC2)+int(CBC3)+int(CBF))))
        f.write(" ")
        f.write(str((float(CBB1))/(int(CBA1)+int(CBA2)+int(CBA3)+int(CBB1)+int(CBB2)+int(CBB3)+int(CBC1)+int(CBC2)+int(CBC3)+int(CBF))))
        f.write(" ")
        f.write(str((float(CBB2))/(int(CBA1)+int(CBA2)+int(CBA3)+int(CBB1)+int(CBB2)+int(CBB3)+int(CBC1)+int(CBC2)+int(CBC3)+int(CBF))))
        f.write(" ")
        f.write(str((float(CBB3))/(int(CBA1)+int(CBA2)+int(CBA3)+int(CBB1)+int(CBB2)+int(CBB3)+int(CBC1)+int(CBC2)+int(CBC3)+int(CBF))))
        f.write(" ")
        f.write(str((float(CBC1))/(int(CBA1)+int(CBA2)+int(CBA3)+int(CBB1)+int(CBB2)+int(CBB3)+int(CBC1)+int(CBC2)+int(CBC3)+int(CBF))))
        f.write(" ")
        f.write(str((float(CBC2))/(int(CBA1)+int(CBA2)+int(CBA3)+int(CBB1)+int(CBB2)+int(CBB3)+int(CBC1)+int(CBC2)+int(CBC3)+int(CBF))))
        f.write(" ")
        f.write(str((float(CBC3))/(int(CBA1)+int(CBA2)+int(CBA3)+int(CBB1)+int(CBB2)+int(CBB3)+int(CBC1)+int(CBC2)+int(CBC3)+int(CBF))))
        f.write(" ")
        f.write(str((float(CBF))/(int(CBA1)+int(CBA2)+int(CBA3)+int(CBB1)+int(CBB2)+int(CBB3)+int(CBC1)+int(CBC2)+int(CBC3)+int(CBF))))
        f.write("\n")
    else:
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write("\n")
        #--------------------------------------------
    if (int(CCA1)+int(CCA2)+int(CCA3)+int(CCB1)+int(CCB2)+int(CCB3)+int(CCC1)+int(CCC2)+int(CCC3)+int(CCF))!=0:
        f.write(str((float(CCA1))/(int(CCA1)+int(CCA2)+int(CCA3)+int(CCB1)+int(CCB2)+int(CCB3)+int(CCC1)+int(CCC2)+int(CCC3)+int(CCF))))
        f.write(" ")
        f.write(str((float(CCA2))/(int(CCA1)+int(CCA2)+int(CCA3)+int(CCB1)+int(CCB2)+int(CCB3)+int(CCC1)+int(CCC2)+int(CCC3)+int(CCF))))
        f.write(" ")
        f.write(str((float(CCA3))/(int(CCA1)+int(CCA2)+int(CCA3)+int(CCB1)+int(CCB2)+int(CCB3)+int(CCC1)+int(CCC2)+int(CCC3)+int(CCF))))
        f.write(" ")
        f.write(str((float(CCB1))/(int(CCA1)+int(CCA2)+int(CCA3)+int(CCB1)+int(CCB2)+int(CCB3)+int(CCC1)+int(CCC2)+int(CCC3)+int(CCF))))
        f.write(" ")
        f.write(str((float(CCB2))/(int(CCA1)+int(CCA2)+int(CCA3)+int(CCB1)+int(CCB2)+int(CCB3)+int(CCC1)+int(CCC2)+int(CCC3)+int(CCF))))
        f.write(" ")
        f.write(str((float(CCB3))/(int(CCA1)+int(CCA2)+int(CCA3)+int(CCB1)+int(CCB2)+int(CCB3)+int(CCC1)+int(CCC2)+int(CCC3)+int(CCF))))
        f.write(" ")
        f.write(str((float(CCC1))/(int(CCA1)+int(CCA2)+int(CCA3)+int(CCB1)+int(CCB2)+int(CCB3)+int(CCC1)+int(CCC2)+int(CCC3)+int(CCF))))
        f.write(" ")
        f.write(str((float(CCC2))/(int(CCA1)+int(CCA2)+int(CCA3)+int(CCB1)+int(CCB2)+int(CCB3)+int(CCC1)+int(CCC2)+int(CCC3)+int(CCF))))
        f.write(" ")
        f.write(str((float(CCC3))/(int(CCA1)+int(CCA2)+int(CCA3)+int(CCB1)+int(CCB2)+int(CCB3)+int(CCC1)+int(CCC2)+int(CCC3)+int(CCF))))
        f.write(" ")
        f.write(str((float(CCF))/(int(CCA1)+int(CCA2)+int(CCA3)+int(CCB1)+int(CCB2)+int(CCB3)+int(CCC1)+int(CCC2)+int(CCC3)+int(CCF))))
        f.write("\n")
    else:
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write("\n")
        #--------------------------------------------
    if (int(CFA1)+int(CFA2)+int(CFA3)+int(CFB1)+int(CFB2)+int(CFB3)+int(CFC1)+int(CFC2)+int(CFC3)+int(CFF))!=0:
        f.write(str((float(CFA1))/(int(CFA1)+int(CFA2)+int(CFA3)+int(CFB1)+int(CFB2)+int(CFB3)+int(CFC1)+int(CFC2)+int(CFC3)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFA2))/(int(CFA1)+int(CFA2)+int(CFA3)+int(CFB1)+int(CFB2)+int(CFB3)+int(CFC1)+int(CFC2)+int(CFC3)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFA3))/(int(CFA1)+int(CFA2)+int(CFA3)+int(CFB1)+int(CFB2)+int(CFB3)+int(CFC1)+int(CFC2)+int(CFC3)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFB1))/(int(CFA1)+int(CFA2)+int(CFA3)+int(CFB1)+int(CFB2)+int(CFB3)+int(CFC1)+int(CFC2)+int(CFC3)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFB2))/(int(CFA1)+int(CFA2)+int(CFA3)+int(CFB1)+int(CFB2)+int(CFB3)+int(CFC1)+int(CFC2)+int(CFC3)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFB3))/(int(CFA1)+int(CFA2)+int(CFA3)+int(CFB1)+int(CFB2)+int(CFB3)+int(CFC1)+int(CFC2)+int(CFC3)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFC1))/(int(CFA1)+int(CFA2)+int(CFA3)+int(CFB1)+int(CFB2)+int(CFB3)+int(CFC1)+int(CFC2)+int(CFC3)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFC2))/(int(CFA1)+int(CFA2)+int(CFA3)+int(CFB1)+int(CFB2)+int(CFB3)+int(CFC1)+int(CFC2)+int(CFC3)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFC3))/(int(CFA1)+int(CFA2)+int(CFA3)+int(CFB1)+int(CFB2)+int(CFB3)+int(CFC1)+int(CFC2)+int(CFC3)+int(CFF))))
        f.write(" ")
        f.write(str((float(CFF))/(int(CFA1)+int(CFA2)+int(CFA3)+int(CFB1)+int(CFB2)+int(CFB3)+int(CFC1)+int(CFC2)+int(CFC3)+int(CFF))))
        f.write("\n")
    else:
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write(" ")
        f.write(str(0.1))
        f.write("\n")

    f.close()
    print "Sub 1 Prob Write"
#----------------------------------------------------------

def getprob(obs):
  tem=[]
  with open('sub1Test.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  sp=[[float(tem[0]),float(tem[1]),float(tem[2]),float(tem[3]),float(tem[4]),float(tem[5]),float(tem[6]),float(tem[7]),float(tem[8]),float(tem[9])],[float(tem[10]),float(tem[11]),float(tem[12]),float(tem[13]),float(tem[14]),float(tem[15]),float(tem[16]),float(tem[17]),float(tem[18]),float(tem[19])],[float(tem[20]),float(tem[21]),float(tem[22]),float(tem[23]),float(tem[24]),float(tem[25]),float(tem[26]),float(tem[27]),float(tem[28]),float(tem[29])],[float(tem[30]),float(tem[31]),float(tem[32]),float(tem[33]),float(tem[34]),float(tem[35]),float(tem[36]),float(tem[37]),float(tem[38]),float(tem[39])]]
  import Model_hhdn1
  val=Model_hhdn1.f(obs,sp)
  return val

import unittest
result=[]
class MyTest(unittest.TestCase):
    def test(self):
        result.append(getprob([0]))
        result.append(getprob([4]))
        result.append(getprob([5]))
        result.append(getprob([1]))
        result.append(getprob([0]))
        result.append(getprob([6]))
        result.append(getprob([3]))
        result.append(getprob([4]))
        result.append(getprob([4]))
        result.append(getprob([2]))
        result.append(getprob([3]))
        result.append(getprob([4]))
        result.append(getprob([1]))
        result.append(getprob([2]))
        result.append(getprob([5]))
        result.append(getprob([3]))
        result.append(getprob([9]))
        result.append(getprob([4]))
        result.append(getprob([3]))
        result.append(getprob([3]))
        result.append(getprob([2]))
        result.append(getprob([4]))
        result.append(getprob([2]))
        result.append(getprob([5]))
        result.append(getprob([4]))
        result.append(getprob([6]))
        result.append(getprob([5]))
        result.append(getprob([8]))
        result.append(getprob([3]))
        result.append(getprob([8]))
        result.append(getprob([6]))
        result.append(getprob([3]))
        result.append(getprob([1]))
        result.append(getprob([4]))
        result.append(getprob([0]))
        result.append(getprob([2]))
        result.append(getprob([3]))
        result.append(getprob([3]))
        result.append(getprob([5]))
        result.append(getprob([2]))
        result.append(getprob([3]))
        real=[0,1,2,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,0,1,1,0,1,0]
        x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]
        plt.xlim(0,42)
        plt.ylim(-1,5)
        plt.plot(x,real, 'r')
        print result
        plt.plot(x,result, 'b')
        plt.show()

