__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 10 
__name__   = "Summation of primes"
__source__ = "https://projecteuler.net/problem="+str(__problem__)
__example__= "The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17."
__question = "Find the sum of all the primes below two million."

import time

def printList(list, listMax):
    for i in range (0, listMax):
        if primes[i]:
            print(primes[i],i)


max = int(input('\nProblem 10: Summation of primes\n\nFind the sum of all the primes below: '))
t = time.clock()


sum=0
primes = [True for i in range (0, max+1)]

primes[0] = False
primes[1] = False

sum=0
for j in range (2, int(max**0.5)+1):
    if primes[j]:
        #print('j=',j)
        for i in range (2, int(max/j)+1):
            primes[j*i]=False
            #print('i=',i)

sum=0
#printList(primes, max)

for i in range (0, max+1):
    if primes[i]:
        sum+=i

print ('sum:', sum)
print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
