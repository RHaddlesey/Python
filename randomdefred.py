

# quiz ideas

"""so here I am defining my global variables that will be
used within definition sub-section. When I call these variables later
I will need to set them as global variable-name"""
st=0
t=0
score = 0
count = 1
import random #here i open the random module that allows me to
                #generate random numbers
operatorList = [ "+", "-", "*" ]#here i set the the types of sums i will use

#menu
def menu(): #this defines the whole menu function
    #START OF THE ACTUAL PROGRAM
    print ("are you a teacher (1)")
    print ("or student (2)?\n""please press 1 or 2\n")
    menuchoice = input()
    if(menuchoice == "1"):
        teacher()#if they press 1 the program will run the teacher definition
    elif(menuchoice == "2"):
        print ("Welcome to the maths quiz")
        name = input("Please enter your name: ")#set the name variable
        year = input("Please enter your class: ")#set the year/class variable
        go = input(str("Are you ready to begin?\n"))#ask if they are ready to start
        if go in ("y", "yes", "Yes", "YES", "yeah", "yep"):
            gener(name, year)#if 2 is preseed the gener definition will be invoked
        
        else:
            print ("\n""OK...Goodbye.....")#end program
        

def again():
    ok = input("\nWould you like to play again?\n")
    if ok in ("y", "yes", "Yes", "YES", "yeah", "yep"):
        menu()
    else:
        print ("\n""OK...Goodbye.....")
    ()#this will end the program

def gener(name, year):
    count = 1
    score = 0
    score1=score
    

    while count<11: #this will make it loop 10 times 
        num1 = random.randint(6,12)#generates a random number between 6 and 12
        num2 = random.randint(1,6)#as above between 1 and 6
        #i have done it this way to avoid negative numbers
        sign = random.choice(operatorList)#this picks a random - + or *

        expression = "%d %s %d" % (num1, sign, num2)#this formats the sum as
        #digit string digit so it can calculate the sum below
        answer = eval(expression)#this runs the question within the program
        print ("\nQuestion", count,":", expression, "= ???")#prints the
        #questions on the screen
        reply = input("Enter your answer here: ")
        if reply.isdigit(): #if the reply is a digit it will convert to an interger
            reply = int(reply)
        else:
            print ("Please type a number\n")#if not a number it will ask for a number
        if (reply == answer):#checks the students reply against the axctual answer
           print ("Correct!\n")
           score1=score1+1 #if the answer is correct it will add 1 to the score
        else:
            print ("Oh dear, I'm afraid that is wrong. It should be: ", answer," \n")
            #this tells the user they are wrong and shows the correct answer
        count=count+1 #enables the loop      
    else:
        result = (name, year, score1)#sets up the students result against their name and class 
        showtotal(result, name, year, score1)#run the showtotal and bring accross the variables in the ()
       
def showtotal(result, name, year, score1):#defines showtotal and calls the variables in ()
    #if a variable is defined outside of this block you need
    #to call it as a global variable so it updates all the instances of the variable
    global st
    global count
    global score
    while st==0: #this allows this to loop once
        #tell the student they have finished and print their score
        print ("Well done",name,". You have finished the quiz.\n")
        print ("You scored...",score1,"out of 10\n")
        score1 = int(score1)#this makes sure score1 is a number so we can do >5 below

        if score1 ==10:
            print ("Excellent...Full marks!\n ")
            st=st+1 #i needed this to stop the loop
            
        elif score1 > 5:#if they get more than 5 right they get great score
                    #instead of good score
            print ("great score!\n")
            st=st+1
        else:
            print ("good work\n")
            st=st+1
    else:
        print (result)  #so it can be written to file
        f = open("myfile.txt", "a")#opens a file in a state it can be added to "a"
        f.write (" - New student - ")#seperates the students in the file
        result = (str(result))#converts result to a string so it can be written to the file
        f.write(result)#add result to the file
        f.close()#you have to close the file
        print ("Saving your score!...")
        import time #this opens the time module
        time.sleep(2)#this will pause the program for 2 seconds
        again() #invokes the again def


#load the results file and print it on screen
def teacher(): #task 3
    fname = ("myfile.txt")#defines fname as the file
    infile = open(fname, 'r') #opens in the file fname so it can be read
    data = infile.readlines() #sets to to the contents of the file
    print(data) #prints the contents of the file as data
    again() #invokes the again def


"""here we Invoke menu and start the program. This is where it all starts.
But you have to define the whole program before you can run it or you will get errors"""

menu()


