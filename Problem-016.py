__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 16
__name__   = "Power digit sum"
__source__ = "https://projecteuler.net/problem="+str(__problem__)
__example__= "2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26."
__question__= "What is the sum of the digits of the number 2^1000"

import time
import math

max = int(input("What is the sum of the digits of the number 2^"))

t = time.clock()

total = pow(2, max)

Digit_sum = sum(int(x) for x in str(total))

print ("The sum of the digits in the number 2^"+str(max), "is", Digit_sum)

print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
