__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 12
__name__   = "Highly divisible triangular number"
__source__ = "https://projecteuler.net/problem="+str(__problem__)
__example__= """
Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
"""
__question__= "What is the value of the first triangle number to have over five hundred divisors?"


import time
from itertools import groupby
import operator
import functools

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


max = int(input("Prime Factorize: "))

t = time.clock()
Total_factors  =0
triangular_num =0
triangle_count =0
while Total_factors<max:
	triangle_count =  triangle_count+1
	triangular_num += triangle_count

	Exponents = ([len(list(group)) for key, group in groupby(prime_factors(triangular_num))])
	Total_factors = 1
	for i in Exponents:
		Total_factors*=i+1


print ("Total Number of factors of the", triangle_count, "th triangular number", triangular_num, "is: ", Total_factors)

print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
