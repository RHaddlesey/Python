#Using instead of adding task 1 and 2 in here
words = ['#+/084&"', '#3*#%#+', '8%203:', ',1$&', '!-*%',
         '.#7&33&', '#*#71%', "&-&641'2", '#))85', '9&330*']
clues = ['A#', 'M*', 'N%']
    
#Task 3 Decode words
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


decodedWords = decodeWords(words, clues, False)
print(decodedWords)

input()
#Task 1 Read file
def readFile(filename):
	words = []	
	file = open(filename, "r")
	lines = file.readlines()	
	words.append(line.rstrip("\n"))		
	file.close()	
	return words

#Task 1 Show words in appropiate way
def showWords(words):
        for word in words:
                print("\t"+word.rstrip('\n'))
        input("Press Enter to continue")

words = readFile("words.txt")
showWords (words)         
