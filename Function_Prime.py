"""
File Name           : Function_Prime.py
Designed by         : Viraj (vb.bviraj@gmail.com)
Created on          : 24-01-2016
Last Updated        : 24-01-2016
Current Version     : V0_24012016 (Version number + Last Updated Date)
                    : V0 - Initial setup
"""

## Function Definition Starts

def fnPrime(num):
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               print(str(num) + " is not a prime number")
               break
       else:
           print(str(num) + " is a prime number")
    else:
       print(str(num) + " is not a prime number")

# Call the function and pass 100 numbers
for i in range(10):
    fnPrime(i)
