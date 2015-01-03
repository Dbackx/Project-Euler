__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 20
__name__   = "Factorial digit sum"
__source__ = "https://projecteuler.net/problem=20"
__example__= "For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27."
__question__ = "Find the sum of the digits in the number 100!"

import time

def factorial(n):
	sum=0
	if n>0:
		return n*factorial(n-1)
	else:
		return 1

def digitsum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

max = int(input('\nProblem 20: Factorial digit sum\n\nFind the sum of the digits in the number(factorial): '))
t = time.clock()

fact = factorial(max)

print (max,'! is:', fact, ', and the sum of those digits is:', digitsum(fact))


print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
