#Using instead of adding task 1 and 2 in here
words = ['#+/084&"', '#3*#%#+', '8%203:', ',1$&', '!-*%',
         '.#7&33&', '#*#71%', "&-&641'2", '#))85', '9&330*']
clues = ['A#', 'M*', 'N%']
    
def addNewLink():
        print(clues)
        letter = input("Please Enter letter")
        code = input("Please Enter Symbol")
        letter = letter.upper()
        codeTaken = False
        letterTaken = False
        for clue in clues:    
            if(clue[0] == letter):
                letterTaken = True
            if(clue[1] == codeTaken):
                codeTaken = True
        if(letterTaken | codeTaken):
            print("ERROR: Code Or Letter taken")
        else:
            clues.append(letter+code)
            print("Code Link Added")            
        input("Press Enter to continue")
        return clues

clues = addNewLink(clues)
print(clues)
