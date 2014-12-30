# Problem 20: Factorial digit sum
#
# Source: https://projecteuler.net/problem=20
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#

def factorial(n):
	sum=0
	if n>0:
		return n*factorial(n-1)
	else:
		return 1

def digitsum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

max = int(input('\nProblem 20: Factorial digit sum\n\nFind the sum of the digits in the number(factorial): '))

fact = factorial(max)

print (max,'! is:', fact, ', and the sum of those digits is:', digitsum(fact))


