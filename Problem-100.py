__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 100
__name__   = "Arranged probability"
__source__ = "https://projecteuler.net/problem=100"
__example__= """
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50'%%' chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

"""
__question__= "By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain."

import time
import math
from decimal import *

max = int(input("By finding the first arrangement to contain over X discs in total, determine the number of blue discs that the box would contain. (10^12 = 1,000,000,000,000) Where X="))

t = time.clock()

	#Initialize the 1st numbers in the set (similar to the fibonacci sequence)
prev_blue=1
prev_total=1
blue=0
total=0

	#Search until the total number of discs is over the set max
while (2*total+1<max):
	total 		= prev_blue + 2*prev_total
	blue 		= prev_blue + prev_total
	prev_blue 	= total
	prev_total 	= blue
		#In Bell's Equation, when k=-1, each OTHER iteration 
	total 		= prev_blue + 2*prev_total
	blue 		= prev_blue + prev_total
	prev_blue 	= total
	prev_total 	= blue
		#print ("Total:", int((total+1)/2), "\t\tBlue:", int((blue+1)/2), "\tRed:", int((total+1)/2)-int((blue+1)/2))



print ("\nThere will be", int((total+1)/2), "total discs where", int((blue+1)/2), "discs are blue.")

print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")


#old solution which takes in excess of 6hours (and counting)
while False:
	#Initialize num to cause a Do While loop instead of a While loop
	num=0.14123
	#check 1st number
	x-=1
	while (+Decimal(num/x*(num-1)/(x-1))!=0.5):
		x+=1
		num=+Decimal((2+(4-8*(x-(x**2)))**(1/2))/4)

	print ("\nThere will be", x, "total discs where", int(num), "discs are blue.")

