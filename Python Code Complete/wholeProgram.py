words = [] # Global array to store words read in from words.txt
clues = [] # Global array to store the inital clues.txt data and the new linking pairs of code and letter
complete = [] # Global array to store the correct answer, this is used to match up and see if the user has completed the task
frequency = {'0': 0, '$': 0, '6': 0, '4': 0, '"': 0, '3': 0,
             '%': 0, '-': 0, '2': 0, '/': 0, '+': 0, ')': 0,
             '#': 0, '7': 0, '5': 0, '&': 0, '8': 0, ':': 0,
             '1': 0, '!': 0, '.': 0, "'": 0, ',': 0, '*': 0, '9': 0}




def setupEnvironment(words,clues,complete,frequency):
    print("Setup Environment")
    words = readFile("words.txt")#Task 1 Read words.txt
    clues = readFile("clues.txt")#Task 2 Read words.txt
    complete = readFile("complete.txt")#Task 7 Read words.txt

    for clue in clues:
        frequency[clue[1]] = 0    
    return words,clues,complete,frequency


#Task 1,2,7 Read words.txt, clues.txt and solved.txt
def readFile(filename):
	words = []	
	file = open(filename, "r")
	lines = file.readlines()	
	for line in lines :		
		words.append(line.rstrip("\n"))		
	file.close()	
	return words


def decodeWords(words, clues, showOutput=False):    
    if(showOutput):
        print ("\nBelow is the oringial word and its current decode value:\n")
    counter = 0
    for word in words:
        oringialWord = word
        for clue in clues:
            letter = clue[0]
            code = clue[1]
            word = word.replace(code,letter)		

        if(showOutput):
            print(oringialWord+" => "+word)
        words[counter] = word
        counter = counter + 1    
    return words


def checkIfComplete(words,clues,complete): # CHANGE WITH COMPARING ARRAYS
    words = decodeWords(words, clues)    
    if(words == complete):
        print("\n\tComplete you have finished")
        return True
    else:
        print("Not Complete keep trying")
        return False
    


def showMenu():
	print ("1. Show Words")
	print ("2. Show Code Links")
	print ("3. Add New Code Link")

	print ("4. Remove Code Link")
	print ("5. Show Decoded Values")

	print ("6. Check Complete")

	print ("7. Restart")

	print ("0. EXIT")
	choiceNum = input("Please Choose")	

	return choiceNum



def showCodeLinks(clues):
	print("\nCurrent Code Linkings\n")		
	for clue in clues:
		print("\t"+clue[1]+" => "+clue[0])
	input("Press Enter to continue")
	

def addNewLink(clues):
        print(clues)
        letter = input("Please Enter letter")
        code = input("Please Enter Symbol")
        letter = letter.upper()
        codeTaken = False
        letterTaken = False
        for clue in clues:    
            if(clue[0] == letter):
                letterTaken = True
            if(clue[1] == code):
                codeTaken = True
        if(letterTaken | codeTaken):
            print("ERROR: Code Or Letter taken")
        else:
            clues.append(letter+code)
            print("Code Link Added")            
        input("Press Enter to continue")
        return clues



def removeCodeLink(clues):
        print("\nRemove Code Link")
        for clue in clues:
            print("\t"+clue[1]+" => "+clue[0])
        
        letter = input("Please enter letter:")        
        code = input("Pease enter code:")
        letter = letter.upper()
        print(clues)
        if letter+code in clues:
            clues.remove(letter+code)		
            print("Link Deleted!")		
        else:
            print("\n\tThe code letter pair does not exist!")
        input("Press Enter to continue")
        return clues

#Task 1 Show words in appropiate way


def calculateFrequency(words,frequency):
    for word in words:        
        for letter in word:            
            frequency[letter] = frequency[letter] + 1
    return frequency


def showWords(words):
    for word in words:
        print("\t"+word.rstrip('\n'))
    input("Press Enter to continue")



'''
This is the main program flow. When the program starts then the code under here will be the first to be run.
'''
	# This will store four function about into a array of functions. 


words,clues,complete,frequency = setupEnvironment(words,clues,complete,frequency)

frequency = calculateFrequency(words,frequency)# Task 8
choiceNum = "8"; # the variable choiceNum is initialize with the value 6, this value can be anything apart from -1 to 5

while choiceNum != "0": # this loop will continue to go until the user enters a 0 on the menu screen	
    choiceNum = showMenu()
    if(choiceNum == "1"):
        showWords(words)                    
    elif(choiceNum == "2"):        
        showCodeLinks(clues)
    elif(choiceNum == "3"):
        clues = addNewLink(clues)		
    elif(choiceNum == "4"):
        clues = removeCodeLink(clues)
    elif(choiceNum == "5"):	
        decodeWords(words,clues,True)
    elif(choiceNum == "6"):
        checkIfComplete(words,clues,complete)
    elif(choiceNum == "7"):	
        words,clues,complete,frequency = setupEnvironment(words,clues,complete,frequency)
    
    if(checkIfComplete(words,clues,complete)):        
        choiceNum = "0"
	
print("\n\tGoodbye :)") # if the user enters 0 then the program will exit
