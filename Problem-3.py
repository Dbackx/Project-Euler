Found=True
div = 20
num=0
x=0


getDenom	

while Found:
	num+=div*(div-1)
	print (num)
	z=0
	for x in range (1, div+1):
		print(x)
		if (num%x!=0):
			break
		else:
			z+=1
	if (z==div):
		Found=False

print('ANSWER: ', num)

232792560
174594420

