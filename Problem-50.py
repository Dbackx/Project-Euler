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
	
max=1000000

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