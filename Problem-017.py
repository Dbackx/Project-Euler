__author__ = "Daniel Backx"
__email__  = "dbackx11@gmail.com"

__problem__= 17
__name__   = "Number letter counts"
__source__ = "https://projecteuler.net/problem="+str(__problem__)
__example__= "If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 'and' when writing out numbers is in compliance with British usage."
__question__= "If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?"

import time


max = int(input("If all the numbers from 1 to X inclusive were written out in words, how many letters would be used? Where X ="))

t = time.clock()



print ("Problem",__problem__,"took "+str(round(time.clock()-t,3))+"s to complete\n")




0-9 		= 0+3+3+5+4+4+3+5+5+4

10-12		= 3+6+6

13-19+teen 	= 4+4+3+3+5+4+4
thir
four
fif
six
seven
eigh
nine
20 + 0-9 	= 6*10 + 0-9		#twenty
30 + 0-9 	= 6*10 + 0-9 		#thirty
40 + 0-9 	= 6*10 + 0-9 		#fourty
50 + 0-9 	= 5*10 + 0-9 		#fifty
60 + 0-9 	= 5*10 + 0-9 		#sixty
70 + 0-9 	= 7*10 + 0-9 		#seventy
80 + 0-9 	= 6*10 + 0-9 		#eighty
90 + 0-9 	= 6*10 + 0-9 		#ninety

(1-9)*99 + hundred*99 + (0-99)*9

1 + thousand



