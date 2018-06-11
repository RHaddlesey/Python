questions = []
answers = []
	

def readfile(filename):
	lines = []	
	try:
		f = open(filename, 'r')
		lines = f.readlines()
		#close file
		return lines
	except Exception as err:
   		print ("Unable to read file: ",err)


questions = readfile("question.txt")
answers = readfile("answers.txt")

print(questions)
print(answers)