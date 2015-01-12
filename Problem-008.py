__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 8
__name__   = "Largest product in a series"
__source__ = "https://projecteuler.net/problem=8"
__example__= "The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832."
__question__= "Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?"

import time


num =  "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

max = int(input("Find the X adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product? Where X="))

t = time.clock()

#Initialize the max product, and the numbers that comprise it 
max_product = 0
max_numbers = ""

#1001-X interations where X is the number of adjacent digits required 
for i in range (0, len(num)-max+1):

	#Initialize the current product, and numbers that comprise it
	cur_product = 1
	cur_numbers = ""

	#Multiply the X number of adjacent digits together
	for j in range (i, i+max):
		cur_product*=int(num[j])
		cur_numbers+=num[j]+"*"
		#Check the max product vs the current product and replace if greater
		if (cur_product>max_product):
			max_product = cur_product
			max_numbers = cur_numbers
		#Testing stuff 
		#print (num[j], end="")
	#print ()

#Cleanup: Remove the extra * form the end
max_numbers = max_numbers.replace(' ', '')[:-1].upper()

print ("\nThe", max, "adjacent digits that have the greatest product are "+max_numbers+" =", max_product)

print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")
