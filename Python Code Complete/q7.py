#Using instead of adding task 1 and 2 in here
words = ['#+/084&"', '#3*#%#+', '8%203:', ',1$&', '!-*%',
         '.#7&33&', '#*#71%', "&-&641'2", '#))85', '9&330*']
clues = ['A#', 'M*', 'N%']
complete = ['ACQUIRED', 'ALMANAC', 'INSULT', 'JOKE',
            'HYMN', 'GAZELLE', 'AMAZON', 'EYEBROWS',
            'AFFIX', 'VELLUM']


def checkIfComplete(words,clues,complete): # CHANGE WITH COMPARING ARRAYS
    words = decodeWords(words, clues)# Task 3 REQUIRED    
    if(words == complete):
        print("\n\tComplete you have finished")
        return True
    else:
        print("Not Complete keep trying")
        return False
    

    

choiceNum = "Start"; # the variable choiceNum is initialize with the value 6, this value can be anything apart from -1 to 5

while choiceNum != "0": # this loop will continue to go until the user enters a 0 on the menu screen	
    choiceNum = showMenu()
    
    #Task 7 check to allow to finish program
    if(checkIfComplete(words,clues,complete)):        
        choiceNum = "0"
