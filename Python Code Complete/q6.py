#Using instead of adding task 1 and 2 in here
words = ['#+/084&"', '#3*#%#+', '8%203:', ',1$&', '!-*%',
         '.#7&33&', '#*#71%', "&-&641'2", '#))85', '9&330*']
clues = ['A#', 'M*', 'N%']
complete = ['ACQUIRED', 'ALMANAC', 'INSULT', 'JOKE',
            'HYMN', 'GAZELLE', 'AMAZON', 'EYEBROWS',
            'AFFIX', 'VELLUM']

def showMenu(): #menu to allow choice
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


    

choiceNum = "Start"; # the variable choiceNum is initialize with the value 6, this value can be anything apart from -1 to 5

while choiceNum != "0": # this loop will continue to go until the user enters a 0 on the menu screen	
    choiceNum = showMenu()
    if(choiceNum == "1"):
        showWords(words)#Task 1 Function
    elif(choiceNum == "2"):
        showCodeLinks(clues)#Task 2 Function
    elif(choiceNum == "3"):
        clues = addNewLink(clues)#Task 4 Function		
    elif(choiceNum == "4"):
        clues = removeCodeLink(clues)#Task 5 Function
    elif(choiceNum == "5"):	
        decodeWords(words,clues,True)#Task 3 Function
    elif(choiceNum == "6"):
        checkIfComplete(words,clues,complete)#Task 7 Function
    elif(choiceNum == "7"):	
        words,clues,complete,frequency = setupEnvironment(words,clues,complete,frequency)#Restart Function

    #Task 7 check to allow to finish program
    if(checkIfComplete(words,clues,complete)):        
        choiceNum = "0"
