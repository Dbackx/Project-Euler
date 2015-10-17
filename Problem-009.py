__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 9
__name__   = "Special Pythagorean triplet"
__source__ = "https://projecteuler.net/problem="+str(__problem__)
__example__= "For example, 32 + 42 = 9 + 16 = 25 = 52"
__question__= """
	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc.
	"""

import time
import math

max = int(input("There exists exactly one Pythagorean triplet for which a + b + c ="))

t = time.clock()

for j in range (2, max+1):
	for i in range (1, j):
		k = (i**2+j**2)**(0.5)
		if (k%1 == 0 and i+j+k == max):
			print (i, j, k)
			print (i**2, "+", j**2, "=", i**2+j**2)
			print ("a*b*c =", i*j*k)




print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
