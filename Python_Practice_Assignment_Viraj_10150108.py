""" Python Assignment 101
Programmer: Viraj @ BDAP - SPJAIN

Problem Statement: --
*** Write a program to do following task.
 Read file content from InputFile.tx and display content of it.  Store lines content as an elements of array.
 Ask user to enter a word from user.
 Please enter a word.
 AC
 Then ask user which one of the below options he is interested.
 
 a) Count number of occurrence of user entered word and display it. Program should give error if user entered word is not there in Input file and
 Should ask once again and again to enter the word.(Hint:- You may have to use while loop here)
 while ture:
 print "Please entered a word to check"
 Word = raw_input()

 If ...
 b) Program should give which word is occurred maximum times in Input file.
 (In given InputFile.txt file , AC word is occurred maximum time so it should give output as AC)
 The Python code should ideally be modular - there should be a separate module (function) for each of the task(a and b) listed above.
 There should be a clear menu and communication with the user of the Program, saying user is inserted in option (function) a or option (function) b execution.
 You should also consider unreasonable inputs from the user.
""" 

import os
import string
os.system('cls' if os.name == 'nt' else 'clear')
os.system('color b')


print("\n")
print(" ******************** ******************** ******************** ")
print(" ******************** Python Assignment 101 ******************** ")
print(" ******************** ******************** ******************** ")

### Function Definitions STARTS
def WordCount(ipFile, searchWord):
    wrdCnt = 0
    for line in ipFile:
        for word in line.lower().split():
            if word.lower() == searchWord.lower():
                wrdCnt += 1
    return(wrdCnt)

def maxWordCnt(ipFile):
    wordlist = ipFile.read().split(" ")
    wordfreq = {}
    mostOccrFreq = ''
    tmpmostOccrFreq = ''
    mostOccrWrd = 0
    for w in wordlist:
        if w not in wordfreq.keys():
            wordfreq[w] = 1
        else:
            wordfreq[w] = wordfreq[w] + 1
    for k in wordfreq:
        if wordfreq[k] > mostOccrWrd:
            mostOccrWrd = wordfreq[k]
            mostOccrFreq = k
            tmpmostOccrFreq = tmpmostOccrFreq +  "'" + k + "'" + ", "
    return tmpmostOccrFreq[:-2]

### Function Definitions ENDS

print("\n")

ipFile = open("InputFile.txt", 'r')

print(" The program in reading a file with following text \n")
print(ipFile.read())
ipFile.seek(0) # to go to the start of the file after previous read functions

print("Summary")
print("|===============================|")
print(" No. of lines in the file |%5d"  %len(ipFile.readlines()) + "|")
ipFile.seek(0) # to go to the start of the file after previous read functions
print("|===============================|")
print(" No. of words in the file |%5d"  %len(ipFile.read().split()) + "|")
print("|===============================|")
print("\n")
ipFile.seek(0) # to go to the start of the file after previous read functions

taskCnt = -1
while True:
    try:
        os.system('color b')
        print("\n Please select one option from below:")
        print("\n 1. Count occurances of a word.\n 2. Find the word occurred maximum times.\n 9. Exit.")
        mahChoice = int(raw_input("\n Your selection -- "))
        if mahChoice == 9:
            os.system('color f')
            print(" ******************** ******************** ******************** ")
            print("")
            print ("                         Bye... Bye... ")
            print("")
            print(" ******************** ******************** ******************** ")

            exit()

        if mahChoice == 1:
            os.system('color 1f')
            taskCnt += 1
            if (taskCnt == 0):
                usrInput = raw_input("\n\n Enter the word you want to search : ")
            else:
                usrInput = raw_input("\n\n Enter the next word you want to search : ")

            print("\n")
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            chkStop = 0
            for ch in usrInput:
                if ch in punctuations:
                    chkStop = 1
            if chkStop == 1:
                print("\n The search string has some special characters, please remove and re-try")
                raw_input()
                continue

            usrIPLen = usrInput.strip(" ")

            if (usrInput.isalpha()):
                print(" The word you entered is -- %s" %usrInput)
            else:
                print(" You've entered a number == %s" %usrInput)
            
            chkInput = raw_input("\n Please confirm to proceed... [Y/n]")

            if (chkInput.lower() != "y"):
                continue

            t = WordCount(ipFile,usrInput)
            if t == 0:
                print("\n\n Cannot find the string <- " + str(usrInput) + " ->\n")
            else:
                print("\n ************ The string you searched is occuring < - " + str(t) + " - > times. ************ \n\n")
            ipFile.seek(0) # to go to the start of the file after previous read functions
            continue

        if mahChoice == 2:
            os.system('color 2f')
            ipFile.seek(0) # to go to the start of the file after previous read functions
            print("\n\n The word(s) occurring maximum times is(are) -- " + str(maxWordCnt(ipFile)))
            raw_input("\n\n ... Press any key to continue")
            ipFile.seek(0) # to go to the start of the file after previous read functions
            continue

        if mahChoice > 2 and mahChoice < 9:
            os.system('color cf')
            print("\n\n Please enter the correct choice")
            raw_input("")
            continue

    except ValueError:
        os.system('color c')
        print("\n\n Sorry, I didn't understand that.\n\n Please try again!")
        raw_input()
        #better try again... Return to the start of the loop
        continue
    else:
        break

os.system('color f')
