questions = []
answers = []


f = open("questions.txt", 'r')
questions = f.readlines()
f.close()


f = open("answers.txt", 'r')
answers = f.readlines()
f.close()

print(questions)
print(answers)


for question in questions:
    print(question)
    answer = input()
