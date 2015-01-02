__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 4
__name__   = "Largest palindrome product"
__source__ = "https://projecteuler.net/problem=4"
__example__= "A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99."
__question__= "Find the largest palindrome made from the product of two 3-digit numbers."

def palindrome(num):
    return num == num[::-1]

print()

