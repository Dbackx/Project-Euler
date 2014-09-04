__author__ = "Daniel Backx"
__version__ = "0.0.1"
__email__ = "dbackx11@gmail.com"
__status__ = "Production"
#Project Euler solutions
#Intention: Source runable file used to choose and execute problems according to their number

import sys
import os

while (True):
    userInput = ' '
    userInput = input('Hello, please enter a problem number or 0 to exit: ')
        #User inputs a non-number, reject /w exception
    try:
        val = int(userInput)
    except ValueError:
        print("That's not an int!")
    else:
        #User inputs 0, exit
        if (userInput=='0'): 
           break
        #User inputs number, find & run solution
        else: 
            flag=False
            from os import listdir
            files = [f for f in os.listdir('.') if os.path.isfile(f)]
            for f in files:
                #Search current directory for solution file
                if (f=='Problem-'+userInput+'.py'):
                    print(f)
                    print('It exists!')
                    exec(open(f).read())
                    flag=True
            if (not flag): print('Sorry. Solution does not exist yet.')







