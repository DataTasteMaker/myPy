"""
File Name           : BubbleSort.py
Designed by         : Viraj (vb.bviraj@gmail.com)
Created on          : 24-01-2016
Last Updated        : 24-01-2016
Current Version     : V0_24012016 (Version number + Last Updated Date)
                    : V0 - Initial setup
"""

def bsort(mylist):
    tmp = len(mylist)
    for n in range(len(mylist)-1,0,-1):
        for i in range(n):
            if mylist[i] > mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp
        tmp = tmp - 1


mylist = [6, 5, 3, 1, 8, 7, 2, 4]
print("")
print("Orignal list " + str(mylist))
print("")

bsort(mylist)
print("")
print("Bubble Sort output " + str(mylist))
print("")
