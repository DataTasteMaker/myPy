DictLevel1 = ['a','b','c']
DictLevel2 = ['grade','rc']
mydict = {}
finaldict = {}
tmplist = []

for i in range(0,2):
    if i >= 1 :
        mydict[DictLevel2[i]] = i
        mydict[DictLevel2[i-1]] = "Warning"
    else:
        mydict[DictLevel2[i+1]] = 0
        mydict[DictLevel2[i]] = "Ok"
    tmplist.append(mydict.copy())

mysubDict = {'counts' : 0, 'results': tmplist}

for key in DictLevel1:
    finaldict[key] = {}
    for i in range(1,6):
        finaldict[key][i] = mysubDict

print finaldict
