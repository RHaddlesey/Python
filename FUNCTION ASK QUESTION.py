def askQuestion(question,correctAnswer):
    userAnswer = input(question)
    #userAnswer = userAnswer.Title()
    if(userAnswer == correctAnswer):
        print("Correct")
    else:
        print("Wrong")


askQuestion("What colour is the sky: ","blue")
