#Checks if a number is prime or not
#Input: An integer number
#Input type: int
#Output: True if Prime, False if not
#Output type: Boolean
def primeCheck(prime):
	flag=True
	for i in range (2, int(prime/2)):
		if (prime%i==0):
			#print("-", prime, "is divisible by:", i)
			flag=False
	#if (flag!=False):
	#	print(prime, "is a Prime Number")
	#else:
	#	print(prime, "is not a Prime Number")
	return flag


#Get's the next prime number
#Input: A Prime integer number
#Input type: int
#Output: Returns the next prime number
#Output type: int
def nextPrime(prime):
    if (prime==2): return (3)
    else:
        if (2%prime==0): prime+=1
        else: prime+=2
        while (primeCheck(prime)==False):
            prime+=2
        return prime

#Get's the next prime number
#Input: A Prime integer number
#Input type: int
#Output: Returns the next prime number
#Output type: int
def lastPrime(prime):
    if (prime==3): return (2)
    else:
        if (2%prime==0): prime-=1
        else: prime-=2
        while (primeCheck(prime)==False):
            if (prime<=2):
                print('There are no more')
                return prime
            prime-=2
        return prime


#Get's the nth prime number
#Input: Integer, acts as term 'n'
#Input type: int
#Output: Returns the nth prime number
#Output type: int
def getPrime(term_n):
    #check user Input is integer
    try:
        val = int(term_n)
    except ValueError:
        print("That's not an int!")
    #If user input is integer
    else:

        #There is no 0 integer
        if (term_n<=0): 
            print('Error: Please input an integer greater then 0')
            return 0

        #The 1st Prime is an even number so return 2
        elif (term_n==1): 
            return (2)

        #All other primes are odd, use this method to find them
        else:
            count=0
            prime=1
            for  count in range (2, term_n):
                prime = nextPrime(prime)
            return prime



