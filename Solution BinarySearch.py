# Program to perform a binary search to find the number
# that a user has thought of and written down
endloop = 0
# endloop will be set to 1 when the number is found
#or the user has given wrong answers
max = 1000
min = 1
print("Think of a number between 1 and 1000")
print("\nWrite it down! Are you ready? Press Enter.")
input()
guesses=0

while endloop==0:
    #find midpoint of search
    midpoint = int((max+min)/2)
    print("My guess is ",midpoint,"\nPlease enter Too high, Too low or Correct\n")
    reply=input()
    reply = reply.lower() #change to lowercase
    guesses+=1
    # adjust max or min and find the midpoint of the new range
    if reply =="too high":
        max = midpoint-1
    elif reply=="too low":
        min = midpoint + 1
    elif reply == "correct":
        endloop = 1
        print("I took",guesses,"tries to guess the number")
    else:
        print("Your reply is not recognised!")
        guesses-=1   #subtract 1 from guesses if user answers incorrectly
    if guesses>10:
        print("I think you made a mistake somewhere!")
        endloop = 1
print ("press Enter to exit")
input()

              
              
        
            
