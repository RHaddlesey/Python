questions = []
answers = []


try:
	f = open("question.txt", 'r')
	questions = f.readlines()
	f.close()
except Exception as err:
	print ("Unable to read file: ",err)

try:
	f = open("answers.txt", 'r')
	answers = f.readlines()
	f.close()
except Exception as err:
	print ("Unable to read file: ",err)



print(questions)
print(answers)
