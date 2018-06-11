#Quiz Question

answer = input("What is the capital of France?\n")
answer = answer.title()  #A method to change answer to Title case

while answer != "Paris":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
print("Correct! Well done.")

input("\n\nPress ENTER to exit")
