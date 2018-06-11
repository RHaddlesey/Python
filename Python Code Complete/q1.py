#Task 1 Read file
def readFile(filename):
	words = []	
	file = open(filename, "r")
	lines = file.readlines()	
	for line in lines :		
		words.append(line.rstrip("\n"))		
	file.close()	
	return words

#Task 1 Show words in appropiate way
def showWords(words):
        for word in words:
                print("\t"+word.rstrip('\n'))
        input("Press Enter to continue")

words = readFile("words.txt")
showWords(words)
