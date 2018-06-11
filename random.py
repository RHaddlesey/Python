# quiz ideas

import random
operatorList = [ "+", "-", "*" ]
print ("Welcome to the maths quiz")
s = 1
name = input("Please enter your name: ")
year = input("Please enter your class: ")
for i in range(10):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    sign = random.choice(operatorList)

    expression = "%d %s %d" % (num1, sign, num2)
    answer = eval(expression)
    print ("Question", s,":", expression, "= ???")
    reply = int(input("Enter your answer here: "))
    if (reply == answer):
        print ("Correct")
    else:
        print ("Oh dear, I'm afraid that is wrong. It should be: ", answer)
    s=s+1

print ("Well done! You have finished the quiz.")
