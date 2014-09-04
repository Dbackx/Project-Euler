i = 1000

sum = 0

x=0
while x*3<i:
	print(3*x)
	sum += 3*x
	x+=1
	
x=0
while x*5<i:
	print(5*x)
	if (x%3!=0):
		sum += 5*x
	x+=1

print(sum)
