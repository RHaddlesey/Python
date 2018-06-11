questions = []
answers = []
score = 0

def cleanStr(str):
	str = str.rstrip('\n')
	str = str.rstrip('\r')
	return str


def readfile(filename):
	lines = []	
	try:
		f = open(filename, 'r')
		lines = f.readlines()		
		i = 0
		for line in lines :				
			lines[i] = cleanStr(line)
			i += 1		
		return lines
	except Exception as err:
   		print ("Unable to read file: ",err)



questions = readfile("question.txt")
answers = readfile("answers.txt")

i = 0
for question in questions :				
	print(question)
	answer = input()
	if(answer == answers[i]):
		print("correct")
		score += 1
	else:
		print("Nope :(")
	i += 1
print("You scored: "+str(score))