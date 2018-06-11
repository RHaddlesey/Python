questions = []
answers = []
score = 0

def readfile(filename):
	lines = []	
	try:
		f = open(filename, 'r')
		lines = f.readlines()
		return lines
        except Exception as err:
		print ("Unable to read file: ",err)


questions = readfile("question.txt")
answers = readfile("answers.txt")

#print(questions)
#print(answers)


for question in questions:
        print(question)
        answer = input()
        if(answer == answers):
                print("Correct")
        else:
                print("Wrong")
