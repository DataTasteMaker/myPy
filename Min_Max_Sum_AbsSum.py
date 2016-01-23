#************************* Maximum
Alist = [-2,-4,4,10,-100]
Blist = [7,8,6,0,2,1,99]

# Function Definition begins for finding Maximum value in a list
def fnmax(mylist):
    maxvalue = mylist[0]      # Take one random value to initiate comparision
    x = 0                     # Initialise Counter
    while x < len(mylist):    # Loop till counter is less than the length of the list passed
        if mylist[x] > maxvalue: # Compare the maxvalue with the current item of the list
            maxvalue = mylist[x] # if found store it in the maxvalue variable to be returned
        x = x + 1
    return(maxvalue)

print ""
print(" Maximum value from the list " + str(Alist) + " is = " + str(fnmax(Alist)))
print ""
print(" Maximum value from the list " + str(Blist) + " is = " + str(fnmax(Blist)))
print ""
print(" Maximum value from the list " + str(Alist + Blist) + " is = " + str(fnmax(Alist + Blist)))


#************************* Minimum

Alist = [-2,-4,4,10,-100]
Blist = [7,8,6,0,2,1,99]

# Function Definition begins for finding Minimum value in a list
def fnmin(mylist):
    minvalue = mylist[0]        # Take one random value to initiate comparision
    x = 0                       # Initialise Counter
    while x < len(mylist):      # Loop till counter is less than the length of the list passed
        if mylist[x] < minvalue:   # Compare the minvalue with the current item of the list
            minvalue = mylist[x]   # if found store it in the minvalue variable to be returned
        x = x +1
    return(minvalue)

print ""
print(" Minimum value from the list " + str(Alist) + " is = " + str(fnmin(Alist)))
print ""
print(" Minimum value from the list " + str(Blist) + " is = " + str(fnmin(Blist)))
print ""
print(" Minimum value from the list " + str(Alist + Blist) + " is = " + str(fnmin(Alist + Blist)))


#************************* Sum and Absolute Sum

Alist = [-2,-4,4,10,-100]
Blist = [7,8,6,0,2,1,99]

# Function Definition begins
def fnsum(mylist):
    cntr , sum, abssum = 0, 0, 0 # Initialise all to zero

    while cntr < len(mylist):       # Iterate the loop till the length of the list
        sum = sum + mylist[cntr]    # start summing up the values
        if (mylist[cntr] < 1):
            abssum = abssum + (mylist[cntr] * -1)  # If the value is negative, then multiply it with -1 and then sum it up
        else:
            abssum = abssum + mylist[cntr]
        cntr = cntr + 1
    print ''
    print('Sum of ' + str(mylist) + ' = ' + str(sum))
    print ''
    print('Abs Sum of ' + str(mylist) + ' = ' + str(abssum))

fnsum(Alist)
print ""
fnsum(Blist)
print ""
fnsum(Alist+Blist)

