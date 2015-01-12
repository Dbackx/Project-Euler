__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 7
__name__   = "10001st prime"
__source__ = "https://projecteuler.net/problem=7"
__example__= "By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13."
__question__= "What is the 10 001st prime number?"

import time
import getPrime


x = int(input("What is the xth prime number? Where X="))

t = time.clock()

prime=1
for i in range (0, x):
	prime = getPrime.nextPrime(prime)

print ("The", x, "prime is", prime)

print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
