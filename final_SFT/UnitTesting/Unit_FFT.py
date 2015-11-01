__author__ = 'Yas'
import numpy as np
import matplotlib.pyplot as plt
import unittest

def f(X,Y):
    #x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    #y = np.array([1,1,1,1,7,1,1,1,1,1,1,1,5,1,1])
    #input data taking
    x=np.array(X)
    y=np.array(Y)
    #x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
    #y = np.array([1,1,1,1,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1])
    # filter
    y2 = abs(np.fft.fft(y))
    y3 = abs(np.fft.ifft(y2))
    plt.plot(x, y,'.')
    plt.plot(x, y3,'g')#[1,1,1,1,7,1,1,1,1,1,1,1,5,1,1]
    plt.xlim(0, 61)
    plt.ylim(0, 15)
    plt.show()
    return 0
#unit testing
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(f([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,1,1,1,7,1,1,1,1,1,1,1,5,1,1]), 0)
        self.assertEqual(f([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[1,1,1,1,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1]), 0)
        self.assertEqual(f([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40],[1,1,1,1,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1]), 0)
