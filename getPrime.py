Set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 
        97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 
        191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 
        283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 
        401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 
        509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 
        631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 
        751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 
        877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


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

#Get's the previous prime number
#Input: A Prime integer number
#Input type: int
#Output: Returns the previous prime number
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


#Return the first x prime numbers (below 100)
#Input: Integer, acts as term 'n'
#Input type: int
#Output: Returns a set of integers of size x
#Output type: int[x]
def primeSet(n):
    #check user Input is integer
    try:
        val = int(n)
    except ValueError:
        print("That's not an int!")
    #If user input is integer
    else:
        return Set[:n]

