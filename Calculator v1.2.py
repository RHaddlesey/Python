import time, sys
def calculator():
    while True:
        try:
            print("|Welcome to the calculator|")
            time.sleep(1)   
            num1 = int(input("Enter first number: "))    
            num2 = int(input("Enter second number: "))
            time.sleep(0.5)
            print("Your numbers are", num1 ,"and", num2)
            time.sleep(1)
            menu = "|Welcome to the calculator|\n\
            Please choose what you would like to do:\n\
            \n\
                1. Addition +\n\
                2. Subtraction -\n\
                3. Multiplication * or x \n\
                4. Division / or ÷\n\
                5. Square number 1\n\
                6. Square number 2\n\
                7. Square Bumber 1 by Number 2\n"
            

            x = int(input(menu))
            #functions
            def square(num1):

                return num1 ** 2
                #This function squares num1
         
            def square(num2):

                return num2 ** 2
                #This function squares num2

            def square(num1, num2):

                return num1 ** num2
                #this function squares num1 by num2 
                    
            def add(num1, num2):
                #this function adds num1 and num2 together

                return num1 + num2

            def subtract(num1, num2):
                #this function subtracts num2 from num1

                return num1 - num2

            def multiply(num1, num2):
                #this function multiplies num2 and num1 together

                return num1 * num2

            def division(num1, num2):
                #This function divides num1 by num2

                return num1 / num2
            def end():
                
                y = int(input("Type 1 to restart, 0 to exit: "))
                if y == 1:
                    calculator()
                if y == 0:
                    print("Exiting..")
                    time.sleep(0.1)
                    sys.exit()
                else:
                    print("Invalid command")
                    time.sleep(0.4)
                    end()
                

            time.sleep(0.1)

            #calling functions
            if x == 1:
                print("Answer: ", add(num1, num2))
            if x == 2:
                print("Answer: ", subtract(num1, num2))
            if x == 3:
                print("Answer: ", multiply(num1, num2))
            if x == 4:
                print("Answer: ", division(num1, num2))
            if x == 5:
                print("Answer: ", square(num1))
            if x == 6:
                print("Answer: ", square(num2))
            if x == 7:
                print("Answer: ", square(num1, num2))
            if x > 7 or x < 1:
                print("Invalid command")
                time.sleep(0.1)
                print("Restarting")
                calculator()
            
            
            time.sleep(0.5)
            end()
        except ValueError:
            print("Incorrect value or command")
            print("Restarting")
            time.sleep(0.5)
            calculator()


                    
            
calculator()


    
