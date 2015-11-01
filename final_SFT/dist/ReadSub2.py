from Tkinter import *
import MySQLdb
from ttk import Frame, Button, Style
from Tkinter import Tk
import base64
import tkMessageBox as box
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
'''
This is the class for hidden marcov model which ralate to 2 previous subject  of the system.
This reads the calculated proberbility value in the text file at the configeration level
This is the class which create the model relationship
starting probabilities are assign to the state equal brobabilities Ex: [0.25, 0.25,0.25, 0.25]
Emmission proberbilities are assign more more gerneral way. It is if 2nd prediction is much closer of same to the second prediction
'''
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
def getSub2():
     #OOSD marks of previous batch
  with open('PreSub2.txt','r') as f:
    for line in f:
        for word in line.split():
           sub2.append(word)
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
def fun2():
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
            if sub2[i]=="A+":
                CAA1=int(int(CAA1)+1)
            if sub2[i]=="A":
                CAA2=int(int(CAA2)+1)
            if sub2[i]=="A-":
                CAA3=int(int(CAA3)+1)
            if sub2[i]=="B+":
                CAB1=int(int(CAB1)+1)
            if sub2[i]=="B":
                CAB2=int(int(CAB2)+1)
            if sub2[i]=="B-":
                CAB3=int(int(CAB3)+1)
            if sub2[i]=="C+":
                CAC1=int(int(CAC1)+1)
            if sub2[i]=="C":
                CAC2=int(int(CAC2)+1)
            if sub2[i]=="C-":
                CAC3=int(int(CAC3)+1)
            if sub2[i]=="F":
                CAF=int(int(CAF)+1)
        if sub1[i]=='B':
                #for j in range(0,NoStd):
            if sub2[i]=="A+":
                CBA1=int(int(CBA1)+1)
            if sub2[i]=="A":
                CBA2=int(int(CBA2)+1)
            if sub2[i]=="A-":
                CBA3=int(int(CBA3)+1)
            if sub2[i]=="B+":
                CBB1=int(int(CBB1)+1)
            if sub2[i]=="B":
                CBB2=int(int(CBB2)+1)
            if sub2[i]=="B-":
                CBB3=int(int(CBB3)+1)
            if sub2[i]=="C+":
                CBC1=int(int(CBC1)+1)
            if sub2[i]=="C":
                CBC2=int(int(CBC2)+1)
            if sub2[i]=="C-":
                CBC3=int(int(CBC3)+1)
            if sub2[i]=='F':
                CBF=int(int(CBF)+1)
              #  print "B"
                #print i
        if sub1[i]=='C':
                #for j in range(0,NoStd):
                if sub2[i]=="A+":
                    CCA1=CCA1+1
                if sub2[i]=="A":
                    CCA2=CCA2+1
                if sub2[i]=="A-":
                    CCA3=CCA3+1
                if sub2[i]=="B+":
                    CCB1=CCB1+1
                if sub2[i]=="B":
                    CCB2=CCB2+1
                if sub2[i]=="B-":
                    CCB3=CCB3+1
                if sub2[i]=="C+":
                    CCC1=CCC1+1
                if sub2[i]=="C":
                    CCC2=CCC2+1
                if sub2[i]=="C-":
                    CCC3=CCC3+1
                if sub2[i]=='F':
                    CCF=CCF+1
               # print "C"
              #  print i
        if sub1[i]=='F':
                if sub2[i]=="A+":
                    CFA1=CFA1+1
                if sub2[i]=="A":
                    CFA2=CFA2+1
                if sub2[i]=="A-":
                    CFA3=CFA3+1
                if sub2[i]=="B+":
                    CFB1=CFB1+1
                if sub2[i]=="B":
                    CFB2=CFB2+1
                if sub2[i]=="B-":
                    CFB3=CFB3+1
                if sub2[i]=="C+":
                    CFC1=CFC1+1
                if sub2[i]=="C":
                    CFC2=CFC2+1
                if sub2[i]=="C-":
                    CFC3=CFC3+1
                if sub2[i]=='F':
                    CFF=CFF+1
    f = open('sub2Test.txt',"w")
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
    print "Sub 2 Prob Write"
#----------------------------------------------------------

def getprob2(obs):
  tem=[]
  with open('sub1Test.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  with open('sub2Test.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  sp=[[float(tem[0])/2,float(tem[1])/2,float(tem[2])/2,float(tem[3])/2,float(tem[4])/2,float(tem[5])/2,float(tem[6])/2,float(tem[7])/2,float(tem[8])/2,float(tem[9])/2,float(tem[40])/2,float(tem[41])/2,float(tem[42])/2,float(tem[43])/2,float(tem[44])/2,float(tem[45])/2,float(tem[46])/2,float(tem[47])/2,float(tem[48])/2,float(tem[49])/2],[float(tem[10])/2,float(tem[11])/2,float(tem[12])/2,float(tem[13])/2,float(tem[14])/2,float(tem[15])/2,float(tem[16])/2,float(tem[17])/2,float(tem[18])/2,float(tem[19])/2,float(tem[50])/2,float(tem[51])/2,float(tem[52])/2,float(tem[53])/2,float(tem[54])/2,float(tem[55])/2,float(tem[56])/2,float(tem[57])/2,float(tem[58])/2,float(tem[59])/2],[float(tem[20])/2,float(tem[21])/2,float(tem[22])/2,float(tem[23])/2,float(tem[24])/2,float(tem[25])/2,float(tem[26])/2,float(tem[27])/2,float(tem[28])/2,float(tem[29])/2,float(tem[60])/2,float(tem[61])/2,float(tem[62])/2,float(tem[63])/2,float(tem[64])/2,float(tem[65])/2,float(tem[66])/2,float(tem[67])/2,float(tem[68])/2,float(tem[69])/2],[float(tem[30])/2,float(tem[31])/2,float(tem[32])/2,float(tem[33])/2,float(tem[34])/2,float(tem[35])/2,float(tem[36])/2,float(tem[37])/2,float(tem[38])/2,float(tem[39])/2,float(tem[70])/2,float(tem[71])/2,float(tem[72])/2,float(tem[73])/2,float(tem[74])/2,float(tem[75])/2,float(tem[76])/2,float(tem[77])/2,float(tem[78])/2,float(tem[79])/2]]
  import Model_hhdn2
  val=Model_hhdn2.f(obs,sp)
  return val

