__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 6
__name__   = "Sum square difference"
__source__ = "https://projecteuler.net/problem=6"
__example__= """
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
"""

__question__= "Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."

import time

def square_sum(x):
	if (x==1):
		return 1
	else:
		return (x**2+(square_sum(x-1)))

def sum_square(x):
	if (x==1):
		return 1
	else:
		return (x+(sum_square(x-1)))


max = int(input("Find the difference between the sum of the squares of the first X natural numbers and the square of the sum. X="))

t = time.clock()

	#1^2 + 2^2 + 3^2 + ... + x^2 
square_sum_total = square_sum(max)
	#(1 + 2 + 3 + ... + x)^2
sum_square_total = sum_square(max)**2

print ("Sum of squares:\t", square_sum_total, "\tSquare's Sum:\t", sum_square_total)

print ("Difference:\t", sum_square_total-square_sum_total)

print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
