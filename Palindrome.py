# ****** Function Definition Starts

# Create a function to find Palindrome word in a Sentence
def IsPalindrome(ip_txt):
    txtLen = len(ip_txt)        # Find the text length
    ip_txt = ip_txt.lower()     # Convert the text in lower case to compare it easily as the comparison is case sensitive
    chkPalin = "Is Palindrome"  # Just a flag, set to default as "Is Palindrome"

    i = 0 # set a counter
    while(i < txtLen / 2 + 1): #iterate to half of the string, no need to check all the characters
            # compare the first and the last characters, if anytime not equal then break the loop and flag it as "Not a Palindrome"
            if (ip_txt[i] != ip_txt[txtLen - i - 1]):
                chkPalin = "Not a Palindrome"
            break
            i = i + 1
    return chkPalin
# ****** Function Definition Ends
# *******************************************************

#example string: madam is teaching anna malayalam language today

print 'Please enter a Sring: '
strtext = raw_input()
print ''
# Split the sentence with a delimiter as space and pass each word to check if the word is palindrome or not
temp = strtext.split(" ")

i = 0
while (i < len(temp)):
    print(str(temp[i]) + ' = ' + str(IsPalindrome(temp[i])))
    print ' '
    i = i + 1