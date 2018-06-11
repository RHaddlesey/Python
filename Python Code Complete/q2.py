#Task 2 Read clues.txt file
def readFile(filename):
	words = []	
	file = open(filename, "r")
	lines = file.readlines()	
	for line in lines :		
		words.append(line.rstrip("\n"))		
	file.close()	
	return words

def showCodeLinks(clues):
	print("\nCurrent Code Linkings\n")		
	for clue in clues:
		print("\t"+clue[1]+" => "+clue[0])
	input("Press Enter to continue")
	


clues = readFile("clues.txt")
showCodeLinks(clues)
