
class Prime(object):
    """docstring for Prime"""
    def __init__(self):
        super(Prime, self).__init__()
        self.prime_num = []
        self.prime_new = []
        self.start()

    def __exit__(self):
        #append to the file here
        if (len(self.prime_new)!=0):
            print ("Appending", self.prime_new, "to file")
            
            with open("Primes.txt", "a") as f:
                for i in range (0, len(self.prime_new)):
                    f.write("\n"+str(self.prime_new[i]))
            f.close()


    def start(self):
        print ("Opening file and extracting Primes")
        with open("Primes.txt", "r") as f:
            for line in f:
                self.prime_num.append(int(line))
        f.close()


    def allPrime(self):
        print (self.prime_num)

    #Checks if a number is a known prime number 
    #Input: An integer number
    #Input type: int
    #Output: True if known, False if not
    #Output type: Boolean
    def libraryCheck(self, prime):
        for i in range (0, len(self.prime_num)):
            #print (prime, "=", self.prime_num[i], "=\t", prime==self.prime_num[i])
            if (prime==self.prime_num[i]):
                return True
        return False                

    #Checks if a number is a known prime number 
    #Input: An integer number
    #Input type: int
    #Output: True if known, False if not
    #Output type: Boolean
    def primeCheckLibrary(self, prime):
        for i in range (0, len(self.prime_num)-1):
            #print (prime, "%", self.prime_num[i], "=\t", prime%self.prime_num[i]==0)
            if (prime%self.prime_num[i]==0):
                return prime==self.prime_num[i]
        return True

    #Input: An integer
    #Input type: int
    #Get's the next prime number
    #Output: Returns the next prime number
    #Output type: int
    def nextPrime(self, prime):
        if (prime < self.prime_num[len(self.prime_num)-1]):
            nothing = 0    

        if (2%prime==0):    prime+=1
        else:               prime+=2
        if (5%prime==0 and prime!=5): prime+=2
        while (self.primeCheckLibrary(prime)==False):
            #print (prime)
            if (5%prime==0 and prime!=5): prime+=2
            prime+=2

        if (self.libraryCheck(prime)!=True):
            self.prime_num.append(prime)
            self.prime_new.append(prime)
        return prime

    #Checks if a number is prime or not
    #Input: An integer number
    #Input type: int
    #Output: True if Prime, False if not
    #Output type: Boolean
    def primeCheck(self, prime):
        if (prime < self.prime_num[len(self.prime_num)-1]):
            print (prime, "<", self.prime_num[len(self.prime_num)-1], "Check vs Library")
            return self.primeCheckLibrary(prime)
        else:
            while (prime/2 > self.prime_num[len(self.prime_num)-1]):
                print (prime/2, ">", self.prime_num[len(self.prime_num)-1], "Generate primes until able to check")
                self.nextPrime(self.prime_num[len(self.prime_num)-1])

            i=0
            while (self.prime_num[i] < prime/2):
                if (prime%self.prime_num[i]==0):
                    if (prime==self.prime_num[i]):
                        return True
                    return False
                i+=1
            return True

    #Get's the previous prime number
    #Input: A Prime integer number
    #Input type: int
    #Output: Returns the previous prime number
    #Output type: int
    def lastPrime(self, prime):
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
    def getPrime(self, term_n):
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
                prime=2
                for count in range (0, term_n+2):
                    prime = nextPrime(prime)
                return prime

