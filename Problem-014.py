__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 14
__name__   = "Longest Collatz sequence"
__source__ = "https://projecteuler.net/problem="+str(__problem__)
__example__= """
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
"""
__question__= """
Which starting number, under one million and using the following rule, produces the longest chain?

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)
"""

import time

def collatz_solution(n):
	global collatz_length
	print (n)
	#print ("Solution for:", n, collatz_length[n-1])
	if (collatz_length[n-1]==0):
		if (n%2==0):
			if (n<max):
				collatz_length[n-1] = 1+collatz_solution(int(n/2))
			return (collatz_length[n-1])
		elif (n==1):
			return (1)
		else:
			if (n<max):
				collatz_length[n-1] = 1+collatz_solution(n*3+1)
			return (collatz_length[n-1])
	else:
		print ("skip", n)
		return (collatz_length[n-1])

max = int(input("Collatz Test number: "))

t = time.clock()

collatz_length = [0] * max

max_length=0
maxnum=0


for i in range (0, max):
	if (collatz_length[i]==0):
		collatz_length[i] = collatz_solution(i+1)
	if (collatz_length[i]>max_length):
		max_length=collatz_length[i]
		maxnum = i+1
		print (maxnum, "Total length", max_length)	

for j in range (0, max):
	if (collatz_length[j]!=0):
		print (j+1, collatz_length[j])

	
print ("\nFinal:", maxnum, "Total length", max_length)



if False:
	length = 0
	n = max
	max_length=0
	for i in range (1, max):
		length=1
		n=i
		while (n!=1):
			#print (n)
			length+=1
			if (n%2==0):
				n/=2
			else:
				n*=3
				n+=1
		#print (i, "Total length", length)
		if (length>max_length):
			max_length=length
			maxnum = i
			print (maxnum, "Total length", max_length)
		if (i==999999):
			print (i, "Total length", length)
	print ("\nFinal:", maxnum, "Total length", max_length)


print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")







