__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"



import time
import getPrime

x = int(input("Print the first X Prime numbers, where X="))

t = time.clock()

prime_calc = getPrime.Prime()

#prime_calc.allPrime()

prime = 2

for i in range (0, x-1):
	#print (prime)
	prime = prime_calc.nextPrime(prime)

print (prime, "is the", str(x)+"th prime number")


while False:
	if (prime_calc.primeCheck(x)):
		print (x, "is a prime number!")
	else:
		print (x, "is not a prime number!")

prime_calc.__exit__()

print ("Test took "+str(round(time.clock()-t,3))+"s to complete\n")
