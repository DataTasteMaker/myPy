myDict = {}
txtFile = open("Input_File_for_Count_Words_Most_Least.txt")
keyList = []
valList = []
for line in txtFile:
    words = line.split()
    for word in words:
		if len(word) >=4:
			if word not in myDict.keys():
				word = word.lower()
				myDict[word] = 1
			else:
				myDict[word] = myDict[word] + 1

#print myDict
#print ""
#print ""

for key in myDict.keys():
		keyList.append(key)
		valList.append(myDict[key])

#print keyList, valList


def bsort(myKeylist, myVaLlist):
    tmp = len(myVaLlist)

    for n in range(len(myVaLlist)-1,0,-1):
        for i in range(n):
            if myVaLlist[i] > myVaLlist[i+1]:
                temp = myVaLlist[i]
                myVaLlist[i] = myVaLlist[i+1]
                myVaLlist[i+1] = temp

                temp = myKeylist[i]
                myKeylist[i] = myKeylist[i+1]
                myKeylist[i+1] = temp
        tmp = tmp - 1

bsort(keyList, valList)
#print "Sorting...."
#print ""
#print keyList, valList

mostUsed = []
leastUsed = []

for i in range(11):
	#print i , len(keyList)-i
	leastUsed.append(keyList[i])
	mostUsed.append(keyList[len(keyList)-1-i])

print ""
print "List of <<<MOST>>> used Words :\n\n **" + str(sorted(mostUsed))
print ""
print "List of <<<LEAST>>> used Words :\n\n **" + str(sorted(leastUsed))

