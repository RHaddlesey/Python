#Multiplication tables test
#A program that uses a while loop and elif clauses

#Import the random number module
import random

#Display the initial blurb 
print("Multiplication tables test")
print("**********************\n")
print("What table would you like to be tested on?")
timestable=int(input ())
print("You will be given 5 questions")

#Initialise the variables generate a random number between 3 and 12
score = 0
loopcounter = 1

#Create the loop
#!= means not equal to
while loopcounter<=5:
#generate a random number between 3 and 12
    number = random.randint(3, 12)    
    print(timestable, "X", number,"?")
    useranswer = int(input())
    correctanswer = number * timestable
    loopcounter+=1
    if useranswer == correctanswer:
        score+=1
        print("Correct")
    else:
        print ("Wrong! The correct answer is",correctanswer)

if score == 5:
    print("Congratulatios! You scored", score,"out of 5")
elif score==4:
    print ("Pretty good... you scored",score,"out of 5")
elif score==3:
    print ("Could do better... you scored",score,"out of 5")
else:
    print ("Oh dear! Back to the drawing board... you scored",score,"out of 5")
#Wait for the user to exit the program
#\n creates a blank line
input("\n\nPress ENTER to exit")
