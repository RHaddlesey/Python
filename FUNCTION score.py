score = 0

def askQuestion(question,correctAnswer,score):
    userAnswer = input(question)
    userAnswer = userAnswer.Title()
    if(userAnswer == correctAnswer):
        print("Correct")
        score = score + 1
    else:
        print("Wrong")
    return score


score = askQuestion("What colour is the sky: ","Blue",score)
