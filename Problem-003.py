__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 3
__name__   = "Largest prime factor"
__source__ = "https://projecteuler.net/problem="+str(__problem__)
__example__= "The prime factors of 13195 are 5, 7, 13 and 29."
__question__= "What is the largest prime factor of the number 600851475143?"

import getPrime
from math import sqrt
import time

num = int(input('\nProblem 3: Largest prime factor\n\n\tThe prime factors of 13195 are 5, 7, 13 and 29\n\n What is the largest prime factor of the number: '))
t = time.clock()


#Currently not working, much faster & more efficient version
if False:
    for div in range(2, int(sqrt(num))):
        if (num%div==0 and all(div%checkPrime!=0 for checkPrime in range (2, int(sqrt(div))))==True):
            maxPDiv = div

    print('Max prime divisor is:',div)


#Old method. takes too long, needs fix
flag=False
div = int(num/2)
if (num==4): print('The largest prime factor of', num,' is: 4\n\n')
else: 
    if (div%2==0): div-=1
    while (div!=1):
        if (num%div==0 and getPrime.primeCheck(div)):
            flag=True
            print('The largest prime factor of', num,' is: ',div, '\n\n')
            break
        div-=2

    if (flag==False): print('\nThere is no prime factor of:',num,'\n\n')



#Older Method, terrible, took too long. Waste of time & memory
if False:
    flag=False
    prime = 2
    while (prime<num/2):
        if ((num%prime)==0):
            largestPrime = prime
            flag=True
            print(prime, 'is a factor')
        prime = getPrime.nextPrime(prime)

    if (flag): print('The largest prime factor of', num,' is: ',largestPrime, '\n\n')
    else: print('\nThere is no prime factor of:',num,'\n\n')

print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
