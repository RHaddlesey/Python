# quiz ideas


score = 0
count = 0
import random
operatorList = [ "+", "-", "*" ]

def gener():
    print ("Welcome to the maths quiz")
    name = input("Please enter your name: ")
    year = input("Please enter your class: ")


    global count
    for count in range(1,11):
        
        num1 = random.randint(6,12)
        num2 = random.randint(1,6)
        sign = random.choice(operatorList)

        expression = "%d %s %d" % (num1, sign, num2)
        answer = eval(expression)
        print ("\nQuestion", count,":", expression, "= ???")
        reply = input("Enter your answer here: ")
        if reply.isdigit():
            reply = int(reply)
        else:
            print ("Please type a number\n")
        global score
        if (reply == answer):
            print ("Correct!\n")
            score = score + 1
        else:
            print ("Oh dear, I'm afraid that is wrong. It should be: ", answer," \n")
    count=count+1
    if count == 10:
        teacher
        
    

#tell the student they have finished and print their score
    print ("Well done",name,". You have finished the quiz.\n")
    print ("You scored...",score,"out of 10\n")
#if score == ("5")
 #   print ("great score!\n")
#else
    print ("good work\n")
    result = (name, year, score)
    result = (str(result))

#open a file and add the new student and their score
    f = open("myfile.txt", "a", encoding="utf-8")
    result=str(result)
    f.write("new student - ")
    f.write(result)
    f.close


#load the results file and print it
def teacher():
    for count in range(1,3):
        fname = "myfile.txt"
        infile = open(fname, 'r')
        data = infile.readline()
        print(data)
        count=count+1
    return data
        


#menu

print ("are you a teacher (1)")
print ("or student (2)?\n")
menuchoice = input("please press 1 or 2\n")


           
while menuchoice != "0":
    menuchoice = menuchoice
    if(menuchoice == "1"):
        teacher()
        

    elif(menuchoice == "2"):
        gener()
    


#tell the student they have finished and print their score
print ("Well done",name,". You have finished the quiz.\n")
print ("You scored...",score,"out of 10\n")
#if score == ("5")
 #   print ("great score!\n")
#else
print ("good work\n")
result = (name, year, score)
result = (str(result))

#open a file and add the new student and their score
f = open("myfile.txt", "a", encoding="utf-8")
result=str(result)
f.write("new student - ")
f.write(result)
f.close


