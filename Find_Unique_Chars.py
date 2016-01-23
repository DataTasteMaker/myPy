# File Name: Find_Unique_Chars.py
# Date : 07-11-2015
#
# Description:
#   The script takes a string as input and displays the characters and their count in dictionary format
#   then a loop iterates through the dictionary and creates a list of unique characters
#

#Get a string as input
print 'Please enter a string: '
strTxt = raw_input()

print ''

if strTxt == "":
    strTxt = "The quick brown fox jumps over lazy dog"

#initialise the dictionary to null
myDict = {}

strTxt = strTxt.lower() # convert the string to lower case for easy comparision

print "The string used = " + str(strTxt)

for char in strTxt: # loop on each character in the string
    if char not in myDict.keys(): #if the current character is not already in my Dictionary then add it
        myDict[char] = 1
    else: #if the current character is already in my Dictionary then add increment the count
        myDict[char] = myDict[char] + 1

#print myDict
uniquelist = []

for key in myDict.keys():
		uniquelist.append(key)

print "The list with unique characters --- " + str(uniquelist)
print ''
print ''
print " Execution done"

