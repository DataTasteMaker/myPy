# import random
import numpy as np
from random import *

# NUMPY
myArr = np.arange(56)   # arrange 56 numbers
myArr.shape = (7,8) # put a shape/dimensions to the array
arrDim = np.shape(myArr)    # get dimensions in a list
# print arrDim[0], arrDim[1]    # prints row and col dimensions

for rNum in range(0,arrDim[0]): # for each row in array
    for cNum in range(0,arrDim[1]): # for each column in array
        myArr[rNum,cNum] = randrange(0, 10) # generate random values from range 0 to 10

# Create a new array of same dimensions as myArr
newArr = np.arange(56)  # arrange 56 numbers
newArr.shape = (7,8)    # put a shape/dimensions to the array

for rNum in range(arrDim[0]):
    xMean = int(np.sum(myArr[rNum,])) / int(len(myArr[rNum,]))  # find mean
    tempVar = [int(h) - xMean for h in myArr[rNum,]]        # subtract mean from the value

newArr = myArr - xMean

print "Orginal Array \n" + str(myArr)
print ""
print "New Array \n" + str(newArr)

print ""
print ""
oddColArray = newArr[::, 1:8:2]
print "A new array  which contains only the odd columns from the original array: "
print oddColArray

