__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 1
__name__   = "Multiples of 3 and 5"
__source__ = "https://projecteuler.net/problem=1"
__example__= "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23."
__question__= "Find the sum of all the multiples of 3 or 5 below 1000."

import time

    #Get user input and set to max
max = int(input('\nProblem 1: Multiples of 3 and 5\n\n\tIf we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.\n\n Find the sum of all the multiples of 3 and 5 below: '))
t = time.clock()

sum = 0

#Find sum of all numbers divisible by 3 below max
x=0
while x*3<max:
	#print(3*x)
	sum += 3*x
	x+=1
	

#Find sum of all numbers divisible by 5 below max that are not divisible by 3
x=0
while x*5<max:
	#print(5*x)
	if (x%3!=0):
		sum += 5*x
	x+=1


print ('The sum of all numbers divisible by 3 or 5 below '+str(max)+' is: '+str(sum)+'\n\n')
print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
