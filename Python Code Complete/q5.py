#Using instead of adding task 1 and 2 in here
words = ['#+/084&"', '#3*#%#+', '8%203:', ',1$&', '!-*%',
         '.#7&33&', '#*#71%', "&-&641'2", '#))85', '9&330*']
clues = ['A#', 'M*', 'N%']
    
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

clues = addNewLink(clues)
print(clues)
