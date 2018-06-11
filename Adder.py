#Adder

print("Guess the Number Game!")
print("**********************\n")
print("Enter numbers to add together then press 0 to exit.")

#Initialise the variables
count = 0
running_total = 0
number = int(input("Input the first number: "))

#Add each number together until 0 is entered
while number != 0:
    count = count + 1
    running_total = running_total + number
    number = int(input("Input next number: "))

#Display the total sum and the number of entries made
print ("You entered ",count," numbers")
print ("Total = ",running_total)

input("Press ENTER to exit")
