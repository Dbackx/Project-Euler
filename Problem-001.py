#Problem 1: Multiples of 3 and 5
#
#Source: https://projecteuler.net/problem=1
#
#	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.
#
#Daniel Backx
#

    #Get user input and set to max
userInput = input('\nProblem 1: Multiples of 3 and 5\n\n\tIf we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.\n\n Find the sum of all the multiples of 3 and 5 below: ')
max = int(userInput)

sum = 0

#Find sum of all numbers divisible by 3 below max
x=0
while x*3<max:
	#print(3*x)
	sum += 3*x
	x+=1
	

#Find sum of all numbers divisible by 5 below max that are not divisible by 3
x=0
while x*5<max:
	#print(5*x)
	if (x%3!=0):
		sum += 5*x
	x+=1


print'The sum of all numbers divisible by 3 or 5 below', max,'is:',sum, '\n\n'