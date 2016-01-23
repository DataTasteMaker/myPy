# Classroom Assignment - Dated 09-11-2015
# Programmer: Viraj

# Import the required modules
import csv, sys
import random

# Create a function to find phone and Email values through random
def fnGetPhoneEmail():
    a = [] #Create a list which will hold phoneNo and email ID to return
    y = int(random.random() * 100000) # find first 5 digits by converting random values to integer
    y = str(y) # if at times the integer values are having less than 5 digits, we need to add the additional digits
    while len(y) < 5: # converted the integer to string and till the lenght is 5 digit keep adding a digit
        y = y + str(int(random.random() * 10))

    a.insert(0,str(y) + "@abc.com") # create an email ID here with help of phone no and string @abc.com

    if int(y) % 3 == 0: # if the phone no is divisible by 3 then make the phone no as 0, to keep consistency of values across the column
        a.append(0)
    else:
        a.append(y)
    return a

#----------------------------------------------------------------------

# Open the CSV file in read mode
inputfile = open("RetailScoreData.csv",'rt')

# Write the Dictionary in some file

dictFile = open('DictFile.txt', 'w')

# Create and open a new file in write mode
outputfile = open('OutputFile.csv', 'w')

# some temporary dictionary
rowDict = {}
colDict = {}

rowNum = 0
headerRow = []

# read the CSV into a variable reader
reader = csv.reader(inputfile)

# iterating through each row of the file 
for row in reader:
    if rowNum == 0:
        headerRow = row # get the headers/labels
    else:
        colNum = 0
        tmpDict = {}
        for col in headerRow:
            try:
                valueChk = int(row[colNum])
            except ValueError:
                valueChk = float(row[colNum])
            else:
                valueChk  = int(row[colNum])
            randVal = fnGetPhoneEmail() # call the function to get phone and emailID
            tmpDict['Email'] = randVal[0] # from the return values add a new key - Email
            tmpDict['phone'] = int(randVal[1]) # from the return values add a new key - Phone
            tmpDict[col] = valueChk
            colNum = colNum + 1
        colDict[rowNum] = tmpDict
    rowNum = rowNum + 1

# write the final dictionary structure
dictFile.write(str(colDict))

print " *********************************************************** "
# Add the new keys in the header list
headerRow.append('phone')
headerRow.append('Email')

# Create a string variable which will hold data with delimited by comma so that we can write this string variable 
# directly in a CSV file

mySTr = ""
for i in range(len(headerRow)): # get header/labels
    mySTr = mySTr + headerRow[i] + ", "
mySTr = mySTr + "\n"

for key1, value1 in colDict.items(): # Iterated in the 1nd level Dictionary 
    for i in range(len(headerRow)): # based on the header, extract the values from the dictionary and create a string variable
        if (i < len(headerRow)-1):
            mySTr = mySTr + str(value1[headerRow[i]]) + ","
        else:
            mySTr = mySTr + str(value1[headerRow[i]])
    mySTr = mySTr + "\n"
    #print str(mySTr)

# write the string in the outfile file
outputfile.write(str(mySTr))

inputfile.close()
outputfile.close()
dictFile.close()

