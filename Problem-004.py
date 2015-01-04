__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 4
__name__   = "Largest palindrome product"
__source__ = "https://projecteuler.net/problem=4"
__example__= "A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99."
__question__= "Find the largest palindrome made from the product of two 3-digit numbers."

import time

def palindromecheck(Pal):
	return Pal==Pal[::-1]

def palindrome(Pal):
	return int(str(Pal)+str(Pal)[::-1])

digitcount = int(input("Find the largest palindrome made from the product of two X-digit numbers. Where X="))

t = time.clock()

#Find the largest X-digit number
genPal = ''
for i in range (0, digitcount):
	genPal += str(9)
max = int(genPal)

#Set largest palindrome to 0
greatestx = 0
greatesty = 0
#is (Max-i)*(Max-j) palindrome? If yes, record X,Y,and X*Y
for i in range (max, (9*max)//10, -1):
	for j in range (0, i+1):
		y = max-j
		if (palindromecheck(str(i*y))):
			if (i*y>greatestx*greatesty):
				greatestx=i
				greatesty=y

print ("\nThe largest pallidrome number made from the product of two "+str(digitcount)+"-digit numbers is: "+str(greatestx)+"*"+str(greatesty)+"="+str(greatesty*greatestx))

print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
