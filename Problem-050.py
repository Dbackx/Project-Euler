__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 50
__name__   = "Consecutive prime sum"
__source__ = "https://projecteuler.net/problem=50"
__example__= """
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
"""
__question__= "Which prime, below one-million, can be written as the sum of the most consecutive primes?"


import time

def primeCheck(prime):
	i=0
	flag=True
	for i in range (2, int(prime/2)):
		if (prime%i==0):
			#print("-", prime, "is divisible by:", i)
			flag=False
	if (flag!=False):
		print(prime, "is a Prime Number")
	#else:
		#print(prime, "is not a Prime Number")
	return flag

def nextPrime(prime):
	prime+=2
	while (primeCheck(prime)==False):
		prime+=2
	return prime
	
max = int(input('Which prime, below X, can be written as the sum of the most consecutive primes, where X='))
t = time.clock()

sum = 2

i=1
n=1
prime = 1

while (sum<max):
	prime = nextPrime(prime)
	sum+=prime
	i+=1
	if (sum>max):
		sum-=prime
		break
	n+=1


lastPrime=prime
prime=1

if (primeCheck(sum)!=True):
	sum-=2
	i-=1

while (primeCheck(sum)!=True):
	print("Total =", sum)
	prime=nextPrime(prime)
	sum-=prime
	
	i-=1

print("Number of primes", i)
print("Total =", sum)
print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
