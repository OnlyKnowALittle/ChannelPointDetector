import numpy as np
import sys

def beginnerone():
    #Multiplying two arrays together - cannot do with lists
    a = np.array([4,2,5,32,5,3])
    b = np.array([7,3,2,5,12,4])

    #Multiply two arrays
    print(a*b)
    #Get Dimension
    print(b.ndim)
    #Get Shape
    print(b.shape)
    #Get Type
    print(a.dtype)

#All 0s Matrix
a = np.zeros((8,2,4))
b = np.ones((4,2), dtype='int32')
c = np.full((2,6), 20)
d = np.full((8),25)
'''
print(a)
print("Now the ones")
print(b)
'''
print(c)
print(d)