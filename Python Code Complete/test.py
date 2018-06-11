file = open("words.txt", "r")
words = file.readlines()
file.close()

file = open("clues.txt", "r")
clues = file.readlines()
file.close()

for word in words:
    print(word)

print(words)
