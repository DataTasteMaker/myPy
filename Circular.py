""" -------------------
Given a list of 1000 numbers (randomly generate yourself),
write a function that will delete every alternate element assuming the list is circular.
This function should continue running until only one element is left. The last remaining element has to be returned.
Eg. if * indicates the current pointer in the list, the list will modify as follows
starting [1*,2,3,4,5,6] becomes [1,3*,4,5,6] - [1,3,5*,6] - [1*,3,5] - [1,5*] - [5].
Hence 5 would be the output. Notice when the pointer is at 5, the next element is 1 and hence 1 gets deleted.
"""

""" ---------------------------------------------------------------------------------------------
# Please excute and re-direct the output to a text file for better view of the lists
e.g. python Circular.py > logFile.txt
--------------------------------------------------------------------------------------------- """ 

L = []
L = range(1,1001)

print "Original" , L

# current position of the cursor/pointer
curPos = 1
iterCntr = 0 
while len(L)>1:
    iterCntr = iterCntr + 1
    del L[curPos::len(L)]   # Delete/remove the element at the currposition which will be every alternate position
    curPos = curPos + 1     # increment to move to the next element
    if curPos > len(L):     # if reached to end of list, go to start, but to position 2nd (1st index)
        curPos = 1
    elif curPos == len(L):  # if reached to end of list, go to start, but to position 1st (0th index)
        curPos = 0
    print "List status at Iteration number ", iterCntr , " -- > " , L     # display the modified list

