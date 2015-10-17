__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 15
__name__   = "Lattice paths"
__source__ = "https://projecteuler.net/problem="+str(__problem__)
__example__= "Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner."
__question__= "How many such routes are there through a 20×20 grid?"

import time

def factorial (x):
	if (x<1): return 1
	else:
		return x*factorial(x-1)


size = int(input("How many unique routes from top left to bottom right exist on a square grid of size: "))

t = time.clock()

print ("There exist", int((factorial(2*size))/(factorial(size)*factorial(size))), "lattice routes through a", size, "x", size, "square grid.")


print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")




# OLD Methd. Took too long to solve. (hours for a +10x10 grid)

# def pathway (x, xcur, y, ycur):
# 	global total
# 	print ("(", xcur, ycur, ")", end="")
	
# 	if (xcur<x):
# 		print("       ", end="")
# 		pathway (x, xcur+1, y, ycur)
# 		#print (total)
# 	if (ycur<y):
# 		print("       ", end="")
# 		pathway (x, xcur, y, ycur+1)
# 		#print (total)
# 	if (xcur==x and ycur==y):
# 		total+=1
# 		print ("total=", total)
# 	return (total)

# x = int(input("How many unique routes from top left to bottom right exist on a grid of size: "))
# y = int(input("by:"))

# total=0


# length = pathway(x, 0, y, 0)

# print (length)
