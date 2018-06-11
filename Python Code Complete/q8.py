frequency = {'0': 0, '$': 0, '6': 0, '4': 0, '"': 0, '3': 0,
             '%': 0, '-': 0, '2': 0, '/': 0, '+': 0, ')': 0,
             '#': 0, '7': 0, '5': 0, '&': 0, '8': 0, ':': 0,
             '1': 0, '!': 0, '.': 0, "'": 0, ',': 0, '*': 0, '9': 0}

words = ['#+/084&"', '#3*#%#+', '8%203:', ',1$&', '!-*%',
         '.#7&33&', '#*#71%', "&-&641'2", '#))85', '9&330*']
clues = ['A#', 'M*', 'N%']



print(words[1])

print(frequency) 
for word in words:    
    for letter in word:
        frequency[letter] = frequency[letter] + 1
        
print("\n\n\n")      
print(frequency) # prints all array
print(frequency['#']) # prints just number for the #

