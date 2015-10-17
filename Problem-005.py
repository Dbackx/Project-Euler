__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 5
__name__   = "Smallest multiple"
__source__ = "https://projecteuler.net/problem="+str(__problem__)
__example__= "2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder."
__question__= "What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"

import time
import getPrime

def devisible(max, num):
	for x in range (1, max+1):
		if (num%x!=0):
			return False
	return True

max = int(input("What is the smallest positive number that is evenly divisible by all of the numbers from 1 to: "))

t = time.clock()

num = max*(max-2)
flag = False
while not flag:
	num+=max
	flag = devisible(max,num)


print (getPrime.primeSet(5))

print (num,"Is the smallest number divisible by all numbers between 1 and",max)

print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
