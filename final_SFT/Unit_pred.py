__author__ = 'Yas'

from Tkinter import *
from PIL import Image, ImageTk
import os
import matplotlib.pyplot as pl
import unittest
def curv(student,TestNo):
    import Unit_CurveFitting
    val=Unit_CurveFitting.f(student,TestNo)
    return val
def ExMov(student,TestNo):
    import Unit_ExponentialMovingAverage
    val=Unit_ExponentialMovingAverage.f(student,TestNo)
    return val
def ExWeg(student,TestNo):
    import Unit_EponentialweigtedAverage
    val=Unit_EponentialweigtedAverage.f(student,TestNo)
    return val
grd=""
predValue=[]
def predict(student,TestNo):
    val1=curv(student,TestNo)
    #print val1
    val2=ExMov(student,TestNo)
    #print val2
    val3=ExWeg(student,TestNo)
   # print val3
    #by assuming weights are 3,2,1

    fVal=int(((int(val2)*1)+(int(val3)*1)+(int(val1)*0.85))/3)

    if fVal>=84:
       grd="A+"
    if (fVal>=75)&(fVal<=84):
       grd="A"
    if (fVal>=70)&(fVal<=74):
       grd="A-"
    if (fVal>=65)&(fVal<=69):
       grd="B+"
    if (fVal>=60)&(fVal<=64):
       grd="B"
    if (fVal>=55)&(fVal<=59):
       grd="B-"
    if (fVal>=50)&(fVal<=54):
       grd="C+"
    if (fVal>=45)&(fVal<=49):
       grd="C"
    if (fVal>=40)&(fVal<=44):
       grd="C-"
    if (fVal>=35)&(fVal<=39):
       grd="D"
    if (fVal<=34):
       grd="F"
    predValue.append(grd)
    print "Final Predicted value for "+student+" is: "+grd
    return 0

'''
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(predict("120006T",12),0)
        self.assertEqual(predict("120026L",12),0)
        self.assertEqual(predict("120028L",12),0)
        self.assertEqual(predict("120029P",12),0)
        self.assertEqual(predict("120111K",12),0)
        self.assertEqual(predict("120427J",12),0)
        self.assertEqual(predict("120526L",12),0)
        self.assertEqual(predict("120594P",12),0)
'''
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(predict("120006T",7),0)
        self.assertFalse(predict("120010B",7),0)
        self.assertEqual(predict("120025B",7),0)
        self.assertEqual(predict("120028L",7),0)
        self.assertEqual(predict("120029P",7),0)
        self.assertEqual(predict("120074X",7),0)
        self.assertEqual(predict("120083A",7),0)
        self.assertEqual(predict("120111K",7),0)
        self.assertEqual(predict("120113T",7),0)
        self.assertFalse(predict("120128T",7),0)
        self.assertEqual(predict("120132B",7),0)
        self.assertEqual(predict("120143J",7),0)
        self.assertEqual(predict("120162P",7),0)
        self.assertEqual(predict("120165D",7),0)
        self.assertEqual(predict("120182C",7),0)
        self.assertEqual(predict("120195T",7),0)
        self.assertEqual(predict("120197C",7),0)
        self.assertEqual(predict("120217P",7),0)
        self.assertEqual(predict("120221X",7),0)
        self.assertFalse(predict("120222H",7),0)
        self.assertEqual(predict("120228B",7),0)
        self.assertEqual(predict("120236X",7),0)
        self.assertEqual(predict("120237C",7),0)
        self.assertEqual(predict("120260N ",7),0)
        self.assertEqual(predict("120271A",7),0)
        self.assertEqual(predict("120281E",7),0)
        self.assertEqual(predict("120282H",7),0)
        self.assertEqual(predict("120284P",7),0)
        self.assertEqual(predict("120287D",7),0)
        self.assertFalse(predict("120306M",7),0)
        self.assertEqual(predict("120309B",7),0)
        self.assertEqual(predict("120323L",7),0)
        self.assertEqual(predict("120337H",7),0)
        self.assertEqual(predict("120342T ",7),0)
        self.assertEqual(predict("120343X",7),0)
        self.assertEqual(predict("120345F",7),0)
        self.assertEqual(predict("120353D",7),0)
        self.assertEqual(predict("120357T",7),0)
        self.assertEqual(predict("120374R",7),0)
        self.assertFalse(predict("120375V",7),0)
        self.assertEqual(predict("120391P",7),0)
        self.assertEqual(predict("120399X",7),0)
        self.assertEqual(predict("120410C",7),0)
        self.assertEqual(predict("120418H ",7),0)
        self.assertEqual(predict("120445L",7),0)
        self.assertEqual(predict("120448A",7),0)
        self.assertEqual(predict("120450X",7),0)
        self.assertEqual(predict("120452F",7),0)
        self.assertEqual(predict("120460D",7),0)
        self.assertFalse(predict("120470H",7),0)
        self.assertEqual(predict("120488U",7),0)
        self.assertEqual(predict("120496R",7),0)
        self.assertEqual(predict("120507F",7),0)
        self.assertEqual(predict("120538B",7),0)
        self.assertEqual(predict("120542G",7),0)
        self.assertEqual(predict("120548F",7),0)
        self.assertEqual(predict("120586T",7),0)
        self.assertEqual(predict("120594P",7),0)
        self.assertEqual(predict("120606H",7),0)
        self.assertFalse(predict("120612X",7),0)
        self.assertEqual(predict("120615J",7),0)
        self.assertEqual(predict("120633L",7),0)
        self.assertEqual(predict("120638G",7),0)
        self.assertEqual(predict("120665K ",7),0)
        self.assertEqual(predict("120694X",7),0)
        self.assertFalse(predict("120699R",7),0)
        self.assertEqual(predict("120702A",7),0)
        self.assertEqual(predict("120706N",7),0)
        self.assertEqual(predict("120710V",7),0)
        self.assertEqual(predict("120721F",7),0)
        self.assertEqual(predict("120749X",7),0)
        print predValue
        val=[]
        for x in range(0,len(predValue)):
            if predValue[x]=="A+":
               val.append(84)
            if predValue[x]=="A":
               val.append(75)
            if predValue[x]=="A-":
               val.append(70)
            if predValue[x]=="B+":
               val.append(65)
            if predValue[x]=="B":
               val.append(60)
            if predValue[x]=="B-":
               val.append(55)
            if predValue[x]=="C+":
               val.append(50)
            if predValue[x]=="C":
               val.append(45)
            if predValue[x]=="C-":
               val.append(40)
            if predValue[x]=="D":
               val.append(35)
            if predValue[x]=="F":
               val.append(30)
        print len(val)
        real=[70,55,75,85,30,55,65,50,35,65,75,70,60,60,65,65,50,40,60,35,75,65,50,55,35,50,45,55,70,50,75,70,75,65,55,60,50,85,55,40,85,40,80,45,65,35,70,75,70,70,40,80,70,70,75,30,80,70,30,45,75,40,70,40,60,45,80,75,75,70,55]
        re=[]
        with open('real.txt','r') as f:
            for line in f:
                for word in line.split():
                 re.append(word)
        print len(re)
        xval=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71]
        pl.plot(xval, real,'r')
        pl.plot(xval, val,'b')
        #pl.plot(xval, re,'g')
        pl.ylim(0,100)
        pl.xlim(1,72)
        pl.show()


