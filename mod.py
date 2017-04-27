"""this program will output the modulus of two numbers
entered by the user, giving them the regular division too"""

def moduman(num): #sets the function and loads num
    for i in range (0,num):
        first = int(input("first number \n"))
        second = int(input("second number \n"))
        div = (first / second)
        print ("\nThis gives the answer as straight 'divided by' = ",div)
        div = int(div)
        answer = (div * second)
        print ("\nThis gives the answer to the answer from the sum multiplied by the second number with no decimals= ", answer)
        mod = (first % second) #this % is the modulus operator
        print ("\nThis is the modulos answer = ", mod)
        print ("\nThis would place the data into hash location\n",mod)
    i=i+1


answer = input("Do you want to run the modulus program?\n")
if answer in ("yes", "YES", "yeah", "ok", "y"):
    num = input("\nHow many times do you want to run the program?\n")
    num=int(num) #changes the string to an interger
    moduman(num) #this sends num to the moduman
else:
    print ("Bye then!")
"""note: although there are two variables named answer, because
1 is in a function it will not interfer with the other global variable
unless it is "sent to the def"""
