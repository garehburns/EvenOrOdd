import random  #imports from Python's Random library

print ("*" * 20)  #prints out 20 asterisks
print ("Program 3 - Even or Odd")  #Program title
print ("*" * 20)  #prints out 20 more asterisks

yourNum = input("Please input a number: ")  #creates variable for the random number you input
myNum = random.randrange(0,20000)  #creates variable that uses the random library to create a random integer ranging from 0 to 20,000

print ("")  #creates an empty line to make things spaced out

print ("You entered: ", yourNum)  #shows you what number you inputted

if int(yourNum) % 2 == 0:  #executes a specific command IF the remainder of yourNum is equal to 0
    print ("This is even")  #prints if yourNum was an even number
    
else:  #if yourNum was odd and didn't meet the requirements for the if command, then the else command will be taken into effect
    print ("This is odd")  #prints if yourNum was an odd number

print ("")  #creates an empty line to make things spaced out

print ("I made: ", myNum)  #shows you the number I inputted

if myNum % 2 == 0:  #executes a specific command IF the remainder of myNum is equal to 0
    print ("This is even")  #prints if myNum was an even number
    
else:  #if myNum was odd and didn't meet the requirements for the if command, then the else command will be taken into effect
    print ("This is odd")  #prints if myNum was an odd number

print ("")  #creates an empty line to make things spaced out

input ("Press Enter to Exit.")  #allows the user to kill the program by pressing enter
