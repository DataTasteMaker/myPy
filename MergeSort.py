"""
File Name           : MergeSort.py
Designed by         : Viraj (vb.bviraj@gmail.com)
Created on          : 24-01-2016
Last Updated        : 24-01-2016
Current Version     : V0_24012016 (Version number + Last Updated Date)
                    : V0 - Initial setup
"""

def mergeSort(myList):

    if len(myList) < 2:     # if only one Element return the value as is
        return myList

    midpt = len(myList) // 2     # Find the mid-point to break the list in half
    
    lhs = mergeSort(myList[:midpt])     # The first half goes in lhs
    rhs = mergeSort(myList[midpt:])     # The second half goes in rhs

    result = []

    i = j = 0
    
    while i < len(lhs) and j < len(rhs):
        if lhs[i] < rhs[j]:             # compare elements of left-half and right-half of the list
            result.append(lhs[i])
            i += 1
        else:
            result.append(rhs[j])
            j += 1

    result += lhs[i:]
    result += rhs[j:]

    return result

#mylist = [6,5,3,1,8,7,2,4]
mylist = raw_input("Enter a list of numbers separeated by comma -- ")
print("Original list --> " + str(mylist))
mylist = mylist.replace(",","")

print("Sorted list --> ")
print(mergeSort(mylist))

