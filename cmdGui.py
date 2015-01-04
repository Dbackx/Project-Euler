__author__  = "Daniel Backx"
__version__ = "0.0.2"
__email__   = "dbackx11@gmail.com"
__status__  = "Production"
#Project Euler solutions
#Intention: Source runable file used to choose and execute problems according to their number

import sys
import os

while (True):
    #User inputs a non-number, reject /w exception
    try:
        userInput = int(input("Hello, please enter a problem number or 0 to exit: "))
    except ValueError:
        print("That's not an int!")
    else:
        #User inputs 0, exit
        if (userInput==0): 
            print("\n***Goodbye***")
            break
        #User inputs number, find & run solution
        else: 
            flag=False
            from os import listdir
            files = [f for f in os.listdir('.') if os.path.isfile(f)]
            for f in files:
                #Search current directory for solution file
                if (userInput<10):
                    inputString = '00'+str(userInput)
                elif (userInput<100):
                    inputString = '0'+str(userInput)
                elif (userInput<1000):
                    inputString = str(userInput)
                else:
                    break

                if (f=='Problem-'+inputString+'.py'):
                    print(f)
                    print("It exists!\n")
                    try:
                        exec(open(f).read())
                        break
                    except ValueError:
                        print("Something went wrong! That problem's solution seems to have an issue. . .\n")
                    flag=True
            if (flag): print("Sorry. Solution does not exist yet.")







